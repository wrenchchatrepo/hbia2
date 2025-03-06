# https://cloud.google.com/looker/docs/matches-filter

Depth: 3

The `matches_filter` function can be used in [custom filters](/looker/docs/filtering-and-limiting#custom-filters) and [custom fields](/looker/docs/custom-fields) to determine whether the value of a field matches a [filter expression](/looker/docs/filter-expressions).

### Syntax

**`matches_filter(field,`filter expression`)`**

The `matches_filter` function applies the filter expression to the field and returns `Yes` if the value in the field matches the filter expression or `No` if it does not.

### Examples

This example returns `Yes` in a custom field if the invoice date is less than 30 days old:
    
    
    matches_filter(${billing.invoice_date}, `30 days`)
    

Use the [`if`](/looker/docs/functions-and-operators#functions_for_any_looker_expression_4) function with `matches_filter` to return different values. The next example shows syntax of a custom field that returns "Late" if the invoice date is over 30 days old:
    
    
    if(matches_filter(${billing.invoice_date}, `30 days`), "Current", "Late")
    

### Things to know

The string that defines the filter expression must be enclosed in backtick (`) characters.