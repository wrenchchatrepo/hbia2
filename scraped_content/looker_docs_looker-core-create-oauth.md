# https://cloud.google.com/looker/docs/looker-core-create-oauth

Depth: 3

**Note:** To learn how to set up OAuth for authentication, see the [Use Google OAuth for Looker (Google Cloud core) user authentication](/looker/docs/looker-core-oauth-authentication) documentation page.

An OAuth client must be set up and OAuth credentials must be generated as part of Looker (Google Cloud core) instance creation, even if you want to use a [different authentication method](/looker/docs/looker-core-user-authentication) for authenticating your users into a Looker (Google Cloud core) instance.

## Required roles

To use the Google Cloud console to create and edit OAuth credentials, you need the following permissions. (To hide the list of permissions, collapse the **Required permissions** section.) 

#### Required permissions

  * clientauthconfig.*
    * clientauthconfig.brands.create
    * clientauthconfig.brands.delete
    * clientauthconfig.brands.get
    * clientauthconfig.brands.list
    * clientauthconfig.brands.update
    * clientauthconfig.clients.create
    * clientauthconfig.clients.createSecret
    * clientauthconfig.clients.delete
    * clientauthconfig.clients.get
    * clientauthconfig.clients.getWithSecret
    * clientauthconfig.clients.list
    * clientauthconfig.clients.listWithSecrets
    * clientauthconfig.clients.undelete
    * clientauthconfig.clients.update
  * oauthconfig.*
    * oauthconfig.clientpolicy.get
    * oauthconfig.testusers.get
    * oauthconfig.testusers.update
    * oauthconfig.verification.get
    * oauthconfig.verification.submit
    * oauthconfig.verification.update

You might also be able to get the required permissions through [custom roles](/iam/docs/creating-custom-roles) or other [predefined roles](/iam/docs/understanding-roles). For more information about granting roles, see the [Manage access to projects, folders, and organizations](/iam/docs/granting-changing-revoking-access) page in the Identity and Access Management (IAM) documentation.

## Before you create a Looker (Google Cloud core) instance

Complete the following steps before you create a Looker (Google Cloud core) instance.

### Configure the user consent screen, scopes, and test users

