# https://cloud.google.com/looker/docs/looker-core-user-management

Depth: 3

Within a Looker (Google Cloud core) instance, several settings are available for managing users.

## Required permission

In order to manage users within a Looker (Google Cloud core) instance, you must have the [Admin role](/looker/docs/admin-panel-users-roles#default_permission_sets) within Looker.

## The Users page

The [**Admin > Users** page](/looker/docs/admin-panel-users-users) within Looker displays active users within Looker (Google Cloud core) and lets you make certain edits to their accounts within Looker, such as editing the following account settings:

  * [locale](/looker/docs/admin-panel-users-users#locale)
  * [number format](/looker/docs/admin-panel-users-users#number_format)
  * [timezone](/looker/docs/admin-panel-users-users#timezone)
  * [Groups](/looker/docs/admin-panel-users-users#groups)
  * [Looker roles](/looker/docs/admin-panel-users-users#roles)

Users' names and email addresses must be edited within the identity provider that is used for authentication.

Unlike within Looker (original) instances, the following is not available in the Looker (Google Cloud core) **Users** page:

  * [add users](/looker/docs/admin-panel-users-users#adding_users) (with the exception of service accounts)
  * [send setup link / send reset link](/looker/docs/admin-panel-users-users#send_setup_link_send_reset_link)
  * [set up two-factor authentication](/looker/docs/admin-panel-users-users#two-factor_secret)
  * [sudo](/looker/docs/admin-panel-users-users#impersonating_sudoing_users) as a user

## Adding users to a Looker (Google Cloud core) instance

To add individual Looker (Google Cloud core) users, add users within your [identity provider](/looker/docs/looker-core-user-authentication). Their Looker accounts will be created upon first login. Individual users cannot be added on the **Users** page; however, API-only service accounts can be added on the **Users** page.

**Note:** Looker does not notify users that they have been added to the Looker (Google Cloud core) instance. You must notify users they have been added and provide login information, such as URL.

### Creating an API-only service account

**Note:** Service accounts are the only accounts that can be created within a Looker (Google Cloud core) instance.

You can create [API-only accounts (often called "service accounts")](/looker/docs/api-auth#managing_api_credentials) from the **Users** page within a Looker (Google Cloud core) instance. These accounts can be granted Admin Looker roles and can be granted Looker API credentials. However, these accounts cannot log in to Looker (Google Cloud core) through the UI. To add a service account, follow these steps:

  1. Click the **Add Service Account** button.
  2. Enter an email address for the service account.
  3. Select the [Groups](/looker/docs/admin-panel-users-groups) and [Roles](/looker/docs/admin-panel-users-roles) to assign to the service account.
  4. Click the **Save** button.

**Note:** Service accounts within Looker (Google Cloud core) are not the same as [Google service accounts](/iam/docs/service-account-overview) and are not governed by IAM.

## Removing access to Looker (Google Cloud core)

**Important:** We recommend that you remove access to a Looker (Google Cloud core) instance by using the identity provider that was used for authentication rather than by disabling or deleting the user from the **Users** page. 

Deleting users from a Looker (Google Cloud core) instance that is [associated with a Looker Studio Pro subscription](/looker/docs/looker-core-lsp) reduces the number of complimentary Looker Studio Pro licenses that are allocated to your instance. If the number of complimentary Pro licenses that are allocated to your instance becomes less than the number that is in use, the difference will be converted immediately to paid licenses, subject to Looker Studio Pro [pricing](/looker-studio#pricing).

Remove access to a Looker (Google Cloud core) instance by updating the identity provider that was used for authentication. Although the user can no longer log in to the instance, the user account will still appear active on the **Users** page. To remove the user account from the **Users** page, [delete](/looker/docs/admin-panel-users-users#deleting_users) the user within the Looker (Google Cloud core) instance.

## Selecting an authentication method for Looker (Google Cloud core) users

An OAuth client must be set up as part of instance creation, and OAuth authentication is the backup authentication method for Looker (Google Cloud core). However, you can choose between several different primary authentication methods. The [Authentication methods for Looker (Google Cloud core)](/looker/docs/looker-core-user-authentication) documentation page lists the available authentication methods.

## Setting a default Looker role within the Looker (Google Cloud core) instance

Before you add any users, you can set the default [Looker role](/looker/docs/admin-panel-users-roles) that will be granted to user accounts with the Looker Instance User IAM role upon their first login to a Looker (Google Cloud core) instance. To set a default role, follow the steps provided in the documentation for your identity provider: [OAuth](/looker/docs/looker-core-oauth-authentication#setting_a_default_looker_role_within_the_instance), [SAML](/looker/docs/admin-panel-authentication-saml#default_groups_and_roles), or [OpenID Connect](/looker/docs/admin-panel-authentication-openid-connect#default_groups_and_roles).

## What's next

  * [Connect Looker (Google Cloud core) to your database](/looker/docs/looker-core-dialects)
  * [Configure a Looker (Google Cloud core) instance](/looker/docs/looker-core-instance-setup)
  * [Looker (Google Cloud core) admin settings](/looker/docs/looker-core-admin-looker)
  * [Administer a Looker (Google Cloud core) instance from the Google Cloud console](/looker/docs/looker-core-admin-console)