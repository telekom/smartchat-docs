# Space Settings

Source: https://docs.smartchat.ai.t-systems.net/user/admin/space-settings/

> Confidentiality, Space API key, upload limit and models: the settings a Space Owner controls in Administration.

The **Settings** pages of the **Space Owner** section in [Administration](https://docs.smartchat.ai.t-systems.net/user/admin/) hold the configuration of a Space. This page covers the **Space**, **Models** and **Web Search** pages; data sources have their own guides ([Confluence Sync](https://docs.smartchat.ai.t-systems.net/user/admin/confluence-sync/), [S3 AutoSync](https://docs.smartchat.ai.t-systems.net/user/admin/s3-autosync/)).

Open **Administration → Space Owner** and pick the Space you want to configure in **Selected Space**.

## [Space](https://docs.smartchat.ai.t-systems.net/user/admin/space-settings/#space)

*\[Image: Space page with the Confidential Data switch and the Space API Key field]*

### [Confidential Data](https://docs.smartchat.ai.t-systems.net/user/admin/space-settings/#confidential-data)

The **Confidential Data** switch marks every chat in this Space as confidential, restricting it to models that may process confidential data. Turning it on:

- locks all chats in the Space to Telekom-hosted models, externally hosted models are refused,
- disables web search and tools in those chats,
- applies to every collection of the Space, regardless of the collection’s own confidentiality flag.

If web search is configured for the Space, Smartchat first asks you to confirm (**Mark this space as confidential?**) and then switches web search off for the Space. Its settings are kept and apply again once the Space is no longer confidential.

The change is saved immediately (toast **Space configuration saved**) and members see the confidential badge in the chat composer without reloading. How confidentiality propagates to collections and chats is explained in [Confidentiality](https://docs.smartchat.ai.t-systems.net/user/concepts/confidentiality/).

### [Space API Key](https://docs.smartchat.ai.t-systems.net/user/admin/space-settings/#space-api-key)

Smartchat needs a key from the [API Key Portal](https://apikey.llmhub.t-systems.net/) to reach model serving on behalf of the Space.

1. Paste the key into **Space API Key** and press **Enter** (or click outside the field). The toast **Space API key saved** confirms the update.
2. The hint below the field tells you the state: **A key is configured. Enter a new one to replace it.** or **No key is configured. This space cannot reach model serving without one.**

> **The key is write-only**
>
> Since v3.15.1, nobody can read a saved key: Space Owners and Application Owners see only whether a key is configured, and `GET /space/api-key` no longer returns it either. Keep the key in your team’s secret store. To rotate it, paste the new key over the placeholder.

### [Max Upload Size](https://docs.smartchat.ai.t-systems.net/user/admin/space-settings/#max-upload-size)

Where upload control is enabled for your environment, **Max Upload Size** limits the size of a single file upload in MB. Leave it empty for no limit. The value is saved when you leave the field.

### [Feedback](https://docs.smartchat.ai.t-systems.net/user/admin/space-settings/#feedback)

Where feedback is available for your environment, the **Feedback** switch lets the members of this Space [rate responses](https://docs.smartchat.ai.t-systems.net/user/guide/feedback/) and share them with you. Turning it off hides the rating buttons; feedback given before is kept and stays on the [Feedback](https://docs.smartchat.ai.t-systems.net/user/admin/feedback/) page.

## [Models](https://docs.smartchat.ai.t-systems.net/user/admin/space-settings/#models)

Where Agent Mode is available, its settings for this Space (default mode for new chats, web access for agents) are described in [Agent Mode Settings](https://docs.smartchat.ai.t-systems.net/user/admin/agent-mode/#for-a-space).

*\[Image: Models page with the default model selector and the embedding model card]*

- **Enable and disable models**: the list shows all models available to the Space. Use the toggle in each row to control which ones your members can pick. **Search Models** filters the list.
- **Default model**: the model preselected for new chats in this Space. Pick a model or an [assistant](https://docs.smartchat.ai.t-systems.net/user/guide/workspaces/#creating-and-using-assistants). If the chosen model is later withdrawn, the selector shows **The selected default model is no longer available.** and the eRAG default is used until you pick a new one.
- **Embedding Model**: shown for information only. It was set when the Space was configured and cannot be changed afterwards, because all existing embeddings depend on it.
- **Import Presets / Export Presets**: exchange model presets between Spaces as JSON.

## [Web Search](https://docs.smartchat.ai.t-systems.net/user/admin/space-settings/#web-search)

The **Web Search** page has a switch for each type of web search:

- **Web Search**: searches through an external search provider. It has to be set up for your Smartchat environment first, with a search provider key that is licensed separately.
- **Enable Native Web Search**: lets Claude and Gemini models search through their own provider. It needs no setup.

A switch only appears once its type of web search is available in your environment, and it is then on in every Space. Switch it off and the Space’s users no longer get that type of web search; switch it back on to return it. In a Space marked **Confidential Data**, web search stays off whatever the switches say.

Where per-Space web search configuration is enabled, you also choose the search engine and enter its credentials for this Space only. A banner reminds you that the changes apply only to this Space.

In My Space, the page also has **Allow Web Search with Files/Collections in My Space**. While it is off, web search in My Space is not available as soon as files or collections are attached to a chat, or the selected assistant has a collection. Other Spaces don’t have this switch.
