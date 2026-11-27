# Vertraulichkeit

Source: https://docs.smartchat.ai.t-systems.net/de/user/concepts/confidentiality/

> Wie Smartchat vertrauliche Daten in der Telekom-gehosteten Infrastruktur hält und was sich ändert, wenn eine Kollektion, ein Space oder ein Chat vertraulich ist.

**Vertraulichkeit** ist der eingebaute Schutz von Smartchat für Daten, die die sichere Smartchat-Umgebung nicht verlassen dürfen. Sobald Daten als vertraulich markiert sind, setzt Smartchat die Regeln für Sie durch: Vertrauliche Daten werden ausschließlich von Modellen verarbeitet, die T-Systems hostet, und jede Funktion, die sie an ein externes System senden würde, ist abgeschaltet. Sie müssen sich nicht merken, welches Modell oder welche Funktion sicher ist.

> **Kurz gesagt**
>
> - Markieren Sie eine **Kollektion** oder einen ganzen **Space** als vertraulich.
> - Jeder Chat, der diese Daten verwendet, wird zu einem **vertraulichen Chat** und bleibt es.
> - Ein vertraulicher Chat verwendet nur Telekom-gehostete Modelle (Telekom-**T**-Logo); Websuche, Tools und Teilen sind darin nicht verfügbar.

