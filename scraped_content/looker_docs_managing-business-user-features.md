# https://cloud.google.com/looker/docs/managing-business-user-features

Depth: 3

Many user-facing Looker features must either be enabled by a Looker admin or have Looker admin–specific or developer–specific prerequisites implemented before those features can be made available to Looker users. This page consolidates those user-facing features for easy admin reference.

## Finding content

The **Folders** section of the Looker main navigation menu includes two folders that are specific to Looker admins:

  * **Unused Content** : Shows all Looks and dashboards that haven't been viewed within a time range you select.
  * **Trash** : Shows Looks and dashboards that users have deleted and that you can recover.

For details about these pages, see the [Deleted and unused content for admins](/looker/docs/admin-spaces) documentation page.

## Creating content

This section includes admin-specific or developer-specific functionality and tips for creating dashboards, Looks, and Explores.

### Using custom fields

The **Custom Fields** feature is not a data security feature. Other users can see the custom fields in shared queries, Looks, and dashboard tiles. They also can use **Explore from Here** to create new queries with those fields.

Grant permission to create custom fields if you want to let some of your business users perform these tasks:

  * Visualize unmodeled data using Instant Explore from SQL Runner
  * Create semi-permanent measures and dimensions for a one-time or an infrequent analysis
  * Create semi-permanent measures and dimensions without the need of an analyst

#### Enabling custom fields

