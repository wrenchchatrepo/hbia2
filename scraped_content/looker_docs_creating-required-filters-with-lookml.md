# https://cloud.google.com/looker/docs/creating-required-filters-with-lookml

Depth: 3

You can help curate the [filter experience](/looker/docs/filtering-and-limiting) for your users by specifying filter behavior directly in your LookML. For example, you can add helpful filters that most users would expect to use on an Explore, or you can add a default filter to minimize the risk of queries straining your database resources.  
  
This page provides an overview of each LookML parameter that affects filtering for all users.

## Creating filters that users can change

This table lists LookML parameters that set visible Explore-level filters for all users. Users can see the filters and change the values of the filters while exploring and viewing Looks, but they cannot remove the filters. These filters also apply to dashboards, although users cannot see or change the values of the filters from the dashboard unless you also create a [dashboard filter](/looker/docs/filters-user-defined-dashboards).

LookML parameter | Scope | Visible to users? | Editable by users? | Description  
---|---|---|---|---  
[`always_filter`](/looker/docs/reference/param-explore-always-filter) | Explore | Yes | Yes | Use the [`always_filter`](/looker/docs/reference/param-explore-always-filter) LookML parameter to set an Explore-level filter for all users. Users can see the filter and change its default value, but they cannot remove it from the Explore.  
[`conditionally_filter`](/looker/docs/reference/param-explore-conditionally-filter) | Explore | Yes | Yes | Use the [`conditionally_filter`](/looker/docs/reference/param-explore-conditionally-filter) LookML parameter to set an Explore-level filter for all users. Similar to `always_filter`, users can see the filter and change its default value. However, in contrast to `always_filter`, users can remove a filter that is specified with `conditionally_filter` if a specific field is filtered on instead.  
  
## Creating filters that users cannot change

This table lists LookML parameters that set hidden Explore-level filters for all users. Users cannot change the filter conditions, and the filtering is applied in the SQL of each query. These filters also apply to Looks and dashboards.

LookML parameter | Scope | Visible to users? | Editable by users? | Description  
---|---|---|---|---  
[`sql_always_where`](/looker/docs/reference/param-explore-sql-always-where) | Explore | Sometimes | No | Use the [`sql_always_where`](/looker/docs/reference/param-explore-sql-always-where) LookML parameter to set an Explore-level query restriction into the `WHERE` clause of all SQL queries generated from the Explore. Users will not be able to change the filter condition, and they will only be able to see the filter condition if they have permission to view the generated query SQL.  
[`sql_always_having`](/looker/docs/reference/param-explore-sql-always-having) | Explore | Sometimes | No | Use the [`sql_always_having`](/looker/docs/reference/param-explore-sql-always-having) LookML parameter to set an Explore-level query restriction into the `HAVING` clause of all SQL queries generated from the Explore. As with `sql_always_where`, users will not be able to change the filter condition, and they will only be able to see the filter condition if they have permission to view the generated query SQL.  
[`sql_where`](/looker/docs/reference/param-explore-join-sql-where) | Join | Sometimes | No | Use the [`sql_where`](/looker/docs/reference/param-explore-join-sql-where) LookML parameter to set an Explore-level query restriction into the `WHERE` clause of all SQL queries generated from the Explore when the specified join is included in the query. As with `sql_always_where`, users will not be able to change the filter condition, and they will only be able to see the filter condition if they have permission to view the generated query SQL.  
[`access_filter`](/looker/docs/reference/param-explore-access-filter) | Explore | Sometimes | No | Use the [`access_filter`](/looker/docs/reference/param-explore-access-filter) LookML parameter to set an Explore-level, user-specific query restriction into the `WHERE` clause of all SQL queries generated from the Explore. As with `sql_always_where`, users will not be able to change the filter condition, and they will only be able to see the filter condition if they have permission to view the generated query SQL. However, in contrast to `sql_always_where`, the filter condition is determined by each user's user attribute values.  
  
## Preventing users from filtering on a field

This table lists LookML parameters that prevent individual fields from being filtered on.

LookML parameter | Scope | Visible to users? | Editable by users? | Description  
---|---|---|---|---  
[`can_filter`](/looker/docs/reference/param-field-can-filter) | Field | Yes | No | Use the [`can_filter`](/looker/docs/reference/param-field-can-filter) LookML parameter to specify whether a field can be filtered on. To prevent filtering on a field, add the line `can_filter: no` to that field. This also prevents the field from being filtered on in drill menus.  
[`skip_drill_filter`](/looker/docs/reference/param-field-skip-drill-filter) | Field | Yes | No | Use the [`skip_drill_filter`](/looker/docs/reference/param-field-skip-drill-filter) LookML parameter to specify whether a field can be filtered on in drill menus. To prevent filtering on a field in drill menus, add the line `skip_drill_filter: yes` to that field. The field will still be filterable in other locations.