# https://cloud.google.com/looker/docs/reference/param-lookml-dashboard-google-maps

Depth: 3

**Important:** Charts of `type: looker_google_map` can be viewed only on LookML dashboards with [`preferred_viewer`](/looker/docs/reference/param-lookml-dashboard#preferred_viewer) set to `dashboards-next`.

This page describes the parameters for creating and editing LookML dashboard elements of `type: looker_google_map` with LookML dashboard parameters in a [`dashboard.lkml` file](/looker/docs/other-project-files#dashboard_files).

For information about building a Google Maps chart through the Looker UI, see the [Google Maps chart options](/looker/docs/google-map-options) documentation page. For information about the types of fields required to build an interactive map chart, see the Query parameters section later on this page.

## Example usage

An `N` indicates that a numeric value is required. Single quotation marks indicate descriptive text and should not be included in live code.
    
    
    ## BASIC PARAMETERS
    name: element_name
    title: 'Element Title'
    type: looker_google_map
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
    fields: [view_name.field_name, view_name.field_name, …]
    dimensions: [view_name.field_name, view_name.field_name, …]
    measures: [view_name.field_name, view_name.field_name, …]
    sorts: [view_name.field_name asc | desc, view_name.field_name, …]
    pivots: [view_name.field_name, view_name.field_name, …]
    limit: N
    column_limit: N
    filters:
      view_name.field_name: 'looker filter expression'
    listen:
      dashboard_filter_name: view_name.field_name
    query_timezone: 'specific timezone' | user_timezone
    
    ## PLOT PARAMETERS
    map_plot_mode: points | automagic_heatmap | heatmap | lines | areas
    heatmap_gridlines: true | false
    heatmap_gridlines_empty: true | false
    heatmap_opacity: 'decimal number between 0 and 1'
    
    ## MAP PARAMETERS
    map_tile_provider: light | light_no_labels | dark | dark_no_labels | satellite_streets |
                        satellite | streets | outdoors | traffic_day | traffic_night | minimal
    map_position: fit_data | custom
    map_latitude: 'latitude value'
    map_longitude: 'longitude value'
    map_zoom: N
    map_scale_indicator: off | metric | imperial | metric_imperial
    map_pannable: true | false
    map_zoomable: true | false
    show_view_names: true | false
    show_legend: true | false
    show_region_field: true | false
    draw_map_labels_above_data: true | false
    
    ## POINT PARAMETERS
    map_marker_type: circle | icon | circle_and_icon | none
    map_marker_icon_name: default | airplane | ambulance | anchor | beaker | bell | bolt | briefcase |
                          building | camera | car | checkmark | coffee | comment | envelope | file |
                          gamepad | gavel | gift | glass | headphones | heart | house | key | leaf |
                          microphone | music | person | phone | restaurant | school | shopping_cart |
                          star | suitcase | taxi | tree | trophy | truck | university | wrench
    map_marker_radius_mode: proportional_value | equal_to_value | fixed
    map_marker_radius_fixed: N
    map_marker_radius_min: N
    map_marker_radius_max: N
    map_marker_proportional_scale_type: linear | log
    map_marker_units: meters | pixels
    map_marker_color_mode: value | fixed
    map_marker_color: ['color value']
    
    ## VALUE PARAMETERS
    map_value_colors: ['one or more color values']
    quantize_map_value_colors: true | false
    reverse_map_value_colors: true | false
    map_value_scale_clamp_min: N
    map_value_scale_clamp_max: N
    
    

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
`note` | Starts a section of LookML to define a note for an element. This parameter has subparameters `text`, `state`, and `display`.  
Query Parameters  
`model` | Defines the model to be used for the element's query  
`explore` (for elements) | Defines the Explore to be used for the element's query  
`fields` | Defines the fields to be used for the element's query. This can be used in place of `dimensions` and `measures`.  
`dimensions` | Defines the dimensions to be used for the element's query  
`measures` | Defines the measures to be used for the element's query  
`sorts` | Defines the sorts to be used for the element's query  
`pivots` | Defines the dimensions that should be pivoted to be used for the element's query  
`limit` | Defines the row limit to be used for the element's query  
`column_limit` | Defines the column limit to be used for the element's query  
`filters` (for elements) | Defines the filters that _cannot_ be changed for the element's query  
`listen` | Defines the filters that _can_ be changed for the element's query, if [`filters` (for dashboard)](/looker/docs/reference/param-lookml-dashboard#filters-for-dashboard) have been created  
`query_timezone` | Defines the [time zone](/looker/docs/reference/param-view-timezone-values) that should be used when the query is run  
Plot Parameters  
`map_plot_mode` | Defines how your location data is plotted on an element of `type: looker_map`  
`heatmap_gridlines` | Adds a border around each of the gridlines used for a heatmap element  
`heatmap_gridlines_empty` | For heatmaps with `heatmap_gridlines` set to `true`, displays an outline around map regions that have no associated data  
`heatmap_opacity` | Defines the opacity of the colors used in a heatmap  
Map Parameters  
`map_tile_provider` | Defines the type of background map and whether map labels are displayed  
`map_position` | Defines the center point and zoom level of the visible map  
`map_latitude` | Defines the latitude for a map with `map_position` set to `custom`  
`map_longitude` | Defines the longitude for a map with `map_position` set to `custom`  
`map_zoom` | Defines the zoom for a map with `map_position` set to `custom`  
`map_scale_indicator` | Sets whether a map scale will be shown and the type of units displayed  
`map_pannable` | Sets whether users can reposition the map by dragging it  
`map_zoomable` |  Sets whether users can zoom in and out of the map  
`show_view_names` |  Sets whether to show the view name along with the field name in map tooltips  
`show_legend` | Sets whether a map legend should be displayed in the lower right of the visualization  
`show_region_field` | Sets whether to display the region information in the tooltip of the map  
`draw_map_labels_above_data` | Displays the map's labels above or below the heatmap  
Point Parameters  
`map_marker_type` | Specifies the type of point displayed on the map, for elements with `map_plot_mode` set to `points`, `lines`, or `areas`  
`map_marker_icon_name` | Specifies the type of icon to display on all map markers, for elements with `map_marker_type` set to `icon` or `circle_and_icon`  
`map_marker_radius_mode` | Sets the way the circles are sized, for elements with `map_marker_type` set to `circle` or `circle_and_icon`  
`map_marker_radius_fixed` | Sets a fixed radius to apply to all map markers, for elements with `map_marker_type` set to `circle` or `circle_and_icon` and `map_marker_radius_mode` set to `fixed`  
`map_marker_radius_min` | Sets the minimum radius for circles, for elements with `map_marker_radius_mode` set to `proportional_value`  
`map_marker_radius_max` | Sets the maximum radius for circles, for elements with `map_marker_radius_mode` set to `proportional_value`  
`map_marker_proportional_scale_type` | Specifies whether the circle size is based on a linear or logarithmic scale, for elements with `map_marker_type` set to `circle` or `circle_and_icon` and `map_marker_radius_mode` set to `proportional_value`  
`map_marker_units` | Sets the units used for the radius of a circle to `meters` or `pixels`, for elements with `map_marker_type` set to `circle` or `circle_and_icon`  
`map_marker_color_mode` | Specifies whether the color of the map markers is fixed or the colors are dynamically assigned to markers based on the values of the underlying query  
`map_marker_color` | Specifies a single color to apply to all map markers, for elements with `map_marker_color_mode` set to `fixed`  
Value Parameters  
`map_value_colors` | Specifies the colors of map points, or defines the range of colors to be used if you are color coding according to a measure  
`quantize_map_value_colors` | Changes the color scale from a smooth gradient to only the specific colors you have set  
`reverse_map_value_colors` | Switches the colors that indicate high and low values on the chart, reversing the color gradient  
`map_value_scale_clamp_min` | Sets the minimum value of the color range  
`map_value_scale_clamp_max` | Sets the maximum value of the color range  
  
## Basic parameters

When defining a LookML dashboard element, you must specify values for at least the `name` and `type` basic parameters. Other basic parameters, such as `title`, `height`, and `width`, affect the appearance and position of an element on a dashboard.

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

When defining a LookML dashboard element, you must specify values for at least the `model` and `explore` query parameters.

For LookML dashboard elements of `type: looker_google_map`, you must also specify at least one geographic field as the value of either the `dimensions` or the `fields` parameter. A geographic field can be one of the following:

  * A dimension based on latitude and longitude data, defined in LookML as a dimension of [`type: location`](/looker/docs/reference/param-dimension-filter-parameter-types#location).
  * A dimension with a map layer assigned to it. LookML developers can add a [built-in map layer](/looker/docs/reference/param-field-map-layer-name#built-in_map_layers) or a [custom map layer](/looker/docs/reference/param-model-map-layer) to a measure using the [`map_layer_name`](/looker/docs/reference/param-field-map-layer-name) parameter.
  * A zip code dimension. Zip code regions are based on the 2010 zip code tabulation areas (ZCTAs). If you are visualizing zip codes, there may not be a one-to-one correspondence between zip codes and the ZCTAs used for map visualizations, so it's possible that not all points will be visualized in the map.

You can also use the other query parameters described next to control the way data is displayed in a dashboard element. For more information on the requirements for building an interactive map chart with the Looker UI, see the [Building a Google Maps chart](/looker/docs/google-map-options#building_a_google_maps_chart) section of the **Map chart options** documentation page.

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

### `fields`

The `fields` parameter defines the fields to use for the element query. Use the syntax `view_name.dimension_name` to specify the fields.
    
    
    ## single field example
    - name: orders_by_date
      fields: order.order_date
    
    ## multiple fields example
    - name: orders_by_date
      fields: [order.order_date, order.order_count]
    

If you use the `fields` parameter, you do not need to use the `dimensions` and `measures` parameters.

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
    

### `column_limit`

The `column_limit` parameter defines the column limit that should be used for the element query. The limit applies to the number of columns **after** any pivots are applied.
    
    
    - name: orders_by_date
      column_limit: 100
    

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
    

## Plot parameters

The parameters described in this section correspond to the options in the [**Plot** section](/looker/docs/google-map-options#plot_menu_options) of the visualization editor for map charts.

The parameters you can use with an element of `type: looker_google_map` depend on whether your query includes a dimension of [`type: location`](/looker/docs/reference/param-dimension-filter-parameter-types#location) or has a [map layer](/looker/docs/reference/param-field-map-layer-name) associated with it.

### `map_plot_mode`

The `map_plot_mode` parameter defines the way your data is plotted on a `type: looker_google_map` element that is based on a dimension of `type: location`. This parameter is not available for maps based on a dimension with an associated map layer or for zip code dimensions. The `map_plot_mode` parameter accepts the following values:

  * `points`
  * `automagic_heatmap`
  * `heatmap`
  * `lines`
  * `areas`

#### `points`

Setting `map_plot_mode` to `points` plots each row in the underlying data table as a discrete point on the map.

A dimension of [`type: location`](/looker/docs/reference/param-dimension-filter-parameter-types#location) on its own places points of uniform size and color on the map. Adding a measure to the query lets the points be scaled by color or size using the `map_marker_radius_mode` and `map_marker_color_mode` parameters. 

#### `automagic_heatmap`

Setting `map_plot_mode` to `automagic_heatmap` displays the data in the underlying query as a heatmap grid. It works by dividing the visible map into equal squares and then calculating which values in your data fit into each square. The squares are colored according to a measure that you choose. Zooming this map in or out will prompt Looker to re-calculate the grid, so that the granularity is appropriate to the zoom level.

Your query must include both a dimension of [`type: location`](/looker/docs/reference/param-dimension-filter-parameter-types#location) and a measure for this plot type to work correctly.

#### `heatmap`

Setting `map_plot_mode` to `heatmap` produces a map that can display a large amount of location data with many points clustered closely together. The color intensity and color scale convey the concentration of data points in each area.

Your query must include a dimension of [`type: location`](/looker/docs/reference/param-dimension-filter-parameter-types#location). Optionally, you can add a measure.

#### `lines`

Setting `map_plot_mode` to `lines` takes two dimensions of [`type: location`](/looker/docs/reference/param-dimension-filter-parameter-types#location) from your query and connects them together in the visualization. Adding a measure to your query lets you add color scale to the lines.

#### `areas`

Setting `map_plot_mode` to `areas` takes one dimension of [`type: location`](/looker/docs/reference/param-dimension-filter-parameter-types#location) and connects all the points in the order you've sorted them. This forms boundaries of an area on the map element. Adding a measure to the query lets you format the size and color of the individual location points that make up the boundaries of the area.

### `heatmap_gridlines`

For heatmap elements, setting `heatmap_gridlines` to `true` adds a border around each of the gridlines used for the heatmap. This parameter is available when you're plotting a dimension of [`type: location`](/looker/docs/reference/param-dimension-filter-parameter-types#location) with `map_plot_mode` set to `automagic_heatmap`, or when you're plotting a zip code dimension or a dimension with an associated map layer.
    
    
    heatmap_gridlines: true | false
    
    

### `heatmap_gridlines_empty`

When `heatmap_gridlines` is set to `true` for heatmap elements, and you are plotting data with a defined `map_layer`, setting `heatmap_gridlines_empty` to `true` displays an outline around the map regions that have no associated data.
    
    
    heatmap_gridlines_empty: true | false
    
    

### `heatmap_opacity`

For heatmap elements, you can use `heatmap_opacity` to specify the opacity of the colors used in the heatmap. Specify a decimal number between 0 and 1 as the value for `heatmap_opacity`, where `0` means no color and `1` means totally opaque.
    
    
    heatmap_opacity: 0.5
    
    

## Map parameters

Most of the parameters described in this section correspond to the options in the [**Map menu options** section](/looker/docs/google-map-options#map_menu_options) of the visualization editor for column charts.

### `map_tile_provider`

Available for all maps, the `map_tile_provider` parameter lets you change the type of background map and specify whether map labels (like cities and streets) are displayed.

  * `light`: Subtle, light-colored map designed to provide geographic context while highlighting your data
  * `light_no_labels`: Same as `light`, except the map omits labels such as city names
  * `dark`: Subtle, dark-colored map designed to provide geographic context while highlighting your data
  * `dark_no_labels`: Same as `dark`, except the map omits labels such as city names
  * `satellite_streets`: Map displaying global satellite and aerial imagery
  * `satellite`: Same as `satellite_streets`, except the map omits labels such as city names
  * `streets`: General-purpose map that emphasizes legible styling of road and transit networks
  * `outdoors`: General-purpose map tailored to hiking, biking, and other outdoor uses
  * `traffic_day`: Light-colored map emphasizing transit networks and roads, including current traffic information
  * `traffic_night`: Dark-colored map emphasizing transit networks and roads, including current traffic information
  * `minimal`: Light colored map with no labels or boundary lines

    
    
    map_tile_provider: light | light_no_labels | dark | dark_no_labels | satellite_streets |
                        satellite | streets | outdoors | traffic_day | traffic_night
    
    

### `map_position`

You can use the `map_position` parameter to set the center point and zoom level of the visible map. There are two options for specifying this position:

  * `fit_data`: Automatically centers and zooms the map such that all the data points of your query are visible
  * `custom`: Lets you manually specify latitude, longitude, and zoom level using the `map_latitude`, `map_longitude`, and `map_zoom` parameters

    
    
    map_position: fit_data | custom
    
    

### `map_latitude`

The `map_latitude` parameter specifies the latitude for a map element with `map_position` set to `custom`.
    
    
    map_latitude: -5.804047131379801
    
    

### `map_longitude`

The `map_longitude` parameter specifies the longitude for a map element with `map_position` set to `custom`.
    
    
     map_longitude: 113.34732055664064
    
    

### `map_zoom`

The `map_zoom` parameter lets you specify the zoom level for a map element with `map_position` set to `custom`. Higher numbers create a closer zoom level.
    
    
    map_zoom: 10
    
    

### `map_scale_indicator`

Set to `'off'` by default, the `map_scale_indicator` parameter lets you specify whether a map scale is shown and set the types of units that are displayed.
    
    
    map_scale_indicator: 'off' | metric | imperial | metric_imperial
    
    

### `map_pannable`

The `map_pannable` parameter specifies whether users can reposition the map by dragging it. This option is enabled by default.
    
    
    map_pannable: true | false
    
    

### `map_zoomable`

The `map_zoomable` parameter specifies whether users can zoom in and out of the map element. This option is enabled by default.
    
    
    map_zoomable: true | false
    
    

### `show_view_names`

The `show_view_names` parameter specifies whether to show the view name along with the field name in map tooltips, which are displayed when users click on map data points.
    
    
    show_view_names: true | false
    
    

### `show_legend`

Specify whether a map legend should be displayed in the lower right of the visualization. The legend shows the color scale you are using, if you've added a measure to your visualization.

The `show_legend` parameter is available when the following plot options have been specified:

  * When `map_plot_mode` has been set to `automagic_heatmap`
  * When `map_plot_mode` has been set to `points` and `map_marker_color_mode` is set to `value`

    
    
    show_legend: true | false
    
    

### `show_region_field`

For maps based on a map layer or zip code, the `show_region_field` parameter displays the information in the tooltip of the map. Users can click on a point on the map to see the name of the region.
    
    
    show_region_field: true | false
    
    

### `draw_map_labels_above_data`

For map layer maps or maps based on a zip code dimension, you can use the `draw_map_labels_above_data` parameter to display the map's labels above or below the heatmap. This is especially significant with higher heatmap opacity values. If your heatmap is opaque, the labels will not show unless they are displayed above the data.
    
    
    draw_map_labels_above_data: true | false
    
    

## Point parameters

Point options are not available for maps with `map_plot_mode` set to `automagic_heatmap` or `heatmap`.

### `map_marker_type`

For maps based on a location dimension and with `map_plot_mode` set to `points`, `lines`, or `areas`, the `map_marker_type` parameter defines the type of point displayed on the map element. The `map_marker_type` parameter accepts the following values:

  * `circle`
  * `icon`
  * `circle_and_icon`
  * `none`

The value you specify for `map_marker_type` impacts the parameters that are available for formatting the points displayed on the map.

### `map_marker_icon_name`

If `map_marker_type` is set to `icon` or `circle_and_icon`, you can use the `map_marker_icon_name` parameter to set the type of icon to display on all map markers.
    
    
    map_marker_icon_name: default | airplane | ambulance | anchor | beaker | bell | bolt | briefcase |
                          building | camera | car | checkmark | coffee | comment | envelope | file |
                          gamepad | gavel | gift | glass | headphones | heart | house | key | leaf |
                          microphone | music | person | phone | restaurant | school | shopping_cart |
                          star | suitcase | taxi | tree | trophy | truck | university | wrench
    
    

### `map_marker_radius_mode`

For maps with `map_marker_type` set to `circle` or `circle_and_icon`, you can use the `map_marker_radius_mode` parameter to set the sizes of the circles according to the following options:

  * `proportional_value`: This option adjusts the relative size of the circles according to the measures you've added to your query. You can use the `map_marker_radius_min` and `map_marker_radius_max` parameters with this option to set a minimum radius and a maximum radius for the circles. You can also use the `map_marker_proportional_scale_type` parameter to set whether a linear or a logarithmic scale is used to size the circles.
  * `equal_to_value`: This setting adjust the radius of the circles to the actual measure values in your underlying query.
  * `fixed`: This option lets you set a fixed radius to apply to all map markers using the `map_marker_radius_fixed` parameter. The default value is `500`.

    
    
    map_marker_radius_mode: proportional_value | equal_to_value | fixed
    
    

### `map_marker_radius_fixed`

When `map_marker_radius_mode` is set to `fixed` and `map_marker_type` is set to `circle` or `circle_and_icon`, you can use the `map_marker_radius_fixed` parameter to set a fixed radius that applies to all map markers.
    
    
    map_marker_type: circle
    map_marker_radius_mode: fixed
    map_marker_radius_fixed: 60
    
    

### `map_marker_radius_min`

For maps with `map_marker_type` set to `circle` or `circle_and_icon` and `map_marker_radius_mode` set to `proportional_value`, you can use the `map_marker_radius_min` parameter to define the minimum radius for a circle.
    
    
    map_marker_type: circle
    map_marker_radius_mode: proportional_value
    map_marker_radius_min: 5
    
    

### `map_marker_radius_max`

For maps with `map_marker_type` set to `circle` or `circle_and_icon` and `map_marker_radius_mode` set to `proportional_value`, you can use the `map_marker_radius_max` parameter to define the maximum radius for a circle.
    
    
    map_marker_type: circle
    map_marker_radius_mode: proportional_value
    map_marker_radius_max: 50
    
    

### `map_marker_proportional_scale_type`

For maps with `map_marker_type` set to `circle` or `circle_and_icon` and `map_marker_radius_mode` set to `proportional_value`, you can use the `map_marker_proportional_scale_type` parameter to set the circle size to be based on either a linear or a logarithmic scale. This parameter's value can be either `linear` or `log`.
    
    
    map_marker_radius_mode: proportional_value
    map_marker_proportional_scale_type: linear | log
    
    

### `map_marker_units`

For maps with `map_marker_type` set to `circle` or `circle_and_icon`, you can use the `map_marker_units` parameter to set the units used for the radius of a circle to `meters` or `pixels`.
    
    
    map_marker_units: meters | pixels
    
    

### `map_marker_color_mode`

You can use the `map_marker_color_mode` to set the colors of the map markers:

  * If `map_marker_color_mode` is set to `value`, colors are dynamically assigned to markers based on the values of your underlying query. You can use value parameters to configure the colors in the legend for this option.
  * If `map_marker_color_mode` is set to `fixed`, you can use the `map_marker_color` parameter to set a single color to use for all map markers.

### `map_marker_color`

When `map_marker_color_mode` is set to `fixed`, `map_marker_color_mode` sets a single color to use for all map markers. The color value can be formatted as an RGB hex string, like `2ca6cd`, or as a [CSS color name](https://www.w3schools.com/cssref/css_colors.asp) like `mediumblue`.
    
    
    map_marker_color: [mediumblue]
    
    

## Value parameters

You can use these parameters to configure the colors that will be dynamically assigned to markers based on the values of your underlying query when `map_marker_color_mode` is set to `value`, or for map elements with `map_plot_mode` set to `automagic_heatmap`, `heatmap` `lines`, or `areas`.

### `map_value_colors`

You can use the `map_value_colors` parameter to set the color of map points or, if you are color coding according to a measure, to define the range of colors to be used. You can input a list of hex strings, such as `#2ca6cd`, or [CSS color names](https://www.w3schools.com/cssref/css_colors.asp), such as `mediumblue`. The colors you list first are associated with the lowest values.
    
    
    map_value_colors: [green, mediumblue]
    
    

### `quantize_map_value_colors`

When set to `true`, `quantize_map_value_colors` changes the color scale from a smooth gradient to only the specific colors you have set. This parameter is set to `false` by default.
    
    
    quantize_map_value_colors: true | false
    
    

### `reverse_map_value_colors`

When set to `true`, the `reverse_map_value_colors` parameter switches the colors that indicate high and low values on the chart, reversing the color gradient.
    
    
    reverse_map_value_colors: true | false
    
    

### `map_value_scale_clamp_min`

You can use the `map_value_scale_clamp_min` parameter to set the minimum value for the color range. This lets you color code all points below a certain threshold (the number specified) with the lowest color specified with the `map_value_colors` parameter. By default, the minimum value applied on the legend is the minimum value from your query.
    
    
    map_value_scale_clamp_min: 1000
    
    

### `map_value_scale_clamp_max`

You can use the `map_value_scale_clamp_max` parameter to set the maximum value for the color range, which lets you color code all points above the number specified with the highest color specified with the `map_value_colors` parameter. By default, the maximum value applied on the legend is the maximum value from your query.
    
    
    map_value_scale_clamp_max: 50000