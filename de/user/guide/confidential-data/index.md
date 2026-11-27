# Mit vertraulichen Daten arbeiten

Source: https://docs.smartchat.ai.t-systems.net/de/user/guide/confidential-data/

> Schritt für Schritt – eine vertrauliche Kollektion anlegen, damit chatten und sehen, wie Smartchat vertrauliche Daten auf Telekom-gehosteten Modellen hält.

Smartchat kann vertrauliche Dokumente für Sie innerhalb der Telekom-gehosteten Infrastruktur halten. Diese Seite zeigt ein typisches Beispiel: Ein Controlling-Team legt den Budgetplan für 2027 in einer vertraulichen Kollektion ab und stellt Fragen dazu. Die Regeln dahinter finden Sie unter [Vertraulichkeit](https://docs.smartchat.ai.t-systems.net/de/user/concepts/confidentiality/).

## [1. Eine vertrauliche Kollektion anlegen](https://docs.smartchat.ai.t-systems.net/de/user/guide/confidential-data/#1-eine-vertrauliche-kollektion-anlegen)

1. Öffnen Sie **Arbeitsbereich → Kollektion** und klicken Sie auf **Kollektion erstellen**.
2. Geben Sie einen Namen und eine Beschreibung ein.
3. Schalten Sie **Vertraulich** ein. Fahren Sie mit der Maus über die Bezeichnung, um zu sehen, was sie bedeutet.
4. Klicken Sie auf **Kollektion erstellen** und fügen Sie Ihre Dokumente über die Schaltfläche **+** in der Kollektion hinzu.

*\[Image: Formular Kollektion erstellen mit eingeschaltetem Schalter Vertraulich]*

In der Kollektionsliste trägt die Kollektion nun ein Schild.

*\[Image: Kollektionsliste mit dem Schild neben der vertraulichen Kollektion]*

Um eine bestehende Kollektion vertraulich zu machen, öffnen Sie sie und schalten Sie **Vertraulich** in ihrer Kopfzeile ein. Die Änderung wird sofort gespeichert.

*\[Image: Kopfzeile einer Kollektion mit dem Schalter Vertraulich]*

> **Tipp**
>
> Legen Sie vertrauliche Dokumente in eine vertrauliche Kollektion, statt sie direkt in einen Chat hochzuladen. Eine in einen Chat hochgeladene Datei hat keine eigene Vertraulichkeitsmarkierung.

## [2. Die Kollektion in einem Chat verwenden](https://docs.smartchat.ai.t-systems.net/de/user/guide/confidential-data/#2-die-kollektion-in-einem-chat-verwenden)

Geben Sie in einem neuen Chat **#** ein und wählen Sie die Kollektion aus. Vertrauliche Kollektionen zeigen in der Liste das Schild.

*\[Image: Mit # geöffnete Kollektionsauswahl mit der vertraulichen Kollektion]*

Sobald die Kollektion angehängt ist, ist der Chat vertraulich. War ein extern gehostetes Modell ausgewählt, wechselt Smartchat zu einem Telekom-gehosteten Modell und weist Sie darauf hin.

*\[Image: Meldung, dass der Chat zu einem Telekom-gehosteten Modell gewechselt hat]*

Das Schild-Symbol neben dem Mikrofon zeigt, dass Sie sich in einem vertraulichen Chat befinden.

*\[Image: Tooltip des Symbols für vertrauliche Chats im Eingabefeld]*

## [3. Was Sie im Chat nutzen können](https://docs.smartchat.ai.t-systems.net/de/user/guide/confidential-data/#3-was-sie-im-chat-nutzen-k%C3%B6nnen)

Die Modellauswahl bietet nur Modelle an, die T-Systems hostet. Extern gehostete Modelle sind ausgeblendet.

*\[Image: Modellauswahl mit ausschließlich Telekom-gehosteten Modellen und dem Hinweis zu vertraulichen Daten]*

Die Websuche ist im Menü **+** ausgegraut, weil sie Teile der Konversation an einen externen Suchanbieter senden würde. Auch Tools werden nicht angeboten.

*\[Image: Deaktivierter Eintrag Websuche im Menü + eines vertraulichen Chats]*

Stellen Sie Ihre Frage wie gewohnt. Die Antwort erzeugt ein Telekom-gehostetes Modell, und sie nennt die Dokumente aus Ihrer Kollektion als Quelle.

*\[Image: Antwort eines Telekom-gehosteten Modells mit einem Dokument aus der vertraulichen Kollektion als Quelle]*

## [4. Der Chat bleibt vertraulich](https://docs.smartchat.ai.t-systems.net/de/user/guide/confidential-data/#4-der-chat-bleibt-vertraulich)

Ein vertraulicher Chat behält seine Einschränkungen für immer:

- Wenn Sie die Kollektion aus dem Chat entfernen oder **Vertraulich** an der Kollektion später ausschalten, werden sie nicht aufgehoben.
- **Teilen**, **Klonen** und **Kopieren** werden im Chat-Menü nicht angeboten, damit der Inhalt in Smartchat bleibt. **Exportieren** ist weiterhin möglich.

Brauchen Sie für eine Folgefrage die Websuche oder ein extern gehostetes Modell, starten Sie einen neuen Chat ohne die vertraulichen Daten.

## [In einem vertraulichen Space arbeiten](https://docs.smartchat.ai.t-systems.net/de/user/guide/confidential-data/#in-einem-vertraulichen-space-arbeiten)

Hat Ihr Space Owner den ganzen Space als vertraulich markiert, ist jeder Chat darin von Anfang an vertraulich, mit allen oben beschriebenen Einschränkungen. Einzelne Kollektionen müssen Sie dann nicht markieren.

Wenn Sie aus einem Chat heraus einen vertraulichen Space öffnen, fragt Smartchat zuerst nach. **Fortsetzen** öffnet den Space und beschränkt den aktuellen Chat dauerhaft auf Telekom-gehostete Modelle; **Abbrechen** lässt alles, wie es ist.

*\[Image: Bestätigungsdialog: Sie haben einen vertraulichen Bereich ausgewählt]*

## [Assistenten mit vertraulichen Kollektionen](https://docs.smartchat.ai.t-systems.net/de/user/guide/confidential-data/#assistenten-mit-vertraulichen-kollektionen)

Ein [Assistent](https://docs.smartchat.ai.t-systems.net/de/user/guide/workspaces/), der eine vertrauliche Kollektion verwendet, muss auf einem Telekom-gehosteten Basismodell laufen:

- Wenn Sie im Assistenten-Editor eine vertrauliche Kollektion anhängen, bietet die Liste der Basismodelle nur Telekom-gehostete Modelle an. Ein zuvor gewähltes extern gehostetes Basismodell wird entfernt, und der Editor nennt den Grund.
- Ein bestehender Assistent, dessen Kollektion vertraulich wird, während er auf einem extern gehosteten Modell läuft, wird in der Modellauswahl als **Nicht verfügbar** angezeigt, bis Sie ihn bearbeiten und ein Telekom-gehostetes Basismodell auswählen.

Chats mit einem solchen Assistenten sind vertraulich, genau so, als hätten Sie die Kollektion selbst angehängt.
