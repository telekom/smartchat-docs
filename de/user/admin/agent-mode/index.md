# Einstellungen des Agenten-Modus

Source: https://docs.smartchat.ai.t-systems.net/de/user/admin/agent-mode/

> Legen Sie fest, in welchem Modus neue Chats starten und ob Agenten das Web nutzen dürfen, für die ganze Instanz und pro Space.

> **Preview**
>
> Der Agenten-Modus ist derzeit nur als Preview verfügbar. Diese Einstellungen erscheinen dort, wo er verfügbar ist. Wenn Sie ihn testen möchten, wenden Sie sich bitte an Ihre Ansprechperson bei T-Systems.

Zwei Einstellungen bestimmen, wie sich der [Agenten-Modus](https://docs.smartchat.ai.t-systems.net/de/user/agents/) verhält: der Modus, in dem neue Chats starten, und ob Agenten das Web nutzen dürfen. Anwendungsinhaber legen beides für die ganze Instanz fest; Space Owner können es anschließend für ihren Space anpassen.

## [Für die ganze Instanz](https://docs.smartchat.ai.t-systems.net/de/user/admin/agent-mode/#f%C3%BCr-die-ganze-instanz)

Anwendungsinhaber finden sie unter **Oberfläche → Agenten-Modus**:

- **Standardmodus für neue Chats**: ob ein neuer Chat als normaler Chat oder im **Agenten-Modus** startet. Er gilt für Benutzer, die selbst keinen Modus gewählt haben, in Spaces ohne eigenen Standard. Bestehende Chats behalten ihren Modus.
- **Internetzugriff für Agenten erlauben**: standardmäßig aus. Solange die Einstellung aus ist, kann kein Agent das Web nutzen, auch nicht Agenten, bei denen **Das Web nutzen** ausgewählt ist. Das Einschalten verlangt eine Bestätigung und lässt jeden Space Owner für seinen Space entscheiden. Für Mein Bereich entscheidet der Anwendungsinhaber.

Der Standardmodus gilt nur, wo weder Benutzer noch Space einen eigenen gewählt haben.

> **Mit Webzugriff können Daten SmartChat verlassen**
>
> Agenten mit Webzugriff können beliebige Webseiten öffnen: Daten aus Chats und Dateien können SmartChat dabei über die aufgerufenen Adressen verlassen, und eine Seite kann Anweisungen enthalten, die den Agenten steuern. Vertrauliche Spaces, Chats und Daten erhalten nie Webzugriff.

## [Für einen Space](https://docs.smartchat.ai.t-systems.net/de/user/admin/agent-mode/#f%C3%BCr-einen-space)

Space Owner finden sie in den [Space-Einstellungen](https://docs.smartchat.ai.t-systems.net/de/user/admin/space-settings/):

- **Standardmodus für neue Chats**, auf der Seite **Modelle**: der Modus, in dem ein neuer Chat in diesem Space startet, für Mitglieder, die in diesem Space selbst keinen gewählt haben. **Anwendungsstandard verwenden** folgt der Instanzeinstellung oben.
- **Internetzugriff für Agenten in diesem Space erlauben**, auf der Seite **Bereich**: erlaubt den Agenten dieses Space, **Das Web nutzen** zu verwenden, wenn es bei ihnen ausgewählt ist. Die Einstellung ist standardmäßig aus, verlangt eine Bestätigung und lässt sich erst einschalten, wenn ein Anwendungsinhaber den Webzugriff für die Instanz erlaubt.

Solange der Anwendungsinhaber den Internetzugriff sperrt, lässt sich der Schalter im Space nicht einschalten.
