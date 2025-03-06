# https://cloud.google.com/looker/docs/error-catalog

Depth: 3

The following table is a collection of some common error messages surfaced in Looker, explanations of their underlying causes and where they occur, and troubleshooting resources. The errors appear according to how frequently they are reported to Looker Support, in descending order, starting with the greatest number of support requests at the top.

The **Location** column indicates where in Looker the error message is displayed, and includes the following options (some errors can appear in more than one location in the product):

IDE = [LookML validator/IDE](/looker/docs/lookml-validation)

Ex = [Explore](/looker/docs/creating-and-editing-explores)

SQL = [SQL Runner](/looker/docs/sql-runner-basics)

LD = [LookML dashboard](/looker/docs/reference/lookml-dashboard-overview)

D = [Dashboard](/looker/docs/dashboards)

S = [Schedules](/looker/docs/scheduling)

Error message | Location | Possible Causes | Troubleshooting Resources  
---|---|---|---  
`Variable not found (?).` |  IDE | 

  * The Liquid for variable reference, `{{ }}`, is nested within Liquid for logic, `{% %}`. 
  * A templated filter references a table that is not joined into a derived table. 
  * A field referenced in Liquid is not fully scoped with a view name (`view_name.field_name`). 
  * A filter's value is referenced inside another LookML dashboard filter. 
  * A `parameter` parameter's value is not compatible with the corresponding `type`. For example: `{% if parameters.change_value._parameter_value == "'AA'" %}`. Review the `parameter` `type` to ensure that the value evaluates correctly (`type: string` versus `type: unquoted`). 
  * A field is referenced correctly in Liquid as `view_name.field_name`, but `field_name` is not defined in the scoped view `view_name`, or the view is aliased with `from` in an Explore. 
  * A Liquid reference to a variable is not defined, or the reference includes a typo. 
  * A Liquid reference includes a dimension group of `type: time`, but not the specific timeframe. For example, instead of `{{` `view_name.creation_date }}`, the reference should use `{{` `view_name.creation_date_year }}`. 
  * A field is using Liquid with LookML substitution operator syntax, `${view_name.field_name}`, instead of without, as `view_name.field_name`. 

