# https://cloud.google.com/looker/docs/db-config-amazon-aurora-mysql

Depth: 3

To connect Looker to [Amazon Aurora MySQL](https://aws.amazon.com/rds/aurora/), follow the instructions found on the documentation page for connecting to [Amazon RDS for MySQL](/looker/docs/db-config-mysql-on-amazon-rds).

In addition to the steps in the [Amazon RDS instructions](/looker/docs/db-config-mysql-on-amazon-rds), Amazon Aurora may need further setup, depending on your configuration. If you have a redirected read-only endpoint for Amazon Aurora, or if you want to use [persistent derived tables (PDTs)](/looker/docs/derived-tables#persistent_derived_table), see the following sections.

## Encrypting network traffic

It is a best practice to encrypt network traffic between the Looker application and your database. Consider one of the options described on the [Enabling secure database access](/looker/docs/enabling-secure-db-access) documentation page.

## Alternate failover and load balancing modes

Amazon Aurora MySQL can be configured to use [alternate failover and load balancing modes](https://mariadb.com/kb/en/about-mariadb-connector-j/#failover-and-load-balancing-modes) to choose the appropriate JDBC connection behavior you want. Check the linked documentation to see how these alternative parameters change the behavior.

You can set the `lookerFailover` parameter in the **Additional JDBC parameters** field to control these modes.

The options can be used to change the JDBC string as follows:

  * `lookerFailover=false`: `jdbc:mysql:hostname...`
  * `lookerFailover=sequential`: `jdbc:mysql:sequential:hostname...`
    * You can do the same with `lookerFailover=loadbalance`, `lookerFailover=replication`, and `lookerFailover=aurora`
  * If `lookerFailover` is not included, the default behavior is: `jdbc:mysql:aurora:hostname...`
  * If `cluster-ro` is in the hostname, the default behavior is: `jdbc:mysql:hostname...`

## Configuring Amazon Aurora MySQL for PDTs

In order to use [persistent derived tables (PDTs)](/looker/docs/derived-tables#persistent_derived_table) with Aurora, you must use MySQL replication, not Amazon Aurora's default replication, which is read-only. You must set the `read_only` parameter to `0` to make the MySQL replica writable, as described in our documentation on [RDS and temporary tables](/looker/docs/db-config-mysql-on-amazon-rds#rds_&_temporary_tables).

If you _don't_ want to grant write access to the database, you can copy and paste the derived table SQL into the `sql_table_name` parameter of a `view` file as shown here. This creates a subquery that is used at query time:
    
    
    view: my_name {
    sql_table_name: (sql_of_derived_table_goes_here) ;;
    }
    

For more details on Aurora replication, see [the AWS documentation](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Aurora.Replication.html).

## Creating the Looker connection to your database

In the **Admin** section of Looker, select **Connections** , and then click **Add Connection**.

Fill out the connection details. The majority of the settings are common to most database dialects. See the [Connecting Looker to your database](/looker/docs/connecting-to-your-db) documentation page for information.

To verify that the connection is successful, click **Test**. See the [Testing database connectivity](/looker/docs/testing-db-connectivity) documentation page for troubleshooting information.

To save these settings, click **Connect**.

## Feature support

For Looker to support some features, your database dialect must also support them.

Amazon Aurora MySQL supports the following features as of Looker 25.2:

Feature | Supported?  
---|---  
Support Level | Supported  
Looker (Google Cloud core) | Yes  
Symmetric Aggregates | Yes  
Derived Tables | Yes  
Persistent SQL Derived Tables | Yes  
Persistent Native Derived Tables | Yes  
Stable Views | Yes  
Query Killing | Yes  
SQL-based Pivots | Yes  
Timezones | Yes  
SSL | Yes  
Subtotals | Yes  
JDBC Additional Params | Yes  
Case Sensitive | No  
Location Type | Yes  
List Type | Yes  
Percentile | Yes  
Distinct Percentile | Yes  
SQL Runner Show Processes | Yes  
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