# Gruppen

Source: https://docs.smartchat.ai.t-systems.net/de/user/concepts/groups/

> Die Gruppen, die jeder Space hat, wer sie verwaltet und wie man eine anlegt.

Gruppen sind das zentrale Instrument der Zugriffs- und Berechtigungsverwaltung in einem [Space](https://docs.smartchat.ai.t-systems.net/de/user/concepts/spaces/). Sie haben zwei Aufgaben:

- **Teilen:** Kollektionen, Assistenten, Prompts und Agenten lassen sich mit einer Gruppe teilen, sodass ihre Mitglieder sie verwenden oder bearbeiten können. Siehe [Zugriffskontrolle](https://docs.smartchat.ai.t-systems.net/de/user/concepts/access-control/).
- **Berechtigungen:** Eine Gruppe kann ihren Mitgliedern Funktionen erlauben, zum Beispiel Agenten zu bauen, die Websuche zu nutzen oder Elemente mit allen im Space zu teilen. Siehe [Berechtigungen](https://docs.smartchat.ai.t-systems.net/de/user/concepts/permissions/).

Jede Gruppe gehört zu einem Space und wirkt in keinem anderen Space. Wie sich Rollen, Berechtigungen und Zugriffskontrolle unterscheiden, steht unter [Rollen, Berechtigungen & Zugriffskontrolle](https://docs.smartchat.ai.t-systems.net/de/user/concepts/roles-permissions-access-control/).

Ben ist im Vertrieb und in der Projektgruppe und bekommt beides: Er kann die Websuche nutzen und Agenten bauen, das Vertriebshandbuch verwenden und die Portal-Unterlagen bearbeiten. Acme - Allgemein können alle im Space verwenden. Carlas Prompt-Entwurf ist privat: Sie hat ihn mit keiner Gruppe geteilt.

## [Gruppen, die jeder Space hat](https://docs.smartchat.ai.t-systems.net/de/user/concepts/groups/#gruppen-die-jeder-space-hat)

Smartchat legt in jedem Space zwei Gruppen an und hält ihre Mitglieder aktuell:

- **SpaceOwners {Space}** enthält die Space Owner des Space. An dieser Gruppe lässt sich nichts ändern.
- **Users {Space}** enthält alle Mitglieder des Space. An ihr lassen sich nur die Berechtigungen ändern.

Wer ein Element mit **Alle in diesem Bereich** teilt, gibt der Gruppe **Users** Zugriff. Berechtigungen der Gruppe **Users** gelten für alle Mitglieder des Space.

## [Wer Gruppen verwaltet](https://docs.smartchat.ai.t-systems.net/de/user/concepts/groups/#wer-gruppen-verwaltet)

Space Owner verwalten die Gruppen ihres Space unter **Administration → Bereichsinhaber → Gruppen**. Sie legen Gruppen an und löschen sie, fügen Mitglieder hinzu und entfernen sie und setzen die Berechtigungen jeder Gruppe.

Zwei Berechtigungen erlauben auch anderen Mitgliedern, Gruppen zu verwalten:

- **Gruppenverwaltung** unter **Kritische Berechtigungen**: alle Gruppen im Space verwalten, wie ein Space Owner. Wer sie hat, kann sie auch an andere vergeben.
- **Verwaltung eigener Gruppen** unter **Arbeitsbereichsberechtigungen**: Gruppen anlegen und die Mitglieder der selbst angelegten Gruppen verwalten, ohne ihre Berechtigungen zu ändern.

## [Eine Gruppe anlegen](https://docs.smartchat.ai.t-systems.net/de/user/concepts/groups/#eine-gruppe-anlegen)

1. Klicken Sie auf Ihr Profilbild und wählen Sie **Administration**.
2. Gehen Sie zu **Bereichsinhaber → Gruppen**, prüfen Sie, dass der richtige Space ausgewählt ist, und klicken Sie auf **Gruppe hinzufügen**.
3. Geben Sie einen Namen und optional eine Beschreibung ein und klicken Sie auf **Erstellen**.
4. Öffnen Sie die Gruppe. Fügen Sie im Reiter **Benutzer** ihre Mitglieder hinzu und setzen Sie im Reiter **Berechtigungen** ihre [Berechtigungen](https://docs.smartchat.ai.t-systems.net/de/user/concepts/permissions/).

Eine neue Gruppe startet leer:

- Sie hat keine Mitglieder, auch Sie selbst nicht.
- Nichts ist mit ihr geteilt.
- Ihre Berechtigungen sind die [Standardberechtigungen](https://docs.smartchat.ai.t-systems.net/de/user/concepts/permissions/#standardberechtigungen) des Space zum Zeitpunkt ihrer Erstellung.

Wenn sich Ihr Smartchat über den Identitätsanbieter Ihrer Organisation anmeldet, kann eine Gruppe auch **Gruppenattribute des Identitätsanbieters** enthalten. Benutzer, deren Gruppe beim Identitätsanbieter passt, werden bei der Anmeldung zur Gruppe hinzugefügt.

Wer aus dem Space entfernt wird, wird auch aus allen seinen Gruppen entfernt.
