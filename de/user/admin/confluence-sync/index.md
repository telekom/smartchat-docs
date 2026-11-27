# Confluence-Synchronisation

Source: https://docs.smartchat.ai.t-systems.net/de/user/admin/confluence-sync/

> So verbinden Sie einen Confluence-Data-Center-Space mit Ihrem Smartchat-Space für die automatische Synchronisation.

Diese Anleitung erklärt, wie Sie eine Verbindung zwischen Ihrem Smartchat-Space und einer Confluence-Data-Center-Instanz einrichten. Nach der Verbindung synchronisiert Smartchat die Confluence-Seiten jede Nacht, sodass sie durchsuchbar sind und als Kontext für Ihre Unterhaltungen bereitstehen.

> **Hinweis**
>
> Diese Funktion ist für **Confluence Data Center 9.2.x** ausgelegt. Andere Versionen funktionieren möglicherweise, sind aber nicht offiziell getestet. Confluence Cloud wird derzeit nicht unterstützt.
>
> Details zu dieser Version finden Sie in der [Atlassian-Dokumentation zu Confluence Data Center 9.2](https://confluence.atlassian.com/conf92/confluence-data-center-documentation-1477575463.html).

## [Voraussetzungen](https://docs.smartchat.ai.t-systems.net/de/user/admin/confluence-sync/#voraussetzungen)

- Sie benötigen die Rolle **Space Owner** im Smartchat-Space. Details unter [Rollen](https://docs.smartchat.ai.t-systems.net/de/user/concepts/roles/).
- Ein **Service-Account-Token** oder ein **Personal Access Token** (PAT) des Confluence-Servers, den Sie synchronisieren möchten. Fragen Sie Ihren Confluence-Administrator, wenn Sie nicht wissen, wie Sie eines erhalten.
- Datenverbindungen müssen in Ihrer Smartchat-Umgebung aktiviert sein. Fehlt die Seite **Datenverbindungen**, wenden Sie sich an Ihren Anwendungsinhaber.

> **Verstehen Sie, was synchronisiert wird**
>
> Der Synchronisationsprozess hat Zugriff auf **alle Seiten, die für das angegebene Benutzerkonto sichtbar sind**. Er kann keine Seiten synchronisieren, die der Benutzer nicht sehen kann, aber er **wird** alles synchronisieren, was der Benutzer sehen **kann**, einschließlich Seiten, die als privat oder sensibel gelten.
>
> Stellen Sie vorab sicher, dass Sie berechtigt sind, all diese Inhalte mit allen Personen zu teilen, die Zugriff auf den Smartchat-Space haben.

## [Schritt 1 — Datenverbindungen öffnen](https://docs.smartchat.ai.t-systems.net/de/user/admin/confluence-sync/#schritt-1--datenverbindungen-%C3%B6ffnen)

Klicken Sie auf Ihr Profilbild, wählen Sie **Administration** und wählen Sie unter **Bereichsinhaber** im Feld **Aktueller Bereich** den zu konfigurierenden Space. Öffnen Sie dann **Datenverbindungen**. Sie sehen eine Tabelle mit allen vorhandenen Verbindungen dieses Spaces.

*\[Image: Seite Datenverbindungen mit einer Verbindung]*

## [Schritt 2 — Neue Verbindung anlegen](https://docs.smartchat.ai.t-systems.net/de/user/admin/confluence-sync/#schritt-2--neue-verbindung-anlegen)

Klicken Sie auf **Datenverbindung hinzufügen**. Das Formular hat drei Abschnitte:

*\[Image: Formular Datenverbindung hinzufügen]*

**Quelle**

| Feld | Beschreibung |
| - | - |
| **Art** | Wählen Sie **Confluence**. |
| **Name** | Ein Name für die Verbindung: 3 bis 64 Buchstaben, Ziffern, `-` oder `_`, keine Leerzeichen. Der Name identifiziert die Verbindung und kann später nicht geändert werden. |
| **URL** | Die Basis-URL Ihrer Confluence-Instanz, z. B. `https://example.com/confluence/` |
| **Space-Schlüssel** | Der Confluence-**Space Key**, der synchronisiert werden soll. Das ist das kurze Präfix in Confluence-URLs. Lauten Ihre Seiten-URLs z. B. `https://example.com/confluence/spaces/DOCS/pages/...`, ist der Space Key `DOCS`. |

**Zugangsdaten**

| Feld | Beschreibung |
| - | - |
| **Authentifizierung** | **BASIC AUTH** für Benutzername plus Token oder Passwort, **BEARER TOKEN** für ein allein gesendetes Token. |
| **Benutzername** | Der Benutzername des Service- oder persönlichen Kontos (nur Basic Auth). |
| **Passwort oder Token** | Das zugehörige Zugriffstoken oder Passwort. |

**Synchronisierung**

| Feld | Beschreibung |
| - | - |
| **Zielkollektion** | Wo die synchronisierten Seiten landen. **Allgemeine Kollektion** ist die Standardkollektion des Spaces, sichtbar für jedes Mitglied; wählen Sie eine andere Kollektion des Spaces, um stattdessen dorthin zu synchronisieren. |
| **Aktiv** | Eingeschaltet lassen. Inaktive Verbindungen behalten ihre Einstellungen, werden aber von der nächtlichen Synchronisation übersprungen. |

> **Telekom Wiki (wiki.telekom.de)**
>
> Wenn Sie das interne **Telekom Wiki** anbinden, verwenden Sie diese Werte:
>
> - **URL**: `https://wiki.telekom.de/` (nicht mehr: kein `/wiki`, kein Pfad)
> - **Authentifizierung**: **BASIC AUTH**
> - **Benutzername**: Ihr Telekom-Wiki-Benutzername. Dieser ist **case-sensitive**; verwenden Sie für das Telekom Wiki Ihre E-Mail-Adresse in **Kleinbuchstaben**
> - **Passwort oder Token**: ein **API-Token**, das Sie unter [wiki.telekom.de → API-Tokens](https://wiki.telekom.de/plugins/servlet/no.kantega.kerberosauth.kerberosauth-plugin/user/api-tokens) generieren

> **Verwenden Sie nicht Ihr echtes Passwort**
>
> Auch bei **BASIC AUTH** tragen Sie das generierte **API-Token** in das Feld **Passwort oder Token** ein, nicht Ihr echtes Kontopasswort. „Basic Auth“ bedeutet hier „Benutzername und Token als HTTP-Basic-Credentials senden“, nicht „Ihr Login-Passwort senden“.

## [Schritt 3 — Testen und speichern](https://docs.smartchat.ai.t-systems.net/de/user/admin/confluence-sync/#schritt-3--testen-und-speichern)

Klicken Sie unten im Formular auf **Verbindung testen**. Das Ergebnis-Badge neben der Schaltfläche zeigt, ob Smartchat den Confluence-Space mit diesen Zugangsdaten erreichen konnte (mögliche Ergebnisse siehe [Fehlerbehebung](https://docs.smartchat.ai.t-systems.net/de/user/admin/confluence-sync/#fehlerbehebung)).

Klicken Sie auf **Speichern**. Bei Erfolg erscheint die Meldung **Verbindung gespeichert und nächtliche Synchronisierung eingeplant.**, und die Verbindung wird in der Tabelle gelistet. Schlägt der Test fehl, wird die Verbindung trotzdem gespeichert, ihre Synchronisation bleibt aber pausiert, bis Sie die Einstellungen korrigieren und erneut speichern.

## [Schritt 4 — Verbindung prüfen](https://docs.smartchat.ai.t-systems.net/de/user/admin/confluence-sync/#schritt-4--verbindung-pr%C3%BCfen)

*\[Image: Verbindungszeile mit Status und Aktionen]*

| Spalte | Bedeutung |
| - | - |
| **Status** | **Aktiv** (grün) oder **Inaktiv**. |
| **Dokumente** | Anzahl der bisher synchronisierten Seiten. |
| **Nächste Synchronisierung** | Wann der nächste nächtliche Lauf fällig ist, oder **Pausiert**. |
| **Letzte Synchronisierung** | Datum des letzten erfolgreichen Laufs. |

Ein Klick auf den **Namen** der Verbindung kopiert ihn in die Zwischenablage.

## [Anhänge](https://docs.smartchat.ai.t-systems.net/de/user/admin/confluence-sync/#anh%C3%A4nge)

Neben den Seiten synchronisiert Smartchat auch die Anhänge der synchronisierten Seiten in dieselbe **Zielkollektion**. Standardmäßig werden Anhänge dieser Typen bis jeweils 50 MB synchronisiert: PDF, Word (`doc`, `docx`), PowerPoint (`ppt`, `pptx`), Excel (`xls`, `xlsx`), `csv`, `txt`, `md`, `html`, `xml`, `json`, `rtf`, `epub`, `msg`, `mbox` und `mp3`. Wird ein Anhang oder seine Seite in Confluence gelöscht, wird er auch aus dem Space entfernt.

## [Synchronisierungszeitplan](https://docs.smartchat.ai.t-systems.net/de/user/admin/confluence-sync/#synchronisierungszeitplan)

- Die Synchronisation läuft automatisch jede Nacht. Die Spalte **Nächste Synchronisierung** zeigt die genaue Uhrzeit.
- Die erste Synchronisation importiert alle Seiten und kann je nach Umfang der Inhalte zwischen wenigen Minuten und mehreren Stunden dauern.
- Nachfolgende Synchronisationen verarbeiten nur Änderungen und sind in der Regel deutlich schneller.

## [Verbindungen verwalten](https://docs.smartchat.ai.t-systems.net/de/user/admin/confluence-sync/#verbindungen-verwalten)

Jede Zeile hat rechts eine Reihe von Aktionsschaltflächen:

| Schaltfläche | Aktion |
| - | - |
| **Verbindung testen** | Prüft, ob URL und Zugangsdaten noch gültig sind. Das Ergebnis erscheint als Meldung. |
| **Jetzt synchronisieren** | Startet sofort eine inkrementelle Synchronisation. Smartchat verfolgt den Lauf und meldet **Synchronisierung von … abgeschlossen.** oder **… fehlgeschlagen.** Im Normalfall reicht die nächtliche Synchronisation aus. |
| **Neu indizieren** | Importiert **alle** Inhalte aus Confluence neu statt nur die Änderungen. Nutzen Sie es nach einem Wechsel der Zielkollektion oder wenn Seiten fehlen. Das kann lange dauern und belastet den Confluence-Server, deshalb ist es nach 20:00 Uhr deaktiviert. |
| **Datenverbindung bearbeiten** | URL, Schlüssel, Zugangsdaten, Zielkollektion oder den Schalter **Aktiv** ändern. Lassen Sie die Zugangsdaten leer, um die gespeicherten zu behalten; geben Sie sie erneut ein, um vor dem Speichern zu testen. Name und Art sind fest. |
| **Datenverbindung entfernen** | Löscht die Verbindung und ihren Zeitplan. Bereits in den Space synchronisierte Inhalte **bleiben erhalten**. |

*\[Image: Bestätigungsdialog Neu indizieren]*

> **Synchronisierungsstatus prüfen**
>
> Space Owner können den Fortschritt der Synchronisation in der Zielkollektion unter **Arbeitsbereich → Wissen** verfolgen. Synchronisierte Seiten tragen das Confluence-Symbol. Jede Datei zeigt einen **Status**: **Ingested** bedeutet, dass die Seite erfolgreich verarbeitet wurde. Jeder andere Status weist auf einen Fehler hin, siehe [Ingestion-Fehler](https://docs.smartchat.ai.t-systems.net/de/user/files/ingestion-errors/).

## [Zugriff auf die Daten](https://docs.smartchat.ai.t-systems.net/de/user/admin/confluence-sync/#zugriff-auf-die-daten)

Nach Abschluss der Synchronisation stehen die Confluence-Inhalte in der Smartchat-Chat-Oberfläche zur Verfügung.

> **Achtung**
>
> Synchronisierte Daten werden **nicht** automatisch als Kontext geladen. Die Zielkollektion muss zuerst ausgewählt werden.

1. Wählen Sie den Space über den **Space-Selector** oben links aus.
2. Fügen Sie die Zielkollektion (standardmäßig **„{Space Name} - General“**) mit dem **#**-Shortcut zum Chat hinzu.

*\[Image: Kollektionen: General-Space-Kollektion mit # hinzufügen]*

## [Fehlerbehebung](https://docs.smartchat.ai.t-systems.net/de/user/admin/confluence-sync/#fehlerbehebung)

Der Verbindungstest liefert eines der folgenden Ergebnisse:

| Ergebnis | Bedeutung |
| - | - |
| **WORKS** | Die Verbindung ist funktionsfähig. |
| **CONNECTION\_ERROR** | Smartchat kann den Server nicht erreichen (Timeout, DNS-Fehler, Verbindung abgelehnt). |
| **MISSING\_CREDENTIALS** | Kein Benutzername oder Secret wurde angegeben. |
| **HTTP\_AUTH\_FAILED** | Die Zugangsdaten wurden abgelehnt (falscher Benutzername/falsches Passwort oder abgelaufenes Token). |
| **HTTP\_ERROR\_400** | Die Anfrage ist fehlerhaft (meist ein falscher URL-Pfad oder fehlende Parameter). |
| **HTTP\_ERROR\_404** | Die URL oder der Space Key wurde auf dem Server nicht gefunden. |
| **HTTP\_ERROR\_4XX** | Ein anderer clientseitiger Fehler (z. B. 403 Forbidden, 429 Rate Limited). |
| **HTTP\_ERROR\_500** | Interner Serverfehler auf Confluence-Seite. |
| **HTTP\_ERROR\_5XX** | Ein anderer serverseitiger Fehler auf Confluence-Seite. |
| **HTTP\_ERROR** | Ein nicht klassifizierter HTTP-Fehler. |
| **INVALID\_RESPONSE** | Der Server hat geantwortet, aber nicht mit der erwarteten Confluence-API-Antwort, meist ein falscher URL-Pfad. |
| **FAILED** | Ein unerwarteter Fehler ist aufgetreten. |

### [CONNECTION\_ERROR](https://docs.smartchat.ai.t-systems.net/de/user/admin/confluence-sync/#connection_error)

**Ursache:** Der Confluence-Server ist nicht erreichbar. Die URL ist möglicherweise falsch, der Server nicht verfügbar oder es liegt ein Netzwerk-/Firewall-Problem vor.

**Lösung:** Überprüfen Sie die Confluence-Basis-URL. Data-Center-Instanzen verwenden typischerweise einen Pfad wie `https://your-server.example.com/confluence/`. Verwenden Sie die API-Basis-URL, nicht die URL, die Sie beim Navigieren im Browser sehen.

### [HTTP\_AUTH\_FAILED](https://docs.smartchat.ai.t-systems.net/de/user/admin/confluence-sync/#http_auth_failed)

**Ursache:** Der Benutzername oder das Passwort ist falsch, oder das API-Token ist abgelaufen oder wurde widerrufen.

**Lösung:** Erstellen Sie das API-Token in Ihren Confluence-Kontoeinstellungen neu und prüfen Sie, ob der Benutzername zum Token-Inhaber passt.

### [HTTP\_ERROR\_404](https://docs.smartchat.ai.t-systems.net/de/user/admin/confluence-sync/#http_error_404)

**Ursache:** Entweder ist der URL-Pfad falsch (z. B. mit oder ohne `/wiki`), oder der Space Key ist falsch. Möglicherweise wurde der Anzeigename statt des Space Keys verwendet, oder es liegt ein Tippfehler vor. Space Keys unterscheiden Groß- und Kleinschreibung.

**Lösung:** Prüfen Sie zuerst den URL-Pfad. Schlagen Sie dann den korrekten Space Key in Confluence unter **Settings → Space details** nach.

### [Einrichtung erfolgreich, aber Ingestion oder Chat schlägt fehl](https://docs.smartchat.ai.t-systems.net/de/user/admin/confluence-sync/#einrichtung-erfolgreich-aber-ingestion-oder-chat-schl%C3%A4gt-fehl)

**Ursache:** Die Konfiguration des Smartchat-Spaces ist unvollständig (kein API-Schlüssel oder Standardmodell gesetzt). Alternativ drosselt Confluence die API mit einer `429`-Antwort, weil zu viele Seiten gleichzeitig abgefragt werden.

**Lösung:** Stellen Sie sicher, dass der Space über einen gültigen [API-Schlüssel und ein Standardmodell](https://docs.smartchat.ai.t-systems.net/de/user/admin/space-settings/) verfügt, bevor Sie die Confluence-Synchronisation einrichten. Bei Ratenbegrenzung wenden Sie sich an Ihren Confluence-Administrator. Den Ingestion-Status sehen Sie in der Zielkollektion.

### [Einige oder alle Seiten fehlen nach der Ingestion](https://docs.smartchat.ai.t-systems.net/de/user/admin/confluence-sync/#einige-oder-alle-seiten-fehlen-nach-der-ingestion)

**Ursache:** Der Inhaber des API-Tokens hat keinen Zugriff auf den Confluence-Space, oder einzelne Seiten haben eingeschränkte Berechtigungen, die den Token-Inhaber ausschließen.

**Lösung:** Stellen Sie sicher, dass der Token-Inhaber **Lesezugriff** auf den Ziel-Confluence-Space und alle darin enthaltenen Seiten hat. Klären Sie seitenbezogene Einschränkungen mit Ihrem Confluence-Administrator. Führen Sie anschließend **Neu indizieren** aus.
