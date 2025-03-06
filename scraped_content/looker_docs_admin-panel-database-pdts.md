# https://cloud.google.com/looker/docs/admin-panel-database-pdts

Depth: 3

The Looker **Persistent Derived Tables** admin page shows the status of the Looker instance's persisted tables (which include both [persistent derived tables](/looker/docs/derived-tables#persistent-derived-tables) and [aggregate tables](/looker/docs/aggregate_awareness#adding_aggregate_tables_to_your_project). 

The **Persistent Derived Tables** admin page displays several admin features that can help track and troubleshoot persisted table behavior. See the [Derived tables in Looker](/looker/docs/derived-tables#monitoring_and_troubleshooting_pdts) documentation page for information on troubleshooting persisted tables.

Looker admins and users with the [`see_pdts`](/looker/docs/admin-panel-users-roles#see_pdts) permission can access the **Persistent Derived Tables** page. 

**Note:** To access all the admin pages in Looker, you must have the [Admin role](/looker/docs/admin-panel-users-roles#default_roles). If you have a permission that enables only parts of the **Admin** panel, such as [`manage_schedules`](/looker/docs/admin-panel-users-roles#manage_schedules) or [`manage_themes`](/looker/docs/admin-panel-users-roles#manage_themes), but you don't have the Admin role, then Looker may not display the page or pages described in this article in the **Admin** panel. Also, the `see_admin` permission grants read-only permission to most (but not all) Admin pages. See the [`see_admin`](/looker/docs/admin-panel-users-roles#see_admin) description for more information.

To open the **Persistent Derived Tables** page, follow these steps:

  1. Click the Looker **Main menu** icon menu and select **Admin** , if the **Admin** menu isn't already displayed. (If you are in the **Explore** or **Develop** section of the Looker **Main menu** , you may have to click the back arrow to see the **Admin** menu.)
  2. From the **Admin** menu, select **Persistent Derived Tables**.

The **Persistent Derived Tables** page shows only the connections that [are enabled for PDTs](/looker/docs/connecting-to-your-db#persistent_derived_tables) and only the persisted tables that meet the following criteria:

  * The persisted table is defined in a view file that is in production, unless you are in [Development Mode](/looker/docs/dev-mode-prod-mode), in which case you can use the **Development** tab to see the development version of persisted tables.
  * The persisted table is part of a model that is correctly configured.
  * The persisted table is part of a model for which you have [data access](/looker/docs/access-control-and-permission-management#controlling_feature_and_data_access).

Information on this page is based on an internal PDT event log, described in the PDT Event Log Explore section on this page.

## Customizing the table

By default, the **Persistent Derived Tables** page displays a maximum of 25 persisted tables on the page and loads persisted tables for all connections for which you have [data access](/looker/docs/access-control-and-permission-management#controlling_feature_and_data_access) on the Looker instance. There are several ways you can change the data that is displayed in the table:

![](/static/looker/docs/images/admin-pdt-customize-2220.png)

  1. To view the persisted tables from a specific connection only, click the arrow next to **All Connections** , and then select the name of the specific connection. The selector shows only connections that [are enabled for PDTs](/looker/docs/connecting-to-your-db#persistent_derived_tables) and for which you have data access.
  2. Enter keywords in the search box to narrow the persisted table list to persisted tables whose names include the keyword. The table will show the persisted tables with the matching search term in bold. Click the **X** in the search bar to clear your search query terms.
  3. Click the **Filters** icon to define a filter for the table.
  4. Click the close/open icon to display or hide the **At a Glance** section.
  5. Click the name of a column to sort the table by that column. Click the column name a second time to reverse the sort order.
  6. Click the **Select columns to display** icon to hide or display columns in the table.
  7. Use the display selector to choose the number of results that are displayed on a single page. If the table is longer than a single page, you can click the arrows at the bottom center of the page to navigate to the next or previous page.

### Filtering

You can use the **Filters** icon next to the search bar to choose which persisted tables are shown on the **Persistent Derived Tables** page. For example, you can filter by **Last Build Status** to view only the persisted tables that are experiencing a build error, or you can filter by **Model** to limit the persisted tables that are shown to a specific model.

To filter the **Persistent Derived Tables** page, follow these steps:

  1. Click the **Filters** icon filter_list.
  2. Select a filter option from the first filter selector in the filter menu. The following options are available: 
     * **Not Triggered in the Last** : Filters the **Persistent Derived Tables** page by persisted tables that have not been triggered in a specified number of hours and minutes.
     * **Triggered in the Last** : Filters the **Persistent Derived Tables** page by persisted tables that have been triggered in a specified number of hours and minutes.
     * **Model** : Filters the **Persistent Derived Tables** page for persisted tables that are included in a specified model.
     * **Persistence Rule** : Filters the **Persistent Derived Tables** page by persistence type.
     * **Last Attempt Status** : Filters the **Persistent Derived Tables** page by a specified persisted table status.
     * **Published as Stable View** : A Boolean that filters the **Persistent Derived Tables** page for persisted tables and displays **Yes** for persisted tables that were published as a stable view, and **No** for persisted tables that were not published as a stable view, as determined by their [`publish_as_db_view`](/looker/docs/reference/param-view-publish-as-db-view) parameter value.
     * **Last Build Duration Longer Than** : Filters the **Persistent Derived Tables** page by persisted tables whose builds took longer than a specified number of seconds.
     * **Project** : Filters the **Persistent Derived Tables** page by persisted tables from the specified LookML project.
  3. Choose the value on which you want to filter the **Persistent Derived Tables** page in the second filter selector. For the **Not Triggered in the Last** or **Triggered in the Last** options, enter a number of hours or minutes. For the **Last Build Duration Longer Than** option, enter a number of seconds.
  4. Click **Add Filter** to add more filters, and repeat steps 2 and 3 for each filter you are adding. 
     * To clear your filter selections and start over at any point, click **Clear All**.
     * To remove any individual additional filters, click the **Clear** option for the filter you want to remove.
  5. To apply the selected filter criteria to the **Persistent Derived Tables** page, click **Apply**.

You will see the applied filters at the top of the **Persistent Derived Tables** page.

Click the **X** next to an applied filter on the **Persistent Derived Tables** page to remove the filter from the **Persistent Derived Tables** page. Click **Clear All** to clear all filters.

## Understanding the Persistent Derived Tables page

The following sections describe the information on the **Persistent Derived Tables** page.

### Production and Development tabs

If you are a LookML developer in [Development Mode](/looker/docs/dev-mode-prod-mode), the **Persistent Derived Tables** table will have two tabs:

  * The **Production** tab is selected by default and shows the production persisted tables. These are the persisted tables that have been deployed to production on your instance; these persisted tables provide the data for your users' Explore queries. (If you are in [Production Mode](/looker/docs/dev-mode-prod-mode) or if you don't have [`develop`](/looker/docs/admin-panel-users-roles#develop) permissions, the **Persistent Derived Tables** page will not display any tabs, and the page will show information for production persisted tables only.)

  * The **Development** tab shows the [development persisted tables](/looker/docs/derived-tables#persisted_tables_in_development_mode). Development persisted tables have not yet been pushed to the production environment.

Looker creates a development persisted table when a LookML developer in Development Mode makes changes that affect the data in the persisted table or the way that the persisted table is queried. These changes prompt Looker to _create_ the development persisted table, but Looker doesn't actually _build_ the persisted table unless the persisted table is queried after the changes are made. The **Development** tab can help you determine which development persisted tables Looker has created and whether they have been built.

**Tip:** You can also [view unbuilt persisted tables in your project by using the Looker IDE](/looker/docs/derived-tables#checking_for_unbuilt_pdts_in_development_mode).

See the [Derived tables in Looker](/looker/docs/derived-tables#persisted_tables_in_development_mode) documentation page for more information on what prompts Looker to create development persisted tables and how long development persisted tables are persisted on your database.

### At a Glance section

The **At a Glance** section shows a visual summary of the status for the persisted tables that are displayed in the persisted table table. If you have defined filters for the table, or if you have used the arrow next to **All Connections** at the top of the page to narrow the table to a specific connection, the **At a Glance** section will narrow the results to match what is shown in the persisted table table.

You can show or hide the **At a Glance** section by clicking the close/open icon at the top of the section.

### Table columns

The following sections describe the table columns on the **Persistent Derived Tables** page. You click the **Select columns to display** icon to hide or display some of the table columns. For more information, see the Customizing the table section on this page.

#### PDT Name

The **PDT Name** column displays the name of the persisted table as defined in the [`view`](/looker/docs/reference/param-view-view) parameter of the persisted table's LookML view file.

The **PDT Name** column displays this additional information under the persisted table name, when applicable:

  * **Old Build** indicates that the row is displaying information about an old persisted table build. See the **PDT Details** dialog in the **Options** menu for more information about this message.
  * **Incremental** indicates that the persisted table is an [incremental PDT](/looker/docs/incremental-pdts).
  * **Materialized View** indicates that the persisted table is a [materialized view](/looker/docs/derived-tables#materialized_view) on your database.

#### Last Attempt Status

The **Last Attempt Status** column displays the status of the last attempt to build each listed persisted table:

  * Regenerating indicates that the persisted table can be queried and that an updated table is being built. A timestamp indicates when the persisted table began building.
  * Success indicates that a persisted table has successfully built.
  * Building indicates that a persisted table is being built and cannot be queried until the build is completed.
  * Not Built indicates that a persisted table is not built.
  * Build Error indicates that an error has occurred during a build. You can click **Build Error** to see the error's source and navigate to the persisted table's LookML if you have the [appropriate permissions to see LookML](/looker/docs/admin-panel-users-roles#see_lookml). See the Options menu section on this page to learn more about troubleshooting persisted tables from the **Persistent Derived Tables** page.

#### Last Attempted At

The **Last Attempted At** column indicates the time of the last attempted persisted table build.

#### Last Successful Build

The **Last Successful Build** column indicates the time of the last successful persisted table build.

#### Last Build Duration

The **Last Build Duration** column displays the amount of time in seconds that it took for the latest build of that persisted table and how long it takes to build the persisted table on average in seconds.

#### Persistence Rule

The **Persistence Rule** column displays the type of [persistence](/looker/docs/derived-tables#making_a_derived_table_persistent) that is applied to a persisted table, as specified in the persisted table's LookML definition. It also indicates the last time a successfully built persisted table was checked (for trigger type persisted tables) or when a successfully built persisted table is due to expire (for persist type persisted tables). There are two types of persistence displayed in the **Persistence Rule** column:

  * **Persist for: (time)** is displayed for persisted tables that are persisted with the [`persist_for`](/looker/docs/reference/param-view-persist-for-for-derived-table) parameter.
  * **Trigger: (datagroup name)** is displayed for persisted tables that are persisted with a [`datagroup_trigger`](/looker/docs/reference/param-view-datagroup-trigger) parameter. You can click the datagroup name link to view the `sql_trigger` value for the `datagroup` parameter.
  * **Trigger: SQL** is displayed for persisted tables that are persisted with a [`sql_trigger_value`](/looker/docs/reference/param-view-sql-trigger-value) parameter. You can click the link to view the `sql_trigger_value` statement.
  * **Materialized View** is displayed for [materialized views](/looker/docs/derived-tables#materialized_view), which leverage your database's functionality to persist derived tables on your database.

#### Project

The **Project** column indicates the name of the [LookML project](/looker/docs/what-is-lookml#lookml_projects) where the persisted table is defined.

#### Connection

If **All Connections** is selected from the connection select, the **Connection** column appears and displays the name of the [connection](/looker/docs/admin-panel-database-connections) on which the persisted table is enabled.

#### Model

The **Model** column displays the name of the [model file](/looker/docs/model-and-view-files#model_files) that is associated with the persisted table. For a PDT, this is typically the model file that [includes](/looker/docs/reference/param-model-include#including_views_and_dashboards_in_a_model) the view file where the PDT is defined. For an aggregate table, this is typically the model file in which the aggregate table is defined. 

**Note:** If a PDT view file is included in multiple model files that share the same connection, multiple models will appear in the **Model** column. If a PDT view file is included in multiple model files with different connections, the PDT will also appear in other connection PDT lists. 

It is important to be explicit when including view files in models, as [including all view files may clutter your database schema](/looker/docs/reference/param-model-include#including_all_view_files_can_clutter_your_database_schema) and cause multiple copies of PDTs to build on your database, or on multiple databases.

### Options menu

The three-dot **Options** menu more_vert is especially useful for troubleshooting unexpected behavior. The options it presents allow you to check when tables were last built, check how long they took to build, compare the latest build time against the average build time, and check whether triggers are working correctly. You can select from:

  * **Go to LookML** : Opens the view file in which the persisted table is defined if you have the [appropriate permissions to see LookML](/looker/docs/admin-panel-users-roles#see_lookml).
  * **PDT Activity Dashboard** : Opens the **PDT Activity** dashboard, which is filtered to show activity for the selected persisted table over the last four weeks. 
  * **PDT Details** : Opens a dialog that contains more information and statistics for a specific persisted table. See the PDT details modal section on this page for more information.

See the [Monitoring and troubleshooting PDTs section](/looker/docs/derived-tables#monitoring_and_troubleshooting_pdts) on the [Derived tables in Looker](/looker/docs/derived-tables) documentation page for troubleshooting tips.

### PDT details modal

Click the **PDT Details** option from the persisted table's three-dot **Options** menu more_vert to see the PDT details modal.

The information in the modal depends on the configuration of the persisted table. Here is the information that you may see:

  * **Table Name** : The hash of the latest successfully built persisted table.
  * **Model** : The name of the [model file](/looker/docs/model-and-view-files#model_files) in which the persisted table's view file is [included](/looker/docs/reference/param-model-include#including_views_and_dashboards_in_a_model).
  * **Stable Name** : The name of the persisted table's stable database view on your database, if the persisted table has been published as a stable view. You can publish a persisted table as a stable view on your database by adding the [`publish_as_db_view: yes`](/looker/docs/reference/param-view-publish-as-db-view) statement to the PDT or aggregate table, or by using the [`materialized_view: yes`](/looker/docs/derived-tables#materialized_view) statement to make the derived table a materialized view.
  * **Connection** : The name of the [connection](/looker/docs/admin-panel-database-connections) on which the persisted table is enabled.
  * **Old Build** : A Boolean that displays **Yes** if a build is an old persisted table build or **No** if it is not. 
    * **Table Type** : For old builds, this field appears and shows the table type. Values include **Old Generation Table** and **Standin**.
  * **Incremental PDT** : A Boolean that displays **Yes** if a persisted table is an [incremental PDT](/looker/docs/incremental-pdts) or **No** if it is not.
  * **Status** : Gives the **Last Attempt Status**. For failed builds, provides a SQL error message and a link to the model's LookML if the user has the [appropriate permissions to see LookML](/looker/docs/admin-panel-users-roles#see_lookml).
  * **Dependencies** : Click the **Show Dependency Graph** button to display a relationship diagram of all derived tables that this persisted table [depends on](/looker/docs/derived-tables#cascading_derived_tables). Each node in the diagram corresponds to a derived table. The color of each node corresponds to that derived table's status, as follows: 
    * A green node represents a persisted table that has been successfully built.
    * A yellow node represents a persisted table that is building or [incrementing](/looker/docs/incremental-pdts).
    * A red node represents a persisted table that failed to build.
    * A gray node represents a persisted table that is not yet built.
    * A white node represents a [temporary derived table](/looker/docs/derived-tables#temporary_derived_tables), which Looker does not build.
  * **Last Build** : 
    * **Latest Successful Build** : The date and time of the most recent successful persisted table build.
    * **Latest Build Duration** : How long the most recent persisted table build took (in seconds; displays **–** if the table has not yet been built).
    * **Average Build Duration** : How long it takes to build the persisted table on average (in seconds; displays **–** if the table has not yet been built).
    * **Build Reason** : The reason a persisted table was built (**inception** for an initial build; **datagroup triggered** if the persisted table is persisted with a datagroup; **trigger value change** if the persisted table's SQL trigger value has changed).
    * **Increment Key** : The [`increment_key`](/looker/docs/reference/param-view-increment-key) parameter for persisted tables that use incremental builds.
    * **Increment Offset** : The [`increment_offset`](/looker/docs/reference/param-view-increment-offset) parameter for persisted tables that use incremental builds.
    * **Increment Build Added/Removed Rows** : The number of rows that were added to or removed from the table when the table was last incremented (displays **–** if no rows were added or removed when the table's persistence strategy last triggered an increment).
    * **Last Attempted SQL** : The SQL that was used to query the database to create the last build of the table.
  * **Persistence Rule** : 
    * **Type** : The type of persistence that is used by the table. See the **Persistence Rule** column section on this page for possible values.
    * **Persist For** : For **Persist** type persisted tables, the persistence duration value. Not applicable for **Trigger** type persisted tables.
    * **Datagroup** : For datagroup trigger persisted tables, gives the name of the datagroup.
    * **SQL code block** : For datagroup and SQL trigger persisted tables, the code block will show the trigger's SQL statement. For datagroup triggers, this is the SQL for the [`sql_trigger`](/looker/docs/reference/param-model-datagroup#sql_trigger) parameter of the datagroup. For SQL triggers, this is the SQL for the [`sql_trigger_value`](/looker/docs/reference/param-view-sql-trigger-value) parameter.
    * **Trigger Value** : For **Trigger** type persisted tables, the value that triggered the persisted table build (displays **–** for successfully built persisted tables that are persisted with a [`datagroup_trigger`](/looker/docs/reference/param-view-datagroup-trigger); to see the most recent trigger value for a [datagroup](/looker/docs/reference/param-model-datagroup), see the [**Datagroups**](/looker/docs/admin-panel-database-datagroups) page in the **Admin** panel).
    * **Last Checked** : For **Trigger** type persisted tables, when the trigger value was last checked.
    * **Expires** : When the persisted table expires, if applicable (not applicable for datagroup triggers).

## PDT Activity dashboard

The **PDT Activity** dashboard shows information about the persisted table, its rebuilds, and its queries.

![](/static/looker/docs/images/pdt-activity-dashboard-2104.png)

The **PDT Activity** dashboard defaults to showing activity information from the previous four weeks. You can change the time period that's shown by using the filter bar at the top of the dashboard. The **PDT Activity** dashboard includes tiles that show the following information:

  * A summary of the persisted table that includes the name of the LookML model and view that define the persisted table, the name of the database [connection](/looker/docs/connecting-to-your-db) that the persisted table uses, the total number of the persisted table's successful and failed build attempts, and the percentage of total build attempts that were failures.
  * The date and time of the most recent full rebuild of the persisted table.
  * If the persisted table is an incremental PDT, the date and time of the most recent incremental rebuild of the PDT.
  * If the persisted table is an incremental PDT, the number of incremental rebuilds that have occurred since the most recent full rebuild.
  * The average time taken to rebuild the persisted table.
  * A visualization that shows all the create [events](/looker/docs/events) that have occurred recently, grouped by a summary of the types of actions that caused the events.
  * A list of all the persisted table rebuilds that have occurred during the dashboard's time period, including the date each rebuild was completed, the number of seconds taken to complete each rebuild, whether rebuilds were incremental builds, the trigger that caused each rebuild, and the number of persisted table builds.
  * A list of all failed rebuild attempts, including the date and time that the failed rebuild began, the type of error that caused the failure, the error message, and the number of create failures.
  * A list of all the persisted table rebuild trigger [events](/looker/docs/events), including the event ID number, the date of the event, the type of event, and the data that was included with the trigger event.
  * A list of all the persisted table rebuild [events](/looker/docs/events), including the event ID number, the date of the event, the type of event, and the data that was included with the rebuild event.
  * The number of queries that directly queried a field, grouped by the source of the query and the average runtime for each query source.
  * The total number of queries run on the persisted table.
  * A list of all the persisted table fields queried, including the LookML view and model in which the field is defined, the field name, the name of the Explore run that included the field, and the number of times the field was included in a query.

## PDT Event Log Explore

Looker includes a prebuilt model named [`system_activity`](/looker/docs/system-activity-pages) that allows exploration of the PDT event log, which is a table in a database connection's temp schema that tracks the trigger and build activity of persisted tables.

You can access the model with the **Recent Build Events** and **Recent Trigger Events** links in the **Options** three-dot menu more_vert of the **Persistent Derived Tables** page, or from the [Connections](/looker/docs/admin-panel-database-connections#show_pdt_event_log) page in the Looker **Admin** panel.

To access the **PDT Event Log** Explore from the **Connections** page, select the **Show PDT Event Log** option from the gear icon drop-down menu settings for each connection.

You can explore the model as with any other Looker Explore. When accessed from the **Connections** page, the **PDT Event Log** Explore is filtered for the entire connection. When accessed from the **Persistent Derived Tables** page, the **PDT Event Log** Explore is filtered for a specific persisted table.

This is a brief guide to the available fields in the **PDT Event Log** Explore:

Field| Description  
---|---  
Action| Describes the action that occurred; this may include regeneration, drop, creation, and reaping activity.See the [Understanding PDT log actions](/looker/docs/pdt-log-actions) documentation page for more information about viewing and understanding PDT log actions and their corresponding action data.  
Action Data| Provides more specific detail about an action, including the trigger that's being used, the value of a trigger, the expiration time for a persistent table, the cause of a rebuild, and the text of an error message.See the [Understanding PDT log actions](/looker/docs/pdt-log-actions) documentation page for more information about viewing and understanding PDT log actions and their corresponding action data.  
Connection| The name of the connection that the derived table exists on.  
Hash| Each derived table contains a hash of the SQL that was written to create it.  
ID| The unique ID of the Looker instance that generated the persisted table. In many cases, there will be only one Looker instance pointing at a database, so you will see only a single ID. However, if you have a staging instance, or something of that nature, you may see multiple IDs.  
Model Name| The name of the model through which the table was generated.  
Occur Date| The date and time that the event occurred.  
Occur Utc Display Date| The date and time that the event occurred in UTC.  
Sequence| A step number in the persisted table build.  
Short Hash| A truncated version of the hash of the SQL that was written to create the derived table.  
Table Name| The full name of the persisted table, including the table-type prefix, a hash, and the view name.  
Tid| The transaction ID.  
View Name| The view name for the derived table.