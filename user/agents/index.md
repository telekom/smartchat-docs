# Agent Mode

Source: https://docs.smartchat.ai.t-systems.net/user/agents/

> What Agent Mode is, how to turn it on, and how agents use connectors to work with your organisation's tools.

> **Preview**
>
> Agent Mode and MCP connectors are currently in preview only. If you would like to test these features, please contact your T-Systems representative.

In **Agent Mode**, Smartchat answers with an agent instead of a single model call. An agent plans its own steps: it can run code in a sandbox, call tools, and work with your organisation’s own systems through [connectors](https://docs.smartchat.ai.t-systems.net/user/agents/connectors/). It decides by itself when a tool or connector helps with your request.

## [Turning on Agent Mode](https://docs.smartchat.ai.t-systems.net/user/agents/#turning-on-agent-mode)

Switch on the **Agent Mode** toggle in the message box before you send the first message of a chat. Off means a regular chat. A new chat starts in the mode you last picked in that Space. If you have not picked one there, it follows the Space’s default, which Space Owners and Application Owners set in the [Agent Mode Settings](https://docs.smartchat.ai.t-systems.net/user/admin/agent-mode/).

The mode is fixed per chat:

- **It cannot be changed once the chat has started.** Start a new chat to switch between Agent Mode and a regular chat.
- **It cannot be changed while a file uploaded for the agent is attached.** Remove the file first.

## [Choosing an agent](https://docs.smartchat.ai.t-systems.net/user/agents/#choosing-an-agent)

Where several agents are available, pick one with **Switch agent**. Each agent can come with its own instructions, example prompts and connectors. To build your own agents, see [Custom Agents](https://docs.smartchat.ai.t-systems.net/user/agents/custom-agents/).

## [Attaching files](https://docs.smartchat.ai.t-systems.net/user/agents/#attaching-files)

When the selected agent has a sandbox, you can attach files of any type to the chat, up to 100 MB per file and 20 files per message. The files go to the agent directly and are not added to a collection. If the agent has no sandbox, it cannot read uploaded files, and Smartchat asks you to select an agent with a sandbox.

## [Web access](https://docs.smartchat.ai.t-systems.net/user/agents/#web-access)

> **Off by default since v3.15.1**
>
> Agents can use the web only when an Application Owner allows it for the instance in Administration and the Space Owner then allows it for their Space. Until both have, the agent editor shows the agent’s web capabilities as disabled. Confidential Spaces and chats never get web access.

Application Owners and Space Owners find these switches in the [Agent Mode Settings](https://docs.smartchat.ai.t-systems.net/user/admin/agent-mode/).

## [Working with an agent](https://docs.smartchat.ai.t-systems.net/user/agents/#working-with-an-agent)

- **Approvals**: before some actions, the agent asks for your approval. Approve or decline in the chat to let it continue.
- **Turn limit**: an agent stops after a fixed number of steps. Your request is still valid: ask the agent to continue from where it stopped.
- **Connectors**: if the agent needs a connector you have not connected yet, it asks you to connect it first. See [Using Connectors](https://docs.smartchat.ai.t-systems.net/user/agents/connectors/).
- **Stop Agent** ends a run at any time.

Agents always work with your own permissions. They can never show you anything your account could not already see.
