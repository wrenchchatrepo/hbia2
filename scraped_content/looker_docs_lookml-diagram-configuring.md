# https://cloud.google.com/looker/docs/lookml-diagram-configuring

Depth: 3

The LookML Diagram is an extension — a web application built using Looker components — developed using the Looker [extension framework](/looker/docs/intro-to-extension-framework) and deployed through the [Looker Marketplace](/looker/docs/marketplace). This documentation page describes the tasks that Looker admins must complete before [Looker users can access and use the extension](/looker/docs/lookml-diagram-using), including:

  1. Enable the appropriate features.
  2. Install the LookML Diagram extension.
  3. Grant permissions to access the LookML Diagram.

## Enabling required features

Before installing the LookML Diagram from the [Marketplace](/looker/docs/marketplace), Looker admins must enable these features:

  * [**Marketplace**](/looker/docs/admin-panel-platform-marketplace): To access the Looker Marketplace (enabled by default)
  * [**Extension Framework**](/looker/docs/admin-panel-platform-extension-framework): To deploy extensions developed using the Looker extension framework (enabled by default)

## Installing the LookML Diagram

Installing applications and tools — such as extensions — from the Marketplace requires [`develop`](/looker/docs/admin-panel-users-roles#develop), [`manage_models`](/looker/docs/admin-panel-users-roles#manage-models), and [`deploy`](/looker/docs/admin-panel-users-roles#deploy) [permissions](/looker/docs/admin-panel-users-roles#permissions_list).

The LookML Diagram extension is listed in the **Applications** section of the Looker Marketplace. See the [Using the Looker Marketplace](/looker/docs/marketplace#installing_a_tool_from_the_marketplace) documentation page for more detailed instructions on installing a tool from the Looker Marketplace.

After you've installed the extension, you can ensure that you always have the most updated version by going to the Looker Marketplace, clicking **Manage** , and clicking the **Update** button next to the extension.

## Granting permissions to use the LookML Diagram

After the LookML Diagram is installed, a model called `lookml-diagram` is automatically added to the list of available models on the [**New Model Set**](/looker/docs/admin-panel-users-roles#creating_a_model_set) and [**Edit Model Set**](/looker/docs/admin-panel-users-roles#editing_a_model_set) pages, accessible from the **Roles** page in the **Admin** panel.

Looker admins must enable users to perform certain tasks with the LookML Diagram extension by granting [permissions](/looker/docs/admin-panel-users-roles#permissions_list) to the `lookml-diagram` model and any models the user needs to work with in the LookML Diagram. To enjoy full functionality of the LookML Diagram, users must have `explore` and `deploy` permissions. Refer to the following table for details.

Permission | Depends on | Extension capabilities  
---|---|---  
[`access_data`](/looker/docs/admin-panel-users-roles#access_data) | None | Users can navigate to the extension but won't be able to interact with it.  
[`explore`](/looker/docs/admin-panel-users-roles#explore) | `see_looks`, `access_data` | Users can view and interact with the diagram and can access Explores. **Go to LookML** links are visible but not functional. Users cannot switch or select Git branches in the **Diagram Settings** panel.  
[`develop`](/looker/docs/admin-panel-users-roles#develop) | `see_lookml`, `see_looks`, `access_data` | Users can interact with the diagram and can access LookML project files. **Explore from Field** links are visible but the user is directed to a page that they are not authorized to access. Users cannot switch or select Git branches in the **Diagram Settings** panel.  
[`deploy`](/looker/docs/admin-panel-users-roles#deploy) | `develop`, `see_lookml`, `see_looks`, `access_data` | The same as with `develop` except that users _can_ switch or select Git branches in the **Diagram Settings** panel. Users can use the extension while in Development Mode.  
  
See the [Setting permissions for Looker extensions](/looker/docs/setting-permissions-for-extensions) documentation page for more information on granting users permissions to access and use extensions.