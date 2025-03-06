# https://cloud.google.com/looker/docs/looker-core-create-psc

Depth: 3

**Note:** For instructions on how to create a public IP instance, see the [Create a public IP Looker (Google Cloud core) instance](/looker/docs/looker-core-instance-create) documentation page. For instructions on how to create a Looker (Google Cloud core) instance that is enabled for private services access, see the [Create a private IP Looker (Google Cloud core) instance](/looker/docs/looker-core-create-private-ip) documentation page.

This page describes the process for using the [gcloud CLI](/sdk/docs/install) to create a Looker (Google Cloud core) production or [non-production instance](/looker/docs/looker-core-overview#staging_environments_and_testing) with [Private Service Connect](/vpc/docs/private-service-connect) enabled.

Private Service Connect can be enabled for a Looker (Google Cloud core) instance that meets the following criteria:

  * The Looker (Google Cloud core) instance must be new. Private Service Connect can be enabled only at the time of instance creation.
  * The instance cannot have public IP enabled.
  * The [instance edition](/looker/docs/looker-core-overview#looker_\(google_cloud_core\)_editions) must be Enterprise (`core-enterprise-annual`) or Embed (`core-embed-annual`).

## Before you begin

  1. In the Google Cloud console, on the project selector page, select the project where you want to create the Private Service Connect instance. 

[ Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. [Enable the Looker API](/apis/docs/getting-started#enabling_apis) for your project in the Google Cloud console. When enabling the API, you may need to refresh the console page to confirm that the API has been enabled. 

[ Enable the API](https://console.cloud.google.com/flows/enableapi?apiid=looker.googleapis.com)

**Caution:** Disabling the Looker API after instance creation will affect Looker (Google Cloud core) features. For example, disabling the API will disable the ability to create [instance backups](/looker/docs/looker-core-backup-restore).
  3. [Set up an OAuth client and create authorization credentials](/looker/docs/looker-core-create-oauth). The OAuth client lets you authenticate and access the instance. You must set up OAuth to create a Looker (Google Cloud core) instance, even if you are using a different [authentication method](/looker/docs/looker-core-user-authentication) to authenticate users into your instance.
  4. If you want to use [VPC Service Controls](/looker/docs/looker-core-vpcsc) or [customer-managed encryption keys (CMEK)](/looker/docs/looker-core-cmek) with the Looker (Google Cloud core) instance that you are creating, additional setup is required prior to instance creation. Additional edition and network configuration may also be required during instance creation.

**Important:** Once Private Service Connect is enabled on a Looker (Google Cloud core) instance, you cannot switch that instance to use public IP or [private IP (private services access) connectivity](/looker/docs/looker-core-create-private-ip).

### Required roles

To get the permissions that you need to create a Looker (Google Cloud core) instance, ask your administrator to grant you the [Looker Admin ](https://cloud.google.com/iam/docs/understanding-roles#looker.admin) (`roles/looker.admin`) IAM role on the project the instance will reside in. For more information about granting roles, see [Manage access to projects, folders, and organizations](/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](/iam/docs/creating-custom-roles) or other [predefined roles](/iam/docs/understanding-roles). 

**Note:** [IAM basic roles](/iam/docs/understanding-roles#basic) might also contain permissions to create a Looker (Google Cloud core) instance. You shouldn't grant basic roles in a production environment, but you can grant them in a development or test environment. 

You may also need additional IAM roles to set up [VPC Service Controls](/looker/docs/looker-core-vpcsc) or [customer-managed encryption keys (CMEK)](/looker/docs/looker-core-cmek). Visit the documentation pages for those features to learn more.

## Create a Private Service Connect instance

### console

  1. Navigate to the Looker (Google Cloud core) product page from your project in the Google Cloud console. If you have already created a Looker (Google Cloud core) instance within this project, the **Instances** page will open. 

[Go to Looker (Google Cloud core)](https://console.cloud.google.com/looker)

  2. Click **CREATE INSTANCE**.
  3. In the **Instance name** section, provide a name for your Looker (Google Cloud core) instance. The instance name isn't associated with the URL of the Looker (Google Cloud core) instance once it is created. The instance name cannot be changed after instance creation.
  4. In the **OAuth Application Credentials** section, enter the OAuth client ID and OAuth secret that you created when you [set up your OAuth client](/looker/docs/looker-core-create-oauth#generate_the_oauth_client_id_and_client_secret).
  5. In the **Region** section, select the appropriate option from the drop-down menu to host your Looker (Google Cloud core) instance. Select the region that matches the region in the subscription contract, which is where the [quota for your project](/docs/quota_detail/view_manage) is allocated. Available regions are listed on the [Looker (Google Cloud core) locations](/looker/docs/looker-core-locations) documentation page.

You cannot change the region once the instance has been created.

  6. In the **Edition** section, choose an **Enterprise** or **Embed** edition option for a production or [non-production instance](/looker/docs/looker-core-overview#staging_environments_and_testing) type. The edition type affects some of the [features that are available](/looker/docs/looker-core-edition-types) for the instance. Make sure that you choose the same edition type as listed in your [annual contract](/looker/pricing) and that you have [quota](/docs/quotas/view-manage) allocated for that edition type.

     * **Enterprise** : Looker (Google Cloud core) platform with enhanced security features for addressing a wide variety of internal BI and analytics use cases
     * **Embed** : Looker (Google Cloud core) platform for deploying and maintaining reliable external analytics and custom applications at scale

Editions cannot be changed after instance creation. If you want to change an edition, you can use [import and export](/looker/docs/looker-core-import-export) to move your Looker (Google Cloud core) instance data into a new instance that is configured with a different edition.

  7. In the **Customize your instance** section, click **SHOW CONFIGURATION OPTIONS** to display a group of additional settings that you can customize for the instance.

  8. In the **Connections** section, under **Instance IP assignment** , select only **Private IP**. The type of network connection that you select impacts the [Looker features available](/looker/docs/looker-core-feature-differences#feature_compatibility_by_edition_type) to the instance.

**Note:** Private IP must be assigned at the time of instance creation. Private IP cannot be added to or removed from an instance after the instance is created.
  9. Under **Private IP Type** , select **Private Service Connect (PSC)**.

  10. Under **Allowed VPCs** , click **Add Item** to add the VPCs that will be allowed [northbound access](/looker/docs/looker-core-psc-overview#psc-access) into the Looker (Google Cloud core) instance. In the **Project** field, select the project in which the network was created. In the **Network** drop-down menu, select the network. Add additional VPCs by clicking **Add Item** as needed.

  11. In the **Encryption** section, you can select the type of encryption to use on your instance. The following encryption options are available:

     * [**Google-managed encryption key**](/security/encryption-at-rest/default-encryption): This option is the default and doesn't require any additional configuration.
     * [**Customer-managed encryption key (CMEK)**](/kms/docs/cmek): See the [Using customer-managed encryption keys with Looker (Google Cloud core)](/looker/docs/looker-core-cmek#create_a_instance_with_cmek) documentation page for more information on CMEK and how to configure it during instance creation. The type of encryption cannot be changed after instance creation.
     * **Enable[FIPS 140-2 Validated Encryption](https://csrc.nist.gov/pubs/fips/140-2/upd2/final)**: See the [Enable FIPS 140-2 level 1 compliance on a Looker (Google Cloud core) instance](/looker/docs/looker-core-fips-mode) documentation page for more information on FIPS 140-2 support on Looker (Google Cloud core).
  12. In the **Maintenance Window** section, you can optionally [specify the day of the week and the hour](/looker/docs/looker-core-maintenance#set_a_preferred_window_for_maintenance) in which Looker (Google Cloud core) schedules maintenance. Maintenance windows last for one hour. By default, the **Preferred Window** option in the **Maintenance Window** is set to **Any window**.

  13. In the **Deny Maintenance Period** section, you can optionally [specify a block of days](/looker/docs/looker-core-maintenance#define_a_maintenance_deny_period_to_defer_maintenance) on which Looker (Google Cloud core) doesn't schedule maintenance. Deny maintenance periods can be up to 60 days long. You must allow at least 14 days of maintenance availability between any 2 deny maintenance periods.

  14. In the **Gemini in Looker** section, you can optionally make [Gemini in Looker features](/looker/docs/looker-core-admin-gemini#gemini-feature-availability) available for the Looker (Google Cloud core) instance. To enable Gemini in Looker, select **Gemini** , and then select **Trusted Tester features**. When **Trusted Tester features** is enabled, users can access the Trusted Tester capabilities of Gemini in Looker. You may request access to the non-public Trusted Tester capabilities through the [Gemini in Looker preview form](https://docs.google.com/forms/d/e/1FAIpQLSefBWbxchQFyZB9EOOcRxYTRi-16TezwRExW-x-XJRfeklCiA/viewform) on a per-user basis. You must enable this setting to use Gemini during the pre-GA preview. Optionally, select **Trusted Tester data use**. When this setting is enabled, you consent to your data being used by Google as described in the [Gemini for Google Cloud Trusted Tester Program terms](/trusted-tester/gemini-for-google-cloud-preview). To disable Gemini for a Looker (Google Cloud core) instance, clear the **Gemini** setting.

  15. Click **Create**.

### gcloud

To create a Private Service Connect instance, run the `gcloud looker instances create` command with all the following flags:
    
    
    
    gcloud looker instances create INSTANCE_NAME \
    --no-public-ip-enabled \
    --psc-enabled \
    --oauth-client-id=OAUTH_CLIENT_ID \
    --oauth-client-secret=OAUTH_CLIENT_SECRET \
    --region=REGION \
    --edition=EDITION \
    --psc-allowed-vpcs=ALLOWED_VPC,ADDITIONAL_ALLOWED_VPCS \
    --async
    
    

Replace the following:

  * `INSTANCE_NAME`: a name for your Looker (Google Cloud core) instance; it is not associated with the instance URL.
  * `OAUTH_CLIENT_ID` and `OAUTH_CLIENT_SECRET`: the OAuth client ID and OAuth secret that you created when you [set up your OAuth client](/looker/docs/looker-core-create-oauth#generate_the_oauth_client_id_and_client_secret). After the instance has been created, [enter the instance's URL in the **Authorized redirect URIs** section of the OAuth client](/looker/docs/looker-core-create-oauth#add_the_authorized_redirect_uri_to_the_oauth_client).
  * `REGION`: the region in which your Looker (Google Cloud core) instance is hosted. Select the region that matches the region in the subscription contract. Available regions are listed on the [Looker (Google Cloud core) locations](/looker/docs/looker-core-locations) documentation page.
  * `EDITION`: the edition and environment type (production or [non-production](/looker/docs/looker-core-overview#staging_environments_and_testing)) for the instance. Its possible values are `core-enterprise-annual`, `core-embed-annual`, `nonprod-core-enterprise-annual`, or `nonprod-core-embed-annual`. Editions cannot be changed after instance creation. If you want to change an edition, you can use [import and export](/looker/docs/looker-core-import-export) to move your Looker (Google Cloud core) instance data into a new instance that is configured with a different edition.
  * `ALLOWED_VPC`: a VPC that will be allowed [northbound](/looker/docs/glossary#northbound-traffic) (ingress) access into Looker (Google Cloud core). To access the instance from outside the VPC that the instance is located in, you must list at least one VPC. Specify a VPC using one of the following formats: 
    * `projects/{project}/global/networks/{network}`
    * `https://www.googleapis.com/compute/v1/projects/{project}/global/networks/{network}`
  * `ADDITIONAL_ALLOWED_VPCS`: any additional VPCs to be allowed northbound access into Looker (Google Cloud core) can be added to the `--psc-allowed-vpcs` flag in a comma-separated list.

**Note:** Don't specify [southbound](/looker/docs/glossary#southbound-traffic) (egress) connections in the `create` command. Southbound connections must be specified after the instance has been created.

If you want, you can add more parameters to apply other instance settings: 
    
    
      [--maintenance-window-day=MAINTENANCE_WINDOW_DAY
              --maintenance-window-time=MAINTENANCE_WINDOW_TIME]
      [--deny-maintenance-period-end-date=DENY_MAINTENANCE_PERIOD_END_DATE
              --deny-maintenance-period-start-date=DENY_MAINTENANCE_PERIOD_START_DATE
              --deny-maintenance-period-time=DENY_MAINTENANCE_PERIOD_TIME]
      --kms-key=KMS_KEY_ID
      [--fips-enabled]
      

Replace the following:

  * `MAINTENANCE_WINDOW_DAY`: must be one of the following: `friday`, `monday`, `saturday`, `sunday`, `thursday`, `tuesday`, `wednesday`. See the [Manage maintenance policies for Looker (Google Cloud core)](/looker/docs/looker-core-maintenance#maintenance_settings) documentation page for more information about maintenance window settings.
  * `MAINTENANCE_WINDOW_TIME` and `DENY_MAINTENANCE_PERIOD_TIME`: must be in UTC in 24-hour format (for example, 13:00, 17:45).
  * `DENY_MAINTENANCE_PERIOD_START_DATE` and `DENY_MAINTENANCE_PERIOD_END_DATE`: must be in the format `YYYY-MM-DD`.
  * `KMS_KEY_ID`: must be the key that is created when setting up [customer-managed encryption keys (CMEK)](/looker/docs/looker-core-cmek#copy_or_write_down_the_kms_key_id_and_the_kms_keyring_id).

You may include the `--fips-enabled` flag to [enable FIPS 140-2 level 1 compliance](/looker/docs/looker-core-fips-mode).

The process for creating a Private Service Connect instance differs from the process for creating a Looker (Google Cloud core) (private services access) instance in the following ways:

  * With Private Service Connect setup, the `--consumer-network` and `--reserved-range` flags are not necessary.
  * Private Service Connect instances require two additional flags: `--no-public-ip-enabled` and `--psc-enabled`.
  * The `--psc-allowed-vpcs` flag is a comma-separated list of VPCs. You can specify as many VPCs as you like in the list.

### Check the status of the instance

It takes approximately 40-60 minutes for the instance to be created.

### console

As the instance is being created, you can view its status on the [**Instances**](/looker/docs/looker-core-view-console) page within the console. You can also see your instance creation activity by clicking on the notifications icon in the Google Cloud console menu. On the **Details** page for the instance, its status will show **Active** once it's created.

### gcloud

To check the status, use the `gcloud looker instances describe` command:
    
    
    gcloud looker instances describe INSTANCE_NAME --region=REGION
    

Replace the following:

  * `INSTANCE_NAME`: the name of your Looker (Google Cloud core) instance.
  * `REGION`: the region in which your Looker (Google Cloud core) instance is hosted.

The instance is ready once it reaches the `ACTIVE` state.

**Important:** When you create a Private Service Connect instance, you **will not receive a URL** for the instance. You must set up a [custom domain](/looker/docs/looker-core-psc-access#create-custom-domain) and configure access to that domain. See the [Northbound access to a Looker (Google Cloud core) instance using Private Service Connect](/looker/docs/looker-core-psc-access) documentation page for more information about how to set up access to your Looker (Google Cloud core) (Private Service Connect) instance.

## Set up Private Service Connect for external services

For your Looker (Google Cloud core) instance to be able to connect to an external service, that external service must be published using Private Service Connect. Follow the [instructions for publishing services by using Private Service Connect](/vpc/docs/configure-private-service-connect-producer) for any service that you want to publish.

Services can be published with [automatic approval](/vpc/docs/configure-private-service-connect-producer#publish-service-auto) or with [explicit approval](/vpc/docs/configure-private-service-connect-producer#publish-service-explicit). If you choose to publish with explicit approval, you must configure the service attachment as follows:

  * Set your service attachment allowlist to use projects (not networks).
  * Add the Looker tenant project ID to the allowlist.

You can find your Looker tenant project ID after your instance has been created by running the following command:
    
    
    gcloud looker instances describe INSTANCE_NAME --region=REGION--format=json
    

Replace the following:

  * `INSTANCE_NAME`: the name of your Looker (Google Cloud core) instance.
  * `REGION`: the region in which your Looker (Google Cloud core) instance is hosted.

In the command output, the `looker_service_attachment_uri` field will contain your Looker tenant project ID. It will have the following format: `projects/{Looker tenant project ID}/regions/…`

### Service attachment URI

When you later update your Looker (Google Cloud core) instance to connect to your service, you'll need the full service attachment URI for the external service. The URI will be specified as follows, using the project, region, and name that you used to create the service attachment:
    
    
    projects/{project}/regions/{region}/serviceAttachments/{name}
    

## Update a Looker (Google Cloud core) Private Service Connect instance

Once your Looker (Google Cloud core) Private Service Connect instance has been created, you can make the following changes:

  * Specify southbound (egress) connections
  * Update allowed VPCs

### Specify southbound connections

### console

  1. On the **Instances** page, click the name of the instance for which you want to enable [southbound](/looker/docs/glossary#southbound-traffic) (egress) connections.
  2. Click **Edit**.
  3. Expand the **Connections** section.
  4. To edit an existing service attachment, update the fully qualified domain name of the service in the **Local FQDN** field and the [service attachment URI](/looker/docs/looker-core-create-psc#service_attachment_uri) in the **Target Service Attachment URI** field.
  5. To add a new service attachment, click **Add Item**. Then, enter the fully qualified domain name of the service in the **Local FQDN** field and the [service attachment URI](/looker/docs/looker-core-create-psc#service_attachment_uri) in the **Target Service Attachment URI** field.
  6. Click **Save**.

### gcloud

Use `--psc-service-attachment` flags to enable [southbound](/looker/docs/glossary#southbound-traffic) (egress) connections to external services for which you have already set up Private Service Connect:
    
    
    gcloud looker instances update INSTANCE_NAME \
    --psc-service-attachment  domain=DOMAIN_1,attachment=SERVICE_ATTACHMENT_URI_1 \
    --psc-service-attachment domain=DOMAIN_2,attachment=SERVICE_ATTACHMENT_URI_2 \
    --region=REGION
    

Replace the following:

  * `INSTANCE_NAME`: the name of your Looker (Google Cloud core) instance.
  * `DOMAIN_1` and `DOMAIN_2`: If you are connecting to a public service, use the service's domain name. If you are connecting to a private service, use your choice of a fully qualified domain name. The following restrictions apply to the domain name:

  * Each southbound connection supports a single domain.

  * The domain name must consist of at least three parts. For example, `mydomain.github.com` is acceptable, but `github.com` is not acceptable.

  * The last part of the name cannot be any the following:

    * `googleapis.com`
    * `google.com`
    * `gcr.io`
    * `pkg.dev`

When you set up a connection to your service from within your Looker (Google Cloud core) instance, use this domain as the alias for your service.

  * `SERVICE_ATTACHMENT_1` and `SERVICE_ATTACHMENT_2`: the full service attachment URI for the published service you are connecting to. Each service attachment URI can be accessed by a single domain.

  * `REGION`: the region in which your Looker (Google Cloud core) instance is hosted.

If you are connecting to a non-Google managed service in a region other than the region where your Looker (Google Cloud core) instance is located, [enable global access](/vpc/docs/manage-endpoints-published-services#enable-global-access) on the producer load balancer.

#### Include all connections that should be enabled

Each time you run an update command with `--psc-service-attachment` flags, you must include every connection that you want to be enabled, including connections that were already enabled previously. For example, suppose you have previously connected an instance called `my-instance` to the `www.cloud.com` domain as follows:
    
    
    gcloud looker instances update my-instance --psc-service-attachment \
    domain=www.cloud.com,attachment=projects/123/regions/us-central1/serviceAttachment/cloud
    

Running the following command to add a new `www.me.com` connection would delete the `www.cloud.com` connection:
    
    
    gcloud looker instances update my-instance --psc-service-attachment \
    domain=www.me.com,attachment=projects/123/regions/us-central1/serviceAttachment/my-sa
    

To prevent deletion of the `www.cloud.com`connection when you add the new `www.me.com` connection, include a separate `psc-service-attachment` flag for both the existing connection and the new connection within the update command as follows:
    
    
    gcloud looker instances update my-instance --psc-service-attachment \
    domain=www.cloud.com,attachment=projects/123/regions/us-central1/serviceAttachment/cloud \
    --psc-service-attachment domain=www.me.com,attachment=projects/123/regions/us-central1/serviceAttachment/my-sa
    

#### Check southbound connection status

You can check the status of your southbound (egress) connections by again running the `gcloud looker instances describe --format=json` command. Each service attachment should be populated with a `connection_status` field.

**Note:** The `connection_status` field is updated every five minutes. If you recently updated your service attachments, this field may be stale.

#### Delete all southbound connections

To delete all southbound (egress) connections, run the following command:
    
    
    gcloud looker instances update MY_INSTANCE --clear-psc-service-attachments \
    --region=REGION
    

Replace the following:

  * `INSTANCE_NAME`: the name of your Looker (Google Cloud core) instance.
  * `REGION`: the region in which your Looker (Google Cloud core) instance is hosted.

### Update allowed VPCs

### console

  1. On the **Instances** page, click the name of the instance for which you want to update the VPCs that are allowed northbound access into the instance.
  2. Click **Edit**.
  3. Expand the **Connections** section.
  4. To add a new VPC, click **Add Item**. Then, select the project in which the VPC in the **Project** field, and select the network from the **Network** drop-down menu.
  5. To delete a VPC, click the **Delete item** trash icon that appears when you hold the pointer over the network.
  6. Click **Save**.

### gcloud

Use the `--psc-allowed-vpcs` flag to update the list of VPCs that have authorized northbound access into the instance.

When you update the allowed VPCs, you must specify the entire list that you want to be in effect after your update. For example, suppose VPC `ALLOWED_VPC_1` is already allowed, and you want to add VPC `ALLOWED_VPC_2`. To add VPC `ALLOWED_VPC_1` while making sure that VPC `ALLOWED_VPC_2` continues to be allowed, add the `--psc-allowed-vpcs` flag as follows:
    
    
    gcloud looker instances update INSTANCE_NAME \
    --psc-allowed-vpcs=ALLOWED_VPC_1,ALLOWED_VPC_2 --region=REGION
    

Replace the following:

  * `INSTANCE_NAME`: the name of your Looker (Google Cloud core) instance.
  * `ALLOWED_VPC_1` and `ALLOWED_VPC_2`: the VPCs that will be allowed ingress into Looker (Google Cloud core). Specify each allowed VPC using one of the following formats: 
    * `projects/{project}/global/networks/{network}`
    * `https://www.googleapis.com/compute/v1/projects/{project}/global/networks/{network}`
  * `REGION`: the region in which your Looker (Google Cloud core) instance is hosted.

#### Delete all allowed VPCs

To delete all allowed VPCs, run the following command:
    
    
    gcloud looker instances update MY_INSTANCE --clear-psc-allowed-vpcs \
    --region=REGION
    

Replace the following:

  * `INSTANCE_NAME`: the name of your Looker (Google Cloud core) instance.
  * `REGION`: the region in which your Looker (Google Cloud core) instance is hosted.

## Northbound access to your instance

After the Looker (Google Cloud core) (Private Service Connect) instance is created, you can set up northbound access to allow your users to access the instance.

To access your instance from another VPC network, first follow the [instructions for creating a Private Service Connect endpoint](/vpc/docs/configure-private-service-connect-services#create-endpoint). Make sure that the network is allowed northbound access to your Looker (Google Cloud core) instance and follow these guidelines when creating the endpoint:

  * Set the **Target service** field (for the Google Cloud console) or the `SERVICE_ATTACHMENT` variable (if following Google Cloud CLI or API instructions) to the Looker service attachment URI, which you can find by checking the [**Details** tab](/looker/docs/looker-core-view-console#details_tab) on the instance configuration page of the console or by running the following command:
    
        gcloud looker instances describe INSTANCE_NAME --region=REGION--format=json

Replace the following:

    * `INSTANCE_NAME`: the name of your Looker (Google Cloud core) instance.
    * `REGION`: the region in which your Looker (Google Cloud core) instance is hosted.
  * You can use any subnet that is hosted in the same region as the Looker (Google Cloud core) instance.

  * Don't enable global access.

To access your instance from a hybrid networking environment, you can follow the instructions on the [Northbound access to a Looker (Google Cloud core) instance using Private Service Connect](/looker/docs/looker-core-psc-access) documentation page to set up a custom domain and access the instance.

## What's next

  * [Northbound access to a Looker (Google Cloud core) instance using Private Service Connect](/looker/docs/looker-core-psc-access)