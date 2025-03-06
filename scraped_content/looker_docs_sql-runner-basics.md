# https://cloud.google.com/looker/docs/sql-runner-basics

Depth: 3

SQL Runner provides a way to directly access your database and to leverage that access in a variety of ways. Using SQL Runner, you can easily navigate the tables in your schema, use an ad hoc Explore from a SQL query, run prewritten descriptive queries on your data, see your SQL Runner history, download results, share queries, add to a LookML project as a derived table, and perform other useful tasks.

This page describes how to navigate to SQL Runner and shows which database dialects support SQL Runner features. See these other documentation pages for information on:

  * [Using SQL Runner to create queries and Explores](/looker/docs/sql-runner-create-queries-and-explores)
  * [Using SQL Runner to create derived tables](/looker/docs/sql-runner-create-derived-tables)
  * [Managing database functions with SQL Runner](/looker/docs/sql-runner-manage-db)

## Navigating to SQL Runner

If you have the permissions [to see LookML](/looker/docs/admin-panel-users-roles#see_lookml) and [to use SQL Runner](/looker/docs/admin-panel-users-roles#use_sql_runner), you can navigate to SQL Runner in two ways:

  * In the **Develop** menu, select **SQL Runner**.

![](/static/looker/docs/images/dev-nav-sql-runner-2300.png)

  * From an Explore, click **SQL** on the Data bar to see the SQL. Then click **Open in SQL Runner** to see the query in SQL Runner, or click **Explain in SQL Runner** to open SQL Runner and request the database's execution plan for the query.

![](/static/looker/docs/images/dev-nav-sql-runner-b-2120.png)

## Basic SQL Runner usage

This section describes how to use SQL Runner to directly access tables in your schema, run a SQL query on your data, and see query results.

![](/static/looker/docs/images/develop-sql-runner-2220.png)

  1. Select the **Connection** that you want to query.
  2. Select the **Schema** that you want to query. For [Google BigQuery](/looker/docs/db-config-google-bigquery) connections, select the **Project** (if your BigQuery connection supports multiple databases) and the **Dataset**.
  3. Select a table to show its columns in the Results area.
  4. Optionally, select the ⊝ icon to collapse the left panel. If the panel is collapsed, select the ⊕ icon to expand the panel.
  5. Check the database SQL dialect used for the query. The dialect is displayed on the right side of the **Query** bar.
  6. Write a SQL command in the text box below the **Query** bar.
  7. Select **Run** to execute the SQL query.
  8. View the information that is returned by the database in the **Results** area.

## SQL Runner visualizations

If your Looker admin has enabled the [**SQL Runner Vis**](/looker/docs/admin-panel-general-labs#sql_runner_vis) Labs feature, you can create visualizations directly in SQL Runner.

![](/static/looker/docs/images/dev-sql-runner-viz-2220.png)

For more information, see the [Using SQL Runner to create queries and Explores](/looker/docs/sql-runner-create-queries-and-explores#creating_visualizations_with_sql_runner) documentation page.

## Supported database dialects for SQL Runner features

For Looker to support SQL Runner features in your Looker project, your database dialect must also support them. The following tables show which dialects support each SQL Runner feature.

These dialects support SQL Runner Show Processes:

Dialect | Supported?  
---|---  
Actian Avalanche | No  
Amazon Athena | No  
Amazon Aurora MySQL | Yes  
Amazon Redshift | Yes  
Apache Druid | No  
Apache Druid 0.13+ | No  
Apache Druid 0.18+ | No  
Apache Hive 2.3+ | No  
Apache Hive 3.1.2+ | No  
Apache Spark 3+ | No  
ClickHouse | Yes  
Cloudera Impala 3.1+ | No  
Cloudera Impala 3.1+ with Native Driver | No  
Cloudera Impala with Native Driver | No  
DataVirtuality | No  
Databricks | No  
Denodo 7 | Yes  
Denodo 8 | Yes  
Dremio | No  
Dremio 11+ | No  
Exasol | No  
Firebolt | Yes  
Google BigQuery Legacy SQL | No  
Google BigQuery Standard SQL | No  
Google Cloud PostgreSQL | Yes  
Google Cloud SQL | Yes  
Google Spanner | No  
Greenplum | Yes  
HyperSQL | No  
IBM Netezza | No  
MariaDB | Yes  
Microsoft Azure PostgreSQL | Yes  
Microsoft Azure SQL Database | Yes  
Microsoft Azure Synapse Analytics | No  
Microsoft SQL Server 2008+ | Yes  
Microsoft SQL Server 2012+ | Yes  
Microsoft SQL Server 2016 | Yes  
Microsoft SQL Server 2017+ | Yes  
MongoBI | Yes  
MySQL | Yes  
MySQL 8.0.12+ | Yes  
Oracle | Yes  
Oracle ADWC | Yes  
PostgreSQL 9.5+ | Yes  
PostgreSQL pre-9.5 | Yes  
PrestoDB | Yes  
PrestoSQL | Yes  
SAP HANA | Yes  
SAP HANA 2+ | Yes  
SingleStore | Yes  
SingleStore 7+ | Yes  
Snowflake | No  
Teradata | No  
Trino | Yes  
Vector | No  
Vertica | Yes  
  
These dialects support SQL Runner Describe Table:

Dialect | Supported?  
---|---  
Actian Avalanche | Yes  
Amazon Athena | Yes  
Amazon Aurora MySQL | Yes  
Amazon Redshift | Yes  
Apache Druid | No  
Apache Druid 0.13+ | No  
Apache Druid 0.18+ | No  
Apache Hive 2.3+ | Yes  
Apache Hive 3.1.2+ | Yes  
Apache Spark 3+ | Yes  
ClickHouse | Yes  
Cloudera Impala 3.1+ | Yes  
Cloudera Impala 3.1+ with Native Driver | Yes  
Cloudera Impala with Native Driver | Yes  
DataVirtuality | Yes  
Databricks | Yes  
Denodo 7 | Yes  
Denodo 8 | Yes  
Dremio | Yes  
Dremio 11+ | Yes  
Exasol | Yes  
Firebolt | Yes  
Google BigQuery Legacy SQL | No  
Google BigQuery Standard SQL | No  
Google Cloud PostgreSQL | Yes  
Google Cloud SQL | Yes  
Google Spanner | No  
Greenplum | Yes  
HyperSQL | Yes  
IBM Netezza | No  
MariaDB | Yes  
Microsoft Azure PostgreSQL | Yes  
Microsoft Azure SQL Database | Yes  
Microsoft Azure Synapse Analytics | Yes  
Microsoft SQL Server 2008+ | Yes  
Microsoft SQL Server 2012+ | Yes  
Microsoft SQL Server 2016 | Yes  
Microsoft SQL Server 2017+ | Yes  
MongoBI | Yes  
MySQL | Yes  
MySQL 8.0.12+ | Yes  
Oracle | Yes  
Oracle ADWC | Yes  
PostgreSQL 9.5+ | Yes  
PostgreSQL pre-9.5 | Yes  
PrestoDB | Yes  
PrestoSQL | Yes  
SAP HANA | Yes  
SAP HANA 2+ | Yes  
SingleStore | Yes  
SingleStore 7+ | Yes  
Snowflake | Yes  
Teradata | Yes  
Trino | Yes  
Vector | Yes  
Vertica | Yes  
  
These dialects support SQL Runner Show Indexes:

Dialect | Supported?  
---|---  
Actian Avalanche | Yes  
Amazon Athena | No  
Amazon Aurora MySQL | Yes  
Amazon Redshift | Yes  
Apache Druid | No  
Apache Druid 0.13+ | No  
Apache Druid 0.18+ | No  
Apache Hive 2.3+ | Yes  
Apache Hive 3.1.2+ | No  
Apache Spark 3+ | No  
ClickHouse | No  
Cloudera Impala 3.1+ | No  
Cloudera Impala 3.1+ with Native Driver | No  
Cloudera Impala with Native Driver | No  
DataVirtuality | No  
Databricks | No  
Denodo 7 | No  
Denodo 8 | No  
Dremio | No  
Dremio 11+ | No  
Exasol | No  
Firebolt | Yes  
Google BigQuery Legacy SQL | No  
Google BigQuery Standard SQL | No  
Google Cloud PostgreSQL | Yes  
Google Cloud SQL | Yes  
Google Spanner | No  
Greenplum | Yes  
HyperSQL | Yes  
IBM Netezza | No  
MariaDB | Yes  
Microsoft Azure PostgreSQL | Yes  
Microsoft Azure SQL Database | Yes  
Microsoft Azure Synapse Analytics | No  
Microsoft SQL Server 2008+ | Yes  
Microsoft SQL Server 2012+ | Yes  
Microsoft SQL Server 2016 | Yes  
Microsoft SQL Server 2017+ | Yes  
MongoBI | Yes  
MySQL | Yes  
MySQL 8.0.12+ | Yes  
Oracle | Yes  
Oracle ADWC | No  
PostgreSQL 9.5+ | Yes  
PostgreSQL pre-9.5 | Yes  
PrestoDB | No  
PrestoSQL | No  
SAP HANA | No  
SAP HANA 2+ | No  
SingleStore | Yes  
SingleStore 7+ | Yes  
Snowflake | No  
Teradata | Yes  
Trino | No  
Vector | Yes  
Vertica | No  
  
These dialects support SQL Runner Select 10:

Dialect | Supported?  
---|---  
Actian Avalanche | Yes  
Amazon Athena | Yes  
Amazon Aurora MySQL | Yes  
Amazon Redshift | Yes  
Apache Druid | Yes  
Apache Druid 0.13+ | Yes  
Apache Druid 0.18+ | Yes  
Apache Hive 2.3+ | Yes  
Apache Hive 3.1.2+ | Yes  
Apache Spark 3+ | Yes  
ClickHouse | Yes  
Cloudera Impala 3.1+ | Yes  
Cloudera Impala 3.1+ with Native Driver | Yes  
Cloudera Impala with Native Driver | Yes  
DataVirtuality | Yes  
Databricks | Yes  
Denodo 7 | Yes  
Denodo 8 | Yes  
Dremio | Yes  
Dremio 11+ | Yes  
Exasol | Yes  
Firebolt | Yes  
Google BigQuery Legacy SQL | Yes  
Google BigQuery Standard SQL | Yes  
Google Cloud PostgreSQL | Yes  
Google Cloud SQL | Yes  
Google Spanner | Yes  
Greenplum | Yes  
HyperSQL | Yes  
IBM Netezza | Yes  
MariaDB | Yes  
Microsoft Azure PostgreSQL | Yes  
Microsoft Azure SQL Database | Yes  
Microsoft Azure Synapse Analytics | Yes  
Microsoft SQL Server 2008+ | Yes  
Microsoft SQL Server 2012+ | Yes  
Microsoft SQL Server 2016 | Yes  
Microsoft SQL Server 2017+ | Yes  
MongoBI | Yes  
MySQL | Yes  
MySQL 8.0.12+ | Yes  
Oracle | Yes  
Oracle ADWC | Yes  
PostgreSQL 9.5+ | Yes  
PostgreSQL pre-9.5 | Yes  
PrestoDB | Yes  
PrestoSQL | Yes  
SAP HANA | Yes  
SAP HANA 2+ | Yes  
SingleStore | Yes  
SingleStore 7+ | Yes  
Snowflake | Yes  
Teradata | Yes  
Trino | Yes  
Vector | Yes  
Vertica | Yes  
  
These dialects support SQL Runner Count:

Dialect | Supported?  
---|---  
Actian Avalanche | Yes  
Amazon Athena | Yes  
Amazon Aurora MySQL | Yes  
Amazon Redshift | Yes  
Apache Druid | Yes  
Apache Druid 0.13+ | Yes  
Apache Druid 0.18+ | Yes  
Apache Hive 2.3+ | Yes  
Apache Hive 3.1.2+ | Yes  
Apache Spark 3+ | Yes  
ClickHouse | Yes  
Cloudera Impala 3.1+ | Yes  
Cloudera Impala 3.1+ with Native Driver | Yes  
Cloudera Impala with Native Driver | Yes  
DataVirtuality | Yes  
Databricks | Yes  
Denodo 7 | Yes  
Denodo 8 | Yes  
Dremio | Yes  
Dremio 11+ | Yes  
Exasol | Yes  
Firebolt | Yes  
Google BigQuery Legacy SQL | Yes  
Google BigQuery Standard SQL | Yes  
Google Cloud PostgreSQL | Yes  
Google Cloud SQL | Yes  
Google Spanner | Yes  
Greenplum | Yes  
HyperSQL | Yes  
IBM Netezza | Yes  
MariaDB | Yes  
Microsoft Azure PostgreSQL | Yes  
Microsoft Azure SQL Database | Yes  
Microsoft Azure Synapse Analytics | Yes  
Microsoft SQL Server 2008+ | Yes  
Microsoft SQL Server 2012+ | Yes  
Microsoft SQL Server 2016 | Yes  
Microsoft SQL Server 2017+ | Yes  
MongoBI | Yes  
MySQL | Yes  
MySQL 8.0.12+ | Yes  
Oracle | Yes  
Oracle ADWC | Yes  
PostgreSQL 9.5+ | Yes  
PostgreSQL pre-9.5 | Yes  
PrestoDB | Yes  
PrestoSQL | Yes  
SAP HANA | Yes  
SAP HANA 2+ | Yes  
SingleStore | Yes  
SingleStore 7+ | Yes  
Snowflake | Yes  
Teradata | Yes  
Trino | Yes  
Vector | Yes  
Vertica | Yes  
  
These dialects support SQL Explain:

Dialect | Supported?  
---|---  
Actian Avalanche | No  
Amazon Athena | No  
Amazon Aurora MySQL | Yes  
Amazon Redshift | Yes  
Apache Druid | Yes  
Apache Druid 0.13+ | Yes  
Apache Druid 0.18+ | Yes  
Apache Hive 2.3+ | Yes  
Apache Hive 3.1.2+ | Yes  
Apache Spark 3+ | Yes  
ClickHouse | No  
Cloudera Impala 3.1+ | Yes  
Cloudera Impala 3.1+ with Native Driver | Yes  
Cloudera Impala with Native Driver | Yes  
DataVirtuality | No  
Databricks | Yes  
Denodo 7 | No  
Denodo 8 | No  
Dremio | No  
Dremio 11+ | No  
Exasol | No  
Firebolt | Yes  
Google BigQuery Legacy SQL | No  
Google BigQuery Standard SQL | No  
Google Cloud PostgreSQL | Yes  
Google Cloud SQL | Yes  
Google Spanner | No  
Greenplum | Yes  
HyperSQL | No  
IBM Netezza | Yes  
MariaDB | Yes  
Microsoft Azure PostgreSQL | Yes  
Microsoft Azure SQL Database | No  
Microsoft Azure Synapse Analytics | Yes  
Microsoft SQL Server 2008+ | No  
Microsoft SQL Server 2012+ | No  
Microsoft SQL Server 2016 | No  
Microsoft SQL Server 2017+ | No  
MongoBI | Yes  
MySQL | Yes  
MySQL 8.0.12+ | Yes  
Oracle | No  
Oracle ADWC | No  
PostgreSQL 9.5+ | Yes  
PostgreSQL pre-9.5 | Yes  
PrestoDB | Yes  
PrestoSQL | Yes  
SAP HANA | No  
SAP HANA 2+ | No  
SingleStore | Yes  
SingleStore 7+ | Yes  
Snowflake | Yes  
Teradata | Yes  
Trino | Yes  
Vector | No  
Vertica | Yes