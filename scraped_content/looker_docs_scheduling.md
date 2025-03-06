# https://cloud.google.com/looker/docs/scheduling

Depth: 3

> This page is about delivering content from Looks and Explores. For information about scheduling [dashboards](/looker/docs/viewing-dashboards), visit the [Scheduling and sending dashboards](/looker/docs/scheduling-and-sending-dashboards) documentation page.

Looker provides several ways to [share](/looker/docs/sharing-data) content from dashboards, data tables or visualizations from a Look, or Explore queries to the applications and services that are already a part of your workflow. With Looker's scheduling capability, you can send instant, one-time content deliveries or periodic, recurring content deliveries — also called "schedules" — to one of Looker's built-in delivery destinations or to a third-party service that is [integrated with Looker](/looker/docs/admin-panel-platform-actions#list_of_integrated_services). Built-in delivery destinations include email, webhook, an Amazon S3 bucket, and an SFTP server.

Looker admins and developers play critical roles in configuring schedules so that all Looker users can deliver content. See the following links for documentation that is relevant to each of these roles and to all Looker users.

## Delivery documentation for Looker admins

  * [Enabling user access](/looker/docs/configuring-deliveries) to Looker's content delivery capabilities
  * Managing users' deliveries using the [**Schedules**](/looker/docs/admin-panel-alerts-and-schedules-schedule) page in the **Alerts & Schedules** section of the **Admin** panel
  * Viewing the recent history of the Scheduler's activity from the [Schedule History](/looker/docs/admin-panel-alerts-and-schedules-schedule-history) page in the **Alerts & Schedules** section of the **Admin** panel
  * [Enabling the third-party services](/looker/docs/admin-panel-platform-actions) that are integrated with Looker through the [Looker Action Hub](/looker/docs/action-hub)

## Delivery documentation for Looker developers

  * [Tagging LookML](/looker/docs/reference/param-field-tags) fields to enable deliveries to some integrated services
  * [Configuring datagroups](/looker/docs/reference/param-model-datagroup#creating_a_datagroup_to_schedule_deliveries_on_the_last_day_of_every_month) that can be used to trigger a content delivery

## Delivery documentation for all Looker users

  * [Delivering dashboards](/looker/docs/scheduling-and-sending-dashboards)
  * [Delivering Looks and Explores](/looker/docs/delivering-looks-explores)
  * [Scheduling deliveries to the Slack integration](/looker/docs/scheduling-slack)
  * [Viewing deliveries that you have created](/looker/docs/user-schedules)

## Delivery options

Each type of Looker content has unique delivery options, which are summarized in the following table. Click each link to access the relevant documentation for that delivery option.

Content | Delivery Options | Destination Options | Format Options  
---|---|---|---  
[Explore](/looker/docs/delivering-looks-explores) | One-time | 

  * [email](/looker/docs/delivering-looks-explores#delivery_options_for_email)
  * [webhook](/looker/docs/delivering-looks-explores#delivery_options_for_webhooks)
  * [Amazon S3 bucket](/looker/docs/delivering-looks-explores#delivery_options_for_amazon_s3_buckets)
  * [SFTP server](/looker/docs/delivering-looks-explores#delivery_options_for_sftp_servers)
  * [Admin-enabled integrations ](/looker/docs/delivering-looks-explores#delivery_options_for_third-party_integrations)

| Data Table, Visualization, CSV, XLSX, JSON, Text, HTML  
[Look](/looker/docs/delivering-looks-explores) | One-time, Recurring | 

  * [email](/looker/docs/delivering-looks-explores#delivery_options_for_email)
  * [webhook](/looker/docs/delivering-looks-explores#delivery_options_for_webhooks)
  * [Amazon S3 bucket](/looker/docs/delivering-looks-explores#delivery_options_for_amazon_s3_buckets)
  * [SFTP server](/looker/docs/delivering-looks-explores#delivery_options_for_sftp_servers)
  * [Admin-enabled integrations](/looker/docs/delivering-looks-explores#delivery_options_for_third-party_integrations)

| Data Table, Visualization, CSV, XLSX, JSON, Text, HTML  
[Dashboard](/looker/docs/scheduling-and-sending-dashboards) | One-time, Recurring | 

  * [email](/looker/docs/scheduling-and-sending-dashboards#email)
  * [webhook](/looker/docs/scheduling-and-sending-dashboards#webhook)
  * [Amazon S3 bucket](/looker/docs/scheduling-and-sending-dashboards#amazon_s3)
  * [SFTP server](/looker/docs/scheduling-and-sending-dashboards#sftp)
  * [Admin-enabled integrations](/looker/docs/scheduling-and-sending-dashboards#integrated_service_destinations)

| PDF, Visualization, CSV ZIP file