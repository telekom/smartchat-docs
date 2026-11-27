#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["httpx"]
# ///
"""Blueprint: bulk-upload a folder of files, ingest them, and tag them with a collection.

Pipeline (all through the API gateway):

    1. auth            POST   /api/v1/auth/user                        -> access_token
    2. switch space    GET    /user-manager/api/v1/spaces/switch       -> 204, then re-auth
                       (active space is a JWT claim; the gateway injects x-active-space-id
                        from the token, so a fresh token is needed after switching)
    3. upload          POST   /file-manager/api/v1/files/              -> [FileMetadata] (202)
    4. wait for OBS    GET    /file-manager/api/v1/files/{file_id}     -> status == uploaded
    5. ingestion cfg   GET    /config-manager/api/v1/space/ingestion/config?file_id=
                                                                        -> .id  (= globalConfigId)
    6. ingest          POST   /ingest-master/api/v1/task               -> Task(id, status)
    7. wait            GET    /ingest-master/api/v1/task/{id}          -> ingested / ingestion_failed

Passing `collectionId` on the ingestion task is all that is needed to put a file into a
collection. A file can sit in several collections.

The gateway is the API gateway address of your Smartchat installation. Pass it with
`--gateway` or set $SMARTCHAT_GATEWAY; the resolved target is logged on every run.

Usage:
    export SMARTCHAT_PASSWORD=...          # or you get prompted
    export SMARTCHAT_GATEWAY=https://<gateway-host>
    python upload-files-to-collection.py \
        --folder ./docs \
        --space-id <space-uuid> \
        --collection-id <collection-id> \
        --glob '**/*.pdf' \
        --dry-run

Only stdlib + httpx.
"""

from __future__ import annotations

import argparse
import getpass
import logging
import mimetypes
import os
import sys
import time
from dataclasses import dataclass
from pathlib import Path

import httpx

log = logging.getLogger("bulk-ingest")

DEFAULT_GATEWAY = os.environ.get("SMARTCHAT_GATEWAY", "")

# Gateway service keys = first path segment. A wrong segment yields 404 "Service not registered".
FILE_MANAGER = "file-manager"
INGEST_MASTER = "ingest-master"
CONFIG_MANAGER = "config-manager"
USER_MANAGER = "user-manager"

# file-manager Status enum — physical (OBS) upload status.
FM_TERMINAL_OK = {"uploaded", "exists", "duplicated"}
FM_TERMINAL_BAD = {"error", "file_too_large", "file_type_not_supported", "deleted"}

# ingest-master TaskStatus enum.
IM_DONE = {"ingested", "migrated"}
IM_FAILED = {"ingestion_failed", "hit_rate_limit", "deleted", "deletion_failed"}


@dataclass
class UploadedFile:
    file_id: str
    file_name: str
    file_uri: str
    status: str


class Spinner:
    """Single-line progress indicator for the poll loops.

    Disabled automatically when stderr isn't a TTY (CI, pipes), so log output
    stays clean. Everything goes to stderr; stdout is left for real output.
    """

    FRAMES = "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"

    def __init__(self, label: str, enabled: bool | None = None):
        self.label = label
        self.enabled = sys.stderr.isatty() if enabled is None else enabled
        self._frame = 0
        self._start = time.monotonic()

    def tick(self, note: str = "") -> None:
        if not self.enabled:
            return
        char = self.FRAMES[self._frame % len(self.FRAMES)]
        self._frame += 1
        elapsed = int(time.monotonic() - self._start)
        suffix = f" — {note}" if note else ""
        sys.stderr.write(f"\r\033[K{char} {self.label} [{elapsed // 60}:{elapsed % 60:02d}]{suffix}")
        sys.stderr.flush()

    def clear(self) -> None:
        """Wipe the line so the next log record starts clean."""
        if self.enabled:
            sys.stderr.write("\r\033[K")
            sys.stderr.flush()

    def sleep(self, seconds: float, note: str = "") -> None:
        """Sleep, animating while we wait — the poll interval is far longer than a frame."""
        if not self.enabled:
            time.sleep(seconds)
            return
        end = time.monotonic() + seconds
        while time.monotonic() < end:
            self.tick(note)
            time.sleep(min(0.12, max(0.0, end - time.monotonic())))


