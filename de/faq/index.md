# FAQ

Source: https://docs.smartchat.ai.t-systems.net/de/faq/

> Antworten auf häufige Fragen zu Smartchat — Integrationen, Sicherheit, Spaces und Gruppen, große Dokumentensammlungen, Skills und Modelle.

Kurze Antworten auf häufige Fragen zu Smartchat.

## [Konto und Anmeldung](https://docs.smartchat.ai.t-systems.net/de/faq/#konto-und-anmeldung)

### [Mein Anmeldelink ist abgelaufen. Was kann ich tun?](https://docs.smartchat.ai.t-systems.net/de/faq/#mein-anmeldelink-ist-abgelaufen-was-kann-ich-tun)

Verwenden Sie **Passwort vergessen** auf dem Anmeldebildschirm von Smartchat. Geben Sie Ihre E-Mail-Adresse ein, und Sie erhalten eine E-Mail mit einem neuen Link, über den Sie Ihr Passwort festlegen. Siehe auch [Registrierung](https://docs.smartchat.ai.t-systems.net/de/user/guide/getting-started/#registrierung).

## [Integrationen und Lösungsentwicklung](https://docs.smartchat.ai.t-systems.net/de/faq/#integrationen-und-l%C3%B6sungsentwicklung)

### [Kann Smartchat Tools ansprechen, die auf dem Rechner eines Benutzers installiert sind?](https://docs.smartchat.ai.t-systems.net/de/faq/#kann-smartchat-tools-ansprechen-die-auf-dem-rechner-eines-benutzers-installiert-sind)

Nicht direkt. Smartchat läuft in der Cloud und kann keine Software erreichen, die auf einem einzelnen Laptop installiert ist.

Tools und Datenquellen werden über das [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) als [Connectors](https://docs.smartchat.ai.t-systems.net/de/user/agents/connectors/) für Agenten angebunden:

- Wir betreiben und stellen keine MCP-Server bereit. Smartchat bindet bestehende MCP-Server an, die Ihre Organisation verwaltet und die über das Internet erreichbar sind.
- MCP-Server müssen Dynamic Client Registration unterstützen.
- Ein Administrator stellt jeden Connector bereit. Benutzer autorisieren danach ihren eigenen Zugriff darauf.

Betreibt Ihre Organisation für ein Tool einen MCP-Server, der über das Internet erreichbar ist, kann ein Agent mit dem Tool arbeiten.

Der Agenten-Modus und Connectors befinden sich derzeit in der Preview.

### [Können Benutzer eigene Projekte erstellen, sie mit GitHub verbinden und Anwendungen wie HTML-Seiten hosten?](https://docs.smartchat.ai.t-systems.net/de/faq/#k%C3%B6nnen-benutzer-eigene-projekte-erstellen-sie-mit-github-verbinden-und-anwendungen-wie-html-seiten-hosten)

Ein Agent arbeitet in einer isolierten Sandbox, einer eigenen virtuellen Maschine pro Benutzer, mit Dateisystem und Terminal. Er kann Code schreiben und ausführen, Dateien erstellen und umwandeln, Daten analysieren und das Web nutzen. Dateien, die er erzeugt, kommen in den Chat zurück.

- Die Sandbox ist ein Arbeitsbereich für die Dauer einer Aufgabe, keine dauerhafte Entwicklungsumgebung.
- Smartchat ist keine Hosting-Plattform. Ergebnisse wie eine HTML-Seite können heruntergeladen und auf Ihren eigenen Servern bereitgestellt werden.
- Alternativ können Sie einen MCP-Server anbinden, über den der Agent Berichte oder andere Ergebnisse zur Veröffentlichung in Ihre eigenen Systeme hochlädt. GitHub wird auf dieselbe Weise angebunden, über einen MCP-Server.

### [Wie schneidet Smartchat im Vergleich zu Codex oder anderen Coding-Agenten ab?](https://docs.smartchat.ai.t-systems.net/de/faq/#wie-schneidet-smartchat-im-vergleich-zu-codex-oder-anderen-coding-agenten-ab)

Codex und ähnliche Coding-Agenten sind für die Softwareentwicklung gebaut: Sie arbeiten direkt in einem Repository und in den Tools der Entwickler. Der Agent von Smartchat ist universell. Seine Stärken sind die Arbeit mit Ihren Dokumenten und Kollektionen, Analysen und das Erstellen von Dateien, wobei die Daten in einer kontrollierten Umgebung bleiben.

Für die laufende Softwareentwicklung ist ein spezialisiertes Coding-Tool die bessere Wahl, und Smartchat ergänzt es. T-Systems bietet dafür [AI Engineer](https://docs.llmhub.t-systems.net/aie/overview/) an, eine Reihe von KI-Tools für Softwareentwickler, darunter IDE-Integrationen, Kommandozeilen-Tools und MCP-Integrationen.

## [Sicherheit und Datenschutz](https://docs.smartchat.ai.t-systems.net/de/faq/#sicherheit-und-datenschutz)

### [Wie werden Daten geschützt und verarbeitet?](https://docs.smartchat.ai.t-systems.net/de/faq/#wie-werden-daten-gesch%C3%BCtzt-und-verarbeitet)

- Smartchat wird von T-Systems auf der T-Cloud Public in Deutschland gehostet. Jeder Kunde hat seine eigene Umgebung.
- Daten, die an von T-Systems gehostete Modelle gesendet werden, und deren Ergebnisse werden nicht gespeichert, sind für T-Systems und Dritte nicht einsehbar und werden nicht zum Training verwendet.
- Anfragen an Modelle externer Anbieter gehen an diesen Anbieter und werden auf dessen Infrastruktur verarbeitet. Es gelten die Datenverarbeitungsbedingungen des Anbieters.
- Daten können als [vertraulich](https://docs.smartchat.ai.t-systems.net/de/user/concepts/confidentiality/) markiert werden, für eine einzelne Kollektion oder für den ganzen Space. Für vertrauliche Daten sind alle externen Modelle und die Websuche abgeschaltet, sodass nur von T-Systems gehostete Modelle genutzt werden können.
- [Spaces](https://docs.smartchat.ai.t-systems.net/de/user/concepts/spaces/) halten Daten getrennt, und der Zugriff wird über [Gruppen](https://docs.smartchat.ai.t-systems.net/de/user/concepts/groups/) gesteuert. Die Anmeldung erfolgt über lokale Konten oder das SSO Ihrer Organisation (OIDC). Alle Verbindungen nutzen HTTPS.

Das Hosting erfolgt in der EU und unterliegt damit der DSGVO und dem Privacy and Security Assessment (PSA) der Telekom. Das PSA regelt die Einhaltung von DSGVO, Datenschutz, Sicherheit und Barrierefreiheit. Sitzt Ihre Organisation außerhalb der EU, prüfen Sie dies anhand Ihrer eigenen Regeln für die grenzüberschreitende Verarbeitung.

### [Unterstützt Smartchat Zwei-Faktor-Authentifizierung?](https://docs.smartchat.ai.t-systems.net/de/faq/#unterst%C3%BCtzt-smartchat-zwei-faktor-authentifizierung)

Ja. Die Zwei-Faktor-Authentifizierung ist standardmäßig für jedes Konto aktiviert, das privilegierte Aktionen ausführen kann, etwa für Administratoren und Anwendungsinhaber. Auf Wunsch aktivieren wir sie für alle Benutzer.

- **Anmeldung über das SSO Ihrer Organisation (OIDC)**, die wir empfehlen: Es gelten die MFA und die Passwort-Richtlinie Ihres eigenen Identity Providers.
- **Anmeldung mit einem lokalen Konto** (E-Mail und Passwort): Der zweite Faktor ist eine Authenticator-App (TOTP).

Wie Einrichtung und Anmeldung funktionieren, beschreibt [Zwei-Faktor-Authentifizierung](https://docs.smartchat.ai.t-systems.net/de/user/concepts/two-factor-authentication/).

### [Welche Authenticator-Apps funktionieren für den zweiten Faktor?](https://docs.smartchat.ai.t-systems.net/de/faq/#welche-authenticator-apps-funktionieren-f%C3%BCr-den-zweiten-faktor)

Jede App, die TOTP implementiert, den offenen Standard [RFC 6238](https://datatracker.ietf.org/doc/html/rfc6238), zum Beispiel Google Authenticator, Microsoft Authenticator, FreeOTP oder Passwortmanager wie 1Password und Bitwarden. Die Anmeldung läuft über Keycloak, daher gilt dessen TOTP-Implementierung; Details stehen in der [Keycloak-Dokumentation](https://www.keycloak.org/docs/latest/server_admin/#one-time-password-otp-policies).

TOTP ist offen und herstellerunabhängig, braucht keinen Übertragungskanal und ist seit 2011 weit verbreitet, zum Beispiel bei Google, Microsoft, GitHub und AWS.

Wird ein Code abgelehnt, prüfen Sie, ob die Uhr des Geräts automatisch gestellt wird. App und Server berechnen den Code beide aus der aktuellen Uhrzeit, daher erzeugt eine Uhr, die mehr als ein paar Sekunden abweicht, falsche Codes.

### [Kann der Einmalcode per E-Mail oder SMS verschickt werden?](https://docs.smartchat.ai.t-systems.net/de/faq/#kann-der-einmalcode-per-e-mail-oder-sms-verschickt-werden)

Nein. Smartchat unterstützt E-Mail und SMS nicht als zweiten Faktor. Codes per E-Mail oder SMS sind deutlich schwächer als eine Authenticator-App: E-Mails können abgefangen werden und sind meist nicht verschlüsselt, ein Postfach kann übernommen werden, und SMS sind anfällig für SIM-Swapping.

Können Ihre Benutzer keine Authenticator-App verwenden, gibt es zwei Alternativen: die Anmeldung über das SSO Ihrer Organisation mit dessen eigener MFA oder ein eigenes Verfahren, das als separates Projekt für Sie umgesetzt wird.

## [Spaces und Gruppen](https://docs.smartchat.ai.t-systems.net/de/faq/#spaces-und-gruppen)

### [Sollten wir mehrere Spaces nutzen?](https://docs.smartchat.ai.t-systems.net/de/faq/#sollten-wir-mehrere-spaces-nutzen)

In der Regel nicht. Arbeiten Sie in einem Space und bilden Sie Abteilungen, Teams und Projekte mit Gruppen ab. Mehrere Spaces sind nur nötig, wenn Daten oder Administration strikt getrennt sein müssen.

[Spaces](https://docs.smartchat.ai.t-systems.net/de/user/concepts/spaces/) sind die Mandantentrennung von Smartchat: Daten und Berechtigungen sind zwischen ihnen vollständig isoliert. Sie sind für getrennte Organisationen gedacht, zum Beispiel verschiedene Gesellschaften eines Konzerns wie T-Systems Brasilien und T-Systems Deutschland. Die meisten Organisationen sind eine einzige Gesellschaft und brauchen einen Space.

Mehr dazu unter [Wann mehrere Spaces sinnvoll sind](https://docs.smartchat.ai.t-systems.net/de/user/concepts/spaces/#wann-mehrere-spaces-sinnvoll-sind).

### [Sollte jede Abteilung einen eigenen Space bekommen?](https://docs.smartchat.ai.t-systems.net/de/faq/#sollte-jede-abteilung-einen-eigenen-space-bekommen)

Nein. Dafür sind Gruppen da. Kollektionen, Assistenten und Prompt-Vorlagen können [mit bestimmten Gruppen geteilt werden](https://docs.smartchat.ai.t-systems.net/de/user/concepts/access-control/), sodass nur die Mitglieder einer Abteilung deren Daten sehen. Space Owner sehen jedes Element, sofern die Instanz nicht so eingerichtet ist, dass sie das einschränkt, siehe [Was Space Owner sehen](https://docs.smartchat.ai.t-systems.net/de/user/concepts/access-control/#was-space-owner-sehen).

Abteilungsübergreifende Arbeit, etwa ein Projekt, ist mit Gruppen einfach: Ein Benutzer kann mehreren Gruppen angehören, und das Projekt bekommt eine eigene Gruppe. Mit einem Space pro Abteilung ist das nicht möglich, weil Daten aus verschiedenen Spaces nicht zusammen genutzt werden können.

### [Wie entscheiden wir, ob mehrere Spaces sinnvoll sind?](https://docs.smartchat.ai.t-systems.net/de/faq/#wie-entscheiden-wir-ob-mehrere-spaces-sinnvoll-sind)

Zwei Fragen helfen:

1. **Soll ein Benutzer in mehreren Spaces arbeiten?** Dann sind Spaces nicht das Richtige. Ein Benutzer hat nur Zugriff auf die Ressourcen des aktiven Space und kann nicht gleichzeitig auf Ressourcen mehrerer Spaces zugreifen.
2. **Könnte ein Projekt oder eine Anfrage Daten aus mehreren Spaces brauchen?** Dann sind Spaces nicht das Richtige. Ein Chat oder Assistent erreicht nur Daten im aktiven Space.

Es hilft auch, die Frage umzudrehen: Ist es in Ordnung, wenn jede Abteilung eine Gruppe hat und nur deren Mitglieder die Daten der Abteilung sehen? Wenn ja, reicht ein Space.

### [Wann sind mehrere Spaces erforderlich?](https://docs.smartchat.ai.t-systems.net/de/faq/#wann-sind-mehrere-spaces-erforderlich)

Nur wenn mindestens einer dieser Punkte zutrifft:

- **Rechtliche oder Compliance-Anforderungen** verlangen eine strikte Datentrennung.
- **Administratoren müssen strikt getrennt sein**, zum Beispiel dürfen die Admins von Einheit A die Mitglieder von Einheit B nicht verwalten. Innerhalb eines Space verwalten Space Owner alle Mitglieder, Gruppen und Inhalte dieses Space.

Auch dann sind mehrere Spaces ein Kompromiss, den Benutzer in ihrer täglichen Arbeit spüren:

- Benutzer müssen wissen, in welchem Space sie sind und wo welche Daten liegen. Admins pflegen Mitglieder, Gruppen und Einstellungen in jedem Space einzeln.
- Dateien, Kollektionen und Assistenten eines Space sind in einem anderen nicht verfügbar.
- Daten zwischen Spaces zu verschieben ist kein Standardvorgang, sondern nur eine Ausnahme.

Wir unterstützen Sie dabei, ein Rollen- und Berechtigungskonzept zu erarbeiten, das Ihre Organisation auf Spaces und Gruppen abbildet, bevor Sie sich entscheiden.

## [Große Dokumentensammlungen](https://docs.smartchat.ai.t-systems.net/de/faq/#gro%C3%9Fe-dokumentensammlungen)

### [Kann Smartchat Informationen aus Millionen oder Milliarden von Dokumenten finden und zusammenfassen?](https://docs.smartchat.ai.t-systems.net/de/faq/#kann-smartchat-informationen-aus-millionen-oder-milliarden-von-dokumenten-finden-und-zusammenfassen)

Finden, ja. Sind die Dokumente in [Kollektionen](https://docs.smartchat.ai.t-systems.net/de/user/concepts/workspace/) indexiert, durchsucht Smartchat Millionen davon schnell und übergibt die relevantesten Passagen an das Modell. Schwierig ist, das Modell alle Dokumente durcharbeiten zu lassen:

- **Das Modell kann nicht alles lesen.** Es nimmt nur eine begrenzte Menge Text auf einmal auf, siehe [Wie viel Inhalt kann das Modell als Kontext nutzen](https://docs.smartchat.ai.t-systems.net/de/faq/#wie-viel-inhalt-kann-das-modell-als-kontext-nutzen-und-l%C3%A4sst-sich-das-begrenzen). Es fasst die Passagen zusammen, die die Suche liefert, nicht das ganze Archiv.
- **Die Nadel im Heuhaufen.** Steckt die Antwort in einem einzelnen Detail eines Dokuments unter Millionen, muss die Suche genau diese Passage finden. Das ist für jedes Suchsystem ein schwieriges Problem, und es wird umso schwieriger, je größer das Archiv ist und je ähnlicher sich die Dokumente sind.

Ein ganzes Archiv mit Millionen von Dokumenten zu indexieren ist außerdem ein eigenes Projekt mit eigener Dimensionierung und eigenen Kosten, weil jedes Dokument verarbeitet und indexiert werden muss. Zwei Wege vermeiden das, und sie lassen sich kombinieren:

- **An der Quelle suchen.** Ein Agent nutzt die Suche des Archivs selbst, über die Websuche oder einen MCP-Server, den Sie anbinden, und ruft nur die relevanten Dokumente ab.
- **Zwei Stufen.** Ein stärkeres Modell mit Internetzugang durchsucht das Archiv, wählt Dokumente aus und ordnet sie, zum Beispiel mit Zusammenfassungen, in eine Kollektion ein. Diese Kollektion wird dann in einem vertraulichen Setup mit einem von T-Systems gehosteten Modell ohne Internetzugang genutzt. [Deep Dive](https://docs.smartchat.ai.t-systems.net/de/user/guide/deep-dive/) passt zur zweiten Stufe: Es recherchiert in mehreren Schritten, nutzt nur die angehängten Kollektionen, nie das Internet, und schreibt einen Bericht mit Quellen.

## [Skills und Wissen](https://docs.smartchat.ai.t-systems.net/de/faq/#skills-und-wissen)

### [Können Benutzer aus ihrem eigenen Wissen und ihren Dateien wiederverwendbare Skills erstellen?](https://docs.smartchat.ai.t-systems.net/de/faq/#k%C3%B6nnen-benutzer-aus-ihrem-eigenen-wissen-und-ihren-dateien-wiederverwendbare-skills-erstellen)

- **Heute verfügbar:** Ein Assistent kombiniert ein Modell, feste Anweisungen und optional Kollektionen. Assistenten und Prompt-Vorlagen können gespeichert, geteilt und gemeinsam gepflegt werden.
- **Agenten:** Agenten lassen sich mit Skills spezialisieren, also mit Anweisungen, wie eine Aufgabe zu erledigen ist, zusammen mit den Tools, die sie dafür braucht. Skills können in einer gemeinsamen Bibliothek abgelegt und über Zugriffsrechte gesteuert werden.
- **Von Benutzern erstellte Skills** sind geplant.

### [Wo werden die Quelldateien gespeichert?](https://docs.smartchat.ai.t-systems.net/de/faq/#wo-werden-die-quelldateien-gespeichert)

Dokumente, die in Kollektionen hochgeladen oder aus S3 oder Confluence synchronisiert werden, werden in Ihrer Smartchat-Umgebung in Deutschland gespeichert. Dateien, die direkt in einen Chat hochgeladen werden, gehören nur zu diesem Chat.

### [Wie viel Inhalt kann das Modell als Kontext nutzen, und lässt sich das begrenzen?](https://docs.smartchat.ai.t-systems.net/de/faq/#wie-viel-inhalt-kann-das-modell-als-kontext-nutzen-und-l%C3%A4sst-sich-das-begrenzen)

Das Modell erhält keine ganzen Bibliotheken. Für jede Frage werden die relevantesten Passagen gesucht und an das Modell übergeben. Wie viel Text ein Modell auf einmal aufnehmen kann, hängt vom Modell ab, von etwa 100.000 Tokens bis zu rund 1 Million. Das Kontextfenster jedes Modells steht in der [Modelldokumentation von LLM Serving](https://docs.llmhub.t-systems.net/models/).

Der Kontext lässt sich auf drei Arten begrenzen:

- Benutzer wählen, welche Kollektionen oder Dateien an einen Chat oder Assistenten angehängt werden.
- Administratoren konfigurieren, wie Dokumente verarbeitet und durchsucht werden.
- Die [Zugriffskontrolle](https://docs.smartchat.ai.t-systems.net/de/user/concepts/access-control/) entscheidet, welche Kollektionen ein Benutzer überhaupt sehen kann.

## [Modelle und Funktionen](https://docs.smartchat.ai.t-systems.net/de/faq/#modelle-und-funktionen)

### [Welche Modelle sind verfügbar, und wie flexibel ist die Auswahl?](https://docs.smartchat.ai.t-systems.net/de/faq/#welche-modelle-sind-verf%C3%BCgbar-und-wie-flexibel-ist-die-auswahl)

Smartchat bietet Modelle aus T-Systems LLM Serving in zwei Gruppen:

- **Von T-Systems in Deutschland gehostete Modelle**, in allen Produktvarianten verfügbar.
- **Modelle externer Anbieter** (OpenAI, Anthropic, Google, Mistral AI), in den Varianten Pro und Agentic verfügbar und nach tatsächlicher Token-Nutzung abgerechnet.

Der Space Owner entscheidet, welche Modelle in seinem Space erscheinen. Modelle kommen monatlich hinzu und werden monatlich abgekündigt. Die aktuelle Liste steht in der [Modelldokumentation von LLM Serving](https://docs.llmhub.t-systems.net/models/).

### [Wie schneidet Smartchat im Vergleich zu Microsoft Copilot ab?](https://docs.smartchat.ai.t-systems.net/de/faq/#wie-schneidet-smartchat-im-vergleich-zu-microsoft-copilot-ab)

Microsoft 365 Copilot ist eng an das Microsoft-365-Ökosystem und dessen Daten (Mail, Teams, SharePoint) gebunden. Smartchat ist unabhängig von Microsoft 365. Es bietet eine Auswahl an Modellen, darunter in Deutschland gehostete, und bindet Ihre eigenen Datenquellen und Tools an.
