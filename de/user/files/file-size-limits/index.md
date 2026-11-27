# Dateigrößenlimits

Source: https://docs.smartchat.ai.t-systems.net/de/user/files/file-size-limits/

> Wie groß eine Datei sein darf, um in einen Smartchat-Space zu gelangen und indexiert zu werden — mit dem Limit für die Dateigröße, dem Seitenlimit für PDFs, dem Limit für die Textmenge, den Gründen für die Limits und dem Umgang mit sehr großen Dateien.

Wenn Sie eine Datei zu einem Space hinzufügen — durch Hochladen oder automatisch über [S3 AutoSync](https://docs.smartchat.ai.t-systems.net/de/user/admin/s3-autosync/) oder Confluence Sync — teilt Smartchat die Datei in kleine Chunks auf und indexiert diese, damit sie in Chats gefunden werden können. Sehr große Dateien erzeugen eine enorme Anzahl an Chunks, was langsam zu verarbeiten und speicherintensiv ist. Damit die Ingestion für alle zuverlässig bleibt, darf eine einzelne Datei nur eine gewisse Größe haben.

## [Die Limits](https://docs.smartchat.ai.t-systems.net/de/user/files/file-size-limits/#die-limits)

Die Größe ist auf mehrere Arten begrenzt: wie viele Megabyte die Datei hat, wie viele Seiten ein PDF hat und wie viel Text sie enthält.

| Limit | Gilt für | Maximum |
| - | - | - |
| **Dateigröße** | Dateien, die Sie in Smartchat hochladen | **100 MB** |
| **Dateigröße** | Dateien, die über die eRAG-API hinzugefügt werden | **200 MB** |
| **Seiten** | PDF-Dateien | **500 Seiten** |
| **Textmenge** | Jede Datei (einschließlich PDFs) | ungefähr **2.000 Chunks** (sehr grob **2 Millionen Tokens** bzw. einige tausend Seiten reiner Text) |

Ein **Chunk** ist ein Ausschnitt des Dokuments von etwa 1.000 Tokens (ein Token entspricht ungefähr ¾ eines Wortes). Die genaue Chunk-Größe hängt von der Konfiguration Ihres Spaces ab, daher variiert die entsprechende Wort- oder Seitenzahl.

Eine Datei muss jedes Limit einhalten, das für sie gilt — ein PDF etwa die Limits für Dateigröße, Seitenzahl und Textmenge gleichermaßen.

Die Limits greifen an unterschiedlichen Stellen: Eine Datei über dem Limit für die Dateigröße wird bereits beim Hochladen abgewiesen und gelangt nie in den Space, während eine zu lange Datei zwar hochgeladen, aber **nicht eingelesen** wird und daher nicht in Chats verwendet werden kann.

> **Hinweis**
>
> Dateien bis 100 MB können Sie direkt in Smartchat unter **Arbeitsbereich → Kollektion** hochladen. Größere Dateien, bis 200 MB, lassen sich nur über die eRAG-API hinzufügen, siehe [Viele Dateien auf einmal hochladen](https://docs.smartchat.ai.t-systems.net/de/user/admin/uploading-many-files/).

## [Warum es ein hartes Limit gibt](https://docs.smartchat.ai.t-systems.net/de/user/files/file-size-limits/#warum-es-ein-hartes-limit-gibt)

Das Limit für die Textmenge ist eine bewusste Sicherheitsgrenze. Die Server, die die Ingestion verarbeiten, haben eine begrenzte Menge an Arbeitsspeicher, und eine beliebig große Datei könnte diesen vollständig aufbrauchen und die Verarbeitung anderer Dateien und Spaces destabilisieren. Da die Verarbeitung innerhalb dieses Speichers bleiben muss, muss eine Datei bei *irgendeiner* Größe abgelehnt werden, um das System stabil zu halten — die genaue Grenze ist daher, ehrlich gesagt, etwas willkürlich. Sie ist weit über dem angesetzt, was reale Dokumente benötigen: Die große Mehrheit der Dateien (weit über 99 %) ist deutlich kleiner als das Limit und ist nie betroffen.

## [Große Dateien brauchen länger](https://docs.smartchat.ai.t-systems.net/de/user/files/file-size-limits/#gro%C3%9Fe-dateien-brauchen-l%C3%A4nger)

Eine große Datei braucht schlicht länger zum Einlesen, weil es mehr Inhalt aufzuteilen und zu indexieren gibt. Diese Langsamkeit rührt von der Größe der Datei selbst her, nicht davon, wie Smartchat sie verarbeitet.

Damit diese langlaufenden Jobs kleinere Dateien nicht aufhalten, verarbeitet Smartchat große Dateien (grob ab 100 Seiten oder rund 400 Chunks) auf einer **separaten Warteschlange**. Diese Warteschlange ist nicht langsamer oder leistungsschwächer; sie hat dieselben Ressourcen wie die Haupt-Warteschlange. Sie hält große Dateien lediglich aus dem Weg, damit schnelle Dateien nicht dahinter feststecken, und gibt einem Job die längere Zeit, die er zum Abschließen braucht. Sie müssen nichts tun; große Dateien werden einfach später fertig.

Dateien, die automatisch über [S3 AutoSync](https://docs.smartchat.ai.t-systems.net/de/user/admin/s3-autosync/) hereinkommen, verwenden immer diese separate Warteschlange, sodass große synchronisierte Dateien nie andere Ingestion aufhalten. Die obigen Größenlimits sind für synchronisierte Dateien exakt dieselben wie für hochgeladene.

## [Wenn eine Datei zu groß ist](https://docs.smartchat.ai.t-systems.net/de/user/files/file-size-limits/#wenn-eine-datei-zu-gro%C3%9F-ist)

- **Teilen Sie sie in kleinere Dateien auf.** Zerlegen Sie zum Beispiel ein großes PDF in Seitenbereiche oder ein langes Dokument in Dateien pro Abschnitt. Jeder Teil wird separat eingelesen.
- **Entfernen Sie Inhalte, die nicht durchsuchbar sein müssen** (zum Beispiel große, reine Bild-Anhänge), bevor Sie die Datei einlesen.
