# https://cloud.google.com/looker/docs/solid-gauge

Depth: 3

**Note:** Starting in Looker 24.8, the Chart Config Editor supports the creation of solid gauge charts.

Solid gauge charts are useful for displaying numbers in a known range. Readers can quickly determine whether the current value is relatively high or low based on expected values.

Using the [Chart Config Editor](/looker/docs/chart-config-editor), you can create solid gauge charts by starting from a column chart in Looker. Solid gauge charts require one dimension and one measure.

For example, the following solid gauge chart shows the current value of the **Customer Satisfaction (CSAT)** measure, which is represented by a circular blue progress bar. Since the possible values of CSAT scores can be from 0 to 100, those values are represented on either end of the gauge.

![](/static/looker/docs/images/solid-gauge-246.png)

## Prerequisites

To access the Chart Config Editor, you must have the [`can_override_vis_config` permission](/looker/docs/admin-panel-users-roles#can_override_vis_config).

### Writing the JSON snippet

To create a solid gauge chart, start from the following JSON snippet:
    
    
    {
      chart: {
        type: 'solidgauge'
      },
      yAxis: [{
        min: 0,
        max: 100,
        tickAmount: 10
      }],
    }
    

Change the following values to fit your use case:

  * The `yAxis.min` attribute defines the minimum value for the solid gauge chart.
  * The `yAxis.max` attribute defines the maximum value for the solid gauge chart.
  * The `yAxis.tickAmount` attribute specifies the number of labels that should be displayed around the solid gauge chart. The labels will be evenly distributed based on the `yAxis.min` and `yAxis.max` attributes.

### Creating a solid gauge chart

To create a solid gauge chart, follow these steps:

  1. View a [column chart](/looker/docs/column-options) in an Explore, or edit a column chart in a Look or dashboard.

For this example, we recommend starting from a column chart with one dimension and one measure, with a limit of one row. Your starting chart might look something like this example:

![Sample column chart with a single column that extends across the Y-axis.](/static/looker/docs/images/solid-gauge-base-246.png)

  2. Open the **Edit** menu in the visualization.

  3. In the **Plot** tab, click the **Edit Chart Config** button. Looker displays the **Edit Chart Config** dialog.

  4. Select the **Chart Config (Override)** section, and enter the HighCharts JSON from the Writing the JSON snippet section of this page.

  5. To let Looker properly format your JSON, click **< > (Format code)**.

  6. To test your changes, click **Preview**.

  7. To apply your changes, click **Apply**. The visualization will be displayed using the custom JSON values.

![](/static/looker/docs/images/solid-gauge-editor-246.png)

Once you've customized your visualization, you can save it.