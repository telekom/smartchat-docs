# Einführung

Source: https://docs.smartchat.ai.t-systems.net/de/user/

> Einführung in Smartchat für Endbenutzer — was es ist, wie es funktioniert und was es zu OpenWebUI hinzufügt.

T-Systems Smartchat ist eine KI-Chatbot-Anwendung. Smartchat ermöglicht die sichere Interaktion mit Ihren eigenen Datenquellen in natürlicher Sprache. Sie können Dokumente nach Informationen durchsuchen, deren Inhalte zusammenfassen und auf deren Basis neue Inhalte oder spezifische Ausgabeformate generieren.

Die technische Grundlage ist eine **Retrieval Augmented Generation (RAG)**-Architektur. RAG ruft Informationen aus Dateien oder Datenbanken ab und stellt sie dem Sprachmodell (Large Language Model, LLM) als Kontext bereit. Das bedeutet, dass Chat-Antworten auf den abgerufenen Inhalten basieren. Smartchat zeigt den Namen jeder verwendeten Quelle an.

> **Datenschutz**
>
> Die in Smartchat verwendeten Sprachmodelle werden **nicht** mit Benutzereingaben trainiert. Die Datenverarbeitung findet in einer sicheren Cloud-Umgebung innerhalb der EU statt, betrieben von der Telekom und gehostet auf der T-Cloud Public. Eine [Auswahl an LLMs](https://docs.llmhub.t-systems.net/plans/) steht zur Verfügung und wird kontinuierlich mit den neuesten Modellen aktualisiert.
>
> Daten, die Sie als [vertraulich](https://docs.smartchat.ai.t-systems.net/de/user/concepts/confidentiality/) markieren, werden ausschließlich von Telekom-gehosteten Modellen verarbeitet und nie an externe Anbieter gesendet.

Smartchat basiert auf einem Fork von [OpenWebUI](https://github.com/open-webui/open-webui) kombiniert mit einem maßgeschneiderten mandantenfähigen Enterprise-RAG-Framework, wobei Inhalte in isolierten Mandanten namens **Spaces** organisiert sind.

## [Was Smartchat zu OpenWebUI hinzufügt](https://docs.smartchat.ai.t-systems.net/de/user/#was-smartchat-zu-openwebui-hinzuf%C3%BCgt)

Mandantenfähigkeit

Vollständig isolierte Mandanten (Spaces) mit separaten Benutzern, Dokumenten und Konfigurationen — alles auf einer einzigen Installation.

Vertrauliche Daten

Markieren Sie eine Kollektion oder einen ganzen Space als vertraulich, und Smartchat hält die Daten auf Telekom-gehosteten Modellen: keine extern gehosteten Modelle, keine Websuche, kein Teilen.

Enterprise-RBAC

[Rollen, Berechtigungen und Zugriffskontrolle](https://docs.smartchat.ai.t-systems.net/de/user/concepts/roles-permissions-access-control/) pro Space, synchronisiert mit Ihrem SSO-Anbieter.

Asynchrone Ingestion-Pipeline

Skalierbare, vollständig asynchrone Dokumentenaufnahme — verarbeitet große Dokumentenmengen ohne Blockierung.

Security-Hardening

Sandboxed Code-Ausführung, Eingabevalidierung und Reduzierung der Angriffsfläche über die Upstream-Standards hinaus.

Compliance & Barrierefreiheit

Zertifiziert für Enterprise-Compliance-Standards und Barrierefreiheitsanforderungen.

Confluence-Integration

Verbinden Sie Confluence Data Center Spaces — Seiten werden automatisch synchronisiert und stehen als durchsuchbarer Kontext in Chats zur Verfügung.

> **Haftungsausschluss**
>
> Bitte beachten Sie, dass diese Dokumentation nur die allgemeinen Funktionen von Smartchat abdeckt. Da der bereitgestellte Funktionsumfang immer individuell in Ihrem Vertrag definiert wird, sind möglicherweise nicht alle hier beschriebenen Funktionen Teil Ihrer Installation.
>
> Darüber hinaus können individuelle Funktionen oder Rollenberechtigungen vereinbart worden sein, die über den Standardumfang dieser Dokumentation hinausgehen.
