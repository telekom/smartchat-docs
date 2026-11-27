# Neuen Space einrichten

Source: https://docs.smartchat.ai.t-systems.net/de/user/admin/setting-up-a-new-space/

> Wie ein Anwendungsinhaber einen neuen Space in einem Schritt anlegt und konfiguriert.

Anwendungsinhaber legen Spaces in der [Administration](https://docs.smartchat.ai.t-systems.net/de/user/admin/) an. Der Space ist beim Anlegen vollständig konfiguriert: API-Schlüssel, Modelle, Vertraulichkeit und die ersten Space Owner werden im selben Dialog festgelegt.

> **Brauchen Sie wirklich einen neuen Space?**
>
> Legen Sie keinen Space pro Abteilung, Team oder Projekt an, sondern arbeiten Sie mit [Gruppen](https://docs.smartchat.ai.t-systems.net/de/user/concepts/groups/) und Kollektionen innerhalb des bestehenden Space. Eine Aufteilung auf mehrere Spaces lässt sich später nur mit Aufwand ändern, und Benutzer können nicht gleichzeitig mit Daten aus mehreren Spaces arbeiten. Legen Sie einen neuen Space nur an, wenn eine strikte Trennung zwingend ist, wie unter [Wann mehrere Spaces sinnvoll sind](https://docs.smartchat.ai.t-systems.net/de/user/concepts/spaces/#wann-mehrere-spaces-sinnvoll-sind) beschrieben.

## [Den Space anlegen](https://docs.smartchat.ai.t-systems.net/de/user/admin/setting-up-a-new-space/#den-space-anlegen)

Öffnen Sie **Administration → Anwendungsinhaber → Bereiche** und klicken Sie auf **Neuer Bereich**:

1. Geben Sie einen **Name** ein. Er muss in der Instanz eindeutig sein.
2. Fügen Sie den **Space-API-Schlüssel** aus dem [API Key Portal](https://apikey.llmhub.t-systems.net/) ein und drücken Sie **Enter**. Die Modelllisten laden, sobald ein Schlüssel eingegeben ist.
3. Wählen Sie das **Embedding-Modell** und das **Standardmodell**. Das Embedding-Modell lässt sich nach dem Anlegen des Spaces nicht mehr ändern.
4. Geben Sie optional ein **IdP-Attribut für automatische Zuordnung** ein und aktivieren Sie **Vertrauliche Daten**.
5. Tragen Sie unter **Bereichsinhaber** mindestens eine E-Mail-Adresse ein.
6. Klicken Sie auf **Erstellen**.

**Einstellungen übernehmen von** oben im Dialog übernimmt alles außer dem Namen und den Ownern aus einem bestehenden Space: API-Schlüssel, Embedding-Modell, Standardmodell, Vertraulichkeit und IdP-Attribut.

*\[Image: Dialog Neuer Bereich mit dem Menü Einstellungen übernehmen von]*

Die neuen Owner sehen den Space nach ihrer nächsten Anmeldung im Space-Selector. Ab dann [verwalten sie seine Mitglieder](https://docs.smartchat.ai.t-systems.net/de/user/admin/managing-space-members/) und können Inhaltsquellen wie [Confluence](https://docs.smartchat.ai.t-systems.net/de/user/admin/confluence-sync/) oder einen [S3-Bucket](https://docs.smartchat.ai.t-systems.net/de/user/admin/s3-autosync/) anbinden.

> **Achtung**
>
> Ohne einen gültigen Space-API-Schlüssel oder ohne Embedding-Modell und Standard-Sprachmodell kann niemand in dem Space arbeiten: Die Anmeldung oder der Wechsel in den Space schlägt mit einer Fehlermeldung fehl, die einen Space Owner um Prüfung der Konfiguration bittet.

> **Tipp**
>
> Das Standardmodell muss kein einfaches Sprachmodell sein. Sie können auch einen [Assistenten](https://docs.smartchat.ai.t-systems.net/de/user/guide/workspaces/#assistenten-erstellen-und-nutzen) auswählen, sodass jeder neue Chat im Space bereits mit dessen System-Prompt und Wissen startet.
