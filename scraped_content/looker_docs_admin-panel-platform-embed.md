# https://cloud.google.com/looker/docs/admin-panel-platform-embed

Depth: 3

**Note:** If you are using a [Looker (Google Cloud core)](/looker/docs/looker-core-overview) instance, you will see this page only if you are using the [**Embed** edition](/looker/docs/looker-core-instance-create#create_edition) of Looker (Google Cloud core).

The **Embed** page in the **Platform** section of the **Admin** menu lets you configure settings for embedded Looker content.

**Note:** To access all the admin pages in Looker, you must have the [Admin role](/looker/docs/admin-panel-users-roles#default_roles). If you have a permission that enables only parts of the **Admin** panel, such as [`manage_schedules`](/looker/docs/admin-panel-users-roles#manage_schedules) or [`manage_themes`](/looker/docs/admin-panel-users-roles#manage_themes), but you don't have the Admin role, then Looker may not display the page or pages described in this article in the **Admin** panel. Also, the `see_admin` permission grants read-only permission to most (but not all) Admin pages. See the [`see_admin`](/looker/docs/admin-panel-users-roles#see_admin) description for more information.

## Embedded Domain Allowlist

You need to use this setting to make use of [JavaScript events](/looker/docs/embedded-javascript-events) to pass data or actions between a parent page and a Looker iframe.

In that case, add the domain where the iframe is being used to this field, and then select **Update**.

## Same-Origin Protections for Looker Login Pages

For the Looker login page, you can use the **Same-Origin Protections for Looker Login Pages** setting to indicate whether or not you want to allow cross-origin embedding:

  * **Disabled** : Looker allows cross-origin embedding.
  * **Enabled** : Looker doesn't allow cross-origin embedding.

For certain use cases, you must allow Looker login pages to appear within a Looker iframe even when the parent page is not compatible with the Looker instance's domain name. In these cases, you need to have the **Same-Origin Protections for Looker Login Pages** option set to **Disabled** :

  * If you use [private embedding](/looker/docs/private-embedding) of Looker content in an iframe of a web page hosted by a non-Looker domain, you need to disable **Same-Origin Protections for Looker Login Pages** so that Looker can display the login page in the iframe and allow users to log into Looker.

Set **Same-Origin Protections for Looker Login Pages** to **Enabled** if either of the following is true:

  * You don't embed any Looker content.
  * You use only [signed embedding](/looker/docs/signed-embedding), since the Looker login page isn't used for signed embeds.

To change the setting for same-origin protection, use the pull-down menu to select your desired option, and then be sure to select the **Update** button to save your selection.

## Embed SSO Authentication

The **Embed SSO Authentication** feature needs to be enabled if you want to make use of Looker's [Signed embedding](/looker/docs/signed-embedding) feature. To do so, select **Enabled** and then select **Update**.

## Alerts and scheduling custom url

Unless [disabled](/looker/docs/privatelabel#looker_mentions_in_scheduled_emails), email deliveries from embedded dashboards, either from [alerts](/looker/docs/alerts-overview) or [scheduled deliveries](/looker/docs/scheduling-and-sending-dashboards), include a link that reads **View full dashboard**. This link lets the email recipients connect to their Looker instance and further explore the data delivered in the email.

The **Alerts and scheduling custom url** option lets you configure a custom URL in alerts and scheduled email deliveries that will link embed users to the embedding application, rather than a Looker instance.

**Note:** The embedding application is responsible for authenticating and verifying any user who clicks on the link to return to a custom URL.

### Embed domain for schedules and alerts allowlist

Specify all domains that custom URLs in email deliveries may link to. The domains listed here will populate the [**Domain**](/looker/docs/scheduling-and-sending-dashboards#domain) field in the scheduling and alerts dialogs.

If this field is left blank, custom links are unavailable, since there will be no domain for a user to select in the schedule or alerts dialog.

### Select content path

This drop-down lets you select how the URL in the custom link is formatted. It has the following options:

  * **Only embed domain** — The URL in the custom link includes only the domain selected in the [**Domain**](/looker/docs/scheduling-and-sending-dashboards#domain) field in the scheduling or alerts dialog. For example, `app.customer.com`.

  * **User defined url** — The URL in the custom link includes the domain that is selected in the **Domain** field in the scheduling or alerts dialog and the path that is entered by the user in the [**Path**](/looker/docs/scheduling-and-sending-dashboards#path) field in the scheduling or alerts dialog. For example, `app.customer.com/my_embed_app`.

  * **Embed domain URL with Looker IDs** — The URL in the custom link will include the domain that is selected in the **Domain** field in the scheduling or alerts dialog and the Looker path to the embedded dashboard, using the content ID. For example, `app.customer.com/dashboards/12`.

**Note:** Instances that have a specific license feature enabled will add the Looker path using the dashboard slug, even when this option is selected. If this occurs and you want to use the dashboard ID in the custom link URL, [open a support request](http://console.cloud.google.com/support/cases).
  * **Embed domain URL with Looker slugs** — The URL in the custom link includes the domain that is selected in the **Domain** field in the scheduling or alerts dialog and the Looker path to the embedded dashboard, using the content slug. For example, `app.customer.com/dashboards/CQ1fu99Z9Y1ggq2wcHDfMm`.

**Note:** The slug is a randomly chosen short string that is used as an alternative to the content ID value for use in URLs. In the previous example, CQ1fu99Z9Y1ggq2wcHDfMm is the dashboard slug. You can view a dashboard slug by selecting **Get link** from the dashboard's [three-dot menu](/looker/docs/viewing-dashboards#three-dot_dashboard_menu).

**Select content path** is not available if the **Embed domain for schedules and alerts allowlist** field is left blank.

### URL label

Use this field to enter new default link text, which will replace the text **View full dashboard** in email deliveries. The default text can be changed in the scheduling and alerts dialogs.

## Show Filters on Embedded Looks

Set this option to **Enabled** if you want to display filter values in embedded Looks.

Set this option to **Disabled** to hide filter values in embedded Looks.

Select **Update** to save your setting.

## Remove Look Navigation

The **Remove Look Navigation** feature lets admins further customize embedded content, specifically embedded Explores and embedded dashboards.

### Removing Look navigation from embedded Explores

By default, embed users who have the `explore` and `save_content` [permissions](/looker/docs/signed-embedding#permissions) will see the following options in the [**Explore Actions** gear menu](/looker/docs/viewing-and-interacting-with-explores#the_explore_actions_gear_menu) of an embedded Explore:

  * The option to [**Save as a Look**](/looker/docs/saving-and-editing-looks#saving_looks_from_an_explore)
  * The [**Save & Schedule**](/looker/docs/scheduling) option (for embed users who have the send or scheduling [permissions](/looker/docs/signed-embedding#permissions))

When set to **Enabled** , the **Remove Look Navigation** feature removes all references to Looks, including the options **Save as a Look** and **Save & Schedule**, from the embedded Explore's **Explore Actions** gear menu.

Leave the option set to **Disabled** to keep references to Looks and the options **Save as a Look** and **Save & Schedule** in embedded Explores.

### Removing Look navigation from embedded dashboards

When **Remove Look Navigation** is **Enabled** , references and navigation options to Looks from embedded Explores and embedded [Look-linked](/looker/docs/creating-user-defined-dashboards#look-linked_tiles) dashboard tiles will be removed.

When **Remove Look Navigation** is **Disabled** , embed users will have the option to [**View Look**](/looker/docs/viewing-dashboards#tile_three-dot_menu) in the three-dot **Tile actions** menu in Look-linked tiles.

## Dashboard Embed Content Navigation

When this option is enabled, embedded dashboard viewers who have been granted the necessary [permissions](/looker/docs/signed-embedding#permissions) can [view folders and the Looks and dashboards that they contain](/looker/docs/viewing-embedded-items#viewing_folders_on_embedded_looks_explores_and_dashboards) from embedded dashboards. Enabling this feature is required to let viewers of embedded dashboards [copy, move, and delete dashboards](/looker/docs/viewing-embedded-items#copying_moving_and_deleting_content_on_embedded_dashboards).

## Embed Content Management

When this option is enabled, embedded dashboard viewers who have been granted the necessary [permissions](/looker/docs/signed-embedding#permissions) can [copy, move, and delete dashboards](/looker/docs/viewing-embedded-items#copying_moving_and_deleting_content_on_embedded_dashboards).

## Cookieless Embed

Starting in Looker 23.8, the embed domain can be included when the cookieless session is acquired. This is an alternative to adding the embed domain using the Looker [**Admin > Embed**](/looker/docs/admin-panel-platform-embed) panel. Looker saves the embed domain in the Looker internal database, so it won't be shown on the **Embed** page in the **Admin** panel. Instead, the embed domain is associated with the cookieless session and exists for the duration of the session only. Review the [security best practices](/looker/docs/security-best-practices-embedded-analytics) if you decide to take advantage of this feature.

**Important:** the [Persistent Sessions](/looker/docs/admin-panel-authentication-sessions#persistent_sessions) setting on the [Admin > Authentication > Sessions](/looker/docs/admin-panel-authentication-sessions) panel must also be enabled to use cookieless embedding.

## Embed JWT Secret

**Note:** When the **Embed SSO Authentication** option is **Enabled** and the **Cookieless Embed** option is enabled, this setting is revealed.

A JSON Web Token (JWT) secret is required to make use of the cookieless embed feature. Cookieless embed requires that **Embed SSO Authentication** be enabled, but cookieless embed uses **Embed JWT Secret** instead of **Embed Secret**.

This option lets you set or reset the embed JWT secret. Setting the JWT secret is _not_ necessary, since the very first attempt to create a cookieless embed session will create the JWT token. Unlike the embed secret, the embed JWT secret is never exposed as it is only used internally by the Looker server.

Resetting the JWT token will invalidate _all_ active cookieless embed sessions.

## Embed Secret

**Note:** This setting is revealed only if **Embed SSO Authentication** is set to **Enabled**.

An embed secret is needed to make use of Looker's [signed embedding](/looker/docs/signed-embedding) feature.

To retrieve the embed secret, select the **Set Secret** button.

**Note:** It's important to copy the secret and save it in a safe place immediately, as you cannot retrieve the secret from this page after you leave it.

To change your secret, select the **Reset Secret** button — you should be aware that this will break any existing signed embeds, however.

## Embed URI Validator

**Note:** This setting is only revealed if the **Embed Secret** has been set.

After generating a URL for Looker's [signed embedding](/looker/docs/signed-embedding) feature, you can test the URL by pasting it in the **Embed URI Validator** field and clicking **Test URI**. The URI validator will return a message indicating whether the signed embed URL is valid.

After you enter a signed embed URL, the **Embed URI quick check** section will display the parameters and values that are included in the signed embed URL.