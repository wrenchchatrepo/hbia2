# https://cloud.google.com/looker/docs/pivot_where

Depth: 3

The `pivot_where` function can be used in a [table calculation](/looker/docs/table-calculations) to select a pivot column by a condition.

## Syntax

**`pivot_where(select_expression, expression)`**

The `pivot_where` function returns the value of `expression` for the pivot column which uniquely satisfies `select_expression` or `null` if such a column does not exist or is not unique.

## Examples

In the following example we look for the pivot column that is based on "Order Status", and has a value of "pending". If we find it, return the "Order Count" in that cell:
    
    
    pivot_where(${orders.status} = "pending", ${orders.count})
    

## Things to know

  1. If there is _exactly_ one pivot column where `select_expression` is true, the `expression` is returned. Otherwise the `expression` returns NULL.

  2. `pivot_where` cannot be used in a [custom filter](/looker/docs/filtering-and-limiting#custom-filters).