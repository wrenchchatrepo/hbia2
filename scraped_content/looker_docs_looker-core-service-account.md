# https://cloud.google.com/looker/docs/looker-core-service-account

Depth: 3

Looker (Google Cloud core) uses a [service agent](/iam/docs/service-account-types#service-agents), called a _Looker service account_ , to perform certain activities. A single Looker service account works on behalf of all Looker (Google Cloud core) instances in a given Google Cloud project. The Looker service account is automatically created the first time a Looker (Google Cloud core) instance is created in a project.

The service account allows Looker (Google Cloud core) to connect to other services, such as [BigQuery](/looker/docs/looker-core-dialects#using-application-default-credentials-to-connect-to-a).

Sometimes, such as when you're using [Application Default Credentials (ADC) with a connection to BigQuery in another project](/looker/docs/looker-core-dialects#adc-different-project), you need to view information about the Looker service account, such as its email address.

Or, if you are planning to use [CMEK](/looker/docs/looker-core-cmek) and are going to use the Google Cloud CLI, Terraform, or the API to configure CMEK before you create the Looker (Google Cloud core) instance, you must create the Looker service account manually _before_ you create the instance.

**Note:** You need to manually create a Looker service account only if you use the Google Cloud CLI, Terraform, or the API to configure CMEK and a Looker service account hasn't already been created for your project.

To view or create the Looker service account, select one of the following options:

### console

To view the Looker service account:

  1. In the Google Cloud console, go to the **IAM** page.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)
  2. Select the project that the Looker (Google Cloud core) instance resides in.
  3. Select the **Include Google-provided role grants** checkbox.

###  gcloud 

To create or view the Looker service account:
    
    
    
    gcloud beta services identity create --service=looker.googleapis.com --project=PROJECT_ID
    
    

Replace `PROJECT_ID` with the project that the Looker (Google Cloud core) instance resides in.

The service account name will be `Looker Service Account`. The email will have the format `service-<project number>@gcp-sa-looker.iam.gserviceaccount.com`.