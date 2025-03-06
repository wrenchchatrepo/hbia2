# https://cloud.google.com/looker/docs/streamgraph

Depth: 3

**Note:** Starting in Looker 24.8, the Chart Config Editor supports the creation of streamgraph charts.

A streamgraph chart is a type of stacked area chart that is useful for displaying compound volume across different categories or over time.

Using the [Chart Config Editor](/looker/docs/chart-config-editor), you can create streamgraph charts by starting from an [area chart](/looker/docs/area-options) in Looker. Streamgraph charts require two dimensions and one measure.

For example, the following streamgraph chart shows the **Total Sale Price** over several different **Category** values, plotted over **Order Created Month**. Categories are stacked on top of one another to show how much each category contributes to the total, as well as how the total changes over time.

![](/static/looker/docs/images/streamgraph-248.png)

## Prerequisites

To access the Chart Config Editor, you must have the [`can_override_vis_config` permission](/looker/docs/admin-panel-users-roles#can_override_vis_config).

### Writing the JSON snippet

To create a streamgraph chart, start from the following JSON snippet:
    
    
    {
      chart: {
        type: 'streamgraph',
      }
    }
    

### Creating a streamgraph chart

To create a streamgraph chart, follow these steps:

  1. View an [area chart](/looker/docs/area-options) in an Explore, or edit an area chart in a Look or dashboard.

For this example, we recommend starting from an area chart with two dimensions and one measure. One dimension should be pivoted. Your starting chart might look something like this example:

![Sample stacked area chart.](/static/looker/docs/images/streamgraph-base-248.png)

  2. Open the **Edit** menu in the visualization.

  3. In the **Plot** tab, click the **Edit Chart Config** button. Looker displays the **Edit Chart Config** dialog.

  4. Select the **Chart Config (Override)** section, and enter the HighCharts JSON from the Writing the JSON snippet section of this page.

  5. To let Looker properly format your JSON, click **< > (Format code)**.

  6. To test your changes, click **Preview**.

  7. To apply your changes, click **Apply**. The visualization will be displayed using the custom JSON values.

![](/static/looker/docs/images/streamgraph-editor-248.png)

Once you've customized your visualization, you can save it.