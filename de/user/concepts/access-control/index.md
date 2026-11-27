# Zugriffskontrolle

Source: https://docs.smartchat.ai.t-systems.net/de/user/concepts/access-control/

> Wer die Elemente in einem Space verwenden und bearbeiten kann, wie man sie teilt und was Space Owner sehen.

Die Zugriffskontrolle bestimmt, wer ein [Arbeitsbereich-Element](https://docs.smartchat.ai.t-systems.net/de/user/concepts/workspace/) verwenden und bearbeiten kann: eine Kollektion, einen Assistenten, einen Prompt oder einen Agenten. Elemente werden mit [Gruppen](https://docs.smartchat.ai.t-systems.net/de/user/concepts/groups/) geteilt, nicht mit einzelnen Personen. Wie Gruppen und Berechtigungen gilt die Zugriffskontrolle immer nur innerhalb eines [Space](https://docs.smartchat.ai.t-systems.net/de/user/concepts/access-control/#geltungsbereich).

Wie sich Rollen, Berechtigungen und Zugriffskontrolle unterscheiden, steht unter [Rollen, Berechtigungen & Zugriffskontrolle](https://docs.smartchat.ai.t-systems.net/de/user/concepts/roles-permissions-access-control/).

## [Standardmäßig privat](https://docs.smartchat.ai.t-systems.net/de/user/concepts/access-control/#standardm%C3%A4%C3%9Fig-privat)

> **Hinweis**
>
> Alles, was Sie im Arbeitsbereich anlegen, startet als **Nur Sie**: Niemand sonst sieht es, bis Sie es mit einer Gruppe oder mit allen im Space teilen. Je nach Einstellung sind die Space Owner eine Ausnahme, siehe [Was Space Owner sehen](https://docs.smartchat.ai.t-systems.net/de/user/concepts/access-control/#was-space-owner-sehen).
>
> **Das gilt nicht für Chats:** Ihre Chats sieht niemand außer Ihnen, auch kein Space Owner.

Die Kollektion **{Space} - Allgemein** ist das einzige Element, das alle Mitglieder von Anfang an verwenden können. Bearbeiten können es nur Space Owner.

## [Wer auf ein Element zugreifen kann](https://docs.smartchat.ai.t-systems.net/de/user/concepts/access-control/#wer-auf-ein-element-zugreifen-kann)

Klicken Sie in der Kopfzeile eines Elements auf **Teilen**, um seinen Teilen-Dialog zu öffnen. Wählen Sie unter **Wer hat Zugriff** eine von vier Optionen:

| Option | Wer es verwenden kann | Wer es bearbeiten kann |
| - | - | - |
| **Nur Sie** | Sie | Sie |
| **Bestimmte Gruppen** | Sie und die Gruppen, die Sie hinzufügen | Sie und die Gruppen mit **Kann bearbeiten** |
| **Alle können verwenden** | Alle Mitglieder des Space | Sie und die Gruppen unter **Gruppen, die auch bearbeiten können** |
| **Alle können verwenden & bearbeiten** | Alle Mitglieder des Space | Alle Mitglieder des Space |

Ein Prompt, geteilt mit zwei Gruppen: Vertrieb kann ihn verwenden, Projekt: Lieferantenportal kann ihn auch bearbeiten.

**Kann verwenden** heißt, das Element zu finden und in Chats zu nutzen, zum Beispiel die Dateien einer Kollektion oder einen Assistenten zum Chatten. **Kann bearbeiten** erlaubt zusätzlich, es zu ändern, zum Beispiel einer Kollektion Dateien hinzuzufügen oder die Anweisungen und Werkzeuge eines Agenten zu ändern.

„Alle“ sind die Mitglieder des aktiven Space. In der Liste der Gruppen erscheinen sie als **Alle in diesem Bereich**.

Wenn Sie in mehreren Gruppen sind, addiert sich ihr Zugriff: Kann eine Ihrer Gruppen ein Element verwenden und eine andere es bearbeiten, können Sie es bearbeiten.

## [Wer teilen kann](https://docs.smartchat.ai.t-systems.net/de/user/concepts/access-control/#wer-teilen-kann)

- **Mit bestimmten Gruppen:** alle, denen ein Element gehört. Space User können nur Gruppen hinzufügen, denen sie selbst angehören; Space Owner können jede Gruppe des Space hinzufügen.
- **Mit allen im Space:** nur Mitglieder mit der passenden Berechtigung **… öffentlich teilen**, siehe [Berechtigungen](https://docs.smartchat.ai.t-systems.net/de/user/concepts/permissions/).

## [Wer die Freigabe ändern kann](https://docs.smartchat.ai.t-systems.net/de/user/concepts/access-control/#wer-die-freigabe-%C3%A4ndern-kann)

> **Geändert in v3.15.1**
>
> Nur der Eigentümer eines Elements, Space Owner und Anwendungsinhaber können ändern, wer Zugriff auf ein Element hat, oder es löschen. Eine Gruppe, die das Element bearbeiten darf, kann seinen Inhalt ändern, sieht seinen Teilen-Dialog aber schreibgeschützt.

## [Was Space Owner sehen](https://docs.smartchat.ai.t-systems.net/de/user/concepts/access-control/#was-space-owner-sehen)

Was Space Owner im Arbeitsbereich ihres Space sehen, hängt von einer Einstellung ab. Es gibt zwei Möglichkeiten:

- **Space Owner sehen alle Elemente (Standard).** Sie sehen jede Kollektion, jeden Assistenten, jeden Prompt und jeden Agenten im Arbeitsbereich ihres Space, auch Elemente mit **Nur Sie**, und können sie bearbeiten und teilen.
- **Space Owner sehen nur, was mit ihnen geteilt ist.** Wie alle anderen Mitglieder sehen sie ihre eigenen Elemente und Elemente, die mit ihren Gruppen oder mit allen geteilt sind.

Die Einstellung gilt für die ganze Smartchat-Instanz, nicht für einen einzelnen Space, und für Anwendungsinhaber genauso wie für Space Owner. Wenden Sie sich an Ihren Smartchat-Ansprechpartner, um die zweite Möglichkeit einzuschalten.

Die Chats anderer Mitglieder sehen Space Owner in keinem Fall.

Den Space verwalten Space Owner in beiden Fällen: seine Mitglieder, Gruppen und Einstellungen. Außerdem haben sie jede Berechtigung ihres Space, siehe [Berechtigungen](https://docs.smartchat.ai.t-systems.net/de/user/concepts/permissions/#space-owner).

## [Geltungsbereich](https://docs.smartchat.ai.t-systems.net/de/user/concepts/access-control/#geltungsbereich)

Zugriff ist immer auf den aktiven Space beschränkt:

- Sie können nur mit Gruppen des aktuellen Space teilen.
- Ein geteiltes Element ist nur innerhalb dieses Space sichtbar. Es kann nicht aus einem anderen Space heraus verwendet werden, auch nicht von jemandem, der Mitglied in beiden ist.
- Gruppen gehören zu einem Space, sodass eine Gruppe namens `engineering` in Space A nichts mit einer gleichnamigen Gruppe in Space B zu tun hat.
