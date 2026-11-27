# Spaces

Source: https://docs.smartchat.ai.t-systems.net/de/user/concepts/spaces/

> Wie Spaces funktionieren — Smartchats Mandantenfähigkeitsgrenze.

Ein **Space** ist Smartchats Mandantenfähigkeitsgrenze. Jede Ressource befindet sich in genau einem Space, und Ressourcen sind zwischen Spaces vollständig isoliert: Auf eine Entität in einem Space kann von einem anderen aus nicht zugegriffen werden, auch nicht vom selben Benutzer, dem sie gehört.

> **Mehrere Spaces sind eine bewusste Entscheidung**
>
> Legen Sie nicht einen Space pro Abteilung an. Häufig beginnt es mit einem Space pro Abteilung, und später zeigt sich, dass abteilungsübergreifend gearbeitet wird, in Projekten oder gemeinsamen Anfragen. Das lässt sich mit Spaces nicht abbilden, und dann ist eine Änderung aufwendig.
>
> Versuchen Sie immer zuerst, mit [Gruppen](https://docs.smartchat.ai.t-systems.net/de/user/concepts/groups/) *innerhalb* eines Space zu arbeiten. Für die tägliche Arbeit mit Abteilungen, Teams und Projekten ist das in der Regel der bessere Weg. Mit mehreren Spaces zu arbeiten hat Nachteile, die die einrichtenden Anwendungsinhaber und Space Owner kennen und tragen müssen:
>
> - **Keine Arbeit über Spaces hinweg.** Ein Chat, Assistent oder Agent greift nur auf die Daten des aktiven Space zu. Ein Projekt, das Dokumente aus zwei Spaces braucht, kann nicht beide nutzen.
> - **Immer nur ein Space.** Benutzer in mehreren Spaces haben nur Zugriff auf die Ressourcen des aktiven Space und müssen wissen, wo welche Daten liegen.
> - **Alles pro Space pflegen.** Mitglieder, Gruppen, Einstellungen und Datenanbindungen werden in jedem Space einzeln eingerichtet und gepflegt.
> - **Später nur mit Aufwand zu ändern.** Spaces später zusammenzuführen ist keine Standardfunktion, und Daten lassen sich nur im Ausnahmefall zwischen Spaces verschieben.
>
> Entscheiden Sie sich nur dann für mehrere Spaces, wenn eine strikte Trennung zwingend ist, wie unter [Wann mehrere Spaces sinnvoll sind](https://docs.smartchat.ai.t-systems.net/de/user/concepts/spaces/#wann-mehrere-spaces-sinnvoll-sind) beschrieben.

## [Was einem Space zugeordnet ist](https://docs.smartchat.ai.t-systems.net/de/user/concepts/spaces/#was-einem-space-zugeordnet-ist)

Folgendes ist pro Space isoliert:

- **Datei-Uploads**. Dateien sind pro Space isoliert; dieselbe physische Datei hat in verschiedenen Spaces separate Identitäten.
- **Kollektionen** (erstellt aus hochgeladenen Dateien)
- **Assistenten**
- **Prompt-Vorlagen**
- **Gruppen**
- **Konfiguration**
- **Verfügbare Modelle** (welche LLMs in der Modellauswahl erscheinen)
- **Chats**

Wenn Sie eine Datei in Space A hochladen, existiert sie nicht in Space B. Dasselbe gilt für jede andere der oben genannten Ressourcen.

Ein Benutzer hat nur Zugriff auf die Ressourcen des aktiven Space. Er kann nicht gleichzeitig auf Ressourcen mehrerer Spaces zugreifen.

## [Vertrauliche Spaces](https://docs.smartchat.ai.t-systems.net/de/user/concepts/spaces/#vertrauliche-spaces)

Ein Space kann von seinem Space Owner als vertraulich markiert werden. Jeder Chat in einem vertraulichen Space ist auf Telekom-gehostete Modelle beschränkt, und Funktionen, die Daten an externe Anbieter senden, sind abgeschaltet. Siehe [Vertraulichkeit](https://docs.smartchat.ai.t-systems.net/de/user/concepts/confidentiality/#vertrauliche-spaces).

## [Mitgliedschaft](https://docs.smartchat.ai.t-systems.net/de/user/concepts/spaces/#mitgliedschaft)

- Ein Benutzer kann Mitglied eines oder mehrerer Spaces sein.
- Ein Benutzer ist **jeweils nur in einem Space aktiv**.

## [Wann mehrere Spaces sinnvoll sind](https://docs.smartchat.ai.t-systems.net/de/user/concepts/spaces/#wann-mehrere-spaces-sinnvoll-sind)

Standard ist ein Space pro Organisation. Abteilungen, Teams und Projekte werden in diesem Space mit [Gruppen](https://docs.smartchat.ai.t-systems.net/de/user/concepts/groups/) abgebildet. Mehrere Spaces sind nur nötig, wenn Daten oder Administration strikt getrennt sein müssen:

- Gesetzliche oder Compliance-Vorgaben verlangen eine strikte Datentrennung, zum Beispiel zwischen den juristischen Personen eines Konzerns.
- Die Administration muss strikt getrennt sein: Die Space Owner einer Einheit dürfen die Mitglieder einer anderen nicht verwalten.

Arbeiten Nutzer einheitenübergreifend oder brauchen sie Daten aus mehreren Einheiten, verwenden Sie stattdessen Gruppen.

## [Default Space](https://docs.smartchat.ai.t-systems.net/de/user/concepts/spaces/#default-space)

Jede Smartchat-Instanz verfügt über einen **Default Space**, dem alle Benutzer angehören. Er kann nicht gelöscht oder umbenannt werden und ist in der Chat-Oberfläche nicht sichtbar.
