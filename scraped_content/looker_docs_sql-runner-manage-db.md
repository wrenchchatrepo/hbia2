# https://cloud.google.com/looker/docs/sql-runner-manage-db

Depth: 3

SQL Runner provides a way to directly access your database and use that access in a variety of ways. Using SQL Runner, you can navigate the tables in your schema, use an ad hoc Explore from a SQL query, run prewritten descriptive queries on your data, see your SQL Runner history, download results, share queries, add to a LookML Project as a derived table, and perform other useful tasks.

This page describes how to modify your database schema and data using SQL Runner, view your database's execution plan for a query with the EXAMINE statement, and how to use SQL Runner to get information about your database. See these other documentation pages for information on:

  * [SQL Runner basics](/looker/docs/sql-runner-basics)
  * [Using SQL Runner to create queries and Explores](/looker/docs/sql-runner-create-queries-and-explores)
  * [Using SQL Runner to create derived tables](/looker/docs/sql-runner-create-derived-tables)

## Modifying database schema and data

In addition to running queries on your database, the **Database** tab in SQL Runner lets you execute Data Definition Language (DDL) and Data Manipulation Language (DML) statements on your database. You can use SQL Runner to make schema changes (such as create, drop, and alter) and data changes (such as insert, update, and delete). SQL dialects have varying support for DDL and DML statements, so see the documentation for your database to find out which statements are supported.

