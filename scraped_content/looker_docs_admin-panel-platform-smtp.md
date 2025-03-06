# https://cloud.google.com/looker/docs/admin-panel-platform-smtp

Depth: 3

Disable comment: 

The **SMTP** page (SMTP stands for _Simple Mail Transfer Protocol_) in the **Platform** section of the **Admin** menu lets you configure your email settings. Looker instances send emails in many situations, including new user notifications, password resets, and administrative notifications, as well as when users [deliver](/looker/docs/scheduling) content such as [dashboards](/looker/docs/scheduling-new-dashboards) and [Looks](/looker/docs/delivering-looks-explores).

**Note:** To access all the admin pages in Looker, you must have the [Admin role](/looker/docs/admin-panel-users-roles#default_roles). If you have a permission that enables only parts of the **Admin** panel, such as [`manage_schedules`](/looker/docs/admin-panel-users-roles#manage_schedules) or [`manage_themes`](/looker/docs/admin-panel-users-roles#manage_themes), but you don't have the Admin role, then Looker may not display the page or pages described in this article in the **Admin** panel. Also, the `see_admin` permission grants read-only permission to most (but not all) Admin pages. See the [`see_admin`](/looker/docs/admin-panel-users-roles#see_admin) description for more information.

## Mail settings

**Deprecated:** For customer-hosted Looker instances, the default Looker email service is not available and the SMTP Options won't be visible. You must configure a different email service for all new customer-hosted instances.

In Looker's **Admin** panel, choose **SMTP** to see and change your instance's SMTP settings. You can use the default mail settings to take advantage of Looker's email service, without the need for additional configuration.

To use a different email service, select **Use custom mail settings**.

![](/static/looker/docs/images/menu-admin-smtp-custom-720-2.png)

Custom mail settings can be configured for SMTP servers that support the [`PLAIN` and `LOGIN` authentication protocols](https://en.wikipedia.org/wiki/SMTP_Authentication#Details).

Enter the appropriate values for your email service's SMTP settings:

  * **Mail Server** : The URL of your SMTP server. Any changes to this setting require the Looker admin to also change the SMTP server password.
  * **From** : The name to display as the sender of your Looker emails (see Testing Custom Email Settings for an example). You can enter a name string and an email address encased in angle brackets (for example, **Display Name <email@address.com>**) or an email address without angle brackets (for example, **email@address.com**). Special characters, other than the `@` symbol in an email address and the surrounding angle brackets, if applicable, are not supported.
  * **User Name** : The username that's needed to gain access to your SMTP server.
  * **Password** : The password that's needed to gain access to your SMTP server.
  * **Port** : The port to use for your SMTP server. Any changes to this setting require the Looker admin to also change the SMTP server password.

> Looker instances hosted on Google Cloud cannot use port 25 for SMTP. Google Cloud blocks all traffic on port 25. For more information, see the [Sending email from an instance](/compute/docs/tutorials/sending-mail) page in the Google Cloud documentation. Using port 25 for SMTP on Looker instances hosted on Microsoft Azure is not recommended and may result in errors. For more information, see the [Troubleshooting outbound SMTP connectivity](https://docs.microsoft.com/en-us/azure/virtual-network/troubleshoot-outbound-smtp-connectivity) page in the Azure documentation.

  * **TLS/SSL** : If your SMTP server uses the TLS or SSL protocols for more secure email, select this option. Looker displays a drop-down menu of supported TLS and SSL versions. Select your protocol version. For TLS, TLS 1.2 is recommended.

Once you have entered your SMTP settings, click the **Save** button to save your configuration. You can also test your settings, or refresh the page to see if your configuration has any errors.

> If you are using custom mail settings for SMTP, add [Looker's IP addresses](/looker/docs/enabling-secure-db-access#option_1:_ip_address_allowlist) to your SMTP server's IP allowlist so that your SMTP server will allow inbound traffic from Looker.

Looker restricts how often Looker admins can save or test the SMTP settings to prevent using this feature to scan for open ports.

## Testing custom email settings

To test your custom email setup, use the **Send Test Email** button. Looker will attempt to send a test email to the user who pressed the button. The test email has the following attributes:

  * The sender is `admin@looker.com`.
  * The subject is `Looker Mail Test`.
  * The email body text is `Looker mail is working!`

To prevent malicious agents from scanning for open ports, Looker restricts how frequently Looker admins can test the SMTP settings.

## SMTP error messages

If there are any problems with your SMTP configuration, Looker alerts all admins in the following locations:

  * A warning message on the **SMTP** page
  * A warning icon next to the **SMTP** listing in the **Admin** sidebar

These errors are visible to all admins on your Looker instance. You can check for errors immediately by refreshing the page after saving custom mail settings.

Errors related to custom email settings tests appear below the **Save** and **Send Test Email** buttons at the bottom of the **SMTP** page.