# https://cloud.google.com/looker/docs/reference/param-lookml-dashboard-scatter-chart

Depth: 3

This page demonstrates how to add and customize a LookML dashboard element of `type: looker_scatter` with LookML dashboard parameters in a [`dashboard.lkml` file](/looker/docs/other-project-files#dashboard_files).

For information about building a scatter chart through the Looker UI, see the [Scatter chart options](/looker/docs/scatter-options) documentation page.

## Example usage
    
    
    ## BASIC PARAMETERS
    name: element_name
    title: 'Element Title'
    type: looker_scatter
    height: N
    width: N
    top: N
    left: N
    row: N
    col: N
    refresh: N (seconds | minutes | hours | days)
    note:
      text: 'note text'
      state: collapsed | expanded
      display: above | below | hover
    
    ## QUERY PARAMETERS
    model: model_name
    explore: explore_name
    dimensions: [view_name.field_name, view_name.field_name, …]
    measures: [view_name.field_name, view_name.field_name, …]
    sorts: [view_name.field_name asc | desc, view_name.field_name, …]
    pivots: [view_name.field_name, view_name.field_name, …]
    limit: N
    column_limit: N
    filters:
      view_name.field_name: 'Looker filter expression' | 'filter value'
    listen:
      dashboard_filter_name: dimension_or_measure_name
    query_timezone: 'specific timezone' | user_timezone
    merged_queries:
    - 'primary query definition'
    - 'next source query definition'
      join_fields:
      - field_name: view_name.field_name
        source_field_name: view_name.field_name
    
    ## PLOT PARAMETERS
    stacking: normal | percent | ''
    show_null_points: true | false
    swap_axes: true | false
    cluster_points: true | false
    hide_legend: true | false
    legend_position: center | left | right
    hidden_fields: [view_name.field_name, view_name.field_name, …]
    limit_displayed_rows: true | false
    limit_displayed_rows_values:
      show_hide: show | hide
      first_last: first | last
      num_rows: 'N'
    quadrants_enabled: true | false
      quadrant_properties:
        '0':
          color: ''
          label: 'Quadrant 1 label'
        '1':
          color: ''
          label: 'Quadrant 2 label'
        '2':
          color: ''
          label: 'Quadrant 3 label'
        '3':
          color: ''
          label: 'Quadrant 4 label'
    custom_quadrant_point_x: 3
    custom_quadrant_point_y: 6
    custom_quadrant_value_x: 55
    custom_quadrant_value_y: 40
    
    ## SERIES PARAMETERS
    colors: [css_color, css_color, …]
    show_view_names: true | false
    point_style: none | circle | circle_outline
    size_by_field: view_name.field_name
    plot_size_by_field: true | false
    series_colors:
      series_name: css_color
      # Possibly more series color assignments
    
    series_labels:
      'Series Name': desired series label
      # Possibly more series label assignments
    series_types:
      series_name: column | line | area | scatter
      # Possibly more series visualization assignments
    series_point_styles:
      series_name: square | diamond | triangle | triangle-down | auto
    
    ## VALUE PARAMETERS
    show_value_labels: true | false
    custom_value_label_column: default | series_name
    label_color: [css_color, css_color, …]
    font_size: Npx
    label_value_format: 'value formatting string'
    hidden_series: [series_name, series_name, …]
    
    ## X-AXIS PARAMETERS
    x_axis_scale: auto | linear | ordinal | time
    x_axis_reversed: true | false
    show_x_axis_label: true | false
    x_axis_label: desired x-axis label
    show_x_axis_ticks: true | false
    x_axis_gridlines: true | false
    x_axis_label_rotation: N
    x_axis_datetime_label: 'time formatting string'
    x_axis_zoom: true | false
    
    ## Y-AXIS PARAMETERS
    y_axis_gridlines: true | false
    y_axis_reversed: true | false
    reference_lines:
      # reference line options
    y_axis_zoom: true | false
    
    

## Parameter definitions

Parameter Name | Description  
---|---  
Basic Parameters  
`name` (for elements) | Creates an element  
`title` (for elements) | Changes the way an element name appears to users  
`type` (for elements) | Determines the type of visualization to be used in the element  
`height` (for elements) | Defines the height of an element in units of [`tile_size`](/looker/docs/reference/param-lookml-dashboard#tile_size) for [`layout: tile`](/looker/docs/reference/param-lookml-dashboard#layout) and [`layout: static`](/looker/docs/reference/param-lookml-dashboard#layout) dashboards  
`width` (for elements) | Defines the width of an element in units of [`tile_size`](/looker/docs/reference/param-lookml-dashboard#tile_size) for [`layout: tile`](/looker/docs/reference/param-lookml-dashboard#layout) and [`layout: static`](/looker/docs/reference/param-lookml-dashboard#layout) dashboards  
`top` | Defines the top-to-bottom position of an element in units of [`tile_size`](/looker/docs/reference/param-lookml-dashboard#tile_size) for [`layout: static`](/looker/docs/reference/param-lookml-dashboard#layout) dashboards  
`left` | Defines the left-to-right position of an element in units of [`tile_size`](/looker/docs/reference/param-lookml-dashboard#tile_size) for [`layout: static`](/looker/docs/reference/param-lookml-dashboard#layout) dashboards  
`row` | Defines the top-to-bottom position of an element in units of rows for [`layout: newspaper`](/looker/docs/reference/param-lookml-dashboard#layout) dashboards  
`col` | Defines the left-to-right position of an element in units of columns for [`layout: newspaper`](/looker/docs/reference/param-lookml-dashboard#layout) dashboards  
`refresh` (for elements) | Sets the interval at which the element will automatically refresh  
`note` | Starts a section of LookML to define a note for an element. This parameter has the subparameters `text`, `state`, and `display`.  
Query Parameters  
`model` | Defines the model to be used for the element's query  
`explore` (for elements) | Defines the Explore to be used for the element's query  
`dimensions` | Defines the dimensions to be used for the element's query  
`measures` | Defines the measures to be used for the element's query  
`sorts` | Defines the sorts to be used for the element's query  
`pivots` | Defines the dimensions that should be pivoted to be used for the element's query  
`limit` | Defines the row limit to be used for the element's query  
`filters` (for elements) | Defines the filters that _cannot_ be changed for the element's query  
`listen` | Defines the filters that _can_ be changed for the element's query, if [`filters` (for dashboard)](/looker/docs/reference/param-lookml-dashboard#filters-for-dashboard) have been created  
`query_timezone` | Defines the [time zone](/looker/docs/reference/param-view-timezone-values) that should be used when the query is run  
`merged_queries` | Defines a [merged results](/looker/docs/merged-results) query  
Plot Parameters  
`stacking` | Stacks series on top of each other to create a stacked chart  
`show_null_points` | Specifies whether to plot points that have null values  
`swap_axes` | Reverses the x and y axes on a chart  
`cluster_points` | Groups large numbers of data values into clusters  
`hide_legend` | Hides the chart legend  
`legend_position` | Specifies whether legend appears to the left, center, or right of the chart  
`hidden_fields` | Specifies any fields to use in the query but hide in the chart  
`limit_displayed_rows` | Shows or hides rows in a visualization based on their position in the results  
`limit_displayed_rows_values` | Specifies which rows to show or hide in a visualization. This parameter has the subparameters `show_hide`, `first_last`, and `num_rows`.  
`quadrants_enabled` | Adds quadrant lines to a dashboard element of `type: looker_scatter`  
`custom_quadrant_point_x` | Defines the location of the vertical quadrant line  
`custom_quadrant_point_y` | Defines the location of the horizontal quadrant line  
`custom_quadrant_value_x` | Defines the location of the vertical quadrant line based on a value on the x-axis  
`custom_quadrant_value_y` | Defines the location of the horizontal quadrant line based on a value on the y-axis  
Series Parameters  
`colors` | Sets the colors of chart series based on the order in which the series appear  
`show_view_names` | Hides view names from chart label  
`point_style` | Specifies how data points appear  
`size_by_field` | Sizes all points on the chart by a specific field  
`plot_size_by_field` | Sets whether the field used to size the points is plotted separately  
`series_colors` | Sets the colors of chart series based on the name of the series  
`series_labels` | Changes the way a series name appears to users  
`series_types` | Mixes visualization types by defining the type for each series  
`series_point_styles` | Specifies the shape of chart points  
Value Parameters  
`show_value_labels` | Shows labels next to data points  
`custom_value_label_column` | Set the field that will be used as the value labels for data points when `show_value_labels` is set to true  
`label_color` | Specifies a comma-separated list of color values  
`font_size` | Sets the font size of value labels  
`label_value_format` | Specifies Excel-style formatting for value label  
`hidden_series` | Hides a chart series when the element loads  
X-Axis Parameters  
`x_axis_scale` | Specifies how the x-axis scale is calculated  
`x_axis_reversed` | Specifies the direction of the x-axis  
`show_x_axis_label` | Hides the x-axis label  
`x_axis_label` | Defines a custom x-axis label  
`show_x_axis_ticks` | Shows ticks on the x-axis  
`x_axis_gridlines` | Extends grid lines from the x-axis  
`x_axis_label_rotation` | Rotates x-axis labels a number of degrees  
`x_axis_datetime_label` | Defines a format string for the x-axis labels, if they are dates  
`x_axis_zoom` | Specifies whether to allow zooming along the x-axis  
Y-Axis Parameters  
`y_axis_gridlines` |  Extends gridlines from the y-axis  
`y_axis_reversed` | Sets the direction of the x-axis  
`reference_lines` | Adds reference lines to a chart  
`y_axis_zoom` | Specifies whether to allow zooming along the y-axis. Disabled if `x_axis_zoom: false`.  
  
## Basic parameters

When defining a LookML dashboard element, you must specify values for at least the `name` and `type` basic parameters. Other basic parameters like `title`, `height`, and `width` affect the appearance and position of an element on a dashboard.

### `name`

> This section refers to the `name` parameter that is part of a [dashboard element](/looker/docs/reference/param-lookml-dashboard-element).
> 
> `name` can also be used as part of a dashboard filter, described on the [Dashboard parameters](/looker/docs/reference/param-lookml-dashboard#name-for-filters) documentation page.

Each `name` declaration creates a new dashboard element and assigns it a name. Element names must be unique. Names are sometimes referenced in the [`elements`](/looker/docs/reference/param-lookml-dashboard#elements-for-rows) parameter when you're using [`layout: grid`](/looker/docs/reference/param-lookml-dashboard#layout) dashboards.
    
    
    - name: orders_by_date
    

### `title`

> This section refers to the `title` parameter that is part of a [dashboard element](/looker/docs/reference/param-lookml-dashboard-element).
> 
> `title` can also be used as part of a dashboard, described on the [Dashboard parameters](/looker/docs/reference/param-lookml-dashboard#title_\(for_dashboard\)) documentation page.
> 
> `title` can also be used as part of a dashboard filter, described on the [Dashboard parameters](/looker/docs/reference/param-lookml-dashboard#title-for-filters) documentation page.

The `title` parameter lets you change how an element's name will appear to users. If unspecified, the title defaults to the element `name`.

Consider this example:
    
    
    - name: sales_overview
      title: '1) Sales Overview'
    

If you used this format, instead of the element appearing as **Sales Overview** , it would appear as **1) Sales Overview**.

### `type`

> This section refers to the `type` parameter that is part of a [dashboard element](/looker/docs/reference/param-lookml-dashboard-element).
> 
> `type` can also be used as part of a dashboard filter, described on the [Dashboard parameters](/looker/docs/reference/param-lookml-dashboard#type-for-filters) documentation page.
> 
> `type` can also be used as part of a join, described on the [`type` (for joins)](/looker/docs/reference/param-explore-join-type) parameter documentation page.
> 
> `type` can also be used as part of a dimension, described on the [Dimension, filter, and parameter types](/looker/docs/reference/param-dimension-filter-parameter-types) documentation page.
> 
> `type` can also be used as part of a measure, described on the [Measure types](/looker/docs/reference/param-measure-types) documentation page.

The `type` parameter determines the type of visualization to be used in the element.
    
    
    - name: element_name
      type: text | looker_grid | table | single_value | looker_single_record |
            looker_column | looker_bar | looker_scatter | looker_line | looker_area |
            looker_pie | looker_donut_multiples | looker_funnel | looker_timeline |
            looker_map | looker_google_map | looker_geo_coordinates | looker_geo_choropleth | looker_waterfall | looker_wordcloud | looker_boxplot
    

See the [`type` (for LookML dashboards)](/looker/docs/reference/param-lookml-dashboard-type) documentation page for an overview of the different types of LookML dashboard elements.

### `height`

> This section refers to the `height` parameter that is part of a [dashboard element](/looker/docs/reference/param-lookml-dashboard-element).
> 
> `height` can also be used as part of a dashboard row, described on the [Dashboard parameters](/looker/docs/reference/param-lookml-dashboard#height-for-rows) documentation page.

#### For dashboards with `tile` or `static` layouts

The `height` parameter defines the height of an element, in units of [`tile_size`](/looker/docs/reference/param-lookml-dashboard#tile_size) (which is defined in pixels), for [`layout: tile`](/looker/docs/reference/param-lookml-dashboard#layout) and [`layout: static`](/looker/docs/reference/param-lookml-dashboard#layout) dashboards.

For example, the following code specifies `tile_size: 100` and `height: 4`, making the `orders_by_date` element 400 pixels in height.
    
    
    - dashboard: sales_overview
      tile_size: 100
      ...
    
      elements:
      - name: orders_by_date
        height: 4
        ...
    

#### For dashboards with `newspaper` layout

The `height` parameter defines the height of an element, in units of row, for [`layout: newspaper`](/looker/docs/reference/param-lookml-dashboard#layout) dashboards.

A dashboard with newspaper layout defaults to an element height of 6 rows, or about 300 pixels. The minimum height is 1 row for dashboards with a [`preferred viewer`](/looker/docs/reference/param-lookml-dashboard#preferred_viewer) parameter set to `dashboards-next`. The minimum height is 2 rows for dashboards with a `preferred viewer` parameter set to `dashboards`.

For example, the following code sets an element to be 12 rows tall, or twice as tall as other elements that are set to the default:
    
    
    - dashboard: sales_overview
      layout: newspaper
      ...
    
      elements:
      - name: orders_by_date
        height: 12
        ...
    

### `width`

> This section refers to the `width` parameter that is part of a [dashboard element](/looker/docs/reference/param-lookml-dashboard-element).
> 
> `width` can also be used as part of a dashboard, described on the [Dashboard parameters](/looker/docs/reference/param-lookml-dashboard#width-for-dashboard) documentation page.

The `width` parameter defines the width of an element, in units of [`tile_size`](/looker/docs/reference/param-lookml-dashboard#tile_size), for [`layout: tile`](/looker/docs/reference/param-lookml-dashboard#layout) and [`layout: static`](/looker/docs/reference/param-lookml-dashboard#layout) dashboards.

For example, the following code specifies `tile_size: 100` and `width: 4`, making the `orders_by_date` element 400 pixels in width.
    
    
    - dashboard: sales_overview
      tile_size: 100
      ...
    
      elements:
      - name: orders_by_date
        width: 4
        ...
    

The `width` parameter defines the width of an element, in units of columns, for [`layout: newspaper`](/looker/docs/reference/param-lookml-dashboard#layout) dashboards.

A dashboard with newspaper layout defaults to a width of 24 columns.

For example, the following code sets the element to half the width of the dashboard:
    
    
    - dashboard: sales_overview
      layout: newspaper
      ...
    
      elements:
      - name: orders_by_date
        width: 12
        ...
    

### `top`

The `top` parameter defines the top-to-bottom position of an element, in units of [`tile_size`](/looker/docs/reference/param-lookml-dashboard#tile_size), for [`layout: static`](/looker/docs/reference/param-lookml-dashboard#layout) dashboards.

For example, the following code specifies `tile_size: 100` and `top: 4`, positioning the top edge of the `orders_by_date` element 400 pixels from the top of the dashboard.
    
    
    - dashboard: sales_overview
      tile_size: 100
      ...
    
      elements:
      - name: orders_by_date
        top: 4
        ...
    

### `left`

The `left` parameter defines the left-to-right position of an element, in units of [`tile_size`](/looker/docs/reference/param-lookml-dashboard#tile_size), for [`layout: static`](/looker/docs/reference/param-lookml-dashboard#layout) dashboards.

For example, the following code specifies `tile_size: 100` and `left: 4`, positioning the left edge of the `orders_by_date` element 400 pixels from the left side of the dashboard.
    
    
    - dashboard: sales_overview
      tile_size: 100
      ...
    
      elements:
      - name: orders_by_date
        left: 4
        ...
    

### `row`

For [`layout: newspaper`](/looker/docs/reference/param-lookml-dashboard#layout) dashboards, the `row` parameter defines the row that the top edge of an element is placed on.

A dashboard begins with row 0 at the top of the dashboard. A dashboard with newspaper layout defaults to an element height of 6 rows, meaning the dashboard elements at the top of a dashboard (`row: 0`) would default to taking up rows 0-5.

Each row is 50 pixels tall, which means the default element height of 6 rows is 300 pixels.

For example, the following code sets an element to be set on the second row of elements in the dashboard, assuming elements are set at the default height:
    
    
    - dashboard: sales_overview
      layout: newspaper
      ...
    
      elements:
      - name: orders_by_date
        row: 6
        ...
    

### `col`

For [`layout: newspaper`](/looker/docs/reference/param-lookml-dashboard#layout) dashboards, the `col` parameter defines the column that the left edge of the element is placed on.

Dashboards are divided into 24 columns. A dashboard begins with column 0 at the left of the dashboard. A dashboard with newspaper layout defaults to an element width of 8 columns, meaning the dashboard elements at the left of a dashboard (`col: 0`) would default to taking up columns 0-7.

For example, the following code sets an element to be set in the third column of elements in the dashboard:
    
    
    - dashboard: sales_overview
      layout: newspaper
      ...
    
      elements:
      - name: orders_by_date
        col: 16
        ...
    

### `refresh`

> This section refers to the `refresh` parameter that is part of a [dashboard element](/looker/docs/reference/param-lookml-dashboard-element).
> 
> `refresh` can also be used as part of a dashboard, described on the [Dashboard parameters](/looker/docs/reference/param-lookml-dashboard#refresh-for-dashboard) documentation page.

The `refresh` parameter allows an element to reload automatically on some periodic basis, thereby retrieving fresh data. This is often helpful in settings where a dashboard is constantly displayed, such as on an office TV. Note that the dashboard must be open in a browser window for this parameter to have an effect. This setting does not run in the background to "pre-warm" the dashboard cache.

The refresh rate can be any number (without decimals) of seconds, minutes, hours, or days. For example:
    
    
    - name: orders_by_date
      refresh: 2 hours
    

Use caution when setting short refresh intervals. If the query behind the element is resource-intensive, certain elements may strain your database more than desired.

### `note`

You can add descriptive notes to elements like this:
    
    
    - name: element_name
      note:
        text: 'note text'
        state: collapsed | expanded
        display: above | below | hover
    

`note` has the subparameters `text`, `state`, and `display`.

#### `text`

The `text` subparameter specifies the text displayed in the note. The text can be [localized](/looker/docs/model-localization).

#### `state`

The `state` subparameter determines whether the note will be `collapsed` or `expanded` if it is too big to fit on a single row within the element's width. If you choose `collapsed` and the note is too long, the note will end in a clickable ellipsis (`...`) that can be used to read the full note.

#### `display`

The `display` subparameter determines where the note is displayed on an element. `above` places the note at the top of an element, `below` places it at the bottom of an element, and `hover` requires the user to hover their mouse over the element to see the note.

## Query parameters

When defining a LookML dashboard element, you must specify values for at least the `model` and `explore` query parameters, and at least one field must be specified using either the `dimensions` parameter or the `measures` parameter. You can also use the other query parameters to control the way data is displayed in a dashboard element.

### `model`

The `model` parameter defines the model to use for the element query. If unspecified, it will default to the model where the dashboard resides.
    
    
    - name: orders_by_date
      model: ecommerce
    

The `model` parameter accepts [LookML constants](/looker/docs/reference/param-manifest-constant). You can define a constant in the [manifest file](/looker/docs/other-project-files#project_manifest_files) for your project, then use the syntax `"@{constant_name}"` to set the constant as the value for `model`. Using a constant lets you define the name of a model in one place, which is particularly useful if you're updating the name of a model that is used by multiple dashboard elements.

For more information and an example of using constants with LookML dashboards, see the [`constant`](/looker/docs/reference/param-manifest-constant#using_constants_in_lookml_dashboards) parameter documentation page.

### `explore`

> This section refers to the `explore` parameter that is part of a [dashboard element](/looker/docs/reference/param-lookml-dashboard-element).
> 
> `explore` can also be used as part of a model, described on the [`explore`](/looker/docs/reference/param-explore-explore) parameter documentation page.
> 
> `explore` can also be used as part of a dashboard filter, described on the [Dashboard parameters](/looker/docs/reference/param-lookml-dashboard#explore-for-filters) documentation page.

The `explore` parameter defines the Explore to use for the element query.
    
    
    - name: orders_by_date
      explore: order
    

The `explore` parameter accepts [LookML constants](/looker/docs/reference/param-manifest-constant). You can define a constant in the [manifest file](/looker/docs/other-project-files#project_manifest_files) for your project, then use the syntax `"@{constant_name}"` to set the constant as the value for `explore`. Using a constant lets you define the name of an Explore in one place, which is particularly useful if you're updating the name of an Explore that is used by multiple dashboard elements.

For more information and an example of using constants with LookML dashboards, see the [`constant`](/looker/docs/reference/param-manifest-constant#using_constants_in_lookml_dashboards) parameter documentation page.

### `dimensions`

The `dimensions` parameter defines the dimension or dimensions to use for the element query. Use the syntax `view_name.dimension_name` to specify the dimension. Don't include `dimensions` if the query doesn't have any.
    
    
    ## single dimension example
    - name: orders_by_date
      dimensions: order.order_date
    
    ## multiple dimension example
    - name: orders_by_date
      dimensions: [order.order_date, customer.name]
    

### `measures`

The `measures` parameter defines the measure or measures to use for the element query. Use the syntax `view_name.measure_name` to specify the measure. Don't include `measures` if the query doesn't have any.
    
    
    ## single measure example
    - name: orders_by_date
      measures: order.count
    
    ## multiple measure example
    - name: orders_by_date
      measures: [order.count, order_item.count]
    

### `sorts`

The `sorts` parameter defines the sorts to be used for the element query. The primary sort is listed first, then the secondary sort, and so on. Use the syntax `view_name.field_name` to specify the dimension or measure. Don't include `sorts` if you want to use Looker's default sort order. Descending sorts are suffixed with `desc`; ascending sorts don't need a suffix.
    
    
    ## single sort example
    - name: orders_by_date
      sorts: order.order_date desc
    
    ## multiple sort example
    - name: orders_by_date
      sorts: [order.order_date desc, customer.name]
    

### `pivots`

The `pivots` parameter defines the dimensions that should be pivoted for the element query. Use the syntax `view_name.dimension_name` to specify the dimension. Don't include `pivots` if the query doesn't have any.
    
    
    ## single pivot example
    - name: orders_by_date
      pivots: customer.gender
    
    ## multiple pivot example
    - name: orders_by_date
      pivots: [customer.gender, customer.age_tier]
    

### `limit`

The `limit` parameter defines the row limit that should be used for the element query. The limit applies to the number of rows **before** any pivots are applied.
    
    
    - name: orders_by_date
      limit: 100
    

### `filters`

> This section refers to the `filters` parameter that is part of a [dashboard element](/looker/docs/reference/param-lookml-dashboard-element).
> 
> `filters` can also be used as part of a dashboard, described on the [Dashboard parameters](/looker/docs/reference/param-lookml-dashboard#filters-for-dashboard) documentation page.
> 
> `filters` can also be used as part of a measure, described on the [`filters`](/looker/docs/reference/param-field-filters) parameter documentation page.

The `filters` parameter defines the non-changeable filters that should be used for the element's query. If you would like filters that a user _can_ change in the dashboard, you should set up the filters using [`filters` for dashboards](/looker/docs/reference/param-lookml-dashboard#filters-for-dashboard), then apply them to the elements using `listen`.

The syntax for `filters` is:
    
    
    - name: element_name
      filters:
        orders.created_date: 2020/01/10 for 3 days
        orders.status: Shipped
        # You can create multiple filter statements
    

Each filter can accept a Looker [filter expression](/looker/docs/filter-expressions) or a value constant. You can also use the [`_localization`](/looker/docs/model-localization#filter_localization_example) or [`_user_attributes`](/looker/docs/liquid-variable-reference#user_attributes) Liquid variables in the filter expression for flexible filter values.

### `listen`

Dashboard filters let viewers interactively refine the data that is shown in dashboard elements. Define dashboard filters with the [`filters` parameter for LookML dashboards](/looker/docs/reference/param-lookml-dashboard#filters-for-dashboard). Then, use the `listen` parameter to link dashboard elements to the dashboard filter.

The syntax for `listen` is as follows:
    
    
    - name: element_name
      listen:
        filter_name_goes_here: dimension or measure on which to apply
                               the filter using view_name.field_name syntax
        # You can add more than one listen statement
    

Add the `listen` parameter to an element, and then provide the name of the filter followed by a colon and a reference to the field to which the filter should apply, using the `view_name.field_name` syntax. For example, you might create a filter called **Date** that requires a user to enter a date into the filter field in the UI. You could then apply the value that the user enters to the `orders_by_date` element like this:
    
    
    - dashboard: sales_overview
      ...
    
      filters:
      - name: date
        type: date_filter
    
      elements:
     - name: orders_by_date
        listen:
          date: order.order_date
        ...
    

For additional examples of using the `filters` parameter and the `listen` parameter to apply dashboard filters to individual dashboard elements, see [Building LookML dashboards](/looker/docs/building-lookml-dashboards#dashboard_filters).

### `query_timezone`

The `query_timezone` parameter specifies the time zone in which the query will be run. The time zone options are shown on the [Values for `timezone`](/looker/docs/reference/param-view-timezone-values) documentation page. If you want the query to run using the viewer's time zone, you can assign the value as `user_timezone`.
    
    
    - name: orders_by_date
      query_timezone: America/Los Angeles
    
    
    
    - name: orders_by_customer
      query_timezone: user_timezone
    

### `merged_queries`

The `merged_queries` parameter lets you [combine the results of multiple queries](/looker/docs/merged-results) into a single dashboard element. Define each source query within the element's `merged_queries` parameter and use the `join_fields`subparameter to specify [how the results should be merged](/looker/docs/merged-results#checking_the_merge_rules_and_running_the_merge).

The following sample LookML code creates a merged results [element of `type: looker_grid`](/looker/docs/reference/param-lookml-dashboard-table-chart). In this example, the `merged_queries` parameter is used to create a dashboard element that combines data from two separate queries into a single table chart:
    
    
    - name: merged_results_element
      title: Merged Results Tile
      type: looker_grid
      merged_queries:
      - model: ecommerce
        explore: users
        type: table
        fields: [users.state, users.count, users.city]
        sorts: [users.count desc 0]
        limit: 5000
        column_limit: 50
        query_timezone: UTC
        listen:
        - State: users.state
      - model: ecommerce
        explore: users
        type: table
        fields: [users.state, users.city]
        sorts: [users.state]
        limit: 500
        column_limit: 50
        query_timezone: UTC
        join_fields:
        - field_name: users.state
          source_field_name: users.state
        - field_name: users.city
          source_field_name: users.city
        listen:
        - State: users.state
    

In this example, the dashboard element combines data from two source queries that are based on the `users` Explore in the `ecommerce` model. The primary query includes the `users.state`, `users.count`, and `users.city` fields, and it sorts the results by the `users.count` field. The second source query includes the `users.state` and `users.city` fields and sorts the results by the `users.state` field.

The `join_field` parameter merges the source queries based on matching values in the `users.state` and `users.city` fields.

The `listen` parameter applies a `State` filter to both queries, which lets dashboard viewers refine the query results that are displayed in the dashboard tile by selecting a specific state.

#### Example: Merging company data

Suppose you want to create a merged query that combines information about companies from two different Explores: `company_info` and `companies`. You want to join the queries on the `ipo.stock_symbol`, `companies.name`, and `companies.contact_email` fields from each Explore to create a query that returns results for company name, company contact email, IPO year, stock symbol, number of employees, and job count. You can define the merged query element in LookML as follows:
    
    
    - name: merged_results_element
      title: Merged Results Tile
      merged_queries:
      - model: market_research
        explore: company_info
        fields: [companies.name, companies.contact_email, ipo.public_year, ipo.stock_symbol]
        filters:
          companies.contact_email: "-NULL"
          ipo.valuation_amount: NOT NULL
        sorts: [ipo.public_year desc]
      - model: company_data
        explore: companies
        fields: [companies.name, ipo.stock_symbol, companies.contact_email,
          companies.number_of_employees, jobs.job_count]
        filters:
          companies.number_of_employees: NOT NULL
          ipo.stock_symbol: "-NULL"
          companies.contact_email: "-NULL"
        sorts: [jobs.job_count desc]
        join_fields:
        - field_name: ipo.stock_symbol
          source_field_name: ipo.stock_symbol
        - field_name: companies.name
          source_field_name: companies.name
        - field_name: companies.contact_email
          source_field_name: companies.contact_email
    

#### Applying filters to merged query elements

The previous example of a merged query element demonstrates how to apply hard-coded filters directly within each source query by using the `filters` parameter. For example, the filters `companies.contact_email: "-NULL"` and `ipo.valuation_amount: NOT NULL` in the primary query restrict the results to companies that have valid contact emails and valuations. These query-level filters pre-filter the data before merging the queries and cannot be changed by the user.

You can also apply [dashboard filters](/looker/docs/building-lookml-dashboards#dashboard_filters) to merged query elements by using the `listen` parameter within the definition of each source query. For example, suppose you have a dashboard filter named `Industry` that you defined at the dashboard level by using the [`filters` parameter for LookML dashboards](/looker/docs/reference/param-lookml-dashboard#filters-for-dashboard):
    
    
    filters:
    - name: Industry
      title: Industry
      type: field_filter
      ui_config:
        type: dropdown_menu
        display: inline
      model: market_research
      explore: company_info
      field: companies.industry
    

To apply the `Industry` filter to the `companies.industry` field in both source queries, add the `listen` parameter to each of the merged query's source query definitions as follows:
    
    
    listen:
      Industry: companies.industry
    

For example, the following sample code adds the `Industry` filter to both source queries in the merged results element from the previous example.
    
    
    - name: merged_results_element
      title: Merged Results Tile
      merged_queries:
      - model: market_research
        explore: company_info
        fields: [companies.name, companies.contact_email, ipo.public_year, ipo.stock_symbol]
        filters:
          companies.contact_email: "-NULL"
          ipo.valuation_amount: NOT NULL
        sorts: [ipo.public_year desc]
        listen:
          Industry: companies.industry
      - model: company_data
        explore: companies
        fields: [companies.name, ipo.stock_symbol, companies.contact_email,
          companies.number_of_employees, jobs.job_count]
        filters:
          companies.number_of_employees: NOT NULL
          ipo.stock_symbol: "-NULL"
          companies.contact_email: "-NULL"
        sorts: [jobs.job_count desc]
        join_fields:
        - field_name: ipo.stock_symbol
          source_field_name: ipo.stock_symbol
        - field_name: companies.name
          source_field_name: companies.name
        - field_name: companies.contact_email
          source_field_name: companies.contact_email
        listen:
          Industry: companies.industry
    

With this addition, when a user interacts with the `Industry` dashboard filter, the corresponding source query in the merged query element will be filtered accordingly.

**Tip:** Each source query can listen to one or more dashboard filters. This lets you define filter logic for each source query independently, regardless of the number of source queries in your merged results element. If a query does not have a `listen` parameter, then it won't be affected by any dashboard filters.

## Plot parameters

Most of the parameters described in this section correspond to the options in the [**Plot** section](/looker/docs/scatter-options#plot_menu_options) of the visualization editor for scatter charts.

### `stacking`

The `stacking` parameter specifies how series are clustered visually on a chart.

  * `normal`: Stacks bars, lines, and points one on top of each other, as in a normal stacked column chart.

  * `percent`: Stack bars, lines, and points to total 100% fill of the chart and set the y-axis values to be percentages.

  * `''`: Bars, lines, and points are not stacked and are instead grouped.

    
    
    stacking: normal | percent | ''
    
    ## default value: ''
    

### `show_null_points`

The `show_null_points` parameter determines whether to plot points that have null values. When it is set to `true`, null values are plotted at zero on the y-axis. When it is set to `false`, null values are not plotted at all, and the chart will draw a straight line between the points before and after the null point. If you want the chart to show a blank space for the null value instead, consider `discontinuous_nulls: true`.
    
    
    show_null_points: true | false
    
    ## default value: true
    

### `swap_axes`

Swap the x-axis and y-axis from the normal configuration. When the axes are swapped, dimensions will be plotted on the y-axis, and measures will be plotted on the x-axis.
    
    
    swap_axes: true | false
    
    ## default value: false
    

**Note:** You cannot use the `swap_axes` parameter to swap the x-axis and the y-axis when the `cluster_points` parameter is set to `true`.

### `cluster_points`

**Note:** New in Looker 22.20, you can use the `cluster_points` parameter with a dashboard element of `type: looker_scatter` to combine densely clustered data points into larger blocks of data.

When the `cluster_points` parameter is set to `true`, Looker [groups densely clustered data points](/looker/docs/scatter-options#cluster_points) into blocks of data values. The number on a cluster shows how many data points it contains. When viewing a scatterplot visualization, users can select a specific cluster of data to view the individual data points that are contained within that cluster.
    
    
    cluster_points: true | false
    
    

**Note:** You cannot use the `swap_axes` parameter to swap the x-axis and the y-axis when the `cluster_points` parameter is set to `true`.

### `hide_legend`

This declaration will hide the legend from the visualization.
    
    
    hide_legend: true | false
    
    ## default value: false
    

### `legend_position`

If `hide_legend` is set to `false` (and there is more than one series), you can use the `legend_position` parameter to specify whether the series legend will appear to the left, center, or right of the chart.
    
    
    legend_position: center | left | right
    
    ## default value: false
    

### `hidden_fields`

The `hidden_fields` parameter indicates which fields, if any, are used in the query but hidden in the chart. Any hidden fields will appear in the data table section of an Explore.
    
    
    hidden_fields: [inventory_items.count, distribution_centers.id]
    

### `limit_displayed_rows`

The `limit_displayed_rows` parameter lets you show or hide rows in a visualization, based on their position in the results. For example, if your visualization displays a 7-day rolling average, you may want to hide the first 6 rows. Setting this to `true` lets you specify the values and positions in the visualization to which this applies using the `limit_displays_rows_values` parameter and its subparameters.
    
    
    limit_displayed_rows: true
    limit_displayed_rows_values:
      show_hide: hide | show
      first_last: first | last
      num_rows: '10'
    
    

### `limit_displayed_rows_values`

Use the `limit_displayed_rows_values` parameter, and its subparameters `show_hide`, `first_last`, and `num_rows`, with `limit_displayed_rows` to specify which rows to show or hide in a visualization. See the `limit_displayed_rows` section for sample usage.

#### `show_hide`

The `show_hide` subparameter sets whether to hide certain rows from the visualization. Set `show_hide` to `show` to display only a limited number of rows in the visualization, and set `show_hide` to `hide` to exclude certain rows from the visualization.

#### `first_last`

The `first_last` subparameter sets whether the rows to be hidden or shown will be the first or last rows in the result set. Setting `first_last` to `first` shows or hides the first rows, while set `first_last` to `last` shows or hides the last rows.

#### `num_rows`

The `num_rows` subparameter sets the number of rows to be hidden or shown. For example, `num_rows: '10'` will show or hide either the first or last 10 rows of the result set from the visualization.

### `quadrants_enabled`

The `quadrants_enabled` parameter allows you to add [quadrant lines](/looker/docs/scatter-options#plot_quadrants) to a dashboard element of `type: looker_scatter`.

You can use the `custom_quadrant_point_x` and `custom_quadrant_point_y` parameters or the `custom_quadrant_value_x` and `custom_quadrant_value_y` parameters to define the locations of the vertical and horizontal quadrant lines, and you can use the `quadrant_properties` parameter to customize the background color and label of each quadrant.
    
    
    quadrants_enabled: true
      quadrant_properties:
        '0':
          color: ''
          label: 'Quadrant 1 label'
        '1':
          color: ''
          label: 'Quadrant 2 label'
        '2':
          color: ''
          label: 'Quadrant 3 label'
        '3':
          color: ''
          label: 'Quadrant 4 label'
    
    

### `custom_quadrant_point_x`

You can use the `custom_quadrant_point_x` parameter to define the location of the vertical quadrant line. Set the `custom_quadrant_point_x` parameter to a value between `1` and `9`, inclusive. The default value is `5`, which centers the line on the visualization.
    
    
    custom_quadrant_point_x: 6
    
    

### `custom_quadrant_point_y`

You can use the `custom_quadrant_point_y` parameter to define the location of the horizontal quadrant line. Set the `custom_quadrant_point_y` parameter to a value between `1` and `9`, inclusive. The default value is `5`, which centers the line on the visualization.
    
    
    custom_quadrant_point_y: 2
    
    

### `custom_quadrant_value_x`

You can use the `custom_quadrant_value_x` parameter to set the vertical quadrant line to the location of a specific numeric value on the x-axis of your visualization. When you specify a value for `custom_quadrant_value_x`, this overrides any value that was provided for the `custom_quadrant_point_x` parameter.
    
    
    custom_quadrant_value_x: 55
    
    

### `custom_quadrant_value_y`

You can use the `custom_quadrant_value_y` parameter to set the vertical quadrant line to the location of a specific numeric value on the y-axis of your visualization. When you specify a value for `custom_quadrant_value_y`, this overrides any value that was provided for the `custom_quadrant_point_y` parameter.
    
    
    custom_quadrant_value_y: 40
    
    

#### `quadrant_properties`

When the `quadrants_enabled` parameter is set to `true`, you can use the `quadrants_properties` parameter to define custom labels and background colors for each of the four quadrants. To define custom colors or labels for each quadrant using the `quadrant_properties` parameter, use the `color` parameter and the `label` parameter with the appropriate number for each quadrant:

  * `'0'`: First quadrant
  * `'1'`: Second quadrant
  * `'2'`: Third quadrant
  * `'3'`: Fourth quadrant

For example, the following LookML sets the color of the first quadrant to the hex code `#EDEDED` and changes the label that will be displayed to users to **First Quadrant**.
    
    
    quadrant_properties:
      '0':
        color: '#EDEDED'
        label: 'First Quadrant'
    

## Series parameters

The parameters described in this section correspond to the options in the [**Series** section](/looker/docs/scatter-options#series_menu_options) of the visualization editor for scatter charts.

### `colors`

The `colors` parameter specifies a list of colors for the series. The first color in the list corresponds to the first data series. If there are more series than listed colors, the colors will start over at the beginning.
    
    
    colors: [blue, orange, yellow, red, purple]
    
    

For all chart attributes that specify a color, the color value can take a hex string, such as `#2ca6cd`, or a [CSS named color string](https://www.w3schools.com/cssref/css_colors.asp), such as `mediumblue`.

### `show_view_names`

The `show_view_names` parameter determines whether view names are displayed in chart labels, such as axis names and column names.
    
    
    show_view_names: true | false
    
    ## default value: true
    

### `point_style`

The `point_style` parameter specifies how data points appear. The following options are available:

  * `none`: For line and area charts. Points are not displayed.
  * `circle`: Filled circles are displayed.
  * `circle_outline`: Outlined circles are displayed.

### `size_by_field`

Specifying a field for `size_by_field` sizes all points on the chart by the selected field. That field will no longer be plotted separately on the chart, unless `plot_size_by_field` is set to `true`. When points are sized by a field, a key appears in the legend indicating which field the points are sized by.

The `size_by_field` parameter is unavailable when a data table contains a pivot and also contains a measure that falls outside of the pivot. For example, if your table includes a table calculation that uses a `pivot_index` function, `size_by_field` will not be available.
    
    
    size_by_field: order_items.id
    
    

### `plot_size_by_field`

The `plot_size_by_field` parameter can be used when a field is specified for `size_by_field`. This parameter determines whether the field used to size the points is also plotted separately. The default setting is `false`, and means the field is not plotted. When this parameter is set to `true`, additional points appear on the chart representing the field.

### `series_colors`

Set the colors of the series based on the series name, using `name: value` pairs.

For a pivoted chart, the series names are the pivot names.
    
    
    series_colors:
      'Yes': skyblue
      'No': '#000000'
    

For a chart with multiple measures, the series names are the measure field names.
    
    
    series_colors:
      inventory_items.count: crimson
      orders.count: green
    

If the series name is not listed in `series_colors`, the chart will default to the list of colors provided in `colors`. If `colors` is not set, the chart will fall back to the default color scheme.

### `series_labels`

Set the labels of one or more series based on the series name, using `name: label` pairs.

For a pivoted chart, the series names are the pivot names.
    
    
    series_labels:
      'Yes': iOS Users
      'No': Android Users
    

For a chart with multiple measures, the series names are the measure field names.
    
    
    series_labels:
      inventory_items.count: Inventory
      orders.count: Orders
    

### `series_types`

The `series_type` parameter lets you use different Cartesian chart types in the same visualization. Use this parameter to assign a chart type to each series that you want to change. The type options are `line`, `column`, `bar`, `area`, and `scatter`.
    
    
    series_types:
      series_a_name: column
      series_b_name: line
    

All series default to the initial chart type that you choose; you can then modify individual series.

### `series_point_styles`

Specify the shape of the chart points for line, area, or scatter series types. The `series_point_styles` can be set to `square`, `diamond`, `triangle`, `triangle-down`, or `auto`.
    
    
    series_point_styles:
      users.count: triangle
    
    

## Value parameters

The parameters described in this section correspond to the options in the [**Values** section](/looker/docs/scatter-options#values_menu_options) of the visualization editor for scatter charts.

### `show_value_labels`

Display the value of a bar, line, or point next to the data point.
    
    
    show_value_labels: true | false
    
    ## default value: false
    

### `custom_value_label_column`

When the `show_value_labels` parameter is set to `true`, the `custom_value_label_column` parameter is enabled.

Use the `custom_value_label_column` parameter to customize a dimension to be used as value labels for your chart. Assign it the dimension by using the `view_name.field_name` format.
    
    
    custom_value_label_column: default | products.category
    

If this parameter is not set, the default value for the value labels is the measure that is being plotted.

See the [Scatterplot chart options](/looker/docs/scatter-options#select_field_for_value_label) documentation page for more information and an example.

### `labelColor`

If `labelColorEnabled` is set to `true`, use the `labelColor` parameter to specify a custom color for the label and percentages. Labels where `labelPosition` is set to `inline` will appear in the color chosen, and labels on either side of the chart will appear about 40% darker than the chosen color.
    
    
    labelColor: "#4FBC89"
    
    

### `font_size`

Set the font size of value labels using any valid CSS size, such as `10px` or `12px`.
    
    
    font_size: 14px
    
    

### `label_value_format`

The `label_value_format` parameter specifies the formatting to apply to a value, independent of any formatting applied to the underlying dimension or measure. The field accepts Excel-style formatting. If `label_value_format` is not specified, the value will be displayed in the format of the underlying dimension or measure.

You can read about how to specify these formats on the [Adding custom formatting to numeric fields](/looker/docs/custom-formatting#custom_formatting_examples) documentation page. However, color formatting is not supported in Looker.

> The formatting used in the `label_value_format` LookML dashboard parameter is the same as formatting used with the [`value_format` LookML parameter](/looker/docs/reference/param-field-value-format#examples), except that the `value_format` LookML parameter requires the formatting string to be enclosed in double quotes.
    
    
    label_value_format: '0.00'
    
    

### `hidden_series`

The `hidden_series` parameter specifies which series will be disabled in the chart, meaning that the series will appear in the chart legend, but grayed out. Users can enable disabled series by clicking them in the chart legend. Consequently, `hidden_series` may not worked as desired with `hide_legend: true`.

For a pivoted chart, the series names are the pivot names:
    
    
    hidden_series: ['Yes', 'No']
    

For a chart with multiple measures, the series names are the measure field names:
    
    
    hidden_series: [inventory_items.count, orders.count]
    

Used together with the `show_silhouette` parameter, you can specify whether disabled series are shown as a lightly shaded representation in the chart itself.

## X-axis parameters

The parameters described in this section correspond to the options in the [**X** section](/looker/docs/scatter-options#x_menu_options) of the visualization editor for scatter charts.

### `x_axis_scale`

This parameter determines how the x-axis scale is calculated.

  * `auto`: The scale will be inferred from the underlying data. This is the default setting.
  * `linear`: The scale will be plotted as linear numeric data. This will not work if the underlying data can't be converted to numbers.
  * `ordinal`: The data will be plotted as evenly spaced, discrete entries.
  * `time`: The data will be plotted as time and the axis will be labeled appropriately. This will not work if the underlying data can't be converted to dates.

    
    
    x_axis_scale: auto | linear | ordinal | time
    
    ## default value: auto
    

### `x_axis_reversed`

This parameter sets the direction of the x-axis. When `x_axis_reversed` is set to `false`, values increase from left to right. When it is set to `true`, values decrease from left to right.
    
    
    x_axis_reversed: true | false
    
    

### `show_x_axis_label`

This parameter determines whether labels are shown on the x-axis.
    
    
    show_x_axis_label: true | false
    
    ## default value: true
    

### `x_axis_label`

This parameter specifies a label for the x-axis. You can use this parameter when `show_x_axis_label` is set to `true`.
    
    
    x_axis_label: Order Date
    

### `show_x_axis_ticks`

This parameter determines whether value labels are shown on the x-axis.
    
    
    show_x_axis_ticks: true | false
    
    ## default value: true
    

### `x_axis_gridlines`

This parameter determines whether gridlines are extended from the x-axis.
    
    
    x_axis_gridlines: true | false
    
    ## default value: false
    

### `x_axis_label_rotation`

The `x_axis_label_rotation` parameter defines the rotation of the x-axis labels in degrees. This parameter accepts values between `-360` and `360`, denoting the number of degrees to rotate the labels.
    
    
    x_axis_label_rotation: -45
    

### `x_axis_datetime_label`

This parameter specifies a format string for the x-axis labels, if they are dates. If `x_axis_scale` is not set to `time`, this does nothing.
    
    
    x_axis_datetime_label: '%b %d'
    
    

See the [Time formatting for charts](/looker/docs/time-formatting-for-charts) documentation page for information on formatting times.

### `x_axis_zoom`

This parameter specifies whether users can [zoom into](/looker/docs/viewing-dashboards#zooming_on_cartesian_charts) the x-axis of the visualization. When `x_axis_zoom` is set to `true`, zooming is available. When `x_axis_zoom` is set to `false`, zooming is not available.

If `x_axis_zoom` is set to `false`, `y_axis_zoom` is disabled.
    
    
    x_axis_zoom: true | false
    
    # default value: true
    

## Y-axis parameters

> **Under construction:** We are working on updating this section of the page. Meanwhile, you can check out the [Scatter chart options](/looker/docs/scatter-options#y_menu_options) documentation page to view equivalent visualization menu options for the y-axis.

The parameters described in this section correspond to the options in the [**Y** section](/looker/docs/scatter-options#y_menu_options) of the visualization editor for scatter charts.

### `y_axis_gridlines`

This parameter determines whether gridlines are extended from the y-axis.
    
    
    y_axis_gridlines: true | false
    
    ## default value: true
    

### `y_axis_reversed`

This parameter sets the direction of the y-axis. When `y_axis_reversed` is set to `false`, values increase going up the axis. When it is set to `true`, values decrease going down the axis.
    
    
    ## y_axis_reversed: true | false
    
    # default value: false
    
    

### `reference_lines`

This parameter specifies an array of values for specifying reference lines and regions. 

See the [Dashboard reference line parameters](/looker/docs/reference/param-lookml-dashboard-reference-line) documentation page for information on setting up reference lines.
    
    
    reference_lines:
       # reference line options
    
    

### `y_axis_zoom`

This parameter specifies whether users can [zoom into](/looker/docs/viewing-dashboards#zooming_on_cartesian_charts) the y-axis of the visualization. When `y_axis_zoom` is set to `true`, zooming is available.

When `y_axis_zoom` is set to `false`, users cannot zoom into smaller portions of the y-axis. However, users may still be able to zoom into smaller portions of the x-axis if the `x_axis_zoom` parameter is set to `true`.

If `x_axis_zoom` is set to `false`, `y_axis_zoom` is disabled.
    
    
    y_axis_zoom: true | false
    
    # default value: true