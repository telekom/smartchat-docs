# Supported File Types

Source: https://docs.smartchat.ai.t-systems.net/user/files/supported-file-types/

> The file formats Smartchat can extract and index, grouped by category.

Smartchat extracts the content of a file with a parser built for its format, then indexes it with an embedding model so it can be found during chats. Only formats with a parser can be ingested — this page lists them.

The same list applies everywhere a file enters a Space: manual upload, [S3 AutoSync](https://docs.smartchat.ai.t-systems.net/user/admin/s3-autosync/), and [Confluence Sync](https://docs.smartchat.ai.t-systems.net/user/admin/confluence-sync/).

## [Formats](https://docs.smartchat.ai.t-systems.net/user/files/supported-file-types/#formats)

| Category | File types |
| - | - |
| Text documents | `pdf`, `doc`, `docx`, `rtf`, `epub` |
| Presentations | `ppt`, `pptx` |
| Spreadsheets | `xls`, `xlsx`, `csv` |
| Text and markup | `txt`, `md`, `html`, `xml`, `json` |
| Email | `msg`, `mbox` |
| Source code | `py`, `pyw`, `pyi`, `js`, `mjs`, `cjs`, `jsx`, `ts`, `tsx`, `mts`, `go`, `rs`, `java`, `c`, `h`, `cpp`, `hpp`, `cc`, `cs`, `rb`, `php`, `swift`, `kt`, `scala`, `sh`, `bash`, `sql` |
| Audio | `mp3` |

Audio files are transcribed to text before indexing.

> **Note**
>
> The list changes over time. Formats are added as parsers become available, and rarely used ones may be removed.

## [If a format is not listed](https://docs.smartchat.ai.t-systems.net/user/files/supported-file-types/#if-a-format-is-not-listed)

Convert the file to a supported format before uploading it — for example, export to PDF or DOCX. If ingestion fails for a file whose format *is* listed, see [Ingestion Errors](https://docs.smartchat.ai.t-systems.net/user/files/ingestion-errors/).

## [See also](https://docs.smartchat.ai.t-systems.net/user/files/supported-file-types/#see-also)

- [File Size Limits](https://docs.smartchat.ai.t-systems.net/user/files/file-size-limits/) — file size, page and text volume cutoffs
