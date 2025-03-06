# https://cloud.google.com/looker/docs/admin-panel-general-support-access

Depth: 3

For assistance with troubleshooting issues, trial implementations, or engagement with Professional Services, you can grant one or more Google employees temporary access to your Looker instance. The **Support Access** page in the **General** section of Looker's **Admin** section lets you enable or disable support access, set the duration for how long Google personnel will have access to your instance, and create an allowlist to specify which individuals will have access to your instance.

**Note:** To access all the admin pages in Looker, you must have the [Admin role](/looker/docs/admin-panel-users-roles#default_roles). If you have a permission that enables only parts of the **Admin** panel, such as [`manage_schedules`](/looker/docs/admin-panel-users-roles#manage_schedules) or [`manage_themes`](/looker/docs/admin-panel-users-roles#manage_themes), but you don't have the Admin role, then Looker may not display the page or pages described in this article in the **Admin** panel. Also, the `see_admin` permission grants read-only permission to most (but not all) Admin pages. See the [`see_admin`](/looker/docs/admin-panel-users-roles#see_admin) description for more information.

> Versions of Looker earlier than 22.0 don't support the ability to grant Google personnel access. If your instance is running a version of Looker earlier than 22.0, you must upgrade to Looker 22.0 or later to grant Google personnel access to your instance.
> 
> If you have a customer-hosted Looker deployment, you must [add Looker's secure gateway IP address to your allowlist](/looker/docs/support-access-customer-hosted-deployment) to enable Looker support to access your Looker application.

## Viewing status in the Help menu

You can view the status of support access in the Looker **Help** menu live_help.

Support access is disabled by default. When access is disabled, the **Help** menu displays **Support Access: Off**. If access is enabled, the help menu shows the remaining time for which access is enabled.

## Viewing status in the Admin section

The **Support Access** panel, like the **Help** menu, indicates whether and for how long support access is enabled. When support access is disabled, the **Support Access** panel shows you the option to enable support access.

When support access is enabled, the **Support Access** panel indicates that support access is open and for how long access will remain open.

**Note:** Looker admins are able to enable or disable support access. To give this ability to Looker developers, give them a [role](/looker/docs/admin-panel-users-roles) with the `support_access_toggle` [permission](/looker/docs/admin-panel-users-roles#permissions_list) (directly or through a [group](/looker/docs/admin-panel-users-groups)).

## Using support access with Looker (Google Cloud core)

When you use support access with [Looker (Google Cloud core)](/looker/docs/looker-core-overview), support access is available only for [public IP instances](/looker/docs/looker-core-networking-options#public_ip_connections). Support access is **not** available for the following types of instances:

  * private IP
  * private IP and public IP
  * Private Service Connect

## Granting access to your Looker instance to Google personnel

To grant one or more Google employees access to your Looker instance, you must enable support access to your instance and specify which individuals will have access in the support access allowlist.

### Enabling support access

**Note:** If you are using a Looker (original) instance and the [Tiered Support Access](/looker/docs/admin-panel-general-labs#tiered_support_access) Labs feature has been disabled, see the Legacy support access section for steps to enable support access.

You can enable support access in the **Enabling Support Access** section on the **Support Access** page in the Looker **Admin** panel. Enabling support access will enable access to your instance for every individual who is listed in the allowlist. To enable support access to your instance, follow these steps:

  1. **Access Duration** : Set the duration for which you want to enable access by entering the number of hours. The default duration is 1 hour. The maximum duration for which you can enable access is 48 hours. Access duration for a user begins when **Update** is clicked to enable support access.

  2. **Access Level** : Set the level of access that you want to grant to all Google Support personnel who are listed in the **Support users with access** section. The access level options are the following:

     * **Support Basic Editor** : A read-only admin role with a [basic set of permissions](/looker/docs/admin-panel-users-roles#support_basic_editor).
     * **Support Advanced Editor** : A read-only admin role with an [advanced set of permissions](/looker/docs/admin-panel-users-roles#support_advanced_editor).

The **Support Basic Editor** and **Support Advanced Editor** roles can be granted only to support users who have been added to the instance through the **Support Access** page and cannot be given to other Looker users.

  3. Select the box to indicate that you understand you are authorizing Google personnel to access your Looker instance.

  4. To update the support setting, click **Update**.

See the Individuals on the allowlist who were previously granted access section for more information on how support access settings affect support users who have already been added to the allowlist.

### Specifying individuals who have access

In the **Support users with access** section, select **Add users to allowlist**. Looker displays the **Add users to allowlist** dialog. To specify the individuals to whom you want to grant access, follow these steps:

  1. Enter a comma-separated list of email addresses of the Google employees to whom you want to grant access to your instance. Only Google personnel whose email address ends in "@google.com" can be granted access.

  2. Select a reason for granting access.

  3. Click **Add to allowlist**.

Once you have added users to your allowlist, they will be listed in the **Support access user** table. If the Google employee has not logged in to your instance, their email address is displayed. If the Google employee has logged in, you will see their name displayed, and their email address won't be displayed again.

The duration of a user's access begins when support access was enabled, not when the user was added or logged in. For example, if `X` hours of support access was enabled and a user was added 3 hours later, that user will have `X`-3 hours of access.

### Access levels for support users

Support users who are added to the allowlist are granted either the [**Support Basic Editor**](/looker/docs/admin-panel-users-roles#support_basic_editor) or the [**Support Advanced Editor** role](/looker/docs/admin-panel-users-roles#support_advanced_editor), depending on the role that is selected in the **Access Level** field. Their permissions within the Looker instance are based on the permissions that are assigned to the selected role. These users cannot be granted other roles or added to [Groups](/looker/docs/admin-panel-users-groups). The `see_admin` permission within each of these roles grants read-only access to many pages in the **Admin** panel; however, users won't have access to the following pages:

  * **Support Access**
  * **Labs**
  * **Legacy Features**
  * **Export**
  * **Content Access**
  * **Actions** (if the page displays only the enabled or disabled states of actions)

Additionally, some features or settings may be hidden on pages that support users do have access to.

If you change the **Access Level** setting for your instance, the update to the role for each support user occurs after that user has logged out and logged back in again.

## Reducing or extending the access duration

**Note:** Reducing or extending access to your instance will limit or extend access for every individual in the allowlist.

You can change the amount of time for which analysts are granted access to your instance in the **Enabling Support Access** section on the **Support Access** panel. To change the amount of time, follow these steps:

  1. Set the duration for which you want to enable access by entering the number of time units and selecting a time unit from the drop-down menu. The maximum duration for which you can enable access is 48 hours.

  2. Select the box to indicate that you understand you are authorizing Google personnel to access your Looker instance.

  3. Click **Update**. If you want to extend access duration by the same duration that is already entered in the **Access Duration** field, click **Update**.

## Disabling access

If support access is enabled for any duration, you can disable all support access by selecting **Revoke** in the **Enabling Support Access** section of the **Support Access** panel. This action will immediately log out all support access users.

You can also disable access to any individual by selecting the **Remove Access** link in that individual's row in the **Support users with access** table.

## Individuals on the allowlist who were previously granted access

**Any time you enable or disable support access, or extend or reduce the duration for which access is granted, this change affects individuals who were previously granted access and are still in the allowlist.**

For example, you grant one day of access to Analyst_A from Looker's Support team to help with some troubleshooting. One week later, you grant access to Analyst_B from Looker's Professional Services department to assist with configuring a model.

When you enable access for Analyst_B, if Analyst_A is still listed in your allowlist you will also grant Analyst_A access. If you no longer want Analyst_A to have access to your instance, you must remove Analyst_A from your allowlist.

This also holds true if you extend the access duration.

For example, if you grant access to Analyst_A to help with troubleshooting for one day and then two weeks later you grant 36 hours of access to Analyst_B to help configure your model, you will have set the support access to be open for 36 hours. In this scenario, you will also have extended access to Analyst_A for 36 hours. If you want to revoke access to Analyst_A after the troubleshooting is complete, you must remove Analyst_A from your allowlist. There is no option to provide different analysts access for different amounts of time.

Similarly, if you update the **Access Level** setting for your instance, all users in the allowlist will now have the updated role that is listed in the setting. In addition, when you click the **Update** button to update the **Access Level** setting, you also reset the clock on the access duration that users have to the hours that are set in the **Access Duration** field.

## Support access audit

The **Support Access Audit** section links to a dashboard that shows data about access to your Looker instance in the most recent 90 days, updated hourly.

The **Changes to Support Access Settings** tile lists the most recent events when your support access settings were changed, and includes:

  * Whether support access to your Looker instance was enabled, disabled, or extended
  * The name of the user who changed the support access setting, or an explanation for automatic changes (such as expiration of the access timer)
  * The time and date the setting change occurred

The **Recent Access** tile shows information about which Google employees have recently accessed your Looker instance, including:

  * The name of the Google employee who accessed your Looker instance
  * The date that the analyst accessed your instance
  * The purpose for which the analyst accessed your instance (this will be one of the following values): 
    * Professional Services support
    * Technical Support
    * Trial Development Support

## Legacy support access

If you are using a Looker (original) instance and the [Tiered Support Access](/looker/docs/admin-panel-general-labs#tiered_support_access) Labs feature has been disabled, the **Support Access** page in the **Admin** section of Looker behaves differently in the following ways:

  * The maximum duration for support access is 90 days.
  * Admins cannot assign the **Support Advanced Editor** or **Support Basic Editor** roles. Any support users added to an instance's allowlist will have the [Admin](/looker/docs/admin-panel-users-roles#admin) role.
  * Support users can be added to Groups.

To enable legacy support access to your instance, follow these steps:

  1. Set the duration for which you want to enable access by entering the number of time units and selecting a time unit from the drop-down menu. The maximum duration for which you can enable access is 90 days.

  2. Select the box to acknowledge that you are authorizing Google personnel to access your Looker instance.

  3. Click **Enable support access**.