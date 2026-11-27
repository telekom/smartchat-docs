# S3 AutoSync

Source: https://docs.smartchat.ai.t-systems.net/user/admin/s3-autosync/

> Automatically sync files from an S3 (OTC OBS) bucket into your Smartchat Space.

S3 AutoSync ingests files from an S3-compatible bucket (OTC Object Storage, OBS) into your Smartchat Space on a schedule. New, changed and removed files in the bucket are picked up and become searchable context for every member of the Space.

## [Prerequisites](https://docs.smartchat.ai.t-systems.net/user/admin/s3-autosync/#prerequisites)

- You need the **Space Owner** role in the Smartchat Space. See [Roles](https://docs.smartchat.ai.t-systems.net/user/concepts/roles/) for details.
- An S3 bucket, its endpoint URL and an access key pair with read access to it. Files are uploaded to the bucket with your own tooling (for example `boto3`, the OBS Browser or the Huawei SDK).
- S3 AutoSync must be enabled for your Smartchat environment. If the **S3 AutoSync** page is missing, ask your Application Owner.

> **Uploading with boto3: disable integrity signing**
>
> OTC OBS does not support the S3 request-checksum / integrity signing that recent `boto3` versions (`> 1.36`) enable by default. Uploading with it enabled **corrupts the stored files**: they lose metadata and can no longer be ingested.
>
> When uploading to the bucket with `boto3`, disable it by setting both `request_checksum_calculation` and `response_checksum_validation` to `when_required` on the client config:
>
> ```python
> from botocore.config import Config
>
>
> s3 = boto3.client(
>     "s3",
>     config=Config(
>         request_checksum_calculation="when_required",
>         response_checksum_validation="when_required",
>     ),
> )
> ```
>
> Alternatively, upload via the OBS Browser or the Huawei SDK.

## [Step 1 — Open S3 AutoSync](https://docs.smartchat.ai.t-systems.net/user/admin/s3-autosync/#step-1--open-s3-autosync)

Click your profile image, choose **Administration**, and pick the Space in **Selected Space** under **Space Owner**. Then open **S3 AutoSync**. The table lists the S3 connections of this Space and refreshes itself every minute.

*\[Image: S3 AutoSync page with one active connection]*

## [Step 2 — Add a connection](https://docs.smartchat.ai.t-systems.net/user/admin/s3-autosync/#step-2--add-a-connection)

Click **Add S3 connection** and fill in the form:

*\[Image: Add S3 connection form with folder rules]*

**Source**

| Field | Description |
| - | - |
| **Name** | A name for the connection, shown in the table. |
| **Endpoint URL** | The S3 endpoint, e.g. `https://obs.eu-de.otc.t-systems.com`. |
| **Bucket name** | The bucket to watch: lowercase letters, digits, dots and hyphens. |
| **Region** | The bucket’s region, `eu-de` for OTC. |

**Credentials**

| Field | Description |
| - | - |
| **Access key ID** / **Secret access key** | A key pair with read access to the bucket. The values are stored encrypted and never shown again; leave both blank when editing to keep them. |

**Synchronization**

| Field | Description |
| - | - |
| **Sync interval** | How often the bucket is checked: **Every 15 minutes**, **Every hour** (default), **Every 6 hours**, **Every 12 hours**, **Daily** or **Weekly**. |
| **Ingest pipeline** | Only shown when the Space has more than one ingestion configuration. Choose which one processes the synced files. |
| **Target collection** | Where files land that no folder rule covers. **General collection** is the Space’s default collection. Changing it later **moves** already synced files on the next sync. |
| **Folder rules** | Route folders of the bucket into other collections, see [Folder rules](https://docs.smartchat.ai.t-systems.net/user/admin/s3-autosync/#folder-rules). |
| **Active** | Leave on. Paused connections keep their settings, but the bucket is not checked. |

The collection does not have to exist yet: **New collection…** in the **Target collection** picker, or in a folder rule’s picker, opens a dialog for its name and an optional description, creates it right away and selects it. The collection stays in the Workspace even if you do not save the connection.

A collection can be created right from the form. It stays even if you do not save the connection.

Click **Save**. Smartchat checks the bucket with the given credentials right away:

- On **create**, an unreachable bucket is rejected. Nothing is stored until endpoint, bucket and keys are correct.
- On **edit**, the connection is saved either way; if the bucket is not reachable the sync is paused (toast **Connection saved, but the bucket is not reachable. The sync stays paused until the settings are fixed.**).

The first run starts with the next interval. Files already in the bucket are ingested on that run; from then on only additions, changes and deletions are processed.

## [Folder rules](https://docs.smartchat.ai.t-systems.net/user/admin/s3-autosync/#folder-rules)

By default every file of the bucket lands in the **Target collection** of the connection. If you funnel several data sources into one bucket, you can instead route each folder into its own collection with **folder rules**.

In the form, click **Add folder rule** and enter the folder path inside the bucket (e.g. `reports/2026`) and the **Target collection** for it. Add one row per folder; a folder may appear only once.

### [How folders are matched](https://docs.smartchat.ai.t-systems.net/user/admin/s3-autosync/#how-folders-are-matched)

- A rule applies to every object **inside** the folder, at any depth. `reports/2026` matches `reports/2026/q1.pdf` and `reports/2026/archive/old.pdf`.
- Matching stops at folder boundaries: `reports/2026` does **not** match `reports/2026-old/x.pdf`, and a rule `reports` does not match `reportsarchive/x.pdf`.
- If there is a rule for a folder and another rule for one of its subfolders, the rule for the subfolder takes precedence. The order of the rules does not matter.
- Files that no rule covers use the connection’s **Target collection**.
- Leading and trailing slashes are ignored.

Example with the connection’s **Target collection** set to *Misc*:

| Rule | Files | Collection |
| - | - | - |
| `reports/2026` | `reports/2026/q1.pdf` | *Finance 2026* |
| `reports` | `reports/2025/q4.pdf`, `reports/summary.pdf` | *Finance* |
| *(none)* | `reports/2026-old/x.pdf`, `hr/leave.pdf`, `readme.txt` | *Misc* |

### [Changing the rules](https://docs.smartchat.ai.t-systems.net/user/admin/s3-autosync/#changing-the-rules)

Changed rules take effect on the **next scheduled sync**. Files that were already synced under the previous rules are **moved**: on the next run AutoSync re-ingests each affected file into its new collection and removes it from the old one, exactly as if the file had changed in the bucket. The same happens when you change the connection’s **Target collection**.

Keep in mind:

- Moving is a re-ingest. A rule that covers many files causes correspondingly many ingestions, processed in batches over consecutive runs.
- A file whose move fails shows up with a failed status in the collection, like any other failed ingestion, and is retried on the next change of that file.
- Only files that AutoSync itself uploaded are moved. A copy of the same file that someone uploaded manually keeps its collection.

## [Monitoring a connection](https://docs.smartchat.ai.t-systems.net/user/admin/s3-autosync/#monitoring-a-connection)

| Column | Meaning |
| - | - |
| **Status** | **Active**: scheduled and running. **Paused**: settings kept, bucket not checked. **No schedule**: saved without a schedule yet. |
| **Bucket** | The bucket name; hover for the endpoint URL. |
| **Collection** | The target collection and the number of folder rules. |
| **Schedule** | The interval and **Next:** the time of the next run. |
| **Last sync** | When the last run finished, with counts of **Success**, **Failed** and **Pending** files. |

Click the connection’s **Name** to copy it to the clipboard.

### [Sync statistics](https://docs.smartchat.ai.t-systems.net/user/admin/s3-autosync/#sync-statistics)

**Sync statistics** opens a summary of the connection: **All time** totals for **Files processed**, **Added**, **Updated** and **Removed**, and a table of the **Last sync runs** with the same counts per run.

*\[Image: Sync statistics dialog]*

Failed files are listed with their error in the target collection under **Workspace → Knowledge**; see [Ingestion Errors](https://docs.smartchat.ai.t-systems.net/user/files/ingestion-errors/) for the meaning of each status.

## [Managing connections](https://docs.smartchat.ai.t-systems.net/user/admin/s3-autosync/#managing-connections)

| Button | Action |
| - | - |
| **Test connection** | Checks whether the bucket is reachable with the stored credentials. |
| **Pause sync** / **Resume sync** | Stops checking the bucket until you resume. Already synced files stay in the Space. |
| **Sync statistics** | Opens the statistics dialog described above. |
| **Edit S3 connection** | Change endpoint, bucket, credentials, interval, target collection or folder rules. |
| **Remove S3 connection** | Deletes the connection and its schedule. Content already synced into the Space **stays**. |

> **No manual run**
>
> Unlike Confluence connections there is no **Sync now** button. Choose a shorter **Sync interval** if you need faster pick-up of new files.
