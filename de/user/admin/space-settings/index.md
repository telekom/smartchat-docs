# Space-Einstellungen

Source: https://docs.smartchat.ai.t-systems.net/de/user/admin/space-settings/

> Vertraulichkeit, Space-API-Schlüssel, Upload-Limit und Modelle: die Einstellungen, die ein Space Owner in der Administration steuert.

Die **Einstellungen** im Abschnitt **Bereichsinhaber** der [Administration](https://docs.smartchat.ai.t-systems.net/de/user/admin/) enthalten die Konfiguration eines Spaces. Diese Seite behandelt die Seiten **Bereich**, **Modelle** und **Websuche**; Datenquellen haben eigene Anleitungen ([Confluence-Synchronisation](https://docs.smartchat.ai.t-systems.net/de/user/admin/confluence-sync/), [S3 AutoSync](https://docs.smartchat.ai.t-systems.net/de/user/admin/s3-autosync/)).

Öffnen Sie **Administration → Bereichsinhaber** und wählen Sie den zu konfigurierenden Space unter **Aktueller Bereich** aus.

## [Bereich](https://docs.smartchat.ai.t-systems.net/de/user/admin/space-settings/#bereich)

*\[Image: Seite Bereich mit dem Schalter Vertrauliche Daten und dem Feld Space-API-Schlüssel]*

### [Vertrauliche Daten](https://docs.smartchat.ai.t-systems.net/de/user/admin/space-settings/#vertrauliche-daten)

Der Schalter **Vertrauliche Daten** markiert jeden Chat in diesem Space als vertraulich und beschränkt ihn auf Modelle, die vertrauliche Daten verarbeiten dürfen. Eingeschaltet bewirkt er:

- Alle Chats im Space sind auf von der Telekom gehostete Modelle beschränkt, extern gehostete Modelle werden abgelehnt.
- Websuche und Tools sind in diesen Chats deaktiviert.
- Die Einstellung gilt für jede Kollektion des Spaces, unabhängig von deren eigener Vertraulichkeitsmarkierung.

Ist für den Space eine Websuche konfiguriert, fragt Smartchat zuerst nach (**Diesen Bereich als vertraulich markieren?**) und schaltet die Websuche für den Space dann ab. Ihre Einstellungen bleiben erhalten und gelten wieder, sobald der Space nicht mehr vertraulich ist.

Die Änderung wird sofort gespeichert (Meldung **Space-Konfiguration gespeichert**), und Mitglieder sehen das Vertraulichkeits-Badge im Chat-Eingabefeld ohne Neuladen. Wie sich die Vertraulichkeit auf Kollektionen und Chats auswirkt, erklärt [Vertraulichkeit](https://docs.smartchat.ai.t-systems.net/de/user/concepts/confidentiality/).

### [Space-API-Schlüssel](https://docs.smartchat.ai.t-systems.net/de/user/admin/space-settings/#space-api-schl%C3%BCssel)

Smartchat benötigt einen Schlüssel aus dem [API Key Portal](https://apikey.llmhub.t-systems.net/), um im Namen des Spaces auf das Model Serving zuzugreifen.

1. Fügen Sie den Schlüssel in **Space-API-Schlüssel** ein und drücken Sie **Enter** (oder klicken Sie neben das Feld). Die Meldung **Space-API-Schlüssel gespeichert** bestätigt die Aktualisierung.
2. Der Hinweis unter dem Feld zeigt den Zustand: **Ein Schlüssel ist konfiguriert. Geben Sie einen neuen ein, um ihn zu ersetzen.** oder **Es ist kein Schlüssel konfiguriert. Ohne Schlüssel kann dieser Space das Model Serving nicht erreichen.**

> **Der Schlüssel ist nur schreibbar**
>
> Seit v3.15.1 kann niemand einen gespeicherten Schlüssel auslesen: Space Owner und Anwendungsinhaber sehen nur, ob ein Schlüssel konfiguriert ist, und auch `GET /space/api-key` liefert ihn nicht mehr. Bewahren Sie den Schlüssel im Secret-Store Ihres Teams auf. Zum Rotieren fügen Sie den neuen Schlüssel über den Platzhalter ein.

### [Maximale Uploadgröße](https://docs.smartchat.ai.t-systems.net/de/user/admin/space-settings/#maximale-uploadgr%C3%B6%C3%9Fe)

Wo die Upload-Kontrolle in Ihrer Umgebung aktiviert ist, begrenzt **Maximale Uploadgröße** die Größe einer einzelnen hochgeladenen Datei in MB. Leer lassen bedeutet kein Limit. Der Wert wird beim Verlassen des Feldes gespeichert.

### [Feedback](https://docs.smartchat.ai.t-systems.net/de/user/admin/space-settings/#feedback)

Wo Feedback in Ihrer Umgebung verfügbar ist, erlaubt der Schalter **Feedback** den Mitgliedern dieses Spaces, [Antworten zu bewerten](https://docs.smartchat.ai.t-systems.net/de/user/guide/feedback/) und sie mit Ihnen zu teilen. Ausgeschaltet sind die Bewertungsschaltflächen verborgen; bereits gegebenes Feedback bleibt erhalten und auf der Seite [Feedback](https://docs.smartchat.ai.t-systems.net/de/user/admin/feedback/) sichtbar.

## [Modelle](https://docs.smartchat.ai.t-systems.net/de/user/admin/space-settings/#modelle)

Wo der Agenten-Modus verfügbar ist, beschreibt [Einstellungen des Agenten-Modus](https://docs.smartchat.ai.t-systems.net/de/user/admin/agent-mode/#f%C3%BCr-einen-space) seine Einstellungen für diesen Space (Standardmodus für neue Chats, Webzugriff der Agenten).

*\[Image: Seite Modelle mit der Standardmodell-Auswahl und der Embedding-Modell-Karte]*

- **Modelle aktivieren und deaktivieren**: die Liste zeigt alle Modelle, die dem Space zur Verfügung stehen. Mit dem Schalter in jeder Zeile steuern Sie, welche Ihre Mitglieder auswählen können. **Modelle durchsuchen** filtert die Liste.
- **Standardmodell**: das Modell, das für neue Chats in diesem Space vorausgewählt ist. Wählen Sie ein Modell oder einen [Assistenten](https://docs.smartchat.ai.t-systems.net/de/user/guide/workspaces/#assistenten-erstellen-und-nutzen). Wird das gewählte Modell später abgeschaltet, zeigt die Auswahl **Das ausgewählte Standardmodell ist nicht mehr verfügbar.**, und der eRAG-Standard wird genutzt, bis Sie ein neues wählen.
- **Embedding-Modell**: nur zur Information. Es wurde bei der Konfiguration des Spaces festgelegt und kann danach nicht geändert werden, weil alle vorhandenen Embeddings davon abhängen.
- **Voreinstellungen importieren / exportieren**: Modell-Presets als JSON zwischen Spaces austauschen.

## [Websuche](https://docs.smartchat.ai.t-systems.net/de/user/admin/space-settings/#websuche)

Die Seite **Websuche** hat für jeden Typ der Websuche einen Schalter:

- **Websuche**: sucht über einen externen Suchanbieter. Sie muss zuerst für Ihre Smartchat-Umgebung eingerichtet werden, mit einem separat lizenzierten Schlüssel des Suchanbieters.
- **Native Websuche aktivieren**: lässt Claude- und Gemini-Modelle über ihren eigenen Anbieter suchen. Dafür ist keine Einrichtung nötig.

Ein Schalter erscheint erst, wenn sein Typ der Websuche in Ihrer Umgebung verfügbar ist, und ist dann in jedem Space eingeschaltet. Schalten Sie ihn aus, erhalten die Benutzer des Space diesen Typ der Websuche nicht mehr; schalten Sie ihn wieder ein, steht er wieder zur Verfügung. In einem Space mit **Vertrauliche Daten** bleibt die Websuche unabhängig von den Schaltern aus.

Wo die Websuche pro Space konfigurierbar ist, wählen Sie außerdem die Suchmaschine und hinterlegen deren Zugangsdaten nur für diesen Space. Ein Banner erinnert daran, dass die Änderungen nur für diesen Space gelten.

In Mein Bereich hat die Seite zusätzlich den Schalter **Web-Suche mit Dateien/Kollektionen in Mein Bereich zulassen**. Ist er aus, steht die Websuche in Mein Bereich nicht zur Verfügung, sobald Dateien oder Kollektionen an einen Chat angehängt sind oder der ausgewählte Assistent eine Kollektion hat. Andere Spaces haben diesen Schalter nicht.
