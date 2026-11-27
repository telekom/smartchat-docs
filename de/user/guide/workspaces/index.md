# Arbeitsbereich & Kollaboration

Source: https://docs.smartchat.ai.t-systems.net/de/user/guide/workspaces/

> Arbeitsbereich verstehen, navigieren, Berechtigungen vergeben, Kollektionen und Assistenten erstellen.

> **Siehe auch**
>
> Es empfiehlt sich, zunächst die Konzeptseite [Arbeitsbereich](https://docs.smartchat.ai.t-systems.net/de/user/concepts/workspace/) zu lesen, um zu verstehen, was ein Arbeitsbereich ist und wie er mit Spaces zusammenhängt.

## [Im Arbeitsbereich navigieren](https://docs.smartchat.ai.t-systems.net/de/user/guide/workspaces/#im-arbeitsbereich-navigieren)

Der Arbeitsbereich wird über **“Arbeitsbereich”** auf der linken Seite geöffnet.

*\[Image: Arbeitsbereich-Button im Navigationsmenü]*

Der Arbeitsbereich ist in der oberen Leiste nach den verschiedenen Ressourcen aufgeteilt: **Assistenten**, **Wissen**, **Prompts**. Über den jeweiligen Reiter können die Elemente erstellt, bearbeitet und konfiguriert werden. Anwendungsinhaber und Space Owner sehen zusätzlich den Reiter **Connectors**, in dem sie festlegen, wer im Space welchen [Connector](https://docs.smartchat.ai.t-systems.net/de/user/agents/managing-connectors/#festlegen-wer-einen-connector-nutzen-darf) nutzen darf.

*\[Image: Arbeitsbereich mit Reitern Assistenten, Wissen, Prompts]*

## [Teilen](https://docs.smartchat.ai.t-systems.net/de/user/guide/workspaces/#teilen)

Alles, was Sie im Arbeitsbereich anlegen, startet als **Nur Sie**. Klicken Sie in der Kopfzeile eines Elements auf **Teilen**, um es mit Gruppen (**Kann verwenden** oder **Kann bearbeiten**) oder mit allen im Space zu teilen. Siehe [Zugriffskontrolle](https://docs.smartchat.ai.t-systems.net/de/user/concepts/access-control/).

## [Kollektionen anlegen](https://docs.smartchat.ai.t-systems.net/de/user/guide/workspaces/#kollektionen-anlegen)

Lokale Kollektionen können manuell über den Reiter **“Wissen”** erstellt, bearbeitet und durchsucht werden. Auf bestehende Kollektionen kann innerhalb eines Chats mit der **Raute (#)** verwiesen werden. Außerdem können Kollektionen als Kontext bei einem Assistenten hinterlegt werden.

Schalten Sie **Vertraulich** für eine Kollektion ein, deren Inhalt auf Telekom-gehosteten Modellen bleiben muss. Jeder Chat, der sie verwendet, wird zu einem vertraulichen Chat. Siehe [Mit vertraulichen Daten arbeiten](https://docs.smartchat.ai.t-systems.net/de/user/guide/confidential-data/).

*\[Image: Kollektionen im Chat mit #-Shortcut]*

## [Assistenten erstellen und nutzen](https://docs.smartchat.ai.t-systems.net/de/user/guide/workspaces/#assistenten-erstellen-und-nutzen)

Unter “Assistenten” werden Konfigurationen verstanden, die für bestimmte Anwendungsfälle ausgelegt sind. Ein existierendes LLM wird mit Wissen und einer Systemaufforderung verfeinert und in der Organisation geteilt, sodass es für regelmäßig auftretende Aufgaben genutzt werden kann (z.B. E-Mails zusammenfassen und beantworten unter Einhaltung von Konzernrichtlinien).

Erstellte Assistenten können im Chat über die Dropdown-Liste ausgewählt werden — genauso wie die Basismodelle.

*\[Image: Assistenten-Reiter im Arbeitsbereich]*

Über den Reiter **“Assistenten”** können Assistenten erzeugt und bearbeitet werden:

- **Plus-Symbol** — neuen Assistenten hinzufügen
- **Bleistift-Symbol** — bestehenden Assistenten bearbeiten
- **Schalter** — Assistent in der Dropdown-Liste (de-)aktivieren

Wer einen Assistenten im Chat verwenden und wer ihn auch bearbeiten kann, legen Sie beim [Teilen](https://docs.smartchat.ai.t-systems.net/de/user/concepts/access-control/) fest.

Beim Erstellen wird dem Assistenten ein **Name**, eine **Beschreibung** und ein **Basismodell** zugewiesen. Die **Systemaufforderung** ist neben dem hinterlegten Wissen das mächtigste Werkzeug und legt die allgemeine Handlungsweise des Assistenten fest. Kollektionen müssen zuvor über den Reiter “Wissen” angelegt worden sein. **Prompt-Vorschläge** ermöglichen eine schnelle und intuitive Nutzung.

Ein Assistent, der eine [vertrauliche Kollektion](https://docs.smartchat.ai.t-systems.net/de/user/concepts/confidentiality/) verwendet, muss auf einem Telekom-gehosteten Basismodell laufen. Sobald eine vertrauliche Kollektion angehängt ist, bietet der Editor nur noch solche an.

*\[Image: Bearbeitungsansicht für einen Assistenten]*

*\[Image: Weitere Assistenten-Parameter: Werkzeuge, Filter, Aktionen, Fähigkeiten]*

## [Prompt-Vorlagen kreieren und einbinden](https://docs.smartchat.ai.t-systems.net/de/user/guide/workspaces/#prompt-vorlagen-kreieren-und-einbinden)

Prompt-Vorlagen sind Blaupausen für Prompts. Sie können im Arbeitsbereich unter **“Prompts”** erstellt und bearbeitet werden. Über das **Plus-Symbol** wird eine neue Vorlage hinzugefügt. Wie Assistenten und Kollektionen teilen Sie sie über **Teilen**.

Prompt-Vorlagen erhalten einen **Titel**, darunter wird der Befehl (Prompt) eingetragen. Variablen für später auszufüllende Werte werden mit geschweiften Klammern deklariert, z.B. `Schreibe eine E-Mail an {{Name}}.` Eingebaute Variablen wie `{{CURRENT_DATE}}` füllen sich selbst aus, siehe [Prompt-Variablen](https://docs.smartchat.ai.t-systems.net/de/user/guide/prompt-variables/).

*\[Image: Plus-Button für neue Prompt-Vorlage]*

*\[Image: Bearbeitungsansicht einer Prompt-Vorlage]*

Bestehende Vorlagen können innerhalb eines Chats aufgerufen werden, indem im Chat der **Schrägstrich (/)** eingegeben und die gewünschte Vorlage aus dem Dialogfenster ausgewählt wird. Platzhalter können dann mit konkreten Werten gefüllt werden.

> **Tipp**
>
> Aktualisieren Sie mehrere Variablenfelder nacheinander, indem Sie nach jedem Einsetzen die Tabulatortaste im Eingabefeld drücken.

*\[Image: Prompt-Vorlagen-Auswahl mit /-Shortcut]*
