# Roles

Source: https://docs.smartchat.ai.t-systems.net/user/concepts/roles/

> The roles in Smartchat (Application Owner, Data Scientist, Space Owner, Space User) and what each of them can administer.

Every member of a Space starts there with the **Space User** role: they can use the Space’s chat, its features and the items shared with them. Further roles add administrative tasks, such as adding members, creating groups or changing a Space’s settings. Roles exist on two levels:

- **Global roles** apply to the whole Smartchat instance.
- **Space roles** apply to one Space. You hold a separate Space role in each Space you belong to, so you can be a Space Owner in one Space and a Space User in another.

How roles, permissions and access control differ is explained in [Roles, Permissions & Access Control](https://docs.smartchat.ai.t-systems.net/user/concepts/roles-permissions-access-control/).

## [Global roles](https://docs.smartchat.ai.t-systems.net/user/concepts/roles/#global-roles)

The global roles are independent of each other: a user may hold either, both or neither.

- **Application Owner:** the top-level administrator of the instance, working in [**Administration → Application Owner**](https://docs.smartchat.ai.t-systems.net/user/admin/application-owner/).
- **Data Scientist:** manages the ingest and retrieval configuration of the whole instance.

| Capability | Application Owner | Data Scientist |
| - | :-: | :-: |
| Assign the global Data Scientist role | ✅ | ❌ |
| View statistics across all Spaces | ✅ | ❌ |
| [Manage all Spaces and users](https://docs.smartchat.ai.t-systems.net/user/admin/application-owner/) of the instance | ✅ | ❌ |
| Manage settings that apply to the whole instance (**Interface**, **Code Execution**) | ✅ | ❌ |
| Manage global ingest & retrieval configuration (embedding models, pipelines) | ❌ | ✅ |

## [Space roles](https://docs.smartchat.ai.t-systems.net/user/concepts/roles/#space-roles)

- **Space User:** the role every member starts with. The Space appears in their Space selector.
- **Space Owner:** an administrator of the Space, working in [**Administration → Space Owner**](https://docs.smartchat.ai.t-systems.net/user/admin/). A Space can have several Space Owners. A Space Owner has everything a Space User has, plus the administrative tasks below.

| Capability | Space User | Space Owner | Application Owner |
| - | :-: | :-: | :-: |
| Create or delete the Space | ❌ | ❌ | ✅ |
| [Add or remove Space members](https://docs.smartchat.ai.t-systems.net/user/admin/managing-space-members/) | ❌ | ✅ | ✅ |
| [Promote or demote Space Owners](https://docs.smartchat.ai.t-systems.net/user/admin/managing-space-members/#changing-a-members-role) | ❌ | ✅ | ✅ |
| Set the Space’s confidentiality and API key | ❌ | ✅ | ✅ |
| [Manage the other Space settings](https://docs.smartchat.ai.t-systems.net/user/admin/space-settings/) (e.g. LLMs) | ❌ | ✅ | ✅\* |
| Set up [Confluence sync](https://docs.smartchat.ai.t-systems.net/user/admin/confluence-sync/) and [S3 AutoSync](https://docs.smartchat.ai.t-systems.net/user/admin/s3-autosync/) | ❌ | ✅ | ✅\* |
| Choose which [connectors](https://docs.smartchat.ai.t-systems.net/user/agents/managing-connectors/#choosing-who-can-use-a-connector) the members may use | ❌ | ✅ | ✅\* |
| Manage [groups](https://docs.smartchat.ai.t-systems.net/user/concepts/groups/) and their [permissions](https://docs.smartchat.ai.t-systems.net/user/concepts/permissions/) | ❌ | ✅ | ✅\* |

\* Only in Spaces where they also hold a Space role. The Space User role is enough.

> **Note**
>
> - A Space Owner’s tasks apply within their **own** Space. An Application Owner creates, deletes and staffs **any** Space.
> - A Space Owner cannot demote themselves; at least one Space Owner must remain per Space.
> - To work in a Space, an Application Owner gives themselves a Space role there like any other user.
> - Files and roles in a Space belong to the Space, not to the Space Owner who created them. They remain when that Space Owner’s account is deleted.