class SmartchatClient:
    """Thin gateway client. Auth is a bearer token; the gateway derives
    x-active-space-id / x-user-id / x-active-permissions from it — never set them yourself."""

    def __init__(self, gateway: str, username: str, password: str, timeout: float = 120.0):
        self.gateway = gateway.rstrip("/")
        self.username = username
        self._password = password
        self._http = httpx.Client(timeout=timeout, follow_redirects=True)
        self.token: str | None = None

    # --- 1/2: auth + active space -------------------------------------------------

    def authenticate(self) -> None:
        r = self._http.post(
            f"{self.gateway}/api/v1/auth/user",
            json={"username": self.username, "password": self._password},
        )
        r.raise_for_status()
        self.token = r.json()["access_token"]
        log.info("authenticated as %s", self.username)

    def switch_space(self, space_id: str) -> None:
        """Set the active space, then re-auth: the active space rides in the JWT."""
        r = self._request("GET", f"{USER_MANAGER}/api/v1/spaces/switch", params={"space_id": space_id})
        r.raise_for_status()
        self.authenticate()
        log.info("active space -> %s", space_id)

    # --- discovery: whoami + the spaces you belong to ------------------------------

    def whoami(self) -> dict:
        """POST /api/v1/auth/token/validate — your own token, no admin perms needed.

        Returns userId, username, activeSpaceId, activeRoles, activePermissions.
        """
        r = self._http.post(
            f"{self.gateway}/api/v1/auth/token/validate", json={"access_token": self.token}
        )
        self._raise(r, "validate token")
        return r.json()

    def my_spaces(self, user_id: str, *, size: int = 100) -> list[dict]:
        """GET /user-manager/api/v1/users/{user_id}/spaces -> [{id, name, isActive, ...}].

        Scoped to your own membership. (GET /spaces lists *all* spaces but needs
        app-owner-ish permissions.)
        """
        r = self._request(
            "GET", f"{USER_MANAGER}/api/v1/users/{user_id}/spaces", params={"page": 1, "size": size}
        )
        self._raise(r, "list spaces")
        return r.json().get("items", [])

    # --- plumbing -----------------------------------------------------------------

    def _request(self, method: str, path: str, **kw) -> httpx.Response:
        headers = kw.pop("headers", {}) | {"Authorization": f"Bearer {self.token}"}
        return self._http.request(method, f"{self.gateway}/{path.lstrip('/')}", headers=headers, **kw)

    @staticmethod
    def _raise(r: httpx.Response, what: str) -> None:
        if r.is_error:
            raise RuntimeError(f"{what} failed: HTTP {r.status_code} {r.text[:500]}")

    # --- 3: upload ----------------------------------------------------------------

    def upload_files(
        self,
        paths: list[Path],
        *,
        scope: str = "space",
        folder_path: str | None = None,
        overwrite: bool = False,
    ) -> list[UploadedFile]:
        """POST /file-manager/api/v1/files/ — multipart, N files per call.

        Returns 202 + [FileMetadata]. The OBS write happens in a background task, so
        `status` here is usually `pending`/`uploading`; poll with wait_for_upload().

        Semantics from the spec:
          * EXISTS     — same folder + name, *different* content (needs overwrite=true to replace)
          * DUPLICATED — same folder + name + content (no-op, already there)
        """
        files = []
        handles = []
        try:
            for p in paths:
                fh = p.open("rb")
                handles.append(fh)
                ctype = mimetypes.guess_type(p.name)[0] or "application/octet-stream"
                files.append(("files", (p.name, fh, ctype)))

            params: dict[str, object] = {"file_scope": scope, "overwrite": str(overwrite).lower()}
            if folder_path:
                params["folder_path"] = folder_path

            r = self._request("POST", f"{FILE_MANAGER}/api/v1/files/", params=params, files=files)
            self._raise(r, "upload")
        finally:
            for fh in handles:
                fh.close()

        out = []
        for meta in r.json():
            out.append(
                UploadedFile(
                    file_id=meta.get("fileId"),
                    file_name=meta["fileName"],
                    file_uri=meta["fileUri"],
                    status=meta["status"],
                )
            )
        return out

    # --- 4: wait for the OBS write ------------------------------------------------

    def wait_for_upload(
        self,
        file_id: str,
        *,
        scope: str = "space",
        timeout: float = 300,
        interval: float = 3,
        label: str = "",
    ) -> str:
        deadline = time.monotonic() + timeout
        spinner = Spinner(f"uploading {label or file_id}")
        try:
            while True:
                r = self._request("GET", f"{FILE_MANAGER}/api/v1/files/{file_id}", params={"file_scope": scope})
                self._raise(r, f"get file {file_id}")
                meta = r.json()
                status = meta["status"]
                if status in FM_TERMINAL_OK:
                    return status
                if status in FM_TERMINAL_BAD:
                    raise RuntimeError(f"upload of {meta['fileName']} ended as {status}: {meta.get('errorMessage')}")
                if time.monotonic() > deadline:
                    raise TimeoutError(f"file {file_id} stuck in {status} after {timeout}s")
                spinner.sleep(interval, status)
        finally:
            spinner.clear()

    # --- 5: ingestion config ------------------------------------------------------

    def ingestion_config_id(self, file_id: str) -> str:
        """`globalConfigId` in TaskBody is really the *ingestion config id*.
        This returns the file's config, falling back to the space default."""
        r = self._request("GET", f"{CONFIG_MANAGER}/api/v1/space/ingestion/config", params={"file_id": file_id})
        self._raise(r, "get ingestion config")
        return r.json()["id"]

    # --- 6: enqueue ingestion -----------------------------------------------------

    def create_ingestion_task(
        self,
        *,
        file_uri: str,
        file_id: str,
        file_name: str,
        ingestion_config_id: str,
        collection_id: str | None,
        scope: str = "space",
        user_id: str | None = None,
    ) -> str:
        """POST /ingest-master/api/v1/task. NOTE: no dedup — every call creates a new task."""
        body: dict[str, object] = {
            "fileUri": file_uri,
            "scope": scope,
            "globalConfigId": ingestion_config_id,
            "is_auto_sync": False,
            "isOwui": False,
            "metadata": {
                "file_id": file_id,
                "file_name": file_name,
                "file_uri": file_uri,
                "file_path": "",
                **({"user_id": user_id} if user_id else {}),
            },
        }
        if collection_id:
            body["collectionId"] = collection_id

        r = self._request("POST", f"{INGEST_MASTER}/api/v1/task", json=body)
        self._raise(r, "create ingestion task")
        return r.json()["id"]

    # --- 7: wait for ingestion ----------------------------------------------------

    def wait_for_ingestion(
        self, task_id: str, *, timeout: float = 1800, interval: float = 10, label: str = ""
    ) -> str:
        deadline = time.monotonic() + timeout
        spinner = Spinner(f"ingesting {label or task_id}")
        polls = 0
        try:
            while True:
                r = self._request("GET", f"{INGEST_MASTER}/api/v1/task/{task_id}")
                self._raise(r, f"get task {task_id}")
                task = r.json()
                status = task["status"]
                polls += 1
                if status in IM_DONE:
                    return status
                if status in IM_FAILED:
                    raise RuntimeError(f"task {task_id} -> {status}: {task.get('errorMessage')}")
                if time.monotonic() > deadline:
                    raise TimeoutError(f"task {task_id} still {status} after {timeout}s")
                spinner.sleep(interval, f"{status}, poll {polls}")
        finally:
            spinner.clear()

    def close(self) -> None:
        self._http.close()


