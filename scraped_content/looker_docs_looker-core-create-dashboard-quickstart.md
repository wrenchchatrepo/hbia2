# https://cloud.google.com/looker/docs/looker-core-create-dashboard-quickstart

Depth: 3

# Build a dashboard with sample data

Learn how to create a dashboard with sample data from the **Intermediate Ecommerce** Explore in the [sample LookML project](/looker/docs/looker-core-sample-project) on your Looker (Google Cloud core) instance.

This quickstart guides you through building a dashboard with the following tiles, including an optional Look-linked tile that you can add to your dashboard if you've completed the [Build a Look with sample data](/looker/docs/looker-core-create-look-quickstart) quickstart:

  * **Top Weekly Spenders** : Identify the top spenders for the past four weeks to target them with personalized promotions.
  * **Yearly Sales Goal Tracking (2024)** : Visualize your year-to-date sales and compare them to a set goal by using table calculations to visualize a a running total and by adding a reference line.
  * (Optional) **Weekly Shipping Trends (Last 8 Weeks)** : If you've completed the [Build a Look with sample data](/looker/docs/looker-core-create-look-quickstart) quickstart, you can also add your shipping delay analysis Look to this dashboard.

![](/static/looker/docs/images/looker-core-sample-project-dashboard-2420.png)

## Before you begin

To follow along with this quickstart, you'll need access to a Looker (Google Cloud core) instance that includes the [sample LookML project](/looker/docs/looker-core-sample-project). The sample project includes the prebuilt **Intermediate Ecommerce** Explore that is used in this quickstart.

**Note:** The **Intermediate Ecommerce** Explore is found in the **Z) Sample LookML** model. This model name may differ on your Looker instance.

Optionally, if you want to incorporate a pre-existing Look into your dashboard, you can follow the instructions in the [Build a Look with sample data](/looker/docs/looker-core-create-look-quickstart) quickstart.

You'll also need to have a the following [Looker permissions](/looker/docs/admin-panel-users-roles#permissions_list) on your Looker (Google Cloud core) instance (or a Looker role that includes these permissions):

  * `access_data`: Access the sample data in the **Intermediate Ecommerce** Explore
  * `explore` (and its parent permission, `see_looks`): Access [the Explore page](/looker/docs/viewing-and-interacting-with-explores#the_explore_page) and run queries in the **Intermediate Ecommerce** Explore.
  * `see_user_dashboards` (and its parent permission, `see_looks`): View the **Sales and Customer Insights** dashboard.
  * `save_dashboards` (and its parent permission, `save_content`): Save and edit the **Sales and Customer Insights** dashboard.
  * `save_looks` (and its parent permission, `save_content`): Save the **Weekly Shipping Trends (Last 8 Weeks)** Look (if you complete the [Build a Look with sample data](/looker/docs/looker-core-create-look-quickstart) quickstart).
  * `create_table_calculations`: Create the table calculations for the **Yearly Sales Goal Tracking (2024)** tile.

## Create the new dashboard from an Explore

This section guides you through querying data and creating a visualization for the **Top Weekly Spenders** tile, which will show the top 15 customers by sales in the last 4 weeks. You'll then save the visualization as the first tile on your new dashboard.

![](/static/looker/docs/images/looker-core-sample-project-tile-from-explore-2420.png)

### Navigate to the Explore

First, you'll use the **Intermediate Ecommerce** Explore to visualize the sample data. To navigate to the **Intermediate Ecommerce** Explore, follow these steps:

  1. In Looker, click **Main menu** menu to expand the main navigation menu, if not already expanded.
  2. In the main navigation menu, select **Explore**.
  3. Click **Z) Sample LookML** (or the corresponding model name on your instance) to expand the list of Explores, if not already expanded.
  4. Click **2) Intermediate Ecommerce** Explore to open the Explore page.

### Query and visualize the data

Next, you'll select fields from the **Intermediate Ecommerce** Explore and then define the visualization for the **Top Weekly Spenders** tile, which shows the top 15 customers by sales in the last 4 weeks. To select fields and visualize the sample data, follow these steps:

  1. In the **Intermediate Ecommerce** Explore, select the following fields from the field picker: 
     * **Users** > **Email**
     * **System Keys** > **User ID (On Order Item)**
     * **Order Items** > **Sales (Validated)**
  2. In the **Data** section of the Explore, set the value of **Row Limit** to `15`.
  3. In the **Data** section of the Explore, click the gear menu for the **System Keys User ID (On Order Item)** field, and then select **Hide this field from visualization**.
  4. To create a filter that limits the data to the last 4 weeks, follow these steps: 
    1. Click the **Filters** section of the Explore to show the filter options, and then click **\+ Filter**.
    2. In the **Add Filter** window, expand the **Order Items** view to show the **Created At Date** dimension group.
    3. Under the **Created At Date** dimension group, select the **Created At Week** field.
    4. Set the filter condition to **is in the last** and enter the value `4` in the text input field, and then select **weeks** from the list of timeframes.
  5. In the **Data** section of the Explore, click the **Order Items Sales (Validated)** field to sort the results by the **Order Items Sales (Validated)** field in descending order.
  6. To run the query and display the results, click **Run**.
  7. Click the **Visualization** section of the Explore to see the visualization of the query results.

