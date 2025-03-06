# https://cloud.google.com/looker/docs/additional-lookml-basics

Depth: 3

This page describes the following common patterns in LookML:

  * Labeling fields (and names in the UI)
  * Filtering counts by a dimension
  * Percentages
  * Using sets for drill-down details
  * Filtering result sets

## Labeling fields (and names in the UI)

Looker converts LookML field names into the strings that the UI displays by combining the view name in regular-weight font with the field's short name in bold. For example, a field called **Amount** in the **Orders** view would appear in the UI as Orders **Amount**. On this page, both field names are bolded and the view name is capitalized (**ORDERS Amount**) to make the discussion clearer.

If you want a field to have a different name than its column name in a table, change the field name and use the `sql` parameter to link the field to the appropriate column in the table. In the following example, the `airports` table has a `cntrl_twr` column. Looker would generate the following declaration:
    
    
    view: airports {
      dimension: cntrl_twr {        # full name: airports.cntrl_twr
        type: yesno                 # default name: AIRPORT Cntrl Twr (Yes/No)
        sql: ${TABLE}.cntrl_twr ;;  # the sql expression for this field
      }
    }
    

You can rename the `cntrl_twr` dimension to be human-readable:
    
    
    view: airports {
      dimension: has_control_tower {  # full name: airports.has_control_tower
        type: yesno                   # aliased name: AIRPORTS Has Control Tower (Yes/No)
        sql: ${TABLE}.cntrl_twr ;;    # the sql expression for this field
      }
    }
    

## Filtering counts by a dimension

You can group by a dimension and count entities — grouping by **USERS Country** , **ORDERS Count** will tell you where your orders are coming from by country. However, it is often useful to build a count that is filtered by some dimensional value. For example, you could make a new measure and name it **ORDERS France Count** :
    
    
    view: users {
      dimension: country {}
    }
    view: orders {
      dimension: id {
        primary_key: yes
        sql: ${TABLE}.id ;;
      }
      measure: count {
        type: count
        drill_fields: [detail]
      }
      measure: france_count {
        type: count   # COUNT(CASE WHEN users.country = 'France' THEN 1 ELSE NULL END)
        filters: [users.country: "France"]
      }
    }
    

Filters can use any expression. If you wanted a field that counted users from the EU, you could use something like this:
    
    
    measure: eu_count {
      type: count   # COUNT(CASE WHEN users.countrycode IN 'UK','FR','ES' THEN 1 ELSE NULL END)
      drill_fields: [detail]
      filters: [users.countrycode: "UK,FR,ES"]
    }
    

