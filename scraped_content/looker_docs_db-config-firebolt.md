# https://cloud.google.com/looker/docs/db-config-firebolt

Depth: 3

## Encrypting network traffic  
  
It is a best practice to encrypt network traffic between the Looker application and your database. Consider one of the options described on the [Enabling secure database access](/looker/docs/enabling-secure-db-access) documentation page.

## Create a Looker user

In Firebolt, create a user email and password for Looker to use to connect to your Firebolt instance.

## Creating the Looker connection to your database

Follow these steps to create the connection from Looker to your database:

  1. In the **Admin** section of Looker, select **Connections** , and then click **Add Connection**.
  2. Fill out the connection details. The majority of the settings are common to most database dialects. See the [Connecting Looker to your database](/looker/docs/connecting-to-your-db) documentation page for information. Some of the settings are described next:

     * **Name** : Specify the name of the connection. This is how you will refer to the connection in LookML projects.
     * **Dialect** : Specify the dialect **Firebolt**.
**Note:** If you are on a [Looker (Google Cloud core)](/looker/docs/looker-core-overview) instance and you don't see your dialect listed in the **Dialect** drop-down menu, see the [Looker (Google Cloud core) documentation](/looker/docs/looker-core-dialects#supported_dialects_for) to verify that the dialect is supported for Looker (Google Cloud core) instances.
     * **Host** : Specify the endpoint: `api.app.firebolt.io`
     * **Port** : Specify the database port. The default is 443.
     * **Database** : Specify the database name.
     * **Username** : Enter the database user email.
     * **Password** : Enter the database user password.
     * **Additional JDBC parameters** : Add any additional Firebolt JDBC parameters
     * **SSL** : Check to use SSL connections.
     * **Verify SSL** : Check to enforce strict SSL certificate verification.
     * **Max connections per node** : This setting can be left at the default value initially. See the [Connecting Looker to your database](/looker/docs/connecting-to-your-db#max_connections) documentation page for more information.
     * **Connection Pool Timeout** : Can be left at the default value initially. Read more about this setting on the [Connecting Looker to your database](/looker/docs/connecting-to-your-db#connection-pool-timeout) documentation page.
     * **SQL Runner Precache** : To cause SQL Runner not to preload table information and to load table information only when a table is selected, clear this option. Read more about this setting on the [Connecting Looker to your database](/looker/docs/connecting-to-your-db#sql_runner_precache) documentation page.
     * **Database Time Zone** : Specify the time zone used in the database. Leave this field blank if you do not want time zone conversion. See the [Using time zone settings](/looker/docs/using-time-zone-settings) documentation page for more information.
  3. To verify that the connection is successful, click **Test**. See the [Testing database connectivity](/looker/docs/testing-db-connectivity) documentation page for troubleshooting information.

  4. To save these settings, click **Connect**.

## Feature support

For Looker to support some features, your database dialect must also support them.

Firebolt supports the following features as of Looker 25.2:

Feature | Supported?  
---|---  
Support Level | Supported  
Looker (Google Cloud core) | No  
Symmetric Aggregates | Yes  
Derived Tables | Yes  
Persistent SQL Derived Tables | No  
Persistent Native Derived Tables | No  
Stable Views | No  
Query Killing | Yes  
SQL-based Pivots | Yes  
Timezones | No  
SSL | Yes  
Subtotals | No  
JDBC Additional Params | Yes  
Case Sensitive | Yes  
Location Type | Yes  
List Type | Yes  
Percentile | No  
Distinct Percentile | No  
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
Aggregate Awareness | No  
Incremental PDTs | No  
Milliseconds | No  
Microseconds | No  
Materialized Views | No  
Approximate Count Distinct | No