Eine Schritt-für-Schritt-Anleitung mit Screenshots finden Sie unter [Mit vertraulichen Daten arbeiten](https://docs.smartchat.ai.t-systems.net/de/user/guide/confidential-data/).

## [Wo Vertraulichkeit eingestellt wird](https://docs.smartchat.ai.t-systems.net/de/user/concepts/confidentiality/#wo-vertraulichkeit-eingestellt-wird)

### [Vertrauliche Kollektionen](https://docs.smartchat.ai.t-systems.net/de/user/concepts/confidentiality/#vertrauliche-kollektionen)

Jede [Kollektion](https://docs.smartchat.ai.t-systems.net/de/user/guide/workspaces/#kollektionen-anlegen) hat einen Schalter **Vertraulich**, der standardmäßig aus ist. Schalten Sie ihn beim Erstellen der Kollektion ein oder später in der Kopfzeile der Kollektion. Jeder, der die Kollektion bearbeiten kann, kann ihn ändern.

*\[Image: Kopfzeile einer Kollektion mit eingeschaltetem Schalter Vertraulich]*

Dateien haben keine eigene Vertraulichkeitsmarkierung: Eine Datei ist vertraulich, weil sie zu einer vertraulichen Kollektion gehört. Eine Datei, die Sie direkt in einen Chat hochladen, ist für sich genommen nicht vertraulich.

> **Vertrauliche Dokumente in eine vertrauliche Kollektion legen**
>
> Um ein Dokument zu schützen, fügen Sie es einer vertraulichen Kollektion hinzu und verwenden Sie die Kollektion in Ihren Chats. Ein direkt in einen Chat hochgeladenes Dokument ist nur geschützt, wenn der Chat bereits vertraulich ist, etwa weil sein Space vertraulich ist.

### [Vertrauliche Spaces](https://docs.smartchat.ai.t-systems.net/de/user/concepts/confidentiality/#vertrauliche-spaces)

Ein Space Owner oder ein Anwendungsinhaber kann einen ganzen [Space](https://docs.smartchat.ai.t-systems.net/de/user/concepts/spaces/) mit dem Schalter **Vertrauliche Daten** als vertraulich markieren (siehe [Space-Einstellungen](https://docs.smartchat.ai.t-systems.net/de/user/admin/space-settings/#vertrauliche-daten)). Alle Daten in diesem Space werden dann als vertraulich behandelt, unabhängig von der Einstellung der einzelnen Kollektionen. Die Space-Einstellung kann den Schutz nur erweitern: Sie macht jede Kollektion im Space vertraulich, macht aber nie eine vertrauliche Kollektion nicht-vertraulich.

Ihr persönlicher **Mein Bereich** kann nicht als vertraulich markiert werden. Dort ergibt sich die Vertraulichkeit aus den Kollektionen, die Sie verwenden.

### [Vertrauliche Chats](https://docs.smartchat.ai.t-systems.net/de/user/concepts/confidentiality/#vertrauliche-chats)

Ein Chat wird vertraulich, sobald

- sein Space vertraulich ist,
- Sie eine vertrauliche Kollektion oder eine Datei daraus anhängen oder
- Sie einen [Assistenten](https://docs.smartchat.ai.t-systems.net/de/user/guide/workspaces/) auswählen, der eine vertrauliche Kollektion verwendet.

Smartchat wendet die Einschränkungen an, sobald Sie die Daten anhängen, also bevor Sie Ihre Nachricht senden. Ist ein Chat einmal vertraulich, **bleibt er vertraulich** – auch wenn Sie den Anhang wieder entfernen oder die Kollektion später nicht mehr als vertraulich markiert ist. Um ohne die Einschränkungen zu arbeiten, starten Sie einen neuen Chat ohne die vertraulichen Daten.

*\[Image: Chat-Eingabefeld mit angehängter vertraulicher Kollektion und dem Symbol für vertrauliche Chats]*

## [Vertrauliche Daten erkennen](https://docs.smartchat.ai.t-systems.net/de/user/concepts/confidentiality/#vertrauliche-daten-erkennen)

Vertrauliche Daten sind überall mit einem **Schild**-Symbol gekennzeichnet.

| Wo | Was Sie sehen |
| - | - |
| Arbeitsbereich → **Kollektion** | Ein Schild neben jeder vertraulichen Kollektion; ein Schalter **Vertraulich** in der Kopfzeile der Kollektion. |
| Kollektionsauswahl mit **#** im Chat | Ein Schild neben vertraulichen Kollektionen. |
| Anhänge im Eingabefeld und in gesendeten Nachrichten | Ein Schild auf jeder vertraulichen Kollektion oder Datei. |
| Chat-Eingabefeld | Ein Schild-Symbol neben dem Mikrofon. Beim Darüberfahren erscheint *„Vertraulicher Chat: Es sind nur von der Telekom gehostete Modelle verfügbar, damit Ihre Daten nicht an externe Anbieter gesendet werden.“* |
| Modellauswahl | Nur die von der Telekom gehosteten Modelle, mit dem Hinweis *„Vertrauliche Daten: nur Telekom-gehostete Modelle verfügbar.“* |
| Bereichsauswahl | Ein Bestätigungsdialog, wenn Sie aus einem Chat heraus einen vertraulichen Space öffnen. |

## [Was sich in einem vertraulichen Chat ändert](https://docs.smartchat.ai.t-systems.net/de/user/concepts/confidentiality/#was-sich-in-einem-vertraulichen-chat-%C3%A4ndert)

| Funktion | In einem vertraulichen Chat |
| - | - |
| **Modelle** | Nur Modelle, die T-Systems hostet, sind verfügbar. Extern gehostete Modelle sind in der Modellauswahl ausgeblendet. War ein extern gehostetes Modell ausgewählt, wechselt Smartchat zu einem Telekom-gehosteten Modell und meldet: *„Aufgrund von Vertraulichkeitsbeschränkungen wurde zu einem von der Telekom gehosteten Modell gewechselt.“* Ein zweites Modell mit **@** hinzuzufügen ist nicht möglich. |
| **Assistenten** | Ein Assistent, der eine vertrauliche Kollektion verwendet, muss auf einem Telekom-gehosteten Basismodell aufgebaut sein. Andernfalls wird er als nicht verfügbar angezeigt und kann nicht ausgewählt werden. |
| **[Websuche](https://docs.smartchat.ai.t-systems.net/de/user/guide/web-search/)** | Nicht verfügbar: *„Websuche ist in vertraulichen Chats nicht verfügbar“*. Die Websuche sendet Teile der Konversation an einen externen Suchanbieter. |
| **Tools** | Nicht verfügbar, da Tools Daten an externe Systeme weitergeben können. |
| **[Teilen, Klonen, Kopieren](https://docs.smartchat.ai.t-systems.net/de/user/guide/managing-chats/)** | Werden nicht angeboten, damit der Inhalt nicht außerhalb von Smartchat weitergegeben werden kann. |
| **Exportieren** | Bleibt verfügbar. Eine exportierte Datei liegt in Ihrer Verantwortung; behandeln Sie sie nach den Regeln Ihrer Organisation für vertrauliche Daten. |

Die Einschränkungen für Modelle und Websuche setzt Smartchat auch auf dem Server durch. Eine Anfrage, die in einem vertraulichen Chat ein extern gehostetes Modell verwenden will, wird abgelehnt, das Modell wird gewechselt, und Smartchat bittet Sie, Ihre Nachricht erneut zu senden.

Zukünftige Funktionen, die Daten an externe Systeme übertragen, werden durch denselben Mechanismus geschützt.

## [Wer die Vertraulichkeit einstellt](https://docs.smartchat.ai.t-systems.net/de/user/concepts/confidentiality/#wer-die-vertraulichkeit-einstellt)

| Ebene | Wer | Wo |
| - | - | - |
| Kollektion | Jeder, der die Kollektion [bearbeiten](https://docs.smartchat.ai.t-systems.net/de/user/concepts/access-control/) kann | Arbeitsbereich → **Kollektion** → die Kollektion → **Vertraulich** |
| Space | Space Owner | **Administration → Bereichsinhaber → Bereich → Vertrauliche Daten** ([Space-Einstellungen](https://docs.smartchat.ai.t-systems.net/de/user/admin/space-settings/#vertrauliche-daten)) |
| Space | Anwendungsinhaber | **Administration → Anwendungsinhaber → Bereiche** ([Anwendungsinhaber](https://docs.smartchat.ai.t-systems.net/de/user/admin/application-owner/)) |

Beide Schalter lassen sich wieder ausschalten. Chats, die bereits vertraulich sind, bleiben vertraulich.

## [Warum das wichtig ist](https://docs.smartchat.ai.t-systems.net/de/user/concepts/confidentiality/#warum-das-wichtig-ist)

Modelle, die T-Systems in der T-Cloud hostet (erkennbar am Telekom-**T**-Logo in der Modellauswahl), verarbeiten Daten innerhalb der sicheren Umgebung und sind für vertrauliche Daten freigegeben ([PSA DSK3-konform](https://docs.smartchat.ai.t-systems.net/de/user/glossary/)). Extern gehostete Modelle, Websuche und ähnliche Funktionen leiten Daten über die Infrastruktur externer Anbieter. Die Vertraulichkeit stellt sicher, dass Daten, die den höchsten Schutz erfordern, innerhalb der sicheren Grenze bleiben – ohne dass sich jeder Benutzer jedes Mal richtig entscheiden muss.
