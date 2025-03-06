# https://cloud.google.com/looker/docs/powerbi-connector

Depth: 3

The Looker–Power BI Connector lets you use Microsoft Power BI Desktop to connect to data from a Looker [Explore](/looker/docs/lookml-terms-and-concepts#explore).

## Setting up Power BI Desktop to connect to Looker

The general steps to use the Looker–Power BI Connector are as follows:

  1. Verify the requirements.
  2. Enable the connector on your Looker instance.
  3. Download and save the connector file: Each user who wants to access the Looker–Power BI Connector must download the `looker_1.4.0.mez` file and save it in a specific directory on their computer.
  4. Set up Power BI Desktop for a custom connector: Each Power BI user must configure their Power BI Desktop security settings to use a non-certified custom connector.

The sections on this page describe these steps in detail.

After you complete the steps to connect Looker with Power BI Desktop, you can [connect to Looker data from Power BI](/looker/docs/powerbi-connector#connecting_to_looker_data_from_power_bi_desktop) and publish reports in Power BI. You can optionally use Power BI service (Power BI online) to interact with your Looker reports in a web browser. You can also publish reports with Power BI service using row-level security.

**Note:** The `looker_1.4.0.mez` is a Looker product. If you have any questions or need assistance, contact [Looker Support](/looker/docs/best-practices/looker-support-details).

### Requirements

To set up the Looker–Power BI Connector, you need the following:

  * Microsoft Power BI Desktop installed on your computer.
  * A Looker instance that meets the following requirements: 
    * The instance must be hosted by Looker. (Looker (Google Cloud core) instances are hosted by Looker and support the Looker–Power BI Connector.)
    * The instance must be running Looker 23.10 or later.
  * A Looker user account on the Looker instance with the [`explore`](/looker/docs/admin-panel-users-roles#explore) permission, which is required to access Explores in Looker. If you want to work with queries with more than 5,000 rows, you also need the [`download_without_limit`](/looker/docs/admin-panel-users-roles#download_without_limit) permission (see Query row limits for information on downloading limits).

### Enable the connector on your Looker instance

The Looker instance you want to use with the Looker–Power BI Connector must be enabled for the **Microsoft Power BI** connector:

  * For [Looker (Google Cloud core)](/looker/docs/looker-core-overview) instances, BI connectors are enabled by default.
  * For Looker (original) instances, BI connectors are disabled by default.

Your Looker admin can enable BI connectors on the [BI Connectors panel](/looker/docs/bi-connectors) in the **Platform** section of the Looker **Admin** menu.

### Download and save the connector file

To download the connector file, follow these steps on the computer with Microsoft Power BI Desktop installed:

  1. To download the connector file, click the following link: [`looker_1.4.0.mez`](/looker/docs/file-downloads/looker_1.4.0.mez)
  2. When the download is completed, move the `looker_1.4.0.mez` file to the directory **[Documents]\Microsoft Power BI Desktop\Custom Connectors**. (Create the folders on your computer if they don't already exist.)

**Note:** If you were participating in the Looker–Power BI Connector Private Preview, once your instance is updated to Looker 23.10 or later, you need to download the `looker_1.4.0.mez` file and replace the earlier version of the `.mez` file that was supported for the Private Preview. The `looker_1.4.0.mez` file has improvements and bug fixes that the Private Preview version does not have.

### Setting up Power BI Desktop for a custom connector

To set up the Looker–Power BI Connector on the Power BI Desktop side, follow the [Custom connectors](https://docs.microsoft.com/en-us/power-bi/connect-data/desktop-connector-extensibility#custom-connectors) instructions on the Microsoft Power BI website.

As it says in the instructions, under **Data Extensions** , you will select the option **(Not Recommended) Allow any extension to load without validation or warning**. Select **OK** , and then restart the Power BI Desktop.

## Connecting to Looker data from Power BI Desktop

Once you have downloaded the `looker_1.4.0.mez` connector file and set up your Power BI Desktop application for a custom connector, you can use Power BI Desktop to connect to data from your Looker instance:

  1. From the Power BI Desktop toolbar, select **Get Data > More...**
  2. In the **Get Data** dialog, enter **Looker** in the search field.
  3. In the search results, click the **Looker** entry, and then click **Connect**.
  4. In the **Connecting to a third-party service** dialog, click **Continue**.
  5. Power BI Desktop will display a Looker sign-in dialog. In the **Host** field, type in the URL of your instance. For example: `example.cloud.looker.com`.
  6. Optionally, use the **Disable Preview Optimization** drop-down to disable the Preview Optimization feature.
  7. Optionally, use the **Show Hidden Fields** drop-down to include fields that configured in LookML as [hidden](/looker/docs/reference/param-field-hidden):

     * **FALSE** (default): Hidden fields are suppressed.
     * **TRUE** : Hidden fields are shown.
  8. Select the **DirectQuery** option to create a live connection to your data on Looker.

**Note:** The Looker–Power BI Connector is designed to be used with the **DirectQuery** option. If you select the **Import** option, Power BI will run a query that includes all fields from all the views that are referenced in the Looker Explore, which could be a very large query. In addition, with the **Import** option, Looker cannot correctly evaluate the [measures](/looker/docs/glossary#measure) used in the Explore.
  9. Click **OK**.

  10. In the **Looker** dialog, click **Sign in**.

  11. In the Looker login screen, sign in to your Looker instance.

  12. Power BI Desktop will return to the Looker sign-in dialog, with a message that says that you are signed in. Click **Connect**.

  13. Power BI Desktop will display a list of the Looker models that you have access to, each represented as a folder. Click the Looker model that you want to access, and then select the checkbox next to the Looker Explore that you want to load in Power BI Desktop. To see a model, you must have Looker user access or group access to a [model set](/looker/docs/admin-panel-users-roles#model-sets) that contains the model. To access Explores, you must have the Looker [`explore`](/looker/docs/admin-panel-users-roles#explore) permission.

  14. Click **Load**.

Power BI Desktop will populate its **Data** pane with the fields from your selected Explore. You can then use the Looker data from the Explore to create reports in Power BI Desktop. See Viewing Looker elements in Power BI Desktop for information on how Looker elements are displayed by the Looker–Power BI Connector.

Field names will appear in a single list in the format `ViewName.FieldName`.

### Preview Optimization

Power BI Desktop typically runs a preview query that returns the first 200 rows of your data (the preview is basically a `SELECT * LIMIT 200` query). For a Looker Explore, this can be a very large query, because Looker Explores can involve many joins and hundreds of fields. Although the `LIMIT 200` argument constrains the results of the preview query to 200 rows, the preview query initiates a full table scan on your database.

The Looker–Power BI Connector uses the **Preview Optimization** feature to prevent Power BI Desktop from running a preview query when it connects to your Looker Explore. When the **Preview Optimization** feature is enabled (the default), the Looker–Power BI Connector disables Power BI Desktop's preview query, so Power BI Desktop will return an empty table for the preview query. If you want Power BI Desktop to run preview queries on your Looker Explore, you can disable the **Preview Optimization** feature.

To enable Power BI Desktop's preview queries, set the **Disable Preview Optimization** value to **TRUE** when you connect to Looker data from Power BI Desktop.

## Viewing Looker elements in Power BI Desktop

After you connect to Looker data from Power BI Desktop, Power BI Desktop will populate its **Data** pane with the fields from your selected Explore.

The Looker–Power BI Connector uses the following format to display Looker fields in Power BI Desktop:

`ViewName.FieldType.FieldName`

  * The `ViewName` value is the LookML [view](/looker/docs/lookml-terms-and-concepts#view) where the field is defined.
  * The `FieldType` value can be one of the following types that are supported by the Looker–Power BI Connector:

    * `dim`: Dimension, a field that represents an attribute, a fact, or a value, such as dates, names, and IDs. Dimensions often correspond to columns in your underlying data table. In LookML, dimensions are defined with the [`dimension`](/looker/docs/reference/param-field-dimension) parameter.
    * `mea`: Measure, a field that represents measurable information about your data, such as sums, counts, averages, minimums, and maximums. In LookML, measures are defined with the [`measure`](/looker/docs/reference/param-field-measure) parameter.
    * `fil`: Filter, a filter-only field that is used only to create a filter in an Explore query; filter fields are not included in a query's result set. In LookML, filters are defined with the [`filter`](/looker/docs/reference/param-field-filter) parameter.
    * `par`: Parameter, a field that is used only to create a filter in an Explore query; parameter fields are not included in a query's result set. A parameter can create interactive query results, labels, URLs, and more when it is defined with the `{% parameter parameter_name %}` and `parameter_name._parameter_value` Liquid variables. In LookML, parameters are defined with the [`parameter`](/looker/docs/reference/param-field-parameter) parameter.
  * The `FieldName` value is the name of the field as it is displayed in the Looker Explore.

Power BI Desktop displays Looker elements just as they are displayed in the Looker Explore, with the same capitalization and word spacing. For example, if a Looker Explore displays a LookML dimension as `Created Date` from a view displayed as `Order Items`, Power BI Desktop will display this field as `Order Items.dim.Created Date`.

## Creating queries with Looker dimensions and measures

The Looker–Power BI Connector lets you use Looker [dimensions and measures](/looker/docs/lookml-terms-and-concepts#dimension_and_measure_fields) to create queries in Power BI Desktop.

**Note:** In the **Data** pane, Looker dimension names include `dim`, and Looker measure names include `mea` (see Viewing Looker elements in Power BI Desktop for details about how Power BI displays Looker elements).

To create a query in Power BI Desktop using Looker dimensions and measures, follow these steps:

  1. Connect to Looker data from Power BI Desktop, and wait for Power BI to populate its **Data** pane with the fields from your selected Looker Explore.
  2. In the Power BI **Data** pane, select the checkbox for each Looker dimension or measure that you want to include in the query.

As you select each dimension or measure, Power BI will update the query that is displayed in the report canvas.

## Filtering queries with Looker filters and parameters

The Looker–Power BI Connector lets you use LookML [parameters](/looker/docs/reference/param-field-parameter) and [filter-only fields](/looker/docs/reference/param-field-filter) from a Looker Explore to add filters to your Power BI report.

**Note:** In the **Data** pane, Looker filter-only field names include `fil`, and Looker parameter names include `par` (see Viewing Looker elements in Power BI Desktop for details about how Power BI displays Looker elements).

To filter a report in Power BI Desktop using Looker parameters and filter-only fields, follow these steps:

  1. If you haven't already, connect to Looker data from Power BI Desktop and wait for Power BI to populate its **Data** pane with the fields from your selected Looker Explore.

  2. In the Power BI **Data** pane, drag the name of a parameter or a filter-only field into one of the **Add data fields here** boxes in **Filters** pane, either for **Filters on this page** or for **Filters on all pages**. See the [Power BI documentation](https://learn.microsoft.com/en-us/power-bi/create-reports/power-bi-report-add-filter?tabs=powerbi-desktop) for details on adding filters to a report in Power BI.

Note the following about using Looker parameters and filter-only fields in Power BI:

  * For filter-only fields that are configured in LookML with the [`suggestions`](/looker/docs/reference/param-field-suggestions) parameter or the [`suggest_dimension`](/looker/docs/reference/param-field-suggest-dimension) parameter, Power BI will fetch the suggestion values and display them in the **Basic filtering** options in the **Filters** pane.
  * For parameters that are configured in LookML with the [`allowed_value`](/looker/docs/reference/param-field-parameter#specifying_allowed_values) attribute, Power BI will fetch all of the allowed values that are configured in LookML for the parameter and display them in the **Basic filtering** options in the **Filters** pane.

**Note:** LookML parameters support only one allowed value, so be sure to select only one of the allowed values that Power BI displays in the **Basic filtering** options.

## Monitoring the Looker–Power BI Connector

A Looker admin can view Looker–Power BI Connector usage using the **Query API Client Properties** group of fields in the [System Activity History Explore](/looker/docs/usage-reports-with-system-activity-explores#history). An entry is created in the **History** Explore every time a new query is run.

In the **Query API Client Properties** group of fields, the **API Client Name** shows a `Power BI` value to identify Looker–Power BI Connector entries.

The following is an example of a System Activity URL that shows Power BI usage. Replace `<instance_name.looker.com>` with your instance URL.
    
    
    https://<instance_name.looker.com>/explore/system__activity/history?fields=query_api_client_context.name,user.name,history.created_date,history.created_time_of_day&f[query_api_client_context.name]=Power+BI&sorts=history.created_time_of_day+desc&limit=5000
    

## Power BI service

After you [connect to Looker data from Power BI](/looker/docs/powerbi-connector#connecting_to_looker_data_from_power_bi_desktop) and publish reports in Power BI, you can optionally use [Power BI service](https://learn.microsoft.com/en-us/power-bi/fundamentals/power-bi-service-overview) (Power BI online) to interact with your Looker reports in a web browser.

You can also publish reports with Power BI service using row-level security.

**Note:** The Looker–Power BI Connector is a Looker product. If you have any questions or need assistance, contact [Looker Support](/looker/docs/best-practices/looker-support-details).

### Publishing a report with Power BI service using row-level security

After you have published reports in Power BI Desktop using the Looker–Power BI Connector, you can optionally use Power BI service to interact with the reports from a web browser.

Power BI Desktop lets you use [row-level security (RLS)](https://learn.microsoft.com/en-us/power-bi/enterprise/service-admin-rls) to restrict data access for certain users. See the Power BI documentation for the procedures for [defining roles and rules](https://learn.microsoft.com/en-us/power-bi/enterprise/service-admin-rls#define-roles-and-rules-in-power-bi-desktop) and [validating the roles](https://learn.microsoft.com/en-us/power-bi/enterprise/service-admin-rls#validating-the-role-within-the-power-bi-service) within Power BI Desktop.

Once you define the roles in Power BI Desktop, you can use the roles and rules online with Power BI service.

To publish a report with Power BI service using row-level security, follow these steps:

  1. In Power BI Desktop, open your report and select the **Home** menu from the top of the window.
  2. Select the **Publish** option from the **Home** menu.
  3. Select a workspace from the drop-down menu, and then click **Select**. Power BI Desktop shows a success message that includes a link to open the report in Power BI.
  4. Click the link to open Power BI.
  5. In Power BI service, go to **Workspaces** and select the workspace where you published the report.
  6. Find the listing for your report's dataset (not the report itself).
  7. In the dataset's listing, click the three-dot **More options** menu, and then select **Security**.

Power BI will show the **Row-Level Security** window. From here, you can select the role that you created in Power BI Desktop and [add people or groups who belong to the role](https://learn.microsoft.com/en-us/power-bi/enterprise/service-admin-rls#working-with-members) and [validate your roles in Power BI service](https://learn.microsoft.com/en-us/power-bi/enterprise/service-admin-rls#validating-the-role-within-the-power-bi-service).

Now you can share the report with anyone you want, and they will see only the data that they are allowed to see, based on the roles that you created.

## Things to consider

### Query row limits

Queries from the Looker–Power BI Connector will automatically include a `LIMIT 5000` statement unless the Looker user account has the [`download_without_limit`](/looker/docs/admin-panel-users-roles#download_without_limit) permission. If the Looker user account has `download_without_limit`, queries from the Looker–Power BI Connector have no imposed query row limit.

### Explore filters

If the Looker Explore is defined with [`always_filter`](/looker/docs/reference/param-explore-always-filter) or [`conditionally_filter`](/looker/docs/reference/param-explore-conditionally-filter) LookML parameters, the filters will be applied to queries in the Looker–Power BI Connector, even though the filters won't be visible in Power BI.

### Supported dimension group timeframes

For the [`dimension_group`](/looker/docs/reference/param-field-dimension-group) of [`type: time`](/looker/docs/reference/param-field-dimension-group#type_time), only the [`date`](/looker/docs/reference/param-field-dimension-group#date) and [`time`](/looker/docs/reference/param-field-dimension-group#time_table) timeframes are supported with the Looker–Power BI Connector. Other timeframes will be hidden.

### Known limitations

The following are known limitations with the Looker–Power BI Connector:

  * Numeric dimensions and measures both render as measures (see [Dimension and measure fields](/looker/docs/lookml-terms-and-concepts#dimension_and_measure_fields) for a description of dimensions and measures). To use a numeric dimension as a dimension, you must first change it to [**Not Summarized**](https://learn.microsoft.com/en-us/power-bi/create-reports/service-aggregates#ways-to-aggregate-your-data) in Power BI Desktop.
  * To ensure optimal performance and functionality, use [DirectQuery Mode](https://learn.microsoft.com/en-us/power-bi/connect-data/service-dataset-modes-understand#directquery-mode) whenever possible. When using the Power BI [Import Mode](https://learn.microsoft.com/en-us/power-bi/connect-data/service-dataset-modes-understand#import-mode) with the Looker–Power BI Connector, be aware of the following limitations: 
    * Import Mode reports that attempt to access larger models may experience performance degradation.
    * If the Get Data process does not resolve or times out, switch to DirectQuery Mode to improve performance and reliability.
    * Don't use filter-only fields and parameter fields if you are using Import Mode, since these fields are disabled in Import Mode.
    * Import Mode does not allow Looker to correctly evaluate measures within the Explore. This limitation can impact the accuracy and functionality of your reports.
  * Power BI attempts to apply its own aggregations on Looker measures, this sometimes will lead to inconsistent results (especially if you are using [matrix visuals](https://learn.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-matrix-visual?tabs=powerbi-desktop)) or lead to aggregations not working due to a lack of equivalent mapping. 
    * Use only the following supported measures types in your Power BI reports: `average`, `count`, `count-distinct`, `max`, `min`, `sum`.
    * Querying for standard deviation and variance is not supported.
    * Querying for the first or last string alphabetically using the Power BI first/last aggregators is not supported.
    * In Power BI, the query for median is performed by pulling all values in the dataset and then calculating the median locally. This can be very slow on larger datasets and may time out.
  * Because of the inconsistencies with [Power Query](https://learn.microsoft.com/en-us/power-query/power-query-what-is-power-query) and [Looker filter expressions](/looker/docs/filter-expressions), be aware of the following advanced filters limitations: 
    * All text filters are supported.
    * Multiple text filters are not supported.
    * All number filters are supported.
    * Multiple number filters are supported only in the following cases: 
      * INEQUALITY AND INEQUALITY (for example, is less than AND is greater than).
      * INEQUALITY OR INEQUALITY (for example, is less than OR is greater than).
      * is OR is.
    * Only the following date/datetime filters are supported: `is`, `is not`, `is on or after`, `is before`.
    * Multiple date and datetimefilters are supported only in the following cases: 
      * `is on or after AND is before`
      * `is or is`
    * The following table functions are not foldable: 
      * `Table.Distinct`
      * `Table.Join`
      * `Table.NestedJoin`
      * `Table.Skip`

## Looker–Power BI Connector changelog

The following sections show the updates in each version of the Looker–Power BI Connector:

  * Version 1.4.0
  * Version 1.3.1
  * Version 1.3.0
  * Version 1.2.0

### Version 1.4.0

Version 1.4.0 of the Looker–Power BI Connector has the following updates:

  * Added support for Import Mode
  * Enabled data preview
  * Improved behavior when performing `SELECT *` queries
  * Improved Looker cache hit rate
  * Improved performance of filter suggestions retrieval

Version 1.4.0 of the Looker–Power BI Connector has the following bug fixes:

  * Fixed bug where Looker wouldn't detect that values had been passed for filter and parameter fields
  * Fixed bug where parameter suggested values would sometimes be missing from slicers
  * Fixed bug where Liquid variables would be ignored by LookML statements
  * Fixed bug where count distinct measure values would be inconsistent in Power BI matrix views

### Version 1.3.1

Click to expand section

Version 1.3.1 of the Looker–Power BI Connector has the following updates:

  * Added option to show hidden fields

Version 1.3.1 of the Looker–Power BI Connector has the following bug fix:

  * Fixed bug where a visual would fail if a filter exists on both the visual and report

### Version 1.3.0

Click to expand section

Version 1.3.0 of the Looker–Power BI Connector has the following updates:

  * Simplified datetime formatting
  * Improved detection on unsupported text expressions
  * Improved error message reporting

Version 1.3.0 of the Looker–Power BI Connector has the following bug fix:

  * Improved support for escape characters in filter values

### Version 1.2.0

Click to expand section

Version 1.2.0 of the Looker–Power BI Connector has the following updates:

  * Parameter and filter-only fields are now supported
  * Advanced filters support for filter-only fields of type text, number, date and datetime
  * Basic filter support for filter-only field utilizing Looker suggested values