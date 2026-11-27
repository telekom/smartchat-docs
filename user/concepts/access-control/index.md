# Access Control

Source: https://docs.smartchat.ai.t-systems.net/user/concepts/access-control/

> Who can use and edit the items in a Space, how to share them, and what Space Owners can see.

Access control decides who can use and edit a [workspace item](https://docs.smartchat.ai.t-systems.net/user/concepts/workspace/): a collection, assistant, prompt or agent. Items are shared with [groups](https://docs.smartchat.ai.t-systems.net/user/concepts/groups/), not with individual people. Like groups and permissions, access control always applies within one [Space](https://docs.smartchat.ai.t-systems.net/user/concepts/access-control/#scope) only.

How roles, permissions and access control differ is explained in [Roles, Permissions & Access Control](https://docs.smartchat.ai.t-systems.net/user/concepts/roles-permissions-access-control/).

## [Private by default](https://docs.smartchat.ai.t-systems.net/user/concepts/access-control/#private-by-default)

> **Note**
>
> Everything you create in the workspace starts as **Only you**: nobody else can see it until you share it with a group or with everyone in the Space. Depending on a setting, Space Owners are an exception, see [What Space Owners can see](https://docs.smartchat.ai.t-systems.net/user/concepts/access-control/#what-space-owners-can-see).
>
> **This does not apply to chats:** nobody but you sees your chats, not even a Space Owner.

The **{Space} - General** collection is the only item that every member can use from the start. Only Space Owners can edit it.

## [Who can access an item](https://docs.smartchat.ai.t-systems.net/user/concepts/access-control/#who-can-access-an-item)

Click **Share** in the header of an item to open its share dialog. Under **Who can access**, choose one of four options:

| Option | Who can use it | Who can edit it |
| - | - | - |
| **Only you** | You | You |
| **Specific groups** | You and the groups you add | You and the groups set to **Can edit** |
| **Everyone can use** | Every member of the Space | You and the groups under **Groups that can also edit** |
| **Everyone can use & edit** | Every member of the Space | Every member of the Space |

A prompt shared with two groups: Sales can use it, Project: Supplier portal can also edit it.

**Can use** means finding the item and using it in chats, for example the files of a collection or an assistant to chat with. **Can edit** also allows changing it, for example adding files to a collection or changing an agent’s instructions and tools.

“Everyone” means the members of the active Space. In the list of groups, they appear as **Everyone in this space**.

If you are in several groups, their access adds up: if one of your groups can use an item and another can edit it, you can edit it.

## [Who can share](https://docs.smartchat.ai.t-systems.net/user/concepts/access-control/#who-can-share)

- **With specific groups:** anyone who owns an item. Space Users can only add groups they belong to; Space Owners can add any group of the Space.
- **With everyone in the Space:** only members who have the matching **Public Sharing** permission, see [Permissions](https://docs.smartchat.ai.t-systems.net/user/concepts/permissions/).

## [Who can change sharing](https://docs.smartchat.ai.t-systems.net/user/concepts/access-control/#who-can-change-sharing)

> **Changed in v3.15.1**
>
> Only an item’s owner, Space Owners and Application Owners can change who has access to an item or delete it. A group that can edit the item can change its content, but sees its share dialog read-only.

## [What Space Owners can see](https://docs.smartchat.ai.t-systems.net/user/concepts/access-control/#what-space-owners-can-see)

What Space Owners see in the workspace of their Space depends on a setting. There are two options:

- **Space Owners see every item (default).** They see every collection, assistant, prompt and agent in the workspace of their Space, including items set to **Only you**, and can edit and share them.
- **Space Owners only see what is shared with them.** Like every other member, they see their own items and items shared with their groups or with everyone.

The setting applies to the whole Smartchat instance, not to a single Space, and to Application Owners just as to Space Owners. Ask your Smartchat contact to turn on the second option.

Space Owners never see other members’ chats.

Space Owners manage the Space either way: its members, groups and settings. They also have every permission of their Space, see [Permissions](https://docs.smartchat.ai.t-systems.net/user/concepts/permissions/#space-owners).

## [Scope](https://docs.smartchat.ai.t-systems.net/user/concepts/access-control/#scope)

Access is always limited to the active Space:

- You can only share with groups of the current Space.
- A shared item is only visible inside that Space. It cannot be used from another Space, even by someone who is a member of both.
- Groups belong to one Space, so a group named `engineering` in Space A is unrelated to a group of the same name in Space B.
