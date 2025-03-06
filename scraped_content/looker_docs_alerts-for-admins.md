# https://cloud.google.com/looker/docs/alerts-for-admins

Depth: 3

Looker has several user permissions that are associated with alerts. Some permissions determine what the user can do with alerts; others determine what destinations a user can send an alert notification to. See the [Roles](/looker/docs/admin-panel-users-roles) documentation page for more information about Looker permissions, including dependencies.

Looker user permissions are distinct from the alert setting called [**Permissions**](/looker/docs/creating-alerts#setting_alert_permissions), which lets the alert's creator determine whether other users will be able to view and potentially follow the alert.

In addition to the permissions that are described in the following table, users need `see_looks` permissions and `see_user_dashboards` and/or `see_lookml_dashboards` permissions for the models on which the dashboard or LookML dashboard tiles, respectively, are based.

Permission | Lets Users | Notes  
---|---|---  
[`admin`](/looker/docs/admin-panel-users-roles#admin) | 

  * See the tile's bell icon: The numeric indicator shows the total number of enabled public alerts on the tile
  * Manage alerts from the [**Alerts**](/looker/docs/admin-panel-alerts-and-schedules-alerts) management admin page, even [private](/looker/docs/creating-alerts#setting_alert_visibility) alerts that are created by other users
  * Access the [**Alert History**](/looker/docs/admin-panel-alerts-and-schedules-alert-history) admin page
  * View, follow, edit, self-assign, and disable any alert on the Looker instance 

| The user must be signed in to Slack from Looker to see alerts that send Slack notifications. | [`see_alerts`](/looker/docs/admin-panel-users-roles#see_alerts) | 

  * Access the [**Alerts**](/looker/docs/admin-panel-alerts-and-schedules-alerts) management admin page
  * View, follow, edit, self-assign, disable any alert on the Looker instance, even [private](/looker/docs/creating-alerts#setting_alert_visibility) alerts that are created by other users
  * Access the [**Alert History**](/looker/docs/admin-panel-alerts-and-schedules-alert-history) admin page

* Users must have permissions to access the alert's underlying content to view or explore from the alert's visualization (in the [**Alert Details**](/looker/docs/admin-panel-alerts-and-schedules-alerts#alert_details_page) page) or to navigate to its dashboard.
* This permission does _not_ grant the ability to create, follow, or delete alerts from the dashboard tile.  
[`create_alerts`](/looker/docs/admin-panel-users-roles#create_alerts) | 

  * See the tile's bell icon: The numeric indicator shows the sum of any public or private alerts that the user has created and other users' alerts that are marked **Public**
  * From the dashboard tile: create, duplicate, and delete their own alerts; duplicate alerts marked **Public** by other users
  * View, edit, disable, and enable their alerts on the [**Manage Alerts** user page](/looker/docs/user-alerts)

| The user must be signed in to Slack to see alerts that send Slack notifications.  
[`follow_alerts`](/looker/docs/admin-panel-users-roles#follow_alerts) | 

  * View and follow [public](/looker/docs/alerts-overview#setting_alert_permissions), [followable](/looker/docs/following-alerts) alerts on a dashboard tile
  * View the alerts that they have followed or for which they are listed as a recipient from the [**Manage Alerts** user page](/looker/docs/user-alerts)

|   
[`schedule_look_emails`](/looker/docs/admin-panel-users-roles#schedule_look_emails) | Send email notifications | Users must also have `create_alerts` permissions.  
[`schedule_external_look_emails`](/looker/docs/admin-panel-users-roles#schedule_external_look_emails) | Send notifications to emails with any domain | Users must also have `create_alerts` permissions.  
[`send_to_integration`](/looker/docs/admin-panel-users-roles#send_to_integration) | Send alert notifications to the [Slack](/looker/docs/scheduling-slack) or [Slack Attachment (API Token)](/looker/docs/best-practices/how-to-use-the-Looker-slack-attachment-api-token-action) integrations, if enabled for the Looker instance | Users must also have `create_alerts` permissions.