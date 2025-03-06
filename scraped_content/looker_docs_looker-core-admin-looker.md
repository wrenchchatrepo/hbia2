# https://cloud.google.com/looker/docs/looker-core-admin-looker

Depth: 3

You can administer many settings of a Looker (Google Cloud core) instance's tasks within the **Admin** section of the instance.

## Required permission

To manage users within a Looker (Google Cloud core) instance, you must have the [Admin role](/looker/docs/admin-panel-users-roles#default_permission_sets) within Looker.

## Administrative settings available within the Looker (Google Cloud core) instance

You can refer to the list of [Administrative tutorials](/looker/docs/set-up-and-administer-looker#administrative-tutorials) for how to perform various administrative tasks for users of your instance. Additionally, the following documentation pages describe Looker's administration functions for the latest version of Looker. Exceptions for Looker (Google Cloud core) instances are noted on this page.

  * [**General** pages](/looker/docs/admin-panel-general-pages) — View a list of pages about setting system-wide options, creating a custom help page for your users, setting a default homepage for your instance or for a user or group.

> The following **General** Admin panel features have moved or changed for Looker (Google Cloud core):
> 
>     * The [**Labs**](/looker/docs/admin-panel-general-labs) and [**Legacy features**](/looker/docs/legacy-feature-schedule) Admin panel pages are not available for Looker (Google Cloud core) instances. Labs and legacy features default to off in Looker (Google Cloud core).
>     * The [**Support Access**](/looker/docs/admin-panel-general-support-access) Admin panel page is available in Looker (Google Cloud core). However, support access is only available for public IP instances. See the [Getting support for Looker (Google Cloud core)](/looker/docs/looker-core-support) documentation page for information about accessing support.
>     * The [**Technical Contacts**](/looker/docs/admin-panel-general-settings#technical_contacts) setting is now managed [within the Google Cloud console](/resource-manager/docs/managing-notification-contacts).
>     * The [**Email Domain Allowlist**](/looker/docs/admin-panel-general-settings#email_domain_allowlist_for_scheduled_content) setting has moved into the Google Cloud console. See the [Edit the Looker (Google Cloud core) instance configuration](/looker/docs/looker-core-view-console#edit_instance_settings) documentation for instructions on setting the email domain allowlist.
>     * The [**Host URL**](/looker/docs/admin-panel-general-settings#host_url) setting has moved into the Google Cloud console. See the [Set up a custom domain for a Looker (Google Cloud core) instance](/looker/docs/looker-core-custom-domain) documentation page for information on setting up a custom domain.
>     * The [**License Key**](/looker/docs/admin-panel-general-settings#license_key) setting is not available in Looker (Google Cloud core) instances.
>     * The [**Export**](/looker/docs/admin-panel-export) page is not available in Looker (Google Cloud core). To export a Looker (Google Cloud core) instance, follow the steps on the [Import or export data from a Looker (Google Cloud core) instance](/looker/docs/looker-core-import-export) documentation page.

  * [**System Activity** pages](/looker/docs/system-activity-pages) — View information about the System Activity dashboards, which show user activity, content activity, and performance data for your Looker instance.

> The following **System Activity** Admin panel features have moved or changed for Looker (Google Cloud core):
> 
>     * Performance recommendations are not available for Looker (Google Cloud core) instances.
>     * [Elite System Activity](/looker/docs/elite-system-activity) is available for **Enterprise** and **Embed** [editions](/looker/docs/looker-core-instance-create#create_edition) of Looker (Google Cloud core), but not for the **Standard** edition.

  * [**Users** pages](/looker/docs/admin-panel-users-pages) — View a list of pages about configuring users, groups, roles, and user attributes; managing user and group access to saved content; and viewing and resetting locked user accounts.

> The following **Users** Admin panel features have moved or changed for Looker (Google Cloud core):
> 
>     * The **Users** page functions slightly differently in Looker (Google Cloud core). See the [Manage users within Looker (Google Cloud core)](/looker/docs/looker-core-user-management#the_users_page) documentation page for details on using the **Users** page with Looker (Google Cloud core).
>     * The [**Custom Welcome Email**](/looker/docs/admin-panel-users-custom-welcome-email) Admin panel page is not available in Looker (Google Cloud core) instances.

  * [**Database** pages](/looker/docs/admin-panel-database-pages) — View a list of pages about configured database connections, database query history, persistent derived tables, and datagroups.

> The following **Database** Admin panel features have moved or changed for Looker (Google Cloud core):
> 
>     * The [**SSH Server** tab](/looker/docs/admin-panel-database-connections#ssh_servers_tab) is not available for Looker (Google Cloud core) instances.

  * [**Alerts & Schedules** pages](/looker/docs/admin-panel-alerts-and-schedules-pages) — View a list of pages about managing user alerts and schedules, viewing alert and schedule histories, specifying an emailed data policy, and monitoring data that is sent to external email addresses.

  * [**Platform** pages](/looker/docs/admin-panel-platform-pages) — View a list of pages about setting system-wide options for integrated services, Looker's API, embedded content, email deliveries, and custom visualization types.

> The following **Platform** Admin panel features have moved or changed for Looker (Google Cloud core):
> 
>     * The Looker Action Hub on the [**Actions** page](/looker/docs/admin-panel-platform-actions) is available only for [public IP network connections](/looker/docs/looker-core-networking-options#public_ip_connections).
> 
>     * The [**BI Connectors** page](/looker/docs/bi-connectors) is available only for [public IP](/looker/docs/looker-core-networking-options#public_ip_connections) or [both public IP and private IP](/looker/docs/looker-core-networking-options#both_public_and_private_ip_connections) network connections. Additionally, all BI connectors are enabled by default for Looker (Google Cloud core) instances that use public IP or both public IP and private IP.
> 
>     * The [**Marketplace** page](/looker/docs/admin-panel-platform-marketplace) isn't available in private IP Looker (Google Cloud core) instances or instances that use both public IP and private IP. However, Marketplace resources can be installed manually on Looker (Google Cloud core) instances. See the [Feature availability in Looker (Google Cloud core)](/looker/docs/looker-core-feature-differences#looker_marketplace) documentation page for more information.
> 
>     * The [**Themes**](/looker/docs/themes-for-embedded-dashboards-and-explores) page is available for the **Enterprise** and **Embed** [editions](/looker/docs/looker-core-instance-create#create_edition) of Looker (Google Cloud core), but not for the **Standard** edition.
> 
>     * The [**Embed**](/looker/docs/admin-panel-platform-embed) and [**Private Label**](/looker/docs/privatelabel) pages are available for the **Embed** [edition](/looker/docs/looker-core-instance-create#create_edition) of Looker (Google Cloud core), but not for the **Standard** or **Enterprise** editions.
> 
>     * The [**Gemini in Looker**](/looker/docs/admin-panel-platform-gil) page is available for all [editions](/looker/docs/looker-core-instance-create#create_edition) of Looker (Google Cloud core). For Looker (Google Cloud core) instances, Gemini in Looker is [enabled and administered](/looker/docs/looker-core-admin-gemini) in the Google Cloud console.

  * [**Authentication** pages](/looker/docs/admin-panel-authentication-pages) — View a list of pages about configuring various authentication methods, including passwords and two-factor authentication, along with configuring options to allow users to stay logged in to Looker.

> The following **Authentication** Admin panel features have moved or changed for Looker (Google Cloud core):
> 
>     * Setting up the Google OAuth client and credentials now happens [within the Google Cloud console](/looker/docs/looker-core-create-oauth). For Looker (Google Cloud core), the [**Google authentication**](/looker/docs/looker-core-oauth-authentication) page is used only to set the [default Looker role](/looker/docs/looker-core-oauth-authentication#setting_a_default_looker_role_within_the_instance) and [merge options](/looker/docs/looker-core-oauth-authentication#specify_the_method_used_to_merge_oauth_users_to_a_account).
>     * The [**Passwords**](/looker/docs/admin-panel-authentication-password), [**Two-Factor**](/looker/docs/admin-panel-authentication-two-factor), and [**LDAP**](/looker/docs/admin-panel-authentication-ldap) pages are not available for Looker (Google Cloud core).

  * The [**Server** pages](/looker/docs/admin-panel-server-pages) are not available for Looker (Google Cloud core).

## What's next

  * [Administer your Looker (Google Cloud core) instance from the Google Cloud console](/looker/docs/looker-core-admin-console)
  * [Authentication methods for Looker (Google Cloud core)](/looker/docs/looker-core-user-authentication)
  * [Manage users within Looker (Google Cloud core)](/looker/docs/looker-core-user-management)