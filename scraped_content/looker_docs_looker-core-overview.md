# https://cloud.google.com/looker/docs/looker-core-overview

Depth: 3

Looker (Google Cloud core) provides simplified and streamlined provisioning, configuration, and management of a Looker instance from the Google Cloud console. Some instance administration tasks may also be performed from the console.

Looker (Google Cloud core) instances are hosted by Google in the Google Cloud. Looker (Google Cloud core) is not available for customer-hosted or multicloud environments.

## Looker (Google Cloud core) features

Most Looker (Google Cloud core) functionality is the same as [Looker (original) functionality](/looker/docs), with a few differences. Learn about Looker (Google Cloud core) features [compared to Looker (original)](/looker/docs/looker-core-feature-differences#core_original_features), and by [edition](/looker/docs/looker-core-edition-types) and [network connection](/looker/docs/looker-core-feature-differences#feature_compatibility_by_network_connection_type).

Functionality that is specific to Looker (Google Cloud core) is documented in the [Looker (Google Cloud core) documentation](/looker/docs/looker-core). Functionality that is shared between Looker (Google Cloud core) and Looker (original) is documented in the [Looker (original) documentation](/looker/docs).

## Looker (Google Cloud core) editions

Looker (Google Cloud core) is available in several editions. Each edition type offers different [functionality](/looker/docs/looker-core-edition-types) and has different [pricing](/looker/pricing). When you create a Looker (Google Cloud core) instance, you choose the edition that meets your needs. Edition type cannot be changed after instance creation. You can also provision, configure, and manage non-production instances of the same edition types for staging and testing. See the Staging environments and testing section on this page for things to know about setting up a non-production instance.

### Standard edition

The **Standard** edition is tailored for small teams and small or medium-sized businesses with up to 50 internal platform users. In addition to many existing Looker (Google Cloud core) features, the **Standard** edition brings new functionality, which includes the following:

  * [Google Cloud Identity access management](/iam/docs) and simplified BigQuery connectivity
  * Support for up to 1,000 Query-related Looker (Google Cloud core) [API calls](/looker/docs/reference/looker-api/latest) per month and 1,000 Admin-related Looker (Google Cloud core) API calls per month

A **Standard** edition can be purchased through an annual contract.

### Enterprise edition

The **Enterprise** edition includes all the features of the **Standard** edition as well as supporting:

  * Unlimited users
  * Additional security features such as [VPC-SC](/looker/docs/looker-core-vpcsc), [Private IP](/looker/docs/looker-core-create-private-ip), and [Private Service Connect](/looker/docs/looker-core-create-psc)
  * More robust monitoring through the [Elite System Activity](/looker/docs/elite-system-activity) feature
  * 100,000 Query-related Looker (Google Cloud core) [API calls](/looker/docs/reference/looker-api/latest) per month and 10,000 Admin-related Looker (Google Cloud core) API calls per month

An **Enterprise** edition can be purchased through an annual contract.

### Embed edition

The **Embed** edition includes all the features of the **Enterprise** edition as well as offering:

  * [Signed embedding](/looker/docs/single-sign-on-embedding)
  * A [private label](/looker/docs/privatelabel) option
  * [Custom themes](/looker/docs/themes-for-embedded-dashboards-and-explores)
  * 500,000 Query-related Looker (Google Cloud core) [API calls](/looker/docs/reference/looker-api/latest) per month and 100,000 Admin-related Looker (Google Cloud core) API calls per month

An **Embed** edition can be purchased through an annual contract.

**Note:** If you purchase an Embed Looker (Google Cloud core) edition, we recommend that you also purchase at least one non-production Embed instance for staging.

## Set up and administer the Looker (Google Cloud core) instance

Before you can explore data, you must create and configure a Looker (Google Cloud core) instance. The process for setting up a Looker (Google Cloud core) instance is as follows:

  1. [Ensure](/looker/docs/looker-core-instance-create#before_you_begin) that you have the proper Google Cloud console set up by checking the instance creation prerequisites.
  2. [Create](/looker/docs/looker-core-instance-create#create_a_instance) a Looker (Google Cloud core) instance.
  3. [Set up](/looker/docs/looker-core-dialects#set_up_a_database_connection) a database connection.
  4. [Write](/looker/docs/write-lookml-intro) LookML.
  5. [Add](/looker/docs/looker-core-user-management#adding-users) users.
  6. [Retrieve and chart](/looker/docs/retrieve-and-chart-data) data.
  7. Administer the instance [from the Google Cloud console](/looker/docs/looker-core-admin-console) and [from the Looker (Google Cloud core) instance](/looker/docs/looker-core-admin-looker).

**Note:** Users and Administrators of Looker (Google Cloud core) must align with any constraints put in place by their Organization in the Google Cloud console [Organization Policies page](/resource-manager/docs/organization-policy/creating-managing-policies). Looker (Google Cloud core) won't align itself to any Organization Policy constraint automatically. This applies to Organization Policy at the organizational, folder, and project level.

## Use the Google Cloud CLI

Throughout the Looker (Google Cloud core) documentation, there are instructions for using the Google Cloud CLI. [Install the gcloud CLI](/sdk/docs/install) to run gcloud CLI commands.

Additionally, refer to the [gcloud CLI reference documentation](/sdk/gcloud/reference/looker) for information about using these commands with Looker (Google Cloud core).

## Use Terraform

You can use Terraform to execute some Looker (Google Cloud core) administrative tasks. See the [Terraform on Google Cloud](/docs/terraform) documentation for more information about how to provision infrastructure on Google Cloud using Terraform. If you are provisioning resources through the [Terraform Google Cloud provider](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/looker_instance), use version 4.75.0+.

## Use the Looker (Google Cloud core) API

View the [Looker (Google Cloud core) Admin API reference](/looker/docs/reference/rest) for information on Looker (Google Cloud core) endpoints for Google Cloud console functionality.

View the [Looker API documentation](/looker/docs/api-intro) for information on using the API for functionality within a Looker (Google Cloud core) instance.

### Types of Looker (Google Cloud core) API calls

The types of API calls that are defined as **query API calls** are as follows:

  * Calls that are required for automated query pipelines
  * Calls that get data from the client database
  * Calls that run SQL queries or grab results for content

Examples include the following:

  * [Run Query](/looker/docs/reference/looker-api/latest/methods/Query/run_query)
  * [Run SQL Runner Query](/looker/docs/reference/looker-api/latest/methods/Query/run_sql_query)
  * [Create Dashboard Render Task](/looker/docs/reference/looker-api/latest/methods/RenderTask/create_dashboard_render_task)

The types of API calls that are defined as **admin API calls** are as follows:

  * Calls that are required to build applications, control content across instances, and perform administrative tasks
  * Calls that control the Looker (Google Cloud core) instance
  * Calls that perform content management, permission and user management, instance administration, or pulling content across folders

Examples include:

  * [Create Connection](/looker/docs/reference/looker-api/latest/methods/Connection/create_connection)
  * [Create User](/looker/docs/reference/looker-api/latest/methods/User/create_user)
  * [Search Folders](/looker/docs/reference/looker-api/latest/methods/Folder/search_folders).

There are also other types of API calls, which are ignored for metering purposes, that include calls that perform login, logout, and user authentication tasks.

## Release notes and process

Release notes for Looker (Google Cloud core) can be found on the [Looker release notes](/looker/docs/release-notes) page. To learn about the Looker (Google Cloud core) release process, visit the [Looker (Google Cloud core) release overview](/looker/docs/looker-core-release-process) documentation page.

## Pricing

See the [Looker (Google Cloud core) pricing](/looker/pricing) page for details about pricing.

## Staging environments and testing

If you're interested in using a staging instance, you can [create a new non-production instance](/looker/docs/looker-core-instance-create) by using the standard process for creating a Looker (Google Cloud core) instance, and selecting the appropriate non-production edition. The billing for this non-production instance will be the same as for any other Looker (Google Cloud core) instance. See the [Looker (Google Cloud core) pricing](/looker/pricing) page for more details.

The types of non-production instance editions are the same as the editions that are available for production instances, and include the following:

  * Standard edition
  * Enterprise edition
  * Embed edition

The functionalities that are available for each non-production edition are the same as the functionalities that are available for the production editions. Non-production Looker (Google Cloud core) instances also can have the same [network connection types](/looker/docs/looker-core-feature-differences#feature_compatibility_by_network_connection_type) as production instances. Having the same functionalities in all environments lets you configure your staging environment to match your production environment, and test updates before deploying to your production instance.

**Note:** If you purchase an Embed Looker (Google Cloud core) edition, we recommend that you also purchase at least one non-production Embed instance.

## Things to know about non-production Looker (Google Cloud core) instances

The following are things to know about non-production Looker (Google Cloud core) instances:

  * Non-production instances are not covered by any Google SLAs.
  * Horizontal scaling is not considered a non-production use case. If you need to spread instance load and offer specific geographical distribution across multiple Looker (Google Cloud core) instances for your production use case, you will need to purchase additional instances of the existing production Looker (Google Cloud core) edition.
  * Non-production Looker (Google Cloud core) instances cannot be used in lieu of a production instance or for production purposes.
  * All production and non-production Looker (Google Cloud core) instances adhere to the same release cycle. You can configure your non-production instance maintenance settings to match your [production instance maintenance settings](/looker/docs/looker-core-maintenance#maintenance_settings).

## Support

For support with your Looker (Google Cloud core) instance, see the [Getting support for Looker (Google Cloud core)](/looker/docs/looker-core-support) documentation page.

## What's next

  * [Looker (Google Cloud core) quickstart overview](/looker/docs/looker-core-qs-overview)
  * [Create a Looker (Google Cloud core) instance](/looker/docs/looker-core-instance-create)