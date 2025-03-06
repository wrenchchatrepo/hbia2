# https://cloud.google.com/looker/docs/looker-core-oauth-authentication

Depth: 3

**Note:** To learn how to set up an OAuth client and credentials as part of instance creation, see the [Create OAuth authorization credentials for a Looker (Google Cloud core) instance](/looker/docs/looker-core-create-oauth) documentation page.

Google OAuth is used in conjunction with Identity and Access Management (IAM) to authenticate Looker (Google Cloud core) users.

When using OAuth for authentication, Looker (Google Cloud core) authenticates users through the [OAuth 2.0](https://developers.google.com/identity/protocols/oauth2) protocol. Use any OAuth 2.0 client to create authorization credentials when creating an instance. As an example, this page walks you through the steps to set up authentication for a Looker (Google Cloud core) instance using the Google Cloud console to create OAuth credentials.

If another method is the primary form of authentication, Google OAuth is by default the backup authentication method. Google OAuth is also the authentication method that Cloud Customer Care uses when providing support.

## Authentication and authorization with OAuth and IAM

When used with OAuth, [Looker (Google Cloud core) IAM roles](/looker/docs/looker-core-access-control) provide the following levels of authentication and authorization for all Looker (Google Cloud core) instances within a given Google Cloud project. [Assign](/looker/docs/looker-core-oauth-authentication#adding-users) one of the following IAM roles to each of your principals, depending on the levels of access that you want them to have:

IAM Role | Authentication | Authorization  
---|---|---  
Looker Instance User (`roles/looker.instanceUser`) | Can sign in to Looker (Google Cloud core) instances | Upon first login to Looker (Google Cloud core), granted the default Looker role set in Roles for new users Cannot access Looker (Google Cloud core) resources in the Google Cloud console.  
Looker Viewer (`roles/looker.viewer`) | Can sign in to Looker (Google Cloud core) instances | Upon first login to Looker (Google Cloud core), granted the default Looker role set in Roles for new users Can view the list of Looker (Google Cloud core) instances and instance details in the Google Cloud console  
Looker Admin (`roles/looker.admin`) | Can sign in to Looker (Google Cloud core) instances | Upon first login to Looker (Google Cloud core), this role (or a custom role that includes the `looker.instances.update` permission) defaults to the [Admin](/looker/docs/admin-panel-users-roles#default_roles) Looker role within the instance  Can perform all administrative tasks for Looker (Google Cloud core) within the Google Cloud console  
  
Additionally, user accounts with the [`owner`](/iam/docs/understanding-roles#basic) role for a project can sign in and administer any Looker (Google Cloud core) instances within that project. These users will be granted the [Admin](/looker/docs/admin-panel-users-roles#default_roles) Looker role.

If the predefined roles don't provide the set of permissions that you want, you can also create your own [custom roles](/iam/docs/creating-custom-roles).

Looker (Google Cloud core) accounts are created at the time of first login to a Looker (Google Cloud core) instance.

## Configuring OAuth within the Looker (Google Cloud core) instance

Within the Looker (Google Cloud core) instance, the **Google** page in the **Authentication** section of the **Admin** menu lets you configure some Google OAuth settings.

### Setting a default Looker role within the Looker (Google Cloud core) instance

**Note:** The default Looker role will be granted upon first login. If there are any changes to the user's IAM role after the first login, those changes won't affect the Looker role that is assigned to the user.

Before you add any users, you can set the default [Looker role](/looker/docs/admin-panel-users-roles) that will be granted to user accounts with the Looker Instance User (`roles/looker.instanceUser`) IAM role or the Looker Viewer (`roles/looker.viewer`) IAM role upon their first login to a Looker (Google Cloud core) instance. To set a default role, follow these steps:

  1. Navigate to the **Google** page within the **Authentication** section of the **Admin** menu.
  2. In the **Roles for new users** setting, select the role that you want to grant all new users by default. The setting contains a list of all the [default roles](/looker/docs/admin-panel-users-roles#default_roles) and [custom roles](/looker/docs/admin-panel-users-roles#assigning_roles) within the Looker (Google Cloud core) instance.

User accounts with a Looker Admin (`roles/looker.admin`) IAM role will be granted the [Admin](/looker/docs/admin-panel-users-roles#default_roles) Looker role regardless of the role selected in the **Roles for new users** setting. If you need to, you can change the Admin role to a different role.

### Specify the method used to merge OAuth users to a Looker (Google Cloud core) account

In the **Merge Users Using** field, specify the method to be used to merge a first-time OAuth login to an existing user account. You can merge users from the following systems:

  * **SAML**
  * **OIDC**

If you have more than one system in place, you can specify more than one system to merge by in this field. Looker (Google Cloud core) will look up users from the systems listed _in the order that they are specified_. For example, if you first created some users using OIDC and then later used SAML, Looker (Google Cloud core) would merge first by OIDC and second by SAML.

When a user logs in for the first time through OAuth, this option will connect the user into their existing account by finding the account with a matching email address. If there is no existing account for the user, a new user account will be created.

## Adding users to a Looker (Google Cloud core) instance

**Note:** Access to the Looker (Google Cloud core) instance is granted through IAM. However, Looker user accounts are not created until users agree to the OAuth consent screen and sign in to the instance.

Once a Looker (Google Cloud core) instance has been [created](/looker/docs/looker-core-instance-create), users can be added through IAM. To add users, follow these steps:

  1. Be sure that you have the [Project IAM Admin](/iam/docs/understanding-roles#resourcemanager.projectIamAdmin) role or [another role that lets you manage IAM access](/iam/docs/granting-changing-revoking-access#required-permissions).
  2. Navigate to the Google Cloud console project that the Looker (Google Cloud core) instance resides in.

**Note:** IAM roles are global within a project. If there is more than one Looker (Google Cloud core) instance in a project, IAM roles that are granted within that project will apply to all Looker (Google Cloud core) instances that reside there.
  3. Navigate to the **IAM & Admin > IAM** section of the Google Cloud console.

  4. Select **Grant Access**.

  5. In the **Add principals** section, add one or more of the following:

     * A Google Account email
     * A Google Group
     * A Google Workspace domain
  6. In the **Assign roles** section, select one of the [predefined Looker (Google Cloud core) IAM roles](/looker/docs/looker-core-access-control#roles) or a custom role that you have added.

  7. Click **Save**.

  8. Communicate to new Looker (Google Cloud core) users that access has been granted and direct them to the URL for the instance. From there they can sign in to the instance, at which point their accounts will be created. No automated communication will be sent.

If you change a user's IAM role, the IAM role propagates to the Looker (Google Cloud core) instance within a few minutes. If there is an existing Looker user account, that user's Looker role remains unchanged.

All users must be provisioned by the IAM steps described previously, with one exception: You can [create Looker API-only service accounts](/looker/docs/looker-core-user-management#creating_an_api-only_service_account) within the Looker (Google Cloud core) instance.

## Logging in to Looker (Google Cloud core) with OAuth

Upon first login, users will be asked to [sign in with their Google Account](https://support.google.com/accounts/answer/112802). They should use the same account that the Looker Admin listed in the **Add principals** field when granting access. Users will view the [OAuth consent screen](/looker/docs/looker-core-create-oauth#configure_the_user_consent_screen_scopes_and_test_users) that was configured during OAuth client creation. After users agree to the consent screen, their accounts within the Looker (Google Cloud core) instance are created and they will be logged in.

After that, users will be automatically logged in to Looker (Google Cloud core) unless their authorization [expires](https://support.google.com/a/answer/7576830) or is [revoked by the user](https://developers.google.com/identity/gsi/web/guides/revoke). In those scenarios, users will again view the OAuth consent screen and be asked to consent to authorization.

Some users may be assigned API credentials for use in retrieving an API access token. If the authorization for those users expires or is revoked, their API credentials stop working. Any current API access tokens will also stop working. To resolve the issue, the user must re-authorize their credentials by logging back in to the Looker (Google Cloud core) UI for each Looker (Google Cloud core) instance that is affected. Alternatively, using [API-only service accounts](/looker/docs/looker-core-user-management#creating_an_api-only_service_account) helps avoid a credential authorization failure for API access tokens.

## Removing OAuth access to Looker (Google Cloud core)

**Important:** It is recommended that access to a Looker (Google Cloud core) instance be removed using IAM rather than from within the instance.

If you have [a role that lets you manage IAM access](/iam/docs/granting-changing-revoking-access#required-permissions), you can remove access to a Looker (Google Cloud core) instance by [revoking the IAM role](/iam/docs/manage-access-other-resources#revoke-single-role) that granted access. If you remove a user account's IAM role, that change propagates to the Looker (Google Cloud core) instance within a few minutes. The user will no longer be able to authenticate to the instance. However, the user account will still appear active on the **Users** page. To remove the user account from the **Users** page, [delete the user](/looker/docs/admin-panel-users-users#deleting_users) within the Looker (Google Cloud core) instance.

## Using OAuth as a backup authentication method

OAuth is the backup authentication method when [SAML](/looker/docs/admin-panel-authentication-saml) or [OIDC](/looker/docs/admin-panel-authentication-openid-connect) is the primary authentication method.

To set up an OAuth as the backup method, [grant](/looker/docs/looker-core-oauth-authentication#adding-users) each Looker (Google Cloud core) user the appropriate [IAM role](/looker/docs/looker-core-access-control#roles) to log in to the instance.

Once the backup method is set up, users access it through the following steps:

  1. Select **Authenticate with Google** on the sign-in page.
  2. A dialog appears to confirm Google authentication. Select **Confirm** in the dialog.

Users can then log in using their Google Accounts. When first logging in with OAuth, they will be prompted to accept the [OAuth consent screen](/looker/docs/looker-core-create-oauth#configure_the_user_consent_screen_scopes_and_test_users) that was set up during instance creation.

## What's next

  * [Connect Looker (Google Cloud core) to your database](/looker/docs/looker-core-dialects)
  * [Configure a Looker (Google Cloud core) instance](/looker/docs/looker-core-instance-setup)
  * [Looker (Google Cloud core) admin settings](/looker/docs/looker-core-admin-looker)
  * [Administer a Looker (Google Cloud core) instance from the Google Cloud console](/looker/docs/looker-core-admin-console)