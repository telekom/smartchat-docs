# Smartchat Docs

Source: https://docs.smartchat.ai.t-systems.net/de/

> Dokumentation für das Smartchat-Projekt — eine mandantenfähige Enterprise-Lösung für KI-gestützten Chat und Retrieval-Augmented Generation.

Smartchat ist ein verwaltetes, souveränes Angebot für KI-gestützte Wissensarbeit mit Funktionen wie Chat mit Ihren Dokumenten, Deep Research sowie Daten- und Tool-Integrationen. Aufgebaut auf den [AI Foundation Services](https://ai.t-systems.net/) von T-Systems und betrieben auf der [T-Cloud](https://www.t-systems.com/us/en/cloud-services/solutions/public-cloud/t-cloud-public), bietet Smartchat DSGVO-Konformität, Audit-Logging, rollenbasierte Zugriffskontrolle und vertraglich vereinbarte Service-Level als festen Bestandteil des Produkts — betrieben auf T-Cloud-Infrastruktur, die nach BSI-C5 und ISO 27017/27018 zertifiziert ist — anstatt diese Anforderungen Ihrem Team zu überlassen.

In der Praxis ist Smartchat die Lösung, wenn die Chat-Oberfläche der einfache Teil ist und die eigentliche Herausforderung darin besteht, sie sicher für regulierte Arbeitslasten zu betreiben: Gesundheitswesen, öffentlicher Sektor, Finanzwesen oder jeder Kontext, in dem Datenresidenz, Berufsgeheimnis und betriebliche Verantwortlichkeit an erster Stelle stehen.

Unsere Chat-Oberfläche basiert auf einem Fork von [OpenWebUI v0.6.5](https://github.com/open-webui/open-webui/tree/v0.6.5) (dem letzten Release unter der Open-Source-Lizenz BSD-3[1](https://docs.smartchat.ai.t-systems.net/de/#user-content-fn-1)). Die Open-Source-Version entsprach nicht den Enterprise-Anforderungen, daher haben wir sie mit Mandantenfähigkeit, Compliance und Security-Hardening als erstklassigen Funktionen erweitert.

Diese Dokumentation führt Sie durch die Architektur, die verfügbaren Modelle, die RAG-Konfiguration, die API und die Integration von Smartchat in Ihre bestehenden Systeme.

> **Teil der AI Foundation Services**
>
> Smartchat ist ein Produkt innerhalb von **AI Foundation Services**. Die Dokumentation zur übergeordneten Plattform, einschließlich LLM-API-Zugang, Modellkatalog, Abrechnung und Plattformadministration, finden Sie in der [AI Foundation Services Dokumentation](https://docs.llmhub.t-systems.net/).

## [Was Smartchat über OpenWebUI hinaus bietet](https://docs.smartchat.ai.t-systems.net/de/#was-smartchat-%C3%BCber-openwebui-hinaus-bietet)

Mandantenfähigkeit

Vollständig isolierte Mandanten (Spaces) gewährleisten strikte Datentrennung für unterschiedliche Vertraulichkeitsstufen und organisatorische Grenzen.

Vertrauliche Daten

Markieren Sie eine Kollektion oder einen ganzen Space als vertraulich, und Smartchat hält die Daten auf Telekom-gehosteten Modellen: keine extern gehosteten Modelle, keine Websuche, kein Teilen.

Enterprise-RBAC

Feingranulare rollenbasierte Zugriffskontrolle über Spaces, Admin-Panels und API-Endpunkte hinweg mit Enterprise-SSO-Integration.

Asynchrone Ingestion-Pipeline

Vollständig asynchrone, verteilte Dokumentenverarbeitung, die im Hintergrund läuft und die Benutzererfahrung nicht beeinträchtigt. Skaliert horizontal, um selbst die größten Dokumentenvolumen im Unternehmensumfeld zu bewältigen — sowohl hinsichtlich der Gesamtgröße als auch des parallelen Durchsatzes.

Security-Hardening

Gehärtet gegen die OWASP Top 10, zertifiziert und durch [Sicherheitsexperten](https://www.telekom.com/en/company/data-privacy-and-security/news/privacy-and-security-assessment-process-358312) der Deutschen Telekom penetrationsgetestet. Sandboxed Code-Ausführung, Eingabevalidierung und Reduktion der Angriffsfläche über das hinaus, was die Open-Source-Version bietet.

Compliance & Barrierefreiheit

DSGVO-konforme Anwendung, betrieben auf T-Cloud-Infrastruktur, die nach BSI-C5 und ISO 27017/27018 zertifiziert ist, und entwickelt zur Erfüllung von Enterprise-Anforderungen an die Barrierefreiheit.

Vollständig souverän & europäisch

Souverän über den gesamten Stack hinweg: die Anwendung, die Cloud, die LLMs und die Infrastruktur bis hin zu den GPUs sind vollständig europäisch und werden von T-Systems in Deutschland betrieben.

## [Schnelleinstieg](https://docs.smartchat.ai.t-systems.net/de/#schnelleinstieg)

[FAQ ](https://docs.smartchat.ai.t-systems.net/de/faq/)Antworten auf häufige Fragen zu Integrationen, Sicherheit, Spaces, großen Dokumentensammlungen und Modellen.

[Benutzerhandbuch ](https://docs.smartchat.ai.t-systems.net/de/user/)Schritt-für-Schritt-Anleitung zur Nutzung von Smartchat.

1. OpenWebUI hat ab Version v0.6.6 auf eine proprietäre Lizenz umgestellt. Weitere Informationen finden Sie unter [OpenWebUI License](https://docs.openwebui.com/license/). [↩](https://docs.smartchat.ai.t-systems.net/de/#user-content-fnref-1)
