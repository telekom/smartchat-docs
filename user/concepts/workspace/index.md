# Workspace

Source: https://docs.smartchat.ai.t-systems.net/user/concepts/workspace/

> The place in the UI where you access your collections, assistants, and prompt templates.

The **workspace** is the place in the UI where you access your data — documents, collections, assistants, and prompt templates.

Workspace contents depend on the [Space](https://docs.smartchat.ai.t-systems.net/user/concepts/spaces/) you are currently in. Switching to another Space replaces the entire workspace with the items of that Space.

Workspace items cannot cross Space boundaries: a collection created in one Space cannot be used in another, and an assistant in one Space cannot reference collections from another. Each Space has its own isolated set of workspace items.

Who can see and edit an item is described under [Access Control](https://docs.smartchat.ai.t-systems.net/user/concepts/access-control/).

## [Workspace items](https://docs.smartchat.ai.t-systems.net/user/concepts/workspace/#workspace-items)

### [Documents](https://docs.smartchat.ai.t-systems.net/user/concepts/workspace/#documents)

Files you upload (PDFs, spreadsheets, code, plain text, etc.) that the AI can search, read, and reason over. Documents are uploaded into a Space and bundled into collections.

### [Collections](https://docs.smartchat.ai.t-systems.net/user/concepts/workspace/#collections)

Named bundles of documents that the LLM can retrieve from when generating responses (RAG). Reference a collection in a chat with the **`#`** shortcut, or attach it to an assistant so it is always available.

### [Assistants](https://docs.smartchat.ai.t-systems.net/user/concepts/workspace/#assistants)

Configuration presets layered on top of a base model — pick an LLM, then bind a system prompt, knowledge collections, tools, and parameter overrides to it. Useful for repeatable tasks where the same prompt and context apply every time.

### [Prompt Templates](https://docs.smartchat.ai.t-systems.net/user/concepts/workspace/#prompt-templates)

Reusable prompts with placeholder variables (e.g. `Write an email to {{Name}}`). Invoke them in a chat with the **`/`** shortcut and fill in the variables before sending.