| 

  * [Liquid variable reference](/looker/docs/liquid-variable-reference#getting_the_%E2%80%9Cvariable_not_found%E2%80%9D_error)
  * [Templated filters and derived tables (Community post)](https://www.googlecloudcommunity.com/gc/Technical-Tips-Tricks/Templated-Filters-and-Derived-Tables-Variable-not-found-quot/ta-p/587380)
  * [`from` (for Explores)](/looker/docs/reference/param-explore-from)
  * [`from` (for joins)](/looker/docs/reference/param-explore-join-from)
  * [Dimension groups must be referenced by their individual dimensions](/looker/docs/reference/param-field-dimension-group#dimension_groups_must_be_referenced_by_their_individual_dimensions)

  
`Inaccessible view (?). (?) is not accessible in explore (?). Check for missing joins in explore (?).` |  IDE | 

  * The referenced view doesn't exist. 
  * A join is missing, making the view inaccessible to some Explores. 
  * The view is renamed with a `from` parameter in an Explore. 

| 

  * [Error: Unknown or inaccessible field (Best Practices page)](/looker/docs/best-practices/error-unknown-or-inaccessible-field)
  * [`from` (for Explores)](/looker/docs/reference/param-explore-from)
  * [`from` (for joins)](/looker/docs/reference/param-explore-join-from)

  
`Unknown or inaccessible field (?). Check for typos or append a timeframe to the name if the field is type time.` |  IDE |  Any of the possible causes listed for the error `Inaccessible view (?). (?) is not accessible in explore (?). Check for missing joins in explore (?).` may apply, plus the following: 

  * There is a typo in a field name or in a reference to the field. 
  * The field is excluded from an Explore by the `fields` parameter. 
  * The reference is to a `dimension_group` without a timeframe specified. 

| 

  * [`fields` (for Explores)](/looker/docs/reference/param-explore-fields)
  * [`fields` (for joins)](/looker/docs/reference/param-explore-join-fields)
[Dimension groups must be referenced by their individual dimensions](/looker/docs/reference/param-field-dimension-group#dimension_groups_must_be_referenced_by_their_individual_dimensions) 
  
`Unknown view (?).` |  IDE Ex SQL | 

  * A view is not included in the model file. 
  * An `explore` is extending a base `explore` that is missing a `view_name` parameter. 
  * An Explore name defined in the `explore` parameter is based on a misspelled or nonexistent view name. 
  * A model-based SQL Runner query is running with the incorrect model selected. 

| 

  * [`include` model parameter reference](/looker/docs/reference/param-model-include)
  * [`extends` (for Explores)](/looker/docs/reference/param-explore-extends#definition)
  * [`explore` parameter](/looker/docs/reference/param-explore-explore)
  * [Running a query against a LookML model in SQL Runner](/looker/docs/sql-runner-create-queries-and-explores#running_a_query_against_a_lookml_model)

  
`Unknown view (?). View does not exist in model (?). Check for typos or missing include statements.` |  IDE Ex SQL | 

  * An `explore` is extending a base `explore` that is missing a `view_name` parameter, and fields from any of the joined views reference the base `explore` name. 
  * A field references a view that is misspelled, nonexistent, or not joined to applicable Explores. 

| 

  * [`extends` (for Explores)](/looker/docs/reference/param-explore-extends#definition)
  * [Scoping and naming LookML objects](/looker/docs/sql-and-referring-to-lookml#scoping_and_naming)

  
`Unknown field (?) in filter` |  IDE | 

  * A native derived table (NDT) definition includes a `bind_all_filters` parameter on a custom field that is not defined in LookML. 
  * A LookML filter references a LookML field that is commented out or that does not exist. 
  * A LookML filter references a LookML field from a different view, and the field is not fully scoped nor joined into all relevant `explore` parameters. 

| 

  * [Native derived table `explore_source` reference](/looker/docs/reference/param-view-explore-source#defining_a_native_derived_table)
  * [`filters` for LookML dashboards](/looker/docs/reference/param-lookml-dashboard#filters-for-dashboard)
  * [`always_filter` reference ](/reference/explore-params/always_filter)
  * [`access_filter` reference](/looker/docs/reference/param-explore-access-filter)
  * [`filters` for measures](/looker/docs/reference/param-field-filters)

  
`Measures with Looker aggregations (sum, average, min, max, list types) may not reference other measures.` |  IDE |  A measure is referenced inside the SQL definition of another aggregate-type measure.  | 

  * [Measure type category reference](/looker/docs/reference/param-measure-types#measure_type_categories)
  * [Error: Measures with Looker aggregations (sum, average, min, max, list types) may not reference other measures (Best Practices page)](/looker/docs/best-practices/error-measures-with-looker-aggregations-reference-other-aggregations)
  * [How to dimensionalize a measure in Looker (Best Practices page)](/looker/docs/best-practices/how-to-dimensionalize-a-measure)

  
`Unknown view (?). View (?) does not exist in model (?). Check for typos or missing include statements in (?).` |  IDE |  A view is not included in a model file, or it is included but is misspelled.  | 

  * [Trouble getting started with model/view/Explore (Community post)](https://www.googlecloudcommunity.com/gc/Modeling/Trouble-Getting-Started-with-Model-View-Explore/td-p/566554?postid=31043#post31043)
  * [`include` model parameter reference](/looker/docs/reference/param-model-include)

  
`Can't construct persistent derived table (?), connection (?) could not be registered` |  IDE Ex | 

  * Any dependencies for an existing PDT have failed to build. 
  * There is an issue with the connection, which needs to be diagnosed by testing the connection (for example, testing the connection may reveal that the Looker user may not have sufficient own or write access to the database). 
  * Imported project files, such as a view that defines the failing PDT, or a view that is referenced by the failing PDT, are not included in the importing project. 
  * The database connection does not have the **Persistent Derived Tables** setting enabled. 
  * A Looker Block's code has not been updated to the connection's SQL dialect, if different from the dialect for which the block was written. 
  * OAuth is enabled for a Snowflake or BigQuery connection. 
  * A value other than the default value, `TRUE`, has been set for the Snowflake database `AUTOCOMMIT` parameter. 

| 

  * [Testing database connections in Looker](/looker/docs/admin-panel-database-connections#testing_connections)
  * [Including files from an imported project](/looker/docs/importing-projects#including_files_from_an_imported_project)
  * [Persistent Derived Tables connection setting](/looker/docs/connecting-to-your-db#persistent_derived_tables)
  * [OAuth for BigQuery connections](/looker/docs/db-config-google-bigquery#oauth_for_bigquery_connections)
  * [OAuth for Snowflake connections](/looker/docs/db-config-snowflake#configuring_oauth_for_snowflake_connections)

  
`Unknown or excluded suggest_dimension (?) in field (?)` |  IDE | 

  * A field referenced by a `suggest_dimension` parameter does not exist, has been commented out, or is excluded in an Explore by a `fields` parameter. 
  * A field referenced by a `suggest_dimension` parameter is defined in another view, but is not fully scoped as `view_name.field_name` in the reference. 
  * A `suggest_dimension` parameter references a field in a different view that is not joined into all relevant `explore` parameters, or a view that is aliased in an `explore` with a `from` parameter. 

| 

  * [Error: Unknown or inaccessible field (Best Practices page)](/looker/docs/best-practices/error-unknown-or-inaccessible-field)
  * [`suggest_dimension` parameter reference](/looker/docs/reference/param-field-suggest-dimension)
  * [`from` (for Explores)](/looker/docs/reference/param-explore-from)
  * [`from` (for joins)](/looker/docs/reference/param-explore-join-from)
  * [`fields` (for Explores)](/looker/docs/reference/param-explore-fields)
  * [`fields` (for joins)](/looker/docs/reference/param-explore-join-fields)

  
`A view named (?) has been defined multiple times. Each view in a model must have a unique name.` |  IDE |  Views with identical names are referenced in the same model, including views imported into the project. View names must be unique in a model.  |  [`view` parameter reference](/looker/docs/reference/param-view-view)  
`This include does not match any files` |  IDE | 

  * A typo in the path to the file is causing en error. 
  * A folder reference is using incorrect syntax. 
  * A project import reference is using incorrect syntax. 

| 

  * [`include` model parameter reference](/looker/docs/reference/param-model-include)
  * [Using `include` with IDE folders](/looker/docs/ide-folders#using_include_with_ide_folders)
  * [Including files from an imported project](/looker/docs/importing-projects#including_files_from_an_imported_project)
  * [Referencing files from an imported project](/looker/docs/importing-projects#referencing_files_from_an_imported_project)

  
`SQL Dialect does not support Symmetric Aggregates with percentiles, field ignored.` |  Ex |  The database dialect does not support measures of `type: median` or `type: percentile` with symmetric aggregates.  | 

  * [Not all database dialects support `median` or `percentile` measure types with symmetric aggregates ](/reference/explore-params/symmetric_aggregates#not_all_database_dialects_support_median_and_percentile_measure_types_with_symmetric_aggregates)
  * [Understanding Symmetric Aggregates (Best Practices page)](/looker/docs/best-practices/understanding-symmetric-aggregates)

  
`Cannot use native derived table (?) with bind_all_filters outside of its source explore (?)` |  IDE Ex |  A native derived table (NDT) with a `bind_all_filters` parameter is joined to one or more Explores other than the Explore defined in the `explore_source` parameter.  |  [Using `bind_all_filters`](/looker/docs/reference/param-view-explore-source#using_bind_all_filters)  
`Measures of type count do not use the sql parameter. Use count_distinct to count by something other than the primary key, or remove the sql parameter.` |  IDE |  A `sql` parameter is used in a measure of `type: count`. Count type measures perform a count by the primary key declared in the view file and do not require a `sql` parameter.  | 

  * [`count` measure type reference](/looker/docs/reference/param-measure-types#count)
  * [How to count a non-primary key (Community post)](https://www.googlecloudcommunity.com/gc/Technical-Tips-Tricks/How-to-count-a-non-primary-key/ta-p/587307)

  
`An explore named (?) has been defined multiple times. Each explore in a model must have a unique name.` |  IDE LD | 

  * An Explore name defined in the `explore` parameter of a model file is duplicating another existing Explore name. Explore names must be unique in a model. 
  * An imported project has an `explore` with the same name as an existing `explore` in the importing project. 
  * An included model file has an `explore` with the same name as an existing `explore` in the including project model file.*****
  * There is a circular reference in the code, referencing the `explore` (or model file) multiple times. 

*****_It is not best practice to include model files in other model files._ | 

  * [`explore` parameter reference](/looker/docs/reference/param-explore-explore)
  * [Including models in a model](/looker/docs/reference/param-model-include#including_models_in_a_model)

  
`Unknown view '(?)' --> Did you '- include: (?)' in (?).model.lookml?` |  IDE | 

  * A model is including the view folder, but the specific view file is outside the folder. 
  * A model is including the name of the view, but not the view file, if named differently. 
  * A view is joined into an `explore` multiple times, but is missing the `from` parameter the second time it is joined. 

| 

  * [Using `include` with IDE folders](/looker/docs/ide-folders#using_include_with_ide_folders)
  * [`include` parameter reference](/looker/docs/reference/param-model-include)
  * [You can join the same table more than once using `from`](/looker/docs/reference/param-explore-join#you_can_join_the_same_table_more_than_once_using_from)

  
`Unknown field '(?)'` |  IDE Ex | 

  * The field you are trying to reference does not exist, has been misspelled, or has been commented out. 
  * A referenced field is defined in a different view, and is not scoped with its view name. 
  * A field is defined in a different view that is not joined into the necessary Explores, or the view is aliased in a join, making the field inaccessible by some Explores. 
  * A `required_fields` parameter references a field that is inaccessible, is misspelled, doesn't exist, or is commented out. 

| 

  * [Error: Unknown or inaccessible field (Best Practices page)](/looker/docs/best-practices/error-unknown-or-inaccessible-field)
  * [`from` (for Explores)](/looker/docs/reference/param-explore-from)
  * [`from` (for joins)](/looker/docs/reference/param-explore-join-from)
  * [`required_fields` parameter reference](/looker/docs/reference/param-field-required-fields)

  
`Cannot use (?) as access filter since any user can edit their own value.` |  Ex |  A user attribute with the **User Access** option set to **Edit** is used in an Explore's `access_filter` parameter.  | 

  * [Creating user attributes](/looker/docs/admin-panel-users-user-attributes#creating_user_attributes)
  * [Using user attributes in access filters](/looker/docs/admin-panel-users-user-attributes#access_filters)
  * [`access_filter` parameter reference](/looker/docs/reference/param-explore-access-filter)

  
`label_from_parameter of (?) must refer to a parameter.` |  IDE Ex | 

  * A field referenced by a `label_from_parameter` parameter doesn't exist, is misspelled, or is commented out. 
  * A field referenced by a `label_from_parameter` parameter exists, but is not a `parameter` type. 

| 

  * [`label_from_parameter` parameter reference](/looker/docs/reference/param-field-label-from-parameter)
  * [`parameter` parameter reference](/looker/docs/reference/param-field-parameter)

  
`Cannot use user-editable attribute (?) for access_grant (?)` |  IDE Ex |  A user attribute with the **User Access** option set to **Edit** is used in a model file's `access_grant` parameter.  | 

  * [Creating user attributes](/looker/docs/admin-panel-users-user-attributes#creating_user_attributes)
  * [Controlling access with access grants](/looker/docs/admin-panel-users-user-attributes#controlling_access_with_access_grants)
  * [`access_grant` parameter reference](/looker/docs/reference/param-model-access-grant)

  
`datagroup (?) has a sql_trigger. This is not allowed in models with a parameterized connection.` |  IDE |  A database connection is using user attributes for database login credentials, and the **PDT overrides** column is not configured for a separate database user for PDT processes.  | 

  * [Using user attributes in database connections](/looker/docs/admin-panel-users-user-attributes#database_connections)
  * [Configuring separate login credentials for PDT processes](/looker/docs/connecting-to-your-db#pdt-overrides)
  * [`datagroup` and `sql_trigger` parameter reference](/looker/docs/reference/param-model-datagroup#sql_trigger)

  
`relationship missing, assumed to be many_to_one.` |  IDE |  A join's `relationship` is not defined. When a `relationship` is not specified, Looker assumes a `many-to-one` relationship by default.  |  [`relationship` parameter reference](/looker/docs/reference/param-explore-join-relationship)  
`No distribution_style specified in persistent derived table (?). Using default distribution style (?).` |  IDE |  A Redshift connection PDT doesn't have a `distribution_style` parameter specified in its `derived_table` definition. When there isn't a `distribution_style` specified, Looker defaults to `ALL`.  |  [`distribution_style` parameter reference](/looker/docs/reference/param-view-distribution-style)  
`always_filter: unknown filter field '(?)'` |  IDE | 

  * A field referenced by an `always_filter` parameter does not exist, is misspelled, or is commented out. 
  * A field referenced by an `always_filter` parameter is a `dimension_group` of `type: time` that does not have a timeframe appended. 
  * A field referenced by an `always_filter` parameter is a field that is defined in a view that is not joined into all relevant `explore` parameters, or the field is not scoped with its view name. 

| 

  * [Error: Unknown or inaccessible field (Best Practices page)](/looker/docs/best-practices/error-unknown-or-inaccessible-field)
  * [Dimension groups must be referenced by their individual dimensions](/looker/docs/reference/param-field-dimension-group#dimension_groups_must_be_referenced_by_their_individual_dimensions)
  * [`always_filter` parameter reference](/looker/docs/reference/param-explore-always-filter)

  
`The location field type requires both sql_latitude and sql_longitude.` |  IDE |  A field of `type: location` is missing either the `sql_latitude` or the `sql_longitude` subparameter. Location type fields require both.  |  [`location` field type reference](/looker/docs/reference/param-dimension-filter-parameter-types#location)  
`Missing required sql_step in create_process of derived table '(?)'.` |  IDE | 

  * There is no `sql_step` specified in the `create_process`, which requires one or more `sql_step` subparameters. 
  * A cached LookML validator error flagged a missing `sql_step` even though a `sql_step` was already added. Validate once more to resolve the error. 

|  [`create_process` parameter reference](/looker/docs/reference/param-view-create-process)  
`Can't construct aggregate table (?), temporary schema for (?) is unset.` |  IDE Ex |  The **Persistent Derived Tables** setting is not set for the connection on the **Connection Settings** page in the **Admin** panel, and/or there is no temp database schema specified in the **Temp Database** setting.  | 

  * [Persistent Derived Tables connection setting reference](/looker/docs/connecting-to-your-db#persistent_derived_tables)
  * [Temp Database connection setting reference](/looker/docs/connecting-to-your-db#temp_database)

  
`Can't construct aggregate table (?), connection (?) could not be registered.` |  IDE Ex |  The **Temp Database** setting is not set on the connection's **Connection Settings** page in the **Admin** panel, or Looker does not have the appropriate permissions to the temp database specified in the **Temp Database** setting.  | 

  * [Aggregate tables must be persisted](/looker/docs/aggregate_awareness#aggregate_tables_must_be_persisted)
  * [Temp Database connection setting reference](/looker/docs/connecting-to-your-db#temp_database)

  
`Unknown view (?) referenced by explore (?)` |  IDE | 

  * A view is included using the default `include: "*.view.lkml"`, but the view is in a different folder. 
  * A view name or file path is misspelled in an `include` statement, or the `include` statement is including the name of the view, but not the view file, if named differently. 
  * There is an issue with special characters, such as `_views`, in a folder. 
  * An `explore` is extending another `explore` that is missing a `view_name` parameter that specifies the base view. 

| 

  * [`include` parameter reference](/looker/docs/reference/param-model-include)
  * [Using `include` with IDE folders](/looker/docs/ide-folders#using_include_with_ide_folders)
  * [`extends` (for Explores)](/looker/docs/reference/param-explore-extends#definition)
  * [`view_name` parameter reference](/looker/docs/reference/param-explore-view-name)

  
`The location field type does not use the sql parameter. Please use sql_latitude and sql_longitude instead.` |  IDE |  A `sql` parameter is used in a field of `type: location`. Location type fields require `sql_latitude` and `sql_longitude` subparameters instead of the `sql` parameter.  |  [`location` field type reference](/looker/docs/reference/param-dimension-filter-parameter-types#location)  
`A list_field must be defined for measures of type list.` |  IDE Ex |  To generate a list from a field, the field must be specified for a measure of `type: list`.  |  [`list` field type reference](/looker/docs/reference/param-measure-types#list)  
`Query failed with unexpected exception (?)` |  IDE Ex SQL LD D S | 

  * A database other than the main connection database is specified in the **PDT Overrides** column on a connection's **Connection Settings** page in the **Admin** panel. 
  * The per-user query limit has been exceeded and a queued query has hit the connection pool timeout. 
  * A JDBC connection has failed. 
  * An unexpected Looker application failure has occurred. 

| 

  * [Configuring separate login credentials for PDT processes](/looker/docs/connecting-to-your-db#pdt-overrides)
  * [Connection Pool Timeout](/looker/docs/connecting-to-your-db#connection_pool_timeout)
  * [Looker startup options](/looker/docs/startup-options)
  * [Query timeouts and queueing](/looker/docs/admin-panel-database-queries#query_timeouts_and_queueing)
  * [Connection settings additional params (including JDBC parameters)](/looker/docs/connecting-to-your-db#additional_params)

  
`Looker is having trouble connecting to your database.` |  Ex SQL |  A connection's max connection pool limit has been reached, and queued queries have timed out after the connection pool timeout window has elapsed.  | 

  * [What does the "Looker is having trouble connecting to your database" error mean? (Community post)](https://www.googlecloudcommunity.com/gc/Administering-Looker/What-does-the-quot-Looker-is-having-trouble-connecting-to-your/td-p/591967)
  * [ Max Connections connection setting reference](/looker/docs/connecting-to-your-db#max_connections)
  * [Connection Pool connection setting reference](/looker/docs/connecting-to-your-db#connection_pool_timeout)

  
`SQL Error in incremental PDT: Query execution failed` |  Ex D S |  The underlying schema has changed for one or more tables that were referenced in an SQL-based incremental PDT.  |  [Incremental PDT fails to build after schema change](/looker/docs/incremental-pdts#schema-change)  
`Missing dates/values for '(?)' were not filled.` |  Ex | 

  * Dimension fill cannot be applied because more than one dimension was selected in an Explore. 
  * Dimension fill cannot be applied because one or more fields were pivoted in an Explore. 
  * Dimension fill cannot be applied because a field has distinct string values (for example, `allowed_value` or `case` parameters), and there is a filter applied to that field. 

|  [Filling in missing dates and values](/looker/docs/creating-visualizations#filling_in_missing_dates_and_values)  
`filters: ` is not supported for measures of non-aggregate type '(?)'` |  IDE Ex |  A `filters` parameter was used with any measure type other than the following: `count`, `sum`, `average`, and `count_distinct`.  | 

  * [`filters` parameter reference](/looker/docs/reference/param-field-filters)
  * [Creating a dynamic filtered measure](/looker/docs/reference/param-field-filters#creating_a_dynamic_filtered_measure)

  
`Unknown source explore (?) in lookml test (?) declaration.` |  IDE | 

  * A misspelled, nonexistent, or commented-out Explore name is used in a data test's `explore_source` subparameter. 
  * A data test is defined in a file that does not include or is not included in the file that contains the Explore's `explore_source` definition. 
  * An Explore with the `extension: required` parameter specification is used as the `explore_source` of a data test. 

| 

  * [`test` parameter reference](/looker/docs/reference/param-model-test)
  * [`explore_source` (for data tests)](/looker/docs/reference/param-model-test#explore_source)
  * [LookML data tests recommendations and best practices (Community post)](https://www.googlecloudcommunity.com/gc/Administering-Looker/What-does-the-quot-Looker-is-having-trouble-connecting-to-your/td-p/591967)

  
`filter_expression: is not supported for measures of non-aggregate type '(?)'` |  IDE Ex |  A `filters_expression` parameter was used with any measure type other than the following: `count`, `sum`, `average`, or `count_distinct`.  | 

  * [`filter_expression` LookML dashboard query parameter reference (for waterfall chart)](/looker/docs/reference/param-lookml-dashboard-waterfall-chart#filter_expression)
  * [LookML dashboard query parameter reference (for table chart)](/looker/docs/reference/param-lookml-dashboard-table-chart#filter_expression)

  
`Field references an aggregate but is specified as a dimension. If you want to use aggregations such as sum, average, count, use a measure type instead.` |  IDE Ex |  A dimension references a measure or another aggregation in its `sql` parameter  | 

  * [Dimension and measure fields ](/data-modeling/learning-lookml/lookml-terms-and-concepts#dimension_and_measure_fields)
  * [`sql` (for dimensions) ](/reference/field-params/sql#sql_for_dimensions)

  
`Cannot specify both sql_table_name and derived_table for view (?)` |  IDE |  A view has both `sql_table_name` and `derived_table` parameters defined. A view can only reference one table — either an existing schema in the database connection with `sql_table_name`, or a new table with `derived_table`.  | 

  * [`view` parameter reference](/looker/docs/reference/param-view-view)
[`sql_table_name` (for views)](/looker/docs/reference/param-view-sql-table-name)
  * [`derived_table` parameter reference](/looker/docs/reference/param-view-derived-table)

  
`Persistent Native Derived Table for view (?) has an explore source (?) that has access filters. Persisting this table may result in unexpected behavior.` |  IDE |  A persisted NDT is based on an Explore with an `access_filter` parameter that references user attributes.  | 

  * [Things to consider when deciding whether to persist a derived table](/looker/docs/derived-tables#things_to_consider_when_deciding_whether_or_not_to_persist_a_derived_table)
  * [`access_filter` parameter reference](/looker/docs/reference/param-explore-access-filter)

  
`Unknown or unexpected parameter "(?)" in (?).` |  IDE | 

  * A `distribution_style` parameter is used for a dialect that does not support that parameter 
  * A `cluster_keys` parameter is used for a dialect that does not support that parameter 
  * A `sql_always_where` parameter is defined in a `join` instead of an `explore`. 
  * Timeframes defined in a `dimension_group` are not of `type: time`. 
  * A `sql_distinct_key` parameter is defined in a dimension instead of a measure. 

| 

  * [Dialect support for `distribution_style`](/looker/docs/reference/param-view-distribution-style#dialect_support_for_distribution_style)
  * [Dialect support for `cluster_keys`](/looker/docs/reference/param-view-cluster-keys#dialect_support_for_cluster_keys)
  * [`dimension_group` field type reference](/looker/docs/reference/param-field-dimension-group)
  * [`sql_distinct_key` parameter reference](/looker/docs/reference/param-field-sql-distinct-key)

  
`Could not find the constant` |  IDE |  A constant is referenced from an imported project in an importing project, and is only defined in the imported project. Constants can only be referenced in the projects in which they are defined. The constant needs to be redefined in the manifest file.  |  [Using constants in files from an imported project](/looker/docs/importing-projects#using_constants_in_files_from_an_imported_project)  
`Multiple primary key definitions for view '(?)': '(?)' and '(?)'` |  IDE |  More than one primary key exists in a view file. Either more than one dimension is specified as a primary key with `primary_key: yes`, or an extending view specifies a new dimension as a primary key with `primary_key: yes`.  | 

  * [`primary_key` parameter reference](/looker/docs/reference/param-field-primary-key)
  * [`extends` (for views)](/looker/docs/reference/param-view-extends)
  * [Reusing code with extends](/looker/docs/reusing-code-with-extends)

  
`Persistent Native Derived Table for view (?) references user attributes. Persisting this table may result in unexpected behavior.` |  IDE |  A persisted NDT or an aggregate awareness table is based on an `explore` with an `access_filter` or `sql_always_where` parameter referencing user attributes.  | 

  * [Things to consider when deciding whether to persist a derived table](/looker/docs/derived-tables#things_to_consider_when_deciding_whether_or_not_to_persist_a_derived_table)
  * [`access_filter` parameter reference](/looker/docs/reference/param-explore-access-filter)
  * [`sql_always_where` parameter reference](/looker/docs/reference/param-explore-sql-always-where)
  * [Creating native derived tables](/looker/docs/creating-ndts)
  * [Aggregate awareness](/looker/docs/aggregate_awareness)

  
`No map layer named (?) is defined. Must be one of countries, uk_postcode_areas, us_counties_fips, us_states, us_zipcode_tabulation_areas` |  IDE |  A dimension references a map layer with `map_layer_name` when there is no map layer defined in all models in which the field's view is included. For example, a view is included in multiple models, but the map layer is defined in only one model.  | 

  * [`map_layer` parameter reference](/looker/docs/reference/param-model-map-layer)
  * [Built-in map layers for `map_layer_name`](/looker/docs/reference/param-field-map-layer-name#built-in_map_layers)

  
`Persistent derived table (?) should include at least one index` |  IDE |  A PDT or an aggregate table definition includes an `index` in which a PDT or an aggregate table column has not been specified.  | 

  * [`indexes` parameter reference](/looker/docs/reference/param-view-indexes)
  * [Persistent derived tables reference](/looker/docs/derived-tables#persistent-derived-tables)
  * [`aggregate_table` parameter reference](/looker/docs/reference/param-explore-aggregate-table)

  
`The x database encountered an error while running this query.` |  Ex SQL |  The database cannot locate a column that is referenced by a field's [`sql` parameter](/looker/docs/reference/param-field-sql). This can be caused by one of the following conditions: 

  * There is a typo in the table or column name that is referenced in a `sql` parameter. 
  * The underlying data in the database, for example, a column name, has changed. 

|  [Common SQL error troubleshooting tips in Looker (Community post)](https://www.googlecloudcommunity.com/gc/Technical-Tips-Tricks/Common-SQL-error-troubleshooting-tips-in-Looker/ta-p/586852)  
`Render job (?) failed [orphaned job]` |  S |  The Looker instance was unavailable during the time that the scheduled job ran. This can happen during version updates and scheduled maintenance.  |  [Google maintenance policy for Looker-hosted services](/looker/docs/google-maintenance-policy-for-looker-hosted-services)