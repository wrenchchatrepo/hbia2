# https://cloud.google.com/looker/docs/admin-panel-platform-marketplace

Depth: 3

The [Looker Marketplace](/looker/docs/marketplace) is a central location for finding, deploying, and managing any type of Looker content, such as Looker Blocks, applications, visualizations, and plug-ins.

The **Marketplace** page in the **Platform** section of the **Admin** menu lets you configure settings for the Looker Marketplace.

**Note:** To access all the admin pages in Looker, you must have the [Admin role](/looker/docs/admin-panel-users-roles#default_roles). If you have a permission that enables only parts of the **Admin** panel, such as [`manage_schedules`](/looker/docs/admin-panel-users-roles#manage_schedules) or [`manage_themes`](/looker/docs/admin-panel-users-roles#manage_themes), but you don't have the Admin role, then Looker may not display the page or pages described in this article in the **Admin** panel. Also, the `see_admin` permission grants read-only permission to most (but not all) Admin pages. See the [`see_admin`](/looker/docs/admin-panel-users-roles#see_admin) description for more information.

## Marketplace

The **Marketplace** option enables the [Looker Marketplace](/looker/docs/marketplace). This option is enabled by default. When this option is disabled, the Marketplace icon is hidden, and users won't be able to access the Marketplace to install or manage applications.

## Auto Install

The **Auto Install** option, when enabled, causes some Looker-built applications to automatically install and update on your Looker instance. The [API Explorer](/looker/docs/api-explorer) is the only extension that will automatically install, but more Looker-built applications may be added in the future.

When you enable **Auto Install** , Looker displays the **Enabling Marketplace Auto Install** dialog. The dialog contains license information and a list of necessary entitlements and permissions that are required to install and run Looker-built extensions.

Click **Accept**. Looker will install any Looker-built extensions that are not yet installed. Then, every eight hours, Looker checks to see if there are any Looker-built extensions that need to be installed or updated. If there are, Looker will install the new extension or extensions and make any available updates to existing extensions at that time.

After you accept the license and entitlements, Looker returns you to the **Marketplace** page with **Auto Install** enabled.

If you enable **Auto Install** but do not enable the **Marketplace** option, Looker displays an error and won't run auto install until the **Marketplace** option is enabled.

If the [**Extension Framework**](/looker/docs/admin-panel-platform-extension-framework) option is not enabled, auto install will still occur but any extensions installed will not be available to users until the **Extension Framework** option is enabled.

Any installed Marketplace content, such as the [API Explorer](/looker/docs/api-explorer), can be accessed only by users who have the proper permissions and access to the associated models. For more information, see the [Setting permissions for Looker extensions](/looker/docs/setting-permissions-for-extensions#permissions_to_install_extensions_from_the_looker_marketplace) documentation page.

If you uninstall an auto installable application when **Auto Install** is enabled, the application will no longer be automatically installed and updated. To reverse this, either manually install the application again while **Auto Install** is enabled, or turn **Auto Install** off and back on again.

## Auto Update Looker applications

The **Auto Update Looker applications** option, when enabled, causes some Looker-built applications to automatically update on your Looker instance.

Every eight hours, Looker checks for available updates for the Looker-built applications on your instance. If Looker finds updates, Looker then updates the existing applications.

The **Auto Update Looker applications** option doesn't check any applications for updates.