Looker displays the query results in the **Visualization** section of the Explore page, with the query results showing only the top 15 customers by sales amounts in the last 4 weeks.

### Save your visualization as a new dashboard

To save the visualization that you created in the previous section as a new dashboard, follow these steps:

  1. Click the **Explore actions** gear icon settings and select **Save** , and then select **As a new dashboard**.
  2. In the **Save as a new dashboard** window, in the **Title** field, enter a title. This title will be applied to both the new dashboard and the tile that you have created. You can change the title of the dashboard later if you want to.
  3. In the **Settings** tab, in the **Folders** section, select the folder to which you want to save the dashboard.
  4. Click **Save**. Looker displays a notification informing you that your tile has been saved to a new dashboard.
  5. Optionally, click the **View dashboard** link within the notification to be taken directly to your new dashboard in [edit mode](/looker/docs/editing-user-defined-dashboards#entering_edit_mode_in_dashboards). When in edit mode, you can select the existing dashboard title and enter a new title. In this example, you can enter `Sales and Customer Insights` as the title.

## Add additional tiles to the dashboard

Next, you'll add more tiles to your dashboard. You'll create a query tile that tracks progress against a yearly sales goal and, if you completed the [Build a Look with sample data](/looker/docs/looker-core-create-look-quickstart) quickstart, you'll add that Look to your dashboard as a tile.

### Create a new query tile within the dashboard

In this section, you'll create the **Sales Goal Tracking (2024)** tile, which will show your cumulative sales over time compared to a yearly sales goal and uses [table calculations](/looker/docs/table-calculations) to define the running total and the target sales.

![](/static/looker/docs/images/looker-core-sample-project-tile-from-dashboard-2420.png)

To create the tile from within the **Sales and Customer Insights** dashboard, follow these steps:

  1. Navigate to your **Sales and Customer Insights** dashboard.
  2. Click the **Dashboard actions** three-dot icon more_vert, and then select **Edit dashboard**.
  3. In the page header, click **Add** , and then select **Visualization**.
  4. In the **Choose an Explore** window, select the **Intermediate Ecommerce** Explore.
  5. In the title field, enter a title (in this example, enter `Sales Goal Tracking (2024)`).
  6. In the Explore field picker, select the following fields: 
     * **Order Items** > **Created At Week**
     * **Order Items** > **Sales (Validated)**
  7. To filter the data to show only 2024 sales, follow these steps: 
    1. Click the **Filters** section of the Explore to show the filter options, and then click **\+ Filter**.
    2. In the **Add Filter** window, expand the **Order Items** view to see the fields in the **Created At Date** dimension group.
    3. Under the **Created At Date** dimension group, select the **Created At Date** field and choose the **is in the year** condition. Enter `2024` in the text input field.
  8. In the **Custom Fields** section, click **Add** and then select **Table Calculation** to create the following table calculations: 
     * **Cumulative Sales** : 
       1. Enter the formula `running_total(${order_items.total_sales_price_validated})`.
       2. Set the value of **Format** to **short_dollars**.
       3. In the **Name** field, enter `Cumulative Sales`.
       4. To save the table calculation, click **Save**.
     * **Target Sales** : 
       1. Enter the formula `row() * 72000 + (${cumulative_sales} * 0)`.
       2. Set the value of **Format** to **Decimals**.
       3. Set the value of **Decimals** to **0**.
       4. In the **Name** field, enter `Target Sales`.
       5. To save the table calculation, click **Save**.
  9. To hide the **Order Items Sales (Validated)** field from the visualization, in the **Data** section of the Explore, click the gear menu for the **Order Items Sales (Validated)** field, and then select **Hide this field from visualization**.
  10. To run the query and visualize the query results, click **Run**.
  11. In the **Visualization** section of the Explore, configure the visualization: 
    1. In the **Visualization** menu, select **Column** to display the query results in columns.
    2. Click **Edit** tune to open the **Visualization** menu.
    3. In the **Series** tab, in the **Customizations** section, expand **Target Sales** , then in the **Type** field select the **Line** option.
    4. In the **Y** tab, in the **Markings** section, click **Add Reference Line**. In the **Value** menu, select **Custom** , and then enter the value `3750000` in the text input field. This value represents the yearly sales goal.
    5. Set the **Label Position** setting to **Center**.`
  12. To save the visualization, click **Save**.
  13. In the **Edit Dashboard** window, click **Save** to save the dashboard.

The **Sales Goal Tracking (2024)** tile is now displayed on the **Sales and Customer Insights** dashboard.

### Add an existing Look as a tile (Optional)

If you have completed the [Build a Look with sample data](/looker/docs/looker-core-create-look-quickstart) quickstart, you can add your **Weekly Shipping Trends (Last 8 Weeks)** Look to your dashboard as a tile.

![](/static/looker/docs/images/looker-core-sample-project-look-2412.png)

To add this Look to the **Sales and Customer Insights** dashboard, follow these steps:

  1. In the Looker main navigation menu, navigate to the folder where you saved your **Weekly Shipping Trends (Last 8 Weeks)** Look.
  2. Click the **Weekly Shipping Trends (Last 8 Weeks)** Look.
  3. Within the Look, click the **Explore actions** gear icon settings, select **Save** , and then select **To an existing dashboard**.
  4. In the **Add to a Dashboard in this folder** window, select the **Sales and Customer Insights** dashboard.
  5. Click **Save to Dashboard**.

**Note:** Clicking **Save to Dashboard** adds the Look as a [static query tile](/looker/docs/creating-user-defined-dashboards#adding_query_tiles_from_a_look), rather than as a [Look-linked tile](/looker/docs/creating-user-defined-dashboards#adding_look-linked_tiles_from_a_look). To keep the tile updated with changes to the Look, use the **Add Look to Dashboard** option instead of the **Save to Dashboard** option.

The **Weekly Shipping Trends (Last 8 Weeks)** tile is now displayed as a static query tile on the **Sales and Customer Insights** dashboard. You may need to refresh the page to see the newly added Look in your dashboard.

## Create an interactive dashboard filter

In this section, you'll add an [interactive dashboard filter](/looker/docs/filters-user-defined-dashboards) to the **Sales and Customer Insights** dashboard. This filter lets viewers dynamically adjust the timeframe for the data displayed, choosing options like **Today** , **Last 7 Days** , or **Last 30 Days**.

**Note:** Depending on the tiles that you've added, a filter may already be applied to your dashboard. You can edit or delete any existing filters.

To add a relative date filter on the **Order Items Created At Date** field, follow these steps:

  1. Navigate to the **Sales and Customer Insights** dashboard.
  2. Click the **Dashboard actions** three-dot icon more_vert, and then select **Edit dashboard**.
  3. In the page header, click **Filters** , and then select **Add filter**.
  4. In the **Add Filter** window, in the **Filter by** section, expand the **Order Items** view, then expand the **Created At Date** dimension group, then select the **Created At Date** field.
  5. In the **Title** field, enter `Order Date`.
  6. Optionally, in the **Configure Default Value** section, select the timeframe that you want to be displayed by default.
  7. Optionally, in the **Tiles To Update** tab of the **Add Filter** window, configure the tiles that you want to update when the filter is applied.
  8. Click **Add**.

The **Order Date** filter is now added to the **Sales and Customer Insights** dashboard. Users can now filter the data by selecting timeframes like **Today** , **Last 7 Days** , or **Last 30 Days**.

## Reposition and resize the dashboard tiles

This section explains how to arrange and format the tiles on your dashboard to customize its layout and appearance. To reposition or resize tiles on your dashboard, follow these steps:

  1. Navigate to the **Sales and Customer Insights** dashboard.
  2. Click the **Dashboard actions** three-dot icon more_vert, and then select **Edit dashboard**.
  3. To reposition a tile, click and hold the tile's six-dot **Hold and drag to reorder** icon reorder, and then drag the tile to its new location.
  4. To resize a tile, hold your cursor over the bottom right corner of the tile, and then click and hold to drag the tile's border to resize it.

**Tip:** You can also use the [**Quick layout** option](/looker/docs/editing-user-defined-dashboards#quick_layout) in the page header to quickly arrange tiles in rows with a uniform size. Select the number of tiles that you want per row, and then adjust the arrangement or resize individual tiles as needed.

## What's next

  * [Creating user-defined dashboards](/looker/docs/creating-user-defined-dashboards)
  * [Editing user-defined dashboards](/looker/docs/editing-user-defined-dashboards)
  * [Adding and editing user-defined dashboard filters](/looker/docs/filters-user-defined-dashboards)
  * [Filtering and limiting data](/looker/docs/filtering-and-limiting)
  * [Sharing data](/looker/docs/sharing-data)