# https://cloud.google.com/looker/docs/admin-panel-platform-visualizations

Depth: 3

Looker includes a robust list of built-in [visualization types](/looker/docs/visualization-types), letting you chart your data in a variety of ways. If you need a type of chart that is not included in Looker's native visualization types, Looker provides several ways to add custom JavaScript visualizations to your Looker instance:

  1. Add a `visualization` parameter to your LookML project's manifest file to add custom visualizations directly to your LookML project. See the [`visualization`](/looker/docs/reference/param-manifest-visualization) parameter documentation page for more information.
  2. Install a visualization from the Looker Marketplace. With the [**Marketplace**](/looker/docs/admin-panel-platform-marketplace) feature enabled, you can install Looker Marketplace _plug-ins_ , including visualization types that you can add to Looker's built-in visualization library. See the [Using the Looker Marketplace](/looker/docs/marketplace) documentation page for more information about installing plug-ins from the Looker Marketplace. See the [Developing a custom visualization for the Looker Marketplace](/looker/docs/marketplace/adding-viz-marketplace) documentation page for information about creating a visualization that can be added to the Looker Marketplace and accessed by other Looker users.
  3. Use the **Visualizations** page in the **Platform** section of Looker's **Admin** menu to install and administer custom JavaScript visualizations from Looker's custom visualizations repository.

This page describes how to add custom JavaScript visualizations using the **Visualizations** page in the Looker **Admin** panel.

**Note:** To access all the admin pages in Looker, you must have the [Admin role](/looker/docs/admin-panel-users-roles#default_roles). If you have a permission that enables only parts of the **Admin** panel, such as [`manage_schedules`](/looker/docs/admin-panel-users-roles#manage_schedules) or [`manage_themes`](/looker/docs/admin-panel-users-roles#manage_themes), but you don't have the Admin role, then Looker may not display the page or pages described in this article in the **Admin** panel. Also, the `see_admin` permission grants read-only permission to most (but not all) Admin pages. See the [`see_admin`](/looker/docs/admin-panel-users-roles#see_admin) description for more information.

## Viewing a list of custom visualizations

To ensure full functionality of downloaded visualizations, admins for customer-hosted deployments should make sure to install the appropriate version of the [Chromium renderer](/looker/docs/installation-of-rendering-software#chromium).

The **Visualizations** page in the **Platform** section of Looker's **Admin** menu lists all the custom visualizations that have been added to your Looker instance.

The list includes the following columns:

  * **ID** : The unique ID assigned to the custom visualization. This value is assigned either in the JavaScript code, or when you add or edit a visualization using the **Admin** page, or in the visualization's [`id`](/looker/docs/reference/param-manifest-visualization#id) parameter when you [add a visualization using the LookML project manifest file](/looker/docs/reference/param-manifest-visualization).
  * **Label** : The name given to the visualization type in the Looker visualization menu. This value is assigned when you add or edit a visualization using the Admin page, or in the visualization's [`label`](/looker/docs/reference/param-manifest-visualization#label) parameter when you [add a visualization using the LookML project manifest file](/looker/docs/reference/param-manifest-visualization).
  * **Main** : The URI of the visualization's main JavaScript code. This value is assigned when you add or edit a visualization using the Admin page, or in the visualization's [`url`](/looker/docs/reference/param-manifest-visualization#url) parameter when you [add a visualization using the LookML project manifest file](/looker/docs/reference/param-manifest-visualization).
  * **Actions** : Buttons to edit or delete the visualization configuration. These buttons are not shown for visualizations added using the [LookML project's manifest file](/looker/docs/reference/param-manifest-visualization). To edit these visualizations, go to the LookML project's manifest file and edit the [`visualization`](/looker/docs/reference/param-manifest-visualization) parameter directly.

## Adding a new custom visualization

You can find a list of Looker's [Viz Blocks](/looker/docs/blocks#viz_blocks) in the Looker [Looker Marketplace](https://marketplace.looker.com/marketplace/directory?Type=visualizations). Looker also maintains a library of custom visualizations for public use on this [Looker GitHub page](https://github.com/looker-open-source/custom_visualizations_v2). You can find instructions for using Looker's Visualization API to create your own visualization types on this [Looker GitHub page](https://github.com/looker-open-source/custom_visualizations_v2/blob/master/docs/getting_started.md).

Once you know which visualization you'd like to add to your instance, you can use the The **Visualizations** page in the **Platform** section of Looker's **Admin** menu to add a custom visualization by selecting the **Add Visualization** button.

Looker displays the **New Visualization:** page. To add a new visualization, perform the following steps:

  1. In the **ID** field, enter the unique ID of the visualization defined in the visualization JavaScript.

  2. In the **Label** field, enter the name of the visualization. Looker displays this name in the Looker visualization menu on an Explore.

  3. In the **Main** field, enter the URI of the visualization's main JavaScript file to point Looker to your JavaScript code repository.

  4. If the site that hosts your custom visualization code uses a [subresource integrity (SRI) hash](https://en.wikipedia.org/wiki/Subresource_Integrity) for verification purposes, enter the SRI hash in the **SRI Hash** field. This field can be found under **Advanced options**. Looker's custom visualization hosts don't use an SRI hash.

  5. In the **Dependencies** field, enter the URIs of any other files that the visualization JavaScript is dependent upon, and click **Add**. You can enter multiple URIs separated by commas, or you can add multiple URIs one at a time. The **Dependencies** field can be found under **Advanced options**.

  6. Select **Save**.

Once the visualization has been added, you will see it as you've labeled it in the visualization menu in an Explore. You can use the new visualization type like any of Looker's existing visualization types.

To view custom visualizations from the visualization menu:

  1. Select the **`...`** three-dot icon from the [visualization menu bar](/looker/docs/creating-visualizations#quick_guide) to access the custom visualization.

  2. Once the visualization is selected, the name of the visualization appears on the visualization menu bar.

## Editing a custom visualization

To edit an existing visualization, select the **Edit** button to the right of the visualization. Looker displays the same page that you use to add a visualization (described in Adding a new custom visualization), but with the relevant information already filled in. Make any desired changes, and then click **Save**.

## Deleting a custom visualization

To delete a visualization, select the **Delete** button to the right of the visualization on the **Visualizations** page in the **Platform** section of Looker's **Admin** menu, and then click **OK** in the confirmation box.

Deleting a visualization removes it from Looker but won't affect anything in the visualization's external code repository.

Deleting a visualization disables any Looks or dashboards that use that visualization type. You can correct that by adding back the deleted visualization with the same visualization ID.

## Troubleshooting

Custom visualizations are a community-supported effort. Looker's support team does not troubleshoot issues relating to custom visualizations or your custom visualization code. For tracking and closing out bugs, use GitHub issues in the custom visualization's repository, or visit the [Looker Community](https://www.googlecloudcommunity.com/gc/Looker/ct-p/looker) for how-to posts, conversations, and tips regarding custom visualizations.