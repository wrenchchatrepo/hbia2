# https://cloud.google.com/looker/docs/looker-core-instance-create

Depth: 3

**Note:** Private IP must be assigned at instance creation. For instructions on how to create a private IP instance, follow the procedure on the [Create a private IP Looker (Google Cloud core) instance](/looker/docs/looker-core-create-private-ip) or on the [Create a Looker (Google Cloud core) Private Service Connect instance](/looker/docs/looker-core-create-psc) documentation pages instead of the following procedure.

This page discusses how to provision a public IP Looker (Google Cloud core) production or [non-production instance](/looker/docs/looker-core-overview#staging_environments_and_testing).

## Before you begin

  1. In the Google Cloud console, on the project selector page, [create a Google Cloud project](/resource-manager/docs/creating-managing-projects) or navigate to an existing one. 

[ Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. [Enable the Looker API](/apis/docs/getting-started#enabling_apis) for your project in the Google Cloud console. When enabling the API, you may need to refresh the console page to confirm that the API has been enabled. 

[ Enable the API](https://console.cloud.google.com/flows/enableapi?apiid=looker.googleapis.com)

**Caution:** Disabling the Looker API after instance creation will affect Looker (Google Cloud core) features. For example, disabling the API will disable the ability to create [instance backups](/looker/docs/looker-core-backup-restore).
  3. [Set up an OAuth client and create authorization credentials](/looker/docs/looker-core-create-oauth). The OAuth client lets you authenticate and access the instance. You must set up OAuth to create a Looker (Google Cloud core) instance, even if you are using a different [authentication method](/looker/docs/looker-core-user-authentication) to authenticate users into your instance.
  4. If you want to use [VPC Service Controls](/looker/docs/looker-core-vpcsc), you must create a [private IP](/looker/docs/looker-core-create-private-ip) instance instead of a public IP instance.

### Required roles

To get the permissions that you need to create a Looker (Google Cloud core) instance, ask your administrator to grant you the [Looker Admin ](https://cloud.google.com/iam/docs/understanding-roles#looker.admin) (`roles/looker.admin`) IAM role on the project the instance will reside in. For more information about granting roles, see [Manage access to projects, folders, and organizations](/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](/iam/docs/creating-custom-roles) or other [predefined roles](/iam/docs/understanding-roles). 

**Note:** [IAM basic roles](/iam/docs/understanding-roles#basic) might also contain permissions to create a Looker (Google Cloud core) instance. You shouldn't grant basic roles in a production environment, but you can grant them in a development or test environment. 

You may also need additional IAM roles if you want to set up [customer-managed encryption keys (CMEK)](/looker/docs/looker-core-cmek). Visit the [Access control with IAM](/kms/docs/iam) page of the Cloud Key Management Service documentation to learn more.

## Create a Looker (Google Cloud core) instance

> Looker (Google Cloud core) requires approximately 60 minutes to generate a new instance.

**Important:** If you want to use customer-managed encryption keys (CMEK) with the Looker (Google Cloud core) instance that you are creating, see the [Enable CMEK for Looker (Google Cloud core)](/looker/docs/looker-core-cmek) documentation page for information on the additional setup that's required prior to instance creation.

To create your Looker (Google Cloud core) instance, select one of the following options:

### console

  1. Navigate to the Looker (Google Cloud core) product page from your project in the Google Cloud console. If you have already created a Looker (Google Cloud core) instance within this project, this will open the **Instances** page. 

[Go to Looker (Google Cloud core)](https://console.cloud.google.com/looker)

  2. Click **CREATE INSTANCE**.
  3. In the **Instance name** section, provide a name for your Looker (Google Cloud core) instance. The instance name isn't associated with the URL of the Looker (Google Cloud core) instance once it is created. The instance name cannot be changed after instance creation.
  4. In the **OAuth Application Credentials** section, enter the OAuth client ID and OAuth secret that you created when you [set up your OAuth client](/looker/docs/looker-core-create-oauth#generate_the_oauth_client_id_and_client_secret).
  5. In the **Region** section, select the appropriate option from the drop-down menu to host your Looker (Google Cloud core) instance. Select the region that matches the region in the subscription contract, which is where the [quota for your project](/docs/quota_detail/view_manage) is allocated. Available regions are listed on the [Looker (Google Cloud core) locations](/looker/docs/looker-core-locations) documentation page.  **Note:** You cannot change the region once the instance has been created.
  6. In the **Edition** section, set the instance edition and environment type (production or [non-production](/looker/docs/looker-core-overview#staging_environments_and_testing)) according to your organization's needs. The edition type affects some of the [features that are available](/looker/docs/looker-core-edition-types) for the instance. Make sure that you choose the same edition type as listed in your [annual contract](/looker/pricing) and that you have [quota](/docs/quotas/view-manage) allocated for that edition type. These are the edition options:

     * **Standard** : Looker (Google Cloud core) platform for small organizations or teams with fewer than 50 users
     * **Enterprise** : Looker (Google Cloud core) platform with enhanced security features for addressing a wide variety of internal BI and analytics use cases
     * **Embed** : Looker (Google Cloud core) platform for deploying and maintaining reliable external analytics and custom applications at scale

Editions cannot be changed after instance creation. If you want to change an edition, you can use [import and export](/looker/docs/looker-core-import-export) to move your Looker (Google Cloud core) instance data into a new instance that is configured with a different edition.

  7. In the **Customize your instance** section, click **SHOW CONFIGURATION OPTIONS** to display a group of additional settings that you can customize for the instance.

  8. In the **Connections** section, select only **Public IP**. A public IP connection setting assigns an external, internet-accessible IP address and is available for all edition types.

**Note:** If you are creating an **Enterprise** and **Embed** edition, you can also use private IP, which assigns an internal, Google-hosted IP address that is accessible on a [Virtual Private Cloud (VPC)](/vpc/docs/overview). If you want to use private IP, or both private IP and public IP, follow the steps on the [Create a private IP Looker (Google Cloud core) instance](/looker/docs/looker-core-create-private-ip) or the [Create a Looker (Google Cloud core) Private Service Connect](/looker/docs/looker-core-create-psc) documentation pages to complete instance creation.

If you select only **Private IP** or both **Public IP** and **Private IP** , follow the steps on the [Create a private IP Looker (Google Cloud core) instance](/looker/docs/looker-core-create-private-ip) documentation page to complete your network setup during instance creation.

  9. In the **Encryption** section, you can select the type of encryption to use on your instance. The following encryption options are available:

     * [**Google-managed encryption key**](/security/encryption-at-rest/default-encryption): This option is the default and doesn't require any additional configuration.
     * [**Customer-managed encryption key (CMEK)**](/kms/docs/cmek): See the [Using customer-managed encryption keys with Looker (Google Cloud core)](/looker/docs/looker-core-cmek#create_a_instance_with_cmek) documentation page for more information on CMEK and how to configure it during instance creation. The type of encryption cannot be changed after instance creation.
     * **Enable[FIPS 140-2 Validated Encryption](https://csrc.nist.gov/pubs/fips/140-2/upd2/final)**: See the [Enable FIPS 140-2 level 1 compliance on a Looker (Google Cloud core) instance](/looker/docs/looker-core-fips-mode) documentation page for more information on FIPS 140-2 support on Looker (Google Cloud core). 
  10. In the **Maintenance Window** section, you can optionally [specify the day of the week and the hour](/looker/docs/looker-core-maintenance#set_a_preferred_window_for_maintenance) in which Looker (Google Cloud core) schedules maintenance. Maintenance windows last for one hour. By default, the **Preferred Window** option in the **Maintenance Window** is set to **Any window**.

  11. In the **Deny Maintenance Period** section, you can optionally [specify a block of days](/looker/docs/looker-core-maintenance#define_a_maintenance_deny_period_to_defer_maintenance) in which Looker (Google Cloud core) doesn't schedule maintenance. Deny maintenance periods can be up to 60 days long. You must allow at least 14 days of maintenance availability between any 2 deny maintenance periods.

  12. In the **Gemini in Looker** section, you can optionally make [Gemini in Looker features](/looker/docs/looker-core-admin-gemini#gemini-feature-availability) available for the Looker (Google Cloud core) instance. To enable Gemini in Looker, select **Gemini** , and then select **Trusted Tester features**. When **Trusted Tester features** is enabled, users can access the Trusted Tester capabilities of Gemini in Looker. You may request access to the non-public Trusted Tester capabilities through the [Gemini in Looker preview form](https://docs.google.com/forms/d/e/1FAIpQLSefBWbxchQFyZB9EOOcRxYTRi-16TezwRExW-x-XJRfeklCiA/viewform) on a per-user basis. You must enable this setting to use Gemini during the pre-GA preview. Optionally, select **Trusted Tester data use**. When this setting is enabled, you consent to your data being used by Google as described in the [Gemini for Google Cloud Trusted Tester Program terms](/trusted-tester/gemini-for-google-cloud-preview). To disable Gemini for a Looker (Google Cloud core) instance, clear the **Gemini** setting.

  13. Click **Create**.

###  gcloud 

  1. If you are using [CMEK](/looker/docs/looker-core-cmek), then [create the Looker service account](/looker/docs/looker-core-cmek#create_a_service_account) and follow the instructions for setting up CMEK first.
  2. Use the `gcloud looker instances create` command to create the instance:
    
        gcloud looker instances create INSTANCE_NAME \
    --project=PROJECT_ID \
    --oauth-client-id=OAUTH_CLIENT_ID \
    --oauth-client-secret=OAUTH_CLIENT_SECRET \
    --region=REGION \
    --edition=EDITION \
    [--consumer-network=CONSUMER_NETWORK --private-ip-enabled --reserved-range=RESERVED_RANGE]
    [--no-public-ip-enabled]
    [--public-ip-enabled]
    [--async]
    

Replace the following:

     * `INSTANCE_NAME`: a name for your Looker (Google Cloud core) instance; it isn't associated with the instance URL.
     * `PROJECT_ID`: the name of the Google Cloud project in which you are creating the Looker (Google Cloud core) instance.
     * `OAUTH_CLIENT_ID` and `OAUTH_CLIENT_SECRET`: the OAuth client ID and OAuth secret that you created when you [set up your OAuth client](/looker/docs/looker-core-create-oauth#generate_the_oauth_client_id_and_client_secret). After the instance has been created, [set up the authorized redirect URI in the OAuth client that you previously created](/looker/docs/looker-core-create-oauth#add_the_authorized_redirect_uri_to_the_oauth_client).
     * `REGION`: the region in which your Looker (Google Cloud core) instance is hosted. Select the region that matches the region in the subscription contract. Available regions are listed on the [Looker (Google Cloud core) locations](/looker/docs/looker-core-locations) documentation page.
     * `EDITION`: the edition and environment type (production or [non-production](/looker/docs/looker-core-overview#staging_environments_and_testing)) for the instance. Its possible values are `core-standard-annual`, `core-enterprise-annual`, `core-embed-annual`, `nonprod-core-standard-annual`, `nonprod-core-enterprise-annual`, or `nonprod-core-embed-annual`. Editions cannot be changed after instance creation. If you want to change an edition, you can use [import and export](/looker/docs/looker-core-import-export) to move your Looker (Google Cloud core) instance data into a new instance that is configured with a different edition.
     * `CONSUMER_NETWORK`: [your VPC network or Shared VPC](/looker/docs/looker-core-create-private-ip#create-vpc). Must be set if you're creating a private IP instance.
     * `RESERVED_RANGE`: the range of IP addresses within the VPC in which Google will provision a subnetwork for your Looker (Google Cloud core) instance. Don't define a range if you're enabling a private IP network connection for your instance.

Also include these flags:

     * `--public-ip-enabled` is used to enable public IP.
     * `--async` is recommended when you're creating a Looker (Google Cloud core) instance.
  3. You can add more parameters to apply other instance settings: 
    
        [--maintenance-window-day=MAINTENANCE_WINDOW_DAY
          --maintenance-window-time=MAINTENANCE_WINDOW_TIME]
    [--deny-maintenance-period-end-date=DENY_MAINTENANCE_PERIOD_END_DATE
          --deny-maintenance-period-start-date=DENY_MAINTENANCE_PERIOD_START_DATE
          --deny-maintenance-period-time=DENY_MAINTENANCE_PERIOD_TIME]
    --kms-key=KMS_KEY_ID
    [--fips-enabled]
    

Replace the following:

     * `MAINTENANCE_WINDOW_DAY`: must be one of the following: `friday`, `monday`, `saturday`, `sunday`, `thursday`, `tuesday`, `wednesday`. See the [Manage maintenance policies for Looker (Google Cloud core)](/looker/docs/looker-core-maintenance#maintenance_settings) documentation page for more information about maintenance window settings.
     * `MAINTENANCE_WINDOW_TIME` and `DENY_MAINTENANCE_PERIOD_TIME`: must be in UTC time in 24-hour format (for example, 13:00, 17:45).
     * `DENY_MAINTENANCE_PERIOD_START_DATE` and `DENY_MAINTENANCE_PERIOD_END_DATE`: must be in the format `YYYY-MM-DD`.
     * `KMS_KEY_ID`: must be the key that is created when setting up [customer-managed encryption keys (CMEK)](/looker/docs/looker-core-cmek#copy_or_write_down_the_kms_key_id_and_the_kms_keyring_id).

You may include the `--fips-enabled` flag to [enable FIPS 140-2 level 1 compliance](/looker/docs/looker-core-fips-mode).

### Terraform

Use the following [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/looker_instance#example-usage---looker-instance-basic) to provision a **Standard** Looker (Google Cloud core) instance with basic functionality:
    
    
    # Creates a Standard edition Looker (Google Cloud core) instance with basic functionality enabled.
    resource "google_looker_instance" "main" {
      name             = "my-instance"
      platform_edition = "LOOKER_CORE_STANDARD"
      region           = "us-central1"
      oauth_config {
        client_id     = "my-client-id"
        client_secret = "my-client-secret"
      }
    }

Use the following [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/looker_instance#example-usage---looker-instance-full) to provision a **Standard** Looker (Google Cloud core) instance with additional settings applied:
    
    
    # Creates a Standard edition Looker (Google Cloud core) instance with full functionality enabled.
    
    resource "google_looker_instance" "main" {
      name              = "my-instance"
      platform_edition  = "LOOKER_CORE_STANDARD"
      region            = "us-central1"
      public_ip_enabled = true
      admin_settings {
        allowed_email_domains = ["google.com"]
      }
      // User metadata config is only available when platform edition is LOOKER_CORE_STANDARD.
      user_metadata {
        additional_developer_user_count = 10
        additional_standard_user_count  = 10
        additional_viewer_user_count    = 10
      }
      maintenance_window {
        day_of_week = "THURSDAY"
        start_time {
          hours   = 22
          minutes = 0
          seconds = 0
          nanos   = 0
        }
      }
      deny_maintenance_period {
        start_date {
          year  = 2050
          month = 1
          day   = 1
        }
        end_date {
          year  = 2050
          month = 2
          day   = 1
        }
        time {
          hours   = 10
          minutes = 0
          seconds = 0
          nanos   = 0
        }
      }
      oauth_config {
        client_id     = "my-client-id"
        client_secret = "my-client-secret"
      }
    }
    

**Important:** To run the following Terraform resource, you must have the [Cloud KMS Admin (`roles/cloudkms.admin`) IAM role](/kms/docs/create-key-ring#required-roles) on the project in which you are creating the Looker (Google Cloud core) instance. See more about encryption keys on the [Enable CMEK for Looker (Google Cloud core)](/looker/docs/looker-core-cmek#create_a_key_ring_and_key) documentation page.

Use the following [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/looker_instance#example-usage---looker-instance-enterprise-full) to provision an **Enterprise** Looker (Google Cloud core) instance with a private network connection:
    
    
    # Creates an Enterprise edition Looker (Google Cloud core) instance with full, Private IP functionality.
    resource "google_looker_instance" "main" {
      name               = "my-instance"
      platform_edition   = "LOOKER_CORE_ENTERPRISE_ANNUAL"
      region             = "us-central1"
      private_ip_enabled = true
      public_ip_enabled  = false
      reserved_range     = google_compute_global_address.main.name
      consumer_network   = data.google_compute_network.main.id
      admin_settings {
        allowed_email_domains = ["google.com"]
      }
      encryption_config {
        kms_key_name = google_kms_crypto_key.main.id
      }
      maintenance_window {
        day_of_week = "THURSDAY"
        start_time {
          hours   = 22
          minutes = 0
          seconds = 0
          nanos   = 0
        }
      }
      deny_maintenance_period {
        start_date {
          year  = 2050
          month = 1
          day   = 1
        }
        end_date {
          year  = 2050
          month = 2
          day   = 1
        }
        time {
          hours   = 10
          minutes = 0
          seconds = 0
          nanos   = 0
        }
      }
      oauth_config {
        client_id     = "my-client-id"
        client_secret = "my-client-secret"
      }
      depends_on = [
        google_service_networking_connection.main,
        google_kms_crypto_key.main
      ]
    }
    
    resource "google_kms_key_ring" "main" {
      name     = "keyring-example"
      location = "us-central1"
    }
    
    resource "google_kms_crypto_key" "main" {
      name     = "crypto-key-example"
      key_ring = google_kms_key_ring.main.id
    }
    
    resource "google_service_networking_connection" "main" {
      network                 = data.google_compute_network.main.id
      service                 = "servicenetworking.googleapis.com"
      reserved_peering_ranges = [google_compute_global_address.main.name]
    }
    
    resource "google_compute_global_address" "main" {
      name          = "looker-range"
      purpose       = "VPC_PEERING"
      address_type  = "INTERNAL"
      prefix_length = 20
      network       = data.google_compute_network.main.id
    }
    
    data "google_project" "main" {}
    
    data "google_compute_network" "main" {
      name = "default"
    }
    
    resource "google_kms_crypto_key_iam_member" "main" {
      crypto_key_id = google_kms_crypto_key.main.id
      role          = "roles/cloudkms.cryptoKeyEncrypterDecrypter"
      member        = "serviceAccount:service-${data.google_project.main.number}@gcp-sa-looker.iam.gserviceaccount.com"
    }

**Note:** If you create a private IP only instance, a URL won't appear on the **Instances** page. To access the instance, you need to create a [custom domain](/looker/docs/looker-core-custom-domain) or set up a [public-facing proxy](/looker/docs/looker-core-private-ip-config#set_up_a_proxy_server).

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](/docs/terraform/basic-commands).

Instance creation cannot be paused or terminated once it has been initiated. When your Terraform resource has been provisioned successfully, your terminal will print the following message:
    
    
    Creation complete after XmXs [id=projects/PROJECT-ID/locations/REGION/instances/my-instance-randomly-generated-name]
    
    
    
    Apply complete! Resources: X added, X changed, X destroyed.
    

To view the status of your new instance, which will be assigned a randomly generated name, visit the [**Instances**](/looker/docs/looker-core-view-console) page within the console.

As the instance is being created, you can view its status on the [**Instances**](/looker/docs/looker-core-view-console) page within the console. You can also see your instance creation activity by clicking on the notifications icon in the Google Cloud console menu.

Once the public IP instance is created, the instance's public URL will appear in the **Instance URL** column of the **Instances** page.

After the instance has been created, [set up the authorized redirect URI in the OAuth client that you previously created](/looker/docs/looker-core-create-oauth#add_the_authorized_redirect_uri_to_the_oauth_client).

After the instance is created and you have completed OAuth setup, you can view the instance by navigating to the instance URL, which will be shown on the **Instances** page.

## What's next

  * [Set up and access a custom domain for a public IP Looker (Google Cloud core) instance](/looker/docs/looker-core-custom-domain)
  * [Connect Looker (Google Cloud core) to your database](/looker/docs/looker-core-dialects)
  * [Prepare a Looker (Google Cloud core) instance for users](/looker/docs/looker-core-instance-setup)
  * [Manage users within Looker (Google Cloud core)](/looker/docs/looker-core-user-management)