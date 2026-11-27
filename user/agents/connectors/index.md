# Using Connectors

Source: https://docs.smartchat.ai.t-systems.net/user/agents/connectors/

> Connect an agent to tools like Telecontext with your own account, use them in a chat, and disconnect again.

> **Preview**
>
> Agent Mode and MCP connectors are currently in preview only. If you would like to test these features, please contact your T-Systems representative.

A **connector** links Smartchat to one of your organisation’s systems through the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/). Once you have connected it, an agent can read data from that system and use its functions during a chat.

Connectors are registered by the operators of Smartchat, and an Application Owner or Space Owner decides who in the Space may use them. You cannot add your own; you only decide which of the available ones to connect with your account.

## [Connecting a connector](https://docs.smartchat.ai.t-systems.net/user/agents/connectors/#connecting-a-connector)

1. Open a chat and switch on **Agent Mode**. Connectors are only available to agents.

2. Click **Connect a tool** below the message box. The **Connectors** dialog lists every connector made available in your Space.

   *\[Image: Connectors dialog with the available connectors]*

3. Click **Connect** on the connector you want. Smartchat shows what it will be able to do once you approve:

   - read the data you already have access to,
   - use the connector’s tools on your behalf during a chat,
   - act only while you are signed in. Access ends when you disconnect.

   *\[Image: Consent dialog before connecting]*

4. Click **Authorize with** followed by the connector’s name. A new window opens with the sign-in page of that system, for example your Microsoft login.

5. Sign in and approve the permissions the system asks for.

   *\[Image: Sign-in and approval page of the connected system]*

6. Back in Smartchat, the dialog confirms that the connector is ready to use, and the connector shows as **Connected**.

> **Tip**
>
> If your browser blocks the sign-in window, use the **Open the sign-in page** link in the dialog.

You sign in on the system’s own page. Smartchat never sees your password.

## [Using a connector in a chat](https://docs.smartchat.ai.t-systems.net/user/agents/connectors/#using-a-connector-in-a-chat)

A connected connector is not active in every chat automatically. In the **Connectors** dialog, switch on **Use in this chat** for each connector the agent should use. Active connectors are listed under **Active in this chat** below the message box.

*\[Image: Connected connector with the Use in this chat switch]*

Then ask your question as usual. The agent decides when to call the connector.

*\[Image: Agent answering with data from a connected system]*

Because you connected with your own account, the agent only sees what you can see in that system. Two colleagues using the same connector each work with their own data and permissions.

## [Disconnecting](https://docs.smartchat.ai.t-systems.net/user/agents/connectors/#disconnecting)

Open the **Connectors** dialog and click **Disconnect** on the connector. For a few seconds you can still **Undo**. After that, Smartchat’s access ends; to use the connector again, connect it again.

You may also be asked to connect again when a connector’s registration is renewed, your access is revoked and granted back, or your connector’s access token has expired or been revoked.
