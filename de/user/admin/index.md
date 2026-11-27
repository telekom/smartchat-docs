# Administration

Source: https://docs.smartchat.ai.t-systems.net/de/user/admin/

> Wie Anwendungsinhaber und Space Owner Spaces, Benutzer, Einstellungen und Datenverbindungen direkt in Smartchat verwalten.

Smartchat wird direkt in der App verwaltet. Die **Administration** deckt alles ab, was Anwendungsinhaber und Space Owner brauchen: Spaces und ihre Owner, Benutzer und ihre Rollen, die Einstellungen jedes Spaces (Vertraulichkeit, API-Schlüssel, Modelle) sowie die Datenverbindungen, die Inhalte in einen Space bringen. Reguläre Benutzer sehen sie nicht.

> **Das Legacy-Admin-Panel wird abgeschaltet**
>
> Alles, was das separate Admin-Panel unter `admin-panel.smartchat.ai.t-systems.net` konnte, ist jetzt Teil der **Administration** in Smartchat. Das Legacy-Admin-Panel wird Ende Oktober 2026 abgeschaltet.

## [Die Administration öffnen](https://docs.smartchat.ai.t-systems.net/de/user/admin/#die-administration-%C3%B6ffnen)

Klicken Sie unten links auf Ihr Profilbild und wählen Sie **Administration**. Der Eintrag wird nur Anwendungsinhabern und Space Ownern angezeigt.

*\[Image: Benutzermenü mit dem Eintrag Administration]*

Die Administration öffnet sich mit einer eigenen Navigation auf der linken Seite. Sie ist in einen Abschnitt pro Rolle gegliedert, und Sie sehen nur die Abschnitte, die Ihre Rolle Ihnen gibt:

| Abschnitt | Für | Was Sie dort tun |
| - | - | - |
| **Anwendungsinhaber** | Anwendungsinhaber | Alle [Spaces und Benutzer](https://docs.smartchat.ai.t-systems.net/de/user/admin/application-owner/) der Instanz verwalten sowie Einstellungen, die für die gesamte Instanz gelten (**Oberfläche**, **Codeausführung**). |
| **Bereichsinhaber** | Space Owner | Die [Mitglieder](https://docs.smartchat.ai.t-systems.net/de/user/admin/managing-space-members/) und Gruppen eines Spaces verwalten, seine [Einstellungen](https://docs.smartchat.ai.t-systems.net/de/user/admin/space-settings/) sowie seine [Confluence-](https://docs.smartchat.ai.t-systems.net/de/user/admin/confluence-sync/) und [S3-Quellen](https://docs.smartchat.ai.t-systems.net/de/user/admin/s3-autosync/). |

**Einstellung suchen** oben findet jede Seite der Administration über ihren Namen. **Zurück zum Chat** bringt Sie zu Ihren Chats zurück.

*\[Image: Administration mit den Abschnitten Anwendungsinhaber und Bereichsinhaber]*

## [Den Space auswählen](https://docs.smartchat.ai.t-systems.net/de/user/admin/#den-space-ausw%C3%A4hlen)

Alles unter **Bereichsinhaber** wirkt jeweils auf einen Space. Wählen Sie ihn oben im Abschnitt unter **Aktueller Bereich** aus. Um einen anderen Ihrer Spaces zu verwalten, wechseln Sie ihn dort.

*\[Image: Auswahl Aktueller Bereich im Abschnitt Bereichsinhaber]*

Der Abschnitt **Bereichsinhaber** enthält diese Seiten:

| Gruppe | Seiten |
| - | - |
| **Verwalten** | **Bereichsmitglieder**, **Feedback**, **Gruppen** |
| **Einstellungen** | **Modelle**, **Bereich**, **Datenverbindungen**, **S3 AutoSync**, **Websuche** |

> **Hinweis**
>
> **Datenverbindungen** und **S3 AutoSync** werden nur angezeigt, wenn die Integration in Ihrer Smartchat-Umgebung aktiviert ist. **Websuche** erscheint, wenn die Websuche pro Space konfigurierbar ist.

## [Wer hat Zugriff](https://docs.smartchat.ai.t-systems.net/de/user/admin/#wer-hat-zugriff)

- **Anwendungsinhaber**: sieht den Abschnitt **Anwendungsinhaber** und kann die Space-Einstellungen der Spaces öffnen, denen er angehört. **Bereichsmitglieder** erscheint nur für Spaces, die er zusätzlich besitzt: Mitglieder hinzufügen und entfernen bleibt Space Ownern vorbehalten.
- **Space Owner**: sieht den Abschnitt **Bereichsinhaber** für jeden Space, in dem er Space Owner ist. Andere Spaces lassen sich nicht verwalten.

Die vollständige Liste finden Sie unter [Rollen](https://docs.smartchat.ai.t-systems.net/de/user/concepts/roles/).
