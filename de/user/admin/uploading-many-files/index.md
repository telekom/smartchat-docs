# Viele Dateien auf einmal per API in eine Collection hochladen

Source: https://docs.smartchat.ai.t-systems.net/de/user/admin/uploading-many-files/

> Wie Sie einen ganzen Ordner mit Dateien in einen Space hochladen und einer Collection zuordnen, ohne jede Datei einzeln hochzuladen.

Für einzelne Dokumente funktioniert das Hochladen unter **Arbeitsbereich → Kollektion** gut. Wenn Sie aber Dutzende oder Hunderte von Dateien hinzufügen müssen — etwa beim Einrichten eines neuen Space, beim Umzug von Inhalten oder beim Laden eines Archivs — zeigt Ihnen diese Anleitung, wie Sie einen ganzen Ordner auf einmal hochladen und dabei jede Datei der gewünschten Collection zuordnen.

Dazu führen Sie ein kleines Skript auf Ihrem Rechner aus. Sie müssen dafür nicht entwickeln können, arbeiten aber im Terminal.

> **Gibt es eine bessere Lösung?**
>
> Wenn sich die Dateien regelmäßig ändern und Smartchat automatisch nachziehen soll, richten Sie statt eines einmaligen Uploads besser eine Synchronisation ein: [S3 AutoSync](https://docs.smartchat.ai.t-systems.net/de/user/admin/s3-autosync/) überwacht einen Storage-Bucket, [Confluence Sync](https://docs.smartchat.ai.t-systems.net/de/user/admin/confluence-sync/) einen Confluence-Space. Diese Anleitung ist für einen festen Satz von Dateien gedacht, den Sie einmalig hinzufügen.

## [Bevor Sie beginnen](https://docs.smartchat.ai.t-systems.net/de/user/admin/uploading-many-files/#bevor-sie-beginnen)

Sie benötigen:

- Ein Smartchat-Konto, das Dateien im Ziel-Space hinzufügen darf
- Die **Space-ID** des Ziel-Space — das Skript kann sie für Sie ermitteln
- Die **Collection-ID** der Collection, in die die Dateien sollen
- Den Ordner mit den Dateien auf Ihrem Rechner
- Python, eingerichtet wie unten beschrieben

## [Python einrichten](https://docs.smartchat.ai.t-systems.net/de/user/admin/uploading-many-files/#python-einrichten)

Das Skript benötigt **Python 3.10 oder neuer** sowie ein zusätzliches Paket namens `httpx`.

Prüfen Sie Ihre Version im Terminal:

```bash
python3 --version
```

Sie erhalten eine Ausgabe wie `Python 3.12.5`. Entscheidend ist die mittlere Zahl: Sie muss **10 oder höher** sein.

> **Sie wissen nicht, wie Sie Python installieren oder aktualisieren?**
>
> Wir empfehlen **uv** — ein Werkzeug, das Python-Versionen und Pakete für Sie verwaltet. Es lädt die passende Python-Version automatisch herunter, Sie müssen also nichts von Hand installieren oder aktualisieren, und eine bereits vorhandene Python-Installation bleibt unberührt.
>
> Folgen Sie zur Installation der [uv-Installationsanleitung](https://docs.astral.sh/uv/getting-started/installation/) — ein einziger Befehl unter macOS, Linux oder Windows.

Alle Befehle unten sind in zwei Varianten angegeben. Verwenden Sie den Tab **uv**, sofern Sie nicht bereits ein eingerichtetes Python bevorzugen.

## [Skript herunterladen](https://docs.smartchat.ai.t-systems.net/de/user/admin/uploading-many-files/#skript-herunterladen)

Hier herunterladen: [`upload-files-to-collection.py`](https://docs.smartchat.ai.t-systems.net/scripts/upload-files-to-collection.py)

Speichern Sie die Datei an einem Ort, den Sie wiederfinden, und öffnen Sie dort ein Terminal.

**uv (empfohlen)**

Hier ist nichts weiter einzurichten. `uv` liest die benötigten Pakete aus dem Skript selbst und kümmert sich beim ersten Ausführen um alles Weitere.

**Nur Python**

Legen Sie neben dem Skript eine temporäre Python-Umgebung an und installieren Sie `httpx` darin. So bleibt das Paket aus Ihrer Haupt-Python-Installation heraus.

```bash
python3 -m venv .venv
```

Anschließend aktivieren:

```bash
source .venv/bin/activate          # macOS und Linux
.venv\Scripts\activate             # Windows
```

Ihre Eingabeaufforderung beginnt nun mit `(.venv)`. Installieren Sie das Paket:

```bash
pip install httpx
```

Lassen Sie dieses Terminal geöffnet — die Python-Umgebung bleibt aktiv, bis Sie das Fenster schließen oder `deactivate` ausführen. Wenn Sie später weiterarbeiten, aktivieren Sie die Python-Umgebung erneut, bevor Sie das Skript starten. Wenn Sie endgültig fertig sind, löschen Sie den Ordner `.venv`.

## [Skript mit Ihrem Smartchat verbinden](https://docs.smartchat.ai.t-systems.net/de/user/admin/uploading-many-files/#skript-mit-ihrem-smartchat-verbinden)

Das Skript benötigt die Adresse des API-Gateways Ihrer Installation. Wenn Sie sie nicht kennen, fragen Sie Ihre Smartchat-Ansprechperson. Setzen Sie sie einmal im Terminal, in dem Sie arbeiten:

```bash
export SMARTCHAT_GATEWAY=https://<gateway-host>     # macOS und Linux
set SMARTCHAT_GATEWAY=https://<gateway-host>        # Windows
```

Alternativ übergeben Sie sie bei jedem Befehl als `--gateway https://<gateway-host>`.

## [Schritt 1 — Space-ID ermitteln](https://docs.smartchat.ai.t-systems.net/de/user/admin/uploading-many-files/#schritt-1--space-id-ermitteln)

**uv (empfohlen)**

```bash
uv run upload-files-to-collection.py --list-spaces
```

**Nur Python**

```bash
python upload-files-to-collection.py --list-spaces
```

Das Skript fragt nach Ihrer Smartchat-E-Mail-Adresse und Ihrem Passwort und listet anschließend alle Spaces auf, in denen Sie Mitglied sind — jeweils mit ID und Namen. Der Space, in dem Sie gerade arbeiten, ist mit einem `*` markiert.

Kopieren Sie die ID des Space, in den Sie hochladen möchten.

> **Hinweis**
>
> Fehlt ein Space, den Sie erwarten, sind Sie dort kein Mitglied. Bitten Sie einen Space Owner, Sie hinzuzufügen.

## [Schritt 2 — Collection-ID ermitteln](https://docs.smartchat.ai.t-systems.net/de/user/admin/uploading-many-files/#schritt-2--collection-id-ermitteln)

Öffnen Sie in Smartchat **Workspace → Collection** und dort die gewünschte Collection. Verwenden Sie die Schaltfläche **Copy ID** oben rechts auf der Seite.

*\[Image: Die Schaltfläche „Copy ID" oben rechts auf der Collection-Seite]*

Damit liegt die Collection-ID in Ihrer Zwischenablage.

## [Schritt 3 — Prüfen, was hochgeladen wird](https://docs.smartchat.ai.t-systems.net/de/user/admin/uploading-many-files/#schritt-3--pr%C3%BCfen-was-hochgeladen-wird)

Machen Sie vor dem eigentlichen Upload einen Probelauf. Mit `--dry-run` listet das Skript die Dateien auf, die es senden würde, und beendet sich, ohne Smartchat zu kontaktieren:

**uv (empfohlen)**

```bash
uv run upload-files-to-collection.py \
  --folder ./meine-dokumente \
  --space-id <Ihre-Space-ID> \
  --collection-id <Ihre-Collection-ID> \
  --dry-run
```

**Nur Python**

```bash
python upload-files-to-collection.py \
  --folder ./meine-dokumente \
  --space-id <Ihre-Space-ID> \
  --collection-id <Ihre-Collection-ID> \
  --dry-run
```

Lesen Sie die Liste aufmerksam. Standardmäßig nimmt das Skript **alles** aus dem Ordner mit, auch Dateien in Unterordnern. Mit einem Muster grenzen Sie die Auswahl ein:

```bash
--glob '**/*.pdf'      # nur PDFs, auch in Unterordnern
--glob '*.pdf'         # nur PDFs direkt im Ordner
--glob '*'             # alles im Ordner, aber keine Unterordner
```

Behalten Sie die Anführungszeichen um das Muster bei.

Versteckte Dateien werden immer ausgelassen, unabhängig vom Muster. Das betrifft alles, dessen Name mit einem Punkt beginnt, etwa `.DS_Store`, sowie sämtliche Inhalte versteckter Ordner wie `.git`. Das Skript nennt Ihnen die Anzahl der übersprungenen Dateien.

## [Schritt 4 — Hochladen](https://docs.smartchat.ai.t-systems.net/de/user/admin/uploading-many-files/#schritt-4--hochladen)

> **Nutzen Sie Smartchat nicht, während das Skript läuft**
>
> Lassen Sie die Smartchat-Oberfläche vom Start des Uploads bis zur Abschlussmeldung des Skripts unberührt. **Wechseln Sie vor allem nicht in einen anderen Space.**
>
> Das Skript arbeitet in dem Space, der für Ihr Konto gerade aktiv ist. Ein Space-Wechsel im Browser ändert das für Ihr gesamtes Konto — also auch für das Skript. Dateien können dadurch im falschen Space landen, und es gibt keine automatische Möglichkeit, sie zurückzuholen. Auch das gleichzeitige Hochladen, Löschen oder Bearbeiten von Dateien in der Oberfläche kann dazu führen, dass das Skript Fehler für eigentlich einwandfreie Dateien meldet.
>
> Wenn Sie Smartchat weiter nutzen müssen, warten Sie das Ende des Laufs ab oder verwenden Sie für den Upload ein anderes Konto.

Wenn die Liste stimmt, entfernen Sie `--dry-run` und führen den Befehl erneut aus:

**uv (empfohlen)**

```bash
uv run upload-files-to-collection.py \
  --folder ./meine-dokumente \
  --space-id <Ihre-Space-ID> \
  --collection-id <Ihre-Collection-ID>
```

**Nur Python**

```bash
python upload-files-to-collection.py \
  --folder ./meine-dokumente \
  --space-id <Ihre-Space-ID> \
  --collection-id <Ihre-Collection-ID>
```

Das Skript fragt nach Ihrem Passwort und arbeitet dann die Dateien ab. Für jede Datei zeigt es eine Fortschrittsanzeige mit der bisherigen Wartezeit, denn die Verarbeitung dauert je nach Dateigröße von wenigen Sekunden bis zu mehreren Minuten.

Zum Schluss gibt es eine Zusammenfassung aus: wie viele Dateien erfolgreich waren, wie viele fehlgeschlagen sind und woran es jeweils lag. Lassen Sie das Terminal-Fenster bis zum Ende geöffnet.

> **Achtung**
>
> Die erste Zeile jedes Laufs nennt Ihnen die Smartchat-Umgebung, den Space und die Collection, in die geschrieben wird. Prüfen Sie diese Angaben. Es gibt keine Rückfrage, bevor der Upload beginnt, und bereits vorhandene Dateien werden nicht automatisch ersetzt.

## [Was mit jeder Datei passiert](https://docs.smartchat.ai.t-systems.net/de/user/admin/uploading-many-files/#was-mit-jeder-datei-passiert)

Das Skript erledigt pro Datei dieselben drei Schritte, die Sie auch von Hand in der Oberfläche ausführen würden:

1. Es **lädt** die Datei in den Speicher des Space hoch.
2. Es **wartet**, bis der Upload abgeschlossen ist.
3. Es **beauftragt Smartchat mit der Verarbeitung** — dabei wird der Text ausgelesen, in kleine durchsuchbare Abschnitte zerlegt und Ihrer Collection hinzugefügt.

Danach ist nichts weiter zu tun. Die Zuordnung zur Collection ist Teil des Verarbeitungsauftrags; es gibt also keinen separaten Schritt, um die hochgeladenen Dateien in Ihre Collection zu legen.

## [Ergebnis prüfen](https://docs.smartchat.ai.t-systems.net/de/user/admin/uploading-many-files/#ergebnis-pr%C3%BCfen)

Öffnen Sie die Collection unter **Workspace → Collection** und laden Sie die Seite neu. Ihre Dateien sollten dort aufgeführt sein.

Falls noch nicht alle sichtbar sind, warten Sie einen Moment und laden Sie erneut — die Dateien werden von einem Hintergrundprozess in die Collection eingetragen, daher liegt zwischen dem Ende des Skripts und der vollständigen Anzeige oft eine kurze Verzögerung.

## [Warum eine Datei übersprungen werden kann](https://docs.smartchat.ai.t-systems.net/de/user/admin/uploading-many-files/#warum-eine-datei-%C3%BCbersprungen-werden-kann)

Smartchat vermeidet es, dasselbe Dokument doppelt zu speichern; manche Dateien werden deshalb bewusst nicht hochgeladen. Das ist der häufigste Grund, warum ein Lauf so wirkt, als sei nichts passiert:

| Meldung des Skripts | Bedeutung | Was zu tun ist |
| - | - | - |
| `DUPLICATED` | Eine Datei mit demselben Namen **und** demselben Inhalt liegt bereits in diesem Ordner des Space | Nichts — sie ist bereits vorhanden |
| `EXISTS` | Eine Datei mit demselben Namen ist vorhanden, ihr Inhalt unterscheidet sich aber | Mit `--overwrite` ersetzen |
| Es passiert scheinbar nichts | Die Datei wurde bereits hochgeladen und verarbeitet | Der Inhalt muss sich von der vorhandenen Fassung unterscheiden |

Wenn Sie testen und möchten, dass eine Datei jedes Mal durchläuft, ändern Sie **sowohl den Namen als auch den Inhalt**.

## [Wenn etwas schiefgeht](https://docs.smartchat.ai.t-systems.net/de/user/admin/uploading-many-files/#wenn-etwas-schiefgeht)

Schlägt eine Datei fehl, läuft das Skript weiter und meldet die Fehler am Ende — eine einzelne problematische Datei stoppt also nicht den Rest.

Taucht eine Datei gar nicht auf, öffnen Sie die Collection unter **Arbeitsbereich → Kollektion**: Dort ist jede Datei mit ihrem aktuellen Status aufgeführt. [Fehler bei der Dateiverarbeitung](https://docs.smartchat.ai.t-systems.net/de/user/files/ingestion-errors/) erklärt die einzelnen Status und ihre Ursachen. Für sehr große Dateien gelten eigene Regeln, beschrieben unter [Maximale Dateigröße](https://docs.smartchat.ai.t-systems.net/de/user/files/file-size-limits/).

Außerdem sollten Sie wissen:

- **Dateien aus Unterordnern verlieren ihren Ordner.** Es wird nur der Dateiname übertragen; `berichte/zusammenfassung.pdf` und `archiv/zusammenfassung.pdf` werden also zu zwei Dateien mit demselben Namen, und die zweite gilt als Dublette oder Konflikt. Laden Sie solche Ordner nacheinander hoch und trennen Sie sie mit `--folder-path`.
- **Ein erneuter Lauf ist nicht kostenlos.** Ein weiterer Verarbeitungsauftrag erzeugt immer neue Arbeit, selbst wenn die Datei selbst übersprungen wird. Starten Sie einen großen Stapel nicht neu, nur um einzelne Fehlschläge nachzuholen — legen Sie die betroffenen Dateien stattdessen in einen eigenen Ordner.
- **Das Skript abzubrechen ist unbedenklich.** Bereits hochgeladene Dateien bleiben erhalten und werden fertig verarbeitet. Es bleibt nichts halb geschrieben zurück.

## [Alle Optionen](https://docs.smartchat.ai.t-systems.net/de/user/admin/uploading-many-files/#alle-optionen)

| Option | Standard | Wirkung |
| - | - | - |
| `--folder` | — | Der Ordner, aus dem hochgeladen wird (erforderlich) |
| `--space-id` | — | Der Space, in den hochgeladen wird (erforderlich) |
| `--collection-id` | — | Die Collection, in die die Dateien kommen (erforderlich) |
| `--glob` | alles | Welche Dateien ausgewählt werden, als Muster. Versteckte Dateien werden immer übersprungen |
| `--dry-run` | — | Dateien auflisten und beenden, ohne hochzuladen |
| `--list-spaces` | — | Ihre Spaces mit IDs anzeigen und beenden |
| `--overwrite` | aus | Vorhandene Dateien mit abweichendem Inhalt ersetzen |
| `--folder-path` | — | Die Dateien in einen benannten Ordner im Space legen |
| `--gateway` | `SMARTCHAT_GATEWAY` | Die Adresse des API-Gateways Ihrer Smartchat-Installation (erforderlich, sofern die Umgebungsvariable nicht gesetzt ist) |
| `--scope` | `space` | `space` (geteilt) oder `private` (nur für Sie) |
| `--batch-size` | `10` | Wie viele Dateien pro Upload-Anfrage gesendet werden |
| `--ingestion-config-id` | — | Eine feste Verarbeitungskonfiguration für alle Dateien verwenden |
| `-v` | — | Ausführliche Ausgabe, hilfreich beim Melden von Problemen |

Sie können Ihr Passwort in der Umgebungsvariablen `SMARTCHAT_PASSWORD` hinterlegen, um es nicht bei jedem Lauf eingeben zu müssen. Dort abgelegte Werte sind für andere Programme auf Ihrem Rechner sichtbar — geben Sie das Passwort daher besser bei Nachfrage ein.

## [Für Entwicklerinnen und Entwickler](https://docs.smartchat.ai.t-systems.net/de/user/admin/uploading-many-files/#f%C3%BCr-entwicklerinnen-und-entwickler)

Das Skript ist ein ausgearbeitetes Beispiel für die Datei-API und ausdrücklich zum Anpassen gedacht. Es nutzt nur die Python-Standardbibliothek und `httpx`, deklariert als [Inline Script Metadata](https://packaging.python.org/en/latest/specifications/inline-script-metadata/), sodass `uv run` die Abhängigkeit ohne Projekt auflöst. Jeder Schritt ist eine eigene Methode, der Endpunkt jeweils darüber dokumentiert.

Die Aufrufe in ihrer Reihenfolge:

| Schritt | Aufruf |
| - | - |
| Anmelden | `POST /api/v1/auth/user` |
| Aktiven Space setzen | `GET /user-manager/api/v1/spaces/switch?space_id=`, danach erneut anmelden |
| Hochladen | `POST /file-manager/api/v1/files/?file_scope=space` |
| Auf Speicherung warten | `GET /file-manager/api/v1/files/{file_id}`, bis `status` gleich `uploaded` ist |
| Verarbeitungskonfiguration ermitteln | `GET /config-manager/api/v1/space/ingestion/config?file_id=` |
| Verarbeitung beauftragen | `POST /ingest-master/api/v1/task` mit `collectionId` |
| Warten | `GET /ingest-master/api/v1/task/{id}`, bis `status` gleich `ingested` ist |

Drei Fallstricke:

- **Nach dem Space-Wechsel erneut anmelden.** Der aktive Space steckt im Access Token; ein vor dem Wechsel ausgestelltes Token zeigt weiterhin auf den alten Space. Das Gateway setzt die Header `x-active-space-id`, `x-user-id` und `x-active-permissions` aus Ihrem Token — setzen Sie sie niemals selbst. Aus demselben Grund ist ein Space-Wechsel im Browser während eines Laufs gefährlich.
- **Das erste Pfadsegment ist ein Gateway-Service-Key, kein Repository-Name.** `file-manager` führt zu aifs-files-management. Ein falscher Key liefert `404 Service not registered` — das sieht nach einem leeren Ergebnis aus, ist aber eine falsche URL.
- **`collectionId` im Verarbeitungsauftrag genügt.** Damit landet die Datei sowohl für die Suche als auch in der Chat-Oberfläche in der Collection. `PUT /ingest-master/api/v1/files` dient dazu, Dateien nachträglich zu reparieren, die *ohne* Collection verarbeitet wurden; für neue Dateien wird es nicht benötigt.

Die vollständigen API-Definitionen werden pro Service veröffentlicht und sind die maßgebliche Referenz:

```plaintext
https://<gateway-host>/file-manager/api/v1/openapi.json
https://<gateway-host>/ingest-master/api/v1/openapi.json
https://<gateway-host>/config-manager/api/v1/openapi.json
https://<gateway-host>/user-manager/api/v1/openapi.json
```

Die browsbaren Fassungen unter `/file-manager/redoc` beziehen ihre Inhalte aus genau diesen Dateien.
