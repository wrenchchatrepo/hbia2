# https://cloud.google.com/looker/docs/looker-core-psc-access

Depth: 3

**Note:** To use Private Service Connect with Looker (Google Cloud core), the Looker (Google Cloud core) instance must be [enabled to use Private Service Connect](/looker/docs/looker-core-create-psc) during instance creation.

This documentation explains how to use [Private Service Connect](/vpc/docs/private-service-connect) to configure routing from clients to Looker (Google Cloud core), also called [_northbound traffic_](/looker/docs/glossary#northbound-traffic).

## Create a custom domain

The first step after the Looker (Google Cloud core) instance is created is to set up a custom domain and update the OAuth credentials for the instance. The next sections walk you through the process.

When you create a custom domain for private IP (Private Service Connect) instances, the custom domain must meet the following requirements:

  * The custom domain must consist of at least three parts, including at least one subdomain. For example, `subdomain.domain.com`.
  * The custom domain must not contain any of the following: 
    * looker.com
    * google.com
    * googleapis.com
    * gcr.io
    * pkg.dev

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

### Update the OAuth credentials

**Note:** You can use any OAuth client to create authorization credentials for your Looker (Google Cloud core) instance. As an example, these steps walk you through updating the credentials by using the Google Cloud console. If you are using a different client, adjust the steps accordingly.

  1. Access your OAuth client by navigating in the Google Cloud console to **APIs & Services > Credentials** and selecting the OAuth client ID for the OAuth client that is used by your Looker (Google Cloud core) instance.
  2. Click the **Add URI** button to update the **Authorized JavaScript origins** field in your OAuth client to include the same DNS name that your organization will use to access Looker (Google Cloud core). For example, if your custom domain is `looker.examplepetstore.com`, you enter `looker.examplepetstore.com` as the URI.

![](/static/looker/docs/images/core-custom-domain-ajso.png)

  3. [Update or add](/looker/docs/looker-core-create-oauth#add_the_authorized_redirect_uri_to_the_oauth_client) the custom domain to the list of **Authorized redirect URIs** for the [OAuth credentials that you used](/looker/docs/looker-core-create-oauth) when you created the Looker (Google Cloud core) instance. Add `/oauth2callback` to the end of the URI. For example, if your custom domain is `looker.examplepetstore.com`, you enter `looker.examplepetstore.com/oauth2callback`.

![](/static/looker/docs/images/core-custom-domain-aruris.png)

## Access the instance over hybrid networking using an endpoint

**Note:** Alternatively, see the [Looker (Google Cloud core) PSC Northbound Regional External L7 ALB](https://codelabs.developers.google.com/looker-psc-ext-northbound-l7) codelab. In this codelab, you will create an L7 regional application load balancer and Private Service Connect backend to gain northbound access to Looker (Google Cloud core). Northbound access to Looker (Google Cloud core) requires that the Consumer VPC be added to the allowlist for the Looker (Google Cloud core) PSC instance.

After you have set up the custom domain, to access the instance from on-premises or from another cloud provider environment (in other words, through [hybrid networking](/looker/docs/glossary#hybrid_networking)), perform the following steps:

  1. Expose Looker (Google Cloud core) through a Private Service Connect endpoint.
  2. Advertise the endpoint to multi-cloud and on-premises environments.
  3. Set up DNS.

### Networking overview

In a hybrid networking environment, the following network components are required:

  * [Cloud Router](/network-connectivity/docs/router/concepts/overview)
  * [Hybrid networking products](/network-connectivity/docs/how-to/choose-product#google-cloud) such as HA-VPN, Cloud Interconnect, and SD-WAN

In addition, you will need to set up DNS for access.

Private Service Connect allows _consumers_ to access _managed services_ privately from inside their VPC network or over hybrid networking. It allows managed service _producers_ to host these services in their own separate VPC networks and offer a private connection to their consumers. For example, when you use Private Service Connect to access Looker (Google Cloud core), you are the service consumer, and Looker (Google Cloud core) is the service producer.

Looker (Google Cloud core) deployed with Private Service Connect supports [endpoints](/vpc/docs/private-service-connect#endpoints).

An example of a Private Service Connect endpoint network setup is displayed in the following diagram:

![The network architecture for accessing a Looker \(Google Cloud core\) instance from on-premises.](/static/looker/docs/images/psc-endpoint-diagram.png)

In the example, the on-premises environment is connected to a Google Cloud host project through Cloud Interconnect, routing through a Cloud Router to a Private Service Connect endpoint, which connects to a service attachment in a Google-managed producer VPC. A Shared VPC hosts Cloud DNS, for API resolution.

### Required roles

**Role** | **Description**  
---|---  
[Compute Network Admin](/iam/docs/understanding-roles#compute.networkAdmin) `(roles/compute.networkAdmin)` | Grants full control over the VPC network that initiates a connection to a Looker (Google Cloud core) instance.  
[Service Directory Editor](/iam/docs/understanding-roles#servicedirectory.editor) `(roles/servicedirectory.editor)` | Create Private Service Connect endpoints.  
[Looker Admin](/iam/docs/understanding-roles#looker.admin) `(roles/looker.admin)` | Grants full control over Looker (Google Cloud core) resources, including creating an instance that is enabled for Private Service Connect and creating a custom domain.  
[DNS Admin](/iam/docs/understanding-roles#dns.admin) `(roles/dns.admin)` (optional) | Grants full control over Cloud DNS resources, including DNS zones and records.  
  
### Create a Private Service Connect endpoint for Looker (Google Cloud core)

Follow the [instructions for creating a Private Service Connect endpoint within a VPC network](/vpc/docs/configure-private-service-connect-services#create-endpoint). Make sure the network is [allowed ingress](/looker/docs/looker-core-create-psc#update_allowed_vpcs) to your Looker (Google Cloud core) instance, and follow these guidelines:

  * Set the **Target service** field (for the Google Cloud console) or the `SERVICE_ATTACHMENT` variable (if following Google Cloud CLI or API instructions) to the Looker service attachment URI, which you can find by running the following command:
    
        gcloud looker instances describe INSTANCE_NAME --region=REGION--format=json

Replace the following:

    * `INSTANCE_NAME`: the name of your Looker (Google Cloud core) instance.
    * `REGION`: the region in which your Looker (Google Cloud core) instance is hosted.
  * You can use any subnet that is hosted in the same region as the Looker (Google Cloud core) instance.

  * Don't enable global access.

To view the endpoint details after creation, follow the instructions for [viewing endpoint details](/vpc/docs/configure-private-service-connect-services#endpoint-details).

### Advertise the endpoint to multi-cloud and on-premises environments

Use Cloud Router to advertise the Private Service Connect endpoint's IP address to your on-premises network or other environment.

When you're deploying Private Service Connect endpoints, a regular subnet within the consumer Virtual Private Cloud (VPC) is used. This subnet is automatically advertised by the Cloud Router. However, if you are selectively advertising [custom subnets](/network-connectivity/docs/router/how-to/advertising-subnets) through the Cloud Router, make sure to modify the Cloud Router configuration to include the IP address or subnet of the Private Service Connect endpoint.

Make sure that your on-premises (or other environment's) firewall allows outbound traffic to the Private Service Connect endpoint's IP address or subnet while taking into account [hybrid networking considerations](/vpc/docs/configure-private-service-connect-services#on-premises).

### Set up DNS

When setting up DNS, you can use one of the following two options:

  * Update the on-premises DNS to be authoritative for the Looker (Google Cloud core) custom domain that is mapped to the Private Service Connect endpoint IP address.
  * Create a [Cloud DNS private zone](/dns/docs/zones#create-private-zone), [create a record set](/dns/docs/records#create_a_resource_record_set) using the IP address allocated for the Private Service Connect endpoint, and enable [inbound DNS forwarding](/dns/docs/policies#create-in) to allow your VPC to be authoritative for the Looker (Google Cloud core) custom domain that is mapped to the Private Service Connect endpoint IP address.

## What's next

  * [Connect Looker (Google Cloud core) to your database](/looker/docs/looker-core-dialects)
  * [Prepare a Looker (Google Cloud core) instance for users](/looker/docs/looker-core-instance-setup)
  * [Manage users within Looker (Google Cloud core)](/looker/docs/looker-core-user-management)