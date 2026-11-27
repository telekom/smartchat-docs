# Custom Agents

Source: https://docs.smartchat.ai.t-systems.net/user/agents/custom-agents/

> Who can build and share custom agents in a Space, and how Space Owners grant the permission.

> **Preview**
>
> Agent Mode and MCP connectors are currently in preview only. If you would like to test these features, please contact your T-Systems representative.

Besides the agents that come with Smartchat, you can build your own agents in **Workspace → Agents → New agent**, with their own instructions, example prompts and connectors. Building custom agents is only available where the operators of Smartchat have enabled it for you.

*\[Image: Agents in Workspace]*

*\[Image: New agent access]*

## [Permissions](https://docs.smartchat.ai.t-systems.net/user/agents/custom-agents/#permissions)

Two permissions control custom agents:

| Permission | Where to find it | Allows |
| - | - | - |
| **Agent Management** | **Workspace Permissions** | Building, editing and deleting custom agents. Without it, the **Agents** tab does not appear in the Workspace. |
| **Agents Public Sharing** | **Sharing Permissions** | Making an agent available to everyone in the Space. Sharing an agent with specific groups does not need this permission. |

Both permissions are off in a new Space. Like every [permission](https://docs.smartchat.ai.t-systems.net/user/concepts/permissions/), they apply only in their Space, and a custom agent is only available in the Space it was built in.

Space Owners always have both permissions in their own Space, without belonging to a group. Application Owners have them in every Space where they also hold a Space role.

## [Granting the permission](https://docs.smartchat.ai.t-systems.net/user/agents/custom-agents/#granting-the-permission)

Space Owners grant the permissions through [groups](https://docs.smartchat.ai.t-systems.net/user/concepts/groups/) in their Space:

1. Click your profile image and choose **Administration**.
2. Go to **Space Owner → Groups** and check that the right Space is selected.
3. Click on a group, or click **Default permissions** to grant the permission to every member of the Space. Only Application Owners see **Default permissions**.
4. Open the **Permissions** tab.
5. Under **Workspace Permissions**, enable **Agent Management**. To allow sharing agents with the whole Space, also enable **Agents Public Sharing** under **Sharing Permissions**.
6. If you edited a group, add the users who should build agents to it on the **Users** tab.

*\[Image: Agent permissions]*

The two switches only appear when building custom agents is available to you. Who can use or edit an agent once it is built is decided when it is [shared](https://docs.smartchat.ai.t-systems.net/user/concepts/access-control/).
