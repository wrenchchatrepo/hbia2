# https://cloud.google.com/looker/docs/db-config-teradata

Depth: 3

**Note:** See the [Teradata end-user license agreement](/looker/docs/db-teradata-eula).

The procedures that are required to connect Looker to a Teradata database depend on your Looker deployment:

  * For Looker (original) instances, perform the following procedures:

    1. Install the `hash_md5` user-defined function (UDF) on your Teradata server.
    2. Install the Teradata JDBC driver.
    3. Create the Looker connection to your database.
  * For [Looker (Google Cloud core)](/looker/docs/looker-core-overview) instances, perform the following procedures:

    1. Install the `hash_md5` user-defined function (UDF) on your Teradata server.
    2. Create the Looker connection to your database.

## Encrypting network traffic

It is a best practice to encrypt network traffic between the Looker application and your database. Consider one of the options described on the [Enabling secure database access](/looker/docs/enabling-secure-db-access) documentation page.

## Installing the `hash_md5` user-defined function (UDF)

Before configuring Looker to work with Teradata, you must install the `hash_md5` user-defined function (UDF) on your Teradata server. You can find instructions for installing the UDF on this [Teradata downloads](https://downloads.teradata.com/download/extensibility/md5-message-digest-udf) page.

## Installing the Teradata JDBC driver

If you have a Looker (original) instance, you will need to configure a Teradata driver before creating the Looker connection. These instructions describe that process, assuming use of a startup script that is similar to the examples that are provided on the [looker-open-source GitHub page](https://github.com/looker-open-source/customer-scripts/tree/master/startup_scripts).

**Note:** If you have a [Looker (Google Cloud core)](/looker/docs/looker-core-overview) instance, you can create a connection to a Teradata database without configuring a Teradata driver. After you install the `hash_md5` user-defined function (UDF) on your Teradata server, you can go right to the Creating the Looker connection to your database procedure on this page.

To install the driver, you will need to acquire two Teradata files, include them as part of the startup process, and add an option to tell Looker to access the driver.

Follow the steps on the [Unpackaged JDBC drivers](/looker/docs/unpackaged-jdbc-drivers) documentation page using the following values:

**driver symbol** : `teradata`

**driver entry** :
    
    
    - name: teradata
      dir_name: teradata
      module_path: com.teradata.jdbc.TeraDriver
    

For the [step to put the driver in your dialect's directory](/looker/docs/unpackaged-jdbc-drivers#driver_directory), the paths to these files will look like this:

  * `looker/custom_jdbc_drivers/teradata/tdgssconfig.jar`
  * `looker/custom_jdbc_drivers/teradata/terajdbc4.jar`

## Creating the Looker connection to your database

To create the connection from Looker to your database, follow these steps:

  1. In the **Admin** section of Looker, select **Connections** , and then click **Add Connection**.
  2. Select **Teradata** from the **Dialect** drop-down menu.
  3. Fill out the connection details. The majority of the settings are common to most database dialects. See the [Connecting Looker to your database](/looker/docs/connecting-to-your-db) documentation page for information.
  4. To verify that the connection is successful, click **Test**. See the [Testing database connectivity](/looker/docs/testing-db-connectivity) documentation page for troubleshooting information.
  5. To save these settings, click **Connect**.

## Feature support

For Looker to support some features, your database dialect must also support them.

Teradata supports the following features as of Looker 25.2:

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
Timezones | No  
SSL | No  
Subtotals | No  
JDBC Additional Params | Yes  
Case Sensitive | Yes  
Location Type | Yes  
List Type | No  
Percentile | No  
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