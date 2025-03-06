# https://cloud.google.com/looker/docs/reference/param-lookml-dashboard

Depth: 3

Dashboards can be created in one of two ways. User-defined dashboards are created via the Looker UI, and are described on the [Creating user-defined dashboards](/looker/docs/creating-user-defined-dashboards) documentation page. Dashboards can also be [created using LookML](/looker/docs/building-lookml-dashboards) and their overall settings modified as discussed on this page.

This page describes the LookML dashboard parameters that affect the entire dashboard.

A LookML dashboard also contains _elements_ , which are the data visualizations, text tiles, and buttons on the dashboard. See the [Dashboard element parameters](/looker/docs/reference/param-lookml-dashboard-element) page for links to the reference pages for each individual element type.

## Example usage
    
    
    - dashboard: dashboard_name
      preferred_viewer: dashboards | dashboards-next
      title: "desired dashboard title"
      description: "desired dashboard description"
      enable_viz_full_screen: true | false
      extends: name_of_dashboard_being_extended
      extension: required
      layout: tile | static | grid | newspaper
      rows:
        - elements: [element_name, element_name, ...]
          height: N
      tile_size: N
      width: N
      refresh: N (seconds | minutes | hours | days)
      auto_run: true | false
    
      # DASHBOARD FILTER PARAMETERS
      crossfilter_enabled: true | false
      filters_bar_collapsed: true | false
      filters_location_top: true | false
      filters:
      - name: filter_name
        title: "desired filter title"
        type: field_filter | number_filter | date_filter | string_filter
        model: model_name
        explore: explore_name
        field: view_name.field_name
        default_value: Looker filter expression
        allow_multiple_values: true | false
        required: true | false
        ui_config:
          type: button_group | checkboxes | range_slider | tag_list | radio_buttons |
                button_toggles | dropdown_menu | slider | day_picker | day_range_picker |
                relative_timeframes | advanced
          display: inline | popover | overflow
          options:
            min: N
            max: N
          - value options
        listens_to_filters:
        - filter_name
          field: view_name.field_name
    
      # EMBEDDED DASHBOARD PARAMETERS
      embed_style:
        background_color: "css_color"
        show_title: true | false
        title_color: "css_color"
        show_filters_bar: true | false
        tile_background_color: "css_color"
        tile_text_color: "css_color"
    
      # ELEMENTS PARAMETERS
      elements:
      # One or more element declarations
    

## Parameter definitions

