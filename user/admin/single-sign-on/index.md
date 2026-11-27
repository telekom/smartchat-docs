# Single Sign-On

Source: https://docs.smartchat.ai.t-systems.net/user/admin/single-sign-on/

> How people sign in to Smartchat through your identity provider, how IdP attributes map to Space and group membership, and the options that let your identity provider decide who has an account and which roles they get.

With single sign-on (SSO), people sign in to Smartchat with their company account. Smartchat sends them to your identity provider, for example Microsoft Entra ID or Active Directory Federation Services (ADFS), which checks their password and any second factor. Their name and email address come from your identity provider and cannot be edited in Smartchat.

T-Systems sets up single sign-on together with the administrators of your identity provider, and configures the options on this page for your instance. Contact T-Systems to switch an option on or off, or to change which values Smartchat reads from your identity provider.

## [Mapping IdP attributes](https://docs.smartchat.ai.t-systems.net/user/admin/single-sign-on/#mapping-idp-attributes)

With every sign-in, your identity provider can send IdP attributes of the person, also called claims, for example a role or a group they have in your Active Directory. Smartchat can map an IdP attribute in two ways:

| Mapping | Set up by | Where |
| - | - | - |
| [IdP attribute to Space membership](https://docs.smartchat.ai.t-systems.net/user/admin/single-sign-on/#idp-attribute-to-space-membership) | Application Owners | **Application Owner → Spaces**, field **IdP auto-assignment attribute** |
| [IdP attribute to group membership within a Space](https://docs.smartchat.ai.t-systems.net/user/admin/single-sign-on/#idp-attribute-to-group-membership-within-a-space) | Space Owners | **Space Owner → Groups**, field **Identity provider group attributes** |

In both cases, enter the IdP attribute exactly as your identity provider sends it, including spelling, upper and lower case. Ask the administrators of your identity provider for the exact values.

Smartchat reads the IdP attributes every time the person signs in. When your identity provider starts sending an IdP attribute, the person gets what it maps to at their next sign-in. When it stops, they lose it at their next sign-in. What your identity provider assigns cannot be taken away in Administration.

### [IdP attribute to Space membership](https://docs.smartchat.ai.t-systems.net/user/admin/single-sign-on/#idp-attribute-to-space-membership)

Each Space can have an **IdP auto-assignment attribute**, set under **Administration → Application Owner → Spaces**, see [Managing Spaces and Users](https://docs.smartchat.ai.t-systems.net/user/admin/application-owner/). Everyone whose identity provider sends this IdP attribute becomes a **User** of the Space. Several Spaces can have the same IdP attribute.

Further IdP attributes, agreed with T-Systems during setup, assign roles:

- **Space Owner of a Space**: the Space’s IdP attribute with a Space Owner marker makes the person **Space Owner** of that Space. If no Space has the IdP attribute yet, Smartchat creates the Space, names it after the IdP attribute and sets the IdP attribute. If a Space of that name already exists without the IdP attribute, Smartchat assigns nothing: set the IdP attribute on that Space.
- **Space Owner everywhere**: makes the person **Space Owner** instead of **User** in every Space they get from your identity provider.
- **Application Owner**: makes the person **Application Owner**.

### [IdP attribute to group membership within a Space](https://docs.smartchat.ai.t-systems.net/user/admin/single-sign-on/#idp-attribute-to-group-membership-within-a-space)

Space Owners organise the members of their Space in [groups](https://docs.smartchat.ai.t-systems.net/user/concepts/groups/) under **Administration → Space Owner → Groups**. A group can list **Identity provider group attributes**: everyone whose identity provider sends one of these IdP attributes is added to the group. The group shows them as **Managed by identity provider and cannot be removed manually.**

This only sets group membership. It does not add anyone to the Space: people get into a Space through [IdP attribute to Space membership](https://docs.smartchat.ai.t-systems.net/user/admin/single-sign-on/#idp-attribute-to-space-membership), [Space membership by email domain](https://docs.smartchat.ai.t-systems.net/user/admin/single-sign-on/#space-membership-by-email-domain) or an administrator.

## [Space membership by email domain](https://docs.smartchat.ai.t-systems.net/user/admin/single-sign-on/#space-membership-by-email-domain)

Smartchat can add everyone whose email address belongs to a domain, for example `example.com`, to a Space as **User** when they sign in. This needs no IdP attributes from your identity provider. Removing such a person from the Space only lasts until their next sign-in, when Smartchat adds them again. The settings of that Space cannot be changed in Administration.

## [Optional restrictions](https://docs.smartchat.ai.t-systems.net/user/admin/single-sign-on/#optional-restrictions)

T-Systems can enable these options for your instance. Both are off by default.

### [Account creation only through your identity provider](https://docs.smartchat.ai.t-systems.net/user/admin/single-sign-on/#account-creation-only-through-your-identity-provider)

With this option enabled, no accounts can be created in Smartchat directly. Instead, a person’s account is created when they first sign in through single sign-on. In Administration:

- People who have never signed in cannot be added to a Space yet. See [People who have never signed in](https://docs.smartchat.ai.t-systems.net/user/admin/application-owner/#people-who-have-never-signed-in).
- Users cannot be deleted.
- Assigning existing users to Spaces and changing their roles works as usual.

**Users** under **Application Owner** shows: **Users come from the identity provider, so they cannot be created or deleted here. Their spaces and roles can still be changed.**

### [Member and role management only through your identity provider](https://docs.smartchat.ai.t-systems.net/user/admin/single-sign-on/#member-and-role-management-only-through-your-identity-provider)

With this option enabled, your identity provider alone decides who belongs to which Space and with which role. It includes everything from [Account creation only through your identity provider](https://docs.smartchat.ai.t-systems.net/user/admin/single-sign-on/#account-creation-only-through-your-identity-provider), and in addition:

- Neither Application Owners nor Space Owners can add or remove members or change a role in Administration. Administration shows **Users and roles come from the identity provider and cannot be changed here.**
- Every Space needs an **IdP auto-assignment attribute**. A Space cannot be created or saved without one, because the IdP attribute is the only way people get into it.
