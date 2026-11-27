# Workspaces & Collaboration

Source: https://docs.smartchat.ai.t-systems.net/user/guide/workspaces/

> Understanding workspaces, setting permissions, creating knowledge collections and assistants.

> **See also**
>
> It is recommended to read the [Workspace](https://docs.smartchat.ai.t-systems.net/user/concepts/workspace/) concepts page first, to understand what a workspace is and how it relates to Spaces.

## [Navigating the workspace](https://docs.smartchat.ai.t-systems.net/user/guide/workspaces/#navigating-the-workspace)

Open the workspace by clicking **“Workspace”** in the left sidebar.

*\[Image: Workspace button in navigation menu]*

The workspace is divided into tabs along the top bar: **Assistants**, **Knowledge**, **Prompts**. Each tab lets you create, edit, and configure the respective elements. Application Owners and Space Owners also see a **Connectors** tab, where they decide who in the Space may use each [connector](https://docs.smartchat.ai.t-systems.net/user/agents/managing-connectors/#choosing-who-can-use-a-connector).

*\[Image: Workspace with Assistants, Knowledge, Prompts tabs]*

## [Sharing](https://docs.smartchat.ai.t-systems.net/user/guide/workspaces/#sharing)

Everything you create in the workspace starts as **Only you**. Click **Share** in the header of an item to share it with groups (**Can use** or **Can edit**) or with everyone in the Space. See [Access Control](https://docs.smartchat.ai.t-systems.net/user/concepts/access-control/).

## [Creating knowledge collections](https://docs.smartchat.ai.t-systems.net/user/guide/workspaces/#creating-knowledge-collections)

Local knowledge collections can be manually created, edited, and searched via the **“Knowledge”** tab. Existing knowledge collections can be referenced within a chat using the **hash key (#)**. Knowledge collections can also be attached as context to an assistant.

Switch on **Confidential** for a collection whose content must stay on Telekom-hosted models. Every chat that uses it becomes a confidential chat. See [Working with Confidential Data](https://docs.smartchat.ai.t-systems.net/user/guide/confidential-data/).

*\[Image: Knowledge collections in chat with # shortcut]*

## [Creating and using assistants](https://docs.smartchat.ai.t-systems.net/user/guide/workspaces/#creating-and-using-assistants)

Assistants are configurations tailored to specific use cases. An existing LLM is enhanced with knowledge and a system prompt and shared within the organization, so it can be used for recurring tasks (e.g. summarizing emails and writing responses that comply with corporate guidelines).

Created assistants can be selected and used in the chat via the dropdown list like any other model.

*\[Image: Assistants tab in the workspace]*

In the **“Assistants”** tab, you can create and edit assistants:

- **Plus icon** — add a new assistant
- **Pencil icon** — edit an existing assistant
- **Toggle** — activate/deactivate an assistant in the dropdown list

Who can use an assistant in the chat and who can also edit it is decided when you [share](https://docs.smartchat.ai.t-systems.net/user/concepts/access-control/) it.

When creating an assistant, assign a **name**, **description**, and **base model**. The **system prompt** is the most powerful tool alongside the stored knowledge and defines the assistant’s general behavior. Knowledge collections must be created beforehand via the “Knowledge” tab. **Prompt suggestions** enable quick and intuitive usage.

An assistant that uses a [confidential collection](https://docs.smartchat.ai.t-systems.net/user/concepts/confidentiality/) must run on a Telekom-hosted base model. Once a confidential collection is attached, the editor only offers those.

*\[Image: Assistant editing view]*

*\[Image: Additional assistant parameters: Tools, Filters, Actions, Capabilities]*

## [Creating and using prompt templates](https://docs.smartchat.ai.t-systems.net/user/guide/workspaces/#creating-and-using-prompt-templates)

Prompt templates are blueprints for prompts. They can be created and edited in the workspace under **“Prompts”**. Use the **plus icon** to add a new template. Like assistants and knowledge collections, you share them via **Share**.

Prompt templates have a **title** and the actual prompt content below. Variables for values to be filled in later are declared with curly braces, e.g. `Write an email to {{Name}}.` Built-in variables such as `{{CURRENT_DATE}}` fill themselves in, see [Prompt Variables](https://docs.smartchat.ai.t-systems.net/user/guide/prompt-variables/).

*\[Image: Plus button for new prompt template]*

*\[Image: Prompt template editing view]*

Existing templates can be invoked within a chat by typing the **forward slash (/)** and selecting the desired template from the dialog. Placeholders can then be filled with actual values.

> **Tip**
>
> Update multiple variable fields in sequence by pressing the Tab key in the input field after each entry.

*\[Image: Prompt template selection with / shortcut]*
