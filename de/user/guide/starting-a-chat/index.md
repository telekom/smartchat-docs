# Einen Chat starten

Source: https://docs.smartchat.ai.t-systems.net/de/user/guide/starting-a-chat/

> Neuen Chat öffnen, Modell auswählen und Eingaben machen.

## [Neuen Chat öffnen](https://docs.smartchat.ai.t-systems.net/de/user/guide/starting-a-chat/#neuen-chat-%C3%B6ffnen)

*\[Image: Chatfenster mit "Neuer Chat"-Button]*

Durch Klicken auf **“Neuer Chat”** auf der linken Leiste wird ein neuer (leerer) Chat gestartet. In jedem Chat kann ausgewählt werden, welches der verfügbaren Sprachmodelle verwendet werden soll. Neben einem einzeln ausgewählten Modell kann auch mit zwei oder mehr Modellen gleichzeitig in einem Multi-Modell-Chat interagiert werden, sodass die Antworten auf Eingabeprompts miteinander verglichen werden können.

## [Modell auswählen](https://docs.smartchat.ai.t-systems.net/de/user/guide/starting-a-chat/#modell-ausw%C3%A4hlen)

*\[Image: Modellauswahlmenü]*

Durch Klicken auf das **Dropdown-Menü**, in dem das aktuell ausgewählte Modell angezeigt wird, kann das Modell gewechselt werden. Zusätzlich zu den Basis-Modellen kann je nach Konfiguration auch auf [Assistenten](https://docs.smartchat.ai.t-systems.net/de/user/guide/workspaces/#assistenten-erstellen-und-nutzen) zugegriffen werden.

Jeder Nutzer hat eine individuelle Auswahl von Modellen, die sich aus der Kombination dieser Faktoren ergibt:

- Serving-Paket
- Space-Zugehörigkeit
- Die Assistenten, die im Space mit Ihnen geteilt sind

Die Modellnamen sind mit Visualisierungen versehen:

- **Logo** (vor dem Namen): Ist das Logo das Telekom-T, so wird das Modell von T-Systems AI Foundation Services in der T-Cloud gehostet. Diese Modelle sind am sichersten (PSA DSK3-konform für vertrauliche Daten). Modelle ohne T-Logo werden extern auf Hyperscalern gehostet, die nicht der direkten Kontrolle von T-Systems oder der Telekom unterliegen (z.B. Azure, GCP), und sollten nicht für besonders vertrauliche oder interne Dokumente verwendet werden. In einem [vertraulichen Chat](https://docs.smartchat.ai.t-systems.net/de/user/concepts/confidentiality/) werden nur Modelle mit T-Logo angeboten.
- **Landesflagge** (hinter dem Namen): Gibt an, in welchem Land das Modell gehostet wird.
- **Bild-Symbol** (hinter der Flagge): Es handelt sich um ein multimodales Modell, das neben Text auch Bilder verarbeiten kann.

## [Eingaben machen](https://docs.smartchat.ai.t-systems.net/de/user/guide/starting-a-chat/#eingaben-machen)

### [Manuelle Anfragen (Prompts) schreiben](https://docs.smartchat.ai.t-systems.net/de/user/guide/starting-a-chat/#manuelle-anfragen-prompts-schreiben)

*\[Image: Prompt-Eingabe im Chatfenster]*

Ein manueller Prompt ist eine direkt verfasste Eingabe in die Chat-Oberfläche. Die Anfrage oder Aufforderung kann direkt in Textform geschrieben und mittels des Pfeil-Buttons oder der Enter-Taste abgeschickt werden.

### [Bearbeiten des Prompts](https://docs.smartchat.ai.t-systems.net/de/user/guide/starting-a-chat/#bearbeiten-des-prompts)

*\[Image: Bearbeiten-Symbol unter dem Prompt]*

Der Prompt kann mit dem **Bleistiftsymbol** bearbeitet werden. Die Antwort wird für den neuen Prompt neu generiert. Nach dem Bearbeiten wird der Prompt mittels “Senden” automatisch neu generiert.

### [Sprache in Text umwandeln](https://docs.smartchat.ai.t-systems.net/de/user/guide/starting-a-chat/#sprache-in-text-umwandeln)

Statt einen Prompt zu tippen, können Sie ihn einsprechen: Smartchat wandelt die Aufnahme in Text um.

1. Klicken Sie im Eingabefeld auf das **Mikrofon** (**Stimme aufnehmen**) und beginnen Sie zu sprechen.

   *\[Image: Das Mikrofon im Eingabefeld mit dem Tooltip Stimme aufnehmen]*

2. Beim ersten Mal fragt Ihr Browser, ob Smartchat das Mikrofon nutzen darf: Erlauben Sie es. Haben Sie es früher blockiert, erlauben Sie es in den Website-Einstellungen des Browsers wieder, die Sie über das Symbol neben der Adressleiste öffnen.

   *\[Image: Die Website-Einstellungen des Browsers mit der Mikrofon-Berechtigung auf Blockieren]*

3. Während der Aufnahme zeigt ein Zähler die verstrichene Zeit im Verhältnis zur Höchstdauer. Beenden Sie die Aufnahme, um sie im Eingabefeld in Text umwandeln zu lassen.

> **Aufnahmen enden nach etwa 10 Minuten**
>
> Eine Aufnahme endet bei 9:50 von selbst und wird wie gewohnt transkribiert. Ein längeres Diktat nehmen Sie in mehreren Teilen auf.

Für die Diktierfunktion werden ausschließlich von T-Systems auf der T-Cloud bereitgestellte Whisper-Modelle verwendet.

### [Dateien und Bildschirmaufnahmen hochladen](https://docs.smartchat.ai.t-systems.net/de/user/guide/starting-a-chat/#dateien-und-bildschirmaufnahmen-hochladen)

Das Hochladen von Dateien ermöglicht es, direkt mit eigenen Dokumenten zu interagieren. Dabei wird eine private Chat-Sitzung zwischen Nutzer, Smartchat und den hochgeladenen Dokumenten aufgebaut.

(TODO: Diese Einschränkung wird im Multitenancy-Update entfernt.)

Die hochgeladenen Dokumente sind nicht außerhalb des Chats verfügbar.

> **Vertrauliche Dokumente**
>
> Eine hochgeladene Datei hat keine eigene Vertraulichkeitsmarkierung. Um ein Dokument auf Telekom-gehosteten Modellen zu halten, fügen Sie es einer [vertraulichen Kollektion](https://docs.smartchat.ai.t-systems.net/de/user/guide/confidential-data/) hinzu und hängen Sie stattdessen die Kollektion an.

Über das **Plus-Symbol** im Chat-Fenster können Dateien vom Rechner hochgeladen oder ein Foto/Screenshot erstellt werden (je nach Endgerät bzw. Browser). Mittels Drag-and-Drop können Dateien ebenfalls in einen Chat gezogen werden.

*\[Image: Datei-Upload-Menü]*

*\[Image: Bildschirmaufnahme-Dialog]*
