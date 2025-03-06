# https://cloud.google.com/looker/docs/sql-experts-joins

Depth: 3

Just as in SQL, a [join](/looker/docs/working-with-joins) in LookML is used to combine rows from two or more tables, based on a related column between them.

In LookML an [Explore](/looker/docs/creating-and-editing-explores) — as defined by the [`explore`](/looker/docs/reference/param-explore-explore) LookML parameter — is used to define how a user can query the data. An Explore consists of at least one [view](/looker/docs/lookml-terms-and-concepts#view) or a set of views joined together. The main view in the Explore is always included in the query. The joined views are normally only included if they are needed to satisfy the query.

A LookML view corresponds to a SQL table (or another element that has the structure of a table) in the database, or to a [derived table](/looker/docs/derived-tables). The view defines what fields or columns are available in the database, and how they should be accessed.

The following example is a definition for the `orders` Explore.
    
    
    explore: orders {
      join: users {
        type: left_outer
        sql_on: ${orders.user_id} = ${users.id} ;;
        relationship: many_to_one
      }
    }
    

The `orders` view, which is the main view in the Explore, is being joined to the `users` view with a `SQL LEFT OUTER JOIN`, as indicated by the [`type: left_outer`](/looker/docs/reference/param-explore-join-type#left-outer) LookML parameter. The `SQL ON` clause, which is defined by the [`sql_on` LookML parameter](/looker/docs/reference/param-explore-join-sql-on), does not use `table_alias.column` but instead refers `to ${view_name.field_name}`. This is so that if the table name or the column name changes in the database, that change only has to be made in one place.

The [`relationship`](/looker/docs/reference/param-explore-join-relationship) parameter is important. Joins can cause [fanout](https://www.googlecloudcommunity.com/gc/Technical-Tips-Tricks/The-problem-of-SQL-fanouts/ta-p/587483) problems where rows are duplicated. By specifying that many orders will join to only one user, Looker recognizes that fanouts won't occur from this join, so special handling is not needed. However, `one_to_many` relationships can trigger a fanout.

The automatic generation of views and Explores defaults to a left outer join. In the previous example, however, it is very likely that every order will have exactly one user, so the join in this example can be an inner join.

To [view the generated SQL](/looker/docs/how-looker-generates-sql#viewing_the_query) of an Explore, you can [run the Explore in the UI](/looker/docs/viewing-and-interacting-with-explores#the_explore_page) and then select the **SQL** tab in the **Data** panel.

For example, if you open the **Orders** Explore, which was defined previously, and then select the **User ID** and **Count** fields, the generated SQL will look like the following:
    
    
    SELECT
        `user_id` AS `orders.user_id`,
        COUNT(*) AS `orders.count`
    FROM
        `thelook`.`orders` AS `orders`
    GROUP BY
        1
    ORDER BY
        2 DESC
    LIMIT 500
    

In this example, the users table is not referenced at all. It is only brought in if it is needed.

If you remove the **User ID** dimension and add in the **ID** dimension from the **Users** view, the SQL will look like the following:
    
    
    SELECT
        `users`.`id` AS `users.id`,
        COUNT(*) AS `orders.count`
    FROM
        `thelook`.`orders` AS `orders`
        INNER JOIN `thelook`.`users` AS `users` ON `orders`.`user_id` = `users`.`id`
    GROUP BY
        1
    ORDER BY
        2 DESC
    LIMIT 500
    

In this case, since there is a selection from the **Users** view, the join is included.

The following example shows LookML in the `orders` Explore file, which was defined previously, and adds a join to the `order_items` view:
    
    
    explore: orders {
      join: users {
        type: inner
        sql_on: ${orders.user_id} = ${users.id} ;;
        relationship: many_to_one
      }
      join: order_items {
        type: inner
        sql_on: ${orders.id} = ${order_items.order_id} ;;
        relationship: one_to_many
      }
    }
    

Now if you open the **Orders** Explore in the UI, you will see the **Order Items** view. If you select the **Total Sale Price** measure from the **Order Items** view along with the **Count** from **Orders** and **ID** from **Users** , Looker generates the following SQL:
    
    
    SELECT
        `users`.`id` AS `users.id`,
        COUNT(DISTINCT orders.id ) AS `orders.count`,
        COALESCE(SUM(`order_items`.`sale_price`), 0) AS `order_items.total_sale_price`
    FROM
        `thelook`.`orders` AS `orders`
        INNER JOIN `thelook`.`users` AS `users` ON `orders`.`user_id` = `users`.`id`
        INNER JOIN `thelook`.`order_items` AS `order_items` ON `orders`.`id` = `order_items`.`order_id`
    GROUP BY
        1
    ORDER BY
        2 DESC
    LIMIT 500
    

In this example, `COUNT(*) AS orders.count` became `COUNT(DISTINCT orders.id ) AS orders.count`. Looker detected that there was a possible fanout situation and automatically added the `SQL DISTINCT` keyword to the `SQL COUNT` function.