The first step in creating your OAuth credentials is configuring the consent screen. The consent screen is shown to a user of the Looker (Google Cloud core) instance at their first login and at any point when their authorization [expires](https://support.google.com/a/answer/7576830) or is [revoked by the user](https://developers.google.com/identity/gsi/web/guides/revoke).

  1. Navigate to the project you want to create the OAuth client in. You can set up the OAuth client in any Google Cloud project you want. It does not need to be the same project as the Looker (Google Cloud core) instance. However, the Looker (Google Cloud core) API **must be enabled** in this project.
  2. Navigate to **APIs & Services > Credentials**.
  3. Click **Create Credentials**.
  4. From the drop-down menu, select **OAuth client ID**.
  5. Click **Configure Consent Screen**.
  6. Under **User Type** , select one of the following:

     * **Internal** : Only users within your [organization](/resource-manager/docs/cloud-platform-resource-hierarchy#organizations)
     * **External** : Users with any kind of [Google Account](https://www.google.com/account/about/)
**Note:** If you want a user such as Google Support to access your instance using OAuth and IAM, **User Type** must be set to **External** and the Support user must be [added through IAM](/looker/docs/looker-core-oauth-authentication). The **User Type** setting can be edited at any point.
  7. Click **Create**.

  8. Clicking **Create** opens the [**OAuth consent screen**](https://support.google.com/cloud/answer/6158849#userconsent&zippy=%2Cuser-consent) panel.

     * The **App name** , **User support email** , and **Developer contact information** fields are required.
     * In the **Authorized domains** section, the domain must match the domain of the Looker (Google Cloud core) instance that uses the OAuth credentials. If you are going to create a [custom domain](/looker/docs/looker-core-custom-domain) for your Looker (Google Cloud core) instance and know the domain you will assign to it, you may enter it now. Otherwise, you may leave this field empty and add the authorized redirect URI after the Looker (Google Cloud core) instance is created.
  9. Click **Save and continue**.

  10. If needed, add [scopes](https://developers.google.com/identity/protocols/oauth2/scopes) in the **Scopes** panel. Click **Save and continue**.

  11. If needed, add test users in the **Test users** panel. Click **Save and continue**.

  12. Click **Back to dashboard** on the **Summary** panel. This returns you to the **Create OAuth client ID** page.

### Generate the OAuth client ID and client secret

After the initial configuration of the consent screen, you can create an OAuth client and generate the client ID and client secret for that client. These values are required during creation of the Looker (Google Cloud core) instance.

  1. From the **Credentials** page, click **Create Credentials**.
  2. From the drop-down menu, select **OAuth client ID**.
  3. In the **Application type** drop-down, select **Web application**.
  4. In the **Name** field, enter a name for your OAuth client.
  5. Click **Create**.

After you click **Create** , an **OAuth client created** window appears. This window displays the client ID and client secret created for your OAuth client. These values will be required when you [create the Looker (Google Cloud core) instance](/looker/docs/looker-core-instance-create#oauth).

Optionally, click **Download JSON** to download the credential information in a `.json` file. Click **OK** to close the window.

## During Looker (Google Cloud core) instance creation

When you are [creating the Looker (Google Cloud core) instance](/looker/docs/looker-core-instance-create), add the OAuth client ID and client secret in the [**OAuth Application Credentials** section](/looker/docs/looker-core-instance-create#oauth). An instance cannot be created without OAuth credentials.

## After you create a Looker (Google Cloud core) instance

As soon as your OAuth client has the correct authorized domain for the Looker (Google Cloud core) instance, it will be ready for use. If you added the authorized domain during client setup, your OAuth configuration is complete. If you did not add the authorized domain during setup, complete the following instructions to finish configuration.

### Add the authorized redirect URI to the OAuth client

If you have not done so already, follow these steps to enter the URL of the newly created Looker (Google Cloud core) instance into the OAuth client.

  1. After you have created a Looker (Google Cloud core) instance, find and copy the URL for the instance. You can find the URL on the [**Instances** page](/looker/docs/looker-core-view-console).

**Note:** If you are setting up a [custom domain](/looker/docs/looker-core-custom-domain) for your instance, be sure to complete that setup before copying the URL. Once you add the custom domain to the OAuth client, users will no longer be able to log in to the autogenerated instance URL that was granted when the instance was created, even if that domain is also in the OAuth client.

  1. In the Google Cloud console, navigate to **APIs & Services > Credentials**.
  2. Under the **OAuth 2.0 Client IDs** heading, click the name of the client you created.
  3. In the **Authorized redirect URIs** section, click **Add URI**.
  4. Paste the URL of the Looker (Google Cloud core) instance into the **URIs** field. Add `/oauth2callback` to the end of the URL. For example: `https://uuid.looker.app/oauth2callback`
  5. Click **Save**.

**Note:** It may take from five minutes to a few hours for the update to take effect.

### Manage users

Once the OAuth client is configured and the Looker (Google Cloud core) instance is [created](/looker/docs/looker-core-instance-create), you can [choose the authentication method](/looker/docs/looker-core-user-authentication) for your instance.

If using OAuth as your primary authentication method, complete the steps as described on the [Use Google OAuth for Looker (Google Cloud core) user authentication](/looker/docs/looker-core-oauth-authentication) documentation page to complete OAuth setup for user authentication.

Once your authentication method is set up, you can add or remove users through your identity provider and [manage them within Looker](/looker/docs/looker-core-user-management).

### Edit the OAuth client for a Looker (Google Cloud core) instance

If you want, you can edit or change the OAuth credentials for your Looker (Google Cloud core) instance by following these steps:

  1. Set up the new client or credentials.
  2. In the Google Cloud console, from the **Instances** page, click on an instance's name to open the **DETAILS** page.
  3. From the **DETAILS** page, click **Edit**.
  4. On the **Edit Looker (Google Cloud core) instance** page, enter the new values in the **OAuth Client ID** and **OAuth Client Secret** fields.
  5. Click **Save**.

## What's next

  * [Create a public IP Looker (Google Cloud core) instance](/looker/docs/looker-core-instance-create)
  * [Create a private IP Looker (Google Cloud core) instance](/looker/docs/looker-core-create-private-ip)