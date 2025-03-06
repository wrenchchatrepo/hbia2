# https://cloud.google.com/looker/docs/db-config-sap-hana

Depth: 3

This page contains information about connecting Looker to SAP HANA and SAP HANA 2+.

## Encrypting network traffic

It is a best practice to encrypt network traffic between the Looker application and your database. Consider one of the options described on the [Enabling secure database access](/looker/docs/enabling-secure-db-access) documentation page.

## Creating the Looker user

Create a Looker database user with a secure password.
    
    
    CREATE USER LOOKER PASSWORD <SOME_PASSWORD>
    

### Granting permissions

Grant read permissions on the schema(s) that you would like to use in Looker.
    
    
    GRANT SELECT ON SCHEMA <YOUR_SCHEMA> TO LOOKER
    

### Setting up a PDT schema

If using PDTs, create a scratch schema for PDTs to be written into.
    
    
    CREATE SCHEMA LOOKER_SCRATCH OWNED BY LOOKER
    

## Creating the Looker connection to your database

In the **Admin** section of Looker, select **Connections** , and then click **Add Connection**.

Fill out the connection details. The majority of the settings are common to most database dialects. See the [Connecting Looker to your database](/looker/docs/connecting-to-your-db) documentation page for information. Some of the settings are described next:

  * **Name** : The name of the connection. This is how you will refer to the connection in LookML projects.
  * **Dialect** : **SAP HANA** or **SAP HANA 2+**.
  * **Port** : The database port. The default port is 30015.
  * **Host** : Hostname.
  * **Database** : The name of your database.
  * **Username** : The database username.
  * **Password** : The user password.
  * **Schema** : The default schema to use when none is specified. Entering a schema is optional.
  * **Enable PDTs** : Use this toggle to enable [persistent derived tables (PDTs)](/looker/docs/derived-tables#persistent-derived-tables). This reveals additional PDT fields and the [**PDT Overrides**](/looker/docs/connecting-to-your-db#pdt-overrides) section for the connection.
  * **Temp Database** : Schema to use for PDTs.
  * **Additional JDBC Parameters** : Any additional [SAP HANA JDBC connection properties](https://help.sap.com/viewer/0eec0d68141541d1b07893a39944924e/2.0.02/en-US/109397c2206a4ab2a5386d494f4cf75e.html).
  * **Datagroup and PDT Maintenance Schedule** : A [`cron`](https://en.wikipedia.org/wiki/Cron#CRON_expression) expression that indicates when Looker should check [datagroups](/looker/docs/caching-and-datagroups#specifying_caching_policies_with_datagroup_parameters) and persistent derived tables. Read more about this setting in the [Datagroup and PDT Maintenance Schedule](/looker/docs/connecting-to-your-db#pdt_maintenance_schedule) documentation.
  * **SSL** : Check to enable SSL.
  * **Verify SSL** : Check to enforce strict hostname verification.
  * **Max connections per node** : The default is 25. This value can be left at the default value initially. Read more about this setting in the [Max connections per node](/looker/docs/connecting-to-your-db#max_connections) section of the **Connecting Looker to your database** documentation page.
  * **Connection Pool Timeout** : The default is 120 seconds.
  * **SQL Runner Precache** : To cause SQL Runner not to preload table information and to load table information only when a table is selected, uncheck this option. Read more about this setting in the [SQL Runner Precache](/looker/docs/connecting-to-your-db#sql_runner_precache) documentation.
  * **Database Time Zone** : Specify the time zone used in the database. Leave this field blank if you do not want time zone conversion. See the [Using time zone settings](/looker/docs/using-time-zone-settings) documentation page for more information.

To verify that the connection is successful, click **Test**. See the [Testing database connectivity](/looker/docs/testing-db-connectivity) documentation page for troubleshooting information.

To save these settings, click **Connect**.

Test the connection in SQL Runner. Navigate to [SQL Runner](/looker/docs/sql-runner-basics), select your connection and schema, and then [check if you can see your database tables](/looker/docs/sql-runner-basics-manage-db#getting_table_information).

## Feature support

For Looker to support some features, your database dialect must also support them. The following sections show the feature support for SAP HANA and SAP HANA 2+.

### SAP HANA

SAP HANA supports the following features as of Looker 25.2:

Feature | Supported?  
---|---  
Support Level | Supported  
Looker (Google Cloud core) | No  
Symmetric Aggregates | Yes  
Derived Tables | Yes  
Persistent SQL Derived Tables | Yes  
Persistent Native Derived Tables | Yes  
Stable Views | Yes  
Query Killing | Yes  
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
SQL Runner Show Processes | Yes  
SQL Runner Describe Table | Yes  
SQL Runner Show Indexes | No  
SQL Runner Select 10 | Yes  
SQL Runner Count | Yes  
SQL Explain | No  
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
  
### SAP HANA 2+

SAP HANA 2+ supports the following features as of Looker 25.2:

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
SQL Runner Show Processes | Yes  
SQL Runner Describe Table | Yes  
SQL Runner Show Indexes | No  
SQL Runner Select 10 | Yes  
SQL Runner Count | Yes  
SQL Explain | No  
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

After completing the database connection, [configure authentication options](/looker/docs/getting-started-with-users).