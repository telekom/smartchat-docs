# FAQ

Source: https://docs.smartchat.ai.t-systems.net/faq/

> Answers to common questions about Smartchat — integrations, security, Spaces and groups, large document collections, skills and models.

Short answers to common questions about Smartchat.

## [Account and sign-in](https://docs.smartchat.ai.t-systems.net/faq/#account-and-sign-in)

### [My login link has expired. What should I do?](https://docs.smartchat.ai.t-systems.net/faq/#my-login-link-has-expired-what-should-i-do)

Use **Forgot Password** on the Smartchat login screen. Enter your e-mail address, and you receive an e-mail with a new link to set your password. See also [Registration](https://docs.smartchat.ai.t-systems.net/user/guide/getting-started/#registration).

## [Integrations and solution development](https://docs.smartchat.ai.t-systems.net/faq/#integrations-and-solution-development)

### [Can Smartchat connect to tools installed on a user’s computer?](https://docs.smartchat.ai.t-systems.net/faq/#can-smartchat-connect-to-tools-installed-on-a-users-computer)

Not directly. Smartchat runs in the cloud and cannot reach software installed on a single laptop.

Tools and data sources are connected through the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/), as [connectors](https://docs.smartchat.ai.t-systems.net/user/agents/connectors/) for agents:

- We do not run or provide MCP servers. Smartchat connects existing MCP servers that your organization manages and that are reachable over the internet.
- MCP servers must support Dynamic Client Registration.
- An administrator makes each connector available. Users then authorise their own access to it.

If your organization runs an MCP server for a tool and that server is reachable over the internet, an agent can work with the tool.

Agent Mode and connectors are currently in preview.

### [Can users build their own projects, connect them to GitHub and host applications such as HTML pages?](https://docs.smartchat.ai.t-systems.net/faq/#can-users-build-their-own-projects-connect-them-to-github-and-host-applications-such-as-html-pages)

An agent works in an isolated sandbox, a separate virtual machine per user, with a file system and a terminal. It can write and run code, create and convert files, run data analyses and use the web. Files it produces come back into the chat.

- The sandbox is a workspace for the length of a task, not a permanent development environment.
- Smartchat is not a hosting platform. Results such as an HTML page can be downloaded and deployed on your own servers.
- Alternatively, you can connect an MCP server that lets the agent upload reports or other results to your own systems for publishing. GitHub is connected the same way, through an MCP server.

### [How does Smartchat compare with Codex or other coding agents?](https://docs.smartchat.ai.t-systems.net/faq/#how-does-smartchat-compare-with-codex-or-other-coding-agents)

Codex and similar coding agents are built for software development: they work directly in a repository and in the developer’s tools. Smartchat’s agent is general-purpose. Its strengths are working with your documents and knowledge collections, analysis and producing files, with the data staying in a controlled environment.

For ongoing software development, a dedicated coding tool is the better choice, and Smartchat complements it. T-Systems offers [AI Engineer](https://docs.llmhub.t-systems.net/aie/overview/) for that, a set of AI tools for software developers, including IDE integrations, command-line tools and MCP integrations.

## [Security and data protection](https://docs.smartchat.ai.t-systems.net/faq/#security-and-data-protection)

### [How is data protected and processed?](https://docs.smartchat.ai.t-systems.net/faq/#how-is-data-protected-and-processed)

- Smartchat is hosted by T-Systems on T-Cloud Public in Germany. Each customer has its own environment.
- Data sent to models hosted by T-Systems, and the results they return, are not stored, are not visible to T-Systems or third parties, and are not used for training.
- Requests to models from external providers go to that provider and are processed on its infrastructure. The provider’s own data processing terms apply.
- Data can be marked [confidential](https://docs.smartchat.ai.t-systems.net/user/concepts/confidentiality/), for a single collection or for the whole Space. For confidential data, all external models and web search are switched off, so only models hosted by T-Systems can be used.
- [Spaces](https://docs.smartchat.ai.t-systems.net/user/concepts/spaces/) keep data separated, and access is controlled by [groups](https://docs.smartchat.ai.t-systems.net/user/concepts/groups/). Sign-in is through local accounts or your organization’s SSO (OIDC). All connections use HTTPS.

Hosting is in the EU, so it is covered by the GDPR and by Telekom’s Privacy and Security Assessment (PSA). The PSA governs GDPR, data privacy, security and accessibility compliance. If your organization is outside the EU, check this against your own rules for cross-border processing.

### [Does Smartchat support two-factor authentication?](https://docs.smartchat.ai.t-systems.net/faq/#does-smartchat-support-two-factor-authentication)

Yes. Two-factor authentication is enabled by default for every account that can perform privileged actions, such as administrators and Application Owners. On request, we enable it for all users.

- **Sign-in with your organization’s SSO (OIDC)**, which we recommend: the MFA and password policy of your own identity provider apply.
- **Sign-in with a local account** (e-mail and password): the second factor is an authenticator app (TOTP).

How setup and sign-in work is described in [Two-Factor Authentication](https://docs.smartchat.ai.t-systems.net/user/concepts/two-factor-authentication/).

### [Which authenticator apps work for the second factor?](https://docs.smartchat.ai.t-systems.net/faq/#which-authenticator-apps-work-for-the-second-factor)

Any app that implements TOTP, the open standard [RFC 6238](https://datatracker.ietf.org/doc/html/rfc6238), for example Google Authenticator, Microsoft Authenticator, FreeOTP, or password managers such as 1Password and Bitwarden. Sign-in runs on Keycloak, so its TOTP implementation applies; the [Keycloak documentation](https://www.keycloak.org/docs/latest/server_admin/#one-time-password-otp-policies) has the details.

TOTP is open and vendor-independent, needs no delivery channel, and has been in wide use since 2011, for example at Google, Microsoft, GitHub and AWS.

If a code is rejected, check that the device’s clock is set automatically. The app and the server both compute the code from the current time, so a clock that is off by more than a few seconds produces wrong codes.

### [Can the one-time code be sent by e-mail or SMS?](https://docs.smartchat.ai.t-systems.net/faq/#can-the-one-time-code-be-sent-by-e-mail-or-sms)

No. Smartchat does not support e-mail or SMS as a second factor. Codes sent by e-mail or SMS are much weaker than an authenticator app: e-mails can be intercepted and are usually not encrypted, a mailbox can be taken over, and SMS is open to SIM swapping.

If your users cannot use an authenticator app, the alternatives are signing in through your organization’s SSO with its own MFA, or a custom procedure built for you as a separate project.

## [Spaces and groups](https://docs.smartchat.ai.t-systems.net/faq/#spaces-and-groups)

### [Should we use several Spaces?](https://docs.smartchat.ai.t-systems.net/faq/#should-we-use-several-spaces)

Usually not. Work in one Space and model departments, teams and projects with groups. Several Spaces are only needed when data or administration must be strictly separated.

[Spaces](https://docs.smartchat.ai.t-systems.net/user/concepts/spaces/) are Smartchat’s tenant separation: data and permissions are completely isolated between them. They are meant for separate organizations, for example different legal entities of a group, such as T-Systems Brazil and T-Systems Germany. Most organizations are a single legal entity and need one Space.

More on this in [When to use several Spaces](https://docs.smartchat.ai.t-systems.net/user/concepts/spaces/#when-to-use-several-spaces).

### [Should every department get its own Space?](https://docs.smartchat.ai.t-systems.net/faq/#should-every-department-get-its-own-space)

No. Departments are what groups are for. Collections, assistants and prompt templates can be [shared with specific groups](https://docs.smartchat.ai.t-systems.net/user/concepts/access-control/), so only a department’s members see its data. Space Owners see every item unless the instance is set up to limit them, see [What Space Owners can see](https://docs.smartchat.ai.t-systems.net/user/concepts/access-control/#what-space-owners-can-see).

Cross-department work, such as a project, is easy with groups: a user can belong to several groups, and the project gets a group of its own. With one Space per department this is not possible, because data from different Spaces cannot be used together.

### [How do we decide whether several Spaces make sense?](https://docs.smartchat.ai.t-systems.net/faq/#how-do-we-decide-whether-several-spaces-make-sense)

Two questions help:

1. **Should a user work in several Spaces?** Then Spaces are not the right fit. A user only has access to the resources of the active Space and cannot access resources of several Spaces at the same time.
2. **Could a project or request need data from several Spaces?** Then Spaces are not the right fit. A chat or assistant only reaches data in the active Space.

It also helps to turn the question around: is it fine if every department has a group and only its members see the department’s data? If yes, one Space is enough.

### [When are several Spaces required?](https://docs.smartchat.ai.t-systems.net/faq/#when-are-several-spaces-required)

Only when at least one of these applies:

- **Legal or compliance requirements** demand strict data separation.
- **Administrators must be strictly separated**, for example the admins of unit A must not manage the members of unit B. Within one Space, Space Owners manage all members, groups and content of that Space.

Even then, several Spaces are a trade-off that users feel in their daily work:

- Users have to know which Space they are in and where which data lives. Admins maintain members, groups and settings once per Space.
- Files, collections and assistants of one Space are not available in another.
- Moving data between Spaces is not a standard operation, only an exception.

We help you work out a roles and permissions concept that maps your organization to Spaces and groups before you decide.

## [Large document collections](https://docs.smartchat.ai.t-systems.net/faq/#large-document-collections)

### [Can Smartchat find and summarize information across millions or billions of documents?](https://docs.smartchat.ai.t-systems.net/faq/#can-smartchat-find-and-summarize-information-across-millions-or-billions-of-documents)

Finding, yes. Once documents are indexed in [knowledge collections](https://docs.smartchat.ai.t-systems.net/user/concepts/workspace/), Smartchat searches millions of them quickly and passes the most relevant passages to the model. What is hard is having the model sift through all of them:

- **The model cannot read everything.** It takes in only a limited amount of text at once, see [How much content can the model use as context](https://docs.smartchat.ai.t-systems.net/faq/#how-much-content-can-the-model-use-as-context-and-can-it-be-limited). It summarizes the passages the search returns, not the whole archive.
- **The needle in the haystack.** If the answer is a single detail in one document among millions, the search has to find exactly that passage. That is a hard problem for any search system, and it gets harder the larger and more similar the documents are.

Indexing a whole archive of millions of documents is also a dedicated project with its own sizing and cost, because every document has to be processed and indexed. Two routes avoid that, and they can be combined:

- **Search at the source.** An agent uses the archive’s own search, through web search or an MCP server you connect, and retrieves only the relevant documents.
- **Two stages.** A stronger model with internet access searches the archive, selects documents and organises them, for example with summaries, into a knowledge collection. That collection is then used in a confidential setup with a model hosted by T-Systems and no internet access. [Deep Dive](https://docs.smartchat.ai.t-systems.net/user/guide/deep-dive/) fits the second stage: it researches in several steps, uses only the attached collections, never the internet, and writes a report with sources.

## [Skills and knowledge](https://docs.smartchat.ai.t-systems.net/faq/#skills-and-knowledge)

### [Can users create reusable skills from their own knowledge and files?](https://docs.smartchat.ai.t-systems.net/faq/#can-users-create-reusable-skills-from-their-own-knowledge-and-files)

- **Available today:** an assistant combines a model, fixed instructions and optionally knowledge collections. Assistants and prompt templates can be saved, shared and maintained together.
- **Agents:** agents can be specialised with skills, sets of instructions describing how to do a task, combined with the tools it needs. Skills can be stored in a shared library and controlled through access rights.
- **User-authored skills** are planned.

### [Where are the source files stored?](https://docs.smartchat.ai.t-systems.net/faq/#where-are-the-source-files-stored)

Documents uploaded to collections, or synced from S3 or Confluence, are stored in your Smartchat environment in Germany. Files uploaded directly into a chat belong only to that chat.

### [How much content can the model use as context, and can it be limited?](https://docs.smartchat.ai.t-systems.net/faq/#how-much-content-can-the-model-use-as-context-and-can-it-be-limited)

The model does not receive whole libraries. For each question, the most relevant passages are found and passed to the model. How much text a model can take in at once depends on the model, from about 100,000 tokens up to around 1 million. The context window of each model is listed in the [LLM Serving model documentation](https://docs.llmhub.t-systems.net/models/).

The context can be limited in three ways:

- Users choose which collections or files are attached to a chat or assistant.
- Administrators configure how documents are processed and searched.
- [Access control](https://docs.smartchat.ai.t-systems.net/user/concepts/access-control/) decides which collections a user can see at all.

## [Models and capabilities](https://docs.smartchat.ai.t-systems.net/faq/#models-and-capabilities)

### [Which models are available, and how flexible is the selection?](https://docs.smartchat.ai.t-systems.net/faq/#which-models-are-available-and-how-flexible-is-the-selection)

Smartchat offers models from T-Systems LLM Serving in two groups:

- **Models hosted by T-Systems in Germany**, available in all product variants.
- **Models from external providers** (OpenAI, Anthropic, Google, Mistral AI), available in the Pro and Agentic variants and billed by actual token usage.

The Space Owner decides which models appear in their Space. Models are added and retired monthly. For the current list, see the [LLM Serving model documentation](https://docs.llmhub.t-systems.net/models/).

### [How does Smartchat compare with Microsoft Copilot?](https://docs.smartchat.ai.t-systems.net/faq/#how-does-smartchat-compare-with-microsoft-copilot)

Microsoft 365 Copilot is closely tied to the Microsoft 365 ecosystem and its data (mail, Teams, SharePoint). Smartchat is independent of Microsoft 365. It offers a choice of models, including models hosted in Germany, and connects your own data sources and tools.
