# Permissions

Source: https://docs.smartchat.ai.t-systems.net/user/concepts/permissions/

> What permissions allow, where they are set, and how they combine.

Which items a member of a [Space](https://docs.smartchat.ai.t-systems.net/user/concepts/spaces/) can access is decided by [access control](https://docs.smartchat.ai.t-systems.net/user/concepts/access-control/). Permissions decide which features they can use and which actions they can take in the Space, such as using web search, building agents, uploading files to chats or sharing items with everyone in the Space.

How roles, permissions and access control differ is explained in [Roles, Permissions & Access Control](https://docs.smartchat.ai.t-systems.net/user/concepts/roles-permissions-access-control/).

The Space’s [default permissions](https://docs.smartchat.ai.t-systems.net/user/concepts/permissions/#default-permissions) decide which permissions a new [group](https://docs.smartchat.ai.t-systems.net/user/concepts/groups/) starts with. Permissions apply only in their Space.

## [All permissions](https://docs.smartchat.ai.t-systems.net/user/concepts/permissions/#all-permissions)

The **Permissions** tab of a group has these permissions. The **Default** column shows the value in a new Space.

| Permission | Allows | Default |
| - | - | - |
| **Workspace Permissions** | | |
| **Model Management** | Creating assistants | Off |
| **Collection Management** | Creating collections | Off |
| **Prompt Management** | Creating prompts | Off |
| **Agent Management**\* | Building agents | Off |
| **Own Group Management** | Creating groups and managing the members of groups you created | Off |
| **Sharing Permissions** | | |
| **Models Public Sharing** | Sharing assistants with everyone in the Space | Off |
| **Knowledge Public Sharing** | Sharing collections with everyone in the Space | Off |
| **Prompts Public Sharing** | Sharing prompts with everyone in the Space | Off |
| **Agents Public Sharing**\* | Sharing agents with everyone in the Space | Off |
| **Chat Permissions** | | |
| **Allow File Upload** | Attaching files to chat messages | On |
| **Allow Chat Controls**\* | Opening the chat controls, such as the system prompt and model parameters | Off |
| **Allow Speech to Text** | Dictating messages by voice | On |
| **Allow Text to Speech** | Having answers read aloud | On |
| **User Feedback**\* | Giving feedback on answers | Off |
| **Allow Multiple Models in Chat** | Using several models side by side in one chat | On |
| **Allow Temporary Chat** | Having chats that are not saved | On |
| **Features Permissions** | | |
| **Deep Dive**\* | Using Deep Dive | Off |
| **Web Search**\* | Using web search | Off |
| **Danger Zone** | | |
| **Group Management** | Managing every group in the Space, like a Space Owner | Off |

\* Only appears where the feature is available in your Smartchat.

Deleting and editing your own chats needs no permission: every member can always do both.

## [Rules](https://docs.smartchat.ai.t-systems.net/user/concepts/permissions/#rules)

Rules restrict what members can do, instead of allowing something.

- **Enforce Temporary Chat:** every chat of the group’s members is temporary and is not saved. Space Owners are exempt.

## [Default permissions](https://docs.smartchat.ai.t-systems.net/user/concepts/permissions/#default-permissions)

Besides its groups, every Space has **Default permissions** that apply to all of its members. They are under **Space Owner → Groups → Default permissions**.

> **Application Owners only**
>
> Only Application Owners can see and change the default permissions. Space Owners cannot, not even in their own Space.

In a new Space, the values from the **Default** column under [All permissions](https://docs.smartchat.ai.t-systems.net/user/concepts/permissions/#all-permissions) apply.

A new group starts with the default permissions that apply when it is created. Groups that already exist keep their own settings: if a permission is on in an existing group, its members keep it after the default is switched off.

## [How permissions combine](https://docs.smartchat.ai.t-systems.net/user/concepts/permissions/#how-permissions-combine)

A permission is on for you if it is on in the Space’s default permissions or in at least one of your groups. A group can only grant a permission, never take away one that another group grants.

Ben is in the groups Users, Sales and Project. A permission is on for him as soon as the defaults or one of his groups have it on: he gets Web Search through Sales. The Project group has file upload off, but that does not take it away, because it is on in the defaults. Deep Dive is on nowhere, so it is off for him too.

Only your groups in the active Space count.

## [Space Owners](https://docs.smartchat.ai.t-systems.net/user/concepts/permissions/#space-owners)

Space Owners have every permission of their Space, without being in a group.
