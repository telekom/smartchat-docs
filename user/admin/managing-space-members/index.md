# Managing Space Members

Source: https://docs.smartchat.ai.t-systems.net/user/admin/managing-space-members/

> Add and remove members of your Space and promote them to Space Owner, directly in Smartchat.

Space Owners manage who belongs to their Space from **Administration → Space Owner → Space Members**. The page is only shown to Space Owners and acts on the Space chosen in **Selected Space**.

*\[Image: Space Members page with the role switches and the Add User button]*

The list shows every member of the Space with four columns:

| Column | Meaning |
| - | - |
| **Role** | **User** or **Space Owner**. Click the other half of the switch to change the role (see below). |
| **Email** | The member’s login. Click it to open the member’s details. |
| **Last Active** | When the member last used Smartchat. Members who have not logged in yet show no date. |
| **Created at** | When the account was created. |

## [Adding a member](https://docs.smartchat.ai.t-systems.net/user/admin/managing-space-members/#adding-a-member)

1. Click **Add User** above the list.
2. Enter the person’s **Email** in the **Add new member** dialog and click **Add**.

*\[Image: Add new member dialog]*

What happens next depends on the email address:

- **The person already has a Smartchat account**: they are added to the Space with the **User** role and see it in their Space selector on their next page load.
- **The email is unknown**: an account is created for them. They receive an invitation email from the identity provider, and they already appear in the list with the **User** role before their first login. On instances with [account creation only through your identity provider](https://docs.smartchat.ai.t-systems.net/user/admin/single-sign-on/#account-creation-only-through-your-identity-provider) enabled, they have to sign in once before you can add them.

New members can chat right away and use the items shared with them, such as the **{Space} - General** collection. To let them administer the Space, promote them to Space Owner.

> **Seats**
>
> If your contract limits the number of seats in a Space, adding a member beyond that limit fails with a license error. Contact support to raise the limit.

## [Adding several members at once](https://docs.smartchat.ai.t-systems.net/user/admin/managing-space-members/#adding-several-members-at-once)

To add a whole team, switch the **Add new member** dialog to **Several members at once** (the icon next to the title) and paste the email addresses into the text box. One address per line, separated by commas or semicolons, copied recipients from Outlook (`"Doe, Jane" <jane.doe@example.com>`) and a copied column from Excel all work; duplicates are dropped automatically.

Below the box you see how many addresses were recognised. Entries that are not email addresses are listed in red and must be fixed or removed before **Add** becomes available. Then click **Add N members**.

Each address is handled like a single add: existing accounts join the Space, unknown addresses get an account and an invitation email. When the request finishes, the dialog reports how many members were added and lists any address that could not be added with the reason. **Copy failed email addresses** puts those on the clipboard so you can fix them and try again; already added members are skipped on a retry.

> **Limit**
>
> Up to 100 members can be added in one go. For larger groups, an identity provider integration (for example Entra ID) is the better fit. Contact T-Systems.

## [Changing a member’s role](https://docs.smartchat.ai.t-systems.net/user/admin/managing-space-members/#changing-a-members-role)

A Space has two roles: **User** and **Space Owner**. Owners get everything described in [Administration](https://docs.smartchat.ai.t-systems.net/user/admin/); see [Roles](https://docs.smartchat.ai.t-systems.net/user/concepts/roles/) for the complete matrix.

Either use the **Role** switch in the list, or open the member (click the email) and use the **Role** switch of the **Edit member** dialog.

*\[Image: Edit member dialog with the Role switch]*

The new role is applied immediately, there is no separate save step. If the update fails, the switch flips back and a toast explains why.

Two rules apply:

- **You cannot change your own role.** The switch in your own row is greyed out. Ask another owner to promote or demote you.
- **A Space keeps at least one owner.** The last remaining owner cannot be demoted or removed while the Space has other members.

## [Removing a member](https://docs.smartchat.ai.t-systems.net/user/admin/managing-space-members/#removing-a-member)

1. Hover the member’s row and click the bin icon (**Remove user**), or open the member and click **Delete** in the **Edit member** dialog.
2. Confirm with **Remove**.

*\[Image: Remove user confirmation]*

The person loses access to the Space immediately: they are removed from the Space itself and from all of its groups, including custom groups. Their Smartchat account and their other Spaces are not affected. You cannot remove yourself.

## [Restrictions](https://docs.smartchat.ai.t-systems.net/user/admin/managing-space-members/#restrictions)

- **Space owner group**: the **SpaceOwners {Space}** group mirrors the roles above and cannot be edited, see [Groups](https://docs.smartchat.ai.t-systems.net/user/concepts/groups/#groups-every-space-has). Space Owners have every [permission](https://docs.smartchat.ai.t-systems.net/user/concepts/permissions/#space-owners) of their Space.
- **Application Owners** who are not owners of a Space cannot add or remove its members here. They manage Space memberships per user under [**Application Owner → Users**](https://docs.smartchat.ai.t-systems.net/user/admin/application-owner/#users).

> **Who can delete accounts**
>
> Since v3.15.1, a Space Owner can delete the account of a user who is no longer a member of any Space. Only Application Owners can delete the account of a user with an application-level role, such as Application Owner, and on instances that manage accounts through the identity provider, only Application Owners can delete accounts at all.

> **Identity fields are locked**
>
> The **Email** and **Username** of an existing member cannot be edited in Smartchat. Name and email changes come from your identity provider.
