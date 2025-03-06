# https://cloud.google.com/looker/docs/sunburst

Depth: 3

**Note:** Starting in Looker 24.16, the Chart Config Editor supports the creation of sunburst charts.

A sunburst chart displays hierarchical data as a set of concentric rings, where the size of each ring slice is determined by a numeric measure.

Using the [Chart Config Editor](/looker/docs/chart-config-editor), you can create sunburst charts by starting from a [column chart](/looker/docs/column-options) in Looker. For best results, use at least two unpivoted dimensions and exactly one numeric measure to create a sunburst chart.

For example, you can create a sunburst chart that shows the **Orders Count** measure, broken down by the **Users Country** , **Users State** , and **Users City** dimensions. The size of each ring slice corresponds to the **Orders Count** .

![](/static/looker/docs/images/sunburst-2414.png)

## Prerequisites

To access the Chart Config Editor, you must have the [`can_override_vis_config` permission](/looker/docs/admin-panel-users-roles#can_override_vis_config).

## Writing the JSON snippet

To create a sunburst chart, start from the following JSON snippet:
    
    
    {
      chart: {
        type: 'sunburst',
      }
    }
    

## Creating a sunburst chart

To create a sunburst chart, follow these steps:

  1. View a [column chart](/looker/docs/column-options) in an Explore, or edit a column chart in a Look or dashboard.

Start from a column chart with two or more unpivoted dimensions and exactly one numeric measure. Make sure to order the dimensions from least granular to most granular. Your starting chart might look like a column chart plotting a single measure, with a concatenation of dimension values for each x-axis value.

![Sample column chart with a country, state, and city concatenation on the x-axis and Orders Count on the y-axis](/static/looker/docs/images/sunburst-base-2414.png)

**Note:** Even though this example is sorted by each dimension for clarity, sorting is not required and does not affect the sunburst chart.
  2. Open the **Edit** menu in the visualization.

  3. In the **Plot** tab, click the **Edit Chart Config** button. Looker displays the **Edit Chart Config** dialog.

  4. Select the **Chart Config (Override)** section, and enter the HighCharts JSON from the Writing the JSON snippet section of this page.

  5. To let Looker properly format your JSON, click **< > (Format code)**.

  6. To test your changes, click **Preview**.

  7. To apply your changes, click **Apply**. The visualization will be displayed using the custom JSON values.

![](/static/looker/docs/images/sunburst-2414.png)

Once you've customized your visualization, you can save it.

## Drilling into the data

Sunburst charts support the following drill actions:

  * To drill into one dimension value, click the corresponding ring slice.
  * To go back one level, click the center of the sunburst chart.
  * To go back one or more levels, use the breadcrumb navigation at the top left of the chart.