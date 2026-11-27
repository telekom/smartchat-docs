# Fehler beim Datei-Upload

Source: https://docs.smartchat.ai.t-systems.net/de/user/files/ingestion-errors/

> Was die Verarbeitungsstatus einer Datei bedeuten, warum eine Datei nicht verarbeitet werden kann und was Sie bei jeder Ursache tun können.

Wenn Sie eine Datei zu einem Space hinzufügen, sei es durch manuelles Hochladen oder automatisch über [S3 AutoSync](https://docs.smartchat.ai.t-systems.net/de/user/admin/s3-autosync/) oder [Confluence Sync](https://docs.smartchat.ai.t-systems.net/de/user/admin/confluence-sync/), extrahiert Smartchat den Text, teilt ihn in Chunks auf und indexiert diese, damit sie in Chats gefunden werden können. Jede Datei durchläuft denselben Lebenszyklus, und ihre Kollektion unter **Arbeitsbereich → Kollektion** zeigt den aktuellen Status an.

Die meisten Dateien werden problemlos verarbeitet. Wenn nicht, geben Status und Fehlermeldung Aufschluss. Diese Seite erklärt die Status, die häufigsten Fehlerursachen und was Sie dagegen tun können.

## [Status](https://docs.smartchat.ai.t-systems.net/de/user/files/ingestion-errors/#status)

| Status | Bedeutung |
| - | - |
| **pending** | Die Datei ist in der Warteschlange oder wird gerade verarbeitet. Das ist normal und vorübergehend. |
| **ingested** | Die Datei wurde erfolgreich verarbeitet und ist im Space durchsuchbar. |
| **ingestion\_failed** | Die Verarbeitung wurde versucht (und automatisch wiederholt), war aber nicht erfolgreich. Die Datei ist im Space **nicht** verfügbar. Prüfen Sie die Fehlermeldung für Details. |
| **migrated** | Die Datei hat das Zeitlimit in der Standard-Warteschlange überschritten und wurde zur Verarbeitung in die [Warteschlange für große Dateien](https://docs.smartchat.ai.t-systems.net/de/user/files/file-size-limits/#gro%C3%9Fe-dateien-brauchen-l%C3%A4nger) verschoben. Dies ist ein vorübergehender Zustand; die Datei wird schließlich als `ingested` oder `ingestion_failed` abgeschlossen. |
| **hit\_rate\_limit** | Die Verarbeitung ist pausiert, weil der Embedding-Dienst vorübergehend eine Ratelimit erreicht hat. Sie müssen nichts tun; die Datei wird im nächsten verfügbaren Zeitfenster erneut verarbeitet. Dies ist ein vorübergehender Zustand. |

> **Hinweis**
>
> Vorübergehende Probleme werden automatisch einige Male wiederholt, bevor eine Datei als `ingestion_failed` markiert wird. Ein fehlgeschlagener Status bedeutet also, dass der Fehler über mehrere Versuche hinweg bestehen blieb; es handelt sich nicht um einen einmaligen Aussetzer.

## [Warum eine Datei fehlschlägt](https://docs.smartchat.ai.t-systems.net/de/user/files/ingestion-errors/#warum-eine-datei-fehlschl%C3%A4gt)

Nahezu jede `ingestion_failed`-Datei fällt in eine der folgenden Kategorien. Bei einem Fehler zeigt die Kollektion eine detaillierte Fehlermeldung neben dem Status an. Die Überschriften unten entsprechen diesen Fehlermeldungen, damit Sie Ihre direkt nachschlagen können.

### [No nodes were generated for this document.](https://docs.smartchat.ai.t-systems.net/de/user/files/ingestion-errors/#no-nodes-were-generated-for-this-document)

Die häufigste Ursache. Smartchat indexiert **Text**; wenn aus einem Dokument nichts extrahiert werden kann, gibt es nichts zu indexieren und die Verarbeitung schlägt fehl.

Das passiert typischerweise bei:

- **Gescannten PDFs**: Seiten, die Fotos oder Scans von Papier sind und keine hinterlegte Textebene besitzen.
- **Reinen Bilddokumenten**: ein PDF, dessen Seiten vollständig aus Bildern bestehen (Diagramme, Screenshots, eine Wortwolke, ein Poster).
- Dateien, deren eigentlicher Inhalt nur in Bildern liegt, die der Extraktor nicht als Text lesen kann.

**Was Sie tun können:**

- Stellen Sie eine **textbasierte Version** des Dokuments bereit statt eines Scans.
- Führen Sie zuerst eine **OCR** (Texterkennung, Optical Character Recognition) auf der Datei aus, sodass sie eine Textebene erhält, und laden Sie sie dann erneut hoch.
- Wenn nur ein Teil des Dokuments reines Bildmaterial ist, wird eine Version mit ordentlicher Textebene die lesbaren Teile verarbeiten.

### [Error occurred while reading the file.](https://docs.smartchat.ai.t-systems.net/de/user/files/ingestion-errors/#error-occurred-while-reading-the-file)

Die Datei kann nicht verarbeitet werden, weil sie defekt oder unvollständig ist oder von einem Programm erzeugt wurde, das sich nicht an die Spezifikation des Dateiformats hält. Bei PDFs äußert sich das als Lesefehler tief im Parser (zum Beispiel ein defekter interner Bild-Stream oder eine fehlerhafte Seitennummerierungs-Tabelle).

**Was Sie tun können:**

- **Exportieren oder reparieren Sie die Datei neu.** Öffnen Sie sie in einem Viewer und nutzen Sie *Als PDF drucken* / *Als PDF speichern*, oder exportieren Sie sie erneut aus der Originalquelle, und laden Sie anschließend die frische Kopie hoch. Dadurch wird eine saubere Datei erzeugt, was die meisten Parser-Fehler behebt.
- Prüfen Sie, ob sich die Datei in einem normalen Viewer korrekt öffnen lässt; ist sie dort sichtbar defekt, muss sie an der Quelle neu erzeugt werden.

### [File extension is not supported](https://docs.smartchat.ai.t-systems.net/de/user/files/ingestion-errors/#file-extension-is-not-supported)

Die Dateiendung gehört nicht zu den unterstützten Formaten. Smartchat verarbeitet gängige Dokument- und Textformate; andere Typen (ausführbare Dateien, Archive, Rohmediendateien usw.) werden bei der Verarbeitung abgelehnt.

**Was Sie tun können:** Konvertieren Sie den Inhalt in ein unterstütztes Format (PDF, DOCX, TXT oder ein anderes in der Dokumentation Ihrer Installation aufgeführtes Format) und laden Sie die Datei erneut hoch.

### [Task size exceeds the allowed limit.](https://docs.smartchat.ai.t-systems.net/de/user/files/ingestion-errors/#task-size-exceeds-the-allowed-limit)

Die Datei erzeugt mehr Chunks als das Limit pro Datei erlaubt. Siehe [Dateigrößenlimits](https://docs.smartchat.ai.t-systems.net/de/user/files/file-size-limits/) für die genauen Grenzwerte.

**Was Sie tun können:** Teilen Sie das Dokument in kleinere Dateien auf oder entfernen Sie Inhalte, die nicht durchsuchbar sein müssen.

### [OpenAI rate limit exceeded.](https://docs.smartchat.ai.t-systems.net/de/user/files/ingestion-errors/#openai-rate-limit-exceeded)

Der Embedding-Dienst hat ein Tokens-pro-Minute-Limit (TPM). Während der Verarbeitung teilt der Worker den Text in Batches auf und halbiert die Batch-Größe bei jedem Ratenlimit-Fehler. Wenn der Batch nur noch aus einem einzelnen Chunk besteht und das TPM-Budget immer noch überschritten wird, ist keine weitere Aufteilung möglich und die Datei schlägt dauerhaft fehl.

**Was Sie tun können:** Bitten Sie Ihre Plattform-Betreiber, entweder die konfigurierte Chunk-Größe zu reduzieren oder das TPM-Limit des für das Embedding verwendeten API-Schlüssels zu erhöhen.

### [Task hit soft time limit even after migrating to large queue.](https://docs.smartchat.ai.t-systems.net/de/user/files/ingestion-errors/#task-hit-soft-time-limit-even-after-migrating-to-large-queue)

Die Datei hat zu lange für die Verarbeitung gebraucht und ist sowohl in der Standard- als auch in der Warteschlange für große Dateien abgelaufen. **Ein erneuter Versuch hilft nicht**; die Datei wird weiterhin die maximal zulässige Verarbeitungszeit überschreiten.

**Was Sie tun können:** Teilen Sie das Dokument in kleinere Dateien auf oder entfernen Sie Inhalte, die nicht durchsuchbar sein müssen. Siehe [Dateigrößenlimits](https://docs.smartchat.ai.t-systems.net/de/user/files/file-size-limits/) für weitere Hinweise.

### [File was not found.](https://docs.smartchat.ai.t-systems.net/de/user/files/ingestion-errors/#file-was-not-found)

Die Dateireferenz existiert, aber die eigentliche Datei fehlt im Speicher. Es gibt zwei Fälle:

- **Synchronisierte Inhalte** ([S3 AutoSync](https://docs.smartchat.ai.t-systems.net/de/user/admin/s3-autosync/), [Confluence Sync](https://docs.smartchat.ai.t-systems.net/de/user/admin/confluence-sync/) oder andere Datenverbindungen): Die Datei wurde aus der Quelle entfernt, nachdem die Verarbeitung bereits in die Warteschlange gestellt war. Das ist korrektes Verhalten; es gibt nichts zu tun. Wenn Sie die Datei noch benötigen, fügen Sie sie wieder zur Quelle hinzu.
- **Manuelle Uploads**: Das sollte nicht passieren und deutet auf einen Fehler hin. Löschen Sie die Datei aus dem Space und laden Sie sie erneut hoch.

### [Vorübergehende Fehler oder Infrastrukturfehler](https://docs.smartchat.ai.t-systems.net/de/user/files/ingestion-errors/#vor%C3%BCbergehende-fehler-oder-infrastrukturfehler)

Gelegentlich schlägt eine Datei aufgrund einer vorübergehenden Bedingung fehl: ein API-Timeout, ein Speicher-Aussetzer oder eine kurzzeitig nicht verfügbare Verarbeitungskomponente. Diese werden automatisch wiederholt, und die meisten erholen sich von selbst. Wenn eine Datei fehlschlägt und Sie überzeugt sind, dass die Datei selbst in Ordnung ist, stoßen Sie die Verarbeitung etwas später erneut an. Schlägt sie weiterhin fehl, wenden Sie sich an Ihre Plattform-Betreiber.

Die folgenden Fehlermeldungen fallen in diese Kategorie:

- `OpenAI API error occurred.`: ein vorübergehender Fehler des Embedding-Dienstes.
- `Cannot connect to Postgres Database.`: die Datenbank war kurzzeitig nicht erreichbar.
- `Cannot connect to S3 file system.`: der Objektspeicher war kurzzeitig nicht erreichbar.
- `Pipeline could not be built.`: die Verarbeitungs-Pipeline konnte nicht initialisiert werden; dies ist typischerweise ein Infrastrukturproblem.

## [Dateien, die im Status „pending” hängen bleiben](https://docs.smartchat.ai.t-systems.net/de/user/files/ingestion-errors/#dateien-die-im-status-pending-h%C3%A4ngen-bleiben)

`pending` ist ein normaler, vorübergehender Zustand, aber eine Datei, die lange ohne Fortschritt in `pending` verbleibt, ist einen Blick wert. Das ist **nicht** dasselbe wie ein Fehlschlag: die Datei ist nicht auf einen Fehler gelaufen, sie ist nur noch nicht fertig verarbeitet (oder noch nicht gestartet).

Häufige Gründe:

- **Große Dateien dauern länger.** Große Dokumente werden auf einer [separaten Warteschlange](https://docs.smartchat.ai.t-systems.net/de/user/files/file-size-limits/#gro%C3%9Fe-dateien-brauchen-l%C3%A4nger) verarbeitet und werden bewusst später fertig. Eine große Datei, die eine Weile in `pending` liegt, ist zu erwarten. Möglicherweise sehen Sie den Status `migrated`, während die Datei in die Warteschlange für große Dateien verschoben wird; er wird zu `ingested` oder `ingestion_failed` wechseln, sobald die Verarbeitung abgeschlossen ist.
- **Warteschlangen-Rückstau.** Während eines großen Massenimports warten Dateien hinter allem, was bereits in der Warteschlange steht.
- **Der Job wurde nie aufgenommen.** Seltener wird eine Datei nie zur Verarbeitung eingeplant, etwa wegen einer Störung des Ingestion-Dienstes. In diesem Fall zeigt die Datei überhaupt keine Verarbeitungsaktivität.

**Was Sie tun können:** Geben Sie großen Dateien und großen Stapeln Zeit, die Warteschlange zu durchlaufen. In sehr ausgelasteten Systemen, insbesondere in der Warteschlange für große Dateien, kann dies Stunden bis Tage dauern. Ein früherer erneuter Versuch erhöht nur den Druck auf die Warteschlange und hilft nicht.

Versuchen Sie einen erneuten Upload nur dann, wenn die Warteschlange leer ist (d.h. neue Dateien werden sofort verarbeitet), Ihre Datei aber weiterhin in `pending` hängt. Das deutet darauf hin, dass der Task dauerhaft verloren ging und der Status „hängen geblieben” ist. Wenn sich die Datei nach dem erneuten Versuch immer noch nicht bewegt, wenden Sie sich an Ihren Anwendungsinhaber oder Ihre Plattform-Betreiber.

## [Weitere Details erhalten](https://docs.smartchat.ai.t-systems.net/de/user/files/ingestion-errors/#weitere-details-erhalten)

Für eine tiefere Untersuchung protokolliert der Ingestion-Dienst den vollständigen Fehler (einschließlich der Datei, des internen Tasks und der zugrunde liegenden Exception) in seinen Logs. Wenn Sie mehr Kontext benötigen als die Fehlermeldung bietet, bitten Sie Ihre Plattform-Betreiber, die Logs des Ingestion-Workers für diese Datei zu prüfen.
