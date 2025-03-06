# https://cloud.google.com/looker/docs/looker-core-quickstart-public-ip-standard-edition

Depth: 3

# 

# Create a Looker (Google Cloud core) public IP standard edition instance

Learn how to create a Looker (Google Cloud core) instance that uses default configuration settings. Looker (Google Cloud core) requires approximately 60 minutes to generate a new instance.

* * *

To follow step-by-step guidance for this task directly in the Google Cloud console, click **Guide me** : 

[Guide me](https://console.cloud.google.com/freetrial?redirectPath=/?journey_id=looker--create-instance-public)

* * *

## Before you begin

Before you can create an instance, you need to complete these steps for the Google Cloud project in which you want to create the Looker (Google Cloud core) instance:

  1. In the Google Cloud console, on the project selector page, [create a Google Cloud project](/resource-manager/docs/creating-managing-projects) or navigate to an existing one. 

[ Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. [Make sure that billing is enabled for your Google Cloud project.](/billing/docs/how-to/verify-billing-enabled#console)
  3. [Enable the Looker API](/apis/docs/getting-started#enabling_apis) for your project in the Google Cloud console. When enabling the API, you may need to refresh the console page to confirm that the API has been enabled. 

[ Enable the API](https://console.cloud.google.com/flows/enableapi?apiid=looker.googleapis.com)

  4. Create authorization credentials. You can use any OAuth 2.0 client to create authorization credentials when you're creating an instance. See the [Create authorization credentials for a Looker (Google Cloud core) instance](/looker/docs/looker-core-create-oauth) documentation page for an example that uses the Google Cloud console to create OAuth credentials.
  5. Ensure that the [Looker Admin](/iam/docs/understanding-roles#looker.admin) IAM role is enabled for the Google Cloud project in which you want to create the Looker (Google Cloud core) instance.

## Create the Looker (Google Cloud core) instance

To create a Looker (Google Cloud core) instance that uses default configuration settings, follow these steps:

  1. Click [Go to Looker (Google Cloud core)](https://console.cloud.google.com/looker) and select the Google Cloud project in which you want to create the Looker (Google Cloud core) instance, if it is not already pre-selected. When you click the button, depending on what Looker instances already exist in this project, you'll see one of the following: 
     * If a Looker (Google Cloud core) instance already exists within this project, the **Instances** page will open. Click **Create Instance** to open the instance creation page.
     * If no Looker (Google Cloud core) instances have been created in this project, the Looker (Google Cloud core) product page will open. Click **Create An Instance** to open the instance creation page.
  2. In the **Instance name** field, provide a name for your Looker (Google Cloud core) instance. The instance name is not associated with the instance's URL. You won't be able to rename the instance after it has been created.
  3. In the **OAuth Application Credentials** section, enter the **OAuth client ID** and **OAuth secret** that you created when you [set up your OAuth client](/looker/docs/looker-core-create-oauth#generate_the_oauth_client_id_and_client_secret).
  4. In the **Region** field, select the region that matches your subscription contract, as this is where the [quota for your project](/docs/quotas/view_manage) is allocated. Then click **OK**.
  5. In the **Edition** section, set the instance edition to **Standard**. This edition provides a Looker platform that is best for small organizations or teams with fewer than 50 users. This edition is [billed](/looker/pricing) monthly while the instance is active.
  6. Click **Create**. Looker (Google Cloud core) requires approximately 60 minutes to generate a new instance.

## What's next

This Quickstart covered how to create a **Standard** Looker (Google Cloud core) instance that uses a Public IP network connection and Google-managed encryption and that requires no deferred or denied maintenance windows and no additional users beyond the default number that is provided for a **Standard** edition.

For more information about creating and configuring an instance, see the Looker (Google Cloud core) documentation:

  * [Create a Looker (Google Cloud core) instance](/looker/docs/looker-core-instance-create)
  * [Configure a Looker (Google Cloud core) instance](/looker/docs/looker-core-instance-setup)
  * [Connect to your database](/looker/docs/looker-core-dialects)
  * [Use the sample LookML project on a Looker (Google Cloud core) instance](/looker/docs/looker-core-sample-project)