# Groups

Source: https://docs.smartchat.ai.t-systems.net/user/concepts/groups/

> The groups every Space has, who manages them, and how to create one.

Groups are the central tool for access and permission control in a [Space](https://docs.smartchat.ai.t-systems.net/user/concepts/spaces/). They do two jobs:

- **Sharing:** collections, assistants, prompts and agents can be shared with a group, so that its members can use or edit them. See [Access Control](https://docs.smartchat.ai.t-systems.net/user/concepts/access-control/).
- **Permissions:** a group can allow its members to use features, for example building agents, web search, or sharing items with everyone in the Space. See [Permissions](https://docs.smartchat.ai.t-systems.net/user/concepts/permissions/).

Every group belongs to one Space and has no effect in any other Space. How roles, permissions and access control differ is explained in [Roles, Permissions & Access Control](https://docs.smartchat.ai.t-systems.net/user/concepts/roles-permissions-access-control/).

Ben is in Sales and in the project group, so he gets both: he can use Web Search and build agents, use the Sales playbook and edit the Supplier portal docs. Everyone in the Space can use Acme - General. Carla’s draft prompt is private: she has not shared it with any group.

## [Groups every Space has](https://docs.smartchat.ai.t-systems.net/user/concepts/groups/#groups-every-space-has)

Smartchat creates two groups in every Space and keeps their members up to date:

- **SpaceOwners {Space}** contains the Space Owners of the Space. Nothing about this group can be changed.
- **Users {Space}** contains every member of the Space. Only its permissions can be changed.

Sharing an item with **Everyone in this space** gives the **Users** group access. Permissions set on the **Users** group apply to every member of the Space.

## [Who manages groups](https://docs.smartchat.ai.t-systems.net/user/concepts/groups/#who-manages-groups)

Space Owners manage the groups of their Space under **Administration → Space Owner → Groups**. They create and delete groups, add and remove members, and set each group’s permissions.

Two permissions let other members manage groups as well:

- **Group Management**, under **Danger Zone**: manage every group in the Space, like a Space Owner. Anyone who has it can also grant it to others.
- **Own Group Management**, under **Workspace Permissions**: create groups and manage the members of the groups you created, without changing their permissions.

## [Creating a group](https://docs.smartchat.ai.t-systems.net/user/concepts/groups/#creating-a-group)

1. Click your profile image and choose **Administration**.
2. Go to **Space Owner → Groups**, check that the right Space is selected, and click **Add Group**.
3. Enter a name, optionally a description, and click **Create**.
4. Open the group. Add its members on the **Users** tab and set its [permissions](https://docs.smartchat.ai.t-systems.net/user/concepts/permissions/) on the **Permissions** tab.

A new group starts empty:

- It has no members, not even you.
- Nothing is shared with it.
- Its permissions are the Space’s [default permissions](https://docs.smartchat.ai.t-systems.net/user/concepts/permissions/#default-permissions) at the time it is created.

If your Smartchat signs in through your organization’s identity provider, a group can also list **Identity provider group attributes**. Users whose identity provider group matches are added to the group when they sign in.

When someone is removed from the Space, they are removed from all of its groups.
