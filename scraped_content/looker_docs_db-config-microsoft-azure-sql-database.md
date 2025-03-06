# https://cloud.google.com/looker/docs/db-config-microsoft-azure-sql-database

Depth: 3

## Encrypting network traffic  
  
It is a best practice to encrypt network traffic between the Looker application and your database. Consider one of the options described on the [Enabling secure database access](/looker/docs/enabling-secure-db-access) documentation page.

To learn more about using SSL encryption, see the [Microsoft documentation](https://azure.microsoft.com/en-us/documentation/articles/cloud-services-configure-ssl-certificate/).

## Users and security

Looker authenticates to your database using SQL Database Authentication. Using a domain account is not supported.

To create an account, run the following commands, changing `some_password_here` to a unique, secure password:
    
    
    CREATE LOGIN looker
      WITH PASSWORD = 'some_password_here';
    USE MyDatabase;
    CREATE USER looker FOR LOGIN looker;
    GO
    

Looker must be authorized to detect and stop currently running queries, which requires the following permissions:
    
    
    KILL DATABASE CONNECTION
    VIEW DATABASE STATE
    

To grant these permissions, run the following command:
    
    
    GRANT KILL DATABASE CONNECTION TO looker;
    GRANT VIEW DATABASE STATE to looker;
    

## Temp schema setup

Create a schema owned by the Looker user:
    
    
    CREATE SCHEMA looker_scratch AUTHORIZATION looker;
    

## Creating the Looker connection to your database

In the **Admin** section of Looker, select **Connections** , and then click **Add Connection**.

Fill out the connection details. The majority of the settings are common to most database dialects. See the [Connecting Looker to your database](/looker/docs/connecting-to-your-db) documentation page for information. The following fields have additional information that applies to Microsoft Azure SQL Database:

  * **Dialect** : Select **Microsoft Azure SQL Database**.
  * **Remote Host** and **Port** : Enter the hostname and port (the default port is 1433).

If you need to specify a non-default port other than 1433 and your database requires the use of a comma instead of a colon, you can add `useCommaHostPortSeparator=true` in the **Additional JDBC parameters** field further down in the connection settings, which will allow you to use a comma in the **Remote Host:Port** field. For example:

`jdbc:sqlserver://hostname,1434`

To verify that the connection is successful, click **Test**. See the [Testing database connectivity](/looker/docs/testing-db-connectivity) documentation page for troubleshooting information.

To save these settings, click **Connect**.

## Feature support

For Looker to support some features, your database dialect must also support them.

Microsoft Azure SQL Database supports the following features as of Looker 25.2:

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
List Type | No  
Percentile | No  
Distinct Percentile | No  
SQL Runner Show Processes | Yes  
SQL Runner Describe Table | Yes  
SQL Runner Show Indexes | Yes  
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