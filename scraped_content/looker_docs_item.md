# https://cloud.google.com/looker/docs/item

Depth: 3

**Note:** Starting in Looker 24.20, the Chart Config Editor supports the creation of item charts.

An item chart displays categorical and hierarchical data as a set of dots. Each dot represents a data value or group of data values.

Using the [Chart Config Editor](/looker/docs/chart-config-editor), you can create item charts by starting from a [column chart](/looker/docs/column-options) in Looker.

Item charts require at least one dimension and exactly one measure.

For example, you can create an item chart that shows the **Inventory Item Count** measure value over several different **Seasonal Collection** dimension values. The dots will be colored according to the dimension values.

![](/static/looker/docs/images/item-2420.png)

## Prerequisites

To access the Chart Config Editor, you must have the [`can_override_vis_config` permission](/looker/docs/admin-panel-users-roles#can_override_vis_config).

## Writing the JSON snippet

To create an item chart, start from the following JSON snippet:
    
    
    {
      chart: {
        type: 'item',
      }
    }
    

## Creating an item chart

To create an item chart, follow these steps:

  1. View a [column chart](/looker/docs/column-options) in an Explore, or edit a column chart in a Look or dashboard.

Item charts require at least one dimension and exactly one measure. Your starting chart might look something like this example:

![Sample column chart with Seasonal Collection on the x-axis and Inventory Item Count on the y-axis](/static/looker/docs/images/item-base-2420.png)

  2. Open the **Edit** menu in the visualization.

  3. In the **Plot** tab, click the **Edit Chart Config** button. Looker displays the **Edit Chart Config** dialog.

  4. Select the **Chart Config (Override)** section, and enter the HighCharts JSON from the Writing the JSON snippet section of this page.

  5. To let Looker properly format your JSON, click **< > (Format code)**.

  6. To test your changes, click **Preview**.

  7. To apply your changes, click **Apply**. The visualization will be displayed using the custom JSON values.

![](/static/looker/docs/images/item-json-2420.png)

Once you've customized your visualization, you can save it.

### Changing the layout style

By default, the item chart displays items in a semicircle. You can change the shape of the chart by using the `startAngle` and `endAngle` properties.

For example, to create a circular item chart, use the following JSON:
    
    
    {
      chart: {
        type: 'item'
      },
      series: [{
        startAngle: null,
        endAngle: null
      }]
    }
    

![](/static/looker/docs/images/item-circle-2420.png)

To create a rectangular item chart, use the following JSON:
    
    
    {
      chart: {
        type: 'item'
      },
      series: [{
        startAngle: null,
        endAngle: null
      }]
    }
    

![](/static/looker/docs/images/item-rect-2420.png)

## Limitations and requirements

When you're using item charts, keep the following limitations and requirements in mind:

  * Item charts require exactly one measure.
  * Item charts require at least one dimension.
  * Item charts don't support pivoted dimensions.
  * If your measure values are larger than the number of dots that Looker can display, Looker adds a label below the chart that denotes how many values each dot represents.
  * Item charts can only render queries with 50 rows or fewer.