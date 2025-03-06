# https://cloud.google.com/looker/docs/db-config-apache-hive

Depth: 3

This page contains information about connecting Looker to Apache Hive 2.3+ and Apache Hive 3.1.2+.

Note the following about Looker support for the different versions of Apache Hive:

  * Looker supports connections to Apache Hive 2.3+ and Apache Hive 3.1.2+.
  * For Apache Hive 3.1.2+, Looker can fully integrate with Apache Hive 3 databases only on versions later than 3.1.2. This is because of a [query parsing issue](https://issues.apache.org/jira/browse/HIVE-18624) from Hive versions 2.4.0 - 3.1.2 that resulted in extremely long parsing times for Looker-generated SQL.
  * Looker does not support connections to Apache Hive 2. Queries on connections to Apache Hive 2 will return an error.

## Encrypting network traffic

It is a best practice to encrypt network traffic between the Looker application and your database. Consider one of the options described on the [Enabling secure database access](/looker/docs/enabling-secure-db-access) documentation page.

## Introduction

Looker is architected to connect to a database server using JDBC. In the case of Hive, this is the thrift server (HiveServer2). See the [Apache documentation](https://cwiki.apache.org/confluence/display/Hive/Setting+Up+HiveServer2) for more information.

By default, this server will listen on port 10000.

Looker is an interactive querying tool, so it expects to work with an interactive SQL engine. If Hive is running on MapReduce — `hive.execution.engine` is set to `mr` — then Hive will return query results too slowly to be practical.

Looker was tested with Hive on Tez (`hive.execution.engine=tez`), although it is also possible to run Looker against Hive on Spark. Spark support was added in Hive version 1.1. (Looker supports Hive 1.2.1+.)

## Persistent derived tables (PDTs)

To enable [persistent derived tables (PDTs)](/looker/docs/derived-tables#persistent_derived_table) in Looker using a Hive connection, create a scratch schema for Looker to use. The following is an example of a command you can use to create a `looker_scratch` schema:
    
    
     CREATE SCHEMA looker_scratch;
    

The user account that Looker uses to connect to Hive (which can be anonymous if no authentication is used) must have the following abilities in the scratch schema:

  * Create tables
  * Alter tables
  * Drop tables

Test this with a JDBC client before attempting to create PDTs with Hive.

## Queues

If you want queries from Looker to go into a specific queue, enter the queue name parameter in the **Additional JDBC parameters** field on the [**Connection Settings**](/looker/docs/connecting-to-your-db#additional_params) page:
    
    
    ?tez.queue.name=the_bi_queue
    

Other Hive parameters can be set this way in the **Additional JDBC parameters** field on the [**Connection Settings**](/looker/docs/connecting-to-your-db#additional_params) page.

Using [user attributes](/looker/docs/admin-panel-users-user-attributes), it is possible for queries from different users or different groups of users to go into different queues. To do this, create a user attribute named something like `queue_name`; then, in the **Additional JDBC parameters** field, add the following:
    
    
    ?tez.queue.name={{ _user_attributes['queue_name'] }}
    

You can use this to customize other `hive-site.xml` parameters on a per-user or per-group basis as well.

## Creating the Looker connection to your database

Follow these steps to create the connection from Looker to your database:

  1. In the **Admin** section of Looker, select **Connections** , and then click **Add Connection**.
  2. Select **Apache Hive 2.3+** or **Apache Hive 3.1.2+** from the **Dialect** drop-down menu.

**Note:** If you are on a [Looker (Google Cloud core)](/looker/docs/looker-core-overview) instance and you don't see your dialect listed in the **Dialect** drop-down menu, see the [Looker (Google Cloud core) documentation](/looker/docs/looker-core-dialects#supported_dialects_for) to verify that the dialect is supported for Looker (Google Cloud core) instances.
  3. Fill out the connection details. The majority of the settings are common to most database dialects. See the [Connecting Looker to your database](/looker/docs/connecting-to-your-db) documentation page for information. Some of the settings are described next:

     * **Name** : Specify the name of the connection. This is how you will refer to the connection in LookML projects.
     * **Host** : Specify the hostname.
     * **Port** : Specify the database port.
     * **Database** : Specify the database name.
     * **Username** : Specify the database username.
     * **Password** : Specify the database user password.
     * **Enable PDTs** : Use this toggle to enable [persistent derived tables](/looker/docs/derived-tables#persistent-derived-tables). When PDTs are enabled, the **Connection** window reveals additional PDT settings and the [**PDT Overrides**](/looker/docs/connecting-to-your-db#pdt-overrides) section.
     * **Temp Database** : Specify the name of the scratch schema created in the Persistent derived tables (PDTs) section of this documentation page.
     * **Max number of PDT builder connections** : Specify the number of possible concurrent PDT builds on this connection. Setting this value too high could negatively impact query times. For more information, see the [Connecting Looker to your database](/looker/docs/connecting-to-your-db#max_pdt_builder_connections) documentation page.
     * **Additional JDBC parameters** : Specify any additional JDBC string parameters.
     * **Datagroup and PDT Maintenance Schedule** : Specify a [`cron`](https://en.wikipedia.org/wiki/Cron#CRON_expression) expression that indicates when Looker should check [datagroups](/looker/docs/caching-and-datagroups#specifying_caching_policies_with_datagroup_parameters) and persistent derived tables. [Datagroup and PDT Maintenance Schedule](/looker/docs/connecting-to-your-db#pdt_maintenance_schedule) documentation.
     * **SSL** : Check to use SSL connections.
     * **Verify SSL** : Check for hostname verification.
     * **Max connections per node** : This setting can be left at the default value initially. See the [Connecting Looker to your database](/looker/docs/connecting-to-your-db#max_connections) documentation page for more information.
     * **Connection Pool Timeout** : This setting can be left at the default value initially. Read more about this setting in the [Connection Pool Timeout](/looker/docs/connecting-to-your-db#connection-pool-timeout) section of the **Connecting Looker to your database** documentation page.
     * **SQL Runner Precache** : To cause SQL Runner not to preload table information and to load table information only when a table is selected, uncheck this option. Read more about this setting in the [SQL Runner Precache](/looker/docs/connecting-to-your-db#sql_runner_precache) section of the **Connecting Looker to your database** documentation page.
     * **Database Time Zone** : Specify the time zone used in the database. Leave this field blank if you do not want time zone conversion. See the [Using time zone settings](/looker/docs/using-time-zone-settings) documentation page for more information.
  4. To verify that the connection is successful, click **Test**. See the [Testing database connectivity](/looker/docs/testing-db-connectivity) documentation page for troubleshooting information.

  5. To save these settings, click **Connect**.

## Feature support

For Looker to support some features, your database dialect must also support them.

### Apache Hive 2.3+

**Note:** Looker supports connections to Apache Hive 2.3 and later. Looker does not support connections to Apache Hive 2. Queries on connections to Apache Hive 2 will return an error.

Apache Hive 2.3+ supports the following features as of Looker 25.2:

Feature | Supported?  
---|---  
Support Level | Integration  
Looker (Google Cloud core) | No  
Symmetric Aggregates | No  
Derived Tables | Yes  
Persistent SQL Derived Tables | Yes  
Persistent Native Derived Tables | Yes  
Stable Views | Yes  
Query Killing | Yes  
SQL-based Pivots | No  
Timezones | Yes  
SSL | Yes  
Subtotals | Yes  
JDBC Additional Params | Yes  
Case Sensitive | Yes  
Location Type | Yes  
List Type | Yes  
Percentile | Yes  
Distinct Percentile | No  
SQL Runner Show Processes | No  
SQL Runner Describe Table | Yes  
SQL Runner Show Indexes | Yes  
SQL Runner Select 10 | Yes  
SQL Runner Count | Yes  
SQL Explain | Yes  
Oauth Credentials | No  
Context Comments | Yes  
Connection Pooling | No  
HLL Sketches | No  
Aggregate Awareness | Yes  
Incremental PDTs | No  
Milliseconds | Yes  
Microseconds | Yes  
Materialized Views | No  
Approximate Count Distinct | No  
  
### Apache Hive 3.1.2+

Apache Hive 3.1.2+ supports the following features as of Looker 25.2:

Feature | Supported?  
---|---  
Support Level | Supported  
Looker (Google Cloud core) | Yes  
Symmetric Aggregates | No  
Derived Tables | Yes  
Persistent SQL Derived Tables | Yes  
Persistent Native Derived Tables | Yes  
Stable Views | Yes  
Query Killing | Yes  
SQL-based Pivots | No  
Timezones | Yes  
SSL | Yes  
Subtotals | Yes  
JDBC Additional Params | Yes  
Case Sensitive | Yes  
Location Type | Yes  
List Type | Yes  
Percentile | Yes  
Distinct Percentile | No  
SQL Runner Show Processes | No  
SQL Runner Describe Table | Yes  
SQL Runner Show Indexes | No  
SQL Runner Select 10 | Yes  
SQL Runner Count | Yes  
SQL Explain | Yes  
Oauth Credentials | No  
Context Comments | Yes  
Connection Pooling | No  
HLL Sketches | No  
Aggregate Awareness | Yes  
Incremental PDTs | No  
Milliseconds | Yes  
Microseconds | Yes  
Materialized Views | No  
Approximate Count Distinct | No  
  
## Next steps

After you have connected your database to Looker, [configure sign-in options for your users](/looker/docs/getting-started-with-users).