# Websuche

Source: https://docs.smartchat.ai.t-systems.net/de/user/guide/web-search/

> Smartchat mit aktuellen Webergebnissen über einen externen Suchanbieter oder die integrierte Funktion Ihres Modells.

Smartchat unterstützt zwei Wege, um aktuelle Webergebnisse in eine Konversation einzubinden:

- **Websuche**: Smartchat fragt einen externen Suchanbieter (Bing, Brave, Google usw.) ab und fügt die Ergebnisse dem Kontext hinzu. Funktioniert mit jedem Modell; erfordert eine vorherige Einrichtung durch T-Systems.
- **Native Websuche**: Der Modellanbieter führt die Suche als integrierte Funktion durch. Verfügbar nur für Google (Gemini) und Anthropic (Claude) Modelle.

Beide Typen hängen an derselben Berechtigung **Websuche**. Sobald ein Typ verfügbar ist, ist er in jedem Space eingeschaltet, und ein Space Owner kann ihn für seinen Space ausschalten.

## [Websuche](https://docs.smartchat.ai.t-systems.net/de/user/guide/web-search/#websuche)

Die Websuche funktioniert mit jedem Modell, unabhängig vom Anbieter. Smartchat fragt einen konfigurierten externen Suchanbieter ab und übergibt die Ergebnisse als Kontext an das Modell. Eine Tool-Unterstützung des LLM-Anbieters ist nicht erforderlich.

Dies ist eine Opt-in-Funktion: Sie ist nur verfügbar, wenn ein Space Owner sie für den Space eingeschaltet hat und ein Such-API-Schlüssel konfiguriert ist.

### [Unterstützte Suchanbieter](https://docs.smartchat.ai.t-systems.net/de/user/guide/web-search/#unterst%C3%BCtzte-suchanbieter)

