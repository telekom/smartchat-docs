# Setting Up a New Space

Source: https://docs.smartchat.ai.t-systems.net/user/admin/setting-up-a-new-space/

> How an Application Owner creates a new Space and configures it in one step.

Application Owners create Spaces in [Administration](https://docs.smartchat.ai.t-systems.net/user/admin/). The Space is fully configured when it is created: API key, models, confidentiality and its first Space Owners are all set in the same dialog.

> **Is a new Space really needed?**
>
> Do not create a Space per department, team or project: use [groups](https://docs.smartchat.ai.t-systems.net/user/concepts/groups/) and collections within the existing Space instead. Splitting into several Spaces is costly to change later, and users cannot work with data from several Spaces at once. Create a new Space only when strict separation is required, as described in [When to use several Spaces](https://docs.smartchat.ai.t-systems.net/user/concepts/spaces/#when-to-use-several-spaces).

## [Creating the Space](https://docs.smartchat.ai.t-systems.net/user/admin/setting-up-a-new-space/#creating-the-space)

Open **Administration → Application Owner → Spaces** and click **New space**:

1. Enter a **Name**. It must be unique on the instance.
2. Paste the **Space API Key** obtained from the [API Key Portal](https://apikey.llmhub.t-systems.net/) and press **Enter**. The model lists load once a key is entered.
3. Pick the **Embedding Model** and the **Default Model**. The embedding model cannot be changed after the Space is created.
4. Optionally enter an **IdP auto-assignment attribute** and switch on **Confidential Data**.
5. Add at least one email under **Space Owners**.
6. Click **Create**.

**Copy settings from** at the top of the dialog fills in everything except the name and the owners from an existing Space: API key, embedding model, default model, confidentiality and IdP attribute.

*\[Image: New space dialog with the Copy settings from menu]*

The new owners see the Space in their Space selector after their next login. From then on they [manage its members](https://docs.smartchat.ai.t-systems.net/user/admin/managing-space-members/) and can connect content sources such as [Confluence](https://docs.smartchat.ai.t-systems.net/user/admin/confluence-sync/) or an [S3 bucket](https://docs.smartchat.ai.t-systems.net/user/admin/s3-autosync/).

> **Caution**
>
> Without a usable Space API key, or without an embedding model and a default language model, nobody can work in the Space: signing in to it or switching to it fails with an error that asks a Space Owner to check the configuration.

> **Tip**
>
> The default model does not have to be a plain language model. You can also set it to an [assistant](https://docs.smartchat.ai.t-systems.net/user/guide/workspaces/#creating-and-using-assistants), so every new chat in the Space starts with its system prompt and knowledge already applied.
