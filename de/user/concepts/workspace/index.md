# Arbeitsbereich

Source: https://docs.smartchat.ai.t-systems.net/de/user/concepts/workspace/

> Der Bereich in der Benutzeroberfläche, in dem Sie auf Ihre Kollektionen, Assistenten und Prompt-Vorlagen zugreifen.

Der **Arbeitsbereich** ist der Bereich in der Benutzeroberfläche, in dem Sie auf Ihre Daten zugreifen: Dokumente, Kollektionen, Assistenten und Prompt-Vorlagen.

Die Inhalte des Arbeitsbereichs hängen vom [Space](https://docs.smartchat.ai.t-systems.net/de/user/concepts/spaces/) ab, in dem Sie sich gerade befinden. Beim Wechsel zu einem anderen Space wird der gesamte Arbeitsbereich durch die Elemente dieses Space ersetzt.

Arbeitsbereich-Elemente können keine Space-Grenzen überschreiten: Eine Kollektion, die in einem Space erstellt wurde, kann nicht in einem anderen verwendet werden, und ein Assistent in einem Space kann keine Kollektionen aus einem anderen Space referenzieren. Jeder Space hat seinen eigenen isolierten Satz an Arbeitsbereich-Elementen.

Wer ein Element sehen und bearbeiten kann, steht unter [Zugriffskontrolle](https://docs.smartchat.ai.t-systems.net/de/user/concepts/access-control/).

## [Arbeitsbereich-Elemente](https://docs.smartchat.ai.t-systems.net/de/user/concepts/workspace/#arbeitsbereich-elemente)

### [Dokumente](https://docs.smartchat.ai.t-systems.net/de/user/concepts/workspace/#dokumente)

Dateien, die Sie hochladen (PDFs, Tabellen, Code, Klartext usw.), die die KI durchsuchen, lesen und darüber schlussfolgen kann. Dokumente werden in einen Space hochgeladen und in Kollektionen gebündelt.

### [Kollektionen](https://docs.smartchat.ai.t-systems.net/de/user/concepts/workspace/#kollektionen)

Benannte Bündel von Dokumenten, aus denen das LLM bei der Antwortgenerierung abrufen kann (RAG). Referenzieren Sie eine Kollektion in einem Chat mit der **`#`**-Verknüpfung oder hängen Sie sie an einen Assistenten an, damit sie immer verfügbar ist.

### [Assistenten](https://docs.smartchat.ai.t-systems.net/de/user/concepts/workspace/#assistenten)

Konfigurationsvoreinstellungen, die auf ein Basismodell aufgesetzt werden: Wählen Sie ein LLM und binden Sie einen System-Prompt, Kollektionen, Tools und Parameterüberschreibungen daran. Nützlich für wiederkehrende Aufgaben, bei denen jedes Mal derselbe Prompt und Kontext gelten.

### [Prompt-Vorlagen](https://docs.smartchat.ai.t-systems.net/de/user/concepts/workspace/#prompt-vorlagen)

Wiederverwendbare Prompts mit Platzhaltervariablen (z. B. `Schreibe eine E-Mail an {{Name}}`). Rufen Sie sie in einem Chat mit der **`/`**-Verknüpfung auf und füllen Sie die Variablen vor dem Senden aus.
