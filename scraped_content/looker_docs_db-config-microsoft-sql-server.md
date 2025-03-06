# https://cloud.google.com/looker/docs/db-config-microsoft-sql-server

Depth: 3

## Encrypting network traffic  
  
It is a best practice to encrypt network traffic between the Looker application and your database. Consider one of the options described on the [Enabling secure database access](/looker/docs/enabling-secure-db-access) documentation page.

If you're interested in using SSL encryption, see the [Microsoft documentation](http://msdn.microsoft.com/en-us/library/ms189067%28v=sql.105%29.aspx).

## Configuring server authentication

Looker requires "SQL Server Authentication" on your MSSQL server. If your MSSQL server is configured as "Windows Integrated Authentication" only, change the server configuration to "Windows Integrated Authentication and SQL Server Authentication."

If the server configuration is not set properly, Looker will be unable to connect. This will appear in your SQL Server log messages like: "An attempt to log in using SQL authentication failed. Server is configured for windows authentication only."

If this change is required, you can complete the following steps:

  1. In **SQL Server Management Studio Object Explorer** , right-click the server, and then click **Properties**.
  2. On the **Security** page, under **Server authentication** , select the new server authentication mode, and then click **OK**.
  3. In the **SQL Server Management Studio** dialog, click **OK** to acknowledge the requirement to restart SQL Server.
  4. In **Object Explorer** , right-click your server, and then click **Restart**. If SQL Server Agent is running, it must also be restarted.

