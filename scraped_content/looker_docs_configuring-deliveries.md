# https://cloud.google.com/looker/docs/configuring-deliveries

Depth: 3

Admins play a critical role in enabling users to deliver Looker content and in configuring the Looker instance for customized content delivery. To manage users' access to and use of Looker's content delivery capabilities, admins can:

  * Grant users permissions to create schedules
  * Manage the scheduled deliveries created by all Looker users

Looker admins can also configure other Looker instance settings that:

  * [Manage the email domains](/looker/docs/admin-panel-general-settings#email_domain_allowlist_for_scheduled_content) to which users can deliver Looker content
  * [Enable the third-party integrations](/looker/docs/admin-panel-platform-actions) to which users can deliver content
  * Implement an instance-wide [application time zone setting](/looker/docs/admin-panel-general-settings#application_time_zone) or set a [user-specified time zone](/looker/docs/admin-panel-general-settings#user_specific_time_zones) for displaying and delivering Looker content
  * Institute an instance-wide [emailed data policy](/looker/docs/admin-panel-alerts-and-schedules-scheduled-emails) to restrict users to sending Looker links only, Looker data only, or both links and data for content deliveries to email
  * Troubleshoot scheduling challenges

## Granting scheduling permissions for users

Scheduling permissions are tied both to the type of Looker content and to the delivery destination.

> See the [Settings](/looker/docs/admin-panel-general-settings#sso-embed) documentation page for information about scheduling permissions for embed users.

### Delivery permissions for content

To deliver each type of Looker content, users need these permissions — and any [permissions](/looker/docs/admin-panel-users-roles#permissions_list) that those permissions depend on — for the model that the content is based on.

The following table provides permission definition summaries as they apply to delivering content. See the [permissions list](/looker/docs/admin-panel-users-roles#permissions_list) in the [Roles](/looker/docs/admin-panel-users-roles) documentation for complete descriptions of each permission.

Permission | Definition  
---|---  
`explore` | Can access Explores.   
`see_looks` | Can access Looks.   
`see_user_dashboards` | Can access user-defined dashboards _and_ the tiles in the dashboards, including Look-linked tiles.   
`see_lookml_dashboards` | Can access LookML dashboards.   
  
Admins may also choose to grant users the `see_schedules` permission, which exposes part of the **Admin** menu for users to access the list of all schedules that exist on the Looker instance from the **Schedules** and **Schedule History** admin pages. Non-admins will not be able to edit or delete schedules from these admin pages; instead, users can [view and manage their own schedules](/looker/docs/user-schedules) from their user profile.

### Delivery permissions for destinations

Admins must also assign users the permissions to deliver content to specific destination types, including Looker's native delivery destinations and any third-party integrations that have been enabled for the Looker instance. Native destinations include:

  * Email
  * [SFTP](https://en.wikipedia.org/wiki/File_Transfer_Protocol#Simple_File_Transfer_Protocol)
  * [webhook](https://en.wikipedia.org/wiki/Webhook)
  * [Amazon S3 bucket](https://aws.amazon.com/s3/)

Looker's [third-party integrated services](/looker/docs/admin-panel-platform-actions#list_of_integrated_services) — also called actions — are delivered through an action hub server. A Looker admin must enable these actions from the [**Actions**](/looker/docs/admin-panel-platform-actions) page in the **Platform** section of the **Admin** panel.

Users must have these permissions — and any [permissions](/looker/docs/admin-panel-users-roles#permissions_list) that those permissions depend on — assigned for the model that the Looker content is based on.

The following table provides permission definition summaries as they apply to delivering content. See the [permissions list](/looker/docs/admin-panel-users-roles#permissions_list) in the [Roles](/looker/docs/admin-panel-users-roles) documentation for complete descriptions of each permission.

Permission | Definition  
---|---  
`admin` | In addition to the capabilities provided by each of the permissions associated with each delivery destination, users with this permission can view all scheduling pages in the **Admin** panel of Looker.   
`schedule_look_emails` | Users can deliver Looker content to email. If no email domains are specified in the [**Email domain allowlist**](/looker/docs/admin-panel-general-settings#email_domain_allowlist) on the **Settings** page of the **Admin** panel, the user can deliver to any email domain.Users can schedule deliveries to occur after a [datagroup](/looker/docs/reference/param-model-datagroup) has been triggered, has managed the cache, and has [rebuilt relevant persisted derived tables (PDTs)](/looker/docs/caching-and-datagroups#using_a_datagroup_for_a_pdt).To send or schedule [System Activity](/looker/docs/system-activity-pages) dashboards, users must have access to all models.  
`schedule_external_look_emails` | Users can deliver Looker content to email. If any email domains are specified in the [**Email domain allowlist**](/looker/docs/admin-panel-general-settings#email_domain_allowlist) on the **Settings** page of the **Admin** panel, the user can deliver to any email domain.  
`send_to_s3` | Users can deliver Looker content to an Amazon S3 bucket. Users can schedule deliveries to occur after a [datagroup](/looker/docs/reference/param-model-datagroup) has been triggered, has managed the cache, and has [rebuilt relevant persisted derived tables (PDTs)](/looker/docs/caching-and-datagroups#using_a_datagroup_for_a_pdt).  
`send_to_sftp` | Users can deliver Looker content using SFTP. Users can schedule deliveries to occur after a [datagroup](/looker/docs/reference/param-model-datagroup) has been triggered, has managed the cache, and has [rebuilt relevant persisted derived tables (PDTs)](/looker/docs/caching-and-datagroups#using_a_datagroup_for_a_pdt).  
`send_outgoing_webhook` | Users can deliver Looker content using webhook. Users can schedule deliveries to occur after a [datagroup](/looker/docs/reference/param-model-datagroup) has been triggered, has managed the cache, and has [rebuilt relevant persisted derived tables (PDTs)](/looker/docs/caching-and-datagroups#using_a_datagroup_for_a_pdt).  
`send_to_integration` | Users can deliver Looker content using [third-party integrated services](/looker/docs/admin-panel-platform-actions#list_of_integrated_services) — also called actions — through an [action hub server](/looker/docs/action-hub). If using [custom actions](/looker/docs/action-hub#building_a_custom_action) with [user attributes](/looker/docs/admin-panel-users-user-attributes), users must have this permission _and_ have a non-null and valid user attribute value for the specified user attribute to deliver Looker content to that action destination.  This permission is not related to the [LookML `action` parameter](/looker/docs/reference/param-field-action).  Users can schedule deliveries to occur after a [datagroup](/looker/docs/reference/param-model-datagroup) has been triggered, has managed the cache, and has [rebuilt relevant persisted derived tables (PDTs)](/looker/docs/caching-and-datagroups#using_a_datagroup_for_a_pdt).  
  
## Managing schedules created by all users

Admins can view, reassign, and delete content delivery schedules from the [**Schedules**](/looker/docs/admin-panel-alerts-and-schedules-schedule) page and can view the history of and troubleshoot scheduled content deliveries from the [**Schedule History**](/looker/docs/admin-panel-alerts-and-schedules-schedule-history) page, both accessible from the **Alerts & Schedules** section of the **Admin** panel. Admins should be careful about deleting or disabling a user who may be the owner of important scheduled deliveries, because such an action will also delete or disable the schedules.

Admins can also monitor what Looker content is being delivered to users with external email domains in the [**External Recipients**](/looker/docs/admin-panel-alerts-and-schedules-scheduled-emails#external_recipients) section of the **Scheduled Emails** admin page.

## Things to consider

  * Content deliveries are always run on [Production Mode](/looker/docs/dev-mode-prod-mode) LookML. Content deliveries cannot be set up by a user who is in Development Mode.

  * Looker schedules data deliveries according to the time zone indicated in the [**Application Time Zone**](/looker/docs/using-time-zone-settings#application_time_zone) setting on the Admin **Settings** page, or, if enabled, the schedule creator's [User Specific Time Zone](/looker/docs/using-time-zone-settings#user_specific_time_zones).

  * If there are valid results [in cache](/looker/docs/caching-and-datagroups#how_looker_uses_cached_queries), Looker will deliver cached results. If there are no results or if the cached results have expired, Looker will rerun the query and cache those results.

  * At times, a scheduled delivery could show that it has been sent successfully but fail to reach one or more of its recipients. This could happen if the underlying model has an error, if the recipient does not have access to the data, or if there are rendering problems or page errors. The destination reports an error if it is unable to connect to the specified endpoint. If such issues occur, Looker sends the person who set up the schedule an email, which includes a link to the content, a list of the recipients it failed to reach, and more information, if available, about the problem that Looker encountered when trying to reach the recipient.

### Known issues with content deliveries

In the **Admin** section of Looker, admins can use the **Scheduler Plans** and **Scheduler History** pages to look up and resolve schedule issues.

Admins should note that deleting or disabling a user may have an effect on schedules owned by that user, schedules based on content owned by that user, or schedules that list that user as a recipient. For more information about how removing user access affects content deliveries, see the [Users](/looker/docs/admin-panel-users-users#removing_user_access) documentation page.

If you encounter any problems with deliveries of large Excel files, see the discussion about managing large files in Excel format on the [Managing business user features](/looker/docs/managing-business-user-features#large_excel_files_hanging_or_not_opening) documentation page.

Certain scheduling options require that admins of [customer-hosted](/looker/docs/glossary#customer-hosted) Looker deployments have installed the [Chromium renderer](/looker/docs/installation-of-rendering-software#chromium) for their Looker instance. Admins can read more about rendering image-based data formats when sending and scheduling dashboards, Looks, or Explores on the [Managing business user features](/looker/docs/managing-business-user-features#rendering_image-based_formats_delivery) documentation page.

See the [Managing business user features](/looker/docs/managing-business-user-features#delivering_content) page for more admin-specific information about scheduling deliveries of Looker content.