Alle [OpenWebUI-kompatiblen Suchanbieter](https://docs.openwebui.com/category/web-search) werden unterstützt, darunter Bing, Brave, Google, Jina, Kagi, Mojeek, Perplexity und weitere.

### [Einrichtung durch den Space Owner](https://docs.smartchat.ai.t-systems.net/de/user/guide/web-search/#einrichtung-durch-den-space-owner)

1. Klicken Sie auf Ihr Profilbild und wählen Sie **Administration**.
2. Gehen Sie zu **Bereichsinhaber → Websuche** und prüfen Sie, dass unter **Aktueller Bereich** der richtige Space ausgewählt ist.
3. Sobald die Websuche für Ihre Umgebung eingerichtet ist, ist **Websuche** in jedem Space eingeschaltet. Schalten Sie sie aus, um sie den Benutzern des Space zu entziehen, und wieder ein, um sie zurückzugeben.
4. Wählen Sie eine **Suchmaschine** aus dem Dropdown.

## [Native Websuche](https://docs.smartchat.ai.t-systems.net/de/user/guide/web-search/#native-websuche)

Die native Websuche nutzt die integrierte Suchfunktion des Modellanbieters. Es ist kein separates Suchanbieter-Konto oder API-Schlüssel erforderlich. Sie funktioniert in Smartchat sofort für alle, die Zugang zu einem unterstützten Modell haben.

### [Unterstützte Anbieter](https://docs.smartchat.ai.t-systems.net/de/user/guide/web-search/#unterst%C3%BCtzte-anbieter)

- **Google** (Gemini)
- **Anthropic** (Claude)

> **Nicht verfügbar für T-Cloud-Modelle**
>
> Die native Websuche ist eine Fähigkeit des Modellanbieters und funktioniert daher **nicht** mit den von T-Systems in der T-Cloud gehosteten Open-Source-Modellen. Für die Websuche mit diesen Modellen wird die reguläre Websuche verwendet, die eine separate Lizenz für einen Suchanbieter voraussetzt.

Im Modellauswahl-Menü werden Modelle mit nativer Websuche durch ein **Globus-Symbol** (🌐) gekennzeichnet.

### [Einrichtung durch den Space Owner](https://docs.smartchat.ai.t-systems.net/de/user/guide/web-search/#einrichtung-durch-den-space-owner-1)

1. Klicken Sie auf Ihr Profilbild und wählen Sie **Administration**.
2. Gehen Sie zu **Bereichsinhaber → Websuche** und prüfen Sie, dass unter **Aktueller Bereich** der richtige Space ausgewählt ist.
3. **Native Websuche aktivieren** ist in jedem Space eingeschaltet. Schalten Sie den Schalter aus, um die native Websuche den Benutzern des Space zu entziehen, und wieder ein, um sie zurückzugeben.

## [Berechtigungen](https://docs.smartchat.ai.t-systems.net/de/user/guide/web-search/#berechtigungen)

Space Owner haben jede [Berechtigung](https://docs.smartchat.ai.t-systems.net/de/user/concepts/permissions/) ihres Space und brauchen dafür keine Gruppe. Andere Mitglieder brauchen die Berechtigung **Websuche**, über eine ihrer [Gruppen](https://docs.smartchat.ai.t-systems.net/de/user/concepts/groups/) oder die Standardberechtigungen des Space. Sie ist standardmäßig aus.

So erteilen Sie die Berechtigung:

1. Gehen Sie in der Administration zu **Bereichsinhaber → Gruppen**.
2. Klicken Sie auf eine Gruppe oder auf **Standardberechtigungen**, um die Berechtigung allen Mitgliedern des Space zu geben. **Standardberechtigungen** sehen nur Anwendungsinhaber.
3. Öffnen Sie den Reiter **Berechtigungen**.
4. Aktivieren Sie unter **Funktionen-Berechtigungen** die **Websuche**.

Außerdem muss die Websuche für Ihre Smartchat-Instanz eingeschaltet sein. Ist sie dort aus, kann sie niemand nutzen, auch Space Owner nicht. Siehe [Berechtigungen](https://docs.smartchat.ai.t-systems.net/de/user/concepts/permissions/).

## [Websuche verwenden](https://docs.smartchat.ai.t-systems.net/de/user/guide/web-search/#websuche-verwenden)

**Websuche (externer Anbieter):** Verfügbar für jedes Modell, sobald ein Space Owner sie eingeschaltet hat. Aktivieren Sie dazu den Schalter **Websuche** im Eingabebereich und senden Sie dann Ihre Anfrage. Smartchat ruft relevante Ergebnisse ab und stellt sie dem Modell zur Verfügung.

**Native Websuche:** Öffnen Sie einen Chat und wählen Sie im Modellauswahl-Menü ein Modell mit dem Globus-Symbol (🌐) aus. Aktivieren Sie den Schalter **Websuche** im Eingabebereich und senden Sie dann Ihre Anfrage. Das Modell ruft aktuelle Webergebnisse ab und bezieht sie in seine Antwort ein.

**Wenn beide verfügbar sind:** Wenn die Websuche (externer Anbieter) für Ihre Umgebung konfiguriert ist und Sie ein Modell auswählen, das auch native Websuche unterstützt, können Sie in der Chat-Oberfläche pro Nachricht wählen, welchen Typ Sie verwenden möchten. Die Ergebnisse können je nach Suchanbieter und integrierter Suchfunktion des Modells unterschiedlich ausfallen.

## [Websuche mit eigenen Daten kombinieren](https://docs.smartchat.ai.t-systems.net/de/user/guide/web-search/#websuche-mit-eigenen-daten-kombinieren)

Die Websuche kann zusammen mit eigenen Daten im selben Chat verwendet werden – mit Kollektionen ebenso wie mit hochgeladenen Dateien –, solange die Daten **nicht vertraulich** sind. Entscheidend ist die Vertraulichkeit, nicht die Art der Daten:

- **Nicht-vertrauliche Kollektionen, Spaces und hochgeladene Dateien** können mit der Websuche kombiniert werden.
- **Vertrauliche Kollektionen oder Spaces** können nicht mit der Websuche kombiniert werden. Wenn eine Kollektion oder ihr Space als vertraulich markiert ist, ist die Websuche in diesem Chat nicht verfügbar.
- **Dateien aus einer vertraulichen Kollektion** verhalten sich genauso: Wird eine angehängt, ist der Chat vertraulich und die Websuche darin nicht verfügbar.

Die Websuche sendet Teile der Konversation an einen externen Anbieter und darf daher niemals mit vertraulichen Daten verwendet werden. Benutzer müssen sich bewusst sein, dass die Aktivierung der Websuche in einem Chat mit vertraulichen Informationen ein Datensicherheitsrisiko darstellt und vermieden werden muss. Dies kann auf zwei Ebenen durchgesetzt werden: Jeder Benutzer kann eine Kollektion als vertraulich kennzeichnen, und Admins können Spaces als vertraulich kennzeichnen. Siehe [Vertraulichkeit](https://docs.smartchat.ai.t-systems.net/de/user/concepts/confidentiality/) für Details zur Funktionsweise der Vertraulichkeitseinstellung.

## [Siehe auch](https://docs.smartchat.ai.t-systems.net/de/user/guide/web-search/#siehe-auch)

- [Varianten & Funktionen](https://docs.smartchat.ai.t-systems.net/features/v2-feature-overview)
- [Release Notes](https://docs.smartchat.ai.t-systems.net/release-notes/)
