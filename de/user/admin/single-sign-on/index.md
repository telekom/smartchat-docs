# Single Sign-on

Source: https://docs.smartchat.ai.t-systems.net/de/user/admin/single-sign-on/

> Wie sich Personen über Ihren Identity Provider bei Smartchat anmelden, wie IdP-Attribute auf Space- und Gruppenmitgliedschaft abgebildet werden, und die Optionen, mit denen Ihr Identity Provider entscheidet, wer ein Konto hat und welche Rollen er erhält.

Mit Single Sign-on (SSO) melden sich Personen mit ihrem Firmenkonto bei Smartchat an. Smartchat leitet sie an Ihren Identity Provider weiter, zum Beispiel Microsoft Entra ID oder Active Directory Federation Services (ADFS), der ihr Passwort und einen etwaigen zweiten Faktor prüft. Name und E-Mail-Adresse kommen aus Ihrem Identity Provider und lassen sich in Smartchat nicht bearbeiten.

T-Systems richtet Single Sign-on gemeinsam mit den Administratoren Ihres Identity Providers ein und konfiguriert die Optionen auf dieser Seite für Ihre Instanz. Wenden Sie sich an T-Systems, um eine Option ein- oder auszuschalten oder um zu ändern, welche Werte Smartchat aus Ihrem Identity Provider liest.

## [IdP-Attribute abbilden](https://docs.smartchat.ai.t-systems.net/de/user/admin/single-sign-on/#idp-attribute-abbilden)

Ihr Identity Provider kann bei jeder Anmeldung IdP-Attribute der Person mitsenden, auch Claims genannt, zum Beispiel eine Rolle oder Gruppe, die sie in Ihrem Active Directory hat. Smartchat kann ein IdP-Attribut auf zwei Arten abbilden:

