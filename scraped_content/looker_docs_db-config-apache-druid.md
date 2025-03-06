# https://cloud.google.com/looker/docs/db-config-apache-druid

Depth: 3

## Encrypting network traffic  
  
It is a best practice to encrypt network traffic between the Looker application and your database. Consider one of the options described on the [Enabling secure database access](/looker/docs/enabling-secure-db-access) documentation page.

## Configuring your Apache Druid cluster

`<DRUID_BASE_DIR>` refers to the base directory in which the Apache Druid cluster is installed on a server.

### Enabling SQL

To enable SQL on your Druid database, add this line to the [`broker/runtime.properties`](https://druid.apache.org/docs/latest/configuration/index.html#broker) configuration file:

`<DRUID_BASE_DIR>/conf/druid/broker/runtime.properties`
    
    
    druid.sql.enable=true
    

### Turning off `COUNT DISTINCT` approximation (optional)

By default, Druid approximates `COUNT DISTINCT`. For precise results, add this line to the [`broker/runtime.properties`](https://druid.apache.org/docs/latest/configuration/index.html#broker) configuration file:

`<DRUID_BASE_DIR>/conf/druid/broker/runtime.properties`
    
    
    `druid.sql.planner.useApproximateCountDistinct=false`
    

## Creating the Looker connection to your database

In the **Admin** section of Looker, select **Connections** , and then click **Add Connection**.

Fill out the connection details. The majority of the settings are common to most database dialects. See the [Connecting Looker to your database](/looker/docs/connecting-to-your-db) documentation page for information. Some of the settings are described next:

  * **Name** : The name of the connection.
  * **Dialect** : **Apache Druid** , **Apache Druid 0.13+** (Apache Druide 0.13.x - 0.17.x), or **Apache Druid 0.18+**.

**Note:** If you are on a [Looker (Google Cloud core)](/looker/docs/looker-core-overview) instance and you don't see your dialect listed in the **Dialect** drop-down menu, see the [Looker (Google Cloud core) documentation](/looker/docs/looker-core-dialects#supported_dialects_for) to verify that the dialect is supported for Looker (Google Cloud core) instances.
  * **Host** : DNS or IP address of the cluster [Broker](https://druid.apache.org/docs/latest/design/broker.html). You can find this in your [`broker/runtime.properties`](https://druid.apache.org/docs/latest/configuration/index.html#broker) file.

  * **Port** : The port of the [Broker](https://druid.apache.org/docs/latest/design/broker.html). The default port is 8082. If your cluster is secured by SSL, the default port is 8182.

  * **Database** : The name of your database. The default is `druid`.

  * **Username** : The database username if your Apache Druid cluster is configured to use [Druid Basic Security](https://druid.apache.org/docs/latest/development/extensions-core/druid-basic-security.html). If it is not, then you can specify any string.

  * **Password** : The user password. If your cluster is not configured to use [Druid Basic Security](https://druid.apache.org/docs/latest/development/extensions-core/druid-basic-security.html), then you can specify any string.

  * **Schema** : The default schema to use when there is no schema specified. Entering a schema is optional. 

  * **Additional JDBC parameters** : Semicolon delimited [Avatica JDBC parameters](https://calcite.apache.org/avatica/docs/client_reference.html).

    * These properties can be set as connection properties: 
      * `useApproximateCountDistinct`
      * `useApproximateTopN`
      * `useFallback`
      * `sqlTimeZone`

Example: `none useApproximateCountDistinct=false;truststore=/path/to/truststore.jks;truststore_password=changeit`

  * **Datagroup and PDT Maintenance Schedule** : A [`cron`](https://en.wikipedia.org/wiki/Cron#CRON_expression) expression that indicates when Looker should check [datagroups](/looker/docs/caching-and-datagroups#specifying_caching_policies_with_datagroup_parameters) and persistent derived tables. Read more about this setting in the [Datagroup and PDT Maintenance Schedule](/looker/docs/connecting-to-your-db#pdt_maintenance_schedule) documentation.

  * **SSL** : Check if your Apache Druid cluster is configured to use [Druid TLS](https://druid.apache.org/docs/latest/operations/tls-support.html).

  * **Verify SSL** : Check to enforce strict hostname verification.

  * **Max connections per node** : The default is 25. This setting can be left at the default value initially. See the [Connecting Looker to your database](/looker/docs/connecting-to-your-db#max_connections) documentation page for more information.

  * **Connection Pool Timeout** : The default is 120 seconds.

  * **SQL Runner Precache** : To cause SQL Runner not to preload table information and to load table information only when a table is selected, clear this option. Read more about this setting in the [SQL Runner Precache](/looker/docs/connecting-to-your-db#sql_runner_precache) documentation.

  * **Database Time Zone** : Database timezone. Supported in Apache Druid 0.13+ and Apache Druid 0.18+.

To verify that the connection is successful, click **Test**. See the [Testing database connectivity](/looker/docs/testing-db-connectivity) documentation page for troubleshooting information.

Looker runs a `SELECT 1` query to verify a basic connection and perform a query test. It does not validate that the catalog and schema combination exist or that the user has the required access to that schema.

If you have any issues, check out our [Testing Connections](/looker/docs/admin-panel-database-connections#testing_connections) documentation.

To save these settings, click **Connect**.

Test the connection in SQL Runner. Navigate to [SQL Runner](/looker/docs/sql-runner-basics), select your connection and schema, then [check if you can see your database tables](/looker/docs/sql-runner-basics-manage-db#getting_table_information).

## Feature support

For Looker to support some features, your database dialect must also support them.

### Apache Druid

Apache Druid supports the following features as of Looker 25.2:

Feature | Supported?  
---|---  
Support Level | Supported  
Looker (Google Cloud core) | No  
Symmetric Aggregates | No  
Derived Tables | Yes  
Persistent SQL Derived Tables | No  
Persistent Native Derived Tables | No  
Stable Views | No  
Query Killing | No  
SQL-based Pivots | No  
Timezones | No  
SSL | Yes  
Subtotals | No  
JDBC Additional Params | Yes  
Case Sensitive | Yes  
Location Type | Yes  
List Type | No  
Percentile | No  
Distinct Percentile | No  
SQL Runner Show Processes | No  
SQL Runner Describe Table | No  
SQL Runner Show Indexes | No  
SQL Runner Select 10 | Yes  
SQL Runner Count | Yes  
SQL Explain | Yes  
Oauth Credentials | No  
Context Comments | Yes  
Connection Pooling | No  
HLL Sketches | No  
Aggregate Awareness | No  
Incremental PDTs | No  
Milliseconds | Yes  
Microseconds | No  
Materialized Views | No  
Approximate Count Distinct | No  
  
### Apache Druid 0.13+ (Apache Druide 0.13.x - 0.17.x)

Apache Druid 0.13+ supports the following features as of Looker 25.2:

Feature | Supported?  
---|---  
Support Level | Supported  
Looker (Google Cloud core) | No  
Symmetric Aggregates | No  
Derived Tables | Yes  
Persistent SQL Derived Tables | No  
Persistent Native Derived Tables | No  
Stable Views | No  
Query Killing | No  
SQL-based Pivots | No  
Timezones | Yes  
SSL | Yes  
Subtotals | No  
JDBC Additional Params | Yes  
Case Sensitive | Yes  
Location Type | No  
List Type | No  
Percentile | No  
Distinct Percentile | No  
SQL Runner Show Processes | No  
SQL Runner Describe Table | No  
SQL Runner Show Indexes | No  
SQL Runner Select 10 | Yes  
SQL Runner Count | Yes  
SQL Explain | Yes  
Oauth Credentials | No  
Context Comments | Yes  
Connection Pooling | No  
HLL Sketches | No  
Aggregate Awareness | No  
Incremental PDTs | No  
Milliseconds | Yes  
Microseconds | No  
Materialized Views | No  
Approximate Count Distinct | No  
  
### Apache Druid 0.18+

Apache Druid 0.18+ supports the following features as of Looker 25.2:

Feature | Supported?  
---|---  
Support Level | Supported  
Looker (Google Cloud core) | Yes  
Symmetric Aggregates | No  
Derived Tables | Yes  
Persistent SQL Derived Tables | No  
Persistent Native Derived Tables | No  
Stable Views | No  
Query Killing | No  
SQL-based Pivots | No  
Timezones | Yes  
SSL | Yes  
Subtotals | No  
JDBC Additional Params | Yes  
Case Sensitive | Yes  
Location Type | Yes  
List Type | No  
Percentile | No  
Distinct Percentile | No  
SQL Runner Show Processes | No  
SQL Runner Describe Table | No  
SQL Runner Show Indexes | No  
SQL Runner Select 10 | Yes  
SQL Runner Count | Yes  
SQL Explain | Yes  
Oauth Credentials | No  
Context Comments | Yes  
Connection Pooling | No  
HLL Sketches | No  
Aggregate Awareness | No  
Incremental PDTs | No  
Milliseconds | Yes  
Microseconds | No  
Materialized Views | No  
Approximate Count Distinct | No  
  
## Next steps

After you have completed the database connection, [configure authentication options](/looker/docs/getting-started-with-users).