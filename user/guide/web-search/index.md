# Web Search

Source: https://docs.smartchat.ai.t-systems.net/user/guide/web-search/

> Give Smartchat access to live web results via an external search provider or your model's built-in capability.

Smartchat supports two ways to bring live web results into a conversation:

- **Web Search**: Smartchat queries an external search provider (Bing, Brave, Google, etc.) and injects the results into context. Works with any model; requires prior setup by T-Systems.
- **Native Web Search**: The model provider performs the search as a built-in capability. Available for Google (Gemini) and Anthropic (Claude) models only.

Both types are gated behind the same **Web Search** feature permission. Once a type is available, it is on in every Space, and a Space Owner can switch it off for their Space.

## [Web Search](https://docs.smartchat.ai.t-systems.net/user/guide/web-search/#web-search)

Web Search works with every model, regardless of provider. Smartchat queries a configured external search provider and passes the results to the model as context. No LLM provider tool support is needed.

This is an opt-in feature: it is only available when a Space Owner has switched it on for the Space and a search provider API key is configured.

### [Supported Search Providers](https://docs.smartchat.ai.t-systems.net/user/guide/web-search/#supported-search-providers)

All [OpenWebUI-compatible search providers](https://docs.openwebui.com/category/web-search) are supported, including Bing, Brave, Google, Jina, Kagi, Mojeek, Perplexity, and others.

### [Setup by the Space Owner](https://docs.smartchat.ai.t-systems.net/user/guide/web-search/#setup-by-the-space-owner)

1. Click your profile image and choose **Administration**.
2. Go to **Space Owner → Web Search** and check that the right Space is shown in **Selected Space**.
3. Once web search is set up for your environment, **Web Search** is on in every Space. Switch it off to take web search away from the Space’s users, and back on to return it.
4. Select a **Web Search Engine** from the dropdown.

## [Native Web Search](https://docs.smartchat.ai.t-systems.net/user/guide/web-search/#native-web-search)

Native web search uses the model provider’s built-in search capability. No separate search provider account or API key is needed. It works out of the box in Smartchat for anyone who has access to a supported model.

### [Supported Providers](https://docs.smartchat.ai.t-systems.net/user/guide/web-search/#supported-providers)

- **Google** (Gemini)
- **Anthropic** (Claude)

In the model picker, models that support native web search are indicated with a **Globe icon** (🌐).

> **Not available for T-Cloud models**
>
> Native web search is a capability of the model provider, so it does **not** work with the open source models hosted by T-Systems in the T-Cloud. To use web search with those models, use the regular [Web Search](https://docs.smartchat.ai.t-systems.net/user/guide/web-search/#web-search) above, which requires a separate search provider license.

### [Setup by the Space Owner](https://docs.smartchat.ai.t-systems.net/user/guide/web-search/#setup-by-the-space-owner-1)

1. Click your profile image and choose **Administration**.
2. Go to **Space Owner → Web Search** and check that the right Space is shown in **Selected Space**.
3. **Enable Native Web Search** is on in every Space. Switch it off to take native web search away from the Space’s users, and back on to return it.

## [Permissions](https://docs.smartchat.ai.t-systems.net/user/guide/web-search/#permissions)

Space Owners have every [permission](https://docs.smartchat.ai.t-systems.net/user/concepts/permissions/) of their Space, so they need no group. Other members need the **Web Search** permission, through one of their [groups](https://docs.smartchat.ai.t-systems.net/user/concepts/groups/) or the Space’s default permissions. It is off by default.

To grant the permission:

1. In Administration, go to **Space Owner → Groups**.
2. Click on a group, or click **Default permissions** to grant the permission to every member of the Space. Only Application Owners see **Default permissions**.
3. Open the **Permissions** tab.
4. Under **Features Permissions**, enable **Web Search**.

Web search must also be switched on for your Smartchat instance. If it is off there, nobody can use it, Space Owners included. See [Permissions](https://docs.smartchat.ai.t-systems.net/user/concepts/permissions/).

## [Using Web Search](https://docs.smartchat.ai.t-systems.net/user/guide/web-search/#using-web-search)

**Web Search (external provider):** Available for any model once a Space Owner has switched it on. To use it, enable the **Web Search** toggle in the prompt window, then send your prompt. Smartchat fetches relevant results and provides them to the model.

**Native Web Search:** Open a chat and, from the model picker, select a model marked with the Globe icon (🌐). Enable the **Web Search** toggle in the prompt window, then send your prompt. The model fetches live web results and incorporates them into its response.

**When both are available:** If Web Search (external provider) is configured for your environment and you select a model that also supports native web search, you can choose which type to use on a per-message basis in the chat interface. Results may differ between the two types depending on the search provider and the model’s built-in search capability.

## [Combining Web Search with Your Data](https://docs.smartchat.ai.t-systems.net/user/guide/web-search/#combining-web-search-with-your-data)

Web search can be used together with your own data in the same chat — collections as well as files you upload — as long as that data is **not confidential**. Confidentiality is what governs the combination, not the kind of data:

- **Non-confidential collections, Spaces, and uploaded files** can be combined with web search.
- **Confidential collections or Spaces** cannot be combined with web search. If a collection or its Space is marked as confidential, web search is unavailable in that chat.
- **Files from a confidential collection** behave the same way: attaching one makes the chat confidential, so web search is unavailable in it.

Web search sends parts of the conversation to an external provider, so it must never be used with confidential data. Users must be aware that enabling web search in a chat involving confidential information poses a data security risk and must be avoided. This can be enforced at two levels: any user can mark a collection as confidential, and admins can mark Spaces as confidential. See [Confidentiality](https://docs.smartchat.ai.t-systems.net/user/concepts/confidentiality/) for details on how the confidentiality flag works.

## [See also](https://docs.smartchat.ai.t-systems.net/user/guide/web-search/#see-also)

- [Tiers & Features](https://docs.smartchat.ai.t-systems.net/features/v2-feature-overview)
- [Release Notes](https://docs.smartchat.ai.t-systems.net/release-notes/)
