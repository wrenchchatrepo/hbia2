# https://cloud.google.com/looker/docs/marketplace-develop

Depth: 3

The [Looker Marketplace](https://marketplace.looker.com) is a central location for finding, deploying, and managing many types of Looker content, such as Looker models (blocks) and visualizations. Looker customers can install Looker Marketplace content from inside the Looker product. For more information, see [Using the Looker Marketplace](/looker/docs/marketplace).

This page summarizes the Looker Marketplace development process and provides an overview of the different types of Marketplace content that you can create.

### Overview

Developers can contribute to the Marketplace by creating content such as blocks, visualizations, and applications. At a high level, the Marketplace content development process follows these steps:

  1. Create your Marketplace content. Use one of the following guides to help you get started, depending on which type of content you'd like to build: 
     * [Developing a custom block for the Looker Marketplace](/looker/docs/marketplace-develop-custom-blocks)
     * [Developing a visualization for the Looker Marketplace](/looker/docs/marketplace-develop-visualization)
     * [Building a Looker application with the Extension Framework](/looker/docs/extension-intro-to-building)
     * [Building a custom action](/looker/docs/action-hub#building_a_custom_action)
  2. Host the code for your Marketplace content on a public Git repository. (For actions, instead [submit a pull request](https://github.com/looker-open-source/actions/blob/master/docs/adding_actions.md) to Looker's action repository.)
  3. Submit your Markeplace content for review. See [Submitting content to the Looker Marketplace](/looker/docs/marketplace-submit-content) for more details.

The following sections summarize the different types of Marketplace content that you can create.

### Blocks

#### What are blocks?

[Looker Blocks](/looker/docs/blocks) are pre-built pieces of LookML that Looker customers can use as a starting point for quick and flexible data modeling.

You can create a block that models a common third-party dataset, such as [Google Analytics 360](https://marketplace.looker.com/marketplace/detail/ga360-v2), or models a common analytical pattern, such as [Retail Analytics](https://marketplace.looker.com/marketplace/detail/retail-block-v2).

#### Using blocks

Blocks are designed to be plug-and-play, as long as you have the appropriate dataset in an existing Looker connection. You can [install a block](/looker/docs/marketplace) from the Marketplace, customize the LookML, and begin exploring.

To develop a block for submission to the Marketplace, create a new LookML project in your Looker instance and back up the LookML in a public GitHub repository. See [Developing a custom block for the Looker Marketplace](/looker/docs/marketplace-develop-custom-blocks) for detailed instructions and guidelines.

#### Try it out

Want to start using a block without writing any code?

  * Most [blocks on the Looker Marketplace Directory](https://marketplace.looker.com/marketplace/directory?Type=tools) can be [one-click installed](/looker/docs/marketplace) onto your Looker instance.

**Getting started:** [Developing a LookML block](/looker/docs/marketplace-develop-custom-blocks)

### Visualizations

#### What are visualizations?

In addition to Looker's [default visualization library](/looker/docs/visualization-types), you can [create custom visualization types](/looker/docs/marketplace-develop-visualization) in JavaScript. using the [Looker Visualization API](https://github.com/looker-open-source/custom_visualizations_v2/blob/master/docs/getting_started.md) with your Javascript environment.

For example, the [Looker Marketplace](https://marketplace.looker.com/marketplace/directory?Type=visualizations) currently has listings for an [Aster Plot Visualization](https://marketplace.looker.com/marketplace/detail/viz-aster_plot), a [Force-Directed Graph](https://marketplace.looker.com/marketplace/detail/viz-forcedirected), and a [Gauge Visualization](https://marketplace.looker.com/marketplace/detail/viz-gauge), among many others.

#### Using visualizations

Visualizations are designed to be plug-and-play. You can [install a visualization](/looker/docs/marketplace#installing_a_tool_from_the_marketplace) from the Marketplace and immediately select the new visualization type when exploring, building a new dashboard, and editing a dashboard.

To develop a visualization for submission to the Marketplace, start by using the [Looker Visualization API](https://github.com/looker-open-source/custom_visualizations_v2/blob/master/docs/getting_started.md) with your Javascript environment. See [Developing a visualization for the Looker Marketplace](/looker/docs/marketplace-develop-visualization) for detailed instructions and guidelines.

#### Try it out

Want to start using a visualization without writing any code?

  * Most [visualizations on the Looker Marketplace Directory](https://marketplace.looker.com/marketplace/directory?Type=visualizations) can be [one-click installed](/looker/docs/marketplace) onto your Looker instance.

**Getting started:** [Developing a visualization](/looker/docs/marketplace-develop-visualization)

### Applications

#### What are applications?

Looker Applications allow you to provide highly customized and integrated experiences to your Looker instance's users.

A dedicated Looker page becomes your canvas, with a wide array of tools at your disposal, including the ability to:

  * run Javascript code
  * access the Looker APIs through a pre-authenticated client
  * leverage Looker Components for seamless UI
  * make HTTP calls from the client or through a convenient server proxy
  * authenticate with third-party services via OAuth

#### Using Applications

Applications are designed to be plug-and-play. You can [install an Application](https://marketplace.looker.com/marketplace/directory?Type=applications) from the Marketplace and imediately begin using it.

To develop an application for submission to the marketplace, the first step is to is author a Javascript-based client-side application that uses the APIs exposed by Looker's [Extension Framework](/looker/docs/extension-intro-to-building). Looker's [`create-looker-extension`](https://www.npmjs.com/package/create-looker-extension) command line tool can get you started with a template codebase, including the necessary build tooling to bundle your application code via webpack. See the [Building a Looker extension](/looker/docs/extension-intro-to-building) page for detailed instructions and guidelines.

#### Try It Out

Want to start using a Looker Applications without writing any code?

  * Several [Looker-published Applications](https://marketplace.looker.com/marketplace/directory?Type=applications) can be [one-click installed](/looker/docs/marketplace) into your Looker instance from the Looker Marketplace.

**Getting Started:** [Building a Looker extension](/looker/docs/extension-intro-to-building)

### Actions

#### What are actions?

Actions, also called integrations, deliver Looker data to third-party services. Expand on Looker's [action destination library](/looker/docs/admin-panel-platform-actions#list_of_integrated_services) by creating an action to a new destination, such as [Airtable](https://community.looker.com/explores-36/looker-actions-airtable-6812) or [Azure Storage](https://community.looker.com/explores-36/looker-actions-azure-storage-6814).

#### Using actions

Looker customers enable actions from the [Admin settings - Actions](/looker/docs/admin-panel-platform-actions) page in their Looker instance, rather than by installing actions from the Marketplace.

To develop a new action, write a Javascript method that sends either one cell of a Looker data table, one Looker query, or one Looker dashboard to the destination. See the [Building a custom action](/looker/docs/action-hub#building_a_custom_action) page for detailed instructions and guidelines.

#### Try It Out

Want to start using an action without writing any code?

  * Enable an action from the [Admin settings - Actions](/looker/docs/admin-panel-platform-actions) page in your Looker instance. Then, select the action when sending or scheduling data.

**Get started:** [Building a custom action](/looker/docs/action-hub#building_a_custom_action)