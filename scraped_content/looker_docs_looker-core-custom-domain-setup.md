# https://cloud.google.com/looker/docs/looker-core-custom-domain-setup

Depth: 3

You can serve your instance through a custom web domain rather than through the default domain that Looker (Google Cloud core) provides.

This documentation page describes how to use the Google Cloud console to set up a custom domain for any type of Looker (Google Cloud core) instance.

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

After a custom domain is set up in the Google Cloud console, you must configure your network to allow users to access the domain. To learn more about that configuration for your use case, review the following documentation pages:

  * [Set up and access a custom domain for a public IP Looker (Google Cloud core) instance](/looker/docs/looker-core-custom-domain)
  * [Custom domain networking options for Looker (Google Cloud core) private IP instances](/looker/docs/looker-core-custom-domain-private-ip-overview)