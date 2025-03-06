# https://cloud.google.com/looker/docs/marketplace

Depth: 3

**Note:** As of Looker 23.16, [Looker (Google Cloud core)](/looker/docs/looker-core-overview) instances on public IP networks include Marketplace support. Looker (Google Cloud core) instances on private IP networks or on public IP and private IP networks don't support the Looker Marketplace.**Note:** New blocks, applications, visualizations, and plug-ins are announced in the [Looker release notes](/looker/docs/release-notes) for each release. Visit the release notes page to view the latest Looker release notes.

The Looker Marketplace is a central location within the Looker Platform for finding, deploying, and managing Looker Blocks, applications, visualizations, and plug-ins.

The Looker [Marketplace](/looker/docs/admin-panel-platform-marketplace) feature is enabled by default. Before you can install [extensions](/looker/docs/glossary#extension) from the Looker Marketplace, a Looker admin must enable the [**Extension Framework**](/looker/docs/admin-panel-platform-extension-framework) feature.

If the particular block contains a [`local_dependency`](/looker/docs/reference/param-manifest-local-dependency) parameter, the block uses the local project import process. See the [Importing files from other projects](/looker/docs/importing-projects#importing_local_projects) documentation page for details on importing projects. The following blocks contain a `local_dependency` parameter:
    
    
    * Digital Marketing Analytics
    * Sales Analytics
    * Web Analytics
    

**Note:** We inform you when a tool is developed by Looker or by a third-party developer. Before you download or purchase content from the Marketplace, be sure that you have evaluated the third party developer and tool. Looker shares with the developer aggregated, non-identifying and non-profiling, statistical information regarding the performance of their tool in the marketplace, such as upload and deletion counts. These third party developers are not subprocessors to Looker.

## Discovering content in the Looker Marketplace

To enable users to access the Looker Marketplace, a Looker admin must first enable the [Marketplace](/looker/docs/admin-panel-platform-marketplace) feature.

To browse content on the Looker Marketplace, select the **Marketplace** button on the Looker menu bar storefront. (If you have the [`develop`](/looker/docs/admin-panel-users-roles#develop), [`manage_models`](/looker/docs/admin-panel-users-roles#manage_models), and [`deploy`](/looker/docs/admin-panel-users-roles#deploy) permissions, selecting the **Marketplace** button will open a menu of options; select **Discover**.)

The Marketplace homepage shows popular Looker applications and tools.

![](/static/looker/docs/images/dev-marketplace-2314.png)

To find content, use the search bar. You can use the **Applications** , **Models** , **Visualizations** , and **All** filters that appear near the search bar to filter for different types of content:

  * **Applications** : Looker [applications](https://looker.com/product/applications) are comprehensive sets of models, dashboards, and Explores. Applications are designed to let you analyze your sales and marketing data without having to build your own LookML models. Using the Looker Marketplace, you can install an application and connect to your data source. The installation process then loads your data, letting you see results within 24 hours.
  * **Models** : Models are pre-built LookML models, including dashboards and Explores, for a variety of popular data sources.
  * **Plug-ins** : Plug-ins are visualization types that you can install and add to Looker's built-in visualization library.

Once you have selected a type, you can also filter by tag, category, industry, and author using the filter checkboxes on the left side.

**Note:** Some applications, like the Looker Data Dictionary, are extensions that are built using the Looker extension framework. Before you can install such extensions from the Looker Marketplace, a Looker admin must enable the [**Extension Framework**](/looker/docs/admin-panel-platform-extension-framework) feature.

## Automatically installing Looker-built applications

If your Looker admin has enabled the [**Auto Install**](/looker/docs/admin-panel-platform-marketplace#auto_install) option in the [**Marketplace**](/looker/docs/admin-panel-platform-marketplace) page in the **Platform** section of Looker's **Admin** menu, some Looker-built applications will automatically install and update on your Looker instance. The [API Explorer](/looker/docs/api-explorer) is the only extension that will automatically install, but more Looker-built applications may be added in the future.

For more information, see the [Admin settings - Marketplace](/looker/docs/admin-panel-platform-marketplace) documentation page.

## Installing a tool from the Marketplace

**Note:** Note: Customer-hosted Looker instances may require additional configuration to access the Marketplace data:

  * If you are running Looker 23.10 or later, the server running the Looker instance must be configured to access the public internet server running at the URL `https://static-a.cdn.looker.app/`.
  * If you are running Looker 23.8 or earlier, the server running the Looker instance must be configured to access the public internet server running at the URL `https://marketplace-api.looker.com/`.
  * The server running the Looker instance must also be configured to access the public internet server running at the URL `https://github.com/`.

Additionally, customer-hosted deployments using clustered instances must set up a [shared (network) file system](/looker/docs/clustering-looker#shared_file_system) to install applications or tools from the Looker Marketplace.

The installation process varies depending on the tool you are installing. Applications and some models, for example, have the option to connect the tool to your source database. The following procedure shows all the possible installation options; however, depending on the tool you are installing, you may only see a subset of the following steps.

**Note:** For best performance, always install the latest version of any Marketplace tool. Some visualizations serve JavaScript in the [`file:` subparameter](/looker/docs/reference/param-manifest-visualization). If you have the most recent update of the visualization installed and the visualization is not rendering, you must enable Looker cookies in your browser.

Before installing any tool from the Marketplace, a Looker admin should ensure that the following features are enabled:

  * To install any piece of content from the Looker Marketplace, enable the [**Marketplace**](/looker/docs/admin-panel-platform-marketplace) feature.
  * To install [extensions](/looker/docs/glossary#extension), enable the [**Extension Framework**](/looker/docs/admin-panel-platform-extension-framework) feature.

To install a tool from the Looker Marketplace, follow these steps:

  1. Make sure you have at least the [`develop`](/looker/docs/admin-panel-users-roles#develop), [`manage_models`](/looker/docs/admin-panel-users-roles#manage_models), and [`deploy`](/looker/docs/admin-panel-users-roles#deploy) permissions.

  2. From the Marketplace main menu, select the tool that you want to install, and then select its tile.

Looker displays the tool's installation page, which shows a short description of the tool and any needed information about installing and using the tool.

  3. Select **Install** or **Install Free Trial**.

  4. Looker displays pages asking you to accept the tool's license agreements and the Looker permissions that are required by the tool. If you want to accept the license agreements and permission requests, select **Accept** on these pages.

  5. Each tool requires some configuration information that is specific for that tool, such as a connection name or visualization label. Select or enter the configuration information, and then select **Install**. (After the installation is complete, you can change this configuration information at any time by using the **Manage** page.)

  6. Looker will complete the installation. You can now use the installed content

See the [Customizing Looker Marketplace Blocks](/looker/docs/marketplace-customize-blocks) documentation for information on customizing blocks you have installed from the Marketplace.

## Installing a tool from a Git URL

To install models and plug-ins directly from the Git repository, follow these steps:

  1. Select the **Marketplace** button on the Looker menu bar storefront.

  2. From the Marketplace menu, select the **Manage** option.

  3. On the **Manage** page, select the three-dot **Options** button more_vert.

  4. Click the **Install via Git URL** button.

  5. Looker shows the **Install via Git** page. Enter the URL and commit SHA of the repository and the version of the tool or visualization that you want to install.

  6. Select **Install**.

## Using Looker Marketplace content

Once a tool is installed, you can open it through the **Applications** folder in the left navigation panel.

From there, you will see either the application's homepage or a list of prebuilt dashboards and Explores that use the installed model and associated data. All users will be able to view the **Applications** option in the left navigation panel; however, users will be able to access only the installed packages that are based on the models to which they have been [granted access permissions](/looker/docs/admin-panel-users-roles#model_sets).

You will see any Explores built for the tool in Looker's **Explore** menu, and you can view the tool's LookML through the **Develop** menu. If you installed a plug-in, the new visualization will be available in the **Visualization** menu in an Explore.

See the [Customizing Looker Marketplace Blocks](/looker/docs/marketplace-customize-blocks) documentation for information on customizing the blocks that you have installed from the Marketplace.

## Managing installed tools

If you have at least the [`develop`](/looker/docs/admin-panel-users-roles#develop), [`manage_models`](/looker/docs/admin-panel-users-roles#manage_models), and [`deploy`](/looker/docs/admin-panel-users-roles#deploy) permissions, you can use the **Manage** page to manage the tools that are installed on your Looker instance.

To navigate to the **Manage** page, follow these steps:

  1. Select the **Marketplace** button on the Looker menu bar storefront.

  2. From the Marketplace menu, select the **Manage** option.

The **Manage** page displays a list of all tools installed on your Looker instance. From the **Manage** page, you can also update tools, open tools, change a tool's configuration, or uninstall tools.