**Note:** For Google BigQuery connections that use [read-only OAuth credentials](/looker/docs/best-practices/oauth-read-only), users cannot use SQL Runner to execute write operations on the database. For other database connections, Looker does not control authorization of which SQL statements a user is allowed to run on your database. Looker users with the [`use_sql_runner`](/looker/docs/admin-panel-users-roles#use_sql_runner) permission are given access to SQL Runner, but SQL Runner does not gate which commands the user can execute. If your database administrator wants to prevent SQL Runner users from modifying the database schema, the adminstrator must do this by configuring user permissions for the database itself.

To execute a DDL or DML statement on your database in SQL Runner, follow these steps:

  1. [Navigate to SQL Runner](/looker/docs/sql-runner-basics#navigating_to_sql_runner).
  2. In SQL Runner, click the **Database** tab.
  3. Enter the DDL or DML statement in the SQL Runner **Query** box. (See the documentation for your database dialect for the support and syntax of DDL and DML statements.)
  4. Click **Run** to execute the statement on your database.

If the statement is successfully executed on your database, the SQL **Results** box will show a confirmation.

## Examining an execution plan using `EXPLAIN`

In addition to running SQL queries against your database, you can use SQL Runner to run an `EXPLAIN` function for a query. The `EXPLAIN` function, which is supported by most SQL dialects, returns the database's execution plan for a query.

![](/static/looker/docs/images/develop-explain-in-sql-runner-2308.png)

  1. From an Explore, run a query and click the **SQL** tab of the **Data** area to view the query's SQL command.
  2. In the **SQL** tab of the Explore, click the **Explain in SQL Runner** button.

Looker will open SQL Runner and load the query within an `EXPLAIN` function.

  3. In SQL Runner, click **Run** to execute the `EXPLAIN` function.

  4. View the output of the `EXPLAIN` function.

The exact information and format of the `EXPLAIN` response will depend on your specific dialect, so you should see the documentation for your dialect for specifics.

In the preceding MySQL example, the `EXPLAIN` function returns a list of the steps taken by the database to complete the query. This may be useful for queries that seem slow to execute, since you may find that your database is scanning an entire table in a query, when perhaps the table could use an index to improve performance.

For a step-by-step example of using `EXPLAIN` in SQL Runner to optimize SQL, see the [How to Optimize SQL with EXPLAIN ](https://community.looker.com/technical-tips-tricks-1021/how-to-optimize-sql-with-explain-30772) Community post.

## Getting information about your database

The **Database** tab in SQL Runner has a bunch of tools to give you insight into your database.

### Getting database connection information

When you choose a connection in SQL Runner, Looker displays the database dialect for that connection at the right of the **SQL QUERY** banner. If you navigated to SQL Runner by choosing **Open in SQL Runner** or **Explain in SQL Runner** , then Looker preselects the appropriate connection for you and displays the connection's database dialect.

![](/static/looker/docs/images/dev-sql-runner-dialect-2308.png)

Click the connection gear menu to get more options for the database connection:

![](/static/looker/docs/images/dev-sql-runner-show-processes-2308.png)

  * Select the **Show Processes** option to display information about queries and processes currently running on the connection.
  * Select the **Refresh Schemas & Tables** option to repopulate the SQL Runner left navigation pane with the schemas and tables in the database.

### BigQuery gear menu options

When you choose a [BigQuery](/looker/docs/db-config-google-bigquery) connection that supports multiple databases, Looker displays dialect-specific options in the gear menu. The menu item switches between **Show available projects** and **Search public projects** , depending on which option is selected.

![](/static/looker/docs/images/sql-runner-big-query-gear-menu-2204.png)

  * Select **Refresh Schemas & Tables** to repopulate the SQL Runner left navigation pane with the schemas and tables that are in the database.
  * When available projects are displayed, there is a gear menu option to **Search public projects**. Select this option to search for public datasets that are not visible in the information schema.
  * When public projects are displayed, there is a gear menu option to **Show available projects**. Select this option to revert the display back to connection-specific BigQuery projects and tables in the SQL Runner left navigation pane.

### Searching your database

SQL Runner displays a search box under the selected **Schema** (or **Dataset** , for [Google BigQuery](/looker/docs/db-config-google-bigquery) connections).

The SQL Runner search browses the names of all tables and table columns that contain the string in the search box. In the following figure, 'airport_name' is a column and 'airport_remarks' is a table.

![](/static/looker/docs/images/develop-sql-runner-search-2206.png)

Click on one of the search results to navigate to that item in SQL Runner.

### Getting table information

> By default, SQL Runner preloads all table information when you select a connection and a schema. For connections that have many tables or very large tables, an admin can disable this behavior by deselecting the **SQL Runner Precache** option in the [Connections page](/looker/docs/connecting-to-your-db#sql_runner_precache).

SQL Runner's left-hand navigation panel lets you navigate the schemas and tables in your connections. Select a connection and a schema to see all the tables in that schema. Click on a table name to see the fields in that table.

SQL Runner has some prewritten queries to help you understand your data. In order to use these queries, click the gear that appears next to the name of a table or table column and select the query you want to run. Looker generates the SQL automatically in the **SQL Query** section, and the query will be run.

> The available queries will vary by database dialect.

#### Table information

Looker displays the following options when you click the gear next to a table name:

![](/static/looker/docs/images/dev-sql-runner-table-menu-2308.png)

  * **Explore Table** : Opens a new browser tab to a [Looker Explore](/looker/docs/creating-and-editing-explores) of the table.
  * **Describe** : Displays the column names in the underlying table as well as their data types.
  * **Show Indexes** : Displays information about how the table is indexed.
  * **Select 10** : Returns a query of the first ten rows in the table. This is a good way to get a sense of what the data actually looks like.
  * **Count** : Returns a simple `count(*)` query to get the total row count of the table.

#### Column information

Click a table name to see the columns in the table. Looker displays the following options when you click the gear next to a column name:

![](/static/looker/docs/images/dev-sql-runner-field-menu-2308.png)

  * **Most Common Values** : Returns a query of the most common values for that table column, along with a count of the number of times that value is found in the column.
  * **Approximate Count Distinct** : Displays an approximate count of the number of distinct values found in the column.

##### Getting column data type information

You can use SQL Runner to get column data type information by performing the following steps:

![](/static/looker/docs/images/sql-runner-columns-2402.png)

  1. In SQL Runner, select the database connection from the **Connection** drop-down.
  2. Select the schema from the **Schema** drop-down. (For BigQuery connections, select **Project** and **Dataset**.)
  3. SQL Runner displays the list of tables in that schema on your database. Click on a table to see the columns in that table.
  4. Each column name has an icon to represent the data type. Hover over a column name to see the type of data in that column.

#### Editing the prebuilt SQL queries

You can edit any SQL query in the **Query** area, including the preset SQL queries chosen from the table and field gear menus.

For example, you can use the SQL Runner **Count** query to load in a basic count command for a database, then edit the SQL query. So if you think the `id` column in the `public.users` table could be a primary key, you can validate that there are no duplicate values by editing the count query like this:
    
    
    SELECT id ,COUNT(*)
    FROM public.users
    GROUP BY 1
    ORDER BY 2 DESC
    LIMIT 10
    

Because the query is sorted by the count before the results are limited to 10 rows, the results will include the highest count values. If this query returns a count of 1 for each `id` value, then `id` would likely be the primary key in this table. However, this query specifies only the rows in the table at query runtime. Since future insertions to the database may disqualify `id` as a primary key, we recommend implementing restrictions on your database to ensure that your primary keys are unique.