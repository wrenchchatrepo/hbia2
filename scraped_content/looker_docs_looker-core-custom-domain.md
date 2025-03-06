# https://cloud.google.com/looker/docs/looker-core-custom-domain

Depth: 3

You can serve your instance through a custom web domain rather than through the default domain that Looker (Google Cloud core) provides.

This documentation page describes custom domain setup for instances that meet **one of** the following criteria:

  * The instance is public IP only.
  * The instance uses both public IP and private IP.

If you create a custom domain with an instance that uses a public network connection, Google provides a managed, auto-renewing SSL certificate.

To implement a custom domain for this kind of instance, you must perform the following steps:

  1. Set up the custom domain.
  2. Create the DNS A record.
  3. Update the OAuth credentials.

**Important:** If your instance has both the public IP and the private IP connection options enabled, you can follow the instructions on this page; however, if you disable the public IP option at any point, your custom domain will be invalidated and you will need to recreate it for your private network connection.

## Set up a custom domain

After your Looker (Google Cloud core) instance has been created, you can set up a custom domain.

### Before you begin

**Note:** Custom domains cannot be created using a looker.com domain.

Before you can customize the domain of your Looker (Google Cloud core) instance, identify where your domain's DNS records are stored, so that you can update them.

#### Required roles

To get the permissions that you need to create a custom domain for a Looker (Google Cloud core) instance, ask your administrator to grant you the [Looker Admin ](https://cloud.google.com/iam/docs/understanding-roles#looker.admin) (`roles/looker.admin`) IAM role on the project the instance resides in. For more information about granting roles, see [Manage access to projects, folders, and organizations](/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](/iam/docs/creating-custom-roles) or other [predefined roles](/iam/docs/understanding-roles). 

### Create a custom domain

**Note:** You cannot modify a custom domain once it is created. If you want to make changes to the custom domain, you must delete the existing custom domain and create a new one.

In the Google Cloud console, follow these steps to customize the domain of your Looker (Google Cloud core) instance:

  1. On the **Instances** page, click the name of the instance for which you would like to set up a custom domain.
  2. Click the **CUSTOM DOMAIN** tab.
  3. Click **ADD A CUSTOM DOMAIN**.

![](/static/looker/docs/images/core-custom-domain-1.png)

This opens the **Add a new custom domain** panel.

  4. Using only letters, numbers, and dashes, enter the hostname of up to 64 characters for the web domain that you would like to use — for example: `looker.examplepetstore.com`.

![](/static/looker/docs/images/core-custom-domain-2.png)

  5. Click **DONE** on the **Add a new custom domain** panel to return to the **CUSTOM DOMAIN** tab.

**Note:** Updating the custom domain takes 10 to 15 minutes to complete.

Once your custom domain is set up, it is displayed in the **Domain** column on the **CUSTOM DOMAIN** tab of the Looker (Google Cloud core) [instance details page](/looker/docs/looker-core-custom-domain-settings) in the Google Cloud console.

After your custom domain has been created, you can [view information](/looker/docs/looker-core-custom-domain-settings) about it, or [delete](/looker/docs/looker-core-custom-domain-delete) it.

## Access the custom domain

To set up access to a custom domain for a Looker (Google Cloud core) instance that uses public IP, create a DNS record and update the OAuth credentials.

### Before you begin

To get the permissions that you need to set up access to a public IP custom domain, ask your administrator to grant you the following IAM roles on the project the instance resides in: 

  * [Looker Admin ](https://cloud.google.com/iam/docs/understanding-roles#looker.admin) (`roles/looker.admin`)
  * [DNS Admin ](https://cloud.google.com/iam/docs/understanding-roles#dns.admin) (`roles/dns.admin`)
  * Use Google OAuth: [OAuth Config Editor ](https://cloud.google.com/iam/docs/understanding-roles#oauthconfig.editor) (`roles/oauthconfig.editor`) 

For more information about granting roles, see [Manage access to projects, folders, and organizations](/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](/iam/docs/creating-custom-roles) or other [predefined roles](/iam/docs/understanding-roles). 

### Create a DNS record

Wherever your DNS records are stored, create an A record in the DNS zone for your domain. For an instance that uses a public network connection, use the Looker (Google Cloud core) instance's ingress public IP for the A record's IP address. The ingress public IP can be found on the [**Details**](/looker/docs/looker-core-view-console#the_details_and_custom_domain_tabs) tab of the Looker (Google Cloud core) instance in the Google Cloud console. (It is also displayed in the **Data** field in the **Update your DNS records** section of the **Add a new custom domain** panel.)

If a **VERIFY DOMAIN** button appears on the **CUSTOM DOMAIN** tab of the Looker (Google Cloud core) instance, your DNS record may require additional configuration. Click **VERIFY DOMAIN** to complete the setup of your custom domain.

**Note:** It may take up to 24 hours for any changes to your DNS record to take effect. The SSL certificate that is associated with your DNS record may require several minutes to activate.

Once your domain's DNS records are updated and your domain has been verified in the Google Cloud console, the [status](/looker/docs/looker-core-custom-domain-settings) of the custom domain that is mapped to the instance will be updated from **Unverified** to **Available** on the **Custom domain** tab.

### Update the OAuth credentials

**Note:** You can use any OAuth client to create authorization credentials for your Looker (Google Cloud core) instance. As an example, these steps walk you through updating the credentials using the Google Cloud console. If you are using a different client, adjust the steps accordingly.

  1. Access your OAuth client by navigating in the Google Cloud console to **APIs & Services > Credentials** and selecting the OAuth client ID for the OAuth client that is used by your Looker (Google Cloud core) instance.
  2. Click the **Add URI** button to update the **Authorized JavaScript origins** field in your OAuth client to include the same DNS name that your organization will use to access Looker (Google Cloud core). For example, if your custom domain is `looker.examplepetstore.com`, you would enter `looker.examplepetstore.com` as the URI.

![](/static/looker/docs/images/core-custom-domain-ajso.png)

  3. [Update or add](/looker/docs/looker-core-create-oauth#add_the_authorized_redirect_uri_to_the_oauth_client) the custom domain to the list of **Authorized redirect URIs** for the [OAuth credentials that you used](/looker/docs/looker-core-create-oauth) when you created the Looker (Google Cloud core) instance. Add `/oauth2callback` to the end of the URI. For example, if your custom domain is `looker.examplepetstore.com`, you would enter `looker.examplepetstore.com/oauth2callback`.

![](/static/looker/docs/images/core-custom-domain-aruris.png)

### Add users

Once the preceding steps are completed, the custom domain URL is accessible to users.

Ensure that the [user authentication method](/looker/docs/looker-core-user-authentication) is completely set up for the Looker (Google Cloud core) instance before adding users to the instance.

## What's next

  * [Manage users within Looker (Google Cloud core)](/looker/docs/looker-core-user-management)
  * [Configure your Looker (Google Cloud core) instance](/looker/docs/looker-core-instance-setup)
  * [Connect Looker (Google Cloud core) to your database](/looker/docs/looker-core-dialects)