If you want to [filter with a mathematical expression](/looker/docs/functions-and-operators#math), be sure to enclose it in double quotes:
    
    
    measure: total_orders_above_100_dollars {
      type: sum   # SUM(CASE WHEN order.value > 100 THEN order.value ELSE NULL END)
      sql: ${order.value} ;;
      drill_fields: [detail]
      filters: [order.value: ">100"]
    }
    

## Percentages

Many key performance indicators are expressed in the form of percentages, such as "the percent of items returned," "the percent of emails that resulted in a sale," or other instances of "the percent of X that Y." In LookML, the design pattern is to create counts for the two conditions and create a third field that computes the percentage between the two.
    
    
    dimension: returned {
      type: yesno
    }
    measure: count {   # total count of items
      type: count_distinct
      sql: ${TABLE}.id ;;
      drill_fields: [detail]
    }
    measure: returned_count {   # count of returned items
      type: count_distinct
      sql: ${TABLE}.id ;;
      drill_fields: [detail]
      filters: [returned: "Yes"]
    }
    measure: percent_returned {
      type: number
      sql: 100.0 * ${returned_count} / NULLIF(${count}, 0) ;;
      value_format: "0.00"
    }
    

Use the following format to compute percentages. In Postgres, counts are integers, and division between integers results in integers. Multiplying by 100.0 converts the first count to a floating point number, thus converting the rest of the expression to a float. To avoid divide-by-zero errors, the `NULLIF(value, 0)` converts a zero value to null, which makes the result null and avoids an error.
    
    
    100.0 * ${returned_count} / NULLIF(${count}, 0)
    

## Using sets for drill-down details

One of the most powerful features of Looker is the ability to drill into data to see the underlying entities that make up a count or other measure.

When you click a measure in the UI, Looker creates a new query to localize the set of data that makes up the measure. Each value for each dimension on the row in the table gets added to

To show the detail, Looker needs a specified list of drill fields to show when the measure's value has been clicked. When you [generate a model](/looker/docs/generating-a-model), the generator typically creates some initial drill fields for you. In addition, you can add drill fields yourself. For example, assume that you are measuring **ORDERS Count** by **USERS State** in the last week. In Looker, the query would look something like the following:

USERS State| ORDERS Count  
---|---  
California| 24  
Texas| 5  
Colorado| 4  
Florida| 4  
Illinois| 4  
  
If you click **24** in the **California** row, you might expect to see the 24 orders that came from California. Although Looker does add the filter **USERS State: California** , Looker doesn't know which fields you want to show in the order. You would first need to use a set to declare those fields in your model.

In LookML, a **set** is a list of field (dimension, measure, and [filter](/looker/docs/reference/param-field-filter)) names. You use sets to give Looker the following information:

  * The fields that you want to show when drilling into a count or another measure
  * The fields that you want to import when you join a view
  * The fields that you want to be indexed in an Explore

Because the same set can be used in many places in a model, Looker provides several methods for creating sets.

### Literal sets

A literal set is a straightforward way to define a set in LookML, particularly when the set is used only once. A literal set is created by declaring the set as an array. You can declare literal sets by using `[]`.

Consider the following example:
    
    
    view: customers {
      dimension: id {
        primary_key: yes
      }
      measure: count {
        type: count
      }
      dimension: city {}
      dimension: state {}
      dimension: name {}
    }
    

In this example, the fields that you want to show are `id`, `name`, and `city`.

In the measure, you can declare a literal array as follows:
    
    
    measure: count {
      type: count
      drill_fields: [id, name, city]
    }
    

### Named sets

Suppose that two counts are defined in the `customers` view: `count` and `in_california_count`. When a user drills into either the **Count** field or the **In California Count** field in an Explore, you want to display the fields `id`, `name`, and `city`.

Initially, declaring these fields literally might seem sufficient:
    
    
    view: customers {
      measure: count {
        type: count
        drill_fields: [id, name, city]
      }
      measure: in_california_count {
        type: count
        filters: [state: "California"]
        drill_fields: [id, name, city]
      }
    }
    

However, if you wanted to add a new field (such as `customers.state`), you would have to edit both lists, unless you used the [`set` parameter](/looker/docs/reference/param-view-set) to create named sets that you can maintain in one place and use in multiple places.

The following code creates a set `customers.detail` and points both counts to the same set of fields.
    
    
    view: customers {
      set: detail {
        fields: [id, name, city]      # creates named set customers.detail
      }
    
      measure: count {
        type: count
        drill_fields: [detail*]       # show fields in the set "customers.detail"
      }
      measure: in_california_count {
        type: count
        filters: [state: "California"]
        drill_fields: [detail*]      # show fields in the set "customers.detail"
      }
    }
    

LookML sets are powerful in the following ways:

  * Redeclaration of sets is additive. If you declare a set in multiple places, then Looker includes all the fields that were declared for the set in all locations.
  * You can embed sets within other sets by typing the name of the other set followed by an asterisk, for example, `setname*`.
  * You can remove elements from sets by placing a hyphen before the field name, for example, `-fieldname`.

### Customizing drill visualizations

If your Looker admin has enabled the [**Visual Drilling**](/looker/docs/admin-panel-general-labs#visual_drilling) Labs feature, Look and Explore drill visualizations won't always default to a data table. In this case, you can customize the visualization that is displayed by using Liquid variables in the `link` parameter, as shown on the [`link`](/looker/docs/reference/param-field-link#using_link_to_customize_drill_visualizations) parameter documentation page and on the [More powerful data drilling](/looker/docs/best-practices/how-to-use-more-powerful-data-drilling) Best Practices page.

[Dashboards](/looker/docs/viewing-dashboards) support visual drilling using the `link` parameter without the need to enable the **Visual Drilling** Labs feature.

## Filtering result sets

LookML provides a set of filter operations that can be applied to fields and Explores to filter result sets before they are returned to the user.

### `always_filter` on the Explore

Use [`always_filter`](/looker/docs/reference/param-explore-always-filter) to always apply a set of filters to any query that is run within an Explore. The filters will appear in the Looker UI and, although users can change the default filter value that you provide, they cannot remove the filters. Generally, these filters are used to remove data that you normally don't want to include. For example, suppose that in the **Orders** Explore, you only wanted to see orders that were complete or pending. You could add the following LookML code:
    
    
    explore: orders {
      view_name: order
        filters: [status: "complete,pending"]
      }
    }
    

If the user wanted to see orders with other status values, they could set **ORDERS Status** to **%** in the UI.

### `sql_always_where` on the Explore

If you want to apply a query restriction that users cannot change, you can use [`sql_always_where`](/looker/docs/reference/param-explore-sql-always-where). In addition to queries run by human users, the restriction will apply to dashboards, scheduled Looks, and embedded information that relies on that Explore. A `sql_always_where` condition is not displayed to the user, unless they look at the underlying SQL of any queries that they create.

The following example prevents users from looking at orders before 2012-01-01:
    
    
    # Using Looker references
    explore: order {
      sql_always_where: ${created_date} >= '2012-01-01' ;;
    }
    
    # Using raw SQL
    explore: order {
      sql_always_where: DATE(created_time) >= '2012-01-01' ;;
    }
    

### `conditionally_filter` on the Explore

Very large tables require some thought when querying, since unlimited queries can quickly become too burdensome on the database. LookML provides a way to address this in the form of [`conditionally_filter`](/looker/docs/reference/param-explore-conditionally-filter).

You use the `conditionally_filter` parameter to apply a filter to the query unless the user has already added a filter for one of the fields listed in the `unless` section.

The following example won't make any change to the user's query if the user applied a filter on one or more of these fields: `created_date`, `shipped_time`, `shipped_date`, `orders.id`, or `customer.name`. If the user didn't filter on any of those fields, Looker will automatically add a filter of 1 day on `orders.created_time`.
    
    
      filters: [orders.created_time: "1 day"]
      unless: [created_date, shipped_time, shipped_date, orders.id, customer.name]
    }