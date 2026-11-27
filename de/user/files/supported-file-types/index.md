# Unterstützte Dateitypen

Source: https://docs.smartchat.ai.t-systems.net/de/user/files/supported-file-types/

> Die Dateiformate, die Smartchat extrahieren und indexieren kann, nach Kategorien gruppiert.

Smartchat extrahiert den Inhalt einer Datei mit einem auf ihr Format zugeschnittenen Parser und indexiert ihn anschließend mit einem Embedding-Modell, damit er in Chats gefunden werden kann. Nur Formate, für die ein Parser vorhanden ist, können eingelesen werden — diese Seite listet sie auf.

Dieselbe Liste gilt überall dort, wo eine Datei in einen Space gelangt: manueller Upload, [S3 AutoSync](https://docs.smartchat.ai.t-systems.net/de/user/admin/s3-autosync/) und [Confluence Sync](https://docs.smartchat.ai.t-systems.net/de/user/admin/confluence-sync/).

## [Formate](https://docs.smartchat.ai.t-systems.net/de/user/files/supported-file-types/#formate)

| Kategorie | Dateitypen |
| - | - |
| Textdokumente | `pdf`, `doc`, `docx`, `rtf`, `epub` |
| Präsentationen | `ppt`, `pptx` |
| Tabellen | `xls`, `xlsx`, `csv` |
| Text- und Auszeichnungsformate | `txt`, `md`, `html`, `xml`, `json` |
| E-Mail | `msg`, `mbox` |
| Quelltext | `py`, `pyw`, `pyi`, `js`, `mjs`, `cjs`, `jsx`, `ts`, `tsx`, `mts`, `go`, `rs`, `java`, `c`, `h`, `cpp`, `hpp`, `cc`, `cs`, `rb`, `php`, `swift`, `kt`, `scala`, `sh`, `bash`, `sql` |
| Audio | `mp3` |

Audiodateien werden vor der Indexierung in Text transkribiert.

> **Hinweis**
>
> Die Liste ändert sich im Laufe der Zeit. Formate kommen hinzu, sobald Parser dafür verfügbar sind; selten verwendete Formate können entfernt werden.

## [Wenn ein Format nicht aufgeführt ist](https://docs.smartchat.ai.t-systems.net/de/user/files/supported-file-types/#wenn-ein-format-nicht-aufgef%C3%BChrt-ist)

Konvertieren Sie die Datei vor dem Hochladen in ein unterstütztes Format, zum Beispiel nach PDF oder DOCX. Schlägt das Einlesen bei einer Datei fehl, deren Format aufgeführt *ist*, siehe [Ingestion-Fehler](https://docs.smartchat.ai.t-systems.net/de/user/files/ingestion-errors/).

## [Siehe auch](https://docs.smartchat.ai.t-systems.net/de/user/files/supported-file-types/#siehe-auch)

- [Dateigrößen-Limits](https://docs.smartchat.ai.t-systems.net/de/user/files/file-size-limits/) — Grenzen für Dateigröße, Seitenzahl und Textmenge
