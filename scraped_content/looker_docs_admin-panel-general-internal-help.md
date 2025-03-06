# https://cloud.google.com/looker/docs/admin-panel-general-internal-help

Depth: 3

To help users get the most out of Looker, admins can configure a list of company-specific resources with links to wikis, Slack channels, data dictionaries, documentation, key contact information, and other assets. Admins can use the **Internal Help Resources** page in the **General** section of the **Admin** menu to configure this list.

**Note:** To access all the admin pages in Looker, you must have the [Admin role](/looker/docs/admin-panel-users-roles#default_roles). If you have a permission that enables only parts of the **Admin** panel, such as [`manage_schedules`](/looker/docs/admin-panel-users-roles#manage_schedules) or [`manage_themes`](/looker/docs/admin-panel-users-roles#manage_themes), but you don't have the Admin role, then Looker may not display the page or pages described in this article in the **Admin** panel. Also, the `see_admin` permission grants read-only permission to most (but not all) Admin pages. See the [`see_admin`](/looker/docs/admin-panel-users-roles#see_admin) description for more information.

This list is accessible to all Looker users through the drop-down **Help** menu. To access the **Help** menu, click the **Help** icon live_help in the Looker navigation banner.

To create a list of resources in the **Help** menu, follow these steps:

  1. From the **Admin** panel, navigate to the **Internal Help Resources** page.
  2. Once on the page, enable the **Enable Internal Help Resources In The Help Menu** toggle.
  3. Once the feature is enabled, two fields appear that can be edited: 
     * A field in which to enter your organization name. This field can be populated with up to 16 characters. In the user-facing version, the first line will display **Resources for Looker at** and the name you entered.
     * A field in which to enter your list of resources. The text in this field can be styled using [Markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet). You can expand or contract the size of the field by clicking on the lower right corner and dragging the box. Changing the size of this field does not change the size of the dialog box displayed to users.
  4. Click **Save Changes** once you've completed your edits. A **Changes successfully saved** banner will appear.

To edit your resources, follow the preceding steps, with the exception of toggling the **Enable Internal Help Resources In The Help Menu** switch.

To disable the feature, toggle the **Enable Internal Help Resources In The Help Menu** switch to **off**. Any edits you saved will remain, but the list of resources will no longer be available to users.