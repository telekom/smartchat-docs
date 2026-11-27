# Spaces und Benutzer verwalten

Source: https://docs.smartchat.ai.t-systems.net/de/user/admin/application-owner/

> Wie Anwendungsinhaber Spaces anlegen und konfigurieren und Benutzer sowie ihre Space-Rollen für die gesamte Instanz verwalten.

Im Abschnitt **Anwendungsinhaber** der [Administration](https://docs.smartchat.ai.t-systems.net/de/user/admin/) verwalten Anwendungsinhaber die gesamte Smartchat-Instanz: jeden Space, jeden Benutzer und die Einstellungen, die für alle gelten. Sie öffnen ihn über **Administration → Anwendungsinhaber**.

## [Bereiche](https://docs.smartchat.ai.t-systems.net/de/user/admin/application-owner/#bereiche)

**Bereiche** listet jeden Space der Instanz mit der Zahl seiner Mitglieder, seinen Space Ownern und dem Erstellungsdatum. Eine Spalte zeigt, welche Spaces vertrauliche Daten enthalten, und Sie können die Vertraulichkeit eines Spaces direkt in dieser Spalte ein- oder ausschalten.

Klicken Sie auf einen Space, um seine Konfiguration zu öffnen:

| Feld | Beschreibung |
| - | - |
| **Name** | Der Name des Spaces, wie Mitglieder ihn im Space-Selector sehen. |
| **Vertrauliche Daten** | Behandelt alle Daten im Space als vertraulich. Siehe [Vertraulichkeit](https://docs.smartchat.ai.t-systems.net/de/user/concepts/confidentiality/). |
| **IdP-Attribut für automatische Zuordnung** | Verknüpft den Space mit einem Attribut aus Ihrem Identity Provider, zum Beispiel einer Active-Directory-Gruppe. Wer sich mit diesem Attribut anmeldet, wird automatisch zum Space hinzugefügt. Siehe [IdP-Attribut auf Space-Mitgliedschaft](https://docs.smartchat.ai.t-systems.net/de/user/admin/single-sign-on/#idp-attribut-auf-space-mitgliedschaft). |
| **Space-API-Schlüssel** | Der Schlüssel, mit dem Smartchat für diesen Space das Model Serving erreicht. Nach dem Speichern wird er nur maskiert angezeigt. |
| **Max. Anzahl an Mitgliedern** | Wie viele Mitglieder der Space haben darf. **0** bedeutet unbegrenzt. |
| **Mitglieder** | Die Mitglieder und ihre Rollen. Fügen Sie Mitglieder per E-Mail hinzu, einzeln oder mehrere auf einmal, wechseln Sie ein Mitglied zwischen **Benutzer** und **Bereichsinhaber** oder entfernen Sie es. |

*\[Image: Space-Konfiguration mit Vertraulichkeit, IdP-Attribut, API-Schlüssel und Mitgliedern]*

### [Einen Space anlegen](https://docs.smartchat.ai.t-systems.net/de/user/admin/application-owner/#einen-space-anlegen)

Klicken Sie über der Liste auf **Neuer Bereich**, um einen Space anzulegen. Der Dialog konfiguriert ihn in einem Schritt vollständig, siehe [Neuen Space einrichten](https://docs.smartchat.ai.t-systems.net/de/user/admin/setting-up-a-new-space/).

## [Benutzer](https://docs.smartchat.ai.t-systems.net/de/user/admin/application-owner/#benutzer)

**Benutzer** listet alle in der Instanz registrierten Personen, auch solche, die hinzugefügt wurden, sich aber **nie angemeldet** haben, mit Erstellungsdatum und den Spaces, denen sie angehören.

Ein Badge kennzeichnet Konten, die keine Benutzer Ihrer Organisation sind: **Servicekonto** für die technischen Konten von SmartChat, **Intern** für Mitarbeitende von T-Systems und **Testkonto** für Testkonten. Servicekonten lassen sich weder löschen noch aus einem Space entfernen. Die Badges erscheinen auch in der Mitgliederliste eines Space.

Klicken Sie auf einen Benutzer, um **Benutzer bearbeiten** zu öffnen. Der Dialog zeigt jeden Space, dem der Benutzer angehört, und jede Rolle, die er darin hat, auch im Standard-Space:

- Den Benutzer zu einem weiteren Space hinzufügen oder ihm einen Space entziehen.
- Eine Rolle zwischen **Benutzer** und **Bereichsinhaber** wechseln.
- **Anwendungsinhaber** für den Benutzer ein- oder ausschalten.

**Benutzer hinzufügen** über der Liste öffnet denselben Dialog leer. So vergeben Sie Spaces und Rollen auch an Personen, die noch nicht aufgeführt sind. Adressen ohne Konto sind mit **Wird neu angelegt** markiert.

Klicken Sie auf **Speichern**, um die Änderungen zu übernehmen. Vor dem Speichern zeigt der Dialog, was passieren wird: welche Spaces **hinzugefügt** und welche **entzogen** werden und wessen Rolle sich ändert.

*\[Image: Dialog Benutzer bearbeiten mit den Spaces und Rollen des Benutzers]*

### [Ein Benutzer oder mehrere](https://docs.smartchat.ai.t-systems.net/de/user/admin/application-owner/#ein-benutzer-oder-mehrere)

Der Schalter neben **E-Mail** legt fest, wie viele Personen der Dialog ändert:

- **Ein Benutzer**: eine einzelne E-Mail-Adresse.
- **Mehrere Benutzer auf einmal**: eine E-Mail-Adresse pro Zeile. Die Zwischenablage-Schaltfläche neben den Zeilen übernimmt eine ganze Liste von Adressen auf einmal. Die Spaces, Rollen und die Einstellung **Anwendungsinhaber** darunter gelten für jeden aufgeführten Benutzer. Der Dialog weist Sie darauf hin, wenn eine Liste länger ist, als Ihre Instanz in einem Schritt erlaubt.

### [Hinzufügen oder ersetzen](https://docs.smartchat.ai.t-systems.net/de/user/admin/application-owner/#hinzuf%C3%BCgen-oder-ersetzen)

Der Schalter neben **Abbrechen** legt fest, was mit den Spaces geschieht, die die Benutzer bereits haben:

- **Hinzufügen** (Plus-Symbol): Die Benutzer behalten ihre bisherigen Spaces und erhalten die im Dialog aufgeführten dazu. Hinzufügen entzieht nichts, also auch nicht die Rolle **Anwendungsinhaber**.
- **Ersetzen** (Pfeil-Symbol): Die Benutzer haben danach genau die im Dialog aufgeführten Spaces und verlieren alle anderen. **Anwendungsinhaber** wird entzogen, wenn der Schalter dafür aus ist.

**Benutzer bearbeiten** startet mit **Ersetzen**, weil der Dialog bereits alle Spaces des Benutzers aufführt. **Benutzer hinzufügen** startet mit **Hinzufügen**. Ersetzen für mehrere Benutzer auf einmal zeigt eine Warnung, denn jeder von ihnen verliert alle Spaces, die nicht in der Liste stehen.

**Sie können sich die Rolle Anwendungsinhaber nicht selbst entziehen.** Bitten Sie einen anderen Anwendungsinhaber darum.

Spaces, die Ihr Identity Provider zuweist, bleiben zugewiesen, unabhängig davon, was Sie hier ändern.

### [Personen, die sich noch nie angemeldet haben](https://docs.smartchat.ai.t-systems.net/de/user/admin/application-owner/#personen-die-sich-noch-nie-angemeldet-haben)

Auf Instanzen mit aktivierter [Kontenanlage nur über Ihren Identity Provider](https://docs.smartchat.ai.t-systems.net/de/user/admin/single-sign-on/#kontenanlage-nur-%C3%BCber-ihren-identity-provider) lässt sich niemand zum ersten Mal in Smartchat und zugleich in einen Space aufnehmen: Das Konto entsteht erst bei der ersten Anmeldung. Warten Sie, bis sich die Person einmal per Single Sign-on angemeldet hat, und fügen Sie sie dann hinzu. Die beiden Dialoge zum Hinzufügen gehen mit einer solchen Person unterschiedlich um:

- **Benutzer hinzufügen** (hier unter **Benutzer**) lässt sie nicht speichern: **Speichern** bleibt deaktiviert, und der Dialog erklärt den Grund neben ihrer E-Mail-Adresse mit **Dieser Nutzer hat sich noch nicht angemeldet und kann daher nicht hinzugefügt werden.** Wenn Sie mehrere Benutzer auf einmal hinzufügen, entfernen Sie diese Adresse, um die übrigen zu speichern.
- **Neues Mitglied hinzufügen** (bei den Mitgliedern eines Spaces, siehe [Space-Mitglieder verwalten](https://docs.smartchat.ai.t-systems.net/de/user/admin/managing-space-members/)) merkt es erst, wenn Sie auf **Hinzufügen** klicken. Ein einzelnes Mitglied wird dann mit dem Hinweis abgelehnt, dass es sich noch nicht angemeldet hat. Fügen Sie mehrere Mitglieder auf einmal hinzu, wird die ganze Liste abgelehnt und jedes Mitglied darin als nicht hinzugefügt angezeigt.

## [Instanzeinstellungen](https://docs.smartchat.ai.t-systems.net/de/user/admin/application-owner/#instanzeinstellungen)

**Oberfläche** und **Codeausführung** enthalten Einstellungen für die gesamte Instanz, zum Beispiel Banner und die Prompt-Vorschläge auf dem Startbildschirm. Änderungen wirken sich auf alle Benutzer aus.

Für den Agenten-Modus gibt es eigene Einstellungen, siehe [Einstellungen des Agenten-Modus](https://docs.smartchat.ai.t-systems.net/de/user/admin/agent-mode/).
