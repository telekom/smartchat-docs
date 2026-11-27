# Confidentiality

Source: https://docs.smartchat.ai.t-systems.net/user/concepts/confidentiality/

> How Smartchat keeps confidential data inside Telekom-hosted infrastructure, and what changes when a collection, a Space or a chat is confidential.

**Confidentiality** is Smartchat’s built-in protection for data that must not leave the secure Smartchat environment. Once data is marked confidential, Smartchat enforces the rules for you: confidential data is only ever processed by models hosted by T-Systems, and every feature that would send it to an external system is switched off. You do not need to remember which model or feature is safe to use.

> **In short**
>
> - Mark a **collection** or a whole **Space** as confidential.
> - Every chat that uses that data becomes a **confidential chat**, and stays one.
> - A confidential chat only uses Telekom-hosted models (Telekom **T** logo), and web search, tools and sharing are unavailable in it.

For a step-by-step walkthrough with screenshots, see [Working with Confidential Data](https://docs.smartchat.ai.t-systems.net/user/guide/confidential-data/).

## [Where confidentiality is set](https://docs.smartchat.ai.t-systems.net/user/concepts/confidentiality/#where-confidentiality-is-set)

### [Confidential collections](https://docs.smartchat.ai.t-systems.net/user/concepts/confidentiality/#confidential-collections)

Every [collection](https://docs.smartchat.ai.t-systems.net/user/guide/workspaces/#creating-knowledge-collections) has a **Confidential** switch, off by default. Switch it on when you create the collection, or later in the collection’s header. Anyone who can edit the collection can change it.

*\[Image: Collection header with the Confidential switch turned on]*

Files have no confidentiality flag of their own: a file is confidential because it belongs to a confidential collection. A file you upload directly into a chat is not confidential by itself.

> **Keep confidential documents in a confidential collection**
>
> To protect a document, add it to a confidential collection and use the collection in your chats. A document uploaded straight into a chat is only protected if the chat is already confidential, for example because its Space is confidential.

### [Confidential Spaces](https://docs.smartchat.ai.t-systems.net/user/concepts/confidentiality/#confidential-spaces)

A Space Owner or an Application Owner can mark a whole [Space](https://docs.smartchat.ai.t-systems.net/user/concepts/spaces/) as confidential with the **Confidential Data** switch (see [Space Settings](https://docs.smartchat.ai.t-systems.net/user/admin/space-settings/#confidential-data)). All data in that Space is then treated as confidential, regardless of the setting of each collection. The Space setting can only add protection: it makes every collection in the Space confidential, but never makes a confidential collection non-confidential.

Your personal **My Space** cannot be marked confidential. There, confidentiality comes from the collections you use.

### [Confidential chats](https://docs.smartchat.ai.t-systems.net/user/concepts/confidentiality/#confidential-chats)

A chat becomes confidential as soon as:

- its Space is confidential,
- you attach a confidential collection, or a file from one, or
- you pick an [assistant](https://docs.smartchat.ai.t-systems.net/user/guide/workspaces/#creating-and-using-assistants) that uses a confidential collection.

Smartchat applies the restrictions the moment you attach the data, before you send your message. Once a chat is confidential it **stays confidential**, even if you remove the attachment again or the collection is no longer marked confidential later. To work without the restrictions, start a new chat without the confidential data.

*\[Image: Chat input with an attached confidential collection and the confidential chat icon]*

## [How to recognise confidential data](https://docs.smartchat.ai.t-systems.net/user/concepts/confidentiality/#how-to-recognise-confidential-data)

Confidential data is marked with a **shield** icon wherever it appears.

| Where | What you see |
| - | - |
| Workspace → **Collection** | A shield next to every confidential collection; a **Confidential** switch in the collection header. |
| **#** collection picker in the chat | A shield next to confidential collections. |
| Attachments in the chat input and in sent messages | A shield on every confidential collection or file. |
| Chat input | A shield icon next to the microphone. Hover over it for *“Confidential chat: only Telekom hosted models are available to prevent sending your data to external providers.”* |
| Model picker | Only the **Telekom hosted** models, with the note *“Confidential data: only Telekom-hosted models available.”* |
| Space selector | A confirmation dialog when you open a confidential Space from a chat. |

## [What changes in a confidential chat](https://docs.smartchat.ai.t-systems.net/user/concepts/confidentiality/#what-changes-in-a-confidential-chat)

| Feature | In a confidential chat |
| - | - |
| **Models** | Only models hosted by T-Systems are available. Externally hosted models are hidden from the model picker. If an externally hosted model was selected, Smartchat switches to a Telekom-hosted one and tells you: *“Switched to a Telekom-hosted model due to confidentiality restrictions.”* Adding a second model with **@** is not available. |
| **Assistants** | An assistant that uses a confidential collection must be built on a Telekom-hosted base model. Otherwise it is shown as unavailable and cannot be selected. |
| **[Web search](https://docs.smartchat.ai.t-systems.net/user/guide/web-search/)** | Unavailable: *“Web search is not available in confidential chats”*. Web search sends parts of the conversation to an external search provider. |
| **Tools** | Unavailable, because tools can pass data on to external systems. |
| **[Share, Clone, Copy](https://docs.smartchat.ai.t-systems.net/user/guide/managing-chats/#pinning-renaming-and-managing-chats)** | Not offered, so the content cannot be passed on outside Smartchat. |
| **Export** | Still available. An exported file is in your hands; handle it according to your organisation’s rules for confidential data. |

Smartchat enforces the model and web search restrictions on the server as well. A request that tries to use an externally hosted model in a confidential chat is rejected, the model is switched, and Smartchat asks you to send your message again.

Future features that transmit data to external systems will be guarded by the same mechanism.

## [Who can set it](https://docs.smartchat.ai.t-systems.net/user/concepts/confidentiality/#who-can-set-it)

| Level | Who | Where |
| - | - | - |
| Collection | Anyone who can [edit](https://docs.smartchat.ai.t-systems.net/user/concepts/access-control/) the collection | Workspace → **Collection** → the collection → **Confidential** |
| Space | Space Owner | **Administration → Space Owner → Space → Confidential Data** ([Space Settings](https://docs.smartchat.ai.t-systems.net/user/admin/space-settings/#confidential-data)) |
| Space | Application Owner | **Administration → Application Owner → Spaces** ([Application Owner](https://docs.smartchat.ai.t-systems.net/user/admin/application-owner/)) |

Both switches can be turned off again. Chats that are already confidential stay confidential.

## [Why this matters](https://docs.smartchat.ai.t-systems.net/user/concepts/confidentiality/#why-this-matters)

Models hosted by T-Systems in the T-Cloud (indicated by the Telekom **T** logo in the model picker) process data within the secure environment and are approved for confidential data ([PSA DSK3-compliant](https://docs.smartchat.ai.t-systems.net/user/glossary/)). Externally hosted models, web search and similar features route data through the infrastructure of external providers. Confidentiality ensures that data requiring the highest level of protection stays within the secure boundary, without relying on every user to make the right choice every time.
