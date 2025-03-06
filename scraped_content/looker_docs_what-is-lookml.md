# https://cloud.google.com/looker/docs/what-is-lookml

Depth: 3

LookML, short for _Looker Modeling Language_ , is the language that is used in Looker to create semantic data models. You can use LookML to describe dimensions, aggregates, calculations, and data relationships in your SQL database. Looker uses a model that is written in LookML to construct SQL queries against a particular database.

LookML is a dependency language like _make_ , as opposed to an imperative language like C or Ruby. LookML provides predefined data types and syntax for data modeling. You don't need prior experience with programming languages to understand LookML. LookML is independent of particular SQL dialects, and it encapsulates SQL expressions to support any SQL implementation.

For data analysts, LookML fosters DRY style ("don't repeat yourself"), meaning you write SQL expressions _once, in one place,_ and Looker uses the code repeatedly to generate ad hoc SQL queries. Business users can then use the results to build complex queries in Looker, focusing only on the content they need, not the complexities of SQL structure.

## LookML projects

LookML is defined in _projects_. A LookML project is a collection of files including at least model and view files, and optionally [other types of files](/looker/docs/lookml-project-files), that are typically version-controlled together through a Git repository. The model files contain information about which tables the project will use and how the tables should be joined. The view files describe how information is calculated about each table (or across multiple tables if the joins permit this).

LookML separates structure from content, so the query structure (how tables are joined) is independent of the query content (the columns to access, derived fields, aggregate functions to compute, and filtering expressions to apply).

![](/static/looker/docs/images/dev-looker-query-flow-2110.png)

Looker queries are based on LookML project files. Data analysts use LookML to create and maintain data models that define the data structure and business rules for the data that is being analyzed. The Looker SQL generator translates LookML into SQL, which lets business users query without writing any LookML or SQL.

Business users use the Looker query builder, or the [Explore interface](/looker/docs/creating-and-editing-explores), to create queries that are based on the data model that Looker analysts define. Users can select dimensions, measures, and filters to create custom queries that are based on their own questions and to generate their own insights.

When a user creates a query, it is sent to the Looker SQL generator, which translates the query into SQL. The SQL query is executed against the database, and then Looker returns the formatted results to the user in the Explore interface. The user can then visualize the results and generate insights.

For more details on the fundamental LookML elements in a project and how they relate to one another, see [LookML terms and concepts](/looker/docs/lookml-terms-and-concepts).

## What users see

How the project is set up, and the specific contents of its files, determines what users see and how they can interact with Looker.

