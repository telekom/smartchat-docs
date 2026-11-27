# Berechtigungen

Source: https://docs.smartchat.ai.t-systems.net/de/user/concepts/permissions/

> Was Berechtigungen erlauben, wo sie gesetzt werden und wie sie zusammenwirken.

Auf welche Elemente ein Mitglied eines [Space](https://docs.smartchat.ai.t-systems.net/de/user/concepts/spaces/) zugreifen kann, regelt die [Zugriffskontrolle](https://docs.smartchat.ai.t-systems.net/de/user/concepts/access-control/). Berechtigungen regeln, welche Funktionen es im Space nutzen und welche Aktionen es ausführen kann, etwa die Websuche nutzen, Agenten bauen, Dateien in Chats hochladen oder Elemente mit allen im Space teilen.

Wie sich Rollen, Berechtigungen und Zugriffskontrolle unterscheiden, steht unter [Rollen, Berechtigungen & Zugriffskontrolle](https://docs.smartchat.ai.t-systems.net/de/user/concepts/roles-permissions-access-control/).

Die [Standardberechtigungen](https://docs.smartchat.ai.t-systems.net/de/user/concepts/permissions/#standardberechtigungen) des Space legen fest, mit welchen Berechtigungen eine neue [Gruppe](https://docs.smartchat.ai.t-systems.net/de/user/concepts/groups/) startet. Berechtigungen gelten nur in ihrem Space.

## [Alle Berechtigungen](https://docs.smartchat.ai.t-systems.net/de/user/concepts/permissions/#alle-berechtigungen)

Der Reiter **Berechtigungen** einer Gruppe hat diese Berechtigungen. Die Spalte **Standard** zeigt den Wert in einem neuen Space.

| Berechtigung | Erlaubt | Standard |
| - | - | - |
| **Arbeitsbereichsberechtigungen** | | |
| **Modellverwaltung** | Assistenten anlegen | Aus |
| **Kollektionsverwaltung** | Kollektionen anlegen | Aus |
| **Promptverwaltung** | Prompts anlegen | Aus |
| **Agentenverwaltung**\* | Agenten bauen | Aus |
| **Verwaltung eigener Gruppen** | Gruppen anlegen und die Mitglieder selbst angelegter Gruppen verwalten | Aus |
| **Freigabeberechtigungen** | | |
| **Modelle öffentlich teilen** | Assistenten mit allen im Space teilen | Aus |
| **Wissensspeicher öffentlich teilen** | Kollektionen mit allen im Space teilen | Aus |
| **Prompts öffentlich teilen** | Prompts mit allen im Space teilen | Aus |
| **Agenten öffentlich teilen**\* | Agenten mit allen im Space teilen | Aus |
| **Chat-Berechtigungen** | | |
| **Hochladen von Dateien erlauben** | Dateien an Chatnachrichten anhängen | An |
| **Chat-Steuerung erlauben**\* | Die Chat-Steuerung öffnen, etwa Systemprompt und Modellparameter | Aus |
| **Sprache-zu-Text erlauben** | Nachrichten per Sprache diktieren | An |
| **Text-zu-Sprache erlauben** | Antworten vorlesen lassen | An |
| **Benutzer-Feedback**\* | Feedback zu Antworten geben | Aus |
| **Mehrere Modelle im Chat erlauben** | Mehrere Modelle nebeneinander in einem Chat nutzen | An |
| **Temporäre Chats erlauben** | Chats führen, die nicht gespeichert werden | An |
| **Funktionen-Berechtigungen** | | |
| **Deep Dive**\* | Deep Dive nutzen | Aus |
| **Websuche**\* | Die Websuche nutzen | Aus |
| **Kritische Berechtigungen** | | |
| **Gruppenverwaltung** | Alle Gruppen im Space verwalten, wie ein Space Owner | Aus |

\* Erscheint nur, wenn die Funktion in Ihrem Smartchat verfügbar ist.

Eigene Chats zu löschen und zu bearbeiten braucht keine Berechtigung: Das können alle Mitglieder immer.

## [Regeln](https://docs.smartchat.ai.t-systems.net/de/user/concepts/permissions/#regeln)

Regeln schränken ein, was Mitglieder tun können, statt etwas zu erlauben.

- **Temporären Chat erzwingen:** Alle Chats der Mitglieder der Gruppe sind temporär und werden nicht gespeichert. Space Owner sind ausgenommen.

## [Standardberechtigungen](https://docs.smartchat.ai.t-systems.net/de/user/concepts/permissions/#standardberechtigungen)

Neben seinen Gruppen hat jeder Space **Standardberechtigungen**, die für alle seine Mitglieder gelten. Sie stehen unter **Bereichsinhaber → Gruppen → Standardberechtigungen**.

> **Nur für Anwendungsinhaber**
>
> Nur Anwendungsinhaber können die Standardberechtigungen sehen und ändern. Space Owner können das auch in ihrem eigenen Space nicht.

In einem neuen Space gelten die Werte aus der Spalte **Standard** unter [Alle Berechtigungen](https://docs.smartchat.ai.t-systems.net/de/user/concepts/permissions/#alle-berechtigungen).

Eine neue Gruppe startet mit den Standardberechtigungen, die bei ihrer Erstellung gelten. Bestehende Gruppen behalten ihre eigenen Einstellungen: Ist eine Berechtigung in einer bestehenden Gruppe aktiv, behalten ihre Mitglieder sie, auch wenn der Standard ausgeschaltet wird.

## [Wie Berechtigungen zusammenwirken](https://docs.smartchat.ai.t-systems.net/de/user/concepts/permissions/#wie-berechtigungen-zusammenwirken)

Eine Berechtigung ist für Sie aktiv, wenn sie in den Standardberechtigungen des Space oder in mindestens einer Ihrer Gruppen aktiv ist. Eine Gruppe kann eine Berechtigung nur erteilen, nie wegnehmen, was eine andere Gruppe erteilt.

Ben ist in den Gruppen Users, Vertrieb und Projekt. Eine Berechtigung ist für ihn an, sobald die Standardberechtigungen oder eine seiner Gruppen sie an haben: Die Websuche bekommt er über den Vertrieb. In der Gruppe Projekt ist das Hochladen von Dateien aus, das nimmt es ihm aber nicht weg, weil es in den Standardberechtigungen an ist. Deep Dive ist nirgends an, also auch für ihn nicht.

Es zählen nur Ihre Gruppen im aktiven Space.

## [Space Owner](https://docs.smartchat.ai.t-systems.net/de/user/concepts/permissions/#space-owner)

Space Owner haben jede Berechtigung ihres Space, ohne Mitglied einer Gruppe zu sein.
