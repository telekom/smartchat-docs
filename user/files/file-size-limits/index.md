# File Size Limits

Source: https://docs.smartchat.ai.t-systems.net/user/files/file-size-limits/

> How large a file may be to reach a Smartchat space and be indexed, covering the file size limit, the PDF page limit, the limit on how much text a file may contain, why the limits exist, and how very large files are handled.

When you add a file to a space, either by uploading it or automatically through [S3 AutoSync](https://docs.smartchat.ai.t-systems.net/user/admin/s3-autosync/) or Confluence Sync, Smartchat splits the file into small chunks and indexes them so they can be found during chats. Very large files produce a huge number of chunks, which is slow to process and memory-intensive. To keep ingestion reliable for everyone, a single file can only be so large.

## [The limits](https://docs.smartchat.ai.t-systems.net/user/files/file-size-limits/#the-limits)

Size is limited in a few ways: how many megabytes the file has, how many pages a PDF has, and how much text it contains.

| Limit | Applies to | Maximum |
| - | - | - |
| **File size** | Files you upload in Smartchat | **100 MB** |
| **File size** | Files added through the eRAG API | **200 MB** |
| **Pages** | PDF files | **500 pages** |
| **Text volume** | Every file (including PDFs) | roughly **2,000 chunks** (very roughly **2 million tokens**, or a few thousand pages of plain text) |

A **chunk** is a slice of the document of about 1,000 tokens (a token is roughly ¾ of a word). The exact chunk size depends on your space’s configuration, so the equivalent word or page count varies.

A file needs to stay within every limit that applies to it — a PDF, for example, within the file size, page and text volume limits alike.

The limits take effect at different points: a file above the file size limit is refused when you upload it and never reaches the space, while a file that is too long is uploaded but **not ingested**, so it cannot be used in chats.

> **Note**
>
> Files up to 100 MB can be uploaded in Smartchat directly, in **Workspace → Collection**. Larger files, up to 200 MB, can only be added through the eRAG API, see [Uploading Many Files at Once](https://docs.smartchat.ai.t-systems.net/user/admin/uploading-many-files/).

## [Why there is a hard limit](https://docs.smartchat.ai.t-systems.net/user/files/file-size-limits/#why-there-is-a-hard-limit)

The text volume limit is a deliberate safety cutoff. The servers that process ingestion have a finite amount of memory, and an arbitrarily large file could consume all of it and destabilise processing for other files and spaces. Because processing has to stay within that memory, a file has to be rejected at *some* size to keep the system stable, so the exact cutoff is, frankly, somewhat arbitrary. It is set well above what real documents need: the large majority of files (well over 99%) are far smaller than the limit and are never affected.

## [Large files take longer to process](https://docs.smartchat.ai.t-systems.net/user/files/file-size-limits/#large-files-take-longer-to-process)

A large file simply takes longer to ingest, because there is more content to split and index. That slowness comes from the size of the file itself, not from how Smartchat handles it.

To keep these long-running jobs from holding up smaller files, Smartchat processes large files (roughly above 100 pages, or around 400 chunks) on a **separate queue**. That queue is not slower or less powerful; it has the same resources as the main one. It simply keeps large files out of the way so quick files are not stuck behind them, and it allows a job the longer time it needs to finish. You do not need to do anything; large files just finish later.

Files brought in automatically by [S3 AutoSync](https://docs.smartchat.ai.t-systems.net/user/admin/s3-autosync/) always use this separate queue, so large synced files never hold up other ingestion. The size limits above are exactly the same for synced files as for uploaded ones.

## [If a file is too large](https://docs.smartchat.ai.t-systems.net/user/files/file-size-limits/#if-a-file-is-too-large)

- **Split it into smaller files.** For example, break a large PDF into page ranges, or a long document into per-section files. Each part is ingested separately.
- **Remove content that does not need to be searchable** (for example, large image-only appendices) before ingesting.
