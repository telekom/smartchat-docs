# Space-Mitglieder verwalten

Source: https://docs.smartchat.ai.t-systems.net/de/user/admin/managing-space-members/

> Mitglieder Ihres Spaces hinzufügen und entfernen und zum Space Owner ernennen, direkt in Smartchat.

Space Owner verwalten unter **Administration → Bereichsinhaber → Bereichsmitglieder**, wer zu ihrem Space gehört. Die Seite wird nur Space Ownern angezeigt und wirkt auf den Space, der unter **Aktueller Bereich** ausgewählt ist.

*\[Image: Seite Bereichsmitglieder mit den Rollenschaltern und der Schaltfläche Benutzer hinzufügen]*

Die Liste zeigt jedes Mitglied des Spaces mit vier Spalten:

| Spalte | Bedeutung |
| - | - |
| **Rolle** | **Benutzer** oder **Bereichsinhaber**. Klicken Sie auf die andere Hälfte des Schalters, um die Rolle zu ändern (siehe unten). |
| **E-Mail** | Der Login des Mitglieds. Ein Klick öffnet die Details des Mitglieds. |
| **Zuletzt aktiv** | Wann das Mitglied Smartchat zuletzt genutzt hat. Mitglieder, die sich noch nie angemeldet haben, zeigen kein Datum. |
| **Erstellt am** | Wann das Konto angelegt wurde. |

## [Mitglied hinzufügen](https://docs.smartchat.ai.t-systems.net/de/user/admin/managing-space-members/#mitglied-hinzuf%C3%BCgen)

1. Klicken Sie über der Liste auf **Benutzer hinzufügen**.
2. Geben Sie im Dialog **Neues Mitglied hinzufügen** die **E-Mail** der Person ein und klicken Sie auf **Hinzufügen**.

*\[Image: Dialog Neues Mitglied hinzufügen]*

Was danach passiert, hängt von der E-Mail-Adresse ab:

