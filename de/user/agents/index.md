# Agenten-Modus

Source: https://docs.smartchat.ai.t-systems.net/de/user/agents/

> Was der Agenten-Modus ist, wie Sie ihn einschalten und wie Agenten über Connectors mit den Systemen Ihrer Organisation arbeiten.

> **Preview**
>
> Der Agenten-Modus und MCP-Connectors sind derzeit nur als Preview verfügbar. Wenn Sie diese Funktionen testen möchten, wenden Sie sich bitte an Ihren Ansprechpartner bei T-Systems.

Im **Agenten-Modus** antwortet Smartchat mit einem Agenten statt mit einem einzelnen Modellaufruf. Ein Agent plant seine Schritte selbst: Er kann Code in einer Sandbox ausführen, Tools aufrufen und über [Connectors](https://docs.smartchat.ai.t-systems.net/de/user/agents/connectors/) mit den eigenen Systemen Ihrer Organisation arbeiten. Er entscheidet selbst, wann ein Tool oder Connector bei Ihrer Anfrage hilft.

## [Den Agenten-Modus einschalten](https://docs.smartchat.ai.t-systems.net/de/user/agents/#den-agenten-modus-einschalten)

Schalten Sie im Eingabefeld den Schalter **Agenten-Modus** ein, bevor Sie die erste Nachricht eines Chats senden. Ausgeschaltet ist es ein normaler Chat. Ein neuer Chat startet in dem Modus, den Sie in diesem Space zuletzt gewählt haben. Haben Sie dort noch keinen gewählt, folgt er dem Standard des Space, den Space Owner und Anwendungsinhaber in den [Einstellungen des Agenten-Modus](https://docs.smartchat.ai.t-systems.net/de/user/admin/agent-mode/) festlegen.

Der Modus gilt jeweils für einen ganzen Chat:

- **Er kann nach dem Start des Chats nicht mehr geändert werden.** Starten Sie einen neuen Chat, um zwischen Agenten-Modus und normalem Chat zu wechseln.
- **Er kann nicht geändert werden, solange eine für den Agenten hochgeladene Datei angehängt ist.** Entfernen Sie die Datei zuerst.

## [Einen Agenten auswählen](https://docs.smartchat.ai.t-systems.net/de/user/agents/#einen-agenten-ausw%C3%A4hlen)

Stehen mehrere Agenten zur Verfügung, wählen Sie einen über **Agent wechseln** aus. Jeder Agent kann eigene Anweisungen, Beispiel-Prompts und Connectors mitbringen. Wie Sie eigene Agenten erstellen, lesen Sie unter [Eigene Agenten](https://docs.smartchat.ai.t-systems.net/de/user/agents/custom-agents/).

## [Dateien anhängen](https://docs.smartchat.ai.t-systems.net/de/user/agents/#dateien-anh%C3%A4ngen)

Hat der ausgewählte Agent eine Sandbox, können Sie Dateien jedes Typs an den Chat anhängen, bis zu 100 MB pro Datei und 20 Dateien pro Nachricht. Die Dateien gehen direkt an den Agenten und werden keiner Kollektion hinzugefügt. Hat der Agent keine Sandbox, kann er hochgeladene Dateien nicht lesen, und Smartchat bittet Sie, einen Agenten mit Sandbox auszuwählen.

## [Webzugriff](https://docs.smartchat.ai.t-systems.net/de/user/agents/#webzugriff)

> **Seit v3.15.1 standardmäßig aus**
>
> Agenten können das Web nur nutzen, wenn ein Anwendungsinhaber es in der Administration für die Instanz erlaubt und der Space Owner es anschließend für seinen Space erlaubt. Bis beide das getan haben, zeigt der Agenten-Editor die Web-Fähigkeiten des Agenten als deaktiviert an. Vertrauliche Spaces und Chats erhalten nie Webzugriff.

Anwendungsinhaber und Space Owner finden diese Schalter in den [Einstellungen des Agenten-Modus](https://docs.smartchat.ai.t-systems.net/de/user/admin/agent-mode/).

## [Mit einem Agenten arbeiten](https://docs.smartchat.ai.t-systems.net/de/user/agents/#mit-einem-agenten-arbeiten)

- **Freigaben**: Vor manchen Aktionen bittet der Agent um Ihre Freigabe. Bestätigen oder lehnen Sie im Chat ab, damit er weitermachen kann.
- **Schrittlimit**: Ein Agent hält nach einer festen Zahl von Schritten an. Ihre Anfrage bleibt gültig: Bitten Sie den Agenten, dort weiterzumachen, wo er aufgehört hat.
- **Connectors**: Braucht der Agent einen Connector, den Sie noch nicht verbunden haben, bittet er Sie zuerst, ihn zu verbinden. Siehe [Connectors nutzen](https://docs.smartchat.ai.t-systems.net/de/user/agents/connectors/).
- **Agent stoppen** beendet einen Lauf jederzeit.

Agenten arbeiten immer mit Ihren eigenen Berechtigungen. Sie können Ihnen nie etwas zeigen, das Ihr Konto nicht ohnehin sehen dürfte.
