# https://cloud.google.com/looker/docs/looker-core-cmek

Depth: 3

By default, Google Cloud automatically [encrypts data when it is at rest](/security/encryption-at-rest/default-encryption) by using encryption keys that are managed by Google. If you have specific compliance or regulatory requirements related to the keys that protect your data, you can use customer-managed encryption keys (CMEK) for application-level encryption of Looker (Google Cloud core).

For more information about CMEK in general, including when and why to enable it, see the [Cloud Key Management Service documentation](/kms/docs/cmek).

This page walks you through how to configure a Looker (Google Cloud core) instance to use CMEK.

## How does Looker (Google Cloud core) interact with CMEK?

Looker (Google Cloud core) uses a single CMEK key (through a hierarchy of secondary keys) to help protect the sensitive data that is managed by the Looker (Google Cloud core) instance. During startup, each process within the Looker instance makes one initial call to the [Cloud Key Management Service](/kms/docs) (KMS) to decrypt the key. During normal operation (after startup), the entire Looker instance makes a single call to KMS approximately every five minutes to verify that the key is still valid.

**Note:** When you use CMEK keys in Looker (Google Cloud core), your projects can consume Cloud KMS cryptographic requests quotas. Encryption and decryption operations that use CMEK keys impact Cloud KMS quotas only if you use hardware (Cloud HSM) or external (Cloud EKM) keys. For more information, see [Cloud KMS quotas](/kms/quotas).

## What kinds of Looker (Google Cloud core) instances support CMEK?

