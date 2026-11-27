# Deep Dive

Source: https://docs.smartchat.ai.t-systems.net/de/user/guide/deep-dive/

> So nutzen Sie die Deep-Dive-Recherchefunktion in Smartchat.

**Deep Dive** ist der tiefgehende Recherchemodus von Smartchat, vergleichbar mit dem, was andere KI-Chatbots als “Deep Research” bezeichnen. Anstelle einer einzelnen Modellantwort startet Deep Dive einen mehrstufigen Recherche-Agenten, der die Dokumente Ihres Spaces durchsucht, die Ergebnisse zusammenfasst und einen strukturierten Bericht mit Quellenangaben erstellt.

## [Voraussetzungen](https://docs.smartchat.ai.t-systems.net/de/user/guide/deep-dive/#voraussetzungen)

Space User brauchen die [Berechtigung](https://docs.smartchat.ai.t-systems.net/de/user/concepts/permissions/) **Deep Dive**, gesetzt an einer ihrer Gruppen unter **Bereichsinhaber → Gruppen**. Space Owner haben sie in ihrem Space auch ohne Gruppe.

## [So funktioniert Deep Dive](https://docs.smartchat.ai.t-systems.net/de/user/guide/deep-dive/#so-funktioniert-deep-dive)

### [Nur in Spaces verfügbar](https://docs.smartchat.ai.t-systems.net/de/user/guide/deep-dive/#nur-in-spaces-verf%C3%BCgbar)

Deep Dive funktioniert innerhalb eines **Spaces**. Der Agent durchsucht alle Dokumente in dem Space, den Sie aktuell geöffnet haben. Sie können nicht einschränken, welche Dokumente verwendet werden; es wird immer die gesamte Space-Wissensbasis durchsucht. Wenn Sie Antworten aus einer anderen Wissensbasis benötigen, wechseln Sie vor dem Start in den entsprechenden Space.

### [Ihre Einstellungen bleiben außen vor](https://docs.smartchat.ai.t-systems.net/de/user/guide/deep-dive/#ihre-einstellungen-bleiben-au%C3%9Fen-vor)

Modellauswahl, Reasoning-Tiefe und ein im Space konfigurierter System-Prompt haben keinen Einfluss auf einen Deep-Dive-Durchlauf. Der Agent verwendet sein eigenes dediziertes Recherchemodell, um konsistente und zuverlässige Ergebnisse zu gewährleisten. Dieses Recherchemodell ist immer ein von T-Systems gehostetes T-Cloud-Modell, sodass Deep Dive mit [vertraulichen](https://docs.smartchat.ai.t-systems.net/de/user/concepts/confidentiality/) Daten genutzt werden kann: Die gesamte Verarbeitung findet in Deutschland statt, und es werden keine Daten an Dritte übermittelt. Nur Ihre direkte Recherchefrage beeinflusst das Ergebnis. An Ihrem regulären Chat ändert sich nichts.

## [Wie oft kann ich Deep Dive nutzen?](https://docs.smartchat.ai.t-systems.net/de/user/guide/deep-dive/#wie-oft-kann-ich-deep-dive-nutzen)

Jedem Nutzer stehen folgende Kontingente zur Verfügung:

- **10 Durchläufe pro Tag**: Der Schalter zeigt an, wie viele Durchläufe Sie heute bereits verwendet haben (z. B. `0/10`).
- **2 gleichzeitige Durchläufe**: Sie können bis zu zwei Deep-Dive-Durchläufe gleichzeitig über alle Ihre Chats hinweg aktiv haben.

Das Tageskontingent wird täglich um Mitternacht zurückgesetzt.

Individuelle Vereinbarungen können diese Limits überschreiben; Ihr eigenes Kontingent kann daher abweichen. Anwendungsinhaber sind von diesen Limits vollständig ausgenommen.

## [Deep Dive starten](https://docs.smartchat.ai.t-systems.net/de/user/guide/deep-dive/#deep-dive-starten)

*\[Image: Deep-Dive-Schalter im Nachrichteneingabefeld mit Anzeige der genutzten Durchläufe]*

1. Öffnen Sie den Space, dessen Dokumente der Agent recherchieren soll.
2. Aktivieren Sie den **Deep-Dive**-Schalter im Nachrichteneingabefeld. Der Schalter zeigt an, wie viele Durchläufe Sie heute bereits genutzt haben.
3. Geben Sie Ihre Recherchefrage ein und senden Sie sie ab.

## [Recherchefrage bestätigen](https://docs.smartchat.ai.t-systems.net/de/user/guide/deep-dive/#recherchefrage-best%C3%A4tigen)

Nach dem Empfang Ihrer Eingabe schlägt Deep Dive eine verfeinerte Recherchefrage zur Prüfung vor, bevor die eigentliche Arbeit beginnt. Der Statusindikator zeigt **“Awaiting approval”**. Sie haben drei Möglichkeiten:

*\[Image: Vorgeschlagene Recherchefrage mit den Schaltflächen "Approve", "Give Feedback" und "Reject" sowie dem Status "Awaiting approval"]*

| Aktion | Was passiert |
| - | - |
| **Approve** | Der Agent beginnt sofort mit der Arbeit. |
| **Give Feedback** | Es öffnet sich ein Textfeld, in dem Sie beschreiben können, was geändert werden soll. Der Agent überarbeitet die Recherchefrage und fragt erneut nach. |
| **Reject** | Der Durchlauf wird abgebrochen. Es wird kein Kontingent verbraucht. |

Der Agent startet nicht, bis Sie bestätigen. Wenn Sie den Chat schließen, während er auf Ihre Bestätigung wartet, bleibt der Durchlauf pausiert, bis Sie zurückkehren und antworten.

## [Während der Agent arbeitet](https://docs.smartchat.ai.t-systems.net/de/user/guide/deep-dive/#w%C3%A4hrend-der-agent-arbeitet)

Nach der Bestätigung läuft der Agent im Hintergrund. Sie sehen:

*\[Image: Agent überträgt Live-Updates in den Chat mit dem Status "Working"]*

- Einen **Spinner** in der unteren rechten Ecke des Chats.
- Den Statusindikator in der oberen rechten Ecke der Agentennachricht mit dem Status **“Working”**.
- Live-Updates, die während der Arbeit in den Chat gestreamt werden, einschließlich der gefundenen Dokumente.

Sie können den Chat schließen oder in einen anderen Chat wechseln; der Agent läuft weiter. Kehren Sie zu demselben Chat zurück, um den fertigen Bericht zu sehen.

## [Der Recherchebericht](https://docs.smartchat.ai.t-systems.net/de/user/guide/deep-dive/#der-recherchebericht)

Wenn der Durchlauf abgeschlossen ist, wechselt der Status zu **“Completed”** und der Agent liefert die Ergebnisse als formatierten Markdown-Bericht:

*\[Image: Abgeschlossener Deep-Dive-Durchlauf mit "Deep Dive Event History" und der Schaltfläche "Open Report"]*

- **Quellenangaben**: Jede Aussage ist mit dem jeweiligen Quelldokument verknüpft.
- **Herunterladbarer Bericht**: Der vollständige Bericht kann als Datei exportiert werden.

Der Bericht wird wie eine reguläre Nachricht dem Chatverlauf hinzugefügt. Sie können anschließend Folgefragen im selben Chat stellen. Folgefragen verwenden den normalen Chat-Modus und lösen keinen weiteren Deep-Dive-Durchlauf aus, es sei denn, Sie aktivieren Deep Dive erneut.
