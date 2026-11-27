# Eigene Agenten

Source: https://docs.smartchat.ai.t-systems.net/de/user/agents/custom-agents/

> Wer in einem Space eigene Agenten erstellen und teilen darf und wie Space Owner die Berechtigung vergeben.

> **Preview**
>
> Der Agenten-Modus und MCP-Connectors sind derzeit nur als Preview verfügbar. Wenn Sie diese Funktionen testen möchten, wenden Sie sich bitte an Ihren Ansprechpartner bei T-Systems.

Neben den Agenten, die Smartchat mitbringt, können Sie unter **Arbeitsbereich → Agenten → Neuer Agent** eigene Agenten erstellen, mit eigenen Anweisungen, Beispiel-Prompts und Connectors. Eigene Agenten stehen nur zur Verfügung, wenn die Betreiber von Smartchat sie für Sie freigeschaltet haben.

*\[Image: Agenten im Arbeitsbereich]*

*\[Image: Zugang für neue Agenten]*

## [Berechtigungen](https://docs.smartchat.ai.t-systems.net/de/user/agents/custom-agents/#berechtigungen)

Zwei Berechtigungen steuern eigene Agenten:

| Berechtigung | Zu finden unter | Erlaubt |
| - | - | - |
| **Agentenverwaltung** | **Arbeitsbereichsberechtigungen** | Eigene Agenten erstellen, bearbeiten und löschen. Ohne diese Berechtigung erscheint der Reiter **Agenten** im Arbeitsbereich nicht. |
| **Agenten öffentlich teilen** | **Freigabeberechtigungen** | Einen Agenten allen im Space zur Verfügung stellen. Um einen Agenten mit einzelnen Gruppen zu teilen, ist diese Berechtigung nicht nötig. |

Beide Berechtigungen sind in einem neuen Space aus. Wie jede [Berechtigung](https://docs.smartchat.ai.t-systems.net/de/user/concepts/permissions/) gelten sie nur in ihrem Space, und ein eigener Agent ist nur in dem Space verfügbar, in dem er erstellt wurde.

Space Owner haben in ihrem eigenen Space immer beide Berechtigungen, auch ohne Gruppe. Anwendungsinhaber haben sie in jedem Space, in dem sie zusätzlich eine Space-Rolle haben.

## [Die Berechtigung vergeben](https://docs.smartchat.ai.t-systems.net/de/user/agents/custom-agents/#die-berechtigung-vergeben)

Space Owner vergeben die Berechtigungen über [Gruppen](https://docs.smartchat.ai.t-systems.net/de/user/concepts/groups/) in ihrem Space:

1. Klicken Sie auf Ihr Profilbild und wählen Sie **Administration**.
2. Gehen Sie zu **Bereichsinhaber → Gruppen** und prüfen Sie, dass der richtige Space ausgewählt ist.
3. Klicken Sie auf eine Gruppe oder auf **Standardberechtigungen**, um die Berechtigung allen Mitgliedern des Space zu geben. **Standardberechtigungen** sehen nur Anwendungsinhaber.
4. Öffnen Sie den Reiter **Berechtigungen**.
5. Aktivieren Sie unter **Arbeitsbereichsberechtigungen** die Option **Agentenverwaltung**. Damit Agenten mit dem ganzen Space geteilt werden können, aktivieren Sie zusätzlich **Agenten öffentlich teilen** unter **Freigabeberechtigungen**.
6. Wenn Sie eine Gruppe bearbeitet haben, fügen Sie ihr im Reiter **Benutzer** die Benutzer hinzu, die Agenten erstellen sollen.

*\[Image: Agentenberechtigungen]*

Die beiden Schalter erscheinen nur, wenn eigene Agenten für Sie verfügbar sind. Wer einen fertigen Agenten verwenden oder bearbeiten kann, legen Sie beim [Teilen](https://docs.smartchat.ai.t-systems.net/de/user/concepts/access-control/) fest.