- **Die Person hat bereits ein Smartchat-Konto**: sie wird dem Space mit der Rolle **Benutzer** hinzugefügt und sieht ihn beim nächsten Laden der Seite im Space-Selector.
- **Die E-Mail ist unbekannt**: es wird ein Konto für die Person angelegt. Sie erhält eine Einladungs-E-Mail vom Identity Provider und erscheint schon vor der ersten Anmeldung mit der Rolle **Benutzer** in der Liste. Auf Instanzen mit aktivierter [Kontenanlage nur über Ihren Identity Provider](https://docs.smartchat.ai.t-systems.net/de/user/admin/single-sign-on/#kontenanlage-nur-%C3%BCber-ihren-identity-provider) muss sich die Person zuerst einmal anmelden, bevor Sie sie hinzufügen können.

Neue Mitglieder können sofort chatten und die mit ihnen geteilten Elemente nutzen, etwa die Kollektion **{Space} - Allgemein**. Damit sie den Space verwalten, ernennen Sie sie zum Space Owner.

> **Seats**
>
> Wenn Ihr Vertrag die Anzahl der Seats in einem Space begrenzt, schlägt das Hinzufügen über dieses Limit hinaus mit einem Lizenzfehler fehl. Wenden Sie sich an den Support, um das Limit zu erhöhen.

## [Mehrere Mitglieder auf einmal hinzufügen](https://docs.smartchat.ai.t-systems.net/de/user/admin/managing-space-members/#mehrere-mitglieder-auf-einmal-hinzuf%C3%BCgen)

Um ein ganzes Team hinzuzufügen, stellen Sie den Dialog **Neues Mitglied hinzufügen** auf **Mehrere Mitglieder auf einmal** (das Symbol neben dem Titel) um und fügen die E-Mail-Adressen in das Textfeld ein. Eine Adresse pro Zeile, durch Kommas oder Semikolons getrennt, kopierte Empfänger aus Outlook (`"Doe, Jane" <jane.doe@example.com>`) und eine kopierte Spalte aus Excel funktionieren gleichermaßen; Duplikate werden automatisch entfernt.

Unter dem Feld sehen Sie, wie viele Adressen erkannt wurden. Einträge, die keine E-Mail-Adressen sind, werden rot aufgelistet und müssen korrigiert oder entfernt werden, bevor **Hinzufügen** verfügbar wird. Klicken Sie dann auf **N Mitglieder hinzufügen**.

Jede Adresse wird wie ein einzelnes Hinzufügen behandelt: bestehende Konten werden dem Space hinzugefügt, unbekannte Adressen erhalten ein Konto und eine Einladungs-E-Mail. Nach Abschluss meldet der Dialog, wie viele Mitglieder hinzugefügt wurden, und listet alle Adressen mit Begründung auf, die nicht hinzugefügt werden konnten. **Fehlgeschlagene E-Mail-Adressen kopieren** legt diese in die Zwischenablage, sodass Sie sie korrigieren und erneut versuchen können; bereits hinzugefügte Mitglieder werden bei einem erneuten Versuch übersprungen.

> **Limit**
>
> Bis zu 100 Mitglieder können auf einmal hinzugefügt werden. Für größere Gruppen ist eine Identity-Provider-Anbindung (zum Beispiel Entra ID) die bessere Lösung. Wenden Sie sich an T-Systems.

## [Rolle eines Mitglieds ändern](https://docs.smartchat.ai.t-systems.net/de/user/admin/managing-space-members/#rolle-eines-mitglieds-%C3%A4ndern)

Ein Space kennt zwei Rollen: **Benutzer** und **Bereichsinhaber** (Space Owner). Owner erhalten alles, was unter [Administration](https://docs.smartchat.ai.t-systems.net/de/user/admin/) beschrieben ist; die vollständige Matrix finden Sie unter [Rollen](https://docs.smartchat.ai.t-systems.net/de/user/concepts/roles/).

Verwenden Sie entweder den Schalter **Rolle** in der Liste oder öffnen Sie das Mitglied (Klick auf die E-Mail) und verwenden Sie den Schalter **Rolle** im Dialog **Mitglied bearbeiten**.

*\[Image: Dialog Mitglied bearbeiten mit dem Rollenschalter]*

Die neue Rolle wird sofort übernommen, es gibt keinen separaten Speichern-Schritt. Schlägt die Aktualisierung fehl, springt der Schalter zurück und eine Meldung erklärt den Grund.

Zwei Regeln gelten:

- **Sie können Ihre eigene Rolle nicht ändern.** Der Schalter in Ihrer eigenen Zeile ist ausgegraut. Bitten Sie einen anderen Owner, Sie zu befördern oder herabzustufen.
- **Ein Space behält mindestens einen Owner.** Der letzte verbleibende Owner kann weder herabgestuft noch entfernt werden, solange der Space weitere Mitglieder hat.

## [Mitglied entfernen](https://docs.smartchat.ai.t-systems.net/de/user/admin/managing-space-members/#mitglied-entfernen)

1. Fahren Sie mit der Maus über die Zeile des Mitglieds und klicken Sie auf das Papierkorb-Symbol (**Benutzer entfernen**), oder öffnen Sie das Mitglied und klicken Sie im Dialog **Mitglied bearbeiten** auf **Löschen**.
2. Bestätigen Sie mit **Entfernen**.

*\[Image: Bestätigung Benutzer entfernen]*

Die Person verliert sofort den Zugriff auf den Space: Sie wird aus dem Space selbst und aus allen seinen Gruppen entfernt, auch aus eigenen Gruppen. Ihr Smartchat-Konto und ihre anderen Spaces bleiben unberührt. Sich selbst können Sie nicht entfernen.

## [Einschränkungen](https://docs.smartchat.ai.t-systems.net/de/user/admin/managing-space-members/#einschr%C3%A4nkungen)

- **Gruppe der Space Owner**: Die Gruppe **SpaceOwners {Space}** spiegelt die oben beschriebenen Rollen wider und kann nicht bearbeitet werden, siehe [Gruppen](https://docs.smartchat.ai.t-systems.net/de/user/concepts/groups/#gruppen-die-jeder-space-hat). Space Owner haben jede [Berechtigung](https://docs.smartchat.ai.t-systems.net/de/user/concepts/permissions/#space-owner) ihres Space.
- **Anwendungsinhaber**, die nicht Owner eines Spaces sind, können hier keine Mitglieder dieses Spaces hinzufügen oder entfernen. Sie verwalten Space-Mitgliedschaften pro Benutzer unter [**Anwendungsinhaber → Benutzer**](https://docs.smartchat.ai.t-systems.net/de/user/admin/application-owner/#benutzer).

> **Wer Konten löschen kann**
>
> Seit v3.15.1 kann ein Space Owner das Konto eines Benutzers löschen, der keinem Space mehr angehört. Nur Anwendungsinhaber können das Konto eines Benutzers mit einer Rolle auf Anwendungsebene löschen, etwa eines Anwendungsinhabers, und auf Instanzen, die Konten über den Identity Provider verwalten, können nur Anwendungsinhaber überhaupt Konten löschen.

> **Identitätsfelder sind gesperrt**
>
> **E-Mail** und **Benutzername** eines bestehenden Mitglieds lassen sich in Smartchat nicht bearbeiten. Namens- und E-Mail-Änderungen kommen aus Ihrem Identity Provider.
