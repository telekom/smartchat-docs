# Administration

Source: https://docs.smartchat.ai.t-systems.net/user/admin/

> How Application Owners and Space Owners manage Spaces, users, settings and data connections directly in Smartchat.

Smartchat is administered directly in the app. The **Administration** area covers everything Application Owners and Space Owners need: Spaces and their owners, users and their roles, the settings of each Space (confidentiality, API key, models), and the data connections that feed content into a Space. Regular users do not see it.

> **The legacy admin panel is being retired**
>
> Everything the separate admin panel at `admin-panel.smartchat.ai.t-systems.net` could do is now part of **Administration** in Smartchat. The legacy admin panel will be switched off at the end of October 2026.

## [Opening Administration](https://docs.smartchat.ai.t-systems.net/user/admin/#opening-administration)

Click your profile image at the bottom left and choose **Administration**. The entry is only shown to Application Owners and Space Owners.

*\[Image: User menu with the Administration entry]*

Administration opens with a navigation of its own on the left. It is divided into one section per role, and you only see the sections your role gives you:

| Section | For | What you do there |
| - | - | - |
| **Application Owner** | Application Owners | Manage all [Spaces and users](https://docs.smartchat.ai.t-systems.net/user/admin/application-owner/) of the instance, and settings that apply to the whole instance (**Interface**, **Code Execution**). |
| **Space Owner** | Space Owners | Manage the [members](https://docs.smartchat.ai.t-systems.net/user/admin/managing-space-members/) and groups of a Space, its [settings](https://docs.smartchat.ai.t-systems.net/user/admin/space-settings/), and its [Confluence](https://docs.smartchat.ai.t-systems.net/user/admin/confluence-sync/) and [S3](https://docs.smartchat.ai.t-systems.net/user/admin/s3-autosync/) sources. |

**Search settings** at the top finds any page of Administration by name. **Back to Chat** returns to your chats.

*\[Image: Administration with the Application Owner and Space Owner sections]*

## [Choosing the Space](https://docs.smartchat.ai.t-systems.net/user/admin/#choosing-the-space)

Everything under **Space Owner** acts on one Space at a time. Pick it in the **Selected Space** picker at the top of the section. To administer another Space you own, switch it there.

*\[Image: Selected Space picker in the Space Owner section]*

The **Space Owner** section shows these pages:

| Group | Pages |
| - | - |
| **Manage** | **Space Members**, **Feedback**, **Groups** |
| **Settings** | **Models**, **Space**, **Data Connections**, **S3 AutoSync**, **Web Search** |

> **Note**
>
> **Data Connections** and **S3 AutoSync** are only shown when the integration is enabled for your Smartchat environment. **Web Search** appears when per-Space web search configuration is enabled.

## [Who has access](https://docs.smartchat.ai.t-systems.net/user/admin/#who-has-access)

- **Application Owner**: sees the **Application Owner** section and can open the Space settings of the Spaces they belong to. **Space Members** is only shown for Spaces they also own: adding and removing members is reserved for Space Owners.
- **Space Owner**: sees the **Space Owner** section for every Space they own. Other Spaces cannot be administered.

For the full capability list see [Roles](https://docs.smartchat.ai.t-systems.net/user/concepts/roles/).
