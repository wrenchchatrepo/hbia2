# https://cloud.google.com/looker/docs/marketplace-customize-blocks

Depth: 3

Looker Blocks™ are pre-built data models for common analytical patterns and data sources. This page describes how developers can customize Looker Blocks that are installed from the Looker Marketplace. The [Looker Marketplace](/looker/docs/marketplace) is a central location for finding, deploying, and managing many types of Looker content such as applications, visualizations, and plug-ins.

For more information about all [available Looker Blocks](/looker/docs/blocks#available_blocks), including blocks that are not currently available from the Looker Marketplace, as well as alternate block customization methods, see the [Looker Blocks](/looker/docs/blocks) documentation page.

## Requirements for installing and managing Looker Blocks from the Looker Marketplace

Before you can install and use some blocks from the Looker Marketplace, note the following:

  * If you're installing your block through the Looker Marketplace, your Looker admin must enable the [**Marketplace**](/looker/docs/admin-panel-platform-marketplace) feature.
  * Users must have [`develop`](/looker/docs/admin-panel-users-roles#develop), [`manage_models`](/looker/docs/admin-panel-users-roles#manage_models), and [`deploy`](/looker/docs/admin-panel-users-roles#deploy) permissions to install and manage packages from the Marketplace.
  * If the particular block contains a [`local_dependency`](/looker/docs/reference/param-manifest-local-dependency) parameter, the block uses the local project import process. See the [Importing files from other projects](/looker/docs/importing-projects#importing_local_projects) documentation page for details on importing projects. The following blocks contain a `local_dependency` parameter:

    * Digital Marketing Analytics
    * Sales Analytics
    * Web Analytics

See the [Looker Marketplace](/looker/docs/marketplace) documentation page for information on [installing](/looker/docs/marketplace#installing_a_tool_from_the_marketplace) and [managing](/looker/docs/marketplace#managing_installed_tools) Looker Blocks from the Looker Marketplace.

## Accessing the LookML for a Marketplace Block

Blocks that are based on projects that use refinements are [installed from the Marketplace](/looker/docs/marketplace#installing_a_tool_from_the_marketplace) as a single, editable CONFIG project that remotely imports the CORE project, which contains all LookML code and constant parameterization.

Once a block is [installed from the Marketplace](/looker/docs/marketplace#installing_a_tool_from_the_marketplace), you can access its project from the **Develop** menu by clicking the name of the project in the project list. The name of a Marketplace refinements block is typically prepended with **marketplace_** followed by the listing ID.

Although you cannot directly modify a block's read-only CORE project, you may want to use the LookML that is defined in the block's read-only CORE files as a reference when you customize the block's CONFIG files. You can see the block's CORE files by [navigating to the block's project files](/looker/docs/manage-projects#accessing_project_files) in the IDE and expanding the [`imported_projects` directory](/looker/docs/importing-projects#viewing_files_from_an_imported_project) in the IDE file browser.

![](/static/looker/docs/images/dev-customize-blocks-ref-project-files-2108.png)

### Block file structure

When you install a block that is built for refinements, these files are created automatically as part of the CONFIG part of the block project:

Filename | Access | Function  
---|---|---  
`<model_name>.model.lkml` | Read-only for all users | "Virtual" model file that is tied to the block installation; handles the import of any models from the block's CORE project. When a block is uninstalled or updated, the associated model file or files are deleted, preventing model conflicts between multiple block installations.  
`manifest.lkml` | Editable for users with `develop` permissions | Describes the project and its external dependencies. Contains the Marketplace listing ID for the block installation and facilitates the remote import of the block's CORE project files through the `marketplace` keyword.  
`marketplace_lock.lkml` | Read-only for all users | Contains a reference to the [`marketplace_ref`](/looker/docs/reference/marketplace-ref) keyword from the manifest file that handles the remote import of the CORE project. Provides the specific listing, version, and model information that is associated with the installation. Contains information about constants that are configured during [installation](/looker/docs/marketplace#installing_a_tool_from_the_marketplace) (and that can be updated by using the [**Manage**](/looker/docs/marketplace#managing_installed_tools) option in the Marketplace UI).  
`refinements.lkml` | Editable for users with `develop` permissions | Lets developers refine views and Explores defined in the imported CORE project files.  
  
### Customizing a Marketplace Block

> Enable [Development Mode](/looker/docs/dev-mode-prod-mode) to make customizations to the block's editable files.

If you have `develop` permissions, you can customize the LookML in the `refinements.lkml` file of the block's CONFIG project. You can refine the views and Explores that are already defined in the block's CORE project or even add new views and Explores that aren't already defined in the CORE project. Anything that is possible with [LookML refinements](/looker/docs/lookml-refinements) in other LookML projects is possible in the block's `refinements.lkml` file. The combination of the refinement and the original LookML behaves as if it is the original LookML for the object.

You can also make changes to the CONFIG project's `manifest.lkml` file to specify any dependencies that need to be captured for that block.

You are not limited to modifying these files to attain the customizations you want. You can also create new files in the CONFIG project — just be sure to [`include`](/looker/docs/reference/param-model-include) any new files in the `refinements.lkml` file.

#### Customizing the refinements file

If you have `develop` permissions, you can add custom LookML to the CONFIG project to mix in additional data or change the core analytical model of the block. You can create new views and join them to existing Explores, define new fields or redefine existing fields, or apply labels as needed to create a model for the analysis you want to provide. If you've created new files in the CONFIG project, you must [`include`](/looker/docs/reference/param-model-include) them in the refinements file.

For example, say you've installed a block and its `refinements.lkml` file contains:
    
    
    include: "//<listing_id>/**/*.view.lkml"
    include: "//<listing_id>/**/*.explore.lkml"
    

where `listing_id` is the value of the `listing` parameter from the `manifest.lkml` file.

You can use refinements to add a new dimension to a view called `flights`:
    
    
    include: "//<listing_id>/**/*.view.lkml"
    include: "//<listing_id>/**/*.explore.lkml"
    
    view: +flights {
      dimension: air_carrier {
        type: string
        sql: ${TABLE}.air_carrier ;;
      }
    }
    

Or you can apply a label to an Explore called `aircraft` so that it appears in the UI as **Aircraft Simplified** :
    
    
    include: "//<listing_id>/**/*.view.lkml"
    include: "//<listing_id>/**/*.explore.lkml"
    
    explore: +aircraft {
      label: "Aircraft Simplified"
    }
    

The `refinements.lkml` file is included automatically in the block's "virtual" model file, which essentially imports the models from the CORE project.

See the [LookML refinements](/looker/docs/lookml-refinements) documentation for more information about this advanced topic.

#### Customizing the editable manifest file

In blocks that use refinements, both the CORE and CONFIG projects have manifest files; however, only the CONFIG project's manifest file is editable.

You can edit the CONFIG `manifest.lkml` file to add project parameters to those that already appear in the CORE project's manifest file. For example, you can add a `local_dependency` to [join](/looker/docs/reference/param-explore-join) your block to another block on the same Looker instance.

### Updating values for constants

The block's [constants](/looker/docs/reference/param-manifest-constant) are defined in the imported CORE project's manifest file. Overriding a constant's value, if allowed, must be done in the Marketplace UI [during configuration](/looker/docs/marketplace#installing_a_tool_from_the_marketplace) or by updating the block. To update a block, users must have [`develop`](/looker/docs/admin-panel-users-roles#develop), [`manage_models`](/looker/docs/admin-panel-users-roles#manage_models), and [`deploy`](/looker/docs/admin-panel-users-roles#deploy) permissions.

To override a constant's value by updating a block:

  1. In the Looker Marketplace, navigate to the block that you want to update.
  2. Click the **Manage** button.
  3. Next to the name of the block you want to update, click the gear icon. This opens the block configuration window.
  4. Make changes to the constant values as needed.
  5. Click **Update** to close the block configuration window and update the block with your changes.

Your changes are reflected in the read-only `marketplace_lock.lkml` file in your installed project.

## Preserving the customizations from a Marketplace Block that uses extends

Some of the blocks that are available from the Looker Marketplace were composed of projects that use LookML [extends](/looker/docs/reusing-code-with-extends). Looker is converting all Marketplace Blocks for instances on Looker 21.8 or later to a project structure that utilizes [LookML refinements](/looker/docs/lookml-refinements) and will remove support for blocks that are based on [extends](/looker/docs/reusing-code-with-extends).

Looker recommends that you install the refinements-based version of any Marketplace Blocks that you have on your instance as these blocks become available, replacing blocks built with extends. Although this replacement process is simple — you can install the new (refinements) block from the Looker Marketplace Block listing and uninstall the original (extends) block on the **Manage** page in the Looker Marketplace — it will not preserve any of the customizations that may have been made to the block that was built with extends. Looker also will not transfer any Looker content or functions that are based on that content — dashboards, Explores, scheduled content deliveries, alerts — from the original block to the new block.

This section describes how to preserve any customizations to a block built with projects that use extends that would otherwise be difficult or time-consuming to replicate from scratch.

To preserve your block's customizations, a user with the ability to install and manage packages from the Marketplace must:

  1. Update the original block's CONFIG project to prepare for migration
  2. Install the new version of the block from the Looker Marketplace
  3. Transfer the customizations to the new Marketplace Block
  4. Recreate Looker content based on the original block
  5. Uninstall the version of the block that was built with extends

### Updating a customized block to prepare for migration

This section describes how to update key project files in a block that was built with extends so that you can copy over the block's customizations to a new refinements-based version of the block. A block that is based on a project that uses extends is installed from the Marketplace as a read-only CORE project and an editable CONFIG project.

  1. Navigate to the block's CONFIG project from the **Develop** section in one of the following ways:

     * Click the **Projects** option and then click on the name of the project.
     * Click the name of the block's CONFIG project in the list of projects.

CONFIG project names typically end in **_config** , while the name of the CORE project typically does not have a suffix.

  2. Open the project's model file, which may look something like this:

    
    
        explore: ga_sessions_config {
          extends: [ga_sessions_core]
          extension: required
          join: user_sales_data {
            sql_on: ${user_sales_data.full_visitor_id} = ${ga_sessions.full_visitor_id} ;;
          }
          join: sales__by__category {
            sql: LEFT JOIN UNNEST(${user_sales_data.sales_by_category}) as sales__by__category;;
          }
        }
    
        explore: future_input_config {
          extends: [future_input_core]
          extension: required
          join: future_purchase_prediction {
            type: left_outer
            sql_on: ${future_input.full_visitor_id} = ${future_purchase_prediction.full_visitor_id} ;;
            relationship: one_to_one
          }
        }
    
    

  1. In [Development Mode](/looker/docs/dev-mode-prod-mode):

    1. Delete the entire `extends` and `extension` lines.
    2. Delete `_config` from the `explore` names.
    3. Prepend `+` to the `explore` names.

The previous model file example would look like this:

    
    
        explore: +ga_sessions {
          join: user_sales_data {
            sql_on: ${user_sales_data.full_visitor_id} = ${ga_sessions.full_visitor_id} ;;
          }
          join: sales__by__category {
            sql: LEFT JOIN UNNEST(${user_sales_data.sales_by_category}) as sales__by__category;;
          }
        }
    
        explore: +future_input {
          join: future_purchase_prediction {
            type: left_outer
            sql_on: ${future_input.full_visitor_id} = ${future_purchase_prediction.full_visitor_id} ;;
            relationship: one_to_one
          }
        }
    
    

  1. Copy and retain the contents of this file for a future step.

### Installing the new Marketplace Block

A block that is based on a project that uses refinements is installed from the Marketplace as a single, editable LookML project that remotely imports the project containing all LookML and constant parameterization.

  1. Select the shop icon on the Looker menu bar to navigate to the Looker Marketplace.
  2. Click on the listing for the new, refinements-based Marketplace Block. This block has the same name as the existing block that was built with extends.
  3. Click **Install** to install the new block. Once this block is installed, you will see two identical listings on the **Manage** page of the Looker Marketplace.

### Transferring customizations to the new Marketplace Block

This section describes how to transfer the updates that you made to the original (extends) block into the new (refinements) block.

  1. From the **Develop** section, open the new block's project in one of the following ways:

     * Click the **Projects** option and then click on the name of the project.
     * Click the name of the block's project in the list of projects.

The name of a Marketplace refinements block is typically prepended with **marketplace_** followed by the listing ID.

  2. In the `refinements.lkml` file, paste in the updated contents from the original (extends) block's model file. Be sure to retain any [`include`](/looker/docs/reference/param-model-include) statements that are already in the refinements file.

### Recreating Looker content based on the original block

The final step in adopting the refinements-based version of a Marketplace Block is to uninstall the original extends-based version of the block. Some extends-based blocks contain pre-built LookML dashboards and Explores. If users have created [alerts](/looker/docs/alerts-overview) or [scheduled deliveries](/looker/docs/scheduling) that are based on any LookML dashboards defined in the original (extends) block, those alerts or schedules will be disabled or will fail, respectively, once that block is uninstalled from the Looker Marketplace.

You must recreate these alerts or scheduled deliveries on the new (refinements) block's LookML dashboards. Looker admins and users with the appropriate permissions for [schedules](/looker/docs/admin-panel-users-roles#see_schedules) and [alerts](/looker/docs/admin-panel-users-roles#see_alerts) can use the **Alerts & Schedules** pages in the admin section to search for the names of the (extends) block's dashboards and then create new alerts or scheduled deliveries as needed on the (refinements) block's corresponding dashboards.

You also must modify any other Looker content that references the original (extends) block's Explores or LookML dashboards to point to the new (refinements) block, as needed.

### Uninstalling the original block

To uninstall the version of the block that was built with extends:

  1. Select the shop icon on the Looker menu bar to navigate to the Looker Marketplace.

  2. In the Looker Marketplace, select **Manage** in the left side navigation to open the **Manage** page.

  3. On the **Manage** page, click the trash can icon to uninstall the original (extends) block. You can differentiate the extends block list from the refinements block listing by looking at the version numbers. The extends block will be one major version behind the refinements block. For example, the extends block may be version `1.0.4` and the refinements block may be version `2.0.0`.

> Once the block is uninstalled, the original (extends) block listing will disappear from the left navigation in the Looker instance, its Explores will disappear from the **Explore** section, its LookML dashboards will disappear from the **LookML dashboards** folder, and any alerts or scheduled deliveries that are based on the block's LookML dashboards will be disabled or will fail, respectively.

## Troubleshooting a block

If a Marketplace Block displays errors, it's possible that your schema doesn't match the structure of the block.

You may also want to check that the [constants](/looker/docs/reference/param-manifest-constant) that were provided during the block's installation, representing the block's connection, database, or schema, have been defined correctly. To do this, you can:

  1. Select the shop icon on the Looker menu bar to navigate to the Looker Marketplace.

  2. In the Looker Marketplace, select **Manage** in the left side navigation to open the **Manage** page.

  3. On the **Manage** page, click the block's gear icon to view its configuration settings.

  4. In the **Update configurations** window, confirm that the block is configured correctly. Click **Update** after making any changes to save your updates and close the block configuration window.