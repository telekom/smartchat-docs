# Ingestion Errors

Source: https://docs.smartchat.ai.t-systems.net/user/files/ingestion-errors/

> What the ingestion statuses of a file mean, why a file fails to ingest, and what you can do about each cause.

When you add a file to a space, either by uploading it manually or automatically through [S3 AutoSync](https://docs.smartchat.ai.t-systems.net/user/admin/s3-autosync/) or [Confluence Sync](https://docs.smartchat.ai.t-systems.net/user/admin/confluence-sync/), Smartchat extracts its text, splits it into chunks, and indexes them so they can be found during chats. Each file moves through the same lifecycle, and its collection in **Workspace → Collection** shows the current status.

Most files ingest without a hitch. When one doesn’t, the status and error message tell you why. This page explains the statuses, the common causes of failure, and what you can do about each.

## [Ingestion statuses](https://docs.smartchat.ai.t-systems.net/user/files/ingestion-errors/#ingestion-statuses)

| Status | Meaning |
| - | - |
| **pending** | The file is queued or currently being processed. This is normal and temporary. |
| **ingested** | The file was processed successfully and is searchable in the space. |
| **ingestion\_failed** | Processing was attempted (and automatically retried) but did not succeed. The file is **not** available in the space. Check the error message for details about what went wrong. |
| **migrated** | The file exceeded the time limit on the standard processing queue and has been moved to the [large-file queue](https://docs.smartchat.ai.t-systems.net/user/files/file-size-limits/#large-files-take-longer-to-process) for reprocessing. This is a temporary state; the file will eventually finish as `ingested` or `ingestion_failed`. |
| **hit\_rate\_limit** | Processing is paused because the embedding service is temporarily rate-limited. You don’t have to do anything; the file will be retried in the next available time window. This is a temporary state. |

> **Note**
>
> Transient problems are retried automatically a few times before a file is marked `ingestion_failed`, so a failed status means the error persisted across retries; it is not a one-off blip.

## [Why a file fails](https://docs.smartchat.ai.t-systems.net/user/files/ingestion-errors/#why-a-file-fails)

Almost every `ingestion_failed` file falls into one of the categories below. When a file fails, the collection shows a detailed error message next to the status. The headings below match those error messages so you can look yours up directly.

### [No nodes were generated for this document.](https://docs.smartchat.ai.t-systems.net/user/files/ingestion-errors/#no-nodes-were-generated-for-this-document)

The most common cause. Smartchat indexes **text**; if it extracts nothing from a document, there is nothing to index and ingestion fails.

This typically happens with:

- **Scanned PDFs**: pages that are photographs or scans of paper, with no underlying text layer.
- **Image-only documents**: a PDF whose pages are entirely images (diagrams, screenshots, a word cloud / “Wortwolke”, a poster).
- Files where the real content lives only in images that the extractor cannot read as text.

**What you can do:**

- Provide a **text-based version** of the document instead of a scan.
- Run **OCR** (optical character recognition) on the file first so it gains a text layer, then re-upload it.
- If only part of the document is image-only, a version with a proper text layer will ingest the readable parts.

### [Error occurred while reading the file.](https://docs.smartchat.ai.t-systems.net/user/files/ingestion-errors/#error-occurred-while-reading-the-file)

The file cannot be parsed because it is broken, truncated, or was written by a tool that does not follow the file-format specification. For PDFs this shows up as read errors deep in the parser (for example, a broken internal image stream, or a malformed page-numbering table).

**What you can do:**

- **Re-export or repair the file.** Open it in a viewer and use *Print to PDF* / *Save as PDF*, or re-export it from the original source, then upload the fresh copy. This regenerates a clean file and resolves most parser errors.
- Confirm the file opens correctly in a normal viewer; if it is visibly broken there, it needs to be regenerated at the source.

### [File extension is not supported](https://docs.smartchat.ai.t-systems.net/user/files/ingestion-errors/#file-extension-is-not-supported)

The file’s extension is not on the list of supported formats. Smartchat processes common document and text formats; other types (executables, archives, raw media files, etc.) are rejected during ingestion.

**What you can do:** convert the content to a supported format (PDF, DOCX, TXT, or another format listed in your deployment’s documentation) and upload it again.

### [Task size exceeds the allowed limit.](https://docs.smartchat.ai.t-systems.net/user/files/ingestion-errors/#task-size-exceeds-the-allowed-limit)

The file produces more chunks than the per-file limit allows. See [File Size Limits](https://docs.smartchat.ai.t-systems.net/user/files/file-size-limits/) for the exact limits.

**What you can do:** split the document into smaller files, or remove content that does not need to be searchable.

### [OpenAI rate limit exceeded.](https://docs.smartchat.ai.t-systems.net/user/files/ingestion-errors/#openai-rate-limit-exceeded)

The embedding service enforces a tokens-per-minute (TPM) limit. During ingestion the worker splits text into batches and halves the batch size on each rate-limit retry. When the batch is down to a single chunk and still exceeds the TPM budget, no further splitting is possible and the file fails permanently.

**What you can do:** ask your platform operators to either reduce the configured chunk size or increase the TPM rate limit on the API key used for embedding.

### [Task hit soft time limit even after migrating to large queue.](https://docs.smartchat.ai.t-systems.net/user/files/ingestion-errors/#task-hit-soft-time-limit-even-after-migrating-to-large-queue)

The file took too long to process and timed out on both the standard and the large-file processing queue. **Retrying will not help**; the file will still exceed the maximum allowed processing time.

**What you can do:** split the document into smaller files, or remove content that does not need to be searchable. See [File Size Limits](https://docs.smartchat.ai.t-systems.net/user/files/file-size-limits/) for guidance.

### [File was not found.](https://docs.smartchat.ai.t-systems.net/user/files/ingestion-errors/#file-was-not-found)

The file reference exists but the actual file is missing from storage. There are two cases:

- **Synced content** ([S3 AutoSync](https://docs.smartchat.ai.t-systems.net/user/admin/s3-autosync/), [Confluence Sync](https://docs.smartchat.ai.t-systems.net/user/admin/confluence-sync/), or other data connections): the file was removed from the source after ingestion was already queued. This is correct behavior; there is nothing to do. If you still need the file, add it back to the source.
- **Manual uploads**: this should not happen and indicates an error. Delete the file from the space and upload it again.

### [Transient or infrastructure errors](https://docs.smartchat.ai.t-systems.net/user/files/ingestion-errors/#transient-or-infrastructure-errors)

Occasionally a file fails because of a temporary condition: an API timeout, a storage hiccup, or a processing component being briefly unavailable. These are retried automatically, and most recover on their own. If a file fails and you believe the file itself is fine, re-trigger ingestion a little later. If it keeps failing, raise it with your platform operators.

The following error messages fall into this category:

- `OpenAI API error occurred.`: a temporary error from the embedding service.
- `Cannot connect to Postgres Database.`: the database was briefly unreachable.
- `Cannot connect to S3 file system.`: object storage was briefly unreachable.
- `Pipeline could not be built.`: the processing pipeline failed to initialize; this is typically an infrastructure issue.

## [Files stuck as “pending”](https://docs.smartchat.ai.t-systems.net/user/files/ingestion-errors/#files-stuck-as-pending)

`pending` is a normal, temporary state, but a file that stays pending for a long time with no progress is worth a look. This is **not** the same as a failure: the file has not errored, it simply has not finished (or started) processing.

Common reasons:

- **Large files take longer.** Big documents are processed on a [separate queue](https://docs.smartchat.ai.t-systems.net/user/files/file-size-limits/#large-files-take-longer-to-process) and finish later by design. A large file sitting in `pending` for a while is expected. You may see the status change to `migrated` while the file moves to the large-file queue; it will resolve to `ingested` or `ingestion_failed` once processing completes.
- **Queue backlog.** During a large bulk import, files wait their turn behind everything already queued.
- **The job was never picked up.** More rarely, a file is never scheduled for processing, for example because of an ingestion-service disruption. In this case the file shows no processing activity at all.

**What you can do:** give large files and big batches time to work through the queue. In very busy systems, especially in the large-file queue, this can take hours up to days. Retrying earlier just increases the queue pressure and does not help.

Only retry a file if the queue is empty (i.e. new files get processed instantly) but the file you want is still stuck in `pending`. This indicates the task was permanently lost and the pending state is stuck. If it still does not move after retrying, raise it with your Application Owner or platform operators.

## [Getting more detail](https://docs.smartchat.ai.t-systems.net/user/files/ingestion-errors/#getting-more-detail)

For deeper investigation, the ingestion service also records the full error (including the file, the internal task, and the underlying exception) in its logs. If you need more context than the error message provides, ask your platform operators to check the ingestion worker logs for that file.
