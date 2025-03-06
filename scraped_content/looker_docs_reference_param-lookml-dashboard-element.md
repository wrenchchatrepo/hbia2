# https://cloud.google.com/looker/docs/reference/param-lookml-dashboard-element

Depth: 3

Looker has [two kinds of dashboards](/looker/docs/building-lookml-dashboards#types_of_dashboards:_user-defined_and_lookml): [user-defined dashboards](/looker/docs/creating-user-defined-dashboards), which are created via the Looker UI, and [LookML dashboards](/looker/docs/building-lookml-dashboards), which are created in [`dashboard.lkml` files](/looker/docs/other-project-files#dashboard_files).

A dashboard contains _elements_ , which are the data visualizations, text tiles, and buttons on the dashboard. This page discusses options for the visualizations within a LookML dashboard. For settings that affect an entire LookML dashboard, see the [Dashboard LookML](/looker/docs/reference/param-lookml-dashboard) reference page.

The LookML parameters that can be used in a dashboard element depend upon the type of visualization that has been specified using the `type` parameter. Use the links on this documentation page to get information about the parameters for the different visualization types.

> Dashboard LookML and the model development LookML are different languages. Dashboard LookML is based on YAML, in which the number of indentations is very important. Model development LookML uses curly brackets.

An overview of LookML dashboard element types is provided on the documentation page for the [`type` parameter](/looker/docs/reference/param-lookml-dashboard-type).

## Cartesian charts

  * [Column chart parameters](/looker/docs/reference/param-lookml-dashboard-column-chart)
  * [Bar chart parameters](/looker/docs/reference/param-lookml-dashboard-bar-chart)
  * [Scatterplot chart parameters](/looker/docs/reference/param-lookml-dashboard-scatter-chart)
  * [Line chart parameters](/looker/docs/reference/param-lookml-dashboard-line-chart)
  * [Area chart parameters](/looker/docs/reference/param-lookml-dashboard-area-chart)
  * [Boxplot chart parameters](/looker/docs/reference/param-lookml-dashboard-boxplot-chart)
  * [Waterfall chart parameters](/looker/docs/reference/param-lookml-dashboard-waterfall-chart)

## Pie and donut charts

  * [Pie chart parameters](/looker/docs/reference/param-lookml-dashboard-pie-chart)
  * [Donut multiples chart parameters](/looker/docs/reference/param-lookml-dashboard-donut-multiples-chart)

## Progression charts

  * [Funnel chart parameters](/looker/docs/reference/param-lookml-dashboard-funnel-chart)
  * [Timeline chart parameters](/looker/docs/reference/param-lookml-dashboard-timeline-chart)

## Text and tables

  * [Text tile parameters](/looker/docs/reference/param-lookml-dashboard-text-tile)
  * [Button parameters](/looker/docs/reference/param-lookml-dashboard-button)
  * [Single value chart parameters](/looker/docs/reference/param-lookml-dashboard-single-value-chart)
  * [Single record chart parameters](/looker/docs/reference/param-lookml-dashboard-singe-record-chart)
  * [Table (legacy) chart parameters](/looker/docs/reference/param-lookml-dashboard-table-chart-legacy)
  * [Table chart parameters](/looker/docs/reference/param-lookml-dashboard-table-chart)

## Maps

  * [Google Maps chart parameters](/looker/docs/reference/param-lookml-dashboard-google-maps)
  * [Map chart parameters](/looker/docs/reference/param-lookml-dashboard-map)
  * [Coordinate map parameters](/looker/docs/reference/param-lookml-dashboard-coordinate-map)
  * [Choropleth map parameters](/looker/docs/reference/param-lookml-dashboard-choropleth-map)