# S3 AutoSync

Source: https://docs.smartchat.ai.t-systems.net/de/user/admin/s3-autosync/

> Dateien aus einem S3-Bucket (OTC OBS) automatisch in Ihren Smartchat-Space synchronisieren.

S3 AutoSync übernimmt Dateien aus einem S3-kompatiblen Bucket (OTC Object Storage, OBS) nach Zeitplan in Ihren Smartchat-Space. Neue, geänderte und gelöschte Dateien im Bucket werden erkannt und stehen jedem Mitglied des Spaces als durchsuchbarer Kontext zur Verfügung.

## [Voraussetzungen](https://docs.smartchat.ai.t-systems.net/de/user/admin/s3-autosync/#voraussetzungen)

- Sie benötigen die Rolle **Space Owner** im Smartchat-Space. Details unter [Rollen](https://docs.smartchat.ai.t-systems.net/de/user/concepts/roles/).
- Einen S3-Bucket, seine Endpunkt-URL und ein Schlüsselpaar mit Lesezugriff darauf. Dateien laden Sie mit Ihren eigenen Werkzeugen in den Bucket (z. B. `boto3`, OBS Browser oder Huawei SDK).
- S3 AutoSync muss in Ihrer Smartchat-Umgebung aktiviert sein. Fehlt die Seite **S3 AutoSync**, wenden Sie sich an Ihren Anwendungsinhaber.

> **Upload mit boto3: Integritätssignierung deaktivieren**
>
> OTC OBS unterstützt die S3-Request-Checksum-/Integritätssignierung nicht, die neuere `boto3`-Versionen (`> 1.36`) standardmäßig aktivieren. Ein Upload mit aktivierter Signierung **beschädigt die gespeicherten Dateien**: Sie verlieren Metadaten und können nicht mehr aufgenommen werden.
>
> Deaktivieren Sie sie beim Upload mit `boto3`, indem Sie sowohl `request_checksum_calculation` als auch `response_checksum_validation` in der Client-Konfiguration auf `when_required` setzen:
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
> Alternativ laden Sie über den OBS Browser oder das Huawei SDK hoch.

## [Schritt 1 — S3 AutoSync öffnen](https://docs.smartchat.ai.t-systems.net/de/user/admin/s3-autosync/#schritt-1--s3-autosync-%C3%B6ffnen)

Klicken Sie auf Ihr Profilbild, wählen Sie **Administration** und wählen Sie unter **Bereichsinhaber** im Feld **Aktueller Bereich** den Space. Öffnen Sie dann **S3 AutoSync**. Die Tabelle listet die S3-Verbindungen dieses Spaces und aktualisiert sich jede Minute selbst.

*\[Image: Seite S3 AutoSync mit einer aktiven Verbindung]*

## [Schritt 2 — Verbindung hinzufügen](https://docs.smartchat.ai.t-systems.net/de/user/admin/s3-autosync/#schritt-2--verbindung-hinzuf%C3%BCgen)

Klicken Sie auf **S3-Verbindung hinzufügen** und füllen Sie das Formular aus:

*\[Image: Formular S3-Verbindung hinzufügen mit Ordnerregeln]*

**Quelle**

| Feld | Beschreibung |
| - | - |
| **Name** | Ein Name für die Verbindung, wie er in der Tabelle erscheint. |
| **Endpunkt-URL** | Der S3-Endpunkt, z. B. `https://obs.eu-de.otc.t-systems.com`. |
| **Bucket-Name** | Der zu überwachende Bucket: Kleinbuchstaben, Ziffern, Punkte und Bindestriche. |
| **Region** | Die Region des Buckets, `eu-de` für OTC. |

**Zugangsdaten**

| Feld | Beschreibung |
| - | - |
| **Access Key ID** / **Secret Access Key** | Ein Schlüsselpaar mit Lesezugriff auf den Bucket. Die Werte werden verschlüsselt gespeichert und nie wieder angezeigt; lassen Sie beide beim Bearbeiten leer, um sie zu behalten. |

**Synchronisierung**

| Feld | Beschreibung |
| - | - |
| **Synchronisierungsintervall** | Wie oft der Bucket geprüft wird: **Alle 15 Minuten**, **Jede Stunde** (Standard), **Alle 6 Stunden**, **Alle 12 Stunden**, **Täglich** oder **Wöchentlich**. |
| **Ingest-Pipeline** | Nur sichtbar, wenn der Space mehr als eine Ingestion-Konfiguration hat. Wählen Sie, welche die synchronisierten Dateien verarbeitet. |
| **Zielkollektion** | Wo Dateien landen, die keine Ordnerregel abdeckt. **Allgemeine Kollektion** ist die Standardkollektion des Spaces. Eine spätere Änderung **verschiebt** bereits synchronisierte Dateien bei der nächsten Synchronisation. |
| **Ordnerregeln** | Ordner des Buckets in andere Kollektionen leiten, siehe [Ordnerregeln](https://docs.smartchat.ai.t-systems.net/de/user/admin/s3-autosync/#ordnerregeln). |
| **Aktiv** | Eingeschaltet lassen. Pausierte Verbindungen behalten ihre Einstellungen, der Bucket wird aber nicht geprüft. |

Die Kollektion muss noch nicht existieren: **Neue Kollektion …** in der Auswahl **Zielkollektion** oder in der Auswahl einer Ordnerregel öffnet einen Dialog für ihren Namen und eine optionale Beschreibung, legt sie sofort an und wählt sie aus. Die Kollektion bleibt im Arbeitsbereich, auch wenn Sie die Verbindung nicht speichern.

Eine Kollektion lässt sich direkt aus dem Formular anlegen. Sie bleibt erhalten, auch wenn Sie die Verbindung nicht speichern.

Klicken Sie auf **Speichern**. Smartchat prüft den Bucket sofort mit den angegebenen Zugangsdaten:

- Beim **Anlegen** wird ein nicht erreichbarer Bucket abgelehnt. Es wird nichts gespeichert, bis Endpunkt, Bucket und Schlüssel stimmen.
- Beim **Bearbeiten** wird die Verbindung in jedem Fall gespeichert; ist der Bucket nicht erreichbar, wird die Synchronisation pausiert (Meldung **Verbindung gespeichert, aber der Bucket ist nicht erreichbar. Die Synchronisation bleibt pausiert, bis die Einstellungen korrigiert sind.**).

Der erste Lauf startet mit dem nächsten Intervall. Bereits im Bucket liegende Dateien werden in diesem Lauf aufgenommen; danach werden nur noch Ergänzungen, Änderungen und Löschungen verarbeitet.

## [Ordnerregeln](https://docs.smartchat.ai.t-systems.net/de/user/admin/s3-autosync/#ordnerregeln)

Standardmäßig landet jede Datei des Buckets in der **Zielkollektion** der Verbindung. Wenn Sie mehrere Datenquellen in einem Bucket zusammenführen, können Sie stattdessen jeden Ordner mit **Ordnerregeln** in eine eigene Kollektion leiten.

Klicken Sie im Formular auf **Ordnerregel hinzufügen** und geben Sie den Ordnerpfad im Bucket (z. B. `reports/2026`) sowie die **Zielkollektion** dafür an. Legen Sie eine Zeile pro Ordner an; jeder Ordner darf nur einmal vorkommen.

### [Wie Ordner zugeordnet werden](https://docs.smartchat.ai.t-systems.net/de/user/admin/s3-autosync/#wie-ordner-zugeordnet-werden)

- Eine Regel gilt für jedes Objekt **innerhalb** des Ordners, in beliebiger Tiefe. `reports/2026` passt auf `reports/2026/q1.pdf` und `reports/2026/archive/old.pdf`.
- Die Zuordnung endet an Ordnergrenzen: `reports/2026` passt **nicht** auf `reports/2026-old/x.pdf`, und eine Regel `reports` passt nicht auf `reportsarchive/x.pdf`.
- Gibt es eine Regel für einen Ordner und eine weitere für einen seiner Unterordner, hat die Regel für den Unterordner Vorrang. Die Reihenfolge der Regeln spielt keine Rolle.
- Dateien ohne passende Regel verwenden die **Zielkollektion** der Verbindung.
- Führende und abschließende Schrägstriche werden ignoriert.

Beispiel mit der **Zielkollektion** der Verbindung *Misc*:

| Regel | Dateien | Kollektion |
| - | - | - |
| `reports/2026` | `reports/2026/q1.pdf` | *Finance 2026* |
| `reports` | `reports/2025/q4.pdf`, `reports/summary.pdf` | *Finance* |
| *(keine)* | `reports/2026-old/x.pdf`, `hr/leave.pdf`, `readme.txt` | *Misc* |

### [Regeln ändern](https://docs.smartchat.ai.t-systems.net/de/user/admin/s3-autosync/#regeln-%C3%A4ndern)

Geänderte Regeln wirken ab der **nächsten geplanten Synchronisation**. Dateien, die unter den bisherigen Regeln synchronisiert wurden, werden **verschoben**: Beim nächsten Lauf nimmt AutoSync jede betroffene Datei in ihre neue Kollektion auf und entfernt sie aus der alten, genau so, als hätte sich die Datei im Bucket geändert. Dasselbe passiert, wenn Sie die **Zielkollektion** der Verbindung ändern.

Beachten Sie:

- Verschieben ist eine erneute Aufnahme. Eine Regel, die viele Dateien abdeckt, verursacht entsprechend viele Ingestions, die in Batches über aufeinanderfolgende Läufe verarbeitet werden.
- Eine Datei, deren Verschiebung fehlschlägt, erscheint wie jede andere fehlgeschlagene Ingestion mit Fehlerstatus in der Kollektion und wird bei der nächsten Änderung dieser Datei erneut versucht.
- Nur Dateien, die AutoSync selbst hochgeladen hat, werden verschoben. Eine manuell hochgeladene Kopie derselben Datei behält ihre Kollektion.

## [Verbindung überwachen](https://docs.smartchat.ai.t-systems.net/de/user/admin/s3-autosync/#verbindung-%C3%BCberwachen)

| Spalte | Bedeutung |
| - | - |
| **Status** | **Aktiv**: geplant und laufend. **Pausiert**: Einstellungen behalten, Bucket wird nicht geprüft. **Kein Zeitplan**: ohne Zeitplan gespeichert. |
| **Bucket** | Der Bucket-Name; beim Überfahren erscheint die Endpunkt-URL. |
| **Kollektion** | Die Zielkollektion und die Anzahl der Ordnerregeln. |
| **Zeitplan** | Das Intervall und **Nächste:** die Uhrzeit des nächsten Laufs. |
| **Letzte Synchronisierung** | Wann der letzte Lauf endete, mit der Anzahl **erfolgreicher**, **fehlgeschlagener** und **ausstehender** Dateien. |

Ein Klick auf den **Namen** der Verbindung kopiert ihn in die Zwischenablage.

### [Synchronisierungsstatistik](https://docs.smartchat.ai.t-systems.net/de/user/admin/s3-autosync/#synchronisierungsstatistik)

**Synchronisierungsstatistik** öffnet eine Zusammenfassung der Verbindung: **Gesamt**-Werte für **Verarbeitete Dateien**, **Hinzugefügt**, **Aktualisiert** und **Entfernt** sowie eine Tabelle **Letzte Synchronisierungsläufe** mit denselben Zählern pro Lauf.

*\[Image: Dialog Synchronisierungsstatistik]*

Fehlgeschlagene Dateien werden mit ihrem Fehler in der Zielkollektion unter **Arbeitsbereich → Wissen** gelistet; die Bedeutung der einzelnen Status erklärt [Ingestion-Fehler](https://docs.smartchat.ai.t-systems.net/de/user/files/ingestion-errors/).

## [Verbindungen verwalten](https://docs.smartchat.ai.t-systems.net/de/user/admin/s3-autosync/#verbindungen-verwalten)

| Schaltfläche | Aktion |
| - | - |
| **Verbindung testen** | Prüft, ob der Bucket mit den gespeicherten Zugangsdaten erreichbar ist. |
| **Synchronisierung pausieren** / **Synchronisierung fortsetzen** | Setzt die Prüfung des Buckets aus, bis Sie fortsetzen. Bereits synchronisierte Dateien bleiben im Space. |
| **Synchronisierungsstatistik** | Öffnet den oben beschriebenen Statistik-Dialog. |
| **S3-Verbindung bearbeiten** | Endpunkt, Bucket, Zugangsdaten, Intervall, Zielkollektion oder Ordnerregeln ändern. |
| **S3-Verbindung entfernen** | Löscht die Verbindung und ihren Zeitplan. Bereits in den Space synchronisierte Inhalte **bleiben erhalten**. |

> **Kein manueller Lauf**
>
> Anders als bei Confluence-Verbindungen gibt es keine Schaltfläche **Jetzt synchronisieren**. Wählen Sie ein kürzeres **Synchronisierungsintervall**, wenn neue Dateien schneller übernommen werden sollen.
