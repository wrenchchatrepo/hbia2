# https://cloud.google.com/looker/docs/query-performance-metrics

Depth: 3

The **Query Performance Metrics** Explore in [System Activity](/looker/docs/usage-reports-with-system-activity-explores) provides detailed breakdowns of each query that is run from your Looker instance.

For example, you can use this Explore to investigate which components of a query took longest to load. You can also use this Explore to identify query performance trends and anomalies.

For more information about the Explores available in System Activity, see the [Creating Looker usage reports with System Activity Explores](/looker/docs/usage-reports-with-system-activity-explores) documentation page.

## Viewing query performance metrics

Query performance metrics are visible in the System Activity **Query Performance Metrics** Explore. You must be a Looker admin or have the `see_system_activity` permission to view the **Query Performance Metrics** Explore.

## Understanding the Looker query lifecycle

Each query that Looker sends to your database goes through several phases, each with several steps. Each of these steps is represented as a dimension in the **Query Performance Metrics** Explore.

At a high level, the phases can be conceptualized as follows:

  1. **Asynchronous worker phase** : First, the query task must be assigned to an available asynchronous worker. There may be queue time if no worker is available.
  2. **Initialization phase** : Once an asynchronous worker is assigned, the Looker instance runs several initialization steps to prepare the query.
  3. **Connection handling phase** : Once initialization is complete, the Looker instance establishes a connection to the customer database.
  4. **Main query phase** : Once the Looker instance establishes a connection to the customer database, the main query is executed on the customer database. Additional queries to compute results, such as [totals](/looker/docs/table-options#totals), may also be run depending on the options that are chosen for the query. If the query is not [streamed](/looker/docs/downloading#streaming_query_results), then the queries are loaded into memory on the Looker instance. After this, the connection from the Looker instance to the customer database is closed.
  5. **Post-query phase** : Finally, the Looker instance runs several post-query steps to prepare the query for its next destination. At this point, the asynchronous worker is released.

![](/static/looker/docs/images/admin-query-timings-diagram-626.png)

## Query performance metrics

The following sections list each query phase and query step in chronological order.

### Asynchronous worker phase metrics

Query Step | Metric Description  
---|---  
`Queued` | Time in seconds that a query spends waiting for an asynchronous worker to be available to run the query.  
`Async processing` | Time in seconds that an asynchronous worker spends on the query. The worker continues working on the query until after the post-query phase is complete, so this metric will overlap with most other metrics on this page.  
  
### Initialization phase metrics

Query Step | Metric Description  
---|---  
`Model Init: From Cache` | Time it takes in seconds to pull the model definition from cache. If this returns a null value, that means that the model was loaded and parsed instead of pulled from cache. (See the `Model Init: Computed` step.)  
`Model Init: Computed` | Time it takes in seconds to load and parse the model required to run a query. If this returns a null value, that means that the model was retrieved from cache instead of loaded and parsed from scratch. (See the `Model Init: From Cache` step.)  
`Explore Init: From Cache` | Time it takes in seconds to pull the Explore initialization from cache. If this returns a null value, that means that the Explore was loaded and parsed instead of pulled from cache. (See the `Explore Init: Computed` step.)  
`Explore Init: Computed` | Time it takes in seconds to initialize the Explore before starting to `prepare` it. If this returns a null value, that means that the Explore was retrieved from cache instead of loaded and parsed from scratch. (See the `Explore Init: From Cache` step.)  
`Prepare` | Time it takes in seconds to prepare the query from the Explore definition.  
  
### Connection handling phase metrics

Query Step | Metric Description  
---|---  
`Per User Throttler` | Time in seconds that the query spends waiting for a connection to be available for the user to run the query.  
`Acquire Connection` | Time it takes in seconds for the Looker instance to acquire a connection to the customer database. This includes time to look up the credentials for the user, create the connection pool if it does not already exist, and initialize the connection for use.  
`Connection Held` | Time in seconds that the Looker instance maintains a connection to the customer database. This includes the time it takes for the customer database to run the SQL query.  
  
### Main queries phase metrics

Query Step | Metric Description  
---|---  
`Cache Load` | Time it takes in seconds to pull raw results from the [result set cache](/looker/docs/caching-and-datagroups#how_looker_uses_cached_queries).  
`PDTs` | Time it takes in seconds to build the [persistent derived tables](/looker/docs/derived-tables#persistent_derived_tables_\(pdts\)) that are required for the query.  
`Execute Main Query` | Time it takes in seconds to run the `primary` query on the customer database. This does not include the time it takes to acquire a connection on the customer database. This is not tracked for queries that require the use of the **[Allow large results](/looker/docs/downloading#allow_large_results)** feature.  
`Execute Totals Query` | Time it takes in seconds to run the query to generate totals on the customer database. Only applies to queries with [totals](/looker/docs/table-options#totals) enabled.  
`Execute Row Totals Query` | Time it takes in seconds to run the query to generate row totals on the customer database. Only applies to queries with [row totals](/looker/docs/table-options#row_totals) enabled.  
`Execute Grand Totals Query` | Time it takes in seconds to run the query to generate the grand total on the customer database. Only applies to queries with both [totals](/looker/docs/table-options#totals) and [row totals](/looker/docs/table-options#row_totals) enabled.  
`Load Process and Stream Main Query` | Time it takes in seconds to load the main query (from the customer database), process it (on the Looker instance), and stream it (to the client). Only applies to [streamed](/looker/docs/downloading#streaming_query_results) queries.  
`Load Main Query In Memory` | Time it takes in seconds to load the main query results in memory from the customer database. Only applies to [non-streamed](/looker/docs/downloading#streaming_query_results) queries.  
`Load Totals Query In Memory` | Time it takes in seconds to load the query to generate totals into memory. Only applies to [non-streamed](/looker/docs/downloading#streaming_query_results) queries with [totals](/looker/docs/table-options#totals) enabled.  
`Load Row Totals Query In Memory` | Time it takes in seconds to load the query to generate row totals into memory. Only applies to [non-streamed](/looker/docs/downloading#streaming_query_results) queries with [row totals](/looker/docs/table-options#row_totals) enabled.  
`Load Grand Totals Query In Memory` | Time it takes in seconds to load the query to generate the grand total into memory. Only applies to [non-streamed](/looker/docs/downloading#streaming_query_results) queries with both [totals](/looker/docs/table-options#totals) and [row totals](/looker/docs/table-options#row_totals) enabled.  
  
### Post-query phase metrics

Query Step | Metric Description  
---|---  
`Postprocessing` | Time in seconds necessary for post-processing the query. Occurs after the connection is closed.  
`Stream to Cache` | Time it takes in seconds to process and stream results to the render cache.  
  
## BigQuery BI Engine metrics

If you are using [BigQuery BI Engine](/bigquery/docs/bi-engine-intro) with Looker, you can use the **Query Performance Metrics** Explore to view database-specific information about your queries. Queries that don't use BI Engine and queries of databases other than BigQuery databases return null values for these metrics.

Metric | Metric Description  
---|---  
`BigQuery Job ID` | The job ID in BigQuery for the query.  
`BI Engine Mode` | Whether the query was able to run partially or fully accelerated. See [BI Engine acceleration statistics](/bigquery/docs/bi-engine-monitor#query_statistics) for more information on the possible values for this field.  
`BI Engine Reason` | If the query was not able to run fully accelerated, this field displays the reason. This message comes directly from Google BigQuery.  
  
## Troubleshooting with query performance metrics

Analyzing query metrics can help improve performance on your Looker instance. To get started, select the [**Performance Recommendations** dashboard](/looker/docs/system-activity-dashboards#performance_recommendations_dashboard) from the list of [System Activity dashboards](/looker/docs/system-activity-dashboards).