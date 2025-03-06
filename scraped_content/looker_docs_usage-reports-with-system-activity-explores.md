# https://cloud.google.com/looker/docs/usage-reports-with-system-activity-explores

Depth: 3

**Note:** Before enabling System Activity on a customer-hosted Looker deployment with a [MySQL backend](/looker/docs/migrating-looker-backend-db-to-mysql), verify that you have properly set up the user for the backend database. Specifically, you must perform the step to `grant all on looker_tmp.* to '<DB_username>'@'%';` before you enable the **System Activity** feature. See the procedure on the [Migrating the Looker backend database to MySQL](/looker/docs/migrating-looker-backend-db-to-mysql#mysql_create_db) documentation page.

Looker admins and users who have been granted the [`see_system_activity`](/looker/docs/admin-panel-users-roles#see_system_activity) permission have access to Looker's System Activity Explores in the [**Explore** menu](/looker/docs/creating-and-editing-explores#explores_are_the_starting_point_for_exploration).

The System Activity Explores connect to Looker's underlying application database. They show information about your Looker instance, including Looks and dashboards saved on your instance, user information, historical query information, and instance performance statistics. Both the granularity and retention of System Activity data are subject to system constraints. System Activity is designed for collecting high-volume data, and aggregating it can be used to supplement your business logs.

**Note:** This data can be useful for supplementing monitoring and auditing activities, but is not intended to replace your current compliance strategy.

By default, System Activity data is stored in Looker's internal database. Most tables are truncated on a regular schedule to comply with storage limits. For example, the [History table](/looker/docs/usage-reports-with-system-activity-explores#history) is truncated to the past 90 days of data. Some tables have more stringent data retention policies. To increase data retention, consider using [Elite System Activity](/looker/docs/elite-system-activity).

It is not possible to query System Activity data using SQL Runner as permissions for Looker's internal database are limited.

**Note:** The text in filters run by users is accessible in System Activity and can be viewed by any user who has permission to view the System Activity model.

**Take action:** Modify who has view access to the System Activity model. Looker admins have access to this model by default. Non-admin users can be granted access to the System Activity model if they are given the `see_system_activity` permission.

System Activity dashboards and Explores are restricted in the number of concurrent queries that can be run. This restriction may increase loading times for System Activity Explores.

**Chat Team Tip:** Time-based data in System Activity is stored in the Looker System time zone. See the [Using time zone settings](/looker/docs/using-time-zone-settings#system_time_zone) documentation page for more information.

## System Activity Explores

These are the System Activity Explores:

Explore Name | Description | Cache duration  
---|---|---  
Content Usage | Data about Look and dashboard usage, including frequency of views, favoriting, scheduling, embedding, and access through the API. Also includes details about individual Looks and dashboards. | 12 hours  
DB Connection | Details about database connections. Includes information about users who have access to the database connections. | 1 hour  
Dashboard | Details about all dashboards and dashboard elements. Includes information about Looks, queries, roles, users, and folders that are associated with dashboards. | 12 hours  
Dashboard Performance | Performance and historical data about dashboards. | 1 hour  
Event | Information about historical [events](/looker/docs/events) within Looker, including the name, type, and frequency of each event. Includes information about groups and users who are connected to the events. | 1 hour  
Event Attribute | Information about the attributes that make up [events](/looker/docs/events). Includes the data in the **Event** Explore and adds attribute information. | 12 hours  
Field Usage | LookML fields and the number of times used. | 1 hour  
Folders | Information about all folders, the content stored in each folder, and the creator of each folder. | 1 hour  
Group | Listing of groups and details about those groups, including parent and child groups, and users and roles that belong to each group. | 1 hour  
History | Details about all queries run in the previous 90 days. | 12 hours  
Look | Details about all Looks. Includes information about dashboards, queries, users, and folders that are associated with Looks. | 12 hours  
Merge Query | Information about [merged queries](/looker/docs/merged-results), including fields and other elements of both the source and the merged queries. | 1 hour  
PDT Builds | Details about PDT builds, including time taken to finish builds, and the connection and model the PDTs are part of. | 1 hour  
PDT Event Log | Information about historical events related to PDTs, including PDT rebuilds and errors.See the [Understanding PDT log actions](/looker/docs/pdt-log-actions) documentation page for more information about viewing and understanding PDT log actions and their corresponding action data. | 12 hours  
Query Performance Metrics | Detailed breakdowns of queries that are run from your Looker instance. | 1 hour  
Role | Looker roles and the model and permissions sets that make up the roles. | 1 hour  
SQL Query | SQL queries that have been run, including how recently and frequently, and details about users who have run them. | 1 hour  
Scheduled Plan | Information about all scheduled data deliveries, including both previously scheduled jobs and currently scheduled jobs. Includes data about the dashboards, Looks, queries, folders, and users that are associated with scheduled data deliveries. | 12 hours  
User | Details about each user, including historical queries run, and the content and folders to which they have access. | 12 hours  
  
See the Using the System Activity Explores section on this page for some examples of common uses for the Content Usage, Dashboard, Event, Event Attribute, History, Look, Merge Query, PDT Builds, SQL Query, Scheduled Plan, and User Explores.

## Using the System Activity Explores

Following are some examples of how you can use some of the Explores in System Activity, along with the answers to some common questions. You can access the example Explores in this section by replacing `<instance_name.looker.com>` in the example URLs with the address of your Looker instance.

### API Usage

The **API Usage** Explore provides a summary of the volume of API calls made to your Looker instance.

You can use the **API Usage** Explore to answer questions like the following:

  * How can I get a daily audit of API calls?
  * How many total API calls have been made on my instance this year?

#### How can I get a daily audit of API calls?

You can use the **API Usage** Explore to retrieve a list of all API calls made on your instance for any given time period. To see which calls were made on a given day:

  1. Select **Endpoint** from **API Usage**.
  2. Select **Total Usage** from **API Usage**.
  3. Filter on **Created Date** from **API Usage** with the desired date.

    
    
    https://<instance_name.looker.com>/explore/system__activity/api_usage?fields=api_usage.endpoint,api_usage.total_usage&f[api_usage.created_date]=yesterday&sorts=api_usage.total_usage+desc&limit=500&column_limit=50&vis=%7B%7D&filter_config=%7B%22api_usage.created_date%22%3A%5B%7B%22type%22%3A%22advanced%22%2C%22values%22%3A%5B%7B%22constant%22%3A%22yesterday%22%2C%22unit%22%3A%22day%22%7D%2C%7B%7D%5D%2C%22id%22%3A5%2C%22error%22%3Afalse%7D%5D%7D&origin=share-expanded
    

Check the [Looker API Reference](/looker/docs/reference/looker-api/latest) or [Looker API Explorer](/looker/docs/api-explorer) for more information about what each API call does.

#### How many API calls have been made on my instance this year?

You can use the **API Usage** Explore to aggregate the volume of API calls over any timeframe. For example, you can create a yearly report that shows how many API calls were made each month:

  1. Select **Created Month** from **API Usage**.
  2. Select **Total Usage** from **API Usage**.
  3. Filter on **Created Year** from **API Usage** with the desired year.

    
    
    https://<instance_name.looker.com>/explore/system__activity/api_usage?fields=api_usage.total_usage,api_usage.created_month&fill_fields=api_usage.created_month&f[api_usage.created_year]=last+year&sorts=api_usage.created_month+desc&limit=500&column_limit=50&vis=%7B%7D&filter_config=%7B%22api_usage.created_year%22%3A%5B%7B%22type%22%3A%22advanced%22%2C%22values%22%3A%5B%7B%22constant%22%3A%22last+year%22%2C%22unit%22%3A%22yr%22%7D%2C%7B%7D%5D%2C%22id%22%3A6%2C%22error%22%3Afalse%7D%5D%7D&origin=share-expanded
    

### Content Usage

The **Content Usage** Explore in System Activity provides information about Look and dashboard usage, including frequency of views, favoriting, scheduling, and access via the API. It also includes details about individual Looks and dashboards.

#### Quick Start analyses

The **Content Usage** Explore includes [Quick Start](/looker/docs/creating-and-editing-explores#quick_start_analyses) analyses, which you can use to quickly answer questions or as starting points for other queries.

![](/static/looker/docs/images/content-usage-quick-start-2312.png)

Select a Quick Start analysis tile in a blank Explore, or from the [lightning bolt **Quick Start** menu](/looker/docs/creating-and-editing-explores#choosing_a_quick_start_option_once_an_explore_has_run) in an Explore that has run, and Looker will show a query with fields that are preselected and sorted to answer one of the following questions:

  * Which content has been favorited the most times?
  * Which content has been accessed in the previous 3 days?
  * Which content has not been accessed in the past 60 days?
  * Which content has been accessed most frequently using the [Looker API](/looker/docs/api-getting-started)?
  * Which dashboards created in the past 7 days are used the most?
  * Which Looks created in the past 7 days are used the most?
  * Which boards have been favorited the most times?
  * Which content has been viewed the most times?

#### What filters are used by popular Looks and dashboards?

You can use the **Content Usage** Explore to find the most popular Looks or dashboards on your instance. You can then use the **History** Explore to identify the filters used by popular Looks or dashboards. To find the most popular Looks or dashboards:

  1. In the **Content Usage** Explore, select **Content ID** , **Content Title** , and **Content Type** from the **Content Usage** view.
  2. Add a filter on **Content Type** from the **Content Usage** view, and set the filter value to `dashboard OR look`.
  3. Select **View Total** from **Content Usage**. You can also select fields like **Favorites Total** , **Schedule Total** , **API Total** , and **Embed Total** from the **Content Usage** view.
  4. Sort the results in descending order on **View Total** to list the most popular content first.
  5. You can also add a filter on the **Days Since Last Accessed** field from the **Content Usage** view to limit the data to a specific length of time. For example, you can limit the data you view to the last 30 days by setting the filter value to `is less than 30`.

Then, you can use the **History** Explore to find the filters used in a specific Look or dashboard:

  1. In the **History** Explore, filter on the **ID** field from either the **Dashboard** view or the **Look** view, and enter the IDs for the dashboards or Looks you identified using the **Content Usage** Explore.
  2. Select **Filters** from the **Query** view to return a list of filters used by the dashboards or Looks you are filtering on.

### Dashboard

The **Dashboard** Explore includes details about dashboards and dashboard elements, including Looks, queries, roles, users, and folders that are associated with dashboards.

#### Quick Start analyses

The **Dashboard** Explore includes [Quick Start](/looker/docs/creating-and-editing-explores#quick_start_analyses) analyses, which you can use to quickly answer questions or as starting points for other queries.

![](/static/looker/docs/images/dashboard-quick-start-2308.png)

Select a Quick Start analysis tile in a blank Explore, or from the [lightning bolt **Quick Start** menu](/looker/docs/creating-and-editing-explores#choosing_a_quick_start_option_once_an_explore_has_run) in an Explore that has run, and Looker will show a query with fields that are preselected and sorted to answer one of the following questions:

  * Which dashboards use multiple Explores?
  * Which dashboards have short [auto-refresh](/looker/docs/editing-user-defined-dashboards#autorefresh) intervals?
  * How many dashboards are set to [run on load](/looker/docs/editing-user-defined-dashboards#run_on_load)?
  * Which dashboards have more than 25 tiles?
  * Which dashboards use the most [merge queries](/looker/docs/merged-results)?
  * Which dashboards use a particular view or field?
  * Which folders contain which dashboards?
  * What tiles make up an individual dashboard?

### Event

The **Event** Explore includes information about historical events within Looker, including the name, type, and frequency of each event. This Explore also includes information about groups and users who are connected to the events.

Following are some common uses of the **Event** Explore:

  * How can I find and categorize API requests?
  * Is there a way to investigate content updates?
  * How do I view login events?

See the [Looker events](/looker/docs/events) documentation page for more information about viewing events and common event attributes, and for a list of event types.

#### How can I find and categorize API requests?

You can find all the API requests that have been made and categorize them using the **Event** Explore:

  1. Select the **Name** and **Category** fields from the **Event** view.
  2. Add a filter on **Is API Call (Yes / No)** , and set the filter value to `Yes`.
  3. You can also select fields like **Created Date** from **Event** , and **Name** from **User** , for information about specific API requests.

    
    
    https://<instance_name.looker.com>/explore/system__activity/event?fields=event.created_date,event.name,event.category,user.name&f[event.is_api_call]=Yes&sorts=event.name&limit=500
    

#### Is there a way to investigate content updates?

You can use the **Event** Explore to investigate content updates by filtering on events that include the word `update`:

  1. Select the **Name** from the **Event** view.
  2. Add a filter on the **Name** field from the **Event** view, and set the filter value to `contains update`.
  3. You can also select other fields to provide more information about each content update, such as **Created Time** from **Event** , and **ID** from **User**.

    
    
    https://<instance_name.looker.com>/explore/system__activity/event?fields=event.name,user.id,event.created_time&f[event.name]=%25update%25&sorts=event.created_time+desc&limit=500
    

#### How do I view login events?

You can use the **Event** Explore to determine who has logged in to the system with login events. For example:

  1. Add a filter on the **Name** field from the **Event** view, and set the filter value to `login`.
  2. Select the **ID** and **Name** from the **User** view.
  3. Select **Created Time** from the **Event** view.

### Event Attribute

The **Event Attribute** Explore contains the data in the **Event** Explore and provides additional information about the attributes that make up [events](/looker/docs/events).

Following are some common uses of the **Event Attribute** Explore:

  * How do I view permission changes?
  * How do I track when Labs features are turned on?
  * When was a project name changed?

For more information about viewing events, common event attributes, and a list of event types, see the [Looker events](/looker/docs/events) documentation page.

#### How do I view permission changes?

You can use the **Event Attribute** Explore to view permission changes. For example, you can find out when a permission was changed and who changed it:

  1. Select **Created Time** and **Name** from the **Event** view for the time the change was made and the type of event.
  2. Select **Name** and **Value** from **Event Attribute** to return information about the type of change made and either the users whose permissions were changed or the specific permissions that were changed.
  3. Select **ID** and any other desired fields from **User** for information about the user who made the change.
  4. Filter on **Name** in the **Event** view, setting the value to `user_permission_elevation`.

    
    
    https://<instance_name.looker.com>/explore/system__activity/event_attribute?fields=event.created_time,user.id,user.name,event_attribute.name,event_attribute.value&f[event.name]=%22user_permission_elevation%22&sorts=event.created_time+desc&limit=500
    

#### How do I track when Labs features are turned on?

You can use the **Event Attribute** Explore to track when [Labs features](/looker/docs/admin-panel-general-labs) are turned on. For example, select the following fields:

  1. Select **Created Time** from the **Event** field.
  2. Select **Name** and **Value** from the **Event Attribute** field.
  3. Add a filter on **Name** from **Event** , and set the filter value to `update_labs_feature`.
  4. You can also add fields like **ID** or **Name** from **User** to view information about the user who turned on a Labs feature.

In this example, the name of the Labs feature that has been turned on or off is shown in the **Value** field of **Event Attribute** when **Name** from **Event Attribute** has the value `labs_feature_id`. When **Name** from **Event Attribute** has the value `labs_feature_value`, the values `true` and `false` indicate whether the Labs feature was turned on or off.
    
    
    https://<instance_name.looker.com>/explore/system__activity/event_attribute?fields=event.created_time,event_attribute.name,event_attribute.value,user.id&f[event.name]=%22update_labs_feature%22&sorts=event.created_time+desc&limit=500
    

#### When was a project name changed?

You can use the **Event Attribute** Explore to see when the name of a project was changed:

  1. Select **Created Time** and **Name** from the **Event** view.
  2. Select **Name** and **Value** from **Event Attribute**.
  3. Add a filter on **Name** from the **Event** view, and set the filter value to `rename_project_file`.

    
    
    https://<instance_name.looker.com>/explore/system__activity/event_attribute?fields=event.created_time,event.name,event_attribute.name,event_attribute.value&f[event.name]=%22rename_project_file%22&sorts=event.created_time+desc&limit=500&query_timezone=America%2FLos_Angeles&vis=%7B%7D&filter_config=%7B%22event.name%22%3A%5B%7B%22type%22%3A%22%3D%22%2C%22values%22%3A%5B%7B%22constant%22%3A%22rename_project_file%22%7D%2C%7B%7D%5D%2C%22id%22%3A0%2C%22error%22%3Afalse%7D%5D%7D&origin=share-expanded
    

### History

The **History** Explore provides a record of individual queries. It can be useful for troubleshooting, as it provides details about all the queries run on your instance in the past 90 days.

Following are some common questions about using the **History** Explore:

  * What are all the models used by a dashboard?
  * How can I identify long-running queries?
  * When was the last time someone used SQL Runner?
  * How can I find queries that were killed by the database?
  * What is the most popular dashboard by query count?
  * Which Explores are most popular with different roles?
  * Has anyone queried a specific Explore in the last 90 days?
  * Has anyone used a field from a specific view in the last 90 days?
  * Which queries were initiated from within Google Sheets?

#### Truncation of the History table

Because the size of the **History** table can increase rapidly, Looker automatically deletes records that meet any of the following criteria:

  * The `history.created_time` is more than 90 days in the past.
  * The `history.created_time` is more than 7 days in the past, and the `history.source` is `scheduled_task`.

#### Clarification of select fields

Each field in the **History** Explore has a description to help you understand its purpose. The following table contains more detailed descriptions of certain fields that customers often ask about:

Field name | Description | Possible values  
---|---|---  
Source | The source of a query, such as a Look, an Explore, a scheduled task, an alert, a dashboard, etc. | 

  * `alerts`: The query was initiated from an [alert](/looker/docs/alerts-overview).
  * `api`: The query was initiated using the [Looker API](/looker/docs/api-getting-started).
  * `api3`: The query was initiated using the [Looker API](/looker/docs/api-getting-started).
  * `authenticated_download`: The query was initiated using the [Looker Action Hub](/looker/docs/action-hub) with a [streaming action](/looker/docs/downloading#streaming_query_results) on a schedule.
  * `dashboard`: The query was initiated from a [dashboard](/looker/docs/building-dashboards). (The query may have been initiated from the UI, from the API, or from a scheduled task.)
  * `dashboard_prefetch`: The query was initiated from a [dashboard prefetch](https://community.looker.com/looker-api-77/prefetching-3-36-1826).
  * `data-download-api`: This query was initiated from a [dashboard download in CSV format](/looker/docs/downloading#downloading_a_dashboard_as_csvs).
  * `drill_modal`: The query was initiated when a user [drilled into the data](/looker/docs/viewing-and-interacting-with-explores#drilling_down_into_the_data).
  * `explore`: The query was initiated from an [Explore](/looker/docs/creating-and-editing-explores). (The query may have been initiated from the UI or from the API)
  * `guided_analysis`: The query was created with the [Guided analyses in System Activity](/looker/docs/usage-reports-with-system-activity-explores#guided_analyses_in_system_activity_labs_feature) Labs feature.
  * `internal`: The query was run by Looker to retrieve metadata for internal purposes.
  * `look`: The query was initiated from a [Look](/looker/docs/viewing-looks). (The query may have been initiated from the UI, from the API, or from a scheduled task.)
  * `merge_query`: The query was initiated from a [merge query](/looker/docs/merged-results).
  * `private_embed`: The query was initiated from a [private embed](/looker/docs/private-embedding).
  * `public_url`: The query was initiated from a Look with [public access](/looker/docs/publishing-looks-with-public-urls) enabled.
  * `regenerator`: The query was initiated by the [PDT regenerator](/looker/docs/derived-tables#the_looker_regenerator).
  * `render_manager_cache`: The query was initiated by a download in PDF or PNG format. This could be a Look or a dashboard.
  * `scheduled_task`: The query was run on a [schedule](/looker/docs/scheduling-and-sending-dashboards) which generated a PDF. (This source does not include scheduled deliveries of non-PDF formats, such as CSV.) 
  * `sql_interface`: The query was initiated by a third-party application using the [Open SQL Interface](/looker/docs/sql-interface).
  * `sqlrunner`: The query was initiated from [SQL Runner](/looker/docs/sql-runner-basics).
  * `suggest`: The query was created as a [filter suggestions](/looker/docs/changing-filter-suggestions) query.

  
Issuer Source | The source of a query, bucketed. | 

  * **Action Hub** : The query was initiated using the [Looker Action Hub](/looker/docs/action-hub). This includes the **Source** value `authenticated_download`.
  * **API** : The query was initiated using the [Looker API](/looker/docs/api-getting-started). This includes the **Source** value `api3`.
  * **System** : The query was initiated by Looker without direct user intervention. This includes the **Source** values `alerts`, `data-download-api`, and `scheduled_task`.
  * **User** : The query was initiated by a Looker user. This includes the **Source** values `dashboard`, `drill_modal`, `explore`, `look`, `merge_query`, `private_embed`, `render_manager`, `sqlrunner`, and `suggest`.
  * **Other** : The query does not fit into any of the other buckets. This includes the **Source** value `internal`.

  
Status | The current status of the history event. | 

  * `cache_only_miss`: The query was run with the `cache_only=TRUE` option, and the cache entry was not present.
  * `complete`: The query successfully completed.
  * `error`: The query failed with an error. Include the **Message** field to see error details.
  * `killed`: The query was cancelled by a user, by the database, or by Looker.

  
Query Run Count | This field counts the number of query runs by filtering out History entries where the **Status** field value is `cache_only_miss`. In other words, this field only includes History entries where the **Status** field value is either `complete`, `error`, or `killed`.  | A positive integer.  
  
#### Quick Start analyses

The **History** Explore includes [Quick Start](/looker/docs/creating-and-editing-explores#choosing_a_quick_start_option_once_an_explore_has_run) analyses, which you can use to quickly answer questions or as starting points for other queries.

![](/static/looker/docs/images/history-quick-start-2308.png)

Select a Quick Start analysis tile in a blank Explore, or from the [lightning bolt **Quick Start** menu](/looker/docs/creating-and-editing-explores#choosing_a_quick_start_option_once_an_explore_has_run) in an Explore that has run, and Looker will show a query with fields that are preselected and sorted to answer one of the following questions:

  * What query sources have been the most active over the past day?
  * Which users have been the most active over the past week?
  * Which user's dashboards are the most popular?
  * How many times has a particular dashboard been used over the past 30 days?
  * What are the most recently run queries?
  * How many times has a particular Look been used over the past 30 days?
  * What are the average query runtimes of individual models?
  * What is the recent query activity for a particular user?

#### What are all the models used by a dashboard?

You can use the **History** Explore to find all the models used by a dashboard. As an example, this could help identify the models for which a user needs permissions when that user is unable to see the data on a dashboard.

  1. Select **ID (Inclusive)** from the **Dashboard** view.
  2. Select **Model** and **Count** from the **Query** view.
  3. Filter on **ID (Inclusive)** , entering the dashboard ID for the dashboard you want to filter on.

In the following URL example, you can replace the dashboard ID `123` in the filter element `f[history.real_dash_id]=123` with the ID for the dashboard you want to filter on:
    
    
    https://<instance_name.looker.com>/explore/system__activity/history?fields=history.real_dash_id,query.model,query.count&f[history.real_dash_id]=123&sorts=history.real_dash_id+desc&limit=500
    

#### How can I identify long-running queries?

Suppose you want to create [alerts](/looker/docs/user-alerts) for long-running queries. You can use the **History** Explore to, for example, find the queries that take the longest to run:

  1. Select **ID** and **Link** from **Query**.
  2. Select **Average Runtime in Seconds** and **Query Run Count** from **History** to view the average length of time each query ran and how many times the query has been run.
  3. You can add a filter on **Completed Date** from **History** , and set the filter value to a timeframe like `is in the past 7 days` to limit the results that are displayed.
  4. Add a filter on **Is Single Query (Yes / No)** and set its value to `is Yes` to exclude merge queries from the results.
  5. You can display only queries with a runtime that is above a certain threshold, such as 5 minutes; to do this, you can filter on **Average Runtime in Seconds** and set the filter value to `is greater than 300`.
  6. Sort in descending order on **Average Runtime in Seconds** from **History** to list queries with the longest average runtimes first.

You can then save the query as a Look and [create an alert](/looker/docs/alerts-overview#creating_an_alert) to notify you if there are queries with runtimes that exceed the threshold you specify.

In the following URL example, you change the timeframe for which results are displayed by replacing `7+days` in the filter element `f[history.created_date]=7+days` with the desired filter value. You can also change the value of the filter on **Average Runtime in Seconds** by replacing `is greater than 300` with the desired number of seconds in the filter element `f[history.average_runtime]=%3E300`.
    
    
    https://<instance_name.looker.com>/explore/system__activity/history?fields=query.id,history.average_runtime,history.query_run_count,query.link&f[history.is_single_query]=Yes&f[history.created_date]=7+days&f[history.average_runtime]=%3E300&sorts=history.average_runtime+desc&limit=500
    

#### When was the last time someone used SQL Runner?

To determine the last time a specific user ran a SQL Runner query using the **History** Explore:

  1. Select **Last Run Time** and **User ID** from the **SQL Runner Query** view.
  2. Add a filter on **User ID** from the **SQL Runner Query** view, and set the filter value to the ID of the user.

    
    
    https://<instance_name.looker.com>/explore/system__activity/history?fields=sql_query.last_run_time,sql_query.user_id&sorts=sql_query.last_run_time+desc&limit=500&column_limit=50
    

#### How can I find queries that were killed by the database?

To find queries that were killed by your database with the **History** Explore:

  1. Add a filter on **Message** from **History** , and set the filter value to `contains query killed`.
  2. Select **Created Date** , **ID** , and **Message** from **History**.
  3. Select **ID** from **Query**.

    
    
    https://<instance_name.looker.com>/explore/system__activity/history?fields=history.id,history.created_date,query.id,history.message&f[history.message]=%25query+killed%25&sorts=history.message&limit=500
    

#### What is the most popular dashboard by query count?

The **Dashboard** Explore lists the titles of every dashboard accessed in the last 90 days and includes a count of the number of times each of those dashboards was accessed:

  1. Select **Title** from **Dashboard**.
  2. Select **Query Run Count** from **History**.
  3. Add a filter on **Title** from **Dashboard** , and set the filter value to `is not null`.

    
    
    https://<instance_name.looker.com>/explore/system__activity/history?fields=dashboard.title,history.query_run_count&f[dashboard.title]=-NULL&sorts=history.query_run_count+desc&limit=500&column_limit=50
    

#### Which Explores are most popular with different roles?

This Explore shows how many times an Explore was run by each role on your instance in the previous 90 days:

  1. Select **Explore** from **Query**.
  2. Select and pivot on **Name** from **User Role**.
  3. Select **Query Run Count** from **History**.
  4. Add a filter on **Name** from **User Role** , and set the filter value to `is not null`.

    
    
    https://<instance_name.looker.com>/explore/system__activity/history?fields=history.query_run_count,query.view,role.name&pivots=role.name&f[role.name]=-NULL&sorts=history.query_run_count+desc+0,role.name&limit=500&column_limit=50
    

#### Has anyone queried a specific Explore in the last 90 days?

You can use the **History** Explore to determine if a specific Explore was used in the last 90 days:

  1. Select **Created Date** from **History**.
  2. Select **Explore** and **Link** from **Query**.
  3. Add a filter on **Explore** from **Query** , and enter the name of the Explore.

#### Has anyone used a field from a specific view in the last 90 days?

You can use the **History** Explore to determine if any fields from a specific view were used in the last 90 days:

  1. Select **Created Date** from **History**.
  2. Select **Explore** and **Link** from **Query**.
  3. Filter on **Fields Used** from **Query** , enter the name of the view followed by a period — for example, `orders.` — and select **contains** for the filter condition. The period in your filter will ensure that your results return fields from only that view and not fields from similarly named views.

In the following URL example, you can replace `order%5E_items.` in the filter element `f[query.formatted_fields]=%25order%5E_items.` with the name of the view you want to filter on, followed by a period:
    
    
    https://<instance_name.looker.com>/explore/system__activity/history?fields=history.created_date,query.view,query.link&f[query.formatted_fields]=%25order%5E_items.%25&sorts=history.created_date+desc&limit=500&column_limit=50
    

#### Which queries were initiated from within Google Sheets?

You can use the **History** Explore to view a list of queries that were generated from within Google Sheets using the [Connected Sheets for Looker](/looker/docs/connected-sheets) feature:

  1. Select **Date** and **Time of Day** from the **Created Date** group in **History**.
  2. Select **API Client Name** , **Connected Sheets Spreadsheet ID** , and **Connected Sheets Trigger** from the **Query API Client Properties** group in **History**.
  3. Select **Name** from **User**.
  4. Filter on **Connected Sheets Spreadsheet ID** in the **Query API Client Properties** group in **History** , and set the value to `is not null`.

    
    
    https://<instance_name.looker.com>/explore/system__activity/history?fields=query_api_client_context.name,query_api_client_context.cs_spreadsheet_id,query_api_client_context.cs_trigger,user.name,history.created_date,history.created_time_of_day&f[query_api_client_context.cs_spreadsheet_id]=-NULL&sorts=history.created_time_of_day+desc&limit=5000
    

### Look

The **Look** Explore includes details about all Looks, including information about dashboards, queries, users, and folders that are associated with Looks.

Following are some common questions about using the **Look** Explore:

  * Which Looks are shared publicly?
  * Who is the author of a specific Look?
  * Which Looks have been deleted?

#### Which Looks are shared publicly?

You can use the **Look** Explore to see which Looks are being shared publicly or have a public URL enabled.

  * Filter on **Public (Yes / No)** from **Look** , and set the filter value to `Yes`.
  * Select **ID** , **Name** , and **Link** from **Look**.

    
    
    https://<instance_name.looker.com>/explore/system__activity/look?fields=look.id,look.title,look.link&f[look.public]=Yes&limit=500
    

#### Who is the author of a specific Look?

To find the author of a specific Look:

  1. Filter on the **ID** from **Look** , setting the value to the Look's ID.
  2. Select **ID** and **Name** from **User**.
  3. You can also select fields like **Created Date** and **Title** from **Look**.

#### Which Looks have been deleted?

To view a list of all deleted Looks:

  1. Select **ID** , **Title** , **Link** , and **Deleted Date** from **Look**.
  2. Add a filter on **Deleted Date** from **Look** , and set the filter value to `is not null`.

    
    
    https://<instance_name.looker.com>/explore/system__activity/look?fields=look.id,look.title,look.link,look.deleted_date&f[look.deleted_date]=NOT+NULL&sorts=look.title&limit=500&column_limit=50
    

### Merge Query

The **Merge Query** Explore includes information about merged queries, including fields and other elements of both the source and the merged queries.

You can use the **Merge Query** Explore to answer questions like the following:

  * Which Explores are merged most frequently?

#### Which Explores are merged most frequently?

You can use the **Merge Query** Explore to find out which Explores are merged the most often and consider joining the tables for better performance and more features.

  1. Select **Explore** from **Query**.
  2. Select **Count** from **Merge Query Source Query**.

    
    
    https://<instance_name.looker.com>/explore/system__activity/merge_query?fields=query.view,merge_query_source_query.count&sorts=merge_query_source_query.count+desc&limit=500&query_timezone=America%2FLos_Angeles&vis=%7B%7D&filter_config=%7B%7D&origin=share-expanded
    

### PDT Builds

The **PDT Builds** Explore includes information about PDT builds, including time taken to finish builds and the connection and model the PDTs are part of.

Following are some common uses of the **PDT Builds** Explore:

  * How can I see PDT build times?
  * How can I identify long-running PDTs to alert on?

> These queries may take longer to run on instances with many PDTs running concurrently.

#### How can I see PDT build times?

You can use the **PDT Builds** Explore to view build times for PDTs. For example, to see PDT build times in the past 2 days:

  1. Add a filter on **Start Time** from the **PDT Builds** view and set its value to `is in the past 2 days`.
  2. Select **Start Time** , **View Name** , **Connection** , **Model Name** , **Elapsed Minutes** , and **Elapsed Seconds** from the **PDT Builds** view.

    
    
    https://<instance_name.looker.com>/explore/system__activity/pdt_builds?fields=pdt_builds.start_time,pdt_builds.view_name,pdt_builds.connection,pdt_builds.model_name,pdt_builds.elapsed_minutes,pdt_builds.elapsed_seconds&f[pdt_builds.start_time]=2+days&sorts=pdt_builds.start_time+desc&limit=500
    

#### How can I identify long-running PDTs to alert on?

You can use the **PDT Builds** Explore to identify long-running PDTs. Then, you can save the query as a Look and [create an alert](/looker/docs/alerts-overview#creating_an_alert) to notify you if there are PDTs with build times that exceed the threshold you specify.

For example, to see PDTs with an average build time of more than 30 minutes:

  1. Add a filter on **Average Build Time Minutes** from the **PDT Builds** view and set its value to `is greater than 30`.
  2. Select **View Name** , **Connection** , and **Average Build Time Minutes** from the **PDT Builds** view.

To change the value of the filter on **Average Build Time Minutes** from **PDT Builds** , replace `30` in the filter element `f[pdt_builds.average_build_time_minutes]=%3E20` with the desired number of minutes:
    
    
    https://<instance_name.looker.com>/explore/system__activity/pdt_builds?fields=pdt_builds.view_name,pdt_builds.connection,pdt_builds.average_build_time_minutes&f[pdt_builds.average_build_time_minutes]=%3E30&sorts=pdt_builds.average_build_time_minutes+desc&limit=500
    

### Query Performance Metrics

The **Query Performance Metrics** Explore provides detailed breakdowns of each query that is run from your Looker instance.

For example, you can use this Explore to investigate which components of a query took longest to load. You can also use this Explore to identify query performance trends and anomalies. For a more detailed breakdown of the query lifecycle and the fields tracked in this Explore, see the [Understanding query performance metrics](/looker/docs/query-performance-metrics) documentation page.

#### Quick Start analyses

The **Query Performance** Explore includes [Quick Start](/looker/docs/creating-and-editing-explores#quick_start_analyses) analyses, which you can use to quickly answer questions or as starting points for other queries.

Select a Quick Start analysis tile in a blank Explore, or from the [lightning bolt **Quick Start** menu](/looker/docs/creating-and-editing-explores#choosing_a_quick_start_option_once_an_explore_has_run) in an Explore that has run, and Looker will show a query with fields that are preselected and sorted to answer one of the following questions:

  * How much time did each query stage take?
  * Which Explores have the highest average main query execution time?
  * Which users have the highest average main query execution time?
  * Which times of day have the longest asynchronous worker timings?
  * Which times of day have the longest query initialization timings?
  * Which times of day have the longest connection handling timings?
  * Which times of day have the longest main query timings?
  * Which times of day have the longest post-query timings?

### SQL Query

The **SQL Query** Explore includes information about the SQL queries that have run, including how recently and frequently, and details about users who have run them.

You can use the **SQL Query** Explore to answer questions like the following:

  * Which users run the most SQL queries?

#### Which users run the most SQL queries?

You can use the **SQL Query** Explore to identify the users who run the most SQL Runner queries:

  1. Select **ID** and **Name** from **User**.
  2. Select **Count** from **SQL Runner Query**.
  3. Sort in descending order on **Count** from **SQL Runner Query** to list users who run the most queries first.

    
    
    https://<instance_name.looker.com>/explore/system__activity/sql_query?fields=sql_query.count,user.id,user.name&sorts=sql_query.count+desc&limit=500
    

### Scheduled Plan

The **Scheduled Plan** Explore includes information about all scheduled data deliveries, including both previously scheduled jobs and currently scheduled jobs.

Following are some common questions about using the **Scheduled Plan** Explore:

  * How do I view scheduled plans in a consistent time zone?
  * At which stage do schedules get stuck?
  * How do I find schedule owners?
  * Which scheduled plans run at the same time?
  * Which schedules are unlimited?
  * Is it possible to view history for more than 50 schedules?
  * How do I filter results down to a specific set of schedules?
  * Can error trends be identified across schedules?
  * How do I view runtime metrics for schedules?

#### How do I view scheduled plans in a consistent time zone?

You can use the **Scheduled Plan** to view all scheduled plans in a consistent time zone, since System Activity stores time-based data in the [System time zone](/looker/docs/using-time-zone-settings#system_time_zone):

  1. Select **ID** , **Name** , and **Next Runtime** from **Scheduled Plan** to view the next runtime for each scheduled plan in the System time zone.
  2. Select **ID** and **Name** from **User** to see the user who created the schedule.
  3. Filter on **Run Once (Yes/No)** , and set the filter value to `No` to exclude deliveries that were sent once (for example, for a [delivery of a Look](/looker/docs/delivering-looks-explores#creating_a_delivery)) or sent as a one-time test (for example, for the test [delivery of a Look](/looker/docs/delivering-looks-explores#testing_your_schedule)).
  4. You can also add fields like **Cron Schedule** and **Timezone** from the **Scheduled Plan** view.

    
    
    https://<instance_name.looker.com>/explore/system__activity/scheduled_plan?fields=scheduled_plan.id,scheduled_plan.name,user.id,scheduled_plan.next_run_time,scheduled_plan.cron_schedule,scheduled_plan.timezone,user.name&f[scheduled_plan.run_once]=No&sorts=scheduled_plan.timezone+desc&limit=500&column_limit=50
    

#### At which stage do schedules get stuck?

You can use the **Scheduled Plan** Explore to identify the stage at which schedules get stuck. For example:

  1. To view the stage at which a specific scheduled job got stuck, filter on **ID** from **Scheduled Job** , and set the filter value to the scheduled job's ID. Select **Stage** , **Scheduled Job ID** , and **Runtime in Seconds** from **Scheduled Job Stage**.
  2. You can also select **Started Time** and **Completed Time** from **Scheduled Job Stage**.

You can then use the **ID** and **Runtime in Seconds** fields to troubleshoot the failed job, based on whether the scheduled job was stuck in, for example, the `execute` stage or the `enqueued for delivery` stage.

In the following URL example, you can replace the scheduled job ID `12913` in the filter element `&f[scheduled_job.id]=12913` with the ID for the scheduled job you want to filter on:
    
    
    https://<instance_name.looker.com>/explore/system__activity/scheduled_plan?fields=scheduled_job_stage.stage,scheduled_job_stage.scheduled_job_id,scheduled_job_stage.runtime,scheduled_job_stage.started_time,scheduled_job_stage.completed_time&f[scheduled_job.id]=12913&sorts=scheduled_job_stage.scheduled_job_id+desc&limit=500
    

#### How do I find schedule owners?

You can use the **Scheduled Plan** Explore to find schedule owners:

  1. Select **ID** and **Name** from **Scheduled Plan**.
  2. Select **ID** and **Name** from **User**.
  3. Filter on **Run Once (Yes/No)** , and set the filter value to `No` to exclude deliveries that were sent once (for example, for a [delivery of a Look](/looker/docs/delivering-looks-explores#creating_a_delivery)) or sent as a one-time test (for example, for the test [delivery of a Look](/looker/docs/delivering-looks-explores#testing_your_schedule)).
  4. To find the owner of a specific schedule, filter on **ID** from **Scheduled Plan** , and set the filter value to the ID of that schedule.

    
    
    https://<instance_name.looker.com>/explore/system__activity/scheduled_plan?fields=scheduled_plan.id,scheduled_plan.name,user.id,user.name&f[scheduled_plan.run_once]=No&sorts=scheduled_plan.id&limit=500
    

#### Which scheduled plans run at the same time?

You can use the **Scheduled Plan** Explore to identify plans that are scheduled to run at the same time:

  1. Select **ID** , **Name** , **Cron Schedule** , and **Next Run Time** from **Scheduled Plan**.
  2. Filter on **Run Once (Yes/No)** , and set the filter value to `No` to exclude deliveries that were sent once (for example, for a [delivery of a Look](/looker/docs/delivering-looks-explores#creating_a_delivery)) or sent as a one-time test (for example, for the test [delivery of a Look](/looker/docs/delivering-looks-explores#testing_your_schedule)).
  3. You can also add a filter on **Next Run Time** , and set the filter value to `is not null` to include only existing scheduled deliveries in the results.

You can then change the timing of schedules (for example, for the [delivery of a Look](/looker/docs/delivering-looks-explores#triggering_delivery)) so that multiple schedules will not run at the same time.
    
    
    https://<instance_name.looker.com>/explore/system__activity/scheduled_plan?fields=scheduled_plan.id,scheduled_plan.name,scheduled_plan.cron_schedule,scheduled_plan.next_run_time&f[scheduled_job.run_once]=No&f[scheduled_plan.next_run_time]=NOT+NULL&sorts=scheduled_plan.id&limit=500
    

#### Which schedules are unlimited?

You can use the **Scheduled Plan** Explore to find unlimited schedules, or schedules with a row limit of `-1`:

  1. Filter on **Send All Results** , and set the value to **Yes**.
  2. Select **ID** , **Created Time** , **Finalized Time** , and **Count** from **Scheduled Job**.

    
    
    https://<instance_name.looker.com>/explore/system__activity/scheduled_plan?fields=scheduled_job.id,scheduled_job.created_time,scheduled_job.finalized_time,scheduled_job.count&f[scheduled_plan.send_all_results]=Yes&sorts=scheduled_job.created_time+desc&limit=500
    

#### Is it possible to view history for more than 50 schedules?

Using the **Scheduled Plan** Explore, you can view the histories of more than just the 50 schedules that are available to view on the [**Schedule History**](/looker/docs/admin-panel-alerts-and-schedules-schedule-history) admin page. For example:

  1. Select **ID** from **Scheduled Plan**.
  2. Select **Name** from **User** to see who created each schedule.
  3. Select **Cron Schedule** from **Scheduled Job** to see the scheduled delivery time for each scheduled job as a cron string.
  4. Select **Type** from **Scheduled Plan Destination** to see the destination type (for example, for the [delivery of a Look](/looker/docs/delivering-looks-explores#choosing_the_delivery_destination)).
  5. Select **ID** , **Status** , and **Status Detail** from **Scheduled Job** to view the status and any error messages for each scheduled job.
  6. Select **Created Time** and **Finalized Time** from **Scheduled Job**.
  7. Select **Runtime in Seconds** from **Scheduled Job Stage**.
  8. You can also select **Link** from either the **Look** view or the **Dashboard** view for a link to the Look or dashboard for a schedule.
  9. To limit results to only a specific timeframe, add a filter on **Created Date** from **Scheduled Job** , and set the filter value to the desired length of time, such as `is in the past 7 days`.
  10. Filter on **Run Once (Yes/No)** , and set the filter value to `No` to exclude deliveries that were sent once (for example, for a [delivery of a Look](/looker/docs/delivering-looks-explores#creating_a_delivery)) or sent as a one-time test (for example, for the test [delivery of a Look](/looker/docs/delivering-looks-explores#testing_your_schedule)).

    
    
    https://<instance_name.looker.com>/explore/system__activity/scheduled_plan?fields=scheduled_plan.id,user.name,scheduled_job.cron_schedule,scheduled_plan_destination.type,scheduled_job.id,scheduled_job.status,scheduled_job.status_detail,scheduled_job.created_time,scheduled_job.finalized_time,scheduled_job_stage.runtime,look.link,dashboard.link&f[scheduled_plan.run_once]=No&f[scheduled_job.created_date]=7+days&sorts=scheduled_job.created_time+desc&limit=500
    
    

#### How do I filter results down to a specific set of schedules?

You can use the **Scheduled Plan** Explore to view only a specific set of schedules by filtering, for example, on specific dashboards, owners, or models. For example, to view a list of schedules based on a specific model, such as `thelook`:

  1. Add a filter on **Model** from the **Query** view, and set the filter value to the name of the model.
  2. Select **ID** and **Name** from **Scheduled Plan**.
  3. Select **Name** from **User** to see who created each schedule.
  4. Select **Cron Schedule** from **Scheduled Plan** to see the scheduled delivery time for each schedule as a cron string.
  5. You can also select **Link** from either the **Look** view or the **Dashboard** view for a link to the Look or dashboard for a schedule.
  6. Filter on **Run Once (Yes/No)** , and set the filter value to `No` to exclude deliveries that were sent once (for example, for a [delivery of a Look](/looker/docs/delivering-looks-explores#creating_a_delivery)) or sent as a one-time test (for example, for the test [delivery of a Look](/looker/docs/delivering-looks-explores#testing_your_schedule)).

In the following URL example, you can replace the model name `thelook` in the filter element `f[query.model]=thelook` with the name of the model you want to filter on:
    
    
    https://<instance_name.looker.com>/explore/system__activity/scheduled_plan?fields=scheduled_plan.id,scheduled_plan.name,user.name,scheduled_plan.cron_schedule,look.link,dashboard.link&f[scheduled_plan.run_once]=No&f[query.model]=thelook&sorts=scheduled_plan.id&limit=500
    

#### Can error trends be identified across schedules?

Another use case for the **Scheduled Plan** Explore can be to identify error trends across schedules, such as, for example, finding that SFTP schedules are failing with a specific error message:

  1. Select **Created Time** , **Finalized Time** , **ID** , **Status** , and **Status Detail** from **Scheduled Job** to see a list of scheduled jobs and their statuses and error messages.
  2. Select **Stage** from **Scheduled Job Stage**.
  3. Select **Type** and **Format** from **Scheduled Plan Destination** to see the destination type (for example, for the [delivery of a Look](/looker/docs/delivering-looks-explores#choosing_the_delivery_destination)) and data format (for example, for the [delivery of a Look](/looker/docs/delivering-looks-explores#choosing_the_data_format)).
  4. Filter on **Status** from **Scheduled Job** , and set the filter value to `failure` to include only scheduled jobs that have failed.
  5. To include results for only a specific destination, filter on the **Type** field from **Scheduled Plan Destination** , and set the filter value to the desired destination, such as `sftp` or `email`.

    
    
    https://<instance_name.looker.com>/explore/system__activity/scheduled_plan?fields=scheduled_job.created_time,scheduled_job.finalized_time,scheduled_job.id,scheduled_job.status,scheduled_job.status_detail,scheduled_job_stage.stage,scheduled_plan_destination.type,scheduled_plan_destination.format&f[scheduled_job.status]=failure&sorts=scheduled_job.status&limit=500&column_limit=50
    

#### How do I view runtime metrics for schedules?

You can use the **Scheduled Plan** Explore to investigate runtime metrics for schedules. For example, to view the average runtimes for schedules:

  1. Select **ID** and **Name** from **Scheduled Plan**.
  2. Select **Name** from **User**.
  3. Select **Cron Schedule** from **Scheduled Plan**.
  4. Select **Average Runtime in Seconds** from **Scheduled Job Stage**.
  5. Filter on **Run Once (Yes/No)** , and set the filter value to `No` to exclude deliveries that were sent once (for example, for a [delivery of a Look](/looker/docs/delivering-looks-explores#creating_a_delivery)) or sent as a one-time test (for example, for the test [delivery of a Look](/looker/docs/delivering-looks-explores#testing_your_schedule)).

    
    
    https://<instance_name.looker.com>/explore/system__activity/scheduled_plan?fields=scheduled_plan.id,scheduled_plan.name,user.name,scheduled_plan.cron_schedule,scheduled_job_stage.avg_runtime&f[scheduled_plan.run_once]=No&sorts=scheduled_plan.id&limit=500
    

To see runtimes for scheduled jobs:

  1. To view runtimes for all the jobs for a specific plan, add a filter on **ID** from **Scheduled Plan** , and set the filter value to the desired scheduled plan ID.
  2. Select **ID** from **Scheduled Plan**.
  3. Select **Name** from **User**.
  4. Select **Cron Schedule** from **Scheduled Plan**.
  5. Select **ID** , **Status** , **Created Time** , and **Finalized Time** from **Scheduled Job**.
  6. Select **Runtime in Seconds** from **Scheduled Job Stage**.
  7. Filter on **Run Once (Yes/No)** , and set the filter value to `No` to exclude deliveries that were sent once (for example, for a [delivery of a Look](/looker/docs/delivering-looks-explores#creating_a_delivery)) or sent as a one-time test (for example, for the test [delivery of a Look](/looker/docs/delivering-looks-explores#testing_your_schedule)).

To change the filter on **ID** from **Scheduled Plan** in the following URL example, replace `145` in the filter element `f[scheduled_plan.id]=145` with the ID of the scheduled plan you want to filter on:
    
    
    https://<instance_name.looker.com>/explore/system__activity/scheduled_plan?fields=scheduled_plan.id,user.name,scheduled_job.cron_schedule,scheduled_job.id,scheduled_job.status,scheduled_job.created_time,scheduled_job.finalized_time,scheduled_job_stage.runtime&f[scheduled_plan.run_once]=No&f[scheduled_plan.id]=145&sorts=scheduled_job.created_time+desc&limit=500
    

### User

The **User** Explore includes details about each user, including historical queries run, and the content and folders to which they have access.

#### Quick Start analyses

The **User** Explore includes [Quick Start](/looker/docs/creating-and-editing-explores#quick_start_analyses) analyses, which you can use to quickly answer questions or as starting points for other queries.

![](/static/looker/docs/images/user-quick-start-2308.png)

Select a Quick Start analysis tile in a blank Explore, or from the [lightning bolt **Quick Start** menu](/looker/docs/creating-and-editing-explores#choosing_a_quick_start_option_once_an_explore_has_run) in an Explore that has run, and Looker will show a query with fields that are preselected and sorted to answer one of the following questions:

  * How many enabled users have the viewer permission ([`access_data`](/looker/docs/admin-panel-users-roles#access_data))?
  * Which users had greater than 3 scheduled jobs fail over the past 7 days?
  * When was the last time a particular user logged in?
  * Which users are the most active?
  * Which users haven't logged in for over 90 days?
  * Which users have had access disabled?
  * Which users have the developer permission ([`develop`](/looker/docs/admin-panel-users-roles#develop))?
  * How many users are in each role?

#### How do I view which Google personnel have accessed my instance?

In addition to the **Recent Access** panel in the [**Support Access** page](/looker/docs/admin-panel-general-support-access#support_access_audit), you can view information about which Google personnel have accessed your instance. For example, to view which Google personnel accessed your instance, how many minutes they accessed your instance, and how many queries they ran:

  1. Select **Name** from **User**.
  2. Select **Approximate Web Usage in Minutes** and **Query Counts > Query Run Count** from **History**.
  3. Filter on **Created Date > Date** in **History** , and set the value to the time period for which you want to view access by Google personnel.
  4. Filter on **Source > Source** in **History** and set the value to `is not equal to` `scheduled_task` to eliminate any scheduled tasks.
  5. Filter on **User Permissions > Is Looker Employee (Yes / No)** in **User Facts** and set the value to `is Yes` to view only Google personnel.

    
    
    https://<instance_name>/explore/system__activity/user?fields=user.name,history.approximate_usage_in_minutes,history.query_run_count_drill&f[user.is_disabled]=No&f[history.created_date]=70+days&f[history.source]=-%22scheduled_task%22&f[user_facts.is_looker_employee]=Yes
    

## Guided analyses in System Activity Labs feature

**Guided analyses** let Looker admins and users who have been granted the [`see_system_activity`](/looker/docs/admin-panel-users-roles#see_system_activity) permission quickly answer key questions about instance usage in the **History** Explore with a question-and-answer format. For users to be able to access guided analyses, an admin must enable the **Guided analyses in System Activity** [Labs feature](/looker/docs/admin-panel-general-labs#guided_analyses_in_system_activity).

A guided analysis includes pre-populated fields, values, and options to select from, as well as a visualization displaying the selected metrics.

![](/static/looker/docs/images/guided-analysis-example-2230.png)

> The visualization type is chosen by Looker to best display the data selected, and it cannot be changed.

Users can currently access several guided analysis options from the **History** Explore:

  * **Which users are most active in your instance?** — Understand who's getting the most value out of your instance
  * **What content is taxing your instance?** — Identify heavily used content
  * **User audit** — Understand user activity by type and role
  * **Instance usage over time** — Compare different activity metrics over time

### Choosing a guided analysis from a blank Explore

To run a guided analysis, select the analysis option that you want to use. Analysis options are displayed in the **Guided Analysis** section.

![](/static/looker/docs/images/guided-analysis-from-blank-explore-2206.png)

Once the guided analysis has run, you can customize the data values to answer key questions, explore further into the analysis, or save the analysis to share with other users who have access. To close the analysis, simply close its browser tab.

### Choosing a guided analysis once an Explore has run

If you have already run a System Activity **History** Explore, you can select a guided analysis by selecting the **Quick Start** button next to the Explore name.

![](/static/looker/docs/images/explore-quick-start-access-modal-2408.png)

This action launches the **Quick Start** menu.

![](/static/looker/docs/images/guided-analysis-from-a-run-explore-2206.png)

Select a guided analysis from the **Quick Start** menu to open and run the guided analysis in a new browser tab.

Once the guided analysis has run, you can customize the data values to answer key questions, explore further into the analysis, or save the analysis to share with other users who have access. To close the analysis, simply close its browser tab.

### Customizing a guided analysis

Once you have selected a guided analysis from a blank Explore or an Explore's **Quick Start** menu, the analysis will automatically open and run in a new browser tab.

When the guided analysis has finished running, you can change and create combinations of pre-populated values by selecting values and conditions from drop-down menus, date menus, or radio button options, depending upon the analysis.

For example, you can select the **What content is taxing your instance?** analysis to identify heavily used content on your Looker instance. After the guided analysis has loaded, you can change the default timeframe value in **Over what timeframe?** to **Last 30 days**.

![](/static/looker/docs/images/using-guided-analysis-2214.png)

The guided analysis will automatically update with the selected timeframe value.

![](/static/looker/docs/images/using-guided-analysis-2-2300.png)

At this stage, you can choose whether to make additional insights into the analysis by exploring the data further. You can save the analysis as a Look or to a dashboard to share with other users who have access, or you can close the analysis by closing its browser window.

### Guided Analysis three-dot Options menu

The three-dot **Options** menu in a guided analysis lets users:

  * Explore further into a guided analysis
  * Save a guided analysis
  * Reload a guided analysis

![](/static/looker/docs/images/guided-analysis-three-dot-options-menu-2204.png)

#### Exploring further into a guided analysis

Once you have the initial data from a guided analysis, you may choose to further explore the data. To do so, you can select the three-dot **Options** menu, and then select **Explore from Here**.

![](/static/looker/docs/images/guided-analysis-explore-from-here-2300.png)

A new browser tab will open with an Explore that is pre-loaded with the fields and visualization from the guided analysis.

![](/static/looker/docs/images/guided-analysis-explore-from-here-2-2218.png)

You can make further data insights by adding or removing fields, pivots, or filters, among other customizations. See the [**Creating and editing Explores**](/looker/docs/creating-and-editing-explores) documentation page for more Explore best practices and tips.

#### Saving a guided analysis

After customizing a guided analysis, you may want to save the analysis to share with others that have access. You can save a guided analysis in two ways:

  * Add the guided analysis visualization to a dashboard
  * Save the guided analysis as a Look

**Adding a guided analysis visualization to a dashboard**

To add a guided analysis visualization to a dashboard, open the **Save Guided Analysis to a Dashboard** menu by selecting **\+ Add to Dashboard** from the three-dot **Options** menu.

![](/static/looker/docs/images/guided-analysis-save-to-dashboard-2300.png)

Once the **Save Guided Analysis to a Dashboard** menu opens, follow these steps:

![](/static/looker/docs/images/guided-analysis-save-to-dashboard-2-2414.png)

  1. Input a title for the guided analysis dashboard tile.
  2. Select a folder where the dashboard to which you would like to add the guided analysis is saved.
  3. Select the desired dashboard.
  4. Select **Save**.

A dialog box will pop up to notify you that the guided analysis has been added to the selected dashboard.

![](/static/looker/docs/images/guided-analysis-save-to-dashboard-3-2204.png)

  5. Select the link to navigate to the dashboard to view or make [edits](/looker/docs/editing-user-defined-dashboards) to the dashboard.

  6. Alternatively, select **Done** to exit the pop-up.

**Saving a guided analysis as a Look**

To save a guided analysis as a Look, select the **Explore from Here** option from the three-dot **Options** menu:

![](/static/looker/docs/images/guided-analysis-explore-from-here-2300.png)

A new browser tab will open with an Explore that is pre-loaded with the fields and visualization from the guided analysis:

![](/static/looker/docs/images/guided-analysis-explore-from-here-2-2414.png)

Follow these steps to save the Explore as a Look:

![](/static/looker/docs/images/save-look-from-explore-2314.png)

  1. In the upper right of the Explore, select the gear menu.
  2. Choose **Save**.
  3. Select **As a Look** to open the **Save Look** menu.

![](/static/looker/docs/images/save-look-from-explore-2-2312.png)

  4. In the **Title** field, enter a new title. If you will be saving over an existing Look, leave this field blank.

  5. In the **Description** field, you can enter a description of the Look. If you will be saving over an existing Look, leave this field blank.

  6. In the **Folder** field, check whether the current folder is the desired destination. The **Folder** field shows the name and location of the selected folder, and the right side displays the contents of the selected folder. If you choose a folder in which you are not allowed to save the Look, a warning will be displayed at the bottom of the menu, and the **Save & View Look** button will be deactivated.

  7. If you want to save to a different folder, navigate to the folder where you want to save your Look. You can navigate to the folder in any of the following ways:

     * In the **Folder** field, select any parent folders to navigate there.
     * On the left side, select the name of a top-level folder to navigate to it.
     * On the right side, select the name of a subfolder you would like to use or navigate to one of its subfolders.
     * If there are many subfolders, you can enter the subfolder name into the **Filter by title** field to have the list filtered to just that subfolder. 

  8. If you want to save over an existing Look, scroll down or use the **Filter by title** field to find and select the desired Look. The Look's title and description (if any) appear in the **Title** and **Description** fields.

  9. Save your Look.

     * To save your Look and return to the Explore page, select **Save**.
     * To save and view your Look, select **Save & View Look**.

You can also select other options from the Explore to save or share the **Guided Analysis** Explore, such as:

  * [**Download**](/looker/docs/downloading#downloading_data_from_a_look_or_an_explore) — To download the **Guided Analysis** Explore
  * [**Send**](/looker/docs/send-once) — To send the **Guided Analysis** Explore as a one-off delivery
  * [**Save and Schedule**](/looker/docs/scheduling#delivery_options) — To save the **Guided Analysis** Explore as a Look or dashboard and set a recurring delivery
  * [**Merge Results**](/looker/docs/merged-results) — To merge the **Guided Analysis** Explore results with other Explore results

#### Reloading a guided analysis

To reload the data in a guided analysis, select the **Reload** option from the three-dot **Options** menu.

![](/static/looker/docs/images/guided-analysis-reload-2300.png)

The guided analysis will refresh and display the latest data.