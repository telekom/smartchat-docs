# Connectors verwalten

Source: https://docs.smartchat.ai.t-systems.net/de/user/agents/managing-connectors/

> Wie MCP-Server als Connectors registriert werden und wie Anwendungsinhaber und Space Owner festlegen, wer sie in einem Space nutzen darf.

> **Preview**
>
> Der Agenten-Modus und MCP-Connectors sind derzeit nur als Preview verfügbar. Wenn Sie diese Funktionen testen möchten, wenden Sie sich bitte an Ihren Ansprechpartner bei T-Systems.

Connectors bringen MCP-Server in Smartchat. Bis einer verfügbar ist, sind zwei Schritte nötig:

1. Der MCP-Server wird für die gesamte Instanz **registriert**. Das übernehmen die Betreiber von Smartchat. Um einen Server hinzuzufügen, wenden Sie sich mit dessen URL an Ihren Ansprechpartner bei T-Systems.
2. In jedem Space legt ein Anwendungsinhaber oder Space Owner fest, **wer den Connector nutzen darf**.

Benutzer können niemals selbst MCP-Server hinzufügen. Jeder Connector wird von einem Administrator freigegeben, sodass Ihre Organisation entscheidet, mit welchen Systemen Smartchat spricht.

## [Einen MCP-Server registrieren](https://docs.smartchat.ai.t-systems.net/de/user/agents/managing-connectors/#einen-mcp-server-registrieren)

Ein Connector braucht einen **Name** und die **URL** des Servers sowie optional eine **Beschreibung**, die Benutzer sehen. Ein API-Schlüssel oder Passwort wird nicht eingegeben.

*\[Image: Dialog Connector hinzufügen mit Name und URL]*

Mit **Connector bereitstellen** ermittelt Smartchat die Anmelde-Endpunkte des Servers und registriert sich dort selbst als OAuth-Client (Dynamic Client Registration). Das Client-Secret wird im Secret Store von Smartchat abgelegt. Danach meldet sich jeder Benutzer beim [Verbinden](https://docs.smartchat.ai.t-systems.net/de/user/agents/connectors/) mit seinem eigenen Konto am Server an.

Der Server muss daher OAuth 2.1 mit Authorization Code Flow, PKCE und Dynamic Client Registration unterstützen.

*\[Image: Bereitgestellter Connector mit Endpunkten, Client-ID und Scopes]*

Ein neuer Connector ist für alle in jedem Space nutzbar, bis der Zugriff pro Space eingeschränkt wird.

### [Die Registrierung erneuern](https://docs.smartchat.ai.t-systems.net/de/user/agents/managing-connectors/#die-registrierung-erneuern)

**Sync** registriert Smartchat erneut beim Server und erzeugt einen neuen Client. Alle Benutzer, die sich verbunden hatten, werden getrennt und müssen sich bei der nächsten Nutzung des Connectors erneut verbinden.

*\[Image: Dialog Connector synchronisieren mit dem Hinweis, dass alle bisherigen Verbindungen getrennt werden]*

## [Festlegen, wer einen Connector nutzen darf](https://docs.smartchat.ai.t-systems.net/de/user/agents/managing-connectors/#festlegen-wer-einen-connector-nutzen-darf)

Anwendungsinhaber und Space Owner steuern den Zugriff pro Space unter **Arbeitsbereich → Connectors**. Die Seite listet jeden registrierten Connector mit drei Optionen:

| Option | Wer den Connector in diesem Space nutzen darf |
| - | - |
| **Öffentlich** | Jedes Mitglied des Spaces. Das ist die Voreinstellung. |
| **Administrator** | Nur Anwendungsinhaber. |
| **Gruppe** | Mitglieder der ausgewählten [Gruppen](https://docs.smartchat.ai.t-systems.net/de/user/concepts/groups/). |

*\[Image: Reiter Connectors im Arbeitsbereich mit den Optionen Öffentlich, Administrator und Gruppe]*

Space Owner können das für die Spaces tun, deren Owner sie sind. Anwendungsinhaber können es für jeden Space tun, dem sie angehören. Die Einstellung gilt für den Space, der im Space-Selector ausgewählt ist.
