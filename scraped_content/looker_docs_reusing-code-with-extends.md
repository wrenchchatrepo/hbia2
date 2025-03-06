# https://cloud.google.com/looker/docs/reusing-code-with-extends

Depth: 3

> This is an advanced topic that assumes that the reader has a solid knowledge of LookML.  
  
## Overview

As your LookML model expands in size and complexity, it becomes increasingly useful to reuse your LookML in multiple places. The `extends` parameter lets you reuse code, which helps you to do the following:

  * Write DRY (don't repeat yourself) code, so that you can define things in just one place, making your code more consistent and faster to edit
  * Manage different field sets for different users
  * Share design patterns in different parts of your project
  * Reuse sets of joins, dimensions, or measures across a project

To extend a LookML object, you create a new LookML object and then add the `extends` parameter to indicate that the new object is an extension of an existing object. This means that your project will have two versions of the LookML object. If there are any conflicts, the extending object will take precedence and override the settings of the object that is being extended. See the Implementation details for `extends` section later on this page for details.

> **Check out LookML refinements:** Extending a view or an Explore is ideal for scenarios where you want to have multiple versions of the view or Explore. But if your goal is simply to modify a view or an Explore without editing the LookML file that contains it, you may want to use a refinement instead. You can also use an [`extends` parameter inside a refinement](/looker/docs/lookml-refinements#refinements_can_contain_extends). See the [LookML refinements](/looker/docs/lookml-refinements) documentation page for more information and use cases.

You can extend views, Explores, and LookML dashboards: 

  * [`extends` for views](/looker/docs/reference/param-view-extends)
  * [`extends` for Explores](/looker/docs/reference/param-explore-extends)
  * [`extends` for LookML dashboards](/looker/docs/reference/param-lookml-dashboard#extends)

> Models cannot be extended, and you cannot include a model file in another model file. Instead, if you want to reuse or extend Explores across models, you can [create a separate Explore file](/looker/docs/other-project-files#creating_an_explore_file) and then [include that Explore file in a model file](/looker/docs/reference/param-model-include#including_explores_in_a_model).

See the following examples of extending an Explore and extending a LookML dashboard.

## Extending an Explore

Here is an example of extending an Explore:
    
    
    explore: customer {
      persist_for: "12 hours"
    }
    
    explore: transaction {
      extends: [customer]
      persist_for: "5 minutes"
    }
    

In this example we have an Explore called **Customer** , and we created a second Explore called **Transaction** that extends it. Everything that is in **Customer** , such as its joins, will be included in **Transaction**. Anything that is in **Transaction** will remain in **Transaction**.

But notice there is a conflict: The **Customer** Explore says the [`persist_for`](/looker/docs/reference/param-explore-persist-for) setting should be 12 hours, but the **Transaction** Explore says it should be 5 minutes. For the **Transaction** Explore, the `persist_for: "5 minutes"` setting will be used, because it overwrites the setting from the Explore it's extending.

## Extending a LookML dashboard

To extend a LookML dashboard, both the extended and extending dashboards must be [included in the model file](/looker/docs/reference/param-model-include#using_include_in_a_model_file). If a dashboard using the `extends` parameter is included in a model file without the base dashboard it extends, you'll get a LookML validation error that the base dashboard can't be found (among other errors).

Here's an example dashboard file:

File: `faa.dashboard.lookml`
    
    
    - dashboard: faa
      title: FAA Dashboard
      layout: newspaper
      elements:
      - title: Aircraft Location
        name: Aircraft Location
        model: e_faa
        explore: aircraft
        type: looker_map
        fields:
        - aircraft.zip
        - aircraft.count
        sorts:
        - aircraft.count desc
        limit: 500
        query_timezone: America/Los_Angeles
        series_types: {}
        row: 0
        col: 0
        width: 8
        height: 6
    

We can create a new LookML dashboard file and extend the **FAA** dashboard by adding a new tile:

File: `faa_additional.dashboard.lookml`
    
    
    - dashboard: faa_additional
      title: FAA Additional
      extends: faa
      elements:
      - title: Elevation Count
        name: Elevation Count
        model: e_faa
        explore: airports
        type: looker_scatter
        fields:
        - airports.elevation
        - airports.count
        sorts:
        - airports.count desc
        limit: 500
        query_timezone: America/Los_Angeles
        row: 0
        col: 8
        width: 8
        height: 6
    
    

Because it extends the **FAA** dashboard, the **FAA Additional** dashboard will include any tiles that are defined in the `faa.dashboard.lookml` file. In addition, the **FAA Additional** dashboard will have any tiles that are defined in its own `faa_additional.dashboard.lookml` file.

The easiest way to create a LookML dashboard is to [get the LookML from a user-defined dashboard](/looker/docs/building-lookml-dashboards#creating_a_lookml_copy_of_a_user-defined_dashboard). You can also use this technique to get the LookML for individual dashboard tiles. If you are using this method, **be very sure that the positions of your tiles don't overlap**. In the `faa.dashboard.lookml` and `faa_additional.dashboard.lookml` examples, the tiles are both on the top row of the dashboard, which is indicated by `row: 0`:

File: `faa.dashboard.lookml`
    
    
        row: 0
        col: 0
        width: 8
        height: 6
    

However, the new tile we're adding in the **FAA Additional** dashboard is in `col: 8` so it's displayed next to the tile from the extended dashboard:

File: `faa_additional.dashboard.lookml`
    
    
        row: 0
        col: 8
        width: 8
        height: 6
    

This is an easy thing to miss, since these elements are in different dashboard files. So if you're adding tiles to an extended dashboard, be sure to check for positioning conflicts between tiles in the extended dashboard and tiles in the extending dashboard.

## Requiring extension

You can use the [`extension: required`](/looker/docs/reference/param-explore-extension) parameter to flag a LookML object as requiring extension, which means that the object cannot be used on its own. An object with `extension: required` is not visible to users on its own; it is intended only to act as a starting point to be extended by another LookML object. The `extension` parameter is supported for [Explores](/looker/docs/reference/param-explore-extension), [views](/looker/docs/reference/param-view-extension), and [LookML dashboards](/looker/docs/reference/param-lookml-dashboard#extension).

An `explore` with `extension: required` cannot be used as an `explore_source` for a [data test](/looker/docs/reference/param-model-test). The [LookML Validator](/looker/docs/lookml-validation#validating_your_changes) will generate an error stating that the `explore_source` cannot be found.

## Using metadata to see extensions for an object

You can click on an `explore` or a `view` parameter in the Looker IDE and use the metadata panel to see any extensions on the object, or to see what object it extends. See the [Metadata for LookML objects](/looker/docs/lookml-metadata#metadata_for_extensions) documentation page for information.

## Implementation details for `extends`

These are the steps that Looker takes when extending a LookML object:

  1. Copy the object that is being extended: Looker makes a copy of the LookML for the view, Explore, or LookML dashboard that is being extended. This new copy is the extend _ing_ object.
  2. Merge the LookML of the two copies: Looker merges the LookML of the extend _ed_ object into the extend _ing_ object.
  3. Resolve conflicts between the copies: For the most part, if a LookML element is defined in both the extend _ed_ object and the extend _ing_ object, the version in the extending object is used. However, in other cases, extensions will combine parameter values instead of overriding the values. See the Combining parameters section on this page for information.
  4. Apply the LookML: Once all conflicts are resolved, Looker interprets the resultant LookML using the standard logic. In other words, Looker will use all the standard defaults and assumptions as with any other view, Explore, or LookML dashboard.

The following sections show the specifics of these steps, extending a view as an example. Here is the LookML for our base view, the **User** view:
    
    
    view: user {
      suggestions: yes
    
      dimension: name {
        sql: ${TABLE}.name ;;
    
      }
      dimension: status {
        sql: ${TABLE}.status ;;
        type: number
      }
    }
    

Here is the LookML for the **User with Age Extensions** view, which extends the **User** view:
    
    
    include: "/views/user.view"
    
    view: user_with_age_extensions {
      extends: [user]
      suggestions: no
    
      dimension: age {
        type: number
        sql: ${TABLE}.age ;;
      }
    
      dimension: status {
        type: string
      }
    }
    

### Step 1: Copy the LookML

In this case, the `user` view is being extended into the `user_with_age_extensions` view. Since `user` is the view that is being extended, a copy of it is made before merging. The fact that a copy is made is not particularly important to know here; the fact that the original `user` view is left unchanged and is usable as normal is important to know.

![](/static/looker/docs/images/extends-step1-copy-2110.png)

### Step 2: Merge the copies

The next step is for all the LookML from the extend _ed_ view (`user`) to be merged into the extend _ing_ view (`user_with_age_extensions`). It's important to understand the nature of this merge, which is simply a merging of LookML objects. In practical terms this means that any explicitly written LookML gets merged, but the default LookML values that you haven't written down _don't_ get merged. In a sense, it's really just the text of the LookML that is getting put together, and none of the meaning of that text.

![](/static/looker/docs/images/extends-step2-merge-2110.png)

### Step 3: Resolve conflicts

The third step is resolving any conflicts between the merged views.

For the most part, if a LookML element is defined in both the extend _ed_ object and the extend _ing_ object, the version in the extending object is used. However, in other cases, extensions will combine parameter values instead of overriding the values. See the Combining parameters section on this page for information.

In the case of the `user_with_age_extensions` example, none of the parameters are additive, and no special list options or `sql` keywords are specified, so the parameter values in the extending view will override parameter values in the extended view:

![](/static/looker/docs/images/extends-step3-resolve-2110.png)

  * The extend _ing_ view name (`user_with_age_extensions`) overrides the extend _ed_ view name (`user`).
  * The extend _ing_ value for `suggestions: no` overrides the extend _ed_ value `suggestions: yes`.
  * The extend _ing_ view has a dimension called `age`, which doesn't exist in the extend _ed_ view (no conflict).
  * The extend _ed_ view has a dimension called `name`, which doesn't exist in the extend _ing_ view (no conflict).
  * The `status` dimension's `type: string` value in the extend _ing_ view overrides the `type: number` value in the extend _ed_ view.
  * The `status` dimension has a `sql` parameter, which doesn't exist in the extend _ing_ view (no conflict).

The fact that default LookML values aren't being considered yet is important, because you don't want to make the mistake of thinking that conflicts between default values are getting resolved. In actuality, they're just being ignored at this step. That is why we need to explicitly add additional parameters when extending objects:

  * When [extending a view](/looker/docs/reference/param-view-extends), we add the [`sql_table_name`](/looker/docs/reference/param-view-sql-table-name) and [`include`](/looker/docs/reference/param-model-include#using_include_in_a_view_file) parameters.
  * When [extending an Explore](/looker/docs/reference/param-explore-extends), we add the [`view_name`](/looker/docs/reference/param-explore-view-name) and [`view_label`](/looker/docs/reference/param-explore-view-label) parameters.

In this particular example we have _not_ added [`sql_table_name`](/looker/docs/reference/param-view-sql-table-name) to the **User** view, which is going to cause some problems in the next step.

### Step 4: Interpret the LookML as normal

In the final step, the resulting LookML is interpreted as normal, including all the default values. In this particular example, the resulting view LookML would be interpreted as follows:
    
    
    include: "/views/user.view"
    
    view: user_with_age_extensions {
      suggestions: no
    
      dimension: age {
        type: number
        sql: ${TABLE}.age ;;
      }
    
      dimension: name {
        sql: ${TABLE}.name ;;
      }
    
      dimension: status {
        sql: ${TABLE}.status ;;
        type: string
      }
    }
    

Notice that the resultant LookML includes `view: user_with_age_extensions`, but no [`sql_table_name`](/looker/docs/reference/param-view-sql-table-name) parameter. As a result, Looker is going to assume that the value of [`sql_table_name`](/looker/docs/reference/param-view-sql-table-name) is equal to the view name.

The problem is that there is probably no table in our database called `user_with_age_extensions`. This is why we need to add a [`sql_table_name`](/looker/docs/reference/param-view-sql-table-name) parameter to any view that is going to be extended. Adding [`view_name`](/looker/docs/reference/param-explore-view-name) and [`view_label`](/looker/docs/reference/param-explore-view-label) to Explores that will be extended avoids similar problems.

![](/static/looker/docs/images/extends-step4-result-2110.png)

## Combining extends

There are a few ways to leverage LookML objects with extends:

  * An object can extend multiple other objects.
  * An extending object can itself be extended.
  * Extends can be used in refinements (see the [LookML refinements](/looker/docs/lookml-refinements#refinements_can_contain_extends) documentation page for more information).

> To see an example of an advanced use case and read troubleshooting tips, see the [Troubleshooting an example of an advanced `extends` use case](/looker/docs/best-practices/how-to-troubleshoot-advanced-extends-use-cases) Best Practices page.

### Extending more than one object at the same time

It is possible to extend more than one dashboard, view, or Explore at the same time. For example:
    
    
    explore: orders {
      extends: [user_info, marketing_info]
    }
    # Also works for dashboards and views
    

The extension process works exactly as described in the implementation example, but there is one extra rule about how conflicts are resolved. If there are any conflicts between the multiple items listed in the `extends` parameter, priority is given to the items listed last. So, in the preceding example, if there were conflicts between `user_info` and `marketing_info`, the `marketing_info` Explore would win.

### Chaining together multiple extends

You can also chain together as many extends as you'd like. For example:
    
    
    explore: orders {
      extends: [user_info]
      ...
    }
    explore: user_info {
      extends: [marketing_info]
      ...
    }
    

Again, the extension process works exactly as described in the implementation example, with one extra rule about conflict resolution. If there are any conflicts, priority is given to the last item in the chain of extends. In this example:

  * `orders` would have priority over both `user_info` and `marketing_info`.
  * `user_info` would have priority over `marketing_info`.

## Combining parameters

For the most part, if a LookML element is defined in both the extend _ed_ object and the extend _ing_ object, the version in the extending object is used. This was the case in the implementation example on this page.

However, in the following cases, extensions will _combine_ parameter values instead of overriding the values:

  * For additive parameters
  * With the `EXTENDED*` list keyword
  * With the `${EXTENDED}` keyword for the `sql` parameter

### Some parameters are additive

In many cases, if the extending object contains the same parameter as the object that is being extended, the extending object's values will override the parameter values of the extended object. But extensions can be _additive_ for some parameters, meaning that the values from the extending object are used in conjunction with the values from the extended object.

The following parameters are _additive_ :

  * For dimensions and measures:

    * [`action`](/looker/docs/reference/param-field-action)
    * [`filters`](/looker/docs/reference/param-field-filters)
    * [`link`](/looker/docs/reference/param-field-link)
  * For parameters:

    * [`allowed_value`](/looker/docs/reference/param-field-parameter#specifying_allowed_values)
  * For derived tables:

    * [`bind_filters`](/looker/docs/reference/param-view-explore-source#bind_filters_example)
    * [`dev_filters`](/looker/docs/reference/param-view-explore-source#dev_filters)
    * [`filters`](/looker/docs/reference/param-view-explore-source#filters)
    * [`sorts`](/looker/docs/reference/param-view-explore-source#sorts)
  * For views:

    * [`extends`](/looker/docs/reference/param-view-extends)
  * For Explores:

    * [`access_filter`](/looker/docs/reference/param-explore-access-filter)
    * [`aggregate_table`](/looker/docs/reference/param-explore-aggregate-table)
    * [`extends`](/looker/docs/reference/param-explore-extends)
    * [`join`](/looker/docs/reference/param-explore-join)
    * [`query`](/looker/docs/reference/param-explore-query)

In the following example, the `carriers` view has a `name` dimension with a `link` parameter:
    
    
    view: carriers {
      sql_table_name: flightstats.carriers ;;
    
      dimension: name {
        sql: ${TABLE}.name ;;
        type: string
        link: {
          label: "Google {{ value }}"
          url: "http://www.google.com/search?q={{ value }}"
          icon_url: "http://google.com/favicon.ico"
        }
      }
    }
    

And here is the `carriers_extended` view, which extends the `carriers` view. The `carriers_extended` view also has a `name` dimension with different settings in the `link` parameter:
    
    
    include: "/views/carriers.view.lkml"
    
    view: carriers_extended {
      extends: [carriers]
    
      dimension: name {
        sql: ${TABLE}.name ;;
        type: string
        link: {
          label: "Dashboard for {{ value }}"
          url: "https://docsexamples.dev.looker.com/dashboards/307?Carrier={{ value }}"
          icon_url: "https://www.looker.com/favicon.ico"
        }
      }
    }
    

In the `carriers_extended` view, the two `link` parameters are additive, so the `name` dimension will display both links.

![](/static/looker/docs/images/dev-refinements-additive-links-2114.png)

### Additional options with lists

When working with lists you may choose to combine them, instead of having the extending object's list be the winner. Consider this simple extension with a conflicting list called `animals`:
    
    
    view: pets {
      extends: fish
      set: animals {
        fields: [dog, cat]
      }
    }
    view: fish {
      set: animals {
        fields: [goldfish, guppy]
      }
    }
    

In this case the `pets` view is doing the extending, and will therefore win, making `animals` contain `[dog, cat]`. However, by making use of the special `EXTENDED*` set, you can combine the lists instead:
    
    
    view: pets {
      extends: fish
      set: animals {
        fields: [dog, cat, EXTENDED*]
      }
    }
    view: fish {
      set: animals {
        fields: [goldfish, guppy]
      }
    }
    

Now the `animals` list will contain `[dog, cat, goldfish, guppy]`.

### Combining instead of replacing during conflict resolution

For the most part, if there are any conflicts during extension, the extending object wins. For example, take this simple extension:
    
    
    view: product_short_descriptions {
      extends: products
      dimension: description {
        sql: ${TABLE}.short_description ;;
      }
    }
    view: products {
      dimension: description {
        sql: ${TABLE}.full_description ;;
      }
    }
    

You can see there is a conflict of the `sql` parameter within the `description` dimension. Typically, the definition from `product_short_descriptions` will simply overwrite the definition from `products` because it is doing the extending.

However, you can also choose to _combine_ the definitions if you like. To do so, you'll use the `${EXTENDED}` keyword like this:
    
    
    view: product_short_descriptions {
      extends: products
      dimension: description {
        sql: LEFT(${EXTENDED}, 50) ;;
      }
    }
    view: products {
      dimension: description {
        sql: ${TABLE}.full_description ;;
      }
    }
    

Now the conflict of the `sql` parameter will be addressed differently. Instead of the `product_short_descriptions` definition winning, it will take the definition from `products` and insert it where `${EXTENDED}` is used. The resulting definition for `description` in this case will be: `LEFT(${TABLE}.full_description, 50)`.

## Things to consider

### Projects with localization

When extending an object, be aware that localization rules apply to your extensions as well. If you are extending an object and then defining new labels or descriptions, you should provide localization definitions in your project's locale strings files. See the [Localizing your LookML model](/looker/docs/model-localization#understanding_how_localization_rules_apply_to_extended_objects) documentation page for more information.