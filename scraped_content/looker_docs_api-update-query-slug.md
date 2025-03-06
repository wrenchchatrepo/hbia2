# https://cloud.google.com/looker/docs/api-update-query-slug

Depth: 3

**Note:** The change described on this page will be released in phases: 

  * Looker 24.20 (on December 4, 2024): Americas Early customers
  * Looker 25.0: Americas Mid customers
  * Looker 25.2: General Availability (GA)

The following Looker application API methods don't use a numeric `query_id` value or, in the case of the Query APIs, a numeric `id` value. The following methods use the query slug value instead.

  * Look APIs:

    * [Copy Look](/looker/docs/reference/looker-api/latest/methods/Look/copy_look)
    * [Create Look](/looker/docs/reference/looker-api/latest/methods/Look/create_look)
    * [Get Look](/looker/docs/reference/looker-api/latest/methods/Look/look)
    * [Move Look](/looker/docs/reference/looker-api/latest/methods/Look/move_look)
    * [Search Looks](/looker/docs/reference/looker-api/latest/methods/Look/search_looks)
    * [Update Look](/looker/docs/reference/looker-api/latest/methods/Look/update_look)
    * [Get All Looks](/looker/docs/reference/looker-api/latest/methods/Look/all_looks)
  * Dashboard APIs:

    * [Search Dashboard Elements](/looker/docs/reference/looker-api/latest/methods/Dashboard/search_dashboard_elements)
    * [Get DashboardElement](/looker/docs/reference/looker-api/latest/methods/Dashboard/dashboard_element)
    * [Update DashboardElement](/looker/docs/reference/looker-api/latest/methods/Dashboard/update_dashboard_element)
    * [Get All DashboardElements](/looker/docs/reference/looker-api/latest/methods/Dashboard/dashboard_dashboard_elements)
    * [Create DashboardElement](/looker/docs/reference/looker-api/latest/methods/Dashboard/create_dashboard_element)
  * Render Task APIs:

    * [Create Look Render Task](/looker/docs/reference/looker-api/latest/methods/RenderTask/create_look_render_task)
    * [Create Query Render Task](/looker/docs/reference/looker-api/latest/methods/RenderTask/create_query_render_task)
    * [Create Dashboard Render Task](/looker/docs/reference/looker-api/latest/methods/RenderTask/create_dashboard_render_task)
    * [Get Render Task](/looker/docs/reference/looker-api/latest/methods/RenderTask/render_task)
    * [Create Dashboard Element Render Task](/looker/docs/reference/looker-api/latest/methods/RenderTask/create_dashboard_element_render_task)
  * Scheduled Plan APIs:

    * [Scheduled Plans for Space](/looker/docs/reference/looker-api/latest/methods/ScheduledPlan/scheduled_plans_for_space)
    * [Get Scheduled Plan](/looker/docs/reference/looker-api/latest/methods/ScheduledPlan/scheduled_plan)
    * [Update Scheduled Plan](/looker/docs/reference/looker-api/latest/methods/ScheduledPlan/update_scheduled_plan)
    * [Get All Scheduled Plans](/looker/docs/reference/looker-api/latest/methods/ScheduledPlan/all_scheduled_plans)
    * [Create Scheduled Plan](/looker/docs/reference/looker-api/latest/methods/ScheduledPlan/create_scheduled_plan)
    * [Scheduled Plans for Look](/looker/docs/reference/looker-api/latest/methods/ScheduledPlan/scheduled_plans_for_look)
    * [Scheduled Plans for Dashboard](/looker/docs/reference/looker-api/latest/methods/ScheduledPlan/scheduled_plans_for_dashboard)
    * [Scheduled Plans for LookML Dashboard](/looker/docs/reference/looker-api/latest/methods/ScheduledPlan/scheduled_plans_for_lookml_dashboard)
  * Query APIs:

    * [Run Query Async](/looker/docs/reference/looker-api/latest/methods/Query/create_query_task)
    * [Get Query](/looker/docs/reference/looker-api/latest/methods/Query/query)
    * [Get Query for Slug](/looker/docs/reference/looker-api/latest/methods/Query/query_for_slug)
    * [Create Query](/looker/docs/reference/looker-api/latest/methods/Query/create_query)
    * [Run Query](/looker/docs/reference/looker-api/latest/methods/Query/run_query)
    * [Get Merge Query](/looker/docs/reference/looker-api/latest/methods/Query/merge_query)
    * [Create Merge Query](/looker/docs/reference/looker-api/latest/methods/Query/create_merge_query)
    * [Get All Running Queries](/looker/docs/reference/looker-api/latest/methods/Query/all_running_queries)

## What do I need to do?

The `query_id` field or, in the case of the Query APIs, the `id` field, is a string data type. The `query_id` or `id` fields now return a query slug value in the API response. That query slug value can then be used in any API requests.

For example, if you were to create a query with the **Create Query** API, the `id` would be the query slug in the response. You could then use that `id` to make a subsequent request.

If you have hard-coded numeric query ID values for any of the listed API methods, **you need to update your scripts to use query slug values**!

## How do I find the slug value for a query?

You can find the slug value for a query in the following ways:

  * For an Explore, you can find the slug in the Explore's URL following the `qid=` variable in the URL.

  * You can find the slug value that is associated with a numeric query ID using [System Activity](/looker/docs/usage-reports-with-system-activity-explores).

**Note:** To view the System Activity Explores, you must have a [role](/looker/docs/admin-panel-users-roles) that includes the [`see_system_activity` permission](/looker/docs/admin-panel-users-roles#see_system_activity).
    1. From the Looker **Explore menu** , select the [**System Activity > History** Explore](/looker/docs/usage-reports-with-system-activity-explores#history).

    2. From the **Query** view, select the **ID** and **Link** dimensions.

    3. Optionally, add a filter on the **ID** dimension, and enter the query's numeric query ID in the **Query ID** filter field.

    4. Click **Run**.

![](/static/looker/docs/images/system-activity-get-slug-2420.png)

    5. Click the `[Query]` link next to the numeric query ID in the Explore results to open an Explore based on that numeric query ID.

    6. You can then use the slug in the Explore's URL, which follows the `qid=` variable in the URL.

## How can I tell if we use any of the updated API endpoints?

You can view a list of the API calls that were made to your Looker instance using the [API Usage System Activity Explore](/looker/docs/usage-reports-with-system-activity-explores#api_usage).

  1. From the Looker **Explore** menu, select the **System Activity** Explore, and then select the **API Usage** view.

  2. Select the **Created Date > Date** and **Endpoint** dimensions and the **Total Usage** measure.

  3. Add a filter on the **Endpoint** dimension, and, in the filter field, include any of the updated endpoints listed at the beginning of this document that you want to search for.

  4. Click **Run**. Looker will display usage information for those endpoints.

![](/static/looker/docs/images/sa-api-usage-2420.png)