Parameter Name | Description  
---|---  
`dashboard` | Create a dashboard.  
`preferred_viewer` | This parameter is ignored.  
`title` (for dashboard) | Change the way a dashboard name appears to users.  
`description` (for dashboard) | Add a description that can be viewed in the [**Dashboard Details** panel](/looker/docs/viewing-dashboards#dashboard_details) or in a folder set to [list view](/looker/docs/finding-content#list_view).  
`enable_viz_full_screen` | Define whether dashboard viewers can see dashboard tiles in [full-screen and expanded views](/looker/docs/viewing-dashboards#view_options). | `extends` | Base the LookML dashboard on another LookML dashboard.  
`extension` | Require that the dashboard is extended by another dashboard.  
`layout` | Define the way that the dashboard will place elements.  
`rows` | Start a section of LookML to define the elements that should go into each row of a `layout: grid` dashboard.  
`elements` (for rows) | Define the elements that should go into a row of a `layout: grid` dashboard.  
`height` (for rows) | Define the height of a row for a `layout: grid` dashboard.  
`tile_size` | Define the size of a tile for a `layout: tile` dashboard.  
`width` (for dashboard) | Define the width of the dashboard for a `layout: static` dashboard.  
`refresh` (for dashboard) | Set the interval on which dashboard elements will automatically refresh.  
`auto_run` | Determine whether dashboards run automatically when initially opened or reloaded.  
Filter Parameters  
`crossfilter_enabled` | Enable or disable [cross-filtering](/looker/docs/cross-filtering-dashboards) for a dashboard.  
`filters_bar_collapsed` |  ADDED 21.16  Set the dashboard filter bar as default [collapsed or expanded](/looker/docs/editing-user-defined-dashboards#default_filters_view) for a dashboard.  
`filters_location_top` |  ADDED 22.8  Set the dashboard filter bar location as [top or right](/looker/docs/editing-user-defined-dashboards#filters_location) for a dashboard.  
`filters` (for dashboard) | Start a section of LookML to define dashboard filters.  
`name` (for filters) | Create a filter.  
`title` (for filters) | Change the way a filter name appears to users.  
`type` (for filters) | Determine the type of filter to be used.  
`default_value` | Set a default value for a filter, if desired.  
`allow_multiple_values` | Limit users to a single filter value.  
`required` | Require that users enter a filter value to run the dashboard.  
`ui_config` | Configure the filter controls that are available when users view a LookML dashboard. Has subparameters `type`, `display`, and `options`.  
`model` (for filters) | Specify the model that contains the underlying field of a `type: field_filter` filter.  
`explore` (for filters) | Specify the Explore that contains the underlying field of a `type: field_filter` filter.  
`field` | Specify the underlying field of a `type: field_filter` filter.  
`listens_to_filters` | Narrow suggestions for dashboard filters of `field_filter` based on what the user enters for another dashboard filters of `type: field_filter`.   
Embedded Dashboard Parameters  
`embed_style` | Start a section of LookML to define [embedded](/looker/docs/single-sign-on-embedding) dashboard customizations.  
`background_color` | Set a background color of an embedded dashboard.  
`show_title` | Specify whether the dashboard title is visible on an embedded dashboard.  
`title_color` | Set the color of the title of an embedded dashboard.  
`show_filters_bar` | Specify whether the filters bar is visible on an embedded dashboard.  
`tile_background_color` | Set the tile background color of an embedded dashboard.  
`tile_text_color` | Set the tile text color of an embedded dashboard.  
Element Parameters  
`elements` (for dashboard) | Start a section of LookML to define dashboard elements.  
  
## `dashboard`

The `dashboard` parameter declares a new dashboard and specifies a name for the dashboard. The maximum number of characters is 255; and allowed characters are letters (A-Z), numbers (0-9), dashes (-), and underscores (_). It is typically best practice to place each LookML dashboard in its own LookML file, but it is possible to declare multiple dashboards in a single file.
    
    
    - dashboard: sales_overview
    

To display anything, a dashboard requires at least one element to be added via the `elements` parameter.

**Note:** If you change the value of a LookML dashboard's `dashboard` parameter for a dashboard that has been [moved out of the **LookML dashboards** folder](/looker/docs/building-lookml-dashboards#moving_lookml_dashboards_outside_of_the_lookml_dashboards_folder), the LookML dashboard will automatically move back into the **LookML dashboards** folder.

## `preferred_viewer`

**Important:** This parameter is ignored.

Before legacy dashboard deprecation in Looker 23.6, the `preferred_viewer` parameter let you choose the format for viewing and downloading a dashboard as either Looker's default [dashboard experience](/looker/docs/viewing-dashboards) or as a legacy dashboard.

## `title` (for dashboard)

> This section refers to the `title` parameter that is part of a dashboard.
> 
> `title` can also be used as part of a dashboard filter, described on the [`title` (for filters)](/looker/docs/reference/param-lookml-dashboard#title-for-filters) section on this page.
> 
> `title` can also be used as part of any dashboard element. A representative example of its usage is provided on the [column chart elements](/looker/docs/reference/param-lookml-dashboard-column-chart#title) documentation page.

The `title` parameter lets you change how a dashboard name will appear to users in [folders](/looker/docs/organizing-spaces) and at the top of the dashboard. If not specified, the title defaults to the name of the dashboard. The title text can be [localized](/looker/docs/model-localization).

Consider this example:
    
    
    - dashboard: sales_overview
      title: "1) Sales Overview"
    

If you did this, instead of the dashboard appearing as **Sales Overview** , it would appear as **1) Sales Overview**.

## `description` (for dashboard)

> This section refers to the `description` parameter that is part of a dashboard.
> 
> `description` can also be used as part of an Explore, as described on the [`description` (for Explores)](/looker/docs/reference/param-explore-description) parameter documentation page.
> 
> `description` can also be used as part of a field, as described on the [`description` (for fields)](/looker/docs/reference/param-field-description) parameter documentation page.

The `description` parameter lets you add a description to a LookML dashboard.

The contents of the `description` parameter will appear in the **Description** text box of the [**Dashboard Details** panel](/looker/docs/viewing-dashboards#dashboard_details) of a LookML dashboard.

The description is displayed under the dashboard title in the [lists of dashboards](/looker/docs/finding-content#navigating_to_dashboards_and_looks_from_folders) when viewed in a folder set to [list view](/looker/docs/finding-content#list_view). If a description is not specified, the list displays only the dashboard title.

The description text can be [localized](/looker/docs/model-localization).

## `enable_viz_full_screen`

This parameter only takes effect when the **Full Screen Visualizations** [Labs feature](/looker/docs/admin-panel-general-labs#full_screen_visualizations) is enabled by a Looker admin. The **Full Screen Visualization** Labs feature is enabled by default.

The `enable_viz_full_screen` parameter lets you set whether dashboard viewers can see dashboard tiles in [full-screen and expanded views](/looker/docs/viewing-dashboards#view_options). It is equivalent to the [**Allow full-screen mode for visualizations**](/looker/docs/editing-user-defined-dashboards#allow_full-screen_mode_for_visualizations) dashboard setting.

This parameter accepts the values `true` (full-screen and expanded views available) and `false` (full-screen and expanded views not available). The default value is `true`.

## `extends`

As described on the [Reusing codes with extends](/looker/docs/reusing-code-with-extends#extending_a_lookml_dashboard) documentation page, the `extends` parameter lets you base one LookML dashboard on another LookML dashboard, possibly adding or overriding some settings. The `extends` parameter accepts the name of another LookML dashboard.

> When extending an object, be aware that localization rules apply to your extensions as well. If you are extending an object and then defining new labels or descriptions, you should provide localization definitions in your project's locale strings files. See the [Localizing your LookML model](/looker/docs/model-localization#understanding_how_localization_rules_apply_to_extended_objects) documentation page for more information.

## `extension`

As described on the [Reusing code with extends](/looker/docs/reusing-code-with-extends#requiring_extension) documentation page, the `extension` parameter indicates that the dashboard _must_ be extended by another dashboard. This dashboard is never visible to other users but can be used as a template to create other dashboards that are visible to other users. The `extension` parameter only accepts the value `required`. If the `extension` parameter is not included, extension is not required for the dashboard.

## `layout`

The `layout` parameter sets the layout method that Looker will use when positioning dashboard elements. It accepts the following values:

  * **`newspaper`** : Dashboard elements will appear in a 24-column grid. The default size for an element is a width of 8 columns and a height of 6 rows. Elements are configurable along this grid, specified by the `width`, `height`, `row`, and `col` [element parameters](/looker/docs/reference/param-lookml-dashboard-element). This layout option is used when [a user-defined dashboard is converted to a LookML dashboard](/looker/docs/building-lookml-dashboards#creating_a_lookml_copy_of_a_user-defined_dashboard), as well as being the default layout when a new LookML dashboard is created through the Looker IDE. In addition, `newspaper` and `grid` are the only layouts that support [conversion from a LookML dashboard to a user-defined dashboard](/looker/docs/converting-lookml-to-user-defined-dashboard).

  * **`grid`** : Dashboard elements will appear with dynamic widths, which are based on a set of rows that you define with the `rows` parameter and its subparameters `elements` and `height`. `newspaper` and `grid` are the only layouts that support [conversion from a LookML dashboard to a user-defined dashboard](/looker/docs/converting-lookml-to-user-defined-dashboard).

  * **`static`** : Dashboard elements will appear in the order in which they are listed in the LookML file. Each dashboard element must be positioned manually by using the `top` and `left` parameters. These parameters apply to all element types, and details about their usage appear on the [documentation pages](/looker/docs/reference/param-lookml-dashboard-element) for each individual visualization type. For representative examples of how `top` and `left` work, see the [Column chart parameters for LookML dashboards](/looker/docs/reference/param-lookml-dashboard-column-chart#top) documentation page. `static` does not support [conversion from a LookML dashboard to a user-defined dashboard](/looker/docs/converting-lookml-to-user-defined-dashboard).

  * **`tile`** : Dashboard elements will appear in the order in which they are listed in the LookML file. The width of the dashboard is dynamic, and is based on the width of the browser. The dashboard elements will dynamically position themselves within the browser to fill the available space. `tile` does not support [conversion from a LookML dashboard to a user-defined dashboard](/looker/docs/converting-lookml-to-user-defined-dashboard).

## `rows`

For `layout: grid` dashboards, the `rows` parameter starts the section of LookML where you define which elements should go into which rows, as well as the height of each row. Within each row, each element has the same width. If you don't list an element in this section it won't appear on the dashboard.
    
    
    - dashboard: sales_overview
      layout: grid
      rows:
        - elements: [element_name, element_name, ...]
          height: 200
        - elements: [element_name, element_name, ...]
          height: 300
    

### `elements`

The `elements` parameter takes a list of dashboard element names, separated by commas. Each `elements` declaration creates a new row in the dashboard. The elements that are placed into a row will all have the same width. So, if you place 2 elements in a row, they will each take 50% of the available space. If you place 4 elements into a row, they will each take 25% of the available space, and so on.

### `height`

The `height` parameter defines the height of a row in pixels. The default value is 300.

## `tile_size`

For `layout: tile` and `layout: static` dashboards, the unit that is used to size and position elements is tile size. You define `tile_size` in pixels, and the default value is 160. For example:
    
    
    - dashboard: sales_overview
      layout: tile
      tile_size: 100
    

In this situation, a dashboard element with `height: 5` and `width: 3` will be 500 pixels high, and 300 pixels wide. The `height` and `width` parameters apply to all element types, and details about their usage appear on the [documentation pages](/looker/docs/reference/param-lookml-dashboard-element) for each individual visualization type. For a representative example of how `height` and `width` work, see the [Column chart parameters for LookML dashboards](/looker/docs/reference/param-lookml-dashboard-column-chart#height) documentation page.

## `width`

> This section refers to the `width` parameter that is part of a dashboard.
> 
> `width` can also be used as part of a dashboard element. A representative example its usage is provided on the documentation page for [column chart elements](/looker/docs/reference/param-lookml-dashboard-column-chart#width).

For `layout: static` dashboards, the `width` parameter defines the total dashboard width that you plan to use in pixels. The `width` parameter will _not_ restrict the dashboard to a certain size if you define too large of an element, or too many elements in a row. Rather, the `width` setting helps to keep the dashboard centered on the screen. If you do not set a width, the default is 1200.
    
    
    - dashboard: sales_overview
      layout: static
      width: 800
    

## `refresh`

> This section refers to the `refresh` parameter that is part of a dashboard.
> 
> `refresh` can also be used as part of a dashboard element. A representative example of its usage is provided on the documentation page for [column chart elements](/looker/docs/reference/param-lookml-dashboard-column-chart#refresh).

The `refresh` parameter allows a dashboard to automatically reload on some periodic basis, thereby retrieving fresh data. This is often helpful in settings where a dashboard is constantly displayed, such as on an office TV. Note that the dashboard must be open in a browser window for this parameter to have an effect. This setting does not run in the background to "pre-warm" the dashboard cache.

The refresh rate can be any number (without decimals) of seconds, minutes, hours or days. For example:
    
    
    - dashboard: sales_overview
      refresh: 2 hours
    

Use caution when setting short refresh intervals. Since dashboards can contain many queries, some of which may be resource intensive, certain dashboards may strain your database more than desired.

## `auto_run`

The `auto_run` parameter determines whether a dashboard will run when it is initially opened or reloaded. The default value is `true`. When this parameter is set to `false`, users will need to press a **Run** button to load the dashboard. For example, a dashboard like this will automatically run when opened:
    
    
    - dashboard: sales_overview
      auto_run: true
    

Regardless of the `auto_run` setting, users must always click a **Run** button after changing filter values. This helps to prevent unwanted reloads when a user pauses during a filter change or wants to change multiple filters at the same time.

## `crossfilter_enabled`

The `crossfilter_enabled` parameter lets you [turn cross-filters on or off](/looker/docs/cross-filtering-dashboards#enabling_cross-filtering_for_individual_dashboards) for a dashboard. When this parameter is set to `true`, dashboard viewers can [create cross-filters](/looker/docs/cross-filtering-dashboards#creating_cross-filters_on_dashboards) on the dashboard by clicking certain data points.
    
    
    - dashboard: sales_data
      crossfilter_enabled: true
    

## `filters_bar_collapsed`

The `filters_bar_collapsed` parameter lets you set the dashboard filter bar as default [collapsed or expanded](/looker/docs/editing-user-defined-dashboards#default_filters_view) for a dashboard. When this parameter is set to `true`, the filter bar is default collapsed. Dashboard viewers can expand the filter bar by clicking the [filters icon](/looker/docs/viewing-dashboards#filters_icon). The default for this setting is `false`.
    
    
    - dashboard: sales_data
      filters_bar_collapsed: true
    

## `filters_location_top`

The `filters_location_top` parameter lets you place the dashboard filter bar at the [top or the right](/looker/docs/editing-user-defined-dashboards#filters_location) for a dashboard. When this parameter is set to `true`, the filter bar appears at the top of the dashboard; when it is set to `false`, the filter bar appears at the right of the dashboard. The default for this setting is `true`.
    
    
    - dashboard: sales_data
      filters_location_top: false
    

## `filters`

> This section refers to the `filters` parameter that is part of a dashboard.
> 
> `filters` can also be used as part of a dashboard element. A representative example of its usage is provided on the documentation page for [column chart elements](/looker/docs/reference/param-lookml-dashboard-column-chart#filters).
> 
> `filters` can also be used as part of a measure, described on the [`filters`](/looker/docs/reference/param-field-filters) parameter documentation page.

The `filters` parameter starts the section of LookML where you define dashboard filters. Filters appear at the top of the dashboard and let users change the data behind dashboard elements.

For a filter to impact an element, the element must be set up to "listen" for that filter, using the `listen` parameter. This parameter applies to all element types except [`type: text`](/looker/docs/reference/param-lookml-dashboard-text-tile) and [`type: button`](/looker/docs/reference/param-lookml-dashboard-button). For a representative example of how `listen` works, see the [Column chart parameters for LookML dashboards](/looker/docs/reference/param-lookml-dashboard-column-chart#listen) documentation page.

**Note:** For [dashboard elements that use the `merged_queries` parameter](/looker/docs/reference/param-lookml-dashboard-column-chart#merged_queries), each source query can listen to one or more dashboard filters. Within a merged query definition, you can use the `listen` parameter to define filter logic for each source query independently, regardless of the number of source queries in your merged results element. If a query doesn't have a `listen` parameter, then it won't be affected by any dashboard filters.

When filters are applied to an element in this manner, it's important for the filter type to match the dimension or measure type that is listening for the filter (see [Building LookML dashboards](/looker/docs/building-lookml-dashboards#filters) for more details). Filters have the following form:
    
    
    filters:
    - name: filter_name
      title: "desired filter title"
      type: field_filter | number_filter | date_filter | string_filter
      model: model_name
      explore: explore_name
      field: view_name.field_name
      default_value: Looker filter expression
      allow_multiple_values: true | false
      required: true | false
      listens_to_filters:
      - filter_name
        field: view_name.field_name
    
    

### `name`

> This section refers to the `name` parameter that is part of a [dashboard filter](/looker/docs/reference/param-lookml-dashboard#filters-for-dashboard).
> 
> `name` can also be used as part of a dashboard element. A representative example of its usage is provided on the documentation page for [column chart elements](/looker/docs/reference/param-lookml-dashboard-column-chart#name).

Each `name` declaration creates a new dashboard filter, and assigns a name to it. The name will be referenced in the `listen` parameter of elements that should be impacted by the filter. The `listen` parameter applies to all element types besides [`type: text`](/looker/docs/reference/param-lookml-dashboard-text-tile), and details about its usage appear on the [documentation pages](/looker/docs/reference/param-lookml-dashboard-element) for each individual visualization type. For a representative example of how `listen` works, see the [Column chart parameters for LookML dashboards](/looker/docs/reference/param-lookml-dashboard-column-chart#listen) documentation page.
    
    
    filters:
    - name: order_date
    

### `title` (for filters)

> This section refers to the `title` parameter that is part of a [dashboard filter](/looker/docs/reference/param-lookml-dashboard#filters-for-dashboard).
> 
> `title` can also be used as part of a dashboard, as described in the [`title` (for dashboard)](/looker/docs/reference/param-lookml-dashboard#title-for-dashboard) section on this page.
> 
> `title` can also be used as part of a dashboard element. A representative example of its usage is provided on the [Column chart parameters for LookML dashboards](/looker/docs/reference/param-lookml-dashboard-column-chart#title) documentation page.

The `title` parameter lets you change how a filter name will appear to users at the top of a dashboard. If not specified, the title defaults to the name of the filter.

Consider this example:
    
    
    filters:
    - name: order_date
      title: "Order Date(s)"
    

If you did this, instead of the filter appearing as **Order Date** , it would appear as **Order Date(s)**.

### `type`

> This section refers to the `type` parameter that is part of a [dashboard filter](/looker/docs/reference/param-lookml-dashboard#filters-for-dashboard).
> 
> `type` can also be used as part of a dashboard element, described on the [`type` (for LookML dashboards)](/looker/docs/reference/param-lookml-dashboard-type) parameter documentation page.
> 
> `type` can also be used as part of a join, described on the [`type`](/looker/docs/reference/param-explore-join-type) parameter parameter documentation page.
> 
> `type` can also be used as part of a dimension, described on the [Dimension, filter, and parameter types](/looker/docs/reference/param-dimension-filter-parameter-types) documentation page.
> 
> `type` can also be used as part of a measure, described on the [Measure types](/looker/docs/reference/param-measure-types) documentation page.

The `type` parameter specifies the type of input that will be placed in the filter. While any type of input (such as a date) could be written into the `type: string_filter` filter, being more specific provides a more tailored filter widget to the user. The 4 types of filter are:

  * **`field_filter`** : Should generally be your default choice, when you can specify an underlying dimension or measure. Using `type: field_filter` and associating the filter with a `type:string` field causes the filter to suggest possible filter values.
  * **`number_filter`** : Lets the user input a number/integer value or expression.
  * **`date_filter`** : Lets the user input a date value or expression.
  * **`string_filter`** : Lets the user input freeform text.

#### `field_filter`

Suggests options to choose from, changes its presentation to users based on the underlying field you specify.

This should be your go-to filter type in situations where you want to make suggestions to users as they interact with the filter. The dimension from which suggestions will be pulled is defined by using the `explore` and `field` parameters, and must be a field of [`type: string`](/looker/docs/reference/param-dimension-filter-parameter-types#string) to generate filter suggestions.

Please note that suggestions may not work if the field comes from a derived table, if [`sql_always_where`](/looker/docs/reference/param-explore-sql-always-where) is used on the Explore, or if the field is a measure.
    
    
    filters:
    - name: order_date
      type: field_filter
      explore: orders
      field: orders.order_date  # must be of the form view_name.dimension_name
    

#### `number_filter`

Does not make suggestions, lets the user enter an integer/number value or expression.
    
    
    filters:
    - name: order_value
      type: number_filter
    

#### `date_filter`

Does not make suggestions, lets the user enter a date value or expression.
    
    
    filters:
    - name: order_date
      type: date_filter
    

#### `string_filter`

Does not make suggestions, lets the user enter freeform text.
    
    
    filters:
    - name: customer_name
      type: string_filter
    

### `default_value`

The `default_value` parameter lets you specify a default value to use for a filter. This value can be helpful to users by suggesting a reasonable starting point.

Make sure to match the default value with the type of filter being used. For example:
    
    
    filters:
    - name: order_value
      type: number_filter
      default_value: "50 to 100"
    
    - name: order_date
      type: date_filter
      default_value: "last 30 days"
    
    - name: customer_name
      type: string_filter
      default_value: "John Doe"
    

You can use filter expressions to create default values. The [Looker filter expressions](/looker/docs/filter-expressions) documentation page describes this in more detail.

When you use both the `default_value` and the `ui_config` parameters, filter expressions must be compatible with the value given to the `type` subparameter of `ui_config` and the data types that support the `type` value.

You can also use the [`_localization`](/looker/docs/model-localization#filter_localization_example) and [`_user_attributes`](/looker/docs/liquid-variable-reference#user_attributes) Liquid variables for flexible default filter values.

### `allow_multiple_values`

The `allow_multiple_values` parameter lets you control whether users can select a single filter value or multiple filter values. When this parameter is set to `true` (the default), users can select multiple values for the filter. When this parameter is set to `false`, users are able to select only a single filter value.

For example:
    
    
    filters:
    - name: Order ID
      title: Order ID
      type: field_filter
      allow_multiple_values: true
      required: false
      model: thelookstore
      explore: orders
      field: orders.id
    

### `required`

The `required` parameter lets you require that users provide a value for the filter in order to run the dashboard. By default, filters do not require values. If a filter that does not require a value and is left blank, the data simply isn't restricted by the filter field. If a filter that does require a value and is left blank, the dashboard won't run.
    
    
    filters:
      - name: State
        title: State
        type: field_filter
        required: true
    

### `ui_config`

The `ui_config` subparameter of `filters` lets you configure filter settings for a LookML dashboard. These settings include the types of filter controls used, the placement of filter controls, and possible filter values.

For example:
    
    
      filters:
      - name: City
        title: City
        type: field_filter
        default_value: San Francisco
        allow_multiple_values: true
        required: false
        ui_config:
          type: button_group
          display: inline
          options:
          - San Francisco
          - New York
          - Tokyo
        model: thelook
        explore: order_items
        field: users.city
    
    

See the [Adding and editing user-defined dashboard filters](/looker/docs/filters-user-defined-dashboards) documentation page for more information about configuring filters with the UI.

#### `type`

The `type` subparameter of `ui_config` lets you specify the [types of filter controls](/looker/docs/filters-user-defined-dashboards#dashboard_\(beta\)_filter_controls) that are shown.

Depending on the value you enter for `type`, filter controls can be single selection or multiple selection.

> The values that `type` supports depend on the LookML data [`type`](/looker/docs/reference/param-dimension-filter-parameter-types) that is assigned to the field that you're filtering on.

STR = Compatible with the [`string`](/looker/docs/reference/param-dimension-filter-parameter-types#string) data type  |  DIST = Compatible with the [`distance`](/looker/docs/reference/param-dimension-filter-parameter-types#distance) data type   
---|---  
NUM = Compatible with the [`number`](/looker/docs/reference/param-dimension-filter-parameter-types#number) data type and numeric measures  |  DUR = Compatible with the [`duration`](/looker/docs/reference/param-dimension-filter-parameter-types#duration) data type   
TIER = Compatible with the [`tier`](/looker/docs/reference/param-dimension-filter-parameter-types#tier) data type  |  D&T = Compatible with most [date and time](/looker/docs/reference/param-dimension-filter-parameter-types#time) data types   
ZIP = Compatible with the [`zipcode`](/looker/docs/reference/param-dimension-filter-parameter-types#zipcode) data type  |  LOC = Compatible with the [`location`](/looker/docs/reference/param-dimension-filter-parameter-types#location) data type   
Y/N = Compatible with the [`yesno`](/looker/docs/reference/param-dimension-filter-parameter-types#yesno) data type  |  PAR = Compatible with the [`parameter`](/looker/docs/reference/param-field-parameter) parameter   
Value| Description| Supported Data Types  
---|---|---  
Multiple Selection  
`button_group`|  The filter shows a group of buttons, with one button for each value specified with the `options` parameter.|  STR NUM TIER ZIP Y/N DIST DUR  
`checkboxes`|  The filter shows checkboxes, with one checkbox for each value specified with the `options` parameter.|  STR NUM TIER ZIP Y/N DIST DUR  
`tag_list`|  The filter shows a drop-down listing each possible value specifed using the `options` parameter.|  STR NUM TIER ZIP DIST DUR  
`range_slider`|  For numeric fields, the filter shows a slider that lets users set a range of numbers as the filter's value. The `min` and `max` subparameters of `options` are used to specify the minimum and maximum possible values for the filter, and the default range can be specified using the `default_value` parameter.|  NUM DIST DUR  
Single Selection  
`button_toggles`|  The filter shows a group of buttons, with one button for each value specified with the `options` parameter.|  STR NUM TIER ZIP Y/N DIST DUR PAR  
`radio_buttons`|  The filter displays radio buttons, with a button for **any value** and one button for each value specified with the `options` parameter.|  STR NUM TIER ZIP Y/N DIST DUR PAR  
`dropdown_menu`|  The filter shows a drop-down menu listing each possible value specified using the `options` parameter. The drop-down also provides users with the option to select **Any value**.|  STR NUM TIER ZIP Y/N DIST DUR PAR  
`slider`|  For numeric fields, the filter shows a slider that lets users choose a filter by sliding between the minimum and maximum possible values, which are specified using the `options` parameter.|  NUM DIST DUR  
Dates and Times  
`day_picker`|  The filter lets users choose a particular date to filter on.|  D&T The single day control can be used with most [timeframes](/looker/docs/reference/param-field-dimension-group#timeframe_options) and [time-based types](/looker/docs/reference/param-dimension-filter-parameter-types#available_time-based_types), but viewers can only select single dates with this type of control.  
`day_range_picker`|  The filter lets users select a start date and end date to filter on a range of dates.|  D&T The date range control can be used with most [timeframes](/looker/docs/reference/param-field-dimension-group#timeframe_options) and [time-based types](/looker/docs/reference/param-dimension-filter-parameter-types#available_time-based_types), but viewers can only select date ranges with this type of control.  
`date_time_range_input`|  The filter lets the user filter on a range of dates and times.|  D&T The date and time range control can be used with most [time-based types](/looker/docs/reference/param-dimension-filter-parameter-types#available_time-based_types), and viewers must select both date and time options with this type of control.  
`relative_timeframes`|  The filter lets the user filter on a custom range of dates or to choose from timeframe presets like **Today** , **Last 7 Days** , **Last 90 Days** , and so on.|  D&T The timeframe control can be used with most [timeframes](/looker/docs/reference/param-field-dimension-group#timeframe_options) and [time-based types](/looker/docs/reference/param-dimension-filter-parameter-types#available_time-based_types), but viewers cannot select time options with this type of control.  
Other  
`advanced`| The filter presents options for applying one or more [filters](/looker/docs/filtering-and-limiting#basic_filters) or [advanced matches](/looker/docs/filtering-and-limiting#advanced_matches_filters) filters.See the [Using advanced controls](/looker/docs/filters-user-defined-dashboards#using_advanced_controls) section on this page to learn more about advanced controls. |  STR NUM TIER ZIP Y/N D&T DIST DUR LOC PAR  
  
**Note:** Some [timeframes](/looker/docs/reference/param-field-dimension-group#timeframe_options) and [time-based types](/looker/docs/reference/param-dimension-filter-parameter-types#available_time-based_types) are interpreted as different data types when Looker creates control options for them. Two examples are the [`yesno` timeframe](/looker/docs/reference/param-field-dimension-group#yesno), which is interpreted as a [`yesno` data type](/looker/docs/reference/param-dimension-filter-parameter-types#yesno) and therefore supports the values that are supported by the `yesno` type; and the [`hour_of_day` timeframe](/looker/docs/reference/param-field-dimension-group#hour_of_day), which is interpreted as a [`number` data type](/looker/docs/reference/param-dimension-filter-parameter-types#number) and therefore supports the values that are supported by the `number` type.

#### `display`

You can can use the `display` subparameter of `ui_config` to set the position of a dashboard filter. You can position a filter by assigning one of the following values to `display`:

  * `inline`: The filter is displayed directly in the top bar of the dashboard.
  * `popover`: A summary value appears in the top bar of the dashboard; click the value to see the full filter.
  * `overflow`: A **More** button appears in the top bar of the dashboard with a numeric indicator of how many overflow filters there are; users can click the button to see the overflow filters and their values.

Some filter types can only be displayed in certain ways. For example, filters of `type: day_picker` can only be displayed as `inline` or `overflow`. If you give a filter a `display` value that is not valid for that `type`, the filter will display as either `inline` or `popover`, whichever is valid. To learn more, see the [Adding and editing user-defined dashboard filters](/looker/docs/filters-user-defined-dashboards#displaying_dashboard_\(beta\)_filters) documentation page.

For information about positioning dashboard filters using the UI, see the [Adding and editing user-defined filters](/looker/docs/filters-user-defined-dashboards#displaying_dashboard_\(beta\)_filters) documentation page.

#### `options`

The optional `options` subparameter of `ui_config` lets you specify the [values](/looker/docs/filters-user-defined-dashboards#values) that a user can choose from to [temporarily update dashboard filter values](/looker/docs/viewing-dashboards#temporarily_changing_filter_values_on_dashboards) when users view a LookML dashboard. If you do not specify any values for `options`, Looker pulls the first values from the database.

For example, you can set `San Francisco`, `New York`, and `Tokyo` as the possible values for a filter on the `users.city` field as follows:
    
    
    ui_config:
      type: button_group
      display: inline
      options:
      - San Francisco
      - New York
      - Tokyo
    
    

If the `type` subparameter of `ui_config` is set to `range_slider` or `slider`, you can use the `min` and `max` subparameters of `options`:

  * `min`: Set the minimum possible value for a filter.
  * `max`: Set the maximum possible value for a filter.

For example:
    
    
    ui_config:
      type: range_slider
      display: inline
      options:
        min: 0
        max: 500
    
    

### `model`

For dashboard filters of `type: field_filter`, you need to define a model from which the filter will pull suggestions. The `model` parameter specifies which model contains the field you want to use.
    
    
    filters:
    - name: State
      title: State
      type: field_filter
      default_value: California
      model: thelookstore
      explore: users
      field: users.state
    

### `explore`

> This section refers to the `explore` parameter that is part of a [dashboard filter](/looker/docs/reference/param-lookml-dashboard#filters-for-dashboard).
> 
> `explore` can also be used as part of a model, described on the [`explore`](/looker/docs/reference/param-explore-explore) parameter documentation page.
> 
> `explore` can also be used as part of a dashboard element. A representative example of its usage is provided on the documentation page for [column chart elements](/looker/docs/reference/param-lookml-dashboard-column-chart#explore).

For dashboard filters of `type: field_filter`, you need to define a field from which the filter will pull suggestions. The `explore` parameter specifies which Explore contains the field you want to use.
    
    
    filters:
    - name: order_date
      type: field_filter
      explore: orders
      field: orders.order_date
    

### `field`

For dashboard filters of `type: field_filter`, you need to define a field from which the filter will pull suggestions. The `field` parameter specifies which field you want to use. It is important to use the fully scoped field name. In other words, use `view_name.field_name`, not just `field_name`.
    
    
    filters:
    - name: order_date
      type: field_filter
      explore: orders
      field: orders.order_date
    

### `listens_to_filters`

For dashboard filters of `type: field_filter`, you can narrow suggestions for the filter based on what the user enters for another filter of `type: field_filter`.

In the following example, the suggestions provided for the `State` filter will be based on the values from the `Order ID` filter. Whatever values are selected for the `Order ID` filter will have associated `users.state` values, and those values will be suggested values for the `State` filter. See the [Adding and editing user-defined dashboard filters](/looker/docs/filters-user-defined-dashboards#setting_up_linked_filters) documentation page for more information.
    
    
    filters:
    - name: State
      title: State
      type: field_filter
      model: thelookstore
      explore: users
      listens_to_filters:
      - Order ID
      field: users.state
    

## `embed_style`

The `embed_style` parameter starts the section of LookML where you customize the appearance of an [embedded](/looker/docs/single-sign-on-embedding) dashboard. `embed_style` and its associated parameters are supported only on embedded dashboards and are ignored if the dashboard is not embedded.

After you make changes to `embed_style`, you must [deploy your LookML to production](/looker/docs/version-control-and-deploying-changes#deploying_to_production) in order to see your `embed_style` settings reflected in the embedded LookML dashboard.

For the following embedded dashboard attributes that specify a color, the color value can be a hex string like `#2ca6cd` or a [CSS named color string](https://www.w3schools.com/cssref/css_colors.asp) like `mediumblue`.

Embedded dashboard customizations have the following form:
    
    
    embed_style:
      background_color: "css_color"
      show_title: true | false
      title_color: "css_color"
      show_filters_bar: true | false
      tile_background_color: "css_color"
      tile_text_color: "css_color"
    

### `background_color`

Sets the color of the background of an embedded dashboard.
    
    
    embed_style:
      background_color: "#ffffff"
    

### `show_title`

Specifies whether the embedded dashboard title is visible to users.
    
    
    embed_style:
      show_title: false
    

### `title_color`

Sets the color of the title of an embedded dashboard.
    
    
    embed_style:
      title_color: "#008000"
    

### `show_filters_bar`

Specifies whether the embedded dashboard filters are visible to users.

> This parameter affects only the cosmetic appearance of the dashboard, not a user's ability to access data. Hiding the filters bar does NOT prevent users from changing filters by other means. For information on how to set up secure data access control policies, see the [Access control and permission management](/looker/docs/access-control-and-permission-management#control_user_access_to_data) documentation page.
    
    
    embed_style:
      show_filters_bar: true
    

### `tile_background_color`

Sets the color of the background of all tiles on an embedded dashboard.
    
    
    embed_style:
      tile_background_color: "lightyellow"
    

### `tile_text_color`

Sets the color of text on all tiles on an embedded dashboard.
    
    
    embed_style:
      tile_text_color: "crimson"
    

## `elements`

> This section refers to the `elements` parameter that is part of a `dashboard`.
> 
> `elements` can also be used as part of a dashboard row, described on the `elements` for rows section on this page.

The `elements` parameter starts the section of LookML where you define the elements that will make up a dashboard. There are many parameters that can define the appearance of a dashboard element. They are described in more detail on the [Dashboard element parameters](/looker/docs/reference/param-lookml-dashboard-element) page.
    
    
    - dashboard: sales_overview
      layout: tile
      elements:
      - name: order_count
        type: single_value
        model: ecommerce
        explore: orders
        measures: [orders.count]
    

> Think about the number and complexity of elements that you add to a LookML dashboard. More elements require more browser resources, which increases dashboard rendering time. Similarly, elements that render large amounts of data may impact dashboard performance. If rendering becomes an issue, consider reducing the complexity of dashboard element queries or creating multiple dashboards with fewer elements.