def is_hidden(path: Path, root: Path) -> bool:
    """True if the file, or any folder it sits in below `root`, starts with a dot.

    Catches both `.DS_Store` and everything under `.git/`, `.venv/`, etc. Only the
    part below `root` is checked — a hidden *ancestor* of the folder the user pointed
    at (e.g. ~/.config/docs) is their explicit choice and does not disqualify anything.
    """
    return any(part.startswith(".") for part in path.relative_to(root).parts)


def collect_files(folder: Path, pattern: str) -> list[Path]:
    matched = sorted(p for p in folder.glob(pattern) if p.is_file())
    files = [p for p in matched if not is_hidden(p, folder)]
    skipped = len(matched) - len(files)
    if skipped:
        log.info("skipping %d hidden file(s)", skipped)
    if not files:
        raise SystemExit(
            f"no files matching {pattern!r} under {folder}"
            + (f" ({skipped} hidden file(s) skipped)" if skipped else "")
        )
    return files


def chunked(items: list, n: int):
    for i in range(0, len(items), n):
        yield items[i : i + n]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--folder", type=Path, help="folder to upload from")
    ap.add_argument(
        "--glob",
        default="**/*",
        help="glob within the folder (default: everything, recursive). Dotfiles and anything "
        "under a dot-folder are always excluded",
    )
    ap.add_argument("--space-id", help="target space (tenant) UUID — see --list-spaces")
    ap.add_argument("--collection-id", help="predefined collection / knowledge ID")
    ap.add_argument(
        "--list-spaces",
        action="store_true",
        help="print the spaces you belong to (id + name) and exit; needs no other argument",
    )
    ap.add_argument("--username", default=os.environ.get("SMARTCHAT_USERNAME", ""), help="your email")
    ap.add_argument(
        "--gateway",
        default=DEFAULT_GATEWAY,
        help="API gateway address of your Smartchat installation (default: $SMARTCHAT_GATEWAY)",
    )
    ap.add_argument("--scope", default="space", choices=["space", "private"])
    ap.add_argument("--folder-path", default=None, help="logical folder inside the space")
    ap.add_argument("--overwrite", action="store_true", help="replace files whose content changed (EXISTS)")
    ap.add_argument("--batch-size", type=int, default=10, help="files per multipart upload call")
    ap.add_argument("--ingestion-config-id", default=None, help="skip the config-manager lookup and force this id")
    ap.add_argument("--dry-run", action="store_true", help="list what would be uploaded and exit")
    ap.add_argument("-v", "--verbose", action="store_true")
    args = ap.parse_args()

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(asctime)s %(levelname)-7s %(message)s",
        datefmt="%H:%M:%S",
    )
    # httpx logs every request at INFO — one line per poll tick, which would shred the
    # spinner. Keep them behind -v.
    logging.getLogger("httpx").setLevel(logging.DEBUG if args.verbose else logging.WARNING)

    gateway = args.gateway
    if not gateway:
        ap.error("pass --gateway or set SMARTCHAT_GATEWAY to the API gateway address of your Smartchat installation")

    if args.list_spaces:
        username = args.username or input("username (email): ").strip()
        password = os.environ.get("SMARTCHAT_PASSWORD") or getpass.getpass("password: ")
        client = SmartchatClient(gateway, username, password)
        try:
            client.authenticate()
            me = client.whoami()
            print(f"\nuser {me['username']} ({me['userId']})")
            print(f"active space: {me.get('activeSpaceId')}\n")
            spaces = client.my_spaces(me["userId"])
            if not spaces:
                print("  (no space memberships returned)")
            for s in spaces:
                marker = " *" if s["id"] == me.get("activeSpaceId") else "  "
                print(f"{marker} {s['id']}  {s['name']}")
            print("\n* = currently active")
        finally:
            client.close()
        return 0

    missing = [f"--{n.replace('_', '-')}" for n in ("folder", "space_id", "collection_id") if not getattr(args, n)]
    if missing:
        ap.error(f"missing required argument(s): {', '.join(missing)}")

    paths = collect_files(args.folder, args.glob)
    log.info("gateway %s | space %s | collection %s", gateway, args.space_id, args.collection_id)
    log.info("%d file(s) matched under %s", len(paths), args.folder)
    if args.dry_run:
        for p in paths:
            print(f"  {p}  ({p.stat().st_size:,} bytes)")
        return 0

    username = args.username or input("username (email): ").strip()
    password = os.environ.get("SMARTCHAT_PASSWORD") or getpass.getpass("password: ")

    client = SmartchatClient(gateway, username, password)
    failures: list[tuple[str, str]] = []
    succeeded = 0
    uploaded: list[UploadedFile] = []
    try:
        client.authenticate()
        client.switch_space(args.space_id)

        # 3/4 — upload in batches, then wait for each OBS write.
        for batch in chunked(paths, args.batch_size):
            log.info("uploading %d file(s): %s", len(batch), ", ".join(p.name for p in batch))
            for uf in client.upload_files(
                batch, scope=args.scope, folder_path=args.folder_path, overwrite=args.overwrite
            ):
                if uf.status == "duplicated":
                    log.info("  %s: DUPLICATED (identical file already in the space) — skipping", uf.file_name)
                    continue
                if uf.status == "exists" and not args.overwrite:
                    log.warning("  %s: EXISTS with different content — rerun with --overwrite", uf.file_name)
                    failures.append((uf.file_name, "exists, not overwritten"))
                    continue
                if not uf.file_id:
                    log.error("  %s: no fileId returned (%s)", uf.file_name, uf.status)
                    failures.append((uf.file_name, f"no fileId ({uf.status})"))
                    continue
                uploaded.append(uf)

        # 5/6/7/8 — per file: resolve config, enqueue, wait, tag.
        for uf in uploaded:
            try:
                status = client.wait_for_upload(uf.file_id, scope=args.scope, label=uf.file_name)
                log.info("%s: OBS %s (%s)", uf.file_name, status, uf.file_uri)

                cfg_id = args.ingestion_config_id or client.ingestion_config_id(uf.file_id)

                task_id = client.create_ingestion_task(
                    file_uri=uf.file_uri,
                    file_id=uf.file_id,
                    file_name=uf.file_name,
                    ingestion_config_id=cfg_id,
                    collection_id=args.collection_id,
                    scope=args.scope,
                )
                log.info("%s: task %s queued", uf.file_name, task_id)

                client.wait_for_ingestion(task_id, label=uf.file_name)
                log.info("%s: ingested into collection %s", uf.file_name, args.collection_id)
                succeeded += 1
            except Exception as exc:  # keep going; report at the end
                log.error("%s: %s", uf.file_name, exc)
                failures.append((uf.file_name, str(exc)))
    finally:
        client.close()

    log.info("done: %d ok, %d failed, %d/%d files reached ingestion",
             succeeded, len(failures), len(uploaded), len(paths))
    for name, why in failures:
        log.error("  FAILED %s — %s", name, why)
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
