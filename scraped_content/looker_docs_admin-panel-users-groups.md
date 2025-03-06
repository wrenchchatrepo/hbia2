# https://cloud.google.com/looker/docs/admin-panel-users-groups

Depth: 3

The **Groups** page in the **Users** section of the **Admin** menu lists all the user groups on your Looker instance. Placing users into groups is helpful for managing [folder access](/looker/docs/organizing-spaces) and [other permissions](/looker/docs/access-control-and-permission-management).

Consider creating groups related to the type of content they handle. Users can [filter the Top Content by group](/looker/docs/finding-content#viewing_top_content) so good group design can help them find the content they need.

**Note:** To access all the admin pages in Looker, you must have the [Admin role](/looker/docs/admin-panel-users-roles#default_roles). If you have a permission that enables only parts of the **Admin** panel, such as [`manage_schedules`](/looker/docs/admin-panel-users-roles#manage_schedules) or [`manage_themes`](/looker/docs/admin-panel-users-roles#manage_themes), but you don't have the Admin role, then Looker may not display the page or pages described in this article in the **Admin** panel. Also, the `see_admin` permission grants read-only permission to most (but not all) Admin pages. See the [`see_admin`](/looker/docs/admin-panel-users-roles#see_admin) description for more information.

## Viewing and searching groups

The **Groups** page shows the following information:

![](/static/looker/docs/images/admin-groups-2308.png)

  1. You can use the **Filter List** field to limit which groups are displayed. When you click the **Filter List** field, you are given the choice to filter on ID or group name. When you filter on ID, entering a group ID will display that group. In the case of group name, when you enter any string, the list of groups displayed will show all the groups whose name contains the string you entered in the filter field.
  2. You can sort the table by group name in either ascending or descending order by clicking the **Group** column heading.
  3. Each row lists the group name and the group ID assigned to the group. Click on the row to edit the group to add or remove users. Groups that cannot be edited, either because they are system-created groups (such as the All Users group), or because they are externally managed by [LDAP](/looker/docs/admin-panel-authentication-ldap#groups_and_roles), [SAML](/looker/docs/admin-panel-authentication-saml#groups_and_roles), or [OpenID Connect](/looker/docs/admin-panel-authentication-openid-connect#groups_and_roles) protocols, are indicated by a lock on the group icon.
  4. The **Role** column lists any roles assigned to the group.
  5. The **Users** column shows how many members, either users or other groups, belong to the group.
  6. You can click **Add Group** to add a new group. Looker will display a dialog where you can type the name of the new group. After you click the **Create** button, Looker adds the group to the **Groups** page. You can then edit the group to add or remove users.
  7. You can hover over a group to display the three-dot menu at the right. You can use the three-dot menu to delete the group. If you choose to delete a group, Looker will ask you to confirm.

**Warning:** Deleting a group is irreversible. Deleting a group while it is still in use can impact a wide variety of user permissions, which can prevent users from accessing the folders or features they are used to.

## Editing groups

To edit a group, click the row the group is in. There you can view and adjust several settings:

![](/static/looker/docs/images/admin-edit-group-2116.png)

  1. You can use the **Filter List** field to limit which groups members are displayed. When you click the **Filter List** field, you are given the choice to filter on member ID or member name. When you filter on member ID, entering a member ID will display that group member. In the case of member name, when you enter any string, the list of group members displayed will show all the group members whose name contains the string you entered in the filter field.
  2. Each row shows a member of the group with an icon indicating whether the member is an individual user or another group. The row lists the user or group ID and, in the case of a user, the user's primary login credential.
  3. If the group member is a user, the **Active Credential** column shows the type of credentials the user can use to log in to Looker. If the group member is another group, the **Active Credential** column shows how many users are in the member group.
  4. You can hover over a row to display the three-dot menu for that group member at the right. You can use the three-dot menu to remove that member from the group. If you choose to remove the member, Looker will ask you to confirm.
  5. You can click **Add Members** to add a user or another group as a member of the group. Looker will display a dialog where you can search for a username or group name and add the user or group as a member.
  6. You can click the group's three-dot menu to rename the group or delete the group. If you choose to delete the group, Looker will ask you to confirm.

**Warning:** Deleting a group is irreversible. Deleting a group while it is still in use can impact a wide variety of user permissions, which can prevent users from accessing the folders or features they are used to.

## Adding roles to groups

To assign a role to a group, use the **Roles** page in the **Users** section of the **Admin** menu. From there, you can edit the role and assign a group or groups to that role. For more information, see the [Roles](/looker/docs/admin-panel-users-roles#assigning_roles) documentation page.

## Deleting groups

To delete a group, click the **Delete** button on the right side of its row. Looker displays a confirmation dialog before you delete the group.

**Warning:** Deleting a group is irreversible. Deleting a group while it is still in use can impact a wide variety of user permissions, which can prevent users from accessing the folders or features they are used to.