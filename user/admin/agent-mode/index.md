# Agent Mode Settings

Source: https://docs.smartchat.ai.t-systems.net/user/admin/agent-mode/

> Set the mode new chats start in and whether agents may use the web, for the whole instance and per Space.

> **Preview**
>
> Agent Mode is currently in preview only. These settings appear where it is available. If you would like to test it, please contact your T-Systems representative.

Two settings decide how [Agent Mode](https://docs.smartchat.ai.t-systems.net/user/agents/) behaves: the mode new chats start in, and whether agents may use the web. Application Owners set both for the whole instance; Space Owners can then adjust them for their Space.

## [For the whole instance](https://docs.smartchat.ai.t-systems.net/user/admin/agent-mode/#for-the-whole-instance)

Application Owners find them under **Interface → Agent Mode**:

- **Default mode for new chats**: whether a new chat starts as a regular chat or in **Agent Mode**. It applies to users who have not picked a mode themselves, in Spaces without a default of their own. Existing chats keep their mode.
- **Allow agents to use the web**: off by default. While it is off, no agent can use the web, including agents that have **Use the web** selected. Switching it on asks for confirmation and lets each Space Owner decide for their Space. For My Space, the Application Owner decides.

The default mode only applies where neither the user nor the Space has chosen one.

> **Web access lets data leave SmartChat**
>
> Agents with web access can open any web page: data from chats and files can leave SmartChat in the addresses an agent opens, and a page can contain instructions that steer the agent. Confidential Spaces, chats and data never get web access.

## [For a Space](https://docs.smartchat.ai.t-systems.net/user/admin/agent-mode/#for-a-space)

Space Owners find them in the [Space Settings](https://docs.smartchat.ai.t-systems.net/user/admin/space-settings/):

- **Default mode for new chats**, on the **Models** page: the mode a new chat in this Space starts in, for members who have not picked one in this Space themselves. **Use the application default** follows the instance setting above.
- **Allow agents in this space to use the web**, on the **Space** page: lets the agents of this Space use **Use the web** when they have it selected. It is off by default, asks for confirmation, and can only be switched on once an Application Owner allows web access for the instance.

While the Application Owner blocks web access, the Space's switch cannot be turned on.
