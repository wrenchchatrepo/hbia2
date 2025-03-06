# https://cloud.google.com/looker/docs/looker-core-import-export

Depth: 3

You may want to export your Looker (Google Cloud core) instance data — which includes created content and internal data about your Looker (Google Cloud core) instance — from one Looker (Google Cloud core) instance, and then import that data to another Looker (Google Cloud core) instance. There are several reasons that you may want to export and import data:

  * You want to upgrade or downgrade to a different [edition](/looker/docs/looker-core-instance-create#create_edition) of Looker (Google Cloud core).
  * You want to move to a Looker (Google Cloud core) instance in a different project.
  * You want to move to a Looker (Google Cloud core) instance in a different region.
  * You want to export data from a [non-production instance](/looker/docs/looker-core-overview#staging_environments_and_testing) to your production instance.

**Important:** Importing data into an existing Looker (Google Cloud core) instance overwrites any existing instance data.

## Required role

To get the permissions that you need to import or export Looker (Google Cloud core) instance data, ask your administrator to grant you the [Looker Admin ](https://cloud.google.com/iam/docs/understanding-roles#looker.admin) (`roles/looker.admin`) IAM role on the project in which the instance was created. For more information about granting roles, see [Manage access to projects, folders, and organizations](/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](/iam/docs/creating-custom-roles) or other [predefined roles](/iam/docs/understanding-roles). 

## Exporting your Looker (Google Cloud core) instance data to a Cloud Storage bucket

The following sections explain how to export your instance data.

### Required objects and permissions for exporting to a Cloud Storage bucket

**Note:** If you are exporting data using the Google Cloud console, you don't need to grant the following permissions manually — they will be granted automatically.

  * A [Looker service account](/looker/docs/looker-core-service-account). If you used the Google Cloud CLI CLI, Terraform, or the API to create your Looker (Google Cloud core) instance, and you have not yet created a Looker service account, you will need to [create one](/looker/docs/looker-core-instance-create#service_account).
  * A [Cloud Storage bucket](/storage/docs/creating-buckets) with the [`storage.objects.create` permission](/storage/docs/access-control/iam-permissions) assigned to the Looker service account. The Storage Object Creator (`roles/storage.objectCreator`) [IAM role](/storage/docs/access-control/iam-roles) includes this permission, so you can alternatively assign that role to the Looker service account.
  * A [customer-managed encryption key (CMEK)](/kms/docs/create-key). This CMEK is specific to the export and import process and is different from a CMEK used for encrypting your instance data. The CMEK `cloudkms.cryptoKeyVersions.useToEncrypt` permission must be assigned to the Looker service account. The [Cloud KMS CryptoKey Encrypter (`roles/cloudkms.cryptoKeyEncrypter`)](/iam/docs/understanding-roles#cloudkms.cryptoKeyDecrypter) role includes this permission, so you can alternatively assign that role to the Looker service account.

### Exporting to a Cloud Storage bucket

To export your data, select one of the following options:

### console

  1. Go to the Looker page in the Google Cloud console.

[ Go to Looker instances](https://console.cloud.google.com/looker/instances?mods=monitoring_api_prod)

  2. On the **Select organization** drop-down list at the top of the page, select the organization resource that includes the Looker (Google Cloud core) instance for which you want to export data.

  3. Click the name of the instance for which you want to export data.

  4. Click **Export**.

  5. In the **Export Bucket** field, specify the bucket location where you want the export artifact to be created. You can either enter the path in the input field as `<bucket_name>/<folder_name>` or browse to select the appropriate location in the bucket.

  6. In the **Select a customer-managed key** field, select the CMEK to be used for encrypting the export artifact.

  7. Click **EXPORT**.

### gcloud
    
    
    gcloud looker instances export INSTANCE_NAME \
    --target-gcs-uri='gs://BUCKET_NAME/FOLDER_NAME' \
    --kms-key=KMS_KEY_ID
    

Replace the following:

  * `INSTANCE_NAME`: a name for your Looker (Google Cloud core) instance; it is not associated with the instance URL
  * `BUCKET_NAME`: the Cloud Storage bucket location where you want the export artifact to be created
  * `FOLDER_NAME`: the folder you want the export artifact to be placed in within the Cloud Storage bucket
  * `KMS_KEY_ID`: the [full path](/kms/docs/getting-resource-ids#getting_the_id_for_a_key_and_version) to the import- and export-specific CMEK key ID

**Caution:** Your instance will be unavailable during the export process. The export process takes minutes to hours, depending on the size of the instance.

## Importing your data from a Cloud Storage bucket to a Looker (Google Cloud core) instance

The following sections explain how to import your instance data.

### Required permissions for importing from a Cloud Storage bucket

**Note:** If you are importing data using the Google Cloud console, you don't need to grant the following permissions manually — they will be granted automatically.

  * A [Looker service account](/looker/docs/looker-core-instance-create#service_account). If you used the Google Cloud CLI, Terraform, or the API to create your Looker (Google Cloud core) instance, and you have not already created a Looker service account, you will need to [create one](/looker/docs/looker-core-instance-create#service_account).
  * Grant the `storage.objects.get` permission to the Looker service account. The Storage Object Viewer (`roles/storage.objectViewer`) IAM role includes this permission, so you can alternatively assign that role to the Looker service account.
  * The `cloudkms.cryptoKeyVersions.useToDecrypt` permission must be assigned to the Looker service account. The [Cloud KMS CryptoKey Decrypter (`roles/cloudkms.cryptoKeyDecrypter`)](/iam/docs/understanding-roles#cloudkms.cryptoKeyDecrypter) role includes this permission, so you can alternatively assign that role to the Looker service account.

**Note:** If you [created your Looker (Google Cloud core) instance using a CMEK](/looker/docs/looker-core-cmek#workflow_for_creating_a_instance_with_cmek), the import operation must have access to that CMEK and the key version. When you're migrating between two different Google Cloud regions, the import process may need to access a CMEK in a KMS server in a region different from the target region. If the region that hosts the KMS server is unavailable, for example, in the case of a natural disaster, the import process will fail.

### Importing from a Cloud Storage bucket

To import your data, select one of the following options:

### console

  1. Go to the Looker page in the Google Cloud console.

[ Go to Looker instances](https://console.cloud.google.com/looker/instances?mods=monitoring_api_prod)

  2. On the **Select organization** drop-down list at the top of the page, select the organization resource that includes the Looker (Google Cloud core) instance where you want to import data.

  3. Click the name of the instance where you want to import data.

  4. Click **IMPORT**.

  5. In the **Import Bucket** field, either enter the path or browse to the Cloud Storage location where you exported your data. Select the folder containing the `metadata.json` file and other files.

  6. Click **IMPORT**.

### gcloud
    
    
    gcloud looker instances import INSTANCE_NAME \
    --source-gcs-uri='gs://BUCKET_NAME/FOLDER_NAME'
    

Replace the following:

  * `INSTANCE_NAME`: a name for your Looker (Google Cloud core) instance; it is not associated with the instance URL
  * `BUCKET_NAME`: the Cloud Storage bucket location where the `metadata.json` file and other files are located
  * `FOLDER_NAME`: the folder in which the `metadata.json` file and other files are located

After an import, Looker (Google Cloud core) users will be prompted to re-authenticate to any [BigQuery](/looker/docs/db-config-google-bigquery#authentication_with_oauth) or [Snowflake](/looker/docs/db-config-snowflake#configuring-a-snowflake-database-for-oauth-with) database connections that use OAuth for individual user authentication. That is because a Looker (Google Cloud core) export doesn't retain OAuth access or refresh tokens for individual users' database connections.

Users can re-authenticate to their databases with one of the following methods:

  * Follow the **Log in** prompt that appears when they view an Explore or a dashboard that uses an individual OAuth database connection.
  * Go to their [Account](/looker/docs/user-account) page and select **Log in** for each of the databases under the **OAuth Connection Credentials** heading.

Any automated schedules or alerts that are owned by a single user and that reference an OAuth connection will break until that user logs in with their OAuth credentials.

**Note:** If, while you're attempting to import instance data into a new instance, the import fails, the instance is reset to an ACTIVE state rather than remaining in an IMPORTING or ERROR state. This is so the instance can still be accessed, and, for example, deleted if necessary.

## Troubleshooting the export or import of Looker (Google Cloud core) data

This section describes how to remediate error conditions that could cause an export or import process to fail.

### Errors during export

  * Ensure that you have granted the Looker service account the `storage.objects.create` permission or the Storage Object Creator (`roles/storage.objectCreator`) IAM role to the [Cloud Storage bucket](/storage/docs/creating-buckets).

  * Ensure that you have granted the Looker service account the `cloudkms.cryptoKeyVersions.useToEncrypt` permission or the [Cloud KMS CryptoKey Encrypter (`roles/cloudkms.cryptoKeyEncrypter`)](/iam/docs/understanding-roles#cloudkms.cryptoKeyDecrypter) role to the [Customer-managed encryption key (CMEK)](/kms/docs/create-key) that you created.

  * Ensure that the given [Cloud Storage location](/storage/docs/creating-buckets) doesn't have any files from a previous export operation in it before you export your data. If there are any pre-existing files, remove them first.

  * You cannot use a Cloud Storage bucket that has [Requester Pays](/storage/docs/requester-pays) enabled.

### Import errors

  * Ensure that you have granted the Looker service account the `storage.objects.get` permission or the Storage Object Viewer (`roles/storage.objectViewer`) IAM role to the [Cloud Storage bucket](/storage/docs/creating-buckets).

  * Ensure that you have granted the Looker service account the `cloudkms.cryptoKeyVersions.useToDecrypt` permission or the [Cloud KMS CryptoKey Decrypter (`roles/cloudkms.cryptoKeyDecrypter`)](/iam/docs/understanding-roles#cloudkms.cryptoKeyDecrypter) role to the [Customer-managed encryption key (CMEK)](/kms/docs/create-key) that you created.

  * Importing can fail due to version incompatibility between the target instance and the export instance, as follows:

    * The target instance has a Looker minor version that is less than the Looker version of exported data. For example, the target instance is on Looker 23.5.X, but the export was created from an instance on Looker version 23.6.X.
    * The minor version of the instance that created the export data is behind the Looker version of the target instance by more than one release. For example, the target instance is on Looker 23.6.X, but the export was created from an instance on Looker version 23.4.X.

In this case, upgrade either the export instance or the target instance so that both instances are running the same Looker version.