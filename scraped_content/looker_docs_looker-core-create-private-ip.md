# https://cloud.google.com/looker/docs/looker-core-create-private-ip

Depth: 3

**Note:** For instructions on how to create a public IP instance, see the [Create a public IP Looker (Google Cloud core) instance](/looker/docs/looker-core-instance-create) documentation page. For instructions on how to create a Looker (Google Cloud core) Private Service Connect instance, see the [Create a Looker (Google Cloud core) Private Service Connect instance](/looker/docs/looker-core-create-psc) documentation page.

This page explains how to create a private IP Looker (Google Cloud core) production or [non-production instance](/looker/docs/looker-core-overview#staging_environments_and_testing) that uses [private services access](/looker/docs/looker-core-networking-options#psa).

[Private IP connections](/looker/docs/looker-core-networking-options#private_ip_connections) make services reachable without going through the internet or using external IP addresses. Because they don't traverse the internet, connections over private IP typically provide lower latency and limited attack vectors. Private IP connections allow your Looker (Google Cloud core) instance to communicate with other resources in your Virtual Private Cloud (VPC) but don't allow inbound communication from the public internet.

Private IP connectivity enables the use of some features, such as [VPC Service Controls](/looker/docs/looker-core-vpcsc). However, private IP connections aren't compatible with some Looker (Google Cloud core) features. See the [feature compatibility](/looker/docs/looker-core-feature-differences#feature_compatibility_by_network_connection_type) table for more information.

Looker (Google Cloud core) supports private IP for **Enterprise** or **Embed** [instance editions](/looker/docs/looker-core-overview#editions).

## Required roles and permissions

To set up a private IP instance, you must have the following IAM permissions:

  1. To create a Looker (Google Cloud core) instance, you must have the [Looker Admin](/iam/docs/understanding-roles#looker.admin) (`roles/looker.Admin`) role.
  2. To get the permissions that you need to create allocated IP address ranges and manage private connections, ask your administrator to grant you the [Compute Network Admin ](https://cloud.google.com/iam/docs/understanding-roles#compute.networkAdmin) (`roles/compute.networkAdmin`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to create allocated IP address ranges and manage private connections. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create allocated IP address ranges and manage private connections:

     * See available networks in the **Network** drop-down: 
       * ` compute.addresses.list `
       * ` compute.globalAddresses.list `
       * ` compute.networks.list `
       * ` compute.globalAddresses.list `
     * Create a new VPC network: 
       * ` compute.addresses.create `
       * ` compute.globalAddresses.create `
       * ` serviceusage.services.enable `
     * Allocate a private IP range and set up a private services access connection: ` compute.networks.addPeering`

You might also be able to get these permissions with [custom roles](/iam/docs/creating-custom-roles) or other [predefined roles](/iam/docs/understanding-roles). 

**Note:** [IAM basic roles](/iam/docs/understanding-roles#basic) might also contain permissions to create allocated IP address ranges and manage private connections. You shouldn't grant basic roles in a production environment, but you can grant them in a development or test environment. 

If you are creating a private IP instance with Terraform or the Google Cloud CLI and are using a private network that has already been set up, you don't need these permissions.

You may also need additional IAM roles to set up VPC Service Controls or customer-managed encryption keys (CMEK). Learn more by visiting the [VPC Service Controls support for Looker (Google Cloud core)](/looker/docs/looker-core-vpcsc) or the [Enable CMEK for Looker (Google Cloud core)](/looker/docs/looker-core-cmek) documentation pages for those features.

## Before you begin

  1. In the Google Cloud console, on the project selector page, [create a Google Cloud project](/resource-manager/docs/creating-managing-projects) or navigate to an existing one in which you want to create the Looker (Google Cloud core) instance. 

[ Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. [Enable the Looker API](/apis/docs/getting-started#enabling_apis) for your project in the Google Cloud console. When enabling the API, you may need to refresh the console page to confirm that the API has been enabled. 

[ Enable the API](https://console.cloud.google.com/flows/enableapi?apiid=looker.googleapis.com)

**Caution:** Disabling the Looker API after instance creation will affect Looker (Google Cloud core) features. For example, disabling the API will disable the ability to create [instance backups](/looker/docs/looker-core-backup-restore).
  3. Enable the [Service Networking API](/service-infrastructure/docs/service-networking/getting-started) for your project in the Google Cloud console. When enabling the API, you may need to refresh the console page to confirm that the API has been enabled. 

[ Enable the API](https://console.cloud.google.com/flows/enableapi?apiid=servicenetworking.googleapis.com)

  4. Enable the [Compute Engine API](/apis/docs/getting-started#enabling_apis) for your project in the Google Cloud console. When you enable the API, you may need to refresh the console page to confirm that the API has been enabled. 

[ Enable the API](https://console.cloud.google.com/flows/enableapi?apiid=compute.googleapis.com)

  5. [Set up an OAuth client and create authorization credentials](/looker/docs/looker-core-create-oauth). The OAuth client lets you authenticate and access the instance. You must set up OAuth to create a Looker (Google Cloud core) instance, even if you are using a different [authentication method](/looker/docs/looker-core-user-authentication) to authenticate users into your instance.

## Create and configure a VPC network

**Important:** If you are creating a Looker (Google Cloud core) instance in a [Shared VPC](/vpc/docs/shared-vpc), follow the steps in the Creating an instance in a Shared VPC section.

Before you can create a private IP connection, you must first create and configure a Virtual Private Cloud (VPC) network. Looker (Google Cloud core) supports multiple private IP instances in the same VPC, either in the same region or in different regions.

  1. [Create a VPC network](/vpc/docs/create-modify-vpc-networks) in your project. Alternatively, if you are using a [Shared VPC](/vpc/docs/shared-vpc) instead of creating a new VPC network, complete the steps in the following section, Creating an instance in a Shared VPC, in addition to completing the remaining steps in this section for the Shared VPC.
  2. [Allocate an IPv4 IP range (CIDR block)](/vpc/docs/configure-private-services-access#procedure) in your VPC for a private services access connection to Looker (Google Cloud core).
     * Before allocating your range, consider the [constraints](/vpc/docs/configure-private-services-access#considerations).
     * When [setting the IP address range size](/vpc/docs/configure-private-services-access#ip_address_range_size), be aware that the minimum size is a `/22` block.
     * Looker (Google Cloud core) supports all IPv4 ranges within [RFC 1918](https://datatracker.ietf.org/doc/html/rfc1918), which specifies IP addresses that are assigned to be used internally (that is, within an organization) and won't route on the Internet. Specifically, these are the following:
       * `10.0.0.0/8`
       * `172.16.0.0/12`
       * `192.168.0.0/16`
     * Class E IPv4 ranges (`240.0.0.0/4`) are reserved for future use as noted in [RFC 5735](https://datatracker.ietf.org/doc/html/rfc5735) and [RFC 1112](https://datatracker.ietf.org/doc/html/rfc1112) and aren't supported for Looker (Google Cloud core).
**Note:** In addition to Class E IPv4 ranges, some other IPv4 ranges outside of RFC 1918 may not be supported by Looker (Google Cloud core) or its dependencies. If you want to use a range outside of RFC 1918, you may want to test it first. When a Looker (Google Cloud core) instance is created for the first time in a region within a VPC, Looker creates a [proxy-only subnet](/load-balancing/docs/proxy-only-subnets). The proxy-only subnet uses a `/26` range subnet of the `/22` subnet that you reserve when you create the Looker (Google Cloud core) instance. Any subsequent private IP Looker (Google Cloud core) instances in the same VPC and in the same region use the same proxy-only subnet. 
  3. Add the [private services access connection](/vpc/docs/configure-private-services-access#creating-connection) to your VPC network using the IP range allocated in the previous step for the **Assigned allocation**.
  4. Once your VPC network is created, return to the **Create Looker instance** page in your Google Cloud project. You may need to refresh the page so that your VPC network is recognized.

Once you have completed these steps, you can begin to create your instance by following the steps on the [Create a Looker (Google Cloud core) instance ](/looker/docs/looker-core-instance-create) documentation page, starting with the [Before you begin](/looker/docs/looker-core-instance-create#before_you_begin) section.

### Multiple private IP instances in the same VPC

If two or more private IP Looker (Google Cloud core) instances are located in the same region and in the same VPC, and you delete the first Looker (Google Cloud core) instance that was created in the region, the proxy-only subnet is not released because it is still in use by the remaining instances. If you attempt to create a new private IP Looker (Google Cloud core) instance that uses the same address range that you used for the deleted instance (which contains the proxy-only subnet's IP address range), instance creation will fail, and you will see an "IP ranges exhausted" error. To check if an IP range is in use, check VPC peering for Service Networking, and check the import routes to see if they're using the IP range that you are interested in.

### Create an instance in a Shared VPC

If you are creating a Looker (Google Cloud core) instance in a [Shared VPC](/vpc/docs/shared-vpc), complete the following steps in the Shared VPC's host project:

  1. [Enable the Looker API](/apis/docs/getting-started#enabling_apis) in the Shared VPC's host project in the Google Cloud console. When you enable the API, you may need to refresh the console page to confirm that the API has been enabled. 

[ Enable the API](https://console.cloud.google.com/flows/enableapi?apiid=looker.googleapis.com)

  2. Create a [service account](/compute/docs/access/service-accounts) in the Shared VPC's host project, using the gcloud [`services identity create` command](/sdk/gcloud/reference/beta/services/identity/create):
    
        gcloud beta services identity create --service=looker.googleapis.com --project=SHARED_HOST_PROJECT_ID
    

Replace SHARED_HOST_PROJECT_ID with the Shared VPC's host project.

  3. [Grant](/compute/docs/access/service-accounts#usingroles) the [`compute.globalAddresses.get`](/iam/docs/permissions-reference) IAM permission to the service account in the host project.

After creating the service account and granting it the IAM permission, wait a few minutes for the service account and permission to propagate.

In addition, allocate an IPv4 IP range in the Shared VPC and add the private services access connection to the Shared VPC as described in the previous section, Create and configure a VPC network.

**Note:** If you are using VPC Service Controls, and the Shared VPC host project and the Looker (Google Cloud core) service project are in different VPC Service Controls perimeters, you must create a [VPC Service Controls perimeter bridge](/vpc-service-controls/docs/create-perimeter-bridges) between the two perimeters to allow instance creation.

## Create the private IP instance

> Looker (Google Cloud core) requires approximately 60 minutes to generate a new instance.

**Important:** If you want to use customer-managed encryption keys (CMEK) with the Looker (Google Cloud core) instance that you are creating, see the [Enable CMEK for Looker (Google Cloud core)](/looker/docs/looker-core-cmek) documentation page for information on the additional setup that's required prior to instance creation.

Private IP must be assigned at the time of instance creation. Private IP cannot be added to or removed from an instance after the instance is created.

To configure private IP during instance creation, select one of the following options:

### console

  1. Navigate to the Looker (Google Cloud core) product page from your project in the Google Cloud console. If you have already created a Looker (Google Cloud core) instance within this project, this will open the **Instances** page. 

[Go to Looker (Google Cloud core)](https://console.cloud.google.com/looker)

  2. Click **CREATE INSTANCE**.
  3. In the **Instance name** section, provide a name for your Looker (Google Cloud core) instance. The instance name isn't associated with the URL of the Looker (Google Cloud core) instance once it is created. The instance name cannot be changed after instance creation.
  4. In the **OAuth Application Credentials** section, enter the OAuth client ID and OAuth secret that you created when you [set up your OAuth client](/looker/docs/looker-core-create-oauth#generate_the_oauth_client_id_and_client_secret).
  5. In the **Region** section, select the appropriate option from the drop-down menu to host your Looker (Google Cloud core) instance. Select the region that matches the region in the subscription contract, which is where the [quota for your project](/docs/quota_detail/view_manage) is allocated. Available regions are listed on the [Looker (Google Cloud core) locations](/looker/docs/looker-core-locations) documentation page.

You cannot change the region once the instance has been created.

  6. In the **Edition** section, choose an **Enterprise** or **Embed** edition option, for a production or [non-production instance](/looker/docs/looker-core-overview#staging_environments_and_testing) type. The edition type affects some of the [features that are available](/looker/docs/looker-core-edition-types) for the instance. Make sure that you choose the same edition type as listed in your [annual contract](/looker/pricing) and that you have [quota](/docs/quotas/view-manage) allocated for that edition type.

     * **Enterprise** : Looker (Google Cloud core) platform with enhanced security features for addressing a wide variety of internal BI and analytics use cases
     * **Embed** : Looker (Google Cloud core) platform for deploying and maintaining reliable external analytics and custom applications at scale

Editions cannot be changed after instance creation. If you want to change an edition, you can use [import and export](/looker/docs/looker-core-import-export) to move your Looker (Google Cloud core) instance data into a new instance that is configured with a different edition.

  7. In the **Customize your instance** section, click **SHOW CONFIGURATION OPTIONS** to display a group of additional settings that you can customize for the instance.

  8. In the **Connections** section, under **Instance IP assignment** , choose either **Private IP** only or both **Private IP** and **Public IP**. The type of network connection selected impacts the [Looker features available](/looker/docs/looker-core-feature-differences#feature_compatibility_by_edition_type) to the instance. The following network connection options are available:

     * **Public IP** : Assigns an external, internet-accessible IP address.
     * **Private IP** : Assigns an internal, Google-hosted IP address that is accessible on a [Virtual Private Cloud (VPC)](/vpc/docs/overview). You can use this address to connect from other resources with access to the VPC. Only **Enterprise** and **Embed** editions support private IP. If you want to use VPC Service Controls, you must select **Private IP** only.
**Note:** Private IP must be assigned at the time of instance creation. Private IP cannot be added to or removed from an instance after the instance is created. If both public IP and private IP are assigned at the time of instance creation, the public IP option can be [disabled later](/looker/docs/looker-core-view-console#editing_settings).
     * If both **Private IP** and **Public IP** are selected, incoming traffic will be routed through public IP and outgoing traffic will be routed through private IP. The Looker (Google Cloud core) instance won't use the public IP to originate internet outbound traffic.
  9. Under **Private IP Type** , select **Private Services Access (PSA)**.

  10. If an **Enable Required APIs** pop-up is displayed, you must enable additional APIs for your Google Cloud project. To enable the required APIs for a private network connection, click **ENABLE ALL**.

  11. In the **Network** drop-down, select your VPC network. Private IP networks require a [private services access connection](/vpc/docs/configure-private-services-access#creating-connection), which enables your services to communicate exclusively by using internal IP addresses. See the [Configure private services access](/vpc/docs/configure-private-services-access) documentation page for more information about setting up a private IP connection. If you did not set up a private services connection when you created your VPC network, you can click **SET UP CONNECTION** under the message **Private services access connection required**. This opens a side panel where you can allocate an IP range and create a connection.

  12. Under **Allocated IP range** , select the IP range within the VPC in which Google will provision a subnetwork for your Looker (Google Cloud core) instance. Subnetworks reserve an IP range that cannot be used by other resources in the VPC network. You won't be able to modify this IP range after you create the Looker (Google Cloud core) instance. IP range allocation includes these options:

     * Select **Use automatically assigned IP range** to have Google allocate an IP range automatically to provision a subnetwork for the VPC.
     * Select an IP range that was defined during the private services access setup.
  13. In the **Encryption** section, you can select the type of encryption to use on your instance. The following encryption options are available:

     * [**Google-managed encryption key**](/security/encryption-at-rest/default-encryption): This option is the default and doesn't require any additional configuration.
     * [**Customer-managed encryption key (CMEK)**](/kms/docs/cmek): See the [Using customer-managed encryption keys with Looker (Google Cloud core)](/looker/docs/looker-core-cmek#create_a_instance_with_cmek) documentation page for more information on CMEK and how to configure it during instance creation. The type of encryption cannot be changed after instance creation.
     * **Enable[FIPS 140-2 Validated Encryption](https://csrc.nist.gov/pubs/fips/140-2/upd2/final)**: See the [Enable FIPS 140-2 level 1 compliance on a Looker (Google Cloud core) instance](/looker/docs/looker-core-fips-mode) documentation page for more information on FIPS 140-2 support on Looker (Google Cloud core).
  14. In the **Maintenance Window** section, you can optionally [specify the day of the week and the hour](/looker/docs/looker-core-maintenance#set_a_preferred_window_for_maintenance) in which Looker (Google Cloud core) schedules maintenance. Maintenance windows last for one hour. By default, the **Preferred Window** option in the **Maintenance Window** is set to **Any window**.

  15. In the **Deny Maintenance Period** section, you can optionally [specify a block of days](/looker/docs/looker-core-maintenance#define_a_maintenance_deny_period_to_defer_maintenance) in which Looker (Google Cloud core) doesn't schedule maintenance. Deny maintenance periods can be up to 60 days long. You must allow at least 14 days of maintenance availability between any 2 deny maintenance periods.

  16. In the **Gemini in Looker** section, you can optionally make [Gemini in Looker features](/looker/docs/looker-core-admin-gemini#gemini-feature-availability) available for the Looker (Google Cloud core) instance. To enable Gemini in Looker, select **Gemini** , and then select **Trusted Tester features**. When **Trusted Tester features** is enabled, users can access the Trusted Tester capabilities of Gemini in Looker. You may request access to the non-public Trusted Tester capabilities through the [Gemini in Looker preview form](https://docs.google.com/forms/d/e/1FAIpQLSefBWbxchQFyZB9EOOcRxYTRi-16TezwRExW-x-XJRfeklCiA/viewform) on a per-user basis. You must enable this setting to use Gemini during the pre-GA preview. Optionally, select **Trusted Tester data use**. When this setting is enabled, you consent to your data being used by Google as described in the [Gemini for Google Cloud Trusted Tester Program terms](/trusted-tester/gemini-for-google-cloud-preview). To disable Gemini for a Looker (Google Cloud core) instance, clear the **Gemini** setting.

  17. Click **Create**.

###  gcloud 

  1. If you are using [CMEK](/looker/docs/looker-core-cmek), then follow the instructions for creating a service account, key ring, and key before creating your Looker (Google Cloud core) instance.
  2. Use the `gcloud looker instances create` command to create the instance:
    
        gcloud looker instances create INSTANCE_NAME \
    --project=PROJECT_ID \
    --oauth-client-id=OAUTH_CLIENT_ID \
    --oauth-client-secret=OAUTH_CLIENT_SECRET \
    --region=REGION \
    --edition=EDITION \
    --private-ip-enabled \
    --consumer-network=CONSUMER_NETWORK --reserved-range=RESERVED_RANGE
    [--no-public-ip-enabled]
    [--public-ip-enabled]
    

Replace the following:

     * `INSTANCE_NAME`: a name for your Looker (Google Cloud core) instance; it isn't associated with the instance URL.
     * `PROJECT_ID`: the name of the Google Cloud project in which you are creating the Looker (Google Cloud core) instance.
     * `OAUTH_CLIENT_ID` and `OAUTH_CLIENT_SECRET`: the OAuth client ID and OAuth secret that you created when you [set up your OAuth client](/looker/docs/looker-core-create-oauth#generate_the_oauth_client_id_and_client_secret). After the instance has been created, [enter the instance's URL in the **Authorized redirect URIs** section of the OAuth client](/looker/docs/looker-core-create-oauth#add_the_authorized_redirect_uri_to_the_oauth_client).
     * `REGION`: the region in which your Looker (Google Cloud core) instance is hosted. Select the region that matches the region in the subscription contract. Available regions are listed on the [Looker (Google Cloud core) locations](/looker/docs/looker-core-locations) documentation page.
     * `EDITION`: the edition and environment type (production or [non-production](/looker/docs/looker-core-overview#staging_environments_and_testing)) for the instance. For a private IP instance, this should be `core-enterprise-annual`, `core-embed-annual`, `nonprod-core-enterprise-annual`, or `nonprod-core-embed-annual`. Make sure that you choose the same edition type as listed in your [annual contract](/looker/pricing) and that you have [quota](/docs/quotas/view-manage) allocated. Editions cannot be changed after instance creation. If you want to change an edition, you can use [import and export](/looker/docs/looker-core-import-export) to move your Looker (Google Cloud core) instance data into a new instance that is configured with a different edition.
     * `CONSUMER_NETWORK`: [your VPC network or Shared VPC](/looker/docs/looker-core-create-private-ip#create-vpc) network. Must be set if you're creating a private IP instance.
     * `RESERVED_RANGE`: the range of IP addresses within the VPC in which Google will provision a subnetwork for your Looker (Google Cloud core) instance.

You may include the following flags:

     * `--private-ip-enabled` enables private IP. This must be included to create a private IP instance.
     * `--public-ip-enabled` enables public IP.
     * `--no-public-ip-enabled` disables public IP.
     * `--async` is recommended when you're creating a Looker (Google Cloud core) instance.
  3. You can add more parameters to apply other instance settings: 
    
        [--maintenance-window-day=MAINTENANCE_WINDOW_DAY
          --maintenance-window-time=MAINTENANCE_WINDOW_TIME]
    [--deny-maintenance-period-end-date=DENY_MAINTENANCE_PERIOD_END_DATE
          --deny-maintenance-period-start-date=DENY_MAINTENANCE_PERIOD_START_DATE
          --deny-maintenance-period-time=DENY_MAINTENANCE_PERIOD_TIME]
    [--kms-key=KMS_KEY_ID]
    [--fips-enabled]
    

Replace the following:

     * `MAINTENANCE_WINDOW_DAY`: must be one of the following: `friday`, `monday`, `saturday`, `sunday`, `thursday`, `tuesday`, `wednesday`. See the [Manage maintenance policies for Looker (Google Cloud core)](/looker/docs/looker-core-maintenance#maintenance_settings) documentation page for more information about maintenance window settings.
     * `MAINTENANCE_WINDOW_TIME` and `DENY_MAINTENANCE_PERIOD_TIME`: must be in UTC time in 24-hour format (for example, 13:00, 17:45).
     * `DENY_MAINTENANCE_PERIOD_START_DATE` and `DENY_MAINTENANCE_PERIOD_END_DATE`: must be in the format `YYYY-MM-DD`.
     * `KMS_KEY_ID`: must be the key that is created when setting up [customer-managed encryption keys (CMEK)](/looker/docs/looker-core-cmek#copy_or_write_down_the_kms_key_id_and_the_kms_keyring_id).

You may include the `--fips-enabled` flag to [enable FIPS 140-2 level 1 compliance](/looker/docs/looker-core-fips-mode).

**Note:** If you create a private IP instance using Terraform, the network name must follow the format: `projects/<project>/global/networks/<network>`.

As the instance is being created, you can view its status on the [**Instances**](/looker/docs/looker-core-view-console) page within the console. You can also see your instance creation activity by clicking on the notifications icon in the Google Cloud console menu.

If you create a private IP only instance, a URL **won't** appear on the **Instances** page. See the following Accessing a private IP instance after creation section for more information about how to set up access to your private IP instance.

## Access a private IP instance after creation

If you create an instance that is enabled only for private IP, you will **not** receive a URL for the instance. To access the instance, you must configure a custom domain for the instance and add that custom domain to the instance's OAuth credentials. To understand the different private IP networking options for setting up and accessing a custom domain, visit the [Custom domain networking options for Looker (Google Cloud core) private IP instances](/looker/docs/looker-core-custom-domain-private-ip-overview) documentation page.

## What's next

  * [Custom domain networking options for Looker (Google Cloud core) private IP instances](/looker/docs/looker-core-custom-domain-private-ip-overview)