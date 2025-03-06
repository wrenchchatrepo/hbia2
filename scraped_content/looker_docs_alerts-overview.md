# https://cloud.google.com/looker/docs/alerts-overview

Depth: 3

With alerts, you can specify conditions in your data that, when met or exceeded, trigger a notification to be sent to specific recipients at a desired frequency.

## Alerts overview

Alerts are set on [query-based](/looker/docs/creating-user-defined-dashboards#query_tiles) or [Look-linked](/looker/docs/creating-user-defined-dashboards#look-linked_tiles) tiles on [dashboards](/looker/docs/creating-user-defined-dashboards). Based on the alert's [frequency](/looker/docs/creating-alerts#setting_alert_frequency), Looker checks whether each alert's conditions have been met or exceeded; if so, Looker notifies users of this change.

In addition to creating alerts, users can view, duplicate, and follow some alerts created by other users, depending on their [permissions](/looker/docs/alerts-for-admins). Alert conditions will also take into account any dashboard filters that exist when the alert is created.

## Alerts documentation

See the following links for documentation that is relevant to the Admin role and to all Looker users.

### Alerts documentation for Looker admins

Looker admins play critical roles in configuring alert permissions so that Looker users can create and follow alerts to receive alert notifications.

  * [Configuring alerts for Looker users](/looker/docs/alerts-for-admins) discusses how to configure permissions for creating, following, and managing alerts. [Alerts](/looker/docs/admin-panel-alerts-and-schedules-alerts) discusses the **Alerts** page in the **Alerts & Schedules** section of the **Admin** panel, where admins can see and manage all active and inactive alerts for the Looker instance.
  * [Alert History](/looker/docs/admin-panel-alerts-and-schedules-alert-history) discusses the **Alert History** page in the **Alerts & Schedules** section of the **Admin** panel, which lists information about all active alerts that are running, complete, or failed.

### Alerts documentation for Looker users

  * [Viewing alerts](/looker/docs/viewing-alerts) discusses how to view alerts on a dashboard tile.
  * [Following alerts](/looker/docs/following-alerts) discusses how to follow alerts to receive notifications when alerts are triggered.
  * [Creating alerts](/looker/docs/creating-alerts) discusses how to create an alert.
  * [Modifying alerts](/looker/docs/modifying-alerts) discusses how to edit an existing alert.
  * [Receiving alert notifications](/looker/docs/receiving-alerts) discusses what information is sent in an alert notification.
  * [Effect of dashboard edits on alerts](/looker/docs/effect-of-dashboard-edits-on-alerts) discusses how changes made to dashboard affect any alerts associated with that dashboard.
  * [Viewing alerts that you own or follow](/looker/docs/user-alerts) discusses the **Manage Alerts** page in the Looker UI, which shows a list of all the alerts that a user owns or follows, or for which they are listed as a recipient, depending on their [alerts permissions](/looker/docs/alerts-for-admins).