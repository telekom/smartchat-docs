# Managing Connectors

Source: https://docs.smartchat.ai.t-systems.net/user/agents/managing-connectors/

> How MCP servers are registered as connectors, and how Application Owners and Space Owners decide who in a Space may use them.

> **Preview**
>
> Agent Mode and MCP connectors are currently in preview only. If you would like to test these features, please contact your T-Systems representative.

Connectors bring MCP servers into Smartchat. Making one available takes two steps:

1. The MCP server is **registered** for the whole instance. This is done by the operators of Smartchat. To add a server, contact your T-Systems representative with the server’s URL.
2. In each Space, an Application Owner or Space Owner decides **who may use** the connector.

Users can never add MCP servers themselves. Every connector is approved by an administrator, so your organisation decides which systems Smartchat talks to.

## [Registering an MCP server](https://docs.smartchat.ai.t-systems.net/user/agents/managing-connectors/#registering-an-mcp-server)

A connector needs a **Name** and the server’s **URL**, plus an optional **Description** that users see. No API key or password is entered.

*\[Image: Add connector dialog with name and URL]*

When you click **Provision connector**, Smartchat discovers the server’s sign-in endpoints and registers itself with the server as an OAuth client (dynamic client registration). The client secret is stored in Smartchat’s secret store. From then on, each user signs in to the server with their own account when they [connect](https://docs.smartchat.ai.t-systems.net/user/agents/connectors/).

The server therefore has to support OAuth 2.1 with the authorization code flow, PKCE and dynamic client registration.

*\[Image: Provisioned connector with its endpoints, client ID and scopes]*

A new connector is usable by everyone in every Space until access is restricted per Space.

### [Renewing the registration](https://docs.smartchat.ai.t-systems.net/user/agents/managing-connectors/#renewing-the-registration)

**Sync** registers Smartchat with the server again and creates a new client. All users who had connected are disconnected and have to connect again the next time they use the connector.

*\[Image: Sync connector dialog warning that everyone who had connected loses access]*

## [Choosing who can use a connector](https://docs.smartchat.ai.t-systems.net/user/agents/managing-connectors/#choosing-who-can-use-a-connector)

Application Owners and Space Owners control access per Space in **Workspace → Connectors**. The page lists every registered connector with three options:

| Option | Who can use the connector in this Space |
| - | - |
| **Public** | Every member of the Space. This is the default. |
| **Admin** | Application Owners only. |
| **Group** | Members of the [groups](https://docs.smartchat.ai.t-systems.net/user/concepts/groups/) you select. |

*\[Image: Workspace Connectors tab with Public, Admin and Group options]*

Space Owners can do this for the Spaces they own. Application Owners can do it for every Space they are a member of. The setting applies to the Space shown in the Space selector.
