# Prompt-Variablen

Source: https://docs.smartchat.ai.t-systems.net/de/user/guide/prompt-variables/

> Platzhalter wie das heutige Datum oder Ihr Name, die sich in Prompt-Vorlagen und Ihrem persönlichen System-Prompt selbst ausfüllen.

**Prompt-Variablen** sind Platzhalter in doppelten geschweiften Klammern, zum Beispiel `{{CURRENT_DATE}}`. Smartchat ersetzt sie durch einen aktuellen Wert. So bleiben eine [Prompt-Vorlage](https://docs.smartchat.ai.t-systems.net/de/user/guide/workspaces/#prompt-vorlagen-kreieren-und-einbinden) oder Ihr persönlicher System-Prompt aktuell, ohne dass Sie sie bearbeiten müssen.

## [Verfügbare Variablen](https://docs.smartchat.ai.t-systems.net/de/user/guide/prompt-variables/#verf%C3%BCgbare-variablen)

| Variable | Wird ersetzt durch | Prompt-Vorlagen | Persönlicher System-Prompt |
| - | - | :-: | :-: |
| `{{CURRENT_DATE}}` | Das heutige Datum, z. B. `2026-11-04` | ✓ | ✓ |
| `{{CURRENT_TIME}}` | Die aktuelle Uhrzeit, z. B. `14:05:09` (System-Prompt: `2:05:09 PM`) | ✓ | ✓ |
| `{{CURRENT_DATETIME}}` | Datum und Uhrzeit zusammen | ✓ | ✓ |
| `{{CURRENT_WEEKDAY}}` | Den Wochentag auf Englisch, z. B. `Wednesday` | ✓ | ✓ |
| `{{CURRENT_TIMEZONE}}` | Ihre Zeitzone, z. B. `Europe/Berlin` | ✓ | ✓ |
| `{{USER_NAME}}` | Ihren Anzeigenamen | ✓ | ✓ |
| `{{USER_LANGUAGE}}` | Ihre Oberflächensprache, z. B. `de-DE` | ✓ | ✓ |
| `{{USER_LOCATION}}` | Ihre Koordinaten, wenn Sie den Standortzugriff im Browser erlauben | ✓ | – |
| `{{CLIPBOARD}}` | Den Text in Ihrer Zwischenablage | ✓ | – |

Datum, Uhrzeit und Zeitzone stammen von Ihrem Gerät. Variablen müssen genau wie angegeben in Großbuchstaben geschrieben werden.

## [Variablen in Prompt-Vorlagen](https://docs.smartchat.ai.t-systems.net/de/user/guide/prompt-variables/#variablen-in-prompt-vorlagen)

1. Öffnen Sie **Arbeitsbereich → Prompts** und legen Sie eine neue Prompt-Vorlage an oder öffnen Sie eine bestehende.
2. Schreiben Sie die Variablen in den Prompt-Inhalt. Jedes andere Wort in doppelten geschweiften Klammern, etwa `{{empfaenger}}`, ist eine Lücke, die Sie bei jeder Verwendung der Vorlage selbst ausfüllen.
3. Tippen Sie im Chat **/** gefolgt vom Befehl der Vorlage und wählen Sie die Vorlage aus.

Die Variablen werden ausgefüllt, sobald Sie die Vorlage auswählen, und der Text erscheint im Eingabefeld. Die erste Lücke ist markiert, sodass Sie sie direkt überschreiben können. Mit der **Tab**-Taste springen Sie zur nächsten Lücke. Prüfen Sie den Text und senden Sie ihn dann ab.

Beispielvorlage:

```text
Schreibe ein kurzes Status-Update für {{empfaenger}} mit Stand {{CURRENT_DATE}}. Unterschreibe mit {{USER_NAME}}.
```

> **Hinweis**
>
> - Eine Lücke, die Sie nicht ausfüllen, wird unverändert samt geschweiften Klammern an das Modell gesendet.
> - Bei `{{CLIPBOARD}}` und `{{USER_LOCATION}}` fragt Ihr Browser eventuell nach einer Berechtigung. Haben Sie ein Bild kopiert, wird es zusätzlich an die Nachricht angehängt.

## [Variablen im persönlichen System-Prompt](https://docs.smartchat.ai.t-systems.net/de/user/guide/prompt-variables/#variablen-im-pers%C3%B6nlichen-system-prompt)

Variablen funktionieren auch in Ihrem persönlichen System-Prompt unter **Einstellungen → Allgemein → System-Prompt (Erweitert)**. Sie werden bei jeder gesendeten Nachricht neu ausgefüllt, sodass das Modell immer die aktuellen Werte sieht.

> **Achtung**
>
> Im persönlichen System-Prompt wird jede Variable nur an der Stelle ersetzt, an der sie zum ersten Mal vorkommt. Verwenden Sie jede Variable höchstens einmal.

Lücken wie `{{empfaenger}}` sowie `{{CLIPBOARD}}` und `{{USER_LOCATION}}` werden hier nicht ausgefüllt.

## [Wo Variablen nicht ersetzt werden](https://docs.smartchat.ai.t-systems.net/de/user/guide/prompt-variables/#wo-variablen-nicht-ersetzt-werden)

- **System-Prompts von Assistenten:** Der System-Prompt eines [Assistenten](https://docs.smartchat.ai.t-systems.net/de/user/guide/workspaces/#assistenten-erstellen-und-nutzen) wird genau so an das Modell gesendet, wie er geschrieben ist. Variablen darin bleiben unverändert.
- **Prompt-Vorschläge** auf dem Startbildschirm: Hier wird nur `{{CLIPBOARD}}` ausgefüllt.

> **Tipp**
>
> Smartchat teilt dem Modell in jedem Chat das heutige Datum mit. `{{CURRENT_DATE}}` ist also nicht nötig, nur damit das Modell das Datum kennt.
