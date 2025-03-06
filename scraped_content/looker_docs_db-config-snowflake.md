# https://cloud.google.com/looker/docs/db-config-snowflake

Depth: 3

To connect Looker to Snowflake, follow these steps:

  1. Create a Looker user on Snowflake and provision access.
  2. Set up a database connection in Looker.

## Encrypting network traffic

It is a best practice to encrypt network traffic between the Looker application and your database. Consider one of the options described on the [Enabling secure database access](/looker/docs/enabling-secure-db-access) documentation page.

## Creating a Looker user on Snowflake

We recommend the following commands for creating the Looker user. Make sure to run each line individually.

> Optionally, add in the [`ON FUTURE`](https://docs.snowflake.net/manuals/sql-reference/sql/grant-privilege.html#future-grants-on-schema-objects) keyword to persist `GRANT` statements on newly created objects. We recommend running this for tables in all schemas that Looker will use so that you are not required to re-run `GRANT` statements as new tables are created.
    
    
    -- change role to ACCOUNTADMIN
    use role ACCOUNTADMIN;
    
    -- create role for looker
    create role if not exists looker_role;
    grant role looker_role to role SYSADMIN;
        -- Note that we are not making the looker_role a SYSADMIN,
        -- but rather granting users with the SYSADMIN role to modify the looker_role
    
    -- create a user for looker
    create user if not exists looker_user
    password = <enter password here>;
    grant role looker_role to user looker_user;
    alter user looker_user
    set default_role = looker_role
    default_warehouse = looker_wh;
    
    -- change role
    use role SYSADMIN;
    
    -- create a warehouse for looker (optional)
    create warehouse if not exists looker_wh
    
    -- set the size based on your dataset
    warehouse_size = medium
    warehouse_type = standard
    auto_suspend = 1800
    auto_resume = true
    initially_suspended = true;
    grant all privileges
    on warehouse looker_wh
    to role looker_role;
    
    -- grant read only database access (repeat for all database/schemas)
    grant usage on database <database> to role looker_role;
    grant usage on schema <database>.<schema> to role looker_role;
    
    -- rerun the following any time a table is added to the schema
    grant select on all tables in schema <database>.<schema> to role looker_role;
    -- or
    grant select on future tables in schema <database>.<schema> to role looker_role;
    
    -- create schema for looker to write back to
    use database <database>;
    create schema if not exists looker_scratch;
    use role ACCOUNTADMIN;
    grant ownership on schema looker_scratch to role SYSADMIN revoke current grants;
    grant all on schema looker_scratch to role looker_role;
    

If you paste the previous commands as a batch into the Snowflake connection panel, select the **All Queries** checkbox to ensure that all lines are run. By default, Snowflake runs only the lines that are selected.

![The Snowflake console with the All Queries checkbox selected.](/static/looker/docs/images/setup-snowflake-console-524.png)

## Creating the Looker connection to your database

In the **Admin** section of Looker, select **Connections** , and then click **Add Connection**.

Fill out the connection details. The majority of the settings are common to most database dialects. See the [Connecting Looker to your database](/looker/docs/connecting-to-your-db) documentation page for information. Some of the settings are described next:

  * **Name** : Give the connection a name. This is how the LookML model will reference the connection.
  * **Dialect** : Select **Snowflake**.
  * **Host** : Enter the Snowflake hostname. It will look like `<account_name>.snowflakecomputing.com`. Check [Snowflake account name examples by region](https://docs.snowflake.com/en/user-guide/jdbc-configure.html#connection-parameters) to make sure you use the right value for your deployment.
  * **Port** : The default is 443.
  * **Database** : Enter the default database to use. This field is case-sensitive.
  * **Schema** : Enter the default schema.
  * **Authentication** : Select **Database Account** or **OAuth** : 
    * Use **Database Account** to specify the **Username** and **Password** of the Snowflake user account that will be used to connect to Looker.
    * Use **OAuth** if you want to configure OAuth for the connection.
  * **Enable PDTs** : Use this toggle to enable [persistent derived tables (PDTs)](/looker/docs/derived-tables#persistent-derived-tables). Enabling PDTs reveals additional PDT fields and the [**PDT Overrides**](/looker/docs/connecting-to-your-db#pdt-overrides) section for the connection.

**Note:** PDTs are not supported for Snowflake connections that use OAuth.
  * **Temp Database** : If PDTs are enabled, set this field to a schema where the user has full privileges to create, drop, rename, and alter tables.

  * **Max connections per node** : This setting can be left at the default value initially. Read more about this setting in the [Max connections per node](/looker/docs/connecting-to-your-db#max_connections) section of the **Connecting Looker to your database** documentation page.

  * **Cost Estimate** : Enables [cost estimates for Explore queries](/looker/docs/creating-and-editing-explores#cost_estimates_for_explore_queries), [cost estimates for SQL Runner queries](/looker/docs/sql-runner-create-queries-and-explores#cost_estimates_for_sql_runner_queries), and [computation savings estimates for aggregate awareness queries](/looker/docs/aggregate_awareness#computation_savings_estimates_for_aggregate_awareness) on the connection.

  * **Database Time Zone** : The time zone your Snowflake database uses to store dates and times. The default is UTC. This is optional.

  * **Query Time Zone** : The time zone you want your queries to display. For example, US Eastern (America – New York). This is optional.

  * **Additional JDBC parameters** : Add additional JDBC parameters from the [Snowflake JDBC driver](https://docs.snowflake.com/en/user-guide/jdbc-configure.html).

    * Add `warehouse=<YOUR WAREHOUSE NAME>`.
    * Additionally, by default, Looker will set the following [Snowflake parameters](https://docs.snowflake.com/en/sql-reference/parameters.html) on each session:

      * `TIMESTAMP_TYPE_MAPPING=TIMESTAMP_LTZ`
      * `JDBC_TREAT_DECIMAL_AS_INT=FALSE`
      * `TIMESTAMP_INPUT_FORMAT=AUTO`
      * `AUTOCOMMIT=TRUE`

You can override each of these parameters by setting an alternative value in the **Additional JDBC parameters** field, for example: `&AUTOCOMMIT=FALSE`

To verify that the connection is successful, click **Test**. See the [Testing database connectivity](/looker/docs/testing-db-connectivity) documentation page for troubleshooting information.

To save these settings, click **Connect**.

## Designating Snowflake warehouses on a per-group or per-user basis

You can use Looker [user attributes](/looker/docs/admin-panel-users-user-attributes) to assign separate Snowflake [warehouses](https://docs.snowflake.net/manuals/user-guide/warehouses.html) to individual Looker users or groups. This is useful, for example, if you have users who require different levels of computing power. You can assign a warehouse with greater computing resources to just those users who need it, while assigning a warehouse with lesser resources to users with lesser needs.

To designate warehouses on a per-group or per-user basis, follow these steps:

  1. Add the [groups](/looker/docs/admin-panel-users-groups) or [users](/looker/docs/admin-panel-users-users) in Looker.
  2. Define a [user attribute](/looker/docs/admin-panel-users-user-attributes) in Looker where the Snowflake warehouse names will be stored. You can give this attribute any name, such as `snowflake_wh`.

![The User Attributes page in Looker, showing the Snowflake warehouse user attribute.](/static/looker/docs/images/setup-snowflake-user-attribute-64.png)

  3. In the user attribute you just defined, assign the warehouse name values to the [groups](/looker/docs/admin-panel-users-user-attributes#assigning_values_to_user_groups) or [users](/looker/docs/admin-panel-users-user-attributes#assigning_values_to_individual_users).

![The User Attributes page in Looker, showing the Snowflake warehouse user attribute with values assigned to a group.](/static/looker/docs/images/setup-snowflake-group-values-64.png)

  4. In the **Additional JDBC parameters** field on the **Connection Settings** page, add the following, replacing `snowflake_warehouse` with the name of the user attribute that you defined:
    
          warehouse={{ _user_attributes['snowflake_warehouse'] }}
    

For example:

![The Connection Settings page in Looker, showing the Additional JDBC parameters field with the warehouse user attribute parameter.](/static/looker/docs/images/setup-snowflake-add-params-2304.png)

  5. To test the individual connection settings, you can [sudo](/looker/docs/admin-panel-users-users#impersonating_\(sudoing\)_users) as a user to whom you assigned a warehouse name value.

You can see more detailed instructions for this procedure on the [Red Pill Analytics blog](https://blog.redpillanalytics.com/managing-snowflake-data-warehouse-compute-in-looker-e445543987b2).

## Snowflake's autosuspend feature

Snowflake warehouses have an autosuspend feature that is enabled by default. After a specified period, the warehouse will autosuspend. If the warehouse is suspended, all queries produce an error. This error is not visible on dashboards (no data is normally shown), but it is visible when querying with the Explore page.

Snowflake also has an auto-resume feature that will resume the warehouse when it is queried. However, resuming the warehouse can take up to five minutes, causing queries to stop responding for five minutes before returning. These features cannot be configured in Looker. Enable these features on the **Warehouses** tab in the Snowflake UI.

![The Warehouses tab in the Snowflake UI, showing the Autosuspend and Autoresume checkboxes](/static/looker/docs/images/setup-snowflake-warehouses-tab-524.png)

## PDT support

For [persistent derived table](/looker/docs/derived-tables#persistent-derived-tables) support, create a Snowflake user account for PDTs that has write access to your database and the temp schema that Looker will use to create PDTs. On the Looker **Connections Settings** page, in the **Persistent Derived Tables (PDTs)** section, turn on the **Enable PDTs** toggle. Then, in the **Temp database** field, enter the name of the temp schema that Looker will use to create PDTs. Next, in the **PDT Overrides** section, enter the username and password of the PDT user. See the [Connecting Looker to your database](/looker/docs/connecting-to-your-db#configuring_separate_login_credentials_for_pdt_processes) documentation page for more information.

> PDTs are not supported for Snowflake connections that use OAuth.

For Snowflake connections, Looker sets the value for the [`AUTOCOMMIT`](https://docs.snowflake.com/en/sql-reference/parameters.html#autocommit) parameter to `TRUE` (which is Snowflake's default value). AUTOCOMMIT is required for SQL commands that Looker runs to maintain its PDT registration system.

## Configuring OAuth for Snowflake connections

Looker supports OAuth for Snowflake connections, meaning that each Looker user authenticates in to the database and authorizes Looker to run queries on the database with the user's own OAuth user account.

OAuth lets database administrators perform the following tasks:

  * Audit which Looker users are running queries against the database
  * Enforce role-based access controls using database-level permissions
  * Use OAuth tokens for all processes and actions that access the database, instead of embedding database IDs and passwords in multiple places
  * Revoke authorization for a given user through the database directly

With Snowflake connections that use OAuth, users must sign in again periodically when their OAuth tokens expire. The duration of validity for Snowflake OAuth tokens is set through Snowflake itself.

Note the following for database-level OAuth connections:

  * If a user lets their OAuth token expire, any Looker schedules or alerts that they own will be affected. To guard against this, Looker will send a notification email to the owner of each schedule and each alert before the current active OAuth token expires. Looker will send these notifications emails 14 days, 7 days, and 1 day before the token expires. The user can go to their Looker user page to reauthorize Looker to the database and avoid any interruption to their schedules and alerts. See the [Personalizing user account settings](/looker/docs/user-account#configuring_oauth_connection_credentials) documentation page for details.
  * Because database connections that use OAuth are "per user," caching policies are also per user and not just per query. This means that, instead of using cached results whenever the same query is run within the caching period, Looker will use cached results only if the _same user has run the same query_ within the caching period. For further information on caching, see the [Caching queries](/looker/docs/caching-and-datagroups) documentation page.

  * When using OAuth, you cannot switch to different roles in the Snowflake user account. As described in the [Snowflake documentation](https://docs.snowflake.com/en/user-guide/oauth-custom.html#scope), Snowflake uses the default role of the Snowflake user's account, unless the default role is ACCOUNTADMIN or SECURITYADMIN. Because these roles are blocked for OAuth, Snowflake will instead use the PUBLIC role. See the [Snowflake documentation](https://docs.snowflake.com/en/user-guide/oauth-partner.html#blocking-specific-roles-from-using-the-integration) for information.

  * [Persistent derived tables (PDTs)](/looker/docs/derived-tables#persistent_derived_table) are not supported for Snowflake connections with OAuth.

  * When a Looker admin sudos as another user, the admin will use that user's OAuth access token. If the user's access token is expired, the admin cannot create a new token on behalf of the sudoed user. See the [Users](/looker/docs/admin-panel-users-users#impersonating-users) documentation page for information on using the `sudo` command.

### Configuring a Snowflake database for OAuth with Looker

To create a Snowflake connection to Looker using OAuth, you must set up the OAuth integration in Snowflake. This requires a Snowflake user account with ACCOUNTADMIN permission.

  1. Run the following command in Snowflake, where `<looker_hostname>` is the hostname of your Looker instance:
    
          CREATE SECURITY INTEGRATION LOOKER
        TYPE = OAUTH
        ENABLED = TRUE
        OAUTH_CLIENT = LOOKER
        OAUTH_REDIRECT_URI = 'https://<looker_hostname>/external_oauth/redirect';
    

  2. Get the OAuth client ID and secret by running the following command:
    
          SELECT SYSTEM$SHOW_OAUTH_CLIENT_SECRETS('LOOKER');
    

The response will have an `OAUTH_CLIENT_ID` and `OAUTH_CLIENT_SECRET` that you will need later in this procedure.

  3. In Looker, create a new connection to your Snowflake warehouse, as described in the Creating the Looker connection to your database section of this page. When you create the new connection, select the [**OAuth**](/looker/docs/connecting-to-your-db#use_oauth) option in the **Authentication** field. When you select the **OAuth** option, Looker displays the **OAuth Client ID** and **OAuth Client Secret** fields.

  4. Paste in the `OAUTH_CLIENT_ID` and `OAUTH_CLIENT_SECRET` values that you got from your database earlier in this procedure.

  5. Complete the rest of the procedure for [Connecting Looker to your database](/looker/docs/connecting-to-your-db#creating_a_new_database_connection).

Once you configure the Looker connection to your database, you can test the connection itself by doing either of the following:

  * Select the **Test** button at the bottom of the **Connections Settings** page, as described on the [Connecting Looker to your database](/looker/docs/connecting-to-your-db#testing_your_connection_settings) documentation page.
  * Select the **Test** button by the connection's listing on the **Connections** admin page, as described on the [Connections](/looker/docs/admin-panel-database-connections#testing_connections) documentation page.

Beyond that, you can test the connection and deploy it on a model by following these steps:

  1. In Looker, go into [Development Mode](/looker/docs/dev-mode-prod-mode).
  2. [Navigate to the project files](/looker/docs/accessing-project-files) for a Looker project that uses your Snowflake connection.
  3. Open a [model file](/looker/docs/model-and-view-files#model_files) and replace the model's [`connection`](/looker/docs/reference/param-model-connection) value with the name of the new Snowflake connection, and then save the model file.
  4. Open one of the model's Explores or dashboards, and run a query. When you try to run a query, Looker will prompt you to [sign in to Snowflake](/looker/docs/db-config-snowflake#signing_into_snowflake_to_run_queries).
  5. Follow the sign in prompts for Snowflake and enter your Snowflake credentials.

Once you successfully sign in to Snowflake, Looker will return you back to your query. If your query runs correctly, you can [commit the new connection value](/looker/docs/version-control-and-deploying-changes#committing_changes) and [deploy your changes to production](/looker/docs/version-control-and-deploying-changes#deploying_to_production).

### Signing in to Snowflake to run queries

Once the Snowflake connection is set up for OAuth, users will be prompted to sign in to Snowflake before running queries. This includes queries from Explores, dashboards, Looks, and SQL Runner.

![The Looker UI, showing the OAuth login prompt.](/static/looker/docs/images/admin-oauth-login-624.png)

Users can also sign in to Snowflake from the **OAuth Connection Credentials** section on their **Account** page.

To sign in to your Snowflake account using Looker, follow these steps:

![The Account page in Looker, showing the OAuth Connection Credentials section.](/static/looker/docs/images/admin-oauth-credentials-2304.png)

  1. Click the Looker user menu.
  2. Select **Account**.
  3. In the **Account** page, go to the **OAuth Connection Credentials** section, and select the **Log In** button for the appropriate Snowflake database.

Selecting **Log In** will display a Snowflake login dialog. Enter your Snowflake credentials and select **Log In** , and then select **Allow** to give Looker access to your Snowflake account.

Once you sign in to Snowflake through Looker, you can sign out or reauthorize your credentials at any time through your **Account** page, as described on the [Personalizing your user account](/looker/docs/user-account#oauth) documentation page.

## Feature support

For Looker to support some features, your database dialect must also support them.

Snowflake supports the following features as of Looker 25.2:

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
List Type | Yes  
Percentile | Yes  
Distinct Percentile | No  
SQL Runner Show Processes | No  
SQL Runner Describe Table | Yes  
SQL Runner Show Indexes | No  
SQL Runner Select 10 | Yes  
SQL Runner Count | Yes  
SQL Explain | Yes  
Oauth Credentials | Yes  
Context Comments | Yes  
Connection Pooling | Yes  
HLL Sketches | Yes  
Aggregate Awareness | Yes  
Incremental PDTs | Yes  
Milliseconds | Yes  
Microseconds | Yes  
Materialized Views | No  
Approximate Count Distinct | No  
  
## Next steps

After you have connected your database to Looker, [configure sign-in options for your users](/looker/docs/getting-started-with-users).