# Connectors nutzen

Source: https://docs.smartchat.ai.t-systems.net/de/user/agents/connectors/

> Einen Agenten mit Ihrem eigenen Konto mit Tools wie Telecontext verbinden, sie im Chat verwenden und die Verbindung wieder trennen.

> **Preview**
>
> Der Agenten-Modus und MCP-Connectors sind derzeit nur als Preview verfügbar. Wenn Sie diese Funktionen testen möchten, wenden Sie sich bitte an Ihren Ansprechpartner bei T-Systems.

Ein **Connector** verbindet Smartchat über das [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) mit einem System Ihrer Organisation. Sobald Sie ihn verbunden haben, kann ein Agent im Chat Daten aus diesem System lesen und dessen Funktionen nutzen.

Connectors werden von den Betreibern von Smartchat registriert, und ein Anwendungsinhaber oder Space Owner legt fest, wer im Space sie nutzen darf. Eigene Connectors können Sie nicht hinzufügen; Sie entscheiden nur, welche der verfügbaren Sie mit Ihrem Konto verbinden.

## [Einen Connector verbinden](https://docs.smartchat.ai.t-systems.net/de/user/agents/connectors/#einen-connector-verbinden)

1. Öffnen Sie einen Chat und schalten Sie den **Agenten-Modus** ein. Connectors stehen nur Agenten zur Verfügung.

2. Klicken Sie unter dem Eingabefeld auf **Tool verbinden**. Der Dialog **Connectors** listet alle Connectors, die in Ihrem Space freigegeben sind.

   *\[Image: Dialog Connectors mit den verfügbaren Connectors]*

3. Klicken Sie beim gewünschten Connector auf **Verbinden**. Smartchat zeigt, was es nach Ihrer Freigabe tun kann:

   - auf die Daten zugreifen, für die Sie bereits berechtigt sind,
   - die Tools des Connectors in einem Chat in Ihrem Namen nutzen,
   - nur handeln, solange Sie angemeldet sind. Der Zugriff endet beim Trennen.

   *\[Image: Zustimmungsdialog vor dem Verbinden]*

4. Klicken Sie auf **Mit … autorisieren** (mit dem Namen des Connectors). Ein neues Fenster öffnet die Anmeldeseite des Systems, zum Beispiel Ihre Microsoft-Anmeldung.

5. Melden Sie sich an und bestätigen Sie die Berechtigungen, die das System anfragt.

   *\[Image: Anmelde- und Freigabeseite des verbundenen Systems]*

6. Zurück in Smartchat bestätigt der Dialog, dass der Connector einsatzbereit ist, und der Connector wird als **Verbunden** angezeigt.

> **Tipp**
>
> Blockiert Ihr Browser das Anmeldefenster, nutzen Sie im Dialog den Link **Anmeldeseite öffnen**.

Sie melden sich auf der Seite des Systems selbst an. Smartchat sieht Ihr Passwort nie.

## [Einen Connector im Chat verwenden](https://docs.smartchat.ai.t-systems.net/de/user/agents/connectors/#einen-connector-im-chat-verwenden)

Ein verbundener Connector ist nicht automatisch in jedem Chat aktiv. Schalten Sie im Dialog **Connectors** für jeden Connector, den der Agent nutzen soll, **In diesem Chat verwenden** ein. Aktive Connectors stehen unter dem Eingabefeld bei **In diesem Chat aktiv**.

*\[Image: Verbundener Connector mit dem Schalter In diesem Chat verwenden]*

Stellen Sie Ihre Frage dann wie gewohnt. Der Agent entscheidet, wann er den Connector aufruft.

*\[Image: Agent antwortet mit Daten aus einem verbundenen System]*

Da Sie sich mit Ihrem eigenen Konto verbunden haben, sieht der Agent nur, was Sie in diesem System sehen. Zwei Kollegen, die denselben Connector nutzen, arbeiten jeweils mit ihren eigenen Daten und Berechtigungen.

## [Die Verbindung trennen](https://docs.smartchat.ai.t-systems.net/de/user/agents/connectors/#die-verbindung-trennen)

Öffnen Sie den Dialog **Connectors** und klicken Sie beim Connector auf **Trennen**. Einige Sekunden lang können Sie das noch **Rückgängig** machen. Danach endet der Zugriff von Smartchat; um den Connector wieder zu nutzen, verbinden Sie ihn erneut.

Sie werden auch dann zum erneuten Verbinden aufgefordert, wenn die Registrierung eines Connectors erneuert wird, Ihr Zugriff entzogen und wieder gewährt wird oder wenn das Zugriffstoken Ihres Connectors abgelaufen ist oder widerrufen wurde.
