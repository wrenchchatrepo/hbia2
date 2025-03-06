# https://cloud.google.com/looker/docs/db-config-vertica

Depth: 3

## Encrypting network traffic  
  
It is a best practice to encrypt network traffic between the Looker application and your database. Consider one of the options described on the [Enabling secure database access](/looker/docs/enabling-secure-db-access) documentation page.

## Database configuration

Before you create a connection to Vertica, create a new database user and schema that is exclusive for your Looker applications. The Looker user needs read and write permissions into a separate schema to store PDTs and read-only privileges to other schemas in the Vertica database. This is optional but recommended.

The following is an example of creating a user and schema for Looker:
    
    
    CREATE USER looker Identified BY 'mypassword';
    CREATE SCHEMA looker_scratch;
    GRANT CREATE ON SCHEMA looker_scratch to looker;
    

## Creating the Looker connection to your database

In the **Admin** section of Looker, select **Connections** , and then click **Add Connection**.

Fill out the connection details. The majority of the settings are common to most database dialects. See the [Connecting Looker to your database](/looker/docs/connecting-to-your-db) documentation page for information. Some of the settings are described next:

  * **Name** : Give a name to the connection. This is how the LookML model will reference the connection.
  * **Dialect** : Select **Vertica** from the drop-down of dialects.
  * **Host** : Enter the Vertica server name or IP.
  * **Port** : The default is 5433.
  * **Database** : Enter Vertica's database name.
  * **Username and Password** : Enter the username and password of the user that will connect to Looker.
  * **Schema** : Enter the schema that contains the tables that you want to explore in Looker.
  * **Temp Database** : This is the scratch schema where you want Looker to create any temporal derived tables to improve performance. It is optional but recommended, and should be created beforehand.
  * **Max connections per node** : This setting can be left at the default value initially. See the [Connecting Looker to your database](/looker/docs/connecting-to-your-db#max_connections) documentation page for more information.
  * **Connection Pool Timeout** : This is optional. Use the default value.
  * **Database Time Zone** : The time zone your Vertica database uses to store dates and times. For example, UTC. This is optional.
  * **Query Time Zone** : The time zone you want your queries to display. For example, US Eastern (America – New York). This is optional.
  * **Additional JDBC parameters** : This is optional. Use this field to enable additional database settings. For example, to enable Vertica's native load balancing, use the JDBC connection parameter `ConnectionLoadBalance=1`. To assign a label to identify Looker's sessions, use the JDBC connection parameter `Label=<mylabel>`. You can pass several parameters one after the other using `&`, as shown on this page. For a complete list of available JDBC connection parameters, see [Vertica's documentation](https://www.vertica.com/docs/9.1.x/HTML/index.htm#Authoring/ConnectingToVertica/ClientJDBC/JDBCConnectionProperties.htm).

To verify that the connection is successful, click **Test**. See the [Testing database connectivity](/looker/docs/testing-db-connectivity) documentation page for troubleshooting information.

To save these settings, click **Connect**.

## Feature support

For Looker to support some features, your database dialect must also support them.

Vertica supports the following features as of Looker 25.2:

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
Case Sensitive | Yes  
Location Type | Yes  
List Type | No  
Percentile | Yes  
Distinct Percentile | No  
SQL Runner Show Processes | Yes  
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
Incremental PDTs | Yes  
Milliseconds | Yes  
Microseconds | Yes  
Materialized Views | No  
Approximate Count Distinct | No  
  
## Next steps

After you have completed the database connection, [configure authentication options](/looker/docs/getting-started-with-users).