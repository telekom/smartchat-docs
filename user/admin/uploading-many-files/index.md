# Uploading Many Files at Once to a Collection via API

Source: https://docs.smartchat.ai.t-systems.net/user/admin/uploading-many-files/

> How to add a whole folder of files to a space and put them in a collection, without uploading them one by one.

Uploading files in **Workspace → Collection** works well for a few documents at a time. If you need to add dozens or hundreds — when you are setting up a new space, moving content over from somewhere else, or loading an archive — this guide shows you how to add a whole folder at once and put every file into the collection you choose.

You do this by running a small script from your computer. You do not need to be a developer, but you will be working in a terminal.

> **Is there a better fit?**
>
> If the files change regularly and you want Smartchat to keep up with them automatically, set up a connection instead of doing a one-off load: [S3 AutoSync](https://docs.smartchat.ai.t-systems.net/user/admin/s3-autosync/) watches a storage bucket, and [Confluence Sync](https://docs.smartchat.ai.t-systems.net/user/admin/confluence-sync/) watches a Confluence space. Use this guide when you have a fixed set of files to add once.

## [Before you start](https://docs.smartchat.ai.t-systems.net/user/admin/uploading-many-files/#before-you-start)

You will need:

- A Smartchat account that is allowed to add files to the target space
- The **space ID** of the space you are adding to — the script can look this up for you
- The **collection ID** of the collection the files should go into
- The folder of files, on your computer
- Python, set up as described below

## [Set up Python](https://docs.smartchat.ai.t-systems.net/user/admin/uploading-many-files/#set-up-python)

The script needs **Python 3.10 or newer** and one extra package called `httpx`.

Check which version you have by running this in a terminal:

```bash
python3 --version
```

You will get something like `Python 3.12.5`. The number in the middle is what matters: it must be **10 or higher**.

> **Not sure how to install or upgrade Python?**
>
> We recommend using **uv**, a tool that handles Python versions and packages for you. It downloads the right Python automatically, so you do not have to install or upgrade anything by hand, and it will not interfere with any Python you already have.
>
> Install it by following the [uv installation instructions](https://docs.astral.sh/uv/getting-started/installation/) — one command on macOS, Linux, or Windows.

Every command below is shown two ways. Use the **uv** tab unless you already have a working Python setup you prefer.

## [Get the script](https://docs.smartchat.ai.t-systems.net/user/admin/uploading-many-files/#get-the-script)

Download it here: [`upload-files-to-collection.py`](https://docs.smartchat.ai.t-systems.net/scripts/upload-files-to-collection.py)

Save it somewhere you can find it, then open a terminal in that folder.

**uv (recommended)**

Nothing else to set up. `uv` reads the requirements from the script itself and takes care of the rest the first time you run it.

**Python only**

Create a throwaway environment next to the script and install `httpx` into it. This keeps the package out of your main Python installation.

```bash
python3 -m venv .venv
```

Then activate it:

```bash
source .venv/bin/activate          # macOS and Linux
.venv\Scripts\activate             # Windows
```

Your prompt now starts with `(.venv)`. Install the package:

```bash
pip install httpx
```

Keep this terminal open — the environment stays active until you close it or run `deactivate`. If you come back later, activate it again before running the script. When you are finished for good, delete the `.venv` folder.

## [Point the script at your Smartchat](https://docs.smartchat.ai.t-systems.net/user/admin/uploading-many-files/#point-the-script-at-your-smartchat)

The script needs the address of your installation’s API gateway. If you do not know it, ask your Smartchat contact. Set it once in the terminal you are working in:

```bash
export SMARTCHAT_GATEWAY=https://<gateway-host>     # macOS and Linux
set SMARTCHAT_GATEWAY=https://<gateway-host>        # Windows
```

You can also pass it to every command as `--gateway https://<gateway-host>`.

## [Step 1 — Find your space ID](https://docs.smartchat.ai.t-systems.net/user/admin/uploading-many-files/#step-1--find-your-space-id)

**uv (recommended)**

```bash
uv run upload-files-to-collection.py --list-spaces
```

**Python only**

```bash
python upload-files-to-collection.py --list-spaces
```

It asks for your Smartchat email and password, then prints every space you are a member of, with its ID and name. The space you are currently working in is marked with a `*`.

Copy the ID of the space you want to add files to.

> **Note**
>
> If a space you expect is missing, you are not a member of it. Ask a space owner to add you.

## [Step 2 — Find your collection ID](https://docs.smartchat.ai.t-systems.net/user/admin/uploading-many-files/#step-2--find-your-collection-id)

In Smartchat, open **Workspace → Collection** and open the collection you want to add the files to. Use the **Copy ID** button in the top right of the page.

*\[Image: The Copy ID button in the top right of the collection page]*

That copies the collection ID to your clipboard.

## [Step 3 — Check what will be uploaded](https://docs.smartchat.ai.t-systems.net/user/admin/uploading-many-files/#step-3--check-what-will-be-uploaded)

Before uploading anything, do a practice run. Add `--dry-run` and the script lists the files it would send, then stops without contacting Smartchat:

**uv (recommended)**

```bash
uv run upload-files-to-collection.py \
  --folder ./my-documents \
  --space-id <your-space-id> \
  --collection-id <your-collection-id> \
  --dry-run
```

**Python only**

```bash
python upload-files-to-collection.py \
  --folder ./my-documents \
  --space-id <your-space-id> \
  --collection-id <your-collection-id> \
  --dry-run
```

Read the list carefully. By default the script picks up **everything** in the folder, including files in subfolders. To narrow it down, add a pattern:

```bash
--glob '**/*.pdf'      # only PDFs, including those in subfolders
--glob '*.pdf'         # only PDFs sitting directly in the folder
--glob '*'             # everything in the folder, but not subfolders
```

Keep the quotes around the pattern.

Hidden files are always left out, whatever pattern you use. That means anything whose name starts with a dot, such as `.DS_Store`, and everything inside hidden folders like `.git`. The script tells you how many it skipped so you can see it happened.

## [Step 4 — Upload](https://docs.smartchat.ai.t-systems.net/user/admin/uploading-many-files/#step-4--upload)

> **Do not use Smartchat while the script is running**
>
> Leave the Smartchat interface alone from the moment you start the upload until the script prints its summary. **Above all, do not switch to a different space.**
>
> The script works inside whichever space is active for your account. Switching spaces in the browser changes that for your whole account, including the script — files can end up in the wrong space, and there is no automatic way to move them back. Uploading, deleting, or editing files in the UI at the same time can also make the script report failures for files that are actually fine.
>
> If you need to keep using Smartchat, wait for the run to finish, or use a different account for the upload.

When the list looks right, remove `--dry-run` and run it again:

**uv (recommended)**

```bash
uv run upload-files-to-collection.py \
  --folder ./my-documents \
  --space-id <your-space-id> \
  --collection-id <your-collection-id>
```

**Python only**

```bash
python upload-files-to-collection.py \
  --folder ./my-documents \
  --space-id <your-space-id> \
  --collection-id <your-collection-id>
```

The script asks for your password, then works through the files. For each one it shows a spinner with how long it has been waiting, because processing a file takes anything from a few seconds to several minutes depending on its size.

When it finishes it prints a summary: how many files succeeded, how many failed, and why each failure happened. Leave the terminal window open until it is done.

> **Caution**
>
> The first line of every run tells you which Smartchat environment, space, and collection you are about to write to. Check it. There is nothing that asks you to confirm before files start uploading, and files that are already in a space are not automatically replaced.

## [What happens to each file](https://docs.smartchat.ai.t-systems.net/user/admin/uploading-many-files/#what-happens-to-each-file)

The script does the same three things you would do by hand in the UI, once per file:

1. **Uploads** the file to the space’s storage.
2. **Waits** until the upload has finished storing.
3. **Asks Smartchat to process it** — this is the step that reads the text, splits it into small searchable pieces, and adds it to your collection.

You do not need to do anything afterwards. Putting a file in a collection is part of the processing request, so there is no separate step to add the files to your collection once they are uploaded.

## [Check that it worked](https://docs.smartchat.ai.t-systems.net/user/admin/uploading-many-files/#check-that-it-worked)

Open the collection in **Workspace → Collection** and refresh the page. Your files should be listed there.

If they are not all showing yet, wait a moment and refresh again — files are added to the collection by a background job, so there is often a short delay between the script finishing and everything appearing.

## [Why a file might be skipped](https://docs.smartchat.ai.t-systems.net/user/admin/uploading-many-files/#why-a-file-might-be-skipped)

Smartchat avoids storing the same document twice, so some files are deliberately not uploaded. This is the most common reason a run looks like it did nothing:

| What the script reports | What it means | What to do |
| - | - | - |
| `DUPLICATED` | A file with the same name **and** the same contents is already in that folder of the space | Nothing — it is already there |
| `EXISTS` | A file with the same name is already there, but its contents differ | Add `--overwrite` to replace it |
| Nothing appears to happen | The file was uploaded before and already processed | Its contents need to differ from the existing copy |

If you are testing and want a file to go through every time, change **both** its name and its contents.

## [If something goes wrong](https://docs.smartchat.ai.t-systems.net/user/admin/uploading-many-files/#if-something-goes-wrong)

The script keeps going when one file fails and reports the failures at the end, so a single bad file does not stop the rest.

If a file never shows up, open the collection in **Workspace → Collection**: every file appears there with its current status. [Ingestion Errors](https://docs.smartchat.ai.t-systems.net/user/files/ingestion-errors/) explains what each status means and what causes it. Very large files have their own rules, described in [File Size Limits](https://docs.smartchat.ai.t-systems.net/user/files/file-size-limits/).

Some things worth knowing:

- **Files from subfolders lose their folder.** Only the file name is sent, so `reports/summary.pdf` and `archive/summary.pdf` end up as two files with the same name, and the second is treated as a duplicate or a conflict. Upload such folders one at a time using `--folder-path` to keep them apart.
- **Re-running the script is not free.** Asking Smartchat to process a file again always creates new work, even when the file itself is skipped. Avoid re-running a large batch just to catch a few failures — point the script at a folder holding only the files that failed.
- **Interrupting the script is safe.** Files already uploaded stay uploaded and finish processing on their own. Nothing is left half-written.

## [All options](https://docs.smartchat.ai.t-systems.net/user/admin/uploading-many-files/#all-options)

| Option | Default | What it does |
| - | - | - |
| `--folder` | — | The folder to upload from (required) |
| `--space-id` | — | The space to upload into (required) |
| `--collection-id` | — | The collection the files go into (required) |
| `--glob` | everything | Which files to pick, as a pattern. Hidden files are always skipped |
| `--dry-run` | — | List the files and stop, without uploading |
| `--list-spaces` | — | Show your spaces and their IDs, then stop |
| `--overwrite` | off | Replace files that already exist with different contents |
| `--folder-path` | — | Put the files in a named folder inside the space |
| `--gateway` | `SMARTCHAT_GATEWAY` | The API gateway address of your Smartchat installation (required unless the environment variable is set) |
| `--scope` | `space` | `space` (shared) or `private` (only you) |
| `--batch-size` | `10` | How many files to send per upload request |
| `--ingestion-config-id` | — | Use one specific processing configuration for all files |
| `-v` | — | Show detailed output, useful when reporting a problem |

You can set your password as the `SMARTCHAT_PASSWORD` environment variable to avoid being asked each run. Anything stored that way is visible to other programs on your machine, so prefer typing it when prompted.

## [For developers](https://docs.smartchat.ai.t-systems.net/user/admin/uploading-many-files/#for-developers)

The script is a worked example of the file-loading API and is meant to be adapted. It uses only the Python standard library plus `httpx`, declared as [inline script metadata](https://packaging.python.org/en/latest/specifications/inline-script-metadata/) so `uv run` resolves it without a project. Each step is a separate method with the endpoint documented above it.

The calls it makes, in order:

| Step | Call |
| - | - |
| Sign in | `POST /api/v1/auth/user` |
| Set the active space | `GET /user-manager/api/v1/spaces/switch?space_id=` then sign in again |
| Upload | `POST /file-manager/api/v1/files/?file_scope=space` |
| Wait for storage | `GET /file-manager/api/v1/files/{file_id}` until `status` is `uploaded` |
| Look up the processing config | `GET /config-manager/api/v1/space/ingestion/config?file_id=` |
| Request processing | `POST /ingest-master/api/v1/task` with `collectionId` |
| Wait | `GET /ingest-master/api/v1/task/{id}` until `status` is `ingested` |

Three things that are easy to get wrong:

- **Sign in again after switching space.** The active space is carried inside the access token, so a token issued before the switch still points at the old space. The gateway fills in the `x-active-space-id`, `x-user-id` and `x-active-permissions` headers from your token — never set them yourself. This is also why switching spaces in the browser mid-run is dangerous.
- **The first part of the path is a gateway service key, not a repository name.** `file-manager` routes to aifs-files-management. A wrong key returns `404 Service not registered`, which looks like an empty result but is a wrong URL.
- **`collectionId` on the processing request is all you need.** It puts the file in the collection both for search and in the chat interface. `PUT /ingest-master/api/v1/files` exists to repair files that were processed *without* a collection; it is not part of adding new files.

The full API definitions are published per service, and are the authoritative reference:

```plaintext
https://<gateway-host>/file-manager/api/v1/openapi.json
https://<gateway-host>/ingest-master/api/v1/openapi.json
https://<gateway-host>/config-manager/api/v1/openapi.json
https://<gateway-host>/user-manager/api/v1/openapi.json
```

The browsable versions at `/file-manager/redoc` load their content from those same files.