| Abbildung | Eingerichtet von | Wo |
| - | - | - |
| [IdP-Attribut auf Space-Mitgliedschaft](https://docs.smartchat.ai.t-systems.net/de/user/admin/single-sign-on/#idp-attribut-auf-space-mitgliedschaft) | Anwendungsinhabern | **Anwendungsinhaber → Bereiche**, Feld **IdP-Attribut für automatische Zuordnung** |
| [IdP-Attribut auf Gruppenmitgliedschaft innerhalb eines Spaces](https://docs.smartchat.ai.t-systems.net/de/user/admin/single-sign-on/#idp-attribut-auf-gruppenmitgliedschaft-innerhalb-eines-spaces) | Space Ownern | **Bereichsinhaber → Gruppen**, Feld **Gruppenattribute des Identitätsanbieters** |

Tragen Sie das IdP-Attribut in beiden Fällen genau so ein, wie Ihr Identity Provider es sendet, einschließlich Schreibweise sowie Groß- und Kleinschreibung. Fragen Sie die Administratoren Ihres Identity Providers nach den genauen Werten.

Smartchat liest die IdP-Attribute bei jeder Anmeldung. Sendet Ihr Identity Provider ein IdP-Attribut neu, erhält die Person bei ihrer nächsten Anmeldung, worauf es abgebildet ist. Sendet er es nicht mehr, verliert sie es bei ihrer nächsten Anmeldung. Was Ihr Identity Provider zuweist, lässt sich in der Administration nicht entziehen.

### [IdP-Attribut auf Space-Mitgliedschaft](https://docs.smartchat.ai.t-systems.net/de/user/admin/single-sign-on/#idp-attribut-auf-space-mitgliedschaft)

Jeder Space kann ein **IdP-Attribut für automatische Zuordnung** haben, festgelegt unter **Administration → Anwendungsinhaber → Bereiche**, siehe [Spaces und Benutzer verwalten](https://docs.smartchat.ai.t-systems.net/de/user/admin/application-owner/). Wessen Identity Provider dieses IdP-Attribut sendet, wird **Benutzer** des Spaces. Mehrere Spaces können dasselbe IdP-Attribut haben.

Weitere IdP-Attribute, bei der Einrichtung mit T-Systems vereinbart, vergeben Rollen:

- **Space Owner eines Spaces**: Das IdP-Attribut des Spaces mit einer Space-Owner-Kennzeichnung macht die Person zum **Space Owner** dieses Spaces. Hat noch kein Space das IdP-Attribut, legt Smartchat den Space an, benennt ihn nach dem IdP-Attribut und setzt das IdP-Attribut. Gibt es bereits einen Space dieses Namens ohne das IdP-Attribut, weist Smartchat nichts zu: Setzen Sie das IdP-Attribut an diesem Space.
- **Space Owner überall**: macht die Person in jedem Space, den sie über Ihren Identity Provider erhält, zum **Space Owner** statt zum **Benutzer**.
- **Anwendungsinhaber**: macht die Person zum **Anwendungsinhaber**.

### [IdP-Attribut auf Gruppenmitgliedschaft innerhalb eines Spaces](https://docs.smartchat.ai.t-systems.net/de/user/admin/single-sign-on/#idp-attribut-auf-gruppenmitgliedschaft-innerhalb-eines-spaces)

Space Owner ordnen die Mitglieder ihres Spaces unter **Administration → Bereichsinhaber → Gruppen** in [Gruppen](https://docs.smartchat.ai.t-systems.net/de/user/concepts/groups/). Eine Gruppe kann **Gruppenattribute des Identitätsanbieters** enthalten: Wessen Identity Provider eines dieser IdP-Attribute sendet, wird zur Gruppe hinzugefügt. Die Gruppe zeigt diese Personen mit **Wird vom Identitätsanbieter verwaltet und kann nicht manuell entfernt werden.**

Das legt nur die Gruppenmitgliedschaft fest. Es nimmt niemanden in den Space auf: In einen Space kommen Personen über [IdP-Attribut auf Space-Mitgliedschaft](https://docs.smartchat.ai.t-systems.net/de/user/admin/single-sign-on/#idp-attribut-auf-space-mitgliedschaft), [Space-Mitgliedschaft nach E-Mail-Domain](https://docs.smartchat.ai.t-systems.net/de/user/admin/single-sign-on/#space-mitgliedschaft-nach-e-mail-domain) oder einen Administrator.

## [Space-Mitgliedschaft nach E-Mail-Domain](https://docs.smartchat.ai.t-systems.net/de/user/admin/single-sign-on/#space-mitgliedschaft-nach-e-mail-domain)

Smartchat kann alle, deren E-Mail-Adresse zu einer Domain gehört, zum Beispiel `example.com`, bei der Anmeldung als **Benutzer** in einen Space aufnehmen. Dafür sind keine IdP-Attribute aus Ihrem Identity Provider nötig. Entfernen Sie eine solche Person aus dem Space, gilt das nur bis zu ihrer nächsten Anmeldung, bei der Smartchat sie wieder aufnimmt. Die Einstellungen dieses Spaces lassen sich in der Administration nicht ändern.

## [Optionale Einschränkungen](https://docs.smartchat.ai.t-systems.net/de/user/admin/single-sign-on/#optionale-einschr%C3%A4nkungen)

T-Systems kann diese Optionen für Ihre Instanz aktivieren. Standardmäßig sind beide aus.

### [Kontenanlage nur über Ihren Identity Provider](https://docs.smartchat.ai.t-systems.net/de/user/admin/single-sign-on/#kontenanlage-nur-%C3%BCber-ihren-identity-provider)

Ist diese Option aktiviert, lassen sich in Smartchat keine Konten direkt anlegen. Stattdessen wird das Konto einer Person angelegt, wenn sie sich zum ersten Mal per Single Sign-on anmeldet. In der Administration gilt:

- Personen, die sich noch nie angemeldet haben, lassen sich noch keinem Space hinzufügen. Siehe [Personen, die sich noch nie angemeldet haben](https://docs.smartchat.ai.t-systems.net/de/user/admin/application-owner/#personen-die-sich-noch-nie-angemeldet-haben).
- Benutzer lassen sich nicht löschen.
- Bestehende Benutzer Spaces zuzuweisen und ihre Rollen zu ändern funktioniert wie gewohnt.

**Benutzer** unter **Anwendungsinhaber** zeigt: **Die Benutzer werden vom Identity Provider verwaltet und lassen sich hier weder anlegen noch löschen. Ihre Bereiche und Rollen lassen sich weiterhin ändern.**

### [Mitglieder- und Rollenverwaltung nur über Ihren Identity Provider](https://docs.smartchat.ai.t-systems.net/de/user/admin/single-sign-on/#mitglieder--und-rollenverwaltung-nur-%C3%BCber-ihren-identity-provider)

Ist diese Option aktiviert, entscheidet allein Ihr Identity Provider, wer zu welchem Space gehört und mit welcher Rolle. Sie umfasst alles aus [Kontenanlage nur über Ihren Identity Provider](https://docs.smartchat.ai.t-systems.net/de/user/admin/single-sign-on/#kontenanlage-nur-%C3%BCber-ihren-identity-provider) und zusätzlich:

- Weder Anwendungsinhaber noch Space Owner können in der Administration Mitglieder hinzufügen oder entfernen oder eine Rolle ändern. Die Administration zeigt **Der Identitätsanbieter verwaltet Benutzer und Rollen. Sie lassen sich hier nicht ändern.**
- Jeder Space braucht ein **IdP-Attribut für automatische Zuordnung**. Ohne IdP-Attribut lässt sich ein Space weder anlegen noch speichern, denn nur über das IdP-Attribut kommen Personen in den Space.
