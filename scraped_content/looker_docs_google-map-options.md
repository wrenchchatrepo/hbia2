# https://cloud.google.com/looker/docs/google-map-options

Depth: 3

**Note:** This page describes visualization options for Looker. For information about Looker Studio visualizations, see [Types of charts in Looker Studio](/looker/docs/studio/types-of-charts-in-looker-studio).

Google Maps charts let you visualize geographic data on responsive and interactive maps, and they provide significant control over the way that map points are plotted. Google Maps charts have similar functionality to the [Map chart](/looker/docs/map-options) visualization type.

## Viewing a Google Maps chart

When users view a Google Maps chart, several icons appear on the chart that let them interact with the visualization.

![](/static/looker/docs/images/gmaps-chart-icons-2212.png)

  1. **Zoom in and Zoom out icons** : Click the **+** icon to zoom in and the **-** icon to zoom out on the map view.
  2. **Toggle fullscreen view icon** : Click the **Toggle fullscreen view** icon to expand the map to fullscreen. Press the `esc` key on your keyboard or click the icon again to return to standard view.
  3. **Drag Pegman onto the map to open Street View** : Drag the Pegman icon to any location on the chart to switch the map to [Street View](https://support.google.com/maps/answer/3093484) for that location. Click the back arrow at the upper left of Street View to return to the chart.
  4. **Distance scale** : At the bottom of the chart, there is a scale in meters or kilometers for the current view of the map.
  5. **Keyboard shortcuts** : Click **Keyboard shortcuts** at the bottom of the chart to see a window with available keyboard shortcuts for interacting with the chart.
  6. **Value color scale** : If measures are plotted on the chart, a color scale appears at the the bottom left of the chart to indicate the range of colors between the minimum and maximum values. The settings in the **Value menu** can affect the appearance of the value color scale.
  7. **Open this area in Google Maps** : Click the Google logo at the bottom left of the chart to open the map in Google Maps. Google Maps opens in a new browser tab.

## Building a Google Maps chart

To create a Google Maps chart, your query must include at least one of the following fields:

  * A dimension based on latitude and longitude data. This is defined by a LookML developer as a dimension of [`type: location`](/looker/docs/reference/param-dimension-filter-parameter-types#location).
  * A dimension with a map layer assigned to it. LookML developers can add a [built-in map layer](/looker/docs/reference/param-field-map-layer-name#built-in_map_layers) or a [custom map layer](/looker/docs/reference/param-model-map-layer) to a dimension using the [`map_layer_name`](/looker/docs/reference/param-field-map-layer-name) parameter.
  * A zip code dimension, which automatically has a US zip code map layer assigned to it. This is defined by a LookML developer as a dimension of [`type: zipcode`](/looker/docs/reference/param-dimension-filter-parameter-types#zipcode). Zip code regions are based on the US zip code tabulation areas (ZCTAs). There may not be a one-to-one correspondence between zip codes and the ZCTAs used for map visualizations. It is possible that not all points will be visualized in the map.

Limit the precision of latitude and longitude data coordinates to no more than five to six decimal places. If coordinates exceed seven decimal places, the map will not display any data points.

To build a Google Maps chart, select the **Google Maps** visualization type in the **Visualization** bar. You can also edit your map visualization in the visualization menu. Click **Edit** in the upper right corner of the **Visualization** bar.

The options described on this page are available in the different tabs of the **Edit** menu. Options may be grayed out or hidden if they conflict with other settings that you have chosen.

## Plot menu options

The **Plot** tab lets you select the way that your location data is plotted. Each choice has slightly different formatting options, as appropriate for the plot type. **Plot** options also differ depending on whether a [map layer](/looker/docs/reference/param-field-map-layer-name) is defined in the LookML for your dimension.

For visualizations that contain a zip code dimension (which automatically has a US zip code map layer assigned to it) or other dimensions that have a defined map layer, you will see the following **Plot** options:

  * **Heatmap Gridlines**
  * **Gridlines on Empty Regions**
  * **Heatmap Opacity**

For visualizations that do not contain zip code dimensions or dimensions that have a defined a map layer, the following **Plot** options are supported:

  * **Points**
  * **Automagic Heatmap**
  * **Density Heatmap**
  * **Connect with Lines**
  * **Connect with Areas**
  * **Gridlines on Empty Regions**
  * **Heatmap Opacity**

Each of the **Plot** menu options is described in this section.

### Points

![](/static/looker/docs/images/gmaps-points-option-2212.png)

You can plot each row in an underlying data table as a discrete point on the map.

For this plot type to work properly, you must select at least one dimension of [`type: location`](/looker/docs/reference/param-dimension-filter-parameter-types#location). Optionally, you can add a measure.

A location dimension by itself will place points of uniform size and color. Adding a measure to the underlying data table enables the points to be scaled by color or size in the **Points** menu tab.

### Automagic Heatmap

![](/static/looker/docs/images/gmaps-automagic-heatmap-option-2212.png)

An automagic heatmap displays data as a heatmap grid, which readjusts in granularity when viewers zoom in or out on the map.

For this plot type to work properly, you must select both a dimension of [`type: location`](/looker/docs/reference/param-dimension-filter-parameter-types#location) and a measure.

To display data in a query as a heatmap grid, Looker divides the visible map into equal squares and then calculates which values in your data fit into each square. The squares are colored according to a measure that you choose. Zooming this map in or out will prompt Looker to re-calculate the grid, so that the granularity is appropriate to the zoom level.

> The **Automagic Heatmap** option re-queries your data to construct the heatmap grid. A location dimension typically displays as distinct points with one latitude/longitude coordinate, but when you use an automagic heatmap, the dimension changes to the bounding boxes ("Heatmap region from ... to ..") of each square in the grid.

### Density Heatmap

![](/static/looker/docs/images/gmaps-density-heatmap-option-2212.png)

For this plot type to work properly, you must select at least one dimension of [`type: location`](/looker/docs/reference/param-dimension-filter-parameter-types#location). Optionally, you can add a measure.

A density heatmap is useful for displaying large amounts of location data with many points clustered densely together. The density heatmap displays the data using color intensity and a color scale to convey the concentration of data points in each area.

### Connect with Lines

![](/static/looker/docs/images/gmaps-connect-with-lines-option-2212.png)

For this plot type to work properly, you need two dimensions of [`type: location`](/looker/docs/reference/param-dimension-filter-parameter-types#location). Optionally, you can add a measure.

The **Connect with Lines** option takes two fields of `type: location` from your query and then connects them together with a line in the visualization. Adding a measure to the query lets you add a color scale to the lines.

### Connect with Areas

![](/static/looker/docs/images/gmaps-connect-with-areas-option-2212.png)

For this plot type to work properly, you need one dimension of [`type: location`](/looker/docs/reference/param-dimension-filter-parameter-types#location). Optionally, you can add a measure.

The **Connect with Areas** map visualization takes one field of `type: location` and connects all the points in the order in which you've sorted them with lines, forming the boundaries of an area on the map. Adding a measure to the query lets you format the size and color of the individual location points that bound the area in the **Value** menu tab.

### Heatmap Gridlines

This option is available when **Automagic Heatmap** is selected from the **Plot** menu or when a [map layer](/looker/docs/reference/param-model-map-layer) is used in your chart. Enabling this option adds a border around each of the gridlines used for the automagic heatmap.

### Heatmap Opacity

This option is available when **Automagic Heatmap** is selected or when a [map layer](/looker/docs/reference/param-model-map-layer) is used in your chart. This option lets you specify the opacity of the colors used in the heatmap. Enter a single-digit decimal between 0 and 1, where 0 means no color and 1 means totally opaque.

### Gridlines on Empty Regions

If the **Heatmap Gridlines** option is turned on, and you are plotting a dimension that has a defined [map layer](/looker/docs/reference/param-model-map-layer), you can enable the **Gridlines on Empty Regions** toggle to display an outline around the map regions that have no associated data.

![](/static/looker/docs/images/gmaps-gridlines-on-empty-regions-2212.png)

## Map menu options

### Map Style

**Map Style** lets users change the type of background map, and whether map labels (like cities and streets) should be displayed. This option features a drop-down menu with a list of choices:

  * **Light:** Light-colored map designed to provide geographic context while highlighting your data.

![](/static/looker/docs/images/gmaps-light-style-2210.png)

  * **Light (No Labels):** Same as **Light** , except the map omits labels such as city names.

  * **Dark:** Dark-colored map designed to provide geographic context while highlighting your data.

![](/static/looker/docs/images/gmaps-dark-style-2210.png)

  * **Dark (No Labels):** Same as **Dark** , except the map omits labels such as city names.

  * **Satellite:** Map displaying global satellite and aerial imagery.

![](/static/looker/docs/images/gmaps-satellite-style-2210.png)

  * **Satellite (No Labels):** Same as **Satellite** , except the map omits labels such as city names.

  * **Streets:** General-purpose map that emphasizes legible styling of road and transit networks.

![](/static/looker/docs/images/gmaps-streets-style-2210.png)

  * **Outdoors:** General-purpose map tailored to hiking, biking, and other outdoor uses.

![](/static/looker/docs/images/gmaps-outdoors-style-2210.png)

  * **Traffic (Day):** Light-colored map emphasizing transit networks and roads, including current traffic information.

![](/static/looker/docs/images/gmaps-traffic-style-2210.png)

  * **Traffic (Night):** Dark-colored map emphasizing transit networks and roads, including current traffic information.

  * **Minimal:** Light colored map with no labels or boundary lines.

![](/static/looker/docs/images/gmaps-minimal-style-2212.png)

### Map Position

You can change the center point and zoom level of a visible map:

  * **Fit to Data** : Automatically centers and zooms the map such that all the data points of your query are visible.
  * **Custom** : Lets you manually set a **Latitude** , **Longitude** , and **Zoom Level** (higher numbers create a closer zoom level).

### Allow Panning

This option lets you determine whether users can reposition the map by dragging it. This option is enabled by default.

### Allow Zooming

This option lets you determine whether a (+/-) button should display in the upper left of the map visualization, allowing users to zoom in and out. This option is enabled by default.

### Show Full Field Name

This option lets you determine whether to show the view name along with the field name in map tooltips. Tooltips display when users click on map data points. This option is disabled by default.

Visit the Things to consider section on this page for more information about how tooltips display on Google Map charts.

### Show Legend

This option lets you determine whether to show a map legend in the lower left of a visualization. The legend shows the color scale that the map is using, if you've added a measure to your visualization.

The **Show Legend** option is available for the following **Plot** options:

  * **Automagic Heatmap** mode
  * **Points** mode, when **Marker Color Mode** is set to **Based on Value**

### Show Region Field in Tooltip

The **Show Region Field in Tooltip** option is available when the query has at least one dimension with a map layer assigned to it. LookML developers can add a [built-in map layer](/looker/docs/reference/param-field-map-layer-name#built-in_map_layers) or a [custom map layer](/looker/docs/reference/param-model-map-layer) to a dimension using the [`map_layer_name`](/looker/docs/reference/param-field-map-layer-name) parameter.

This option lets you determine whether to display the region information in the tooltips that appear on the map.

When **Show Region Field in Tooltip** is enabled, if users hover over a region of the map, the region information (as provided by any dimensions with a map layer assigned to them) is displayed in the tooltip. In the following example, the query contains **State** and **Zipcode** dimensions with built-in map layers assigned to them:

![The tooltip displays the values New Mexico for State, 97106 for Zipcode, and 4 for Count.](/static/looker/docs/images/gmaps-show-region-2210.png)

When **Show Region Field in Tooltip** is disabled, if users hover over a region of the map, the tooltip contains only the values from the measures in the query. The following example uses the same query as the previous example, but **Show Region Field in Tooltip** is disabled:

![The tooltip displays only the value 4 for the Count field.](/static/looker/docs/images/gmaps-show-region-disabled-2210.png)

Visit the Things to consider section on this page for more information about how tooltips display on Google Map charts.

### Draw Map Labels Above Data

If the data in your visualization contains a [map layer](/looker/docs/reference/param-field-map-layer-name), the **Draw Map Labels Above Data** menu option appears. The option defaults to disabled.

Enabling **Draw Map Labels Above Data** moves the map's labels above the heatmap data. This is helpful with higher heatmap opacity values. If a heatmap is opaque, the labels don't show unless **Draw Map Labels Above Data** is enabled.

## Points menu options

**Note:** The **Points** menu is not available for visualizations that contain dimensions with a defined map layer. When you select an automagic heatmap or a density heatmap, the options in the **Points** menu do not affect the visualization.

### Type

This option is available for maps with points, connect with lines, or connect with areas plot types.

**Type** specifies the type of point displayed on the map visualization:

  * **Circle** : Points on the map are displayed as circles of varying sizes and colors.

![](/static/looker/docs/images/gmaps-points-circle-2210.png)
  * **Icon** : Points on the map are displayed as icons of varying colors. 

![](/static/looker/docs/images/gmaps-points-icon-2210.png)
  * **Both** : Points on the map are displayed as both circles and icons.

![](/static/looker/docs/images/gmaps-points-both-2210.png)
  * **None** : No points are displayed on the map.

![](/static/looker/docs/images/gmaps-points-none-2210.png)

Your point type selection impacts the other formatting options that are available. A **Type** of **Both** includes all options. A **Type** of **None** shows no options.

### Radius

This option is available for maps with points, connect with lines, or connect with areas plot types.

If you select **Circle** in the **Type** option of the **Points** menu, a **Radius** menu option appears. The **Radius** option lets you set the size of the circle points. You can choose one of three options:

  * **Proportional to Value:** Adjusts the relative size of the circles according to measures in your query. When you choose this option you can set a **Minimum Radius** and **Maximum Radius** of the circles, which correspond with the lowest and highest values in your data. You can also choose between a **Linear** and **Logarithmic** scale to size the circles.

  * **Equal to Value:** Adjusts the radius of the circles to the actual measure values in the underlying query. This likely only makes sense if you are plotting distance data — for example, if your measure contained the size of a territory.

  * **Fixed:** Choosing **Fixed** reveals and additional **Fixed Radius** option where you can set a fixed radius to apply to all map markers. The default value is 500 radius units.

### Radius Units

This option is available for maps with points, connect with lines, or connect with areas plot types.

If you select **Circle** or **Both** in the **Type** option of the **Points** menu, a **Radius Units** menu option appears. The **Radius Units** option lets you set the units of the circle points as meters or pixels.

### Icon

This option is available for maps with points, connect with lines, or connect with areas plot types.

If you select **Icon** or **Both** in the **Type** option of the **Points** menu, an **Icon** menu option appears. Expanding the **Icon** drop-down menu lets you choose an icon to display on all map markers. The markers cannot be dynamic according to your data.

### Marker Color Mode

This option is available for maps with points, connect with lines, or connect with areas plot types.

If you select **Circle** , **Icon** , or **Both** in the **Type** option of the **Points** menu, a **Marker Color Mode** menu option appears. This option lets you customize the color of the map markers in an interactive map. You can choose one of two options:

  * **Based on Value** : Colors are dynamically assigned to markers based on the values of the underlying query. To configure the colors in the legend for this option, see the Value Colors option.
  * **Custom** : Lets you set a single color to use for all map markers. The color value can also be formatted as an RGB hex string, such as `#2ca6cd`, or as [CSS color names](https://www.w3schools.com/cssref/css_colors.asp), such as `mediumblue`.

## Value menu options

**Note:** The **Value** menu is not available if the **Marker Color Mode** option in the **Points** menu is set to **Custom**.

### Value Colors

You can set the color of map points or define the range of colors to be used if you are color coding according to a measure.

You can input a list of hex strings, such as `#2ca6cd`, or [CSS color names](https://www.w3schools.com/cssref/css_colors.asp), such as `mediumblue`. The colors you input first are associated with the lowest values.

### Quantize Colors

By default, the **Quantize Colors** option is off, and Looker displays values using a gradient color scale.

![](/static/looker/docs/images/gmaps-quantize-off-2212.png)

When turned on, **Quantize Colors** changes the color scale from a smooth gradient to blocks of specific colors.

![](/static/looker/docs/images/gmaps-quantize-on-2212.png)

### Reverse Color Scale

When turned on, **Reverse Color Scale** switches the colors that indicate high and low values on the chart, reversing the color gradient.

### Minimum Value/Maximum Value

You can set the minimum and maximum values of the color range. This lets you color code all points under a certain threshold with the lowest color and all points over a certain threshold with the highest color.

By default this field is left blank, and the minimum and maximum values applied on the legend are the minimum and maximum values from your query.

## Things to consider

### Tooltip behavior on Google Maps charts

[Tooltips](/looker/docs/creating-visualizations#the_visualization_tooltip) on Google Map charts can behave in specific ways.

When an entire country is visible on a Google Map chart (and it is not repeated):

  * The tooltip will be displayed at the country's geographical center by width.
  * The tooltip display will begin at the country's topmost latitude.

If an entire country is _not_ visible on a Google Map chart (a map is zoomed into a specific point of a country), the tooltip will be displayed next to the cursor.

When a Google Map chart map is zoomed out enough to display two instances of the same country (both geographical centers are displayed), the tooltip will appear in one of two ways:

  * If there is room above both instances of the country, the tooltip will be displayed above the midpoint of the two countries.
  * If there is only room above one instance of the country, the tooltip will only be displayed above that country.