Looker (Google Cloud core) instances support CMEK when two criteria are met:

  * The CMEK configuration steps described on this page are completed **before** the Looker (Google Cloud core) instance is [created](/looker/docs/looker-core-instance-create). You can't enable customer-managed encryption keys on existing instances.
  * [Instance editions](/looker/docs/looker-core-instance-create#create_edition) must be **Enterprise** or **Embed**.

## Workflow for creating a Looker (Google Cloud core) instance with CMEK

This page will walk you through the following steps to set up CMEK for a Looker (Google Cloud core) instance.

  1. Set up your environment.
  2. _Google Cloud CLI, Terraform, and API users only:_ Create a service account for each project that requires customer-managed encryption keys, if a Looker service account has not [already been set up](/looker/docs/looker-core-instance-create#service_account) for the project.
  3. Create a key ring and key, and set the location for the key. The location is the Google Cloud region in which you want to create the Looker (Google Cloud core) instance.
  4. _Google Cloud CLI, Terraform, and API users only:_ Copy or write down the key ID (KMS_KEY_ID) and location for the key, along with the ID (KMS_KEYRING_ID) for the key ring. You need this information when granting the service account access to the key.
  5. _Google Cloud CLI, Terraform, and API users only:_ Grant the service account access to the key.
  6. [Go to your project](https://console.cloud.google.com/projectselector2/home/dashboard) and create a Looker (Google Cloud core) instance with the following options: 
    1. Select the same [location](/looker/docs/looker-core-instance-create#set_the_hosting_region) as the customer-managed encryption key uses.
    2. Set the [edition](/looker/docs/looker-core-instance-create#set_the_instance_edition) to **Enterprise** or **Embed**.
    3. Enable the [customer-managed key](/looker/docs/looker-core-instance-create#encryption) configuration.
    4. Add the customer-managed encryption key either by name or by ID.

Once all these steps are completed, your Looker (Google Cloud core) instance will be enabled with CMEK.

### Before you begin

If you have not done so already, make sure that your environment is configured to let you follow the instructions on this page. Follow the steps in this section to make sure your setup is correct.

  1. In the Google Cloud console, on the project selector page, select or [create a Google Cloud project](/resource-manager/docs/creating-managing-projects). **Note:** If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, which will remove the resources that are associated with the project. 

[ Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. Make sure that billing is enabled for your Google Cloud project. Learn how to [check if billing is enabled on a project](/billing/docs/how-to/verify-billing-enabled).
  3. [Install](/sdk/docs/install) the Google Cloud CLI.
  4. To [initialize](/sdk/docs/initializing) the gcloud CLI, run the following command: 
    
        gcloud init
    

  5. Enable the Cloud Key Management Service API. 

[ Enable the API](https://console.cloud.google.com/flows/enableapi?apiid=cloudkms.googleapis.com)

  6. Enable the Looker (Google Cloud core) API. 

[ Enable the API](https://console.cloud.google.com/flows/enableapi?apiid=looker.googleapis.com)

#### Required roles

To understand the required roles for setting up CMEK, visit the [Access control with IAM](/kms/docs/iam) page of the Cloud Key Management Service documentation.

To create a Looker (Google Cloud core) instance, make sure that you have the [Looker Admin](/iam/docs/understanding-roles#looker.admin) IAM role for the project in which your Looker (Google Cloud core) instance is created. To enable CMEK for the instance within the Google Cloud console, make sure that you have the [Cloud KMS CryptoKey Encrypter/Decrypter](/iam/docs/understanding-roles#cloudkms.cryptoKeyEncrypterDecrypter) IAM role [on the key that is being used](/kms/docs/iam#granting_roles_on_a_resource) for CMEK.

If you need to [grant the Looker service account access to a Cloud KMS key](/looker/docs/looker-core-cmek#grant_the_service_account_access_to_the_key), you need the [Cloud KMS Admin](/iam/docs/understanding-roles#cloudkms.admin) IAM role [on the key that is being used](/kms/docs/iam#granting_roles_on_a_resource).

### Create a service account

If you are using the Google Cloud CLI, Terraform, or the API to create your Looker (Google Cloud core) instance, and a Looker service account has not [already been created](/looker/docs/looker-core-service-account) for the Google Cloud project that it will reside in, you need to create a service account for that project. If you are going to create more than one Looker (Google Cloud core) instance in the project, the same service account applies to all Looker (Google Cloud core) instances in that project, and creation of the service account needs to be done only once. If you use the console to create an instance, Looker (Google Cloud core) automatically creates the service account and grants it access to the CMEK key as you configure the **Use a customer managed encryption key** option.

To allow a user to manage service accounts, grant one of the following roles:

  * Service Account User (`roles/iam.serviceAccountUser`): Includes permissions to list service accounts, get details about a service account, and impersonate a service account.
  * Service Account Admin (`roles/iam.serviceAccountAdmin`): Includes permissions to list service accounts and get details about a service account. Also includes permissions to create, update, and delete service accounts.

Currently, you can use only [Google Cloud CLI](/sdk/gcloud) commands to create the type of service account you need for customer-managed encryption keys. If you are using the Google Cloud console, Looker (Google Cloud core) automatically creates this service account for you.

###  gcloud 

Run the following command to create the service account:
    
    
    gcloud beta services identity create \
    --service=looker.googleapis.com \
    --project=PROJECT_ID
    

Replace `PROJECT_ID` with the project that the Looker (Google Cloud core) instance resides in.

This command creates the service account and returns the service account name. You use this service account name during the procedure in Granting the service account access to the key.

After creating the service account, wait a few minutes for the service account to propagate.

### Create a key ring and key

**Note:** You can use an externally managed key with CMEK using the Cloud EKM service to [make the key available](/kms/docs/ekm) through Cloud KMS.

You can create the key in the same Google Cloud project as the Looker (Google Cloud core) instance or in a separate user project. The Cloud KMS key ring location must match the [region](/looker/docs/looker-core-instance-create#create_region) where you want to create the Looker (Google Cloud core) instance. A multi-region or global region key **will not** work. The Looker (Google Cloud core) instance create request fails if the regions don't match.

**Note:** Sometimes, a Looker (Google Cloud core) instance that is enabled with CMEK has the Cloud KMS key hosted in a different Google Cloud project. For this scenario, when you enable VPC Service Controls, you must add the KMS key hosting project to the security perimeter.

Follow the instructions on the [Create a key ring](/kms/docs/create-key-ring) and [Create a key](/kms/docs/create-key#create-symmetric) documentation pages to create a key ring and key that meet the following two criteria:

  * The **Key ring location** field must match the [region](/looker/docs/looker-core-instance-create#create_a_instance) that you will set for the Looker (Google Cloud core) instance.
  * The key **Purpose** field must be **Symmetric encrypt/decrypt**.

See the Rotate your key section to learn about rotating the key and creating new key versions.

### Copy or write down the `KMS_KEY_ID` and the `KMS_KEYRING_ID`

If you are using the Google Cloud CLI, Terraform, or the API to set up your Looker (Google Cloud core) instance, follow the instructions on the [Getting a Cloud KMS resource ID](/kms/docs/getting-resource-ids) documentation page to locate the resource IDs for the key ring and key you just created. Copy or write down the key ID (KMS_KEY_ID) and location for the key, along with the ID (KMS_KEYRING_ID) for the key ring. You need this information when granting the service account access to the key.

### Grant the service account access to the key

You only need to perform this procedure if both of the following are true:

  * You are using the Google Cloud CLI, Terraform, or the API.
  * The service account has not already been granted access to the key. For example, if there is already a Looker (Google Cloud core) instance in the same project that uses the same key, you do not need to grant access. Alternatively, if access to the key has already been granted by someone else, you do not need to grant access.

You must have the [Cloud KMS Admin](/iam/docs/understanding-roles#cloudkms.admin) IAM role [on the key that is being used](/kms/docs/iam#granting_roles_on_a_resource) to grant the service account access.

To grant the service account access:

###  gcloud 
    
    
    gcloud kms keys add-iam-policy-binding KMS_KEY_ID \
    --location=REGION \
    --keyring=KMS_KEYRING_ID \
    --member=serviceAccount:SERVICE_ACCOUNT_NAME \
    --role=roles/cloudkms.cryptoKeyEncrypterDecrypter
    

Replace the following:

  * KMS_KEY_ID: the ID of the KMS key
  * REGION: the region the Looker (Google Cloud core) is created in and the location of the key ring
  * KMS_KEYRING_ID: the ID of the KMS key ring
  * SERVICE_ACCOUNT_NAME: the service account name returned when you created the service account

After granting the service account the IAM role, wait a few minutes for the permission to propagate.

### Create a Looker (Google Cloud core) instance with CMEK

**Caution:** Once you have created your instance with CMEK settings, you cannot change or remove the CMEK settings.

To create an instance with customer-managed encryption keys in the Google Cloud console, first follow the steps in the Create a key ring and key section, shown previously, to create a key ring and key in the same region that you will use for your Looker (Google Cloud core) instance. Next, using the following settings, follow the instructions for creating a Looker (Google Cloud core) instance.

To create a Looker (Google Cloud core) instance with CMEK settings, select one of the following options:

### console

  1. Make sure that you have the [Cloud KMS CryptoKey Encrypter/Decrypter](/iam/docs/understanding-roles#cloudkms.cryptoKeyEncrypterDecrypter) IAM role [on the key that is being used](/kms/docs/iam#granting_roles_on_a_resource) for CMEK.
  2. In the **Edition** section of the **Create an instance** page, you must select an **Enterprise** or an **Embed** edition to use CMEK.
  3. In the **Encryption** section of the **Create an instance** page, select the **Customer-managed encryption key (CMEK)** radio button. This reveals a **Select a customer-managed key** drop-down field.
  4. In the **Select a customer managed key** field, set the key that you want to use. The key must be in a key ring that has a location set to the same region as the Looker (Google Cloud core) instance that you are creating, or instance creation will fail. You can select the key through one of the following two methods: 
    1. _Select the name of the key from the drop-down list:_ The available keys in your Google Cloud project appear in a drop-down list. Once you have selected your key, click **OK**.
    2. _Enter the key's[resource ID](/kms/docs/getting-resource-ids):_ Click the text **Don't see your key? Enter key resource ID** , which appears at the bottom of the drop-down menu.This reveals an **Enter key resource ID** dialog, where you can enter the key's ID. Once you have entered the ID, select **Save**.
  5. Once you select a key, a message appears asking you to grant permission to your service account to use the key. Click the **Grant** button.
  6. If the service account does not have permission to encrypt and decrypt with the selected key, a message appears. If this happens, click **Grant** to grant the service account the [Cloud KMS CryptoKey Encrypter/Decrypter IAM role](/iam/docs/understanding-roles#cloudkms.cryptoKeyEncrypterDecrypter) on the selected KMS key.
  7. Once you have finished all configuration for your Looker (Google Cloud core) instance, click **Create**.

###  gcloud 
    
    
    gcloud looker instances create INSTANCE_NAME \
    --project=PROJECT_ID \
    --oauth-client-id=OAUTH_CLIENT_ID\
    --oauth-client-secret=OAUTH_CLIENT_SECRET \
    --kms-key=KMS_KEY_ID
    --region=REGION \
    --edition=EDITION
    [--consumer-network=CONSUMER_NETWORK --private-ip-enabled --reserved-range=RESERVED_RANGE]
    [--no-public-ip-enabled]
    [--public-ip-enabled]
    

Replace the following:

  * `INSTANCE_NAME`: a name for your Looker (Google Cloud core) instance; it is not associated with the instance URL
  * `PROJECT_ID`: the name of the Google Cloud project in which you are creating the Looker (Google Cloud core) instance
  * `OAUTH_CLIENT_ID` and `OAUTH_CLIENT_SECRET`: the OAuth client ID and OAuth secret that you created when you [set up your OAuth client](/looker/docs/looker-core-create-oauth#generate_the_oauth_client_id_and_client_secret). After the instance has been created, [enter the instance's URL in the **Authorized redirect URIs** section of the OAuth client](/looker/docs/looker-core-create-oauth#add_the_authorized_redirect_uri_to_the_oauth_client).
  * KMS_KEY_ID: the ID of the KMS key
  * `REGION`: the region in which your Looker (Google Cloud core) instance is hosted. Available regions are listed on the [Looker (Google Cloud core) locations](/looker/docs/looker-core-locations) documentation page.
  * `EDITION`: to enable CMEK, `EDITION` must be `core-embed-annual` or `core-enterprise-annual`
  * `CONSUMER_NETWORK`: [your VPC network or Shared VPC](/looker/docs/looker-core-create-private-ip#create-vpc). Must be set if you're creating a private IP instance.
  * `RESERVED_RANGE`: the range of IP addresses within the VPC in which Google will provision a subnetwork for your Looker (Google Cloud core) instance. Must be set if you're creating a private IP instance.

You may include the following flags:

  * `--private-ip-enabled` enables private IP.
  * `--public-ip-enabled` enables public IP.
  * `--no-public-ip-enabled` disables public IP.

### Terraform

**Important:** To run the following Terraform resource, you must have the [Cloud KMS Admin (`roles/cloudkms.admin`) IAM role](/kms/docs/create-key-ring#required-roles) on the project in which you are creating the Looker (Google Cloud core) instance.

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

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](/docs/terraform/basic-commands).

**Note:** If you create a private IP instance using Terraform, the network name must follow the format: `projects/<project>/global/networks/<network>`.

Your Looker (Google Cloud core) instance is now enabled with CMEK.

**Note:** If you create a private IP only instance, a URL **won't** appear on the **Instances** page. To access the instance, you must configure a custom domain for the instance and add that custom domain to the instance's OAuth credentials. Visit the [Custom domain networking options for Looker (Google Cloud core) private IP instances](/looker/docs/looker-core-custom-domain-private-ip-overview) documentation page to learn more.

## View key information for a CMEK-enabled instance

Once you successfully create a Looker (Google Cloud core) instance, you can check to see if CMEK is enabled.

To see if CMEK is enabled, select one of the following options:

### console

  1. In the Google Cloud console, go to the **Looker Instances** page.
  2. Click an instance name to open its **Details** page. If an instance has CMEK enabled, an **Encryption** row indicates the encryption used for the instance. The **Customer-managed encryption key (CMEK)** field shows the key identifier.

###  gcloud 
    
    
    gcloud looker instances describe INSTANCE_NAME --region=REGION --format config
    

Replace the following:

  * `INSTANCE_NAME`: a name for your Looker (Google Cloud core) instance; it is not associated with the instance URL
  * REGION: the [region](/looker/docs/looker-core-view-console#the_instances_page) the instance was created in

This command should return a `kmsKeyName`, a `kmsKeyNameVersion`, and a `kmsKeyState` to confirm that the instance was configured with CMEK.

## Use Cloud External Key Manager (Cloud EKM)

To protect data in Looker (Google Cloud core) instances, you can use keys that you manage within a supported external key management partner. For more information, see the [Cloud External Key Manager](/kms/docs/ekm) documentation page, including the [Considerations](/kms/docs/ekm#considerations) section.

When you are ready to create a Cloud EKM key, see the [How it works](/kms/docs/ekm#how_it_works) section of the [Cloud External Key Manager](/kms/docs/ekm) documentation page. After a key is created, provide the key name when you create a Looker (Google Cloud core) instance.

Google does not control the availability of keys in an external key management partner system.

**Warning:** If an external key is deleted or cannot be recovered, any Looker (Google Cloud core) instances that are encrypted with that key become permanently inaccessible.

## Rotate your key

**Note:** If you rotate the key used to help secure your Looker (Google Cloud core) instance, Google recommends that you keep your previous key version enabled for 45 days to help ensure that your latest backup remains accessible.

You may want to rotate your key to help promote security. Each time your key is rotated, it creates a new key version. To learn more about key rotation, see the [Key rotation](/kms/docs/key-rotation) documentation page.

If you rotate the key used to help secure your Looker (Google Cloud core) instance, the previous key version is still necessary to access backups or exports made when that key version was in use. For that reason, Google recommends keeping the previous key version enabled for at least 45 days after rotation to help ensure that those items remain accessible. Key versions are kept by default until they are disabled or destroyed.

## Disable and re-enable key versions

See the following documentation pages:

  * [Disable an enabled key version](/kms/docs/enable-disable#disable_an_enabled_key_version)
  * [Enable a disabled key version](/kms/docs/enable-disable#enable_a_disabled_key_version)

If a key version that is used to help secure a Looker (Google Cloud core) instance is disabled, the Looker (Google Cloud core) instance is required to stop operating, clear any unencrypted sensitive data that it may have in memory, and wait until the key becomes available again. The process is as follows:

  1. The key version that is used to help secure a Looker (Google Cloud core) instance is disabled.
  2. Within approximately 15 minutes, the Looker (Google Cloud core) instance detects that the key version is revoked, stops operating, and clears all encrypted data in memory.
  3. After the instance stops operating, calls to Looker APIs return an error message.
  4. After the instance stops operating, the Looker (Google Cloud core) UI returns an error message.
  5. If you re-enable the key version, you must manually trigger a [restart](/looker/docs/looker-core-delete-restart#restart_a_instance) of the instance.

If you disable a key version and do not want to wait for the Looker (Google Cloud core) instance to stop on its own, you can manually trigger an instance restart so that the Looker (Google Cloud core) instance detects the revoked key version immediately.

## Destroying key versions

**Warning:** Destroying a key version used to help secure a Looker (Google Cloud core) instance requires that the instance be deleted.

See the following documentation page:

  * [Destroying and restoring key versions](/kms/docs/destroy-restore)

If a key version that is used to help secure a Looker (Google Cloud core) instance is destroyed, the Looker instance becomes inaccessible. The instance must be deleted, and you will not be able to access its data.

## Troubleshoot

This section describes things to try when you get an error message while setting up or using CMEK-enabled instances.

Looker (Google Cloud core) administrator operations, such as create or update, might fail due to Cloud KMS errors and missing roles or permissions. Common reasons for failure include a missing Cloud KMS key version, a disabled or destroyed Cloud KMS key version, insufficient IAM permissions to access the Cloud KMS key version, or the Cloud KMS key version being in a different region than the Looker (Google Cloud core) instance. Use the following troubleshooting table to diagnose and resolve common problems.

### Customer-managed encryption keys troubleshooting table

**Error message** | **Possible causes** | **Troubleshooting strategies**  
---|---|---  
Per-product, per-project service account not found  | The service account name is incorrect.  | Make sure that you created a service account for the correct user project.  [GO TO THE SERVICE ACCOUNTS PAGE](https://console.cloud.google.com/iam-admin/serviceaccounts)  
Cannot grant access to the service account  | The user account does not have permission to grant access to this key version.  | Add the **[Organization Administrator](/iam/docs/understanding-roles?_ga=2.219977817.1510791600.1679348222-1340276334.1679348222#resourcemanager.organizationAdmin)** role on your user or service account. [GO TO THE IAM ACCOUNTS PAGE](https://console.cloud.google.com/iam-admin/iam)  
Cloud KMS key version is destroyed  | The key version is destroyed.  | If the key version is destroyed, you cannot use it to encrypt or decrypt data. The Looker (Google Cloud core) instance must be deleted.   
Cloud KMS key version is disabled  | The key version is disabled.  | [Re-enable](/kms/docs/enable-disable#enable_a_disabled_key_version) the Cloud KMS key version. [GO TO THE KEY MANAGEMENT PAGE](https://console.cloud.google.com/security/kms)  
Insufficient permission to use the Cloud KMS key  | The `cloudkms.cryptoKeyEncrypterDecrypter` role is missing on the user or service account that you are using to run operations on Looker (Google Cloud core) instances, or the Cloud KMS key version doesn't exist.  | Add the `cloudkms.cryptoKeyEncrypterDecrypter` role on your user or service account. [GO TO THE IAM ACCOUNTS PAGE](https://console.cloud.google.com/iam-admin/iam) If the role is already on your account, see the Create a key ring and key section to learn how to create a new key version. Then complete the instance creation steps again.  
Cloud KMS key is not found  | The key version does not exist.  | Create a new key version and complete the instance creation steps again. See the Create a key ring and key section.   
Looker (Google Cloud core) instance and Cloud KMS key version are in different regions  | The Cloud KMS key version and Looker (Google Cloud core) instance must be in the same region. It does not work if the Cloud KMS key version is in a global region or multi-region.  | Create a key version in the same region where you want to create instances, and complete the instance creation steps again. See the Create a key ring and key section.   
**Note:** If the instance is in a failed state during the `create` operation, you must delete it, add the role to the account that you are using, and create a new instance with an active Cloud KMS key version.

## What's next

  * [Administer a Looker (Google Cloud core) instance from the Google Cloud console](/looker/docs/looker-core-admin-console)
  * [Looker (Google Cloud core) admin settings](/looker/docs/looker-core-admin-looker)