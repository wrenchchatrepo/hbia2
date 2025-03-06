# https://cloud.google.com/looker/docs/db-config-clickhouse

Depth: 3

**Note:** Looker supports ClickHouse version 0.2 and higher.

## Encrypting network traffic

It is a best practice to encrypt network traffic between the Looker application and your database. Consider one of the options described on the [Enabling secure database access](/looker/docs/enabling-secure-db-access) documentation page.

To enable SSL encryption on the server side, see the [ClickHouse Global Server Settings documentation](https://ClickHouse.yandex/docs/en/operations/server_settings/settings/#server_settings-openssl).

## Users and security

First, configure your Looker user on the ClickHouse server. ClickHouse database users are not created with the `CREATE USER` command. Follow the [ClickHouse access rights documentation](https://clickhouse.yandex/docs/en/operations/access_rights/) to configure the `users` section in the `users.xml` file. Here is a basic example:
    
    
    <!-- Users and ACL. -->
    <users>
        <looker>
            <password>CHANGEIT</password>
            <networks incl="networks" />
            <profile>default</profile>
            <quota>default</quota>
        </looker>
    
        <web>
            <password></password>
            <networks incl="networks" />
            <profile>web</profile>
            <quota>default</quota>
            <allow_databases>
               <database>test</database>
            </allow_databases>
            <allow_dictionaries>
               <dictionary>test</dictionary>
            </allow_dictionaries>
        </web>
    </users>
    

Also within this file, configure the appropriate database access.
    
    
    <allow_databases>
        <database>database_1</database>
        <database>database_2</database>
        <database>database_3</database>
    </allow_databases>
    

## Creating the Looker connection to your database

In the **Admin** section of Looker, select **Connections** , and then click **Add Connection**.

Fill out the connection details. The majority of the settings are common to most database dialects. See the [Connecting Looker to your database](/looker/docs/connecting-to-your-db) documentation page for information. Some of the settings are described next:

  * **Dialect** : ClickHouse.
  * **Host** : Reachable hostname.
  * **Port** : Port on which the ClickHouse service is reachable over HTTP(S). 
    * By default, HTTP connections will use 8123, and HTTPS will use 8443.
    * Port 9000 and 9440 are by default used by the ClickHouse command line client, but these ports cannot be used by Looker to connect to ClickHouse.
    * Your ClickHouse administrator may have chosen alternate ports with the [`http_port/https_port`](https://ClickHouse.yandex/docs/en/operations/server_settings/settings/#http-port-https-port) settings in the ClickHouse configuration. Ask your ClickHouse admin for the settings appropriate to your local configuration.
  * **Database** : Database name (must be one of the databases allowed in the `users.xml` file).
  * **Username** : Database username.
  * **Password** : Database password.
  * **Additional JDBC parameters** : (Optional) Additional JDBC string parameters.
  * **Datagroup and PDT Maintenance Schedule** : ClickHouse does not support PDTs, so this can be ignored.
  * **SSL** : Check to connect to ClickHouse over SSL.
  * **Verify SSL** : (Optional) Check to enforce strict hostname verification on the ClickHouse server. Check this only if you are using an SSL certificate that is signed by a generally trusted Certificate Authority. If you are using a self-signed SSL certificate, leave it unchecked.

To verify that the connection is successful, click **Test**. See the [Testing database connectivity](/looker/docs/testing-db-connectivity) documentation page for troubleshooting information.

To save these settings, click **Connect**.

## Feature support

For Looker to support some features, your database dialect must also support them.

ClickHouse supports the following features as of Looker 25.2:

Feature | Supported?  
---|---  
Support Level | Supported  
Looker (Google Cloud core) | Yes  
Symmetric Aggregates | No  
Derived Tables | Yes  
Persistent SQL Derived Tables | No  
Persistent Native Derived Tables | No  
Stable Views | No  
Query Killing | Yes  
SQL-based Pivots | No  
Timezones | No  
SSL | Yes  
Subtotals | No  
JDBC Additional Params | Yes  
Case Sensitive | Yes  
Location Type | Yes  
List Type | Yes  
Percentile | Yes  
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
Aggregate Awareness | No  
Incremental PDTs | No  
Milliseconds | No  
Microseconds | No  
Materialized Views | No  
Approximate Count Distinct | No