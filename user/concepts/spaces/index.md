# Spaces

Source: https://docs.smartchat.ai.t-systems.net/user/concepts/spaces/

> How Spaces work — Smartchat's multi-tenancy boundary.

A **Space** is Smartchat’s multi-tenancy boundary. Every resource lives inside exactly one Space, and resources are completely isolated between Spaces — an entity in one Space cannot be accessed from another, not even by the same user who owns it.

> **Several Spaces are a deliberate decision**
>
> Do not create one Space per department. A common pattern is to start with a Space per department, then find that teams work across departments, in projects or shared requests. Spaces cannot support that, and by then changing it takes effort.
>
> Always try working with [groups](https://docs.smartchat.ai.t-systems.net/user/concepts/groups/) *within* one Space first. For day-to-day work with departments, teams and projects, that is usually the better way. Working with several Spaces has trade-offs that the Application Owners and Space Owners who set it up must accept:
>
> - **No work across Spaces.** A chat, assistant or agent only reaches the data of the active Space. A project that needs documents from two Spaces cannot use both.
> - **One Space at a time.** Users in several Spaces only reach the resources of the active Space and have to know where which data lives.
> - **Everything maintained per Space.** Members, groups, settings and data connections are set up and kept up to date in every Space separately.
> - **Costly to change later.** Merging Spaces later is not a standard operation, and data can be moved between Spaces only as an exception.
>
> Choose several Spaces only when strict separation is required, as described in [When to use several Spaces](https://docs.smartchat.ai.t-systems.net/user/concepts/spaces/#when-to-use-several-spaces).

## [What’s scoped to a Space](https://docs.smartchat.ai.t-systems.net/user/concepts/spaces/#whats-scoped-to-a-space)

The following are isolated per Space:

- **File uploads**. Files are isolated per space — the same physical file has separate identities in different spaces.
- **Collections** (built from uploaded files)
- **Assistants**
- **Prompt templates**
- **Groups**
- **Configuration**
- **Available models** (which LLMs appear in the model picker)
- **Chats**

If you upload a file in Space A, it does not exist in Space B. The same applies to every other resource above.

A user only has access to the resources of the active Space. They cannot access resources of several Spaces at the same time.

## [Confidential Spaces](https://docs.smartchat.ai.t-systems.net/user/concepts/spaces/#confidential-spaces)

A Space can be marked as confidential by its Space Owner. Every chat in a confidential Space is restricted to Telekom-hosted models, and features that send data to external providers are switched off. See [Confidentiality](https://docs.smartchat.ai.t-systems.net/user/concepts/confidentiality/#confidential-spaces).

## [Membership](https://docs.smartchat.ai.t-systems.net/user/concepts/spaces/#membership)

- A user can be a member of one or multiple Spaces.
- A user is **active in only one Space at a time**.

## [When to use several Spaces](https://docs.smartchat.ai.t-systems.net/user/concepts/spaces/#when-to-use-several-spaces)

One Space per organization is the default. Departments, teams and projects are modelled with [groups](https://docs.smartchat.ai.t-systems.net/user/concepts/groups/) inside that Space. Several Spaces are only needed when data or administration must be strictly separated:

- Legal or compliance requirements demand strict data separation, for example between the legal entities of a group.
- Administration must be strictly separated: the Space Owners of one unit must not manage the members of another.

If users work across units, or need data from several of them, use groups instead.

## [Default Space](https://docs.smartchat.ai.t-systems.net/user/concepts/spaces/#default-space)

Every Smartchat instance comes with a **Default space** that all users belong to. It cannot be deleted or renamed, and it is not visible in the Chat Interface.
