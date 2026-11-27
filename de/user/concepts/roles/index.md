# Rollen

Source: https://docs.smartchat.ai.t-systems.net/de/user/concepts/roles/

> Die Rollen in Smartchat (Anwendungsinhaber, Data Scientist, Space Owner, Space User) und was jede von ihnen verwalten kann.

Jedes Mitglied eines Space startet dort mit der Rolle **Space User**: Es kann den Chat, die Funktionen und die mit ihm geteilten Elemente des Space nutzen. Weitere Rollen geben administrative Aufgaben dazu, etwa Mitglieder hinzufügen, Gruppen anlegen oder die Einstellungen eines Space ändern. Rollen gibt es auf zwei Ebenen:

- **Globale Rollen** gelten für die ganze Smartchat-Instanz.
- **Space-Rollen** gelten für einen Space. Sie haben in jedem Space, dem Sie angehören, eine eigene Space-Rolle und können so in einem Space Space Owner und in einem anderen Space User sein.

Wie sich Rollen, Berechtigungen und Zugriffskontrolle unterscheiden, steht unter [Rollen, Berechtigungen & Zugriffskontrolle](https://docs.smartchat.ai.t-systems.net/de/user/concepts/roles-permissions-access-control/).

## [Globale Rollen](https://docs.smartchat.ai.t-systems.net/de/user/concepts/roles/#globale-rollen)

Die globalen Rollen sind voneinander unabhängig: Ein Benutzer kann eine der Rollen, beide oder keine haben.

- **Anwendungsinhaber:** der oberste Administrator der Instanz, arbeitet in [**Administration → Anwendungsinhaber**](https://docs.smartchat.ai.t-systems.net/de/user/admin/application-owner/).
- **Data Scientist:** verwaltet die Ingest- und Retrieval-Konfiguration der ganzen Instanz.

| Fähigkeit | Anwendungsinhaber | Data Scientist |
| - | :-: | :-: |
| Die globale Rolle Data Scientist zuweisen | ✅ | ❌ |
| Statistiken über alle Spaces hinweg einsehen | ✅ | ❌ |
| [Alle Spaces und Benutzer](https://docs.smartchat.ai.t-systems.net/de/user/admin/application-owner/) der Instanz verwalten | ✅ | ❌ |
| Einstellungen für die gesamte Instanz verwalten (**Oberfläche**, **Codeausführung**) | ✅ | ❌ |
| Globale Ingest- & Retrieval-Konfiguration verwalten (Embedding-Modelle, Pipelines) | ❌ | ✅ |

## [Space-Rollen](https://docs.smartchat.ai.t-systems.net/de/user/concepts/roles/#space-rollen)

- **Space User:** die Rolle, mit der jedes Mitglied startet. Der Space erscheint in seiner Space-Auswahl.
- **Space Owner:** ein Administrator des Space, arbeitet in [**Administration → Bereichsinhaber**](https://docs.smartchat.ai.t-systems.net/de/user/admin/). Ein Space kann mehrere Space Owner haben. Ein Space Owner hat alles, was ein Space User hat, und zusätzlich die administrativen Aufgaben unten.

| Fähigkeit | Space User | Space Owner | Anwendungsinhaber |
| - | :-: | :-: | :-: |
| Space erstellen oder löschen | ❌ | ❌ | ✅ |
| [Space-Mitglieder hinzufügen oder entfernen](https://docs.smartchat.ai.t-systems.net/de/user/admin/managing-space-members/) | ❌ | ✅ | ✅ |
| [Space Owner befördern oder herabstufen](https://docs.smartchat.ai.t-systems.net/de/user/admin/managing-space-members/#rolle-eines-mitglieds-%C3%A4ndern) | ❌ | ✅ | ✅ |
| Vertraulichkeit und API-Schlüssel des Space festlegen | ❌ | ✅ | ✅ |
| [Die übrigen Space-Einstellungen verwalten](https://docs.smartchat.ai.t-systems.net/de/user/admin/space-settings/) (z. B. LLMs) | ❌ | ✅ | ✅\* |
| [Confluence-Synchronisation](https://docs.smartchat.ai.t-systems.net/de/user/admin/confluence-sync/) und [S3 AutoSync](https://docs.smartchat.ai.t-systems.net/de/user/admin/s3-autosync/) einrichten | ❌ | ✅ | ✅\* |
| Festlegen, welche [Connectors](https://docs.smartchat.ai.t-systems.net/de/user/agents/managing-connectors/#festlegen-wer-einen-connector-nutzen-darf) die Mitglieder nutzen dürfen | ❌ | ✅ | ✅\* |
| [Gruppen](https://docs.smartchat.ai.t-systems.net/de/user/concepts/groups/) und ihre [Berechtigungen](https://docs.smartchat.ai.t-systems.net/de/user/concepts/permissions/) verwalten | ❌ | ✅ | ✅\* |

\* Nur in Spaces, in denen er zusätzlich eine Space-Rolle hat. Die Rolle Space User genügt.

> **Hinweis**
>
> - Die Aufgaben eines Space Owner gelten in seinem **eigenen** Space. Ein Anwendungsinhaber legt **jeden** Space an, löscht ihn und besetzt ihn.
> - Ein Space Owner kann sich nicht selbst herabstufen; mindestens ein Space Owner muss pro Space bestehen bleiben.
> - Um in einem Space zu arbeiten, gibt sich ein Anwendungsinhaber dort wie jeder andere Benutzer eine Space-Rolle.
> - Dateien und Rollen in einem Space gehören dem Space, nicht dem Space Owner, der sie angelegt hat. Sie bleiben bestehen, wenn sein Konto gelöscht wird.