To enable custom fields, a Looker admin must grant the [`create_custom_fields`](/looker/docs/admin-panel-users-roles#create_table_calculations) permission to users or groups to allow access to the feature. The `create_custom_fields` permission is already part of several [default permission sets](/looker/docs/admin-panel-users-roles#default_permission_sets) that are included with Looker.

#### Custom fields and the LookML model

Although custom fields rely on the LookML model, they are not part of the modeling layer and do not appear in any view files. You cannot save or convert a custom field to a LookML field.

Consider using custom fields instead of LookML for fields that are only needed temporarily or only by your most sophisticated users.

#### You can create a custom field in SQL Runner

You can use custom fields to visualized unmodeled fields in SQL Runner, as described on the [Using SQL Runner to create queries and Explores](/looker/docs/sql-runner-create-queries-and-explores#creating_custom_fields_while_exploring_in_sql_runner) documentation page.

### Changing the field picker choices using LookML

To learn the various ways that a Looker developer can use LookML to create and modify the fields available in the field picker, see the [Changing the Explore menu and field picker](/looker/docs/changing-explore-menu-and-field-picker) page.

## Sharing content

This section includes admin-specific or developer-specific functionality and tips for delivering, downloading, and sharing content.

### Delivering content

This section includes admin-specific or developer-specific functionality and tips for [delivering](/looker/docs/scheduling) data.

#### JSON delivery and download formats

Looker uses the **JSON – Label** format when downloading Looks, Explores, and query tiles on dashboards.

Looker uses the **JSON – Simple** , **JSON – Label** , **JSON – Simple, Inline** , and **JSON – Detailed, Inline** formats when delivering Looks and Explores. The JSON formats available depend on the selected destination. The **JSON – Label** format option uses a dimension or measure's label from the data visualization as its rendered value in its JSON output. For example: `{"rendered_label":"rendered_value"}`

Other JSON format outputs render field names as follows:

**JSON – Label** : `{"rendered_label":"rendered_value"}` (uses label from data visualization)

**JSON – Simple** : `{"view.field_name":"rendered_value"}` (uses field name from data table)

**JSON – Simple, Inline** : `{"view.field_name":"rendered_value"}` (uses field name from data table)

**JSON – Detailed, Inline** : `{"view.field_name":"rendered_value"}` (uses field name from data table)

When delivering Looks and Explores, if **Apply visualization options** is selected, Looker will render any available JSON formats in the delivery as follows:

**JSON – Label** : `{"rendered_label":"rendered_value"}` (uses label from data visualization)

**JSON – Simple** : `{"rendered_label":"rendered_value"}` (uses label from data visualization)

**JSON – Simple, Inline** : `{"rendered_label":"rendered_value"}` (uses label from visualization)

**JSON – Detailed, Inline** : `{"view.field_name":"rendered_value"}` (uses field name from data table)

See this [Looker notice](https://community.looker.com/lookml-5/change-in-json-render-formatting-6-22-14465) for more information.

#### Managing sending and scheduling

In the **Admin** section of Looker, admins can use the **Scheduler Plans** and **Scheduler History** pages to look up and resolve schedule issues. Admins should be careful about deleting or disabling a user who may be the owner of important scheduled deliveries, because the schedules are also deleted or disabled.

See the [Configuring content deliveries](/looker/docs/configuring-deliveries) documentation page for more information about how Looker admins manage users' access to and use of Looker's content delivery capabilities.

#### Run schedule as recipient

This option, available for emailed content deliveries, exhibits behavior unique to the type of content being delivered. To learn more, see the appropriate documentation for each type of content:

  * [Delivering dashboards](/looker/docs/scheduling-and-sending-dashboards#run_schedule_as_recipient)
  * [Delivering Looks and Explores](/looker/docs/delivering-looks-explores#run_schedule_as_recipient)

#### Sending and scheduling data to destinations that support streamed results via action hub

Looker hosts and provides a stateless server, the Looker Action Hub, that implements Looker's Action API and exposes popular [integrations](/looker/docs/admin-panel-platform-actions#list_of_integrated_services) — also called _actions_.

With the Looker Action Hub, you can send and schedule data from within Looker to other SaaS tools automatically. Sending or scheduling data to destinations that support streaming or that use OAuth relies on synchronous queries running between Looker's Action Hub and executable server, or JAR, file. For Looker-hosted instances, these sources are configured to communicate.

**Note:** To use Looker integrations, the Looker Action Hub must be able to communicate with the Looker instance and fulfill these [Looker Action Hub requirements](/looker/docs/action-hub#looker_action_hub_requirements). Admins of customer-hosted instances may need to consider [additional factors](/looker/docs/action-hub#considerations_for_customer-hosted_instances) when choosing to enable Looker integrations from the Looker Action Hub, especially integrations that [support streamed results](/looker/docs/action-hub#uses_streaming) or that use [OAuth](/looker/docs/action-hub#configuring_an_action_for_oauth).

#### Storing SFTP fingerprints

Once you've connected to an SFTP server from Looker at least once to deliver or download data, Looker stores a fingerprint of that SFTP server.

All SFTP fingerprints are kept in the file `~/.ssh/known-hosts` on the Looker server.

If the fingerprint changes, this means that the server you are connecting to has changed the public key. This could indicate that the server was recreated or is behind a load balancer. It could also indicate that you are being targeted with a man-in-the-middle (MitM) attack, where the attacker is somehow intercepting or rerouting your SSH connection to connect to a different host, which could be stealing your credentials.

### Downloading content

This section includes admin-specific or developer-specific functionality and tips for [downloading](/looker/docs/downloading) content.

#### Downloading content from dashboard tiles without downloading permissions

Typically, a user requires a [role](/looker/docs/admin-panel-users-roles) that includes the `see_user_dashboards` and either the `download_with_limits` or the `download_without_limits` [permissions](/looker/docs/admin-panel-users-roles#permissions_list) to [view and download data](/looker/docs/viewing-dashboards#downloading_data_from_dashboard_tiles) from tiles on a dashboard. There is a condition, however, where a user can see and download data from a model to which they do not have those permissions. It occurs when the following is true:

  * A dashboard has tiles that are based on queries from more than one model.
  * A user is assigned one role that includes the [`see_user_dashboards`](/looker/docs/admin-panel-users-roles#see_user_dashboards) or [`see_lookml_dashboards`](/looker/docs/admin-panel-users-roles#see_lookml_dashboards) and either the [`download_with_limit`](/looker/docs/admin-panel-users-roles#download_with_limit) or [`download_without_limit`](/looker/docs/admin-panel-users-roles#download_without_limit) permissions to one of the models on which the dashboard is based.
  * The user has a second role that has only the `access_data` permission to another model on which the dashboard is based.

In this case, that user can view and download data from the entire dashboard, including tiles based on models to which the user does not have permissions to view or download data.

### Considerations for data formats or destinations

Some data formats have quirks to consider when you use Looker to deliver or download content.

#### Rendering emailed images

The **Easy to Read Email Images** feature lets the email client determine the optimal image size for images sent or scheduled in the body of emails. If images appear distorted when delivered by email, your users' email client may be incompatible with this feature.

#### Sending large files in Excel format

For downloads or deliveries of large Excel files (files over 5 GB), the download or delivery screen may appear to freeze, or you may be unable to open the delivered file. Here are some conditions that can cause this behavior, and how you might fix it:

  * Large Excel file data deliveries can time out while streaming. In this case, try sending or downloading your data in the CSV format, which you can then import into Excel.
  * Large Excel files sometimes are delivered successfully, but are too large to open locally. In this case, break your data delivery into smaller CSV files so that they will load successfully by the destination client.

#### Preventing injection of malicious code into CSV files

CSV files can contain macros that can run on Microsoft Excel or Google Sheets. Macros can be used to inject malicious code into CSV files, making CSV files a possible security risk.

To remove this risk, Looker admins can request a license update that causes Looker to pad any value in a cell that could be executable code. When this is enabled, Looker will add a `'` character to any cell value that begins with a special character (`=`, `-`, `+`, or `@`) when generating a CSV file. This disables all macros in Looker-generated CSV files.

To update your license for this feature, please [contact a Google Cloud sales specialist](https://cloud.google.com/contact) or [open a support request](http://console.cloud.google.com/support/cases).

#### Rendering image-based data formats for sending, scheduling, or downloading

Looker uses Chromium to render these formats for your deliveries and downloads:

  * For dashboards: PDF, Visualization (for sending and scheduling only)
  * For Looks: Visualization, HTML
  * For Explores (sending and downloading only): PNG (Image of Visualization), HTML

If your instance is Looker-hosted, Chromium is already installed.

If your instance is customer-hosted, you need to install the appropriate version of the [Chromium renderer](/looker/docs/installation-of-rendering-software#chromium).

> Downloading content in a rendered format may necessitate additional permissions considerations.

#### Downloading content in rendered format

Most types of downloads take into account the models associated with the user's download permissions when determining whether a user can download a piece of content. In some circumstances, users can view and download data from an entire dashboard, including tiles based on models that do not grant those users permissions to view or download data.

Downloads in rendered formats only require a download permission for any model associated with the content.

### Public sharing, importing, and embedding

To enable public access to Look URLs, including the ability to embed a Look, enable **Public URLs** on the **General Settings** page in the **Admin** section.

![](/static/looker/docs/images/admin-public-urls-2216.png)

Consider the security implications of this feature before enabling it. Although the URLs that Looker generates can't be guessed or searched, anyone with the URL can see the data. Anyone who receives the URL could share it with another person who was not intended to have access to your data. You should determine the privacy requirements of the data in question, evaluate your level of trust in anyone who receives a public URL, and clearly establish your expectations about whether — and, if so, how and with whom — it is to be shared.

## Retrieving and charting data

This section includes admin-specific or developer-specific functionality and tips for retrieving and charting data.

### Improving visualizations

For a list of Looker's native visualization types, see the [Visualization types](/looker/docs/visualization-types) documentation page. You can also install and administer [custom JavaScript visualizations](/looker/docs/admin-panel-platform-visualizations), add a [visualization parameter](/looker/docs/reference/param-manifest-visualization) to your LookML to surface in an Explore, or install visualizations from the [Looker Marketplace](/looker/docs/marketplace).

## Considerations for customer-hosted deployments

This section gives a quick list of features that have additional considerations for customer-hosted Looker deployments, with links to the relevant sections on this page.

  * Sending and scheduling data to streamed destinations can require different Looker Action Hub setup for customer-hosted instances.

  * Sending, scheduling, or downloading some data formats requires admins of customer-hosted deployments to install additional software to render those formats.