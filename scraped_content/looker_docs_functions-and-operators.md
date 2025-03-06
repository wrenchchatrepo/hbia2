# https://cloud.google.com/looker/docs/functions-and-operators

Depth: 3

**Note:** This page is part of the [Retrieve and chart data](/looker/docs/retrieve-and-chart-data) learning series.

> If your admin has granted you the [permissions](/looker/docs/admin-panel-users-roles#create_table_calculations) to create [table calculations](/looker/docs/table-calculations), you can use the following features to quickly perform common functions without needing to create Looker expressions:
> 
>   * [**Shortcut Calculations**](/looker/docs/table-calculations#quick_calculations) to quickly perform common calculations on numeric fields that are in an Explore's data table
> 

> 
> If your admin has granted you the [permissions](/looker/docs/admin-panel-users-roles#create_custom_fields) to create [custom fields](/looker/docs/custom-fields), you can use the following features to quickly perform common functions without needing to create Looker expressions:
> 
>   * [**Custom groups**](/looker/docs/custom-fields#custom_grouping) to quickly group values under custom labels without needing to develop `CASE WHEN` logic in [`sql`](/looker/docs/reference/param-field-sql) parameters or [`type: case`](/looker/docs/reference/param-field-case) fields
> 
>   * [**Custom bins**](/looker/docs/custom-fields#custom_binning) to group numeric type dimensions in custom tiers without needing to develop [`type: tier`](/looker/docs/reference/param-dimension-filter-parameter-types#tier) LookML fields
> 
> 

[Looker expressions](/looker/docs/creating-looker-expressions) (sometimes referred to as _Lexp_) are used to perform calculations for:

  * [Table calculations](/looker/docs/table-calculations) (which include expressions used in [data tests](/looker/docs/reference/param-model-test))
  * [Custom fields](/looker/docs/custom-fields)
  * [Custom filters](/looker/docs/filtering-and-limiting#custom-filters)

A major part of these expressions is the functions and operators that you can use in them. The functions and operators can be divided into a few basic categories:

  * Mathematical: Number-related functions
  * String: Word- and letter-related functions
  * Dates: Date- and time-related functions
  * Logical transformation: Includes boolean (true or false) functions and comparison operators
  * Positional transformation: Retrieving values from different rows or pivots

## Some functions are only available for table calculations

Looker expressions for [custom filters](/looker/docs/filtering-and-limiting#custom-filters) and [custom fields](/looker/docs/custom-fields) do not support Looker functions that convert datatypes, aggregate data from multiple rows, or refer to other rows or pivot columns. These functions are supported _only_ for [table calculations](/looker/docs/table-calculations) (including table calculations used in the `expression` parameter of a [data test](/looker/docs/reference/param-model-test)).

This page is organized to clarify which functions and operators are available, depending on where you are using your Looker expression.

## Mathematical functions and operators

Mathematical functions and operators work in one of two ways:

  * Some mathematical functions perform calculations based on a _single_ row. For example, rounding, taking a square root, multiplying, and similar functions can be used for values in a single row, returning a distinct value for each and every row. All mathematical operators, such as `+`, are applied one row at a time.
  * Other mathematical functions, like averages and running totals, operate over _many_ rows. These functions take many rows and reduce them to a single number, then display that same number on every row.

### Functions for any Looker expression

Function | Syntax | Purpose  
---|---|---  
[`abs`](/looker/docs/abs) | `abs(value)` | Returns the absolute value of `value`. For an example, see the [Standard Deviation and Simple Time Series Outlier Detection Using Table Calculations](https://community.looker.com/explores-36/standard-deviation-and-simple-time-series-outlier-detection-using-table-calculations-1367) Community post.  
`ceiling` | `ceiling(value)` | Returns the smallest integer greater than or equal to `value`.  
[`exp`](/looker/docs/exp) | `exp(value)` | Returns _e_ to the power of `value`.  
`floor` | `floor(value)` | Returns the largest integer less than or equal to `value`.  
[`ln`](/looker/docs/ln) | `ln(value)` | Returns the natural logarithm of `value`.  
`log` | `log(value)` | Returns the base 10 logarithm of `value`.  
`mod` | `mod(value, divisor)` | Returns the remainder of dividing `value` by `divisor`.  
[`power`](/looker/docs/power) | `power(base, exponent)` | Returns `base` raised to the power of `exponent`. For an example, see the [Standard Deviation and Simple Time Series Outlier Detection Using Table Calculations](https://community.looker.com/explores-36/standard-deviation-and-simple-time-series-outlier-detection-using-table-calculations-1367) Community post.  
[`rand`](/looker/docs/rand) | `rand()` | Returns a random number between 0 and 1.  
`round` | `round(value, num_decimals)` | Returns `value` rounded to `num_decimals` decimal places. For examples using `round`, see the [Using `pivot_index` in table calculations](https://community.looker.com/explores-36/using-pivot-index-in-table-calculations-3-28-1291) and [Standard Deviation and Simple Time Series Outlier Detection Using Table Calculations](https://community.looker.com/explores-36/standard-deviation-and-simple-time-series-outlier-detection-using-table-calculations-1367) Community posts.  
`sqrt` | `sqrt(value)` | Returns the square root of `value`. For an example, see the [Standard Deviation and Simple Time Series Outlier Detection Using Table Calculations](https://community.looker.com/explores-36/standard-deviation-and-simple-time-series-outlier-detection-using-table-calculations-1367) Community post.  
  
### Functions for table calculations only

> Many of these functions operate over many rows and will only consider the rows returned by your query.

Function | Syntax | Purpose  
---|---|---  
`acos` | `acos(value)` | Returns the inverse cosine of `value`.  
`asin` | `asin(value)` | Returns the inverse sine of `value`.  
`atan` | `atan(value)` | Returns the inverse tangent of `value`.  
`beta_dist` | `beta_dist(value, alpha, beta, cumulative)` | Returns the position of `value` on the beta distribution with parameters `alpha` and `beta`. If `cumulative = yes`, returns the cumulative probability.  
`beta_inv` | `beta_inv(probability, alpha, beta)` | Returns the position of `probability` on the inverse cumulative beta distribution with parameters `alpha` and `beta`.  
`binom_dist` | `binom_dist(num_successes, num_tests, probability, cumulative)` | Returns the probability of getting `num_successes` successes in `num_tests` tests with the given `probability` of success. If `cumulative = yes`, returns the cumulative probability.  
`binom_inv` | `binom_inv(num_tests, test_probability, target_probability)` | Returns the smallest number `k` such that `binom(k, num_tests, test_probability, yes) >= target_probability`.  
`chisq_dist` | `chisq_dist(value, dof, cumulative)` | Returns the position of `value` on the gamma distribution with `dof` degrees of freedom. If `cumulative = yes`, returns the cumulative probability.  
`chisq_inv` | `chisq_inv(probability, dof)` | Returns the position of `probability` on the inverse cumulative gamma distribution with `dof` degrees of freedom.  
`chisq_test` | `chisq_test(actual, expected)` | Returns the probability for the chi-squared test for independence between `actual` and `expected` data. `actual` can be a column or a column of lists, and `expected` must be the same type.  
`combin` | `combin(set_size, selection_size)` | Returns the number of ways of choosing `selection_size` elements from a set of size `set_size`.  
`confidence_norm` | `confidence_norm(alpha, stdev, n)` | Returns half the width of the normal confidence interval at significance level `alpha`, standard deviation `stdev`, and sample size `n`.  
`confidence_t` | `confidence_t(alpha, stdev, n)` | Returns half the width of the [Student's _t_ -distribution confidence interval](https://en.wikipedia.org/wiki/Student's_t-distribution#Confidence_intervals) at significance level `alpha`, standard deviation `stdev`, and sample size `n`.  
`correl` | `correl(column_1, column_2)` | Returns the correlation coefficient of `column_1` and `column_2`.  
`cos` | `cos(value)` | Returns the cosine of `value`.  
`count` | `count(expression)` | Returns the count of non-`null` values in the column defined by `expression`, unless `expression` defines a column of lists, in which case returns the count in each list.  
`count_distinct` | `count_distinct(expression)` | Returns the count of distinct non-`null` values in the column defined by `expression`, unless `expression` defines a column of lists, in which case returns the count in each list.  
`covar_pop` | `covar_pop(column_1, column_2)` | Returns the population covariance of `column_1` and `column_2`.  
`covar_samp` | `covar_samp(column_1, column_2)` | Returns the sample covariance of `column_1` and `column_2`.  
`degrees` | `degrees(value)` | Converts `value` from radians to degrees.  
`expon_dist` | `expon_dist(value, lambda, cumulative)` | Returns the position of `value` on the exponential distribution with parameter `lambda`. If `cumulative = yes`, returns the cumulative probability.  
`f_dist` | `f_dist(value, dof_1, dof_2, cumulative)` | Returns the position of `value` on the F distribution with parameters `dof_1` and `dof_2`. If `cumulative = yes`, returns the cumulative probability.  
`f_inv` | `f_inv(probability, dof_1, dof_2)` | Returns the position of `probability` on the inverse cumulative F distribution with parameters `dof_1` and `dof_2`.  
`fact` | `fact(value)` | Returns the factorial of `value`.  
`gamma_dist` | `gamma_dist(value, alpha, beta, cumulative)` | Returns the position of `value` on the gamma distribution with parameters `alpha` and `beta`. If `cumulative = yes`, returns the cumulative probability.  
`gamma_inv` | `gamma_inv(probability, alpha, beta)` | Returns the position of `probability` on the inverse cumulative gamma distribution with parameters `alpha` and `beta`.  
`geomean` | `geomean(expression)` | Returns the geometric mean of the column created by `expression` unless `expression` defines a column of lists, in which case returns the geometric mean of each list.  
`hypgeom_dist` | `hypgeom_dist(sample_successes, sample_size, population_successes, population_size, cumulative)` | Returns the probability of getting `sample_successes` from the given `sample_size`, number of `population_successes`, and `population_size`. If `cumulative = yes`, returns the cumulative probability.  
`intercept` | `intercept(y_column, x_column)` | Returns the intercept of the linear regression line through the points determined by `y_column` and `x_column`. For an example, see the [How to Forecast in Looker with Table Calculations](https://community.looker.com/technical-tips-tricks-1021/how-to-forecast-in-looker-with-table-calculations-30247) Community post.  
`kurtosis` | `kurtosis(expression)` | Returns the sample excess kurtosis of the column created by `expression` unless `expression` defines a column of lists, in which case returns the sample excess kurtosis of each list.  
`large` | `large(expression, k)` | Returns the `k`th largest value of the column created by `expression` unless `expression` defines a column of lists, in which case returns the `k`th largest value of each list.  
`match` | `match(value, expression)` | Returns the row number of the first occurrence of `value` in the column created by `expression` unless `expression` defines a column of lists, in which case returns the position of `value` in each list.  
`max` | `max(expression)` | Returns the max of the column created by `expression` unless `expression` defines a column of lists, in which case returns the max of each list. For examples using `max`, see the [Using lists in table calculations](https://community.looker.com/explores-36/using-lists-in-table-calculations-3-36-1895) and [Grouping by a dimension in table calculations](https://community.looker.com/explores-36/grouping-by-a-dimension-in-table-calculations-2127) Community posts.  
`mean` | `mean(expression)` | Returns the mean of the column created by `expression` unless `expression` defines a column of lists, in which case returns the mean of each list. For examples using `mean`, see the [Calculating Moving Averages](https://community.looker.com/technical-tips-tricks-1021/calculating-moving-averages-30817) Community post and the [Standard Deviation and simple time series outlier detection using Table Calculations](https://community.looker.com/explores-36/standard-deviation-and-simple-time-series-outlier-detection-using-table-calculations-1367) Community post.  
`median` | `median(expression)` | Returns the median of the column created by `expression` unless `expression` defines a column of lists, in which case returns the median of each list.  
`min` | `min(expression)` | Returns the min of the column created by `expression` unless `expression` defines a column of lists, in which case returns the min of each list.  
`mode` | `mode(expression)` | Returns the mode of the column created by `expression` unless `expression` defines a column of lists, in which case returns the mode of each list.  
`multinomial` | `multinomial(value_1, value_2, ...)` | Returns the factorial of the sum of the arguments divided by the product of each of their factorials.  
`negbinom_dist` | `negbinom_dist(num_failures, num_successes, probability, cumulative)` | Returns the probability of getting `num_failures` failures before getting `num_successes` successes, with the given `probability` of success. If `cumulative = yes`, returns the cumulative probability.  
`norm_dist` | `norm_dist(value, mean, stdev, cumulative)` | Returns the position of `value` on the normal distribution with the given `mean` and `stdev`. If `cumulative = yes`, returns the cumulative probability.  
`norm_inv` | `norm_inv(probability, mean, stdev)` | Returns the position of `probability` on the inverse normal cumulative distribution.  
`norm_s_dist` | `norm_s_dist(value, cumulative)` | Returns the position of `value` on the standard normal distribution. If `cumulative = yes`, returns the cumulative probability.  
`norm_s_inv` | `norm_s_inv(probability)` | Returns the position of `probability` on the inverse standard normal cumulative distribution.  
`percent_rank` | `percent_rank(column, value)` | Returns the rank of `value` in `column` as a percentage from 0 to 1 inclusive, where `column` is the column, field, list, or range containing the dataset to consider; and `value` is the column with the value for which the percentage rank will be determined.Sample Usage:`percent_rank(${view_name.field_1}, ${view_name.field_1})``percent_rank(list(1, 2, 3), ${view_name.field_1})``percent_rank(list(1, 2, 3), 2)`  
`percentile` | `percentile(expression, percentile_value)` | Returns the value from the column created by `expression` corresponding to the given `percentile_value`, unless `expression` defines a column of lists, in which case returns the percentile value for each list. `percentile_value` must be between 0 and 1; otherwise returns `null`.  
`pi` | `pi()` | Returns the value of pi.  
`poisson_dist` | `poisson_dist(value, lambda, cumulative)` | Returns the position of `value` on the poisson distribution with parameter `lambda`. If `cumulative = yes`, returns the cumulative probability.  
`product` | `product(expression)` | Returns the product of the column created by `expression` unless `expression` defines a column of lists, in which case returns the product of each list.  
`radians` | `radians(value)` | Converts `value` from degrees to radians.  
`rank` | `rank(value, expression)` | Returns the rank of `value` in the column created by `expression`. For example, if you want to rank orders by their total sale price, you could use `rank(${order_items.total_sale_price},${order_items.total_sale_price})`, which gives a rank for each value of `order_items.total_sale_price` in your query when comparing it to the entire column of `order_items.total_sale_price` in your query. In the case where the `expression` defines multiple lists, this function returns the relative size of the `value` in each list. For an example, see the [Ranks with Table Calculations](https://community.looker.com/explores-36/ranks-with-table-calculations-8122) Community post.  
`rank_avg` | `rank_avg(value, expression)` | Returns the average rank of `value` in the column created by `expression` unless `expression` defines a column of lists, in which case returns the average rank of `value` in each list.  
`running_product` | `running_product(value_column)` | Returns a running product of the values in `value_column`.  
`running_total` | `running_total(value_column)` | Returns a running total of the values in `value_column`. For an example, see the [Creating a Running Total Down Columns with Table Calculations](/looker/docs/best-practices/how-to-create-running-total-down-columns-with-table-calculations) Best Practices page.  
`sin` | `sin(value)` | Returns the sine of `value`.  
`skew` | `skew(expression)` | Returns the sample skewness of the column created by `expression` unless `expression` defines a column of lists, in which case returns the sample skewness of each list.  
`slope` | `slope(y_column, x_column)` | Returns the slope of the linear regression line through points determined by `y_column` and `x_column`. For an example, see the [How to Forecast in Looker with Table Calculations](https://community.looker.com/technical-tips-tricks-1021/how-to-forecast-in-looker-with-table-calculations-30247) Community post.  
`small` | `small(expression, k)` | Returns the `k`th smallest value of the column created by `expression` unless `expression` defines a column of lists, in which case returns the `k`th smallest value of each list.  
`stddev_pop` | `stddev_pop(expression)` | Returns the standard deviation (population) of the column created by `expression` unless `expression` defines a column of lists, in which case returns the standard deviation (population) of each list.  
`stddev_samp` | `stddev_samp(expression)` | Returns the standard deviation (sample) of the column created by `expression` unless `expression` defines a column of lists, in which case returns the standard deviation (sample) of each list.  
`sum` | `sum(expression)` | Returns the sum of the column created by `expression` unless `expression` defines a column of lists, in which case returns the sum of each list. For examples using `sum`, see the [Aggregating Across Rows (Row Totals) in Table Calculations](/looker/docs/best-practices/how-to-aggregate-values-across-rows) and [How to Calculate Percent-of-Total](/looker/docs/best-practices/how-to-calculate-percent-of-total) Best Practices pages.  
`t_dist` | `t_dist(value, dof, cumulative)` | Returns the position of `value` on the [Student's _t_ -distribution](https://en.wikipedia.org/wiki/Student's_t-distribution) with `dof` degrees of freedom. If `cumulative = yes`, returns the cumulative probability.  
`t_inv` | `t_inv(probability, dof)` | Returns the position of `probability` on the inverse normal cumulative distribution with `dof` degrees of freedom.  
`t_test` | `t_test(column_1, column_2, tails, type)` | Returns the result of a [Student's _t_ -test](https://en.wikipedia.org/wiki/Student%27s_t-test) on the data from `column_1` and `column_2`, using 1 or 2 `tails`. `type`: 1 = paired, 2 = homoscedastic, 3 = heteroscedastic.  
`tan` | `tan(value)` | Returns the tangent of `value`.  
`var_pop` | `var_pop(expression)` | Returns the variance (population) of the column created by `expression` unless `expression` defines a column of lists, in which case returns the variance (population) of each list.  
`var_samp` | `var_samp(expression)` | Returns the variance (sample) of the column created by `expression` unless `expression` defines a column of lists, in which case returns the variance (sample) of each list.  
`weibull_dist` | `weibull_dist(value, shape, scale, cumulative)` | Returns the position of `value` on the Weibull distribution with parameters `shape` and `scale`. If `cumulative = yes`, returns the cumulative probability.  
`z_test` | `z_test(data, value, stdev)` | Returns the one-tailed p-value of the z-test using the existing `data` and `stdev` on the hypothesized mean `value`.  
  
### Operators for any Looker expression

You can use the following standard mathematical operators:

Operator | Syntax | Purpose  
---|---|---  
`+` | `value_1 + value_2` | Adds `value_1` and `value_2`.  
`-` | `value_1 - value_2` | Subtracts `value_2` from `value_1`.  
`*` | `value_1 * value_2` | Multiplies `value_1` and `value_2`.  
`/` | `value_1 / value_2` | Divides `value_1` by `value_2`.  
  
## String functions

String functions operate on sentences, words, or letters, which are collectively called "strings." You can use string functions to capitalize words and letters, extract parts of a phrase, check to see if a word or letter is in a phrase, or replace elements of a word or phrase. String functions can also be used to format the data returned in the table.

### Functions for any Looker expression

Function | Syntax | Purpose  
---|---|---  
`concat` | `concat(value_1, value_2, ...)` | Returns `value_1`, `value_2`, `...`, `value_n` joined as one string.  
`contains` | `contains(string, search_string)` | Returns `Yes` if `string` contains `search_string`, and `No` otherwise. The `contains` function is case-sensitive.  
`length` | `length(string)` | Returns the number of characters in `string`.  
`lower` | `lower(string)` | Returns `string` with all characters converted to lowercase.  
`position` | `position(string, search_string)` | Returns the start index of `search_string` in `string` if it exists, and `0` otherwise.  
`replace` | `replace(string, old_string, new_string)` | Returns `string` with all occurrences of `old_string` replaced with `new_string`.  
`substring` | `substring(string, start_position, length)` | Returns the substring of `string`, beginning at `start_position`, consisting of `length` characters. The `start_position` starts at `1`, with `1` indicating the first character in the string, `2` indicating the second character in the string, and so on.  
`upper` | `upper(string)` | Returns `string` with all characters converted to uppercase.  
  
### Functions for table calculations only

Function | Syntax | Purpose  
---|---|---  
`split` | `split(string, delimeter)` | Returns a list of strings in `string` broken up by `delimiter`.  
`to_number` | `to_number(string)` | Returns the number represented by `string`, or `null` if the string cannot be converted.  
`to_string` | `to_string(value)` | Returns the string representation of `value`, or an empty string if `value` is null.  
  
## Date functions

Date functions enable you to work with dates and times.

### Functions for any Looker expression

Function | Syntax | Purpose  
---|---|---  
`add_days` | `add_days(number, date)` | Adds `number` days to `date`.  
`add_hours` | `add_hours(number, date)` | Adds `number` hours to `date`.  
`add_minutes` | `add_minutes(number, date)` | Adds `number` minutes to `date`.  
`add_months` | `add_months(number, date)` | Adds `number` months to `date`.  
`add_seconds` | `add_seconds(number, date)` | Adds `number` seconds to `date`.  
`add_years` | `add_years(number, date)` | Adds `number` years to `date`.  
`date` | `date(year, month, day)` | Returns "`year-month-day`" date or `null` if the date would be invalid.  
`date_time` | `date_time(year, month, day, hours, minutes, seconds)` | Returns `year-month-day hours:minutes:seconds` date or `null` if the date would be invalid.  
`diff_days` | `diff_days(start_date, end_date)` | Returns the number of days between `start_date` and `end_date`. For an example, see the [Using dates in table calculations](https://community.looker.com/explores-36/using-dates-in-table-calculations-3-30-1398) Community post.  
`diff_hours` | `diff_hours(start_date, end_date)` | Returns the number of hours between `start_date` and `end_date`.  
`diff_minutes` | `diff_minutes(start_date, end_date)` | Returns the number of minutes between `start_date` and `end_date`. For an example, see the [Using dates in table calculations](https://community.looker.com/explores-36/using-dates-in-table-calculations-3-30-1398) Community post.  
`diff_months` | `diff_months(start_date, end_date)` | Returns the number of months between `start_date` and `end_date`. For an example, see the [Grouping by a dimension in table calculations](https://community.looker.com/explores-36/grouping-by-a-dimension-in-table-calculations-2127) Community post.  
`diff_seconds` | `diff_seconds(start_date, end_date)` | Returns the number of seconds between `start_date` and `end_date`.  
`diff_years` | `diff_years(start_date, end_date)` | Returns the number of years between `start_date` and `end_date`.  
`extract_days` | `extract_days(date)` | Extracts the days from `date`. For an example, see the [Using dates in table calculations](https://community.looker.com/explores-36/using-dates-in-table-calculations-3-30-1398) Community post.  
`extract_hours` | `extract_hours(date)` | Extracts the hours from `date`.  
`extract_minutes` | `extract_minutes(date)` | Extracts the minutes from `date`.  
`extract_months` | `extract_months(date)` | Extracts the months from `date`.  
`extract_seconds` | `extract_seconds(date)` | Extracts the seconds from `date`.  
`extract_years` | `extract_years(date)` | Extracts the years from `date`.  
`now` | `now()` | Returns the current date and time. For examples using `now`, see the [Now() Table Calculation Function Has Better Timezone Handling](https://community.looker.com/explores-36/now-table-calculation-function-has-better-timezone-handling-3-48-2753) and [Using dates in table calculations](https://community.looker.com/explores-36/using-dates-in-table-calculations-3-30-1398) Community posts.  
`trunc_days` | `trunc_days(date)` | Truncates `date` to days.  
`trunc_hours` | `trunc_hours(date)` | Truncates `date` to hours.  
`trunc_minutes` | `trunc_minutes(date)` | Truncates `date` to minutes.  
`trunc_months` | `trunc_months(date)` | Truncates `date` to months.  
`trunc_years` | `trunc_years(date)` | Truncates `date` to years.  
  
### Functions for table calculations only

Function | Syntax | Purpose  
---|---|---  
`to_date` | `to_date(string)` | Returns the date and time corresponding to `string` (YYYY, YYYY-MM, YYYY-MM-DD, YYYY-MM-DD hh, YYYY-MM-DD hh:mm, or YYYY-MM-DD hh:mm:ss).  
  
## Logical functions, operators, and constants

Logical functions and operators are used to assess whether something is true or false. Expressions using these elements take a value, evaluate it against some criteria, return `Yes` if the criteria are met, and `No` if the criteria are not met. There are also various logical operators for comparing values and combining logical expressions.

### Functions for any Looker expression

Function | Syntax | Purpose  
---|---|---  
`case` | `case(when(yesno_arg, value_if_yes), when(yesno_arg, value_if_yes), ..., else_value)` |  ADDED 21.10  Allows conditional logic with multiple conditions and outcomes. Returns `value_if_yes` for the first `when` case whose `yesno_arg` value is `yes`. Returns `else_value` if all `when` cases are `no`.  
`coalesce` | `coalesce(value_1, value_2, ...)` | Returns the first non-`null` value in `value_1`, `value_2`, `...`, `value_n` if found and `null` otherwise. For examples using `coalesce`, see the [Creating a running total across rows with table calculations](https://community.looker.com/explores-36/creating-a-running-total-across-rows-with-table-calculations-1375), [Creating a percent of total across rows with table calculations](https://community.looker.com/explores-36/creating-a-percent-of-total-across-rows-with-table-calculations-1057), and [Using pivot_index in table calculations](https://community.looker.com/explores-36/using-pivot-index-in-table-calculations-3-28-1291) Community posts.  
`if` | `if(yesno_expression, value_if_yes, value_if_no)` | If `yesno_expression` evaluates to `Yes`, returns the `value_if_yes` value. Otherwise, returns the `value_if_no` value. For an example, see the [Grouping by a dimension in table calculations](https://community.looker.com/explores-36/grouping-by-a-dimension-in-table-calculations-2127) Community post.  
`is_null` | `is_null(value)` | Returns `Yes` if `value` is `null`, and `No` otherwise. For an example, see the [Creating Looker expressions](/looker/docs/creating-looker-expressions#using_functions) documentation page. For another example that uses `is_null` with the `NOT` operator, see the [Using table calculations](/looker/docs/table-calculations#using_table_calculations_in_visualizations) documentation page.  
  
### Operators for any Looker expression

The following comparison operators can be used with any data type:

Operator | Syntax | Purpose  
---|---|---  
`=` | `value_1 = value_2` | Returns `Yes` if `value_1` is equal to `value_2`, and `No` otherwise.  
`!=` | `value_1 != value_2` | Returns `Yes` if `value_1` is not equal to `value_2`, and `No` otherwise.  
  
The following comparison operators can be used with numbers, dates, and strings:

Operator | Syntax | Purpose  
---|---|---  
`>` | `value_1 > value_2` | Returns `Yes` if `value_1` is greater than `value_2`, and `No` otherwise.  
`<` | `value_1 < value_2` | Returns `Yes` if `value_1` is less than `value_2`, and `No` otherwise.  
`>=` | `value_1 >= value_2` | Returns `Yes` if `value_1` is greater than or equal to `value_2`, and `No` otherwise.  
`<=` | `value_1 <= value_2` | Returns `Yes` if `value_1` is less than or equal to `value_2`, and `No` otherwise.  
  
You also can combine Looker expressions with these logical operators:

Operator | Syntax | Purpose  
---|---|---  
`AND` | `value_1 AND value_2` | Returns `Yes` if both `value_1` and `value_2` are `Yes`, and `No` otherwise.  
`OR` | `value_1 OR value_2` | Returns `Yes` if either `value_1` or `value_2` is `Yes`, and `No` otherwise.  
`NOT` | `NOT value` | Returns `Yes` if `value` is `No`, and `No` otherwise.  
  
> These logical operators must be capitalized. Logical operators written in lowercase will not work.

### Logical constants

You can use logical constants in Looker expressions. These constants are always written in lowercase and have the following meanings:

Constant | Meaning  
---|---  
`yes` | True  
`no` | False  
`null` | No value  
  
Note that the constants `yes` and `no` are the special symbols that ​mean true or false in Looker expressions. In contrast, using quotes such as in `"yes"` and `"no"` creates literal strings with those values.

Logical expressions evaluate to true or false without requiring an `if` function. For example, this:

`if(${field} > 100, yes, no)`

is equivalent to this:

`${field} > 100`

You also can use `null` to indicate no value. For example, you may want to determine if a field is empty, or assign an empty value in a certain situation. This formula returns no value if the field is less than 1, or the value of the field if it is more than 1:

`if(${field} < 1, null, ${field})`

### Combining `AND` and `OR` operators

`AND` operators are evaluated before `OR` operators, if you don't otherwise specify the order with parentheses. Thus, the following expression without additional parentheses:
    
    
    if (
      ${order_items.days_to_process}>=4 OR
      ${order_items.shipping_time}>5 AND
      ${order_facts.is_first_purchase},
    "review", "okay")
    

would be evaluated as:
    
    
    if (
      ${order_items.days_to_process}>=4 OR
      (${order_items.shipping_time}>5 AND ${order_facts.is_first_purchase}),
    "review", "okay")
    

## Positional functions

When creating table calculations, you can use positional transformation functions to extract information about fields in different rows or pivot columns. You can also create lists and retrieve the current row or pivot column index.

### Column and row totals for table calculations only

If your [Explore contains totals](/looker/docs/creating-and-editing-explores#displaying_totals), you can reference total values for columns and rows:

Function | Syntax | Purpose  
---|---|---  
`:total` | `${field:total}` | Returns the column total of the field.  
`:row_total` | `${field:row_total}` | Returns the row total of the field.  
  
### Row-related functions for table calculations only

Some of these functions use the relative positions of rows, so changing the sort order of the rows affects the results of the functions.

Function | Syntax | Purpose  
---|---|---  
`index` | `index(expression, n)` | Returns the value of the `n`th element of the column created by `expression`, unless `expression` defines a column of lists, in which case returns the `n`th element of each list.  
`list` | `list(value_1, value_2, ...)` | Creates a list out of the given values. For an example, see the [Using lists in table calculations](https://community.looker.com/explores-36/using-lists-in-table-calculations-3-36-1895) Community post.  
`lookup` | `lookup(value, lookup_column, result_column)` | Returns the value in `result_column` that is in the same row as `value` is in `lookup_column`.  
`offset` | `offset(column, row_offset)` | Returns the value of row `(n + row_offset)` in `column`, where `n` is the current row number. For examples using `offset`, see the [Calculating Percent of Previous and Percent Change with Table Calculations](/looker/docs/best-practices/how-to-calculate-percent-change-percent-previous) Best Practices page.  
`offset_list` | `offset_list(column, row_offset, num_values)` | Returns a list of the `num_values` values starting at row `(n + row_offset)` in `column`, where `n` is the current row number. For an example, see the [Calculating Moving Averages](https://community.looker.com/technical-tips-tricks-1021/calculating-moving-averages-30817) Community post.  
`row` | `row()` | Returns the current row number.  
  
### Pivot-related functions for table calculations only

Some of these functions use the relative positions of pivot columns, so changing the sort order of the pivoted dimension affects the results of those functions.

Function | Syntax | Purpose  
---|---|---  
`pivot_column` | `pivot_column()` | Returns the index of the current pivot column.  
[`pivot_index`](/looker/docs/pivot_index) | `pivot_index(expression, pivot_index)` | Evaluates `expression` in the context of the pivot column at position `pivot_index` (1 for first pivot, 2 second pivot, etc.). Returns null for unpivoted results. For examples using `pivot_index`, see the [Using pivot_index in table calculations](https://community.looker.com/explores-36/using-pivot-index-in-table-calculations-3-28-1291) and [Creating a percent of total across rows with table calculations](https://community.looker.com/explores-36/creating-a-percent-of-total-across-rows-with-table-calculations-1057) Community posts.  
`pivot_offset` | `pivot_offset(pivot_expression, col_offset)` | Returns the value of the `pivot_expression` in position `(n + col_offset)`, where `n` is the current pivot column position. Returns null for unpivoted results. For examples using `pivot_offset`, see the [Creating a running total across rows with table calculations](https://community.looker.com/explores-36/creating-a-running-total-across-rows-with-table-calculations-1375) Community post and the [Calculating Percent of Previous and Percent Change with Table Calculations](/looker/docs/best-practices/how-to-calculate-percent-change-percent-previous) Best Practices page.  
`pivot_offset_list` | `pivot_offset_list(pivot_expression, col_offset, num_values)` | Returns a list of the `num_values` values in `pivot_expression` starting at position `(n + col_offset)`, where `n` is the current pivot index. Returns `null` for unpivoted results.  
`pivot_row` | `pivot_row(expression)` | Returns the pivoted values of `expression` as a list. Returns `null` for unpivoted results. For examples using `pivot_row`, see the [Aggregating Across Rows (Row Totals) in Table Calculations](/looker/docs/best-practices/how-to-aggregate-values-across-rows) and [How to Calculate Percent-of-Total](/looker/docs/best-practices/how-to-calculate-percent-of-total) Best Practices pages.  
[`pivot_where`](/looker/docs/pivot_where) | `pivot_where(select_expression, expression)` | Returns the value of `expression` for the pivot column that uniquely satisfies `select_expression` or `null` if such a unique column does not exist.  
  
The specific pivot functions you use determine whether the table calculation is displayed next to each pivoted column, or is displayed as a single column at the end of the table.

## Filter functions for custom filters and custom fields

Filter functions let you work with [filter expressions](/looker/docs/filter-expressions) to return values based on filtered data. Filter functions work in [custom filters](/looker/docs/filtering-and-limiting#custom_filters), [filters on custom measures](/looker/docs/custom-fields#adding_a_custom_filter_to_a_custom_field), and [custom dimensions](/looker/docs/custom-fields#creating_a_custom_dimension_using_a_looker_expression), but are not valid in table calculations.

Function | Syntax | Purpose  
---|---|---  
[`matches_filter`](/looker/docs/matches-filter) | `matches_filter(field, filter_expression)` | Returns `Yes` if the value of the field matches the filter expression, `No` if not.