![](/static/looker/docs/images/explore-page-all-1-2300.png)

  1. The Explore panel in the [left navigation panel](/looker/docs/finding-content) is organized by [model](/looker/docs/lookml-terms-and-concepts#model) names. Under each model name is a list of available [Explores](/looker/docs/lookml-terms-and-concepts#explore) that are defined in that model.
  2. Users can search for a specific Explore.
  3. Developers can define descriptions for Explores, which users can view by hovering over the Explore name in the **Explore** menu.

![](/static/looker/docs/images/explore-page-all-2-2400.png)

  4. The [field picker](/looker/docs/changing-explore-menu-and-field-picker#field_picker) pane is organized by [view](/looker/docs/lookml-terms-and-concepts#view) names. Under each view name is a list of available fields from the tables included in that view. Most views show both [dimensions](/looker/docs/reference/param-dimension-filter-parameter-types) and [measures](/looker/docs/reference/param-measure-types). This example selects a **Month** dimension from within a **Returned Date** dimension group, which was defined in the view file.

  5. Users can select multiple measures on which to base the query.

  6. Users can apply options like filters and pivots in the field picker pane.

  7. Users can refine the terms of the query.

  8. Users can choose a [visualization type](/looker/docs/visualization-types) to apply to the query results.

  9. Running this Explore generates a SQL query that returns both a data table and a visualization of the total sale price and total gross margin of the returned orders from the past year.

## Code sample

The following code example shows a minimal LookML project for an e-commerce store, which has a model file — `ecommercestore.model.lkml` — and two view files — `orders.view.lkml` and `customers.view.lkml`:
    
    
    ######################################
    # FILE: ecommercestore.model.lkml    #
    # Define the explores and join logic #
    ######################################
    connection: order_database
    include: "*.view.lkml"
    explore: orders {
      join: customers {
        sql_on: ${orders.customer_id} = ${customers.id} ;;
      }
    }
    
    ##########################################################
    # FILE: orders.view.lkml                                 #
    # Define the dimensions and measures for the ORDERS view #
    ##########################################################
    view: orders {
      dimension: id {
        primary_key: yes
        type: number
        sql: ${TABLE}.id ;;
      }
      dimension: customer_id {      # field: orders.customer_id
        sql: ${TABLE}.customer_id ;;
      }
      dimension: amount {           # field: orders.amount
        type: number
        value_format: "0.00"
        sql: ${TABLE}.amount ;;
      }
      dimension_group: created {                # generates fields:
        type: time                              # orders.created_time, orders.created_date
        timeframes: [time, date, week, month]   # orders.created_week, orders.created_month
        sql: ${TABLE}.created_at ;;
      }
      measure: count {             # field: orders.count
        type: count                # creates a sql COUNT(*)
        drill_fields: [drill_set*] # list of fields to show when someone clicks 'ORDERS Count'
      }
      measure: total_amount {
        type: sum
        sql: ${amount} ;;
      }
      set: drill_set {
        fields: [id, created_time, customers.name, amount]
      }
    }
    
    #############################################################
    # FILE: customers.view.lkml                                 #
    # Define the dimensions and measures for the CUSTOMERS view #
    #############################################################
    view: customers {
      dimension: id {
        primary_key: yes
        type: number
        sql: ${TABLE}.id ;;
      }
      dimension: city {                    # field: customers.city
        sql: ${TABLE}.city ;;
      }
      dimension: state {                   # field: customers.state
        sql: ${TABLE}.state ;;
      }
      dimension: name {
        sql: CONCAT(${TABLE}.firstname, " ", ${TABLE}.lastname) ;;
      }
      measure: count {             # field: customers.count
        type: count                # creates a sql COUNT(*)
        drill_fields: [drill_set*] # fields to show when someone clicks 'CUSTOMERS Count'
      }
      set: drill_set {                     # set: customers.drill_set
        fields: [id, state, orders.count]  # list of fields to show when someone clicks 'CUSTOMERS Count'
      }
    }
    

## Additional resources

If you are new to LookML development, consider using the resources described in the following sections to accelerate your learning:

  * Get access to Looker's learning environment
  * Learn how to use Looker to query and explore data
  * Review SQL basics before diving into LookML
  * Learn LookML fundamentals

### Get access to Looker's learning environment

Check out the courses on [Google Cloud Skills Boost](https://www.cloudskillsboost.google/paths/28).

### Learn how to use Looker to query and explore data

Knowing how to explore data in Looker will help you a great deal when you're modeling your data in LookML. If you're not familiar with using Looker to query, filter, and drill into data, we suggest the following resources:

  * Start with the [Retrieve and chart data](/looker/docs/retrieve-and-chart-data) tutorials. The links at the bottom of each page will guide you through a sequence of the most important Looker features.
  * [The Analyzing and Visualizing Data in Looker skills boost quest](https://www.cloudskillsboost.google/paths/28/course_templates/323) will take you through the basics of exploring.

### Review SQL basics before diving into LookML

Writing LookML requires an understanding of SQL queries. You don't have to be a SQL expert, and even beginners can create powerful Looker models. But, in general, the deeper you go in LookML, the more you benefit from a deeper knowledge of SQL.

If you need a SQL refresher, here are some of our favorite resources:

  * [Khan Academy's SQL Lessons](https://www.khanacademy.org/computing/computer-programming/sql) interactive SQL tutorials
  * [SQLZoo](http://sqlzoo.net/wiki/Main_Page) interactive SQL tutorials
  * [Sams Teach Yourself SQL in 10 Minutes](https://www.google.com/search?q=sql+in+10+minutes+sams+teach+yourself) book by Ben Forta

### Learn LookML fundamentals

These resources will jump-start your LookML knowledge. Use your learning account to experiment with different design patterns.

  * Start with [LookML terms and concepts](/looker/docs/lookml-terms-and-concepts).
  * Continue to [How Looker generates SQL](/looker/docs/how-looker-generates-sql) and [Advanced LookML concepts](/looker/docs/additional-lookml-basics).
  * Once you have a good grasp of LookML and SQL, read about our more advanced features like [derived tables](/looker/docs/derived-tables) and [templated filters](/looker/docs/templated-filters).

After you've learned LookML basics, see the following pages for overviews of the different types of LookML parameters:

  * [Model parameters](/looker/docs/reference/param-model)
  * [Explore parameters](/looker/docs/reference/param-explore)
  * [Join parameters](/looker/docs/reference/param-join)
  * [View parameters](/looker/docs/reference/param-view)
  * [Field parameters](/looker/docs/reference/param-field)
  * [Dashboard parameters](/looker/docs/reference/param-lookml-dashboard)