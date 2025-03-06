# https://cloud.google.com/looker/docs/looker-core-qs-overview

Depth: 3

This page links to a series of quickstart guides that were created to walk you through the different steps you need to get started using Looker (Google Cloud core), from creating an instance to creating and sharing dashboards with rich visualizations.

## Looker (Google Cloud core) instance setup quickstarts

The following quickstart walks you through the steps required to set up a Looker (Google Cloud core) instance:

  * [Create a Looker (Google Cloud core) public IP standard edition instance](/looker/docs/looker-core-quickstart-public-ip-standard-edition)

## Looker (Google Cloud core) onboarding quickstarts

Once you have a Looker (Google Cloud core) instance, you can use the series of onboarding quickstarts to learn how to get started using Looker (Google Cloud core).

To get you up and running quickly, most of these quickstarts use the [sample LookML project](/looker/docs/looker-core-sample-project) that is already configured on Looker (Google Cloud core) instances. The quickstarts walk you through common Looker procedures using the sample LookML project. Once you are familiar with the procedures, you can apply the steps to your own data connections and datasets.

The following quickstarts are shown in the order that is generally required to set up and use a Looker instance from scratch. But because the quickstarts use the sample LookML project that is already configured on a Looker (Google Cloud core) instance, you can do these quickstarts independently of each other, in whatever order you prefer:

  1. [Create a connection for a public IP instance](/looker/docs/looker-core-qs-create-connection) — Learn how to create a database connection for a Looker (Google Cloud core) public IP instance to use as the basis for any LookML project, or for a specific LookML project.
  2. [Generate a model from sample data](/looker/docs/looker-core-qs-model-generation) — Learn how to use Looker (Google Cloud core) to automatically generate a basic data model from a connection that is included in each instance.
  3. [Model your data](/looker/docs/looker-core-qs-model-data) — Learn how to manually create LookML files and fields and how to test your updates in the Looker Explore UI.
  4. [Build a dashboard with sample data](/looker/docs/looker-core-create-dashboard-quickstart) — Learn how to create a dashboard with sample data from the **Intermediate Ecommerce** Explore in the sample LookML project on your Looker (Google Cloud core) instance.
  5. [Build a Look with sample data](/looker/docs/looker-core-create-look-quickstart) — Learn how to query and visualize data in Looker and to save your query results as a [Look](/looker/docs/saving-and-editing-looks) that you can share and reuse.

**Tip:** Some of the procedures in these quickstarts are included in the [Looker Onboarding Webinar: Looker Basics for New Customers](https://cloudonair.withgoogle.com/events/bi-onboarding). You can watch the webinar to see the procedures in action.

### Required permissions for onboarding quickstarts

Each of the onboarding quickstarts requires specific Looker permissions to complete. These permissions are summarized in the following table:

Quickstart name | Required Looker permissions  
---|---  
[Create a connection for a public IP instance](/looker/docs/looker-core-qs-create-connection) | [`manage_project_connections`](/looker/docs/admin-panel-users-roles#manage_project_connections)  
[[Generate a model from sample data](/looker/docs/looker-core-qs-model-generation)](/looker/docs/looker-core-qs-model-generation) | [`develop`](/looker/docs/admin-panel-users-roles#develop)  
[Model your data](/looker/docs/looker-core-qs-model-data) | [`develop`](/looker/docs/admin-panel-users-roles#develop)  
[Build a dashboard with sample data](/looker/docs/looker-core-create-dashboard-quickstart) | 

  * [`access_data`](/looker/docs/admin-panel-users-roles#access_data)
  * [`explore`](/looker/docs/admin-panel-users-roles#explore)
  * [`see_user_dashboards`](/looker/docs/admin-panel-users-roles#see_user_dashboards)
  * [`save_dashboards`](/looker/docs/admin-panel-users-roles#save_dashboards)
  * [`save_looks`](/looker/docs/admin-panel-users-roles#save_looks)
  * [`create_table_calculations`](/looker/docs/admin-panel-users-roles#create_table_calculations)

  
[Build a Look with sample data](/looker/docs/looker-core-create-look-quickstart) | 

  * [`access_data`](/looker/docs/admin-panel-users-roles#access_data)
  * [`explore`](/looker/docs/admin-panel-users-roles#explore)
  * [`save_looks`](/looker/docs/admin-panel-users-roles#save_looks)
  * [`see_looks`](/looker/docs/admin-panel-users-roles#see_looks)

  
  
## Related resources

  * Explore Looker training resources in the [Google Cloud Skills Boost portal](https://www.cloudskillsboost.google/catalog)