You can read about this more in [Microsoft's documentation](https://docs.microsoft.com/en-us/sql/database-engine/configure-windows/change-server-authentication-mode#to-change-security-authentication-mode).

## Creating a Looker user

Looker authenticates to your database using SQL Server Authentication. Using a domain account is not supported.

To create an account, run the following commands. Change `some_password_here` to a unique, secure password:
    
    
    CREATE LOGIN looker
      WITH PASSWORD = 'some_password_here';
    USE MyDatabase;
    CREATE USER looker FOR LOGIN looker;
    GO
    

## Granting the Looker user permission to SELECT from tables

Looker requires the `SELECT` permission for each table or schema that you will want to query. There are multiple ways to assign `SELECT` permission:

  * To grant `SELECT` permission to individual schemas, run the following command for each schema:
    
        GRANT SELECT on SCHEMA :: 'schema_name' to looker;
    

  * To grant `SELECT` permission to individual tables, run the following command for each table:
    
        GRANT SELECT on OBJECT :: 'schema_name'.'table_name' to looker;
    

  * For MSSQL version 2012 or later, you can alternatively assign the Looker user the `db_datareader` role using these commands:
    
        USE MyDatabase;
    ALTER ROLE db_datareader ADD MEMBER looker;
    GO
    

## Granting the Looker user permission to view and stop running queries

Looker must be authorized to detect and stop running queries, which requires the following permissions:

  * `ALTER ANY CONNECTION`
  * `VIEW SERVER STATE`

To grant these permissions, run the following commands:
    
    
    USE Master;
    GRANT ALTER ANY CONNECTION TO looker;
    GRANT VIEW SERVER STATE to looker;
    GO
    

## Granting the Looker user permission to create tables

To give the Looker user the permission to create [PDTs](/looker/docs/derived-tables#persistent_derived_table), run the following commands:
    
    
    USE MyDatabase;
    GRANT CREATE TABLE to looker;
    GO
    

## Temp schema setup

To create a schema that is owned by the Looker user and grant the necessary rights to the Looker user, run this command:
    
    
    CREATE SCHEMA looker_scratch AUTHORIZATION looker;
    

## Configuring Kerberos authentication

**Warning:** Kerberos authentication with an MSSQL database is supported only for customer-hosted instances. Looker-hosted instances cannot support Kerberos authentication with an MSSQL database.

If you use Kerberos authentication with your MSSQL database, follow the steps to configure Looker to connect by using Kerberos, as described in the following section.

### Setting up the Kerberos client configuration

First, you need to ensure the installation of several pieces of software and the presence of several files on the Looker machine.

#### Kerberos client

Verify that the Kerberos client is installed on the Looker machine by running `kinit`. If the Kerberos client is not installed, install the Kerberos client's binaries.

For example, on Redhat or CentOS, this would be the following:
    
    
    sudo yum install krb5-workstation krb5-libs krb5-auth-dialog
    

#### Java 8

Java 8 must be installed on the Looker machine and in the `PATH` and `JAVA_HOME` of the Looker user. If necessary, install it locally in the `looker` directory.

#### Java Cryptography Extension

  1. Download and install the Java Cryptography Extension (JCE) for Java 8 from this [Oracle download page](http://www.oracle.com/technetwork/java/javase/downloads/jce8-download-2133166.html).

     * Locate the `jre/lib/security` directory for the Java installation.
     * Remove the following JAR files from this directory: `local_policy.jar` and `US_export_policy.jar`.
     * Replace these two files with the JAR files included in the JCE Unlimited Strength Jurisdiction Policy Files download.

It may be possible to use versions of Java prior to Java 8 with the JCE installed, but this is not recommended.

  2. Update `JAVA_HOME` and `PATH` in `~looker/.bash_profile` to point to the correct installation of Java and `source ~/.bash_profile` or log out and in again.

  3. Verify the Java version with `java -version`.

  4. Verify the `JAVA_HOME` environment variable with `echo $JAVA_HOME`.

#### `gss-jaas.conf`

Create a `gss-jaas.conf` file in the `looker` directory with these contents:
    
    
    com.sun.security.jgss.initiate {
        com.sun.security.auth.module.Krb5LoginModule required
        useTicketCache=true
        doNotPrompt=true;
    };
    

If necessary for testing, `debug=true` can be added to this file like this:
    
    
    com.sun.security.jgss.initiate {
        com.sun.security.auth.module.Krb5LoginModule required
        useTicketCache=true
        doNotPrompt=true
        debug=true;
    };
    

#### `krb5.conf`

The server that is running Looker should also have a valid `krb5.conf` file. By default, this file is in `/etc/krb5.conf`. If it is in another location, that must be indicated in the environment (`KRB5_CONFIG` in the shell environment).

You may need to copy this from another Kerberos client machine.

#### `lookerstart.cfg`

Point to the `gss-jaas.conf` and `krb5.conf` files by making a file in the `looker` directory (the same directory that contains the `looker` startup script) called `lookerstart.cfg` that contains the following lines:
    
    
      JAVAARGS="-Djava.security.auth.login.config=/path/to/gss-jaas.conf -Djavax.security.auth.useSubjectCredsOnly=false -Djava.security.krb5.conf=/etc/krb5.conf"
      LOOKERARGS=""
    

If the `krb5.conf` file is not at `/etc/krb5.conf` then it will also be necessary to add this variable:
    
    
      -Djava.security.krb5.conf=/path/to/krb5.conf
    

For debugging, add these variables:
    
    
      -Dsun.security.jgss.debug=true -Dsun.security.krb5.debug=true
    

Then restart Looker with `./looker restart`.

### Authenticating with Kerberos

#### User authentication

  1. If `krb5.conf` is not in `/etc/`, then use the environment variable `KRB5_CONFIG` to indicate its location.

  2. Run the command `klist` to make sure there is a valid ticket in the Kerberos ticket cache.

  3. If there is no ticket, run `kinit username@REALM` or `kinit username` to create the ticket.

  4. The account that is used with Looker will likely be headless, so you can get a keytab file from Kerberos to store the credential for long-term use. Use a command like `kinit -k -t looker_user.keytab username@REALM` to get the Kerberos ticket.

#### Automatically renewing the ticket

Set up a cron job that runs every so often to keep an active ticket in the Kerberos ticket cache. How often this should run depends on the configuration of the cluster. `klist` should give an indication of how soon tickets expire.

## Creating the Looker connection to your database

Follow these steps to create the connection from Looker to your database:

  1. In the **Admin** section of Looker, select **Connections** , and then click **Add Connection**.
  2. From the **Dialect** drop-down menu, select your version of Microsoft SQL Server.

**Note:** If you are on a [Looker (Google Cloud core)](/looker/docs/looker-core-overview) instance and you don't see your dialect listed in the **Dialect** drop-down menu, see the [Looker (Google Cloud core) documentation](/looker/docs/looker-core-dialects#supported_dialects_for) to verify that the dialect is supported for Looker (Google Cloud core) instances.
  3. For **Remote Host** and **Port** , enter the hostname and port (the default port is 1433).

If you need to specify a non-default port other than 1433 and your database requires the use of a comma instead of a colon, you can add `useCommaHostPortSeparator=true` in the **Additional JDBC parameters** field further down in the connection settings, which will allow you to use a comma for **Remote Host:Port**. For example:

`jdbc:sqlserver://hostname,1434`

  4. Fill out the rest of the connection details. The majority of the settings are common to most database dialects. See the [Connecting Looker to your database](/looker/docs/connecting-to-your-db) documentation page for information.

  5. To verify that the connection is successful, click **Test**. See the [Testing database connectivity](/looker/docs/testing-db-connectivity) documentation page for troubleshooting information.

  6. To save these settings, click **Connect**.

### Configuring the Looker connection

Follow the instructions on the [Connecting Looker to your database](/looker/docs/connecting-to-your-db) documentation page to create a connection to your MSSQL database. In the **Additional JDBC parameters** section of the **Connection Settings** page, add the following:
    
    
    ;integratedSecurity=true;authenticationScheme=JavaKerberos
    

Some networks are configured for two Kerberos realms, one for Windows Active Directory and the other for Linux and other non-Windows systems. In that case, when the Linux-focused Realm and the Active Directory Realm are configured to trust each other, it is called "cross-realm authentication".

If your network uses cross-realm authentication, you must explicitly specify the Kerberos principal for MSSQL Server. In the **Additional JDBC parameters** field, add the following:
    
    
    ;serverSpn=service_name/FQDN\:PORT@REALM
    

Replacing `FQDN` and `PORT@REALM` with your network information. For example:
    
    
    ;serverSpn=MSSQLSvc/dbserver.internal.example.com:1433@AD.EXAMPLE.COM
    

In addition, the **Connection Settings** page in Looker requires entries in the **Username** and **Password** fields, but these are not required for Kerberos. Enter dummy values in these fields.

Test the connection to make sure that it is configured correctly.

## Feature support

For Looker to support some features, your database dialect must also support them.

Microsoft SQL Server 2008+ supports the following features as of Looker 25.2:

Feature | Supported?  
---|---  
Support Level | Integration  
Looker (Google Cloud core) | No  
Symmetric Aggregates | Yes  
Derived Tables | Yes  
Persistent SQL Derived Tables | Yes  
Persistent Native Derived Tables | Yes  
Stable Views | Yes  
Query Killing | Yes  
SQL-based Pivots | Yes  
Timezones | No  
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
  
Microsoft SQL Server 2016 supports the following features as of Looker 25.2:

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
  
Microsoft SQL Server 2017+ supports the following features as of Looker 25.2:

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