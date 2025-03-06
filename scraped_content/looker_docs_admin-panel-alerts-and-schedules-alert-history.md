# https://cloud.google.com/looker/docs/admin-panel-alerts-and-schedules-alert-history

Depth: 3

The **Alert History** page in the **Alerts & Schedules** section of the **Admin** menu shows the recent history of all active alerts, including running, complete, and failed alerts.

Looker admins and users who have been granted the [`see_alerts`](/looker/docs/admin-panel-users-roles#see_alerts) permission can manage all active and inactive alerts on the [**Alerts**](/looker/docs/admin-panel-alerts-and-schedules-alerts) management admin page.

An alert query is executed at the frequency that is specified in the alert settings. The purpose of the alert query is to check the query results for the tile on which the alert is based against the threshold values that are defined in the alert conditions. If the conditions have been met, Looker sends a notification according to the alert settings.

## Alert status

At the top of the **Alerts History** page, you can filter the active alert jobs by status:

  * **All** — All alerts, sorted in descending order from most recent
  * **Running** — Only alert jobs that are currently running
  * **Complete** — Only alert jobs that completed successfully
  * **Failed** — Only alert jobs that failed to complete successfully

If a user deletes the dashboard or dashboard tile that the alert is on, that alert will be disabled: Any followers or recipients will no longer receive notifications when the alert conditions are met. Admins and users who have been granted the [`see_alerts`](/looker/docs/admin-panel-users-roles#see_alerts) permission will see immediately that the name of the dashboard has been replaced with a **-** for the alert on the **Alert History** page. After the next time the alert query runs, the alert will be removed.

## Alert history information

Column | Definition  
---|---  
Time | The time when the alert job executed.  
Status | Whether the job is current running, complete, or failed.  
Alert Name | The title of the alert. Clicking this link will direct you to the [**Alerts**](/looker/docs/admin-panel-alerts-and-schedules-alerts) management admin page and filter the results to display only the alert you have clicked. To clear the filter and see all alerts on the [**Alerts**](/looker/docs/admin-panel-alerts-and-schedules-alerts) management admin page, click the **X** icon in the banner.  
Dashboard | The name of the dashboard that contains the tile with the alert. Clicking this link will direct you to the dashboard.  
Owner | The name of the person who created the alert. Clicking this link will direct you to the **Edit User** page for that user.  
Condition Met | A **Yes** or **No** that indicates whether the alert conditions were met when the alert query was last run. A **\--** symbol is displayed if the alert query has not yet run or if the alert query ran but it could not be determined whether the alert conditions were met. This column displays red error or yellow warning icons related to any errors or warnings surfaced when the alert query was run or the alert notification was delivered. See the **Message** column or hover over the error or warning icon to see the associated error message, if applicable.A yellow icon indicates that the data on the dashboard tile did not change between the two most recent alert queries. Read more about this message in the Alert error and warning messages section on this page.  
Message | This column displays messages explaining any errors or warnings surfaced when running the alert query or delivering the alert notification. Read more about these messages in the Alert error and warning messages section on this page.  
Runtime | How long the job ran or has been running.  
  
## Alert error and warning messages

The **Alert History** admin page displays any errors or warnings surfaced when running the alert query or delivering the alert notification. Error messages, if applicable, appear in the **Messages** column or when you hover over the error or warning icon in the **Condition Met** column.

For alerts that are set up to deliver notifications to the [Slack](/looker/docs/alerts-overview#sending_alerts_to_the_slack_integration) or [Slack Attachment (API Token)](/looker/docs/alerts-overview#sending_alerts_to_the_slack_attachment_\(api_token\)_integration) integrations, the error message `Notification delivery failed with existing configuration` appears when the alert query determines that the alert conditions have been met but the notification could not be delivered. This failure may occur if something about the Slack configuration has changed since the alert was created — for example, if the Slack workspace that the alert was delivering to was disconnected from the Looker instance or if the Slack channel that the alert was delivering to was deleted, or if Looker cannot connect to the integrations.

### Warning: Querying fresh data

A warning icon in the **Condition Met** column indicates that the data on the dashboard tile upon which the alert is based did not change between the two most recent alert queries. Hovering over this icon displays the message **Stale Alert Warning** and this text:

`The data for this tile did not change between the two most recent alert queries. Verify that the caching policies defined for this dashboard tile are aligned with the alert frequency.`

There are a few possible explanations for why the data did not change between queries. For example, if the alert creator specified that the tile's data is checked at a [frequency](/looker/docs/alerts-overview#setting_alert_frequency) of **every hour** but the [caching policy](/looker/docs/reference/param-model-datagroup) of the tile's underlying model specifies that the database is checked for updates every six hours, then the alert query will be running on unchanged data. Aligning the alert query and data update frequencies should circumvent this warning.

See more details about how Looker handles caching on the [Caching queries](/looker/docs/caching-and-datagroups) documentation page. See more details about how alert queries work with time series data on the [Setting alerts based on time series data](/looker/docs/best-practices/how-to-set-alerts-based-on-time-series-data) page.

## Managing alerts from the Alert History page

You can manage any alert that is listed in the **Alert History** table. Click on the **Alert Name** to be directed back to the [**Alerts**](/looker/docs/admin-panel-alerts-and-schedules-alerts) management admin page.