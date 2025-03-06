# https://cloud.google.com/looker/docs/admin-panel-authentication-saml

Depth: 3

**Note:** Customers who use [Looker (Google Cloud core)](/looker/docs/looker-core-overview) should be aware of their responsibility for controlling access and permissions when using third-party identity providers. For details, refer to the [Our shared security partnership](/looker/product/security) page.

The **SAML** page in the **Authentication** section of the **Admin** menu lets you configure Looker to authenticate users using Security Assertion Markup Language (SAML). This page describes that process and includes instructions for linking SAML groups to Looker roles and permissions.

## Requirements

Looker displays the **SAML** page in the **Authentication** section of the **Admin** menu only if the following conditions are met:

  * You have the [Admin role](/looker/docs/admin-panel-users-roles#default_roles).
  * Your Looker instance is enabled to use SAML.

If these conditions are met, and you don't see the **SAML** page, [open a support request](http://console.cloud.google.com/support/cases) to enable SAML on your instance.

## SAML and identity providers

Companies use different identity providers (IdPs) to coordinate with SAML (for example, Okta or OneLogin). The terms used in the following setup instructions and in the UI may not directly match those used by your IdP. For clarifications during setup, contact your internal SAML or authentication team, or reach out to Looker Support.

Looker assumes that SAML requests and assertions will be **compressed** ; ensure that your IdP is configured as such. Looker's requests to the IdP aren't signed.

Looker supports IdP-initiated login.

Some of the setup process must be completed on the IdP's website.

[Okta offers a Looker app](https://saml-doc.okta.com/SAML_Docs/How-to-Configure-SAML-2.0-for-Looker.html), which is the recommended way to configure Looker and Okta together.

### Setting up Looker on your identity provider

Your SAML IdP will need the Looker instance URL to which the SAML IdP should POST SAML assertions. In your IdP, this might be called "Post Back URL," "Recipient," or "Destination," among other names.

The information to provide is the URL where you typically access your Looker instance using the browser, followed by `/samlcallback`. For example: `none https://instance_name.looker.com/samlcallback`

or
    
    
    https://looker.mycompany.com/samlcallback
    

Some IdPs also require you add `:9999` after your instance URL. For example:
    
    
    https://instance_name.looker.com:9999/samlcallback
    

## Things to know

Keep the following facts in mind:

  * Looker requires SAML 2.0.
  * Don't disable SAML authentication while you are logged in to Looker through SAML unless you have an alternate account login set up. **Otherwise, you could lock yourself out of the app.**
  * Looker can migrate existing accounts to SAML by using email addresses that come either from current email and password setups or from Google Auth, LDAP, or OIDC. You will be able to configure how existing accounts are migrated in the setup process.

## Getting started

Navigate to the **SAML Authentication** page in the **Admin** section of Looker to see the following configuration options. Note that any changes to configuration options don't take effect until you test and save your settings at the bottom of the page.

## SAML auth settings

Looker requires the **IdP URL** , **IdP Issuer** , and **IdP Certificate** to authenticate your IdP.

Your IdP may offer an IdP metadata XML document during the configuration process for Looker on the IdP side. This file contains all the information requested in the **SAML Auth Settings** section. If you have this file, you can upload it in the **IdP Metadata** field, which will populate the required fields in this section. Alternatively, you can fill out the required fields from the output obtained during the IdP-side configuration. **You don't need to fill out the fields if you upload the XML file.**

  * **IdP Metadata (Optional)** : Either paste the public URL of the XML document that contains the IdP information, or paste the document's text in its entirety here. Looker will parse that file to populate the required fields.

If you didn't upload or paste an IdP metadata XML document, instead enter your IdP authentication information in the **IdP URL** , **IdP Issuer** , and **IdP Certificate** fields.

  * **IdP URL** : The URL where Looker will go to authenticate users. This is called the _Redirect URL_ in Okta.

  * **IdP Issuer** : The unique identifier of the IdP. This is called "External Key" in Okta.

  * **IdP Certificate** : The public key to let Looker verify the signature of IdP responses.

Taken together, these three fields let Looker confirm that a set of signed SAML assertions actually came from a trusted IdP.

  * **SP Entity/IdP Audience** : This field isn't required by Looker, but many IdPs will require this field. If you enter a value in this field, that value will be sent to your IdP as Looker's `Entity ID` in authorization requests. In that case, Looker will only accept authorization responses that have this value as the `Audience`. If your IdP requires an `Audience` value, enter that string here.

**Note:** This value is also used as the **issuer** field in messages sent to the IdP. So, if your IdP complains that it is receiving a message without an **issuer** , then you need to fill this in. You can use whatever string your IdP might require. In most cases you can use **Looker**. If this field is present, then your IdP _must_ send it as the **audience** field in the message it sends back to Looker.

  * **Allowed Clock Drift** : The number of seconds of clock drift (the difference in timestamps between the IdP and Looker) allowed. This value will usually be the default of 0, but some IdPs may require extra leeway for successful logins.

## User attributes settings

In the following fields, specify the attribute name in your IdP's SAML configuration that contains the corresponding information for each field. Entering the SAML attribute names tells Looker how to map those fields and extract their information at login time. Looker isn't particular about how this information is constructed, it's just important that the way you input it into Looker matches the way that the attributes are defined in your IdP. Looker provides default suggestions about how to construct those inputs.

### Standard attributes

You'll need to specify these standard attributes:

  * **Email Attr** : The attribute name your IdP uses for user email addresses.

  * **FName Attr** : The attribute name your IdP uses for user first names.

  * **LName Attr** : The attribute name your IdP uses for user last names.

### Pairing SAML attributes with Looker user attributes

You can optionally use the data in your SAML attributes to automatically populate values in Looker [user attributes](/looker/docs/admin-panel-users-user-attributes) when a user logs in. For example, if you have configured SAML to make user-specific connections to your database, you could pair your SAML attributes with Looker user attributes to [make your database connections user-specific](/looker/docs/admin-panel-users-user-attributes#connections) in Looker.

To pair SAML attributes with corresponding Looker user attributes:

  1. Enter the name of the SAML attribute in the **SAML Attribute** field and the name of the Looker user attribute you want to pair it with in the **Looker User Attributes** field.
  2. Check **Required** if you want to require a SAML attribute value to allow a user to log in.
  3. Click **+** and repeat these steps to add more attribute pairs.

## Groups and roles

You have the option for Looker to create [groups](/looker/docs/admin-panel-users-groups) that mirror your externally managed SAML groups, and then assign Looker [roles](/looker/docs/admin-panel-users-roles) to users based on their mirrored SAML groups. When you make changes to your SAML group membership, those changes are automatically propagated into Looker's group configuration.

Mirroring SAML groups lets you use your externally defined SAML directory to manage Looker groups and users. This, in turn, lets you manage your group membership for multiple software as a service (SaaS) tools, such as Looker, in one place.

If you turn on **Mirror SAML Groups** , then Looker will make one Looker group for every SAML group that is introduced into the system. Those Looker groups can be viewed on the [**Groups** page](/looker/docs/admin-panel-users-groups) of the **Admin** section of Looker. Groups can be used for assigning [roles](/looker/docs/admin-panel-users-roles) to group members, setting [content access controls](/looker/docs/admin-panel-users-content-access), and assigning [user attributes](/looker/docs/admin-panel-users-user-attributes).

### Default groups and roles

By default, the **Mirror SAML Groups** switch is off. In this case, you can set a default group for new SAML users. In the **New User Groups** and **New User Roles** fields, enter the names of any Looker groups or roles to which you want to assign new Looker users when they first log in to Looker:

These groups and roles are applied to new users at their initial login. The groups and roles aren't applied to pre-existing users, and they aren't reapplied if they are removed from users after the users' initial login.

If you later enable mirror SAML groups, these defaults will be removed for users upon their next login and replaced by roles assigned in the **Mirror SAML Groups** section. These default options will no longer be available or assigned, and they will be fully replaced by the mirrored groups configuration.

### Enabling mirror SAML groups

If you choose to mirror your SAML groups within Looker, turn on the **Mirror SAML Groups** switch. Looker displays these settings:

**Group Finder Strategy** : Select the system the IdP uses to assign groups, which depends on your IdP.

  * Almost all IdPs use a single attribute value to assign groups, as shown in this sample SAML assertion: `none <saml2:Attribute Name='Groups'> <saml2:AttributeValue >Everyone</saml2:AttributeValue> <saml2:AttributeValue >Admins</saml2:AttributeValue> </saml2:Attribute>` In this case, select **Groups as values of single attributes**.

  * Some IdPs use a separate attribute for each group and then require a second attribute to determine whether a user is a member of a group. A sample SAML assertion showing this system follows: `none <saml2:Attribute Name='group_everyone'> <saml2:AttributeValue >yes</saml2:AttributeValue> </saml2:Attribute> <saml2:Attribute Name='group_admins'> <saml2:AttributeValue >no</saml2:AttributeValue> </saml2:Attribute>` In this case, select **Groups as individual attributes with membership value**.

**Groups Attribute** : Looker displays this field when the **Group Finder Strategy** is set to **Groups as values of single attribute**. Enter the name of the **Groups Attribute** used by the IdP.

**Group Member Value** : Looker displays this field when the **Group Finder Strategy** is set to **Groups as individual attributes with membership value**. Enter the value that indicates that a user is a member of a group.

**Preferred Group Name/Roles/SAML Group ID** : This set of fields lets you assign a custom group name and one or more roles that are assigned to the corresponding SAML group in Looker:

  1. Enter the SAML group ID in the **SAML Group ID** field. For Okta users, enter the Okta group name as the SAML group ID. SAML users who are included in the SAML group will be added to the mirrored group within Looker.

  2. Enter a custom name for the mirrored group in the **Custom Name** field. This is the name that will be displayed on the [**Groups** page](/looker/docs/admin-panel-users-groups) of the **Admin** section of Looker.

  3. In the field to the right of the **Custom Name** field, select one or more Looker [roles](/looker/docs/admin-panel-users-roles) that will be assigned to each user in the group.

  4. Click `+` to add additional sets of fields to configure additional mirrored groups. If you have multiple groups configured and want to remove the configuration for a group, click `X` next to that group's set of fields.

If you edit a mirrored group that was previously configured in this screen, the configuration of the group will change but the group itself will remain intact. For example, you could change the custom name of a group, which would change how the group appears in Looker's **Groups** page but wouldn't change the assigned roles and group members. Changing the **SAML Group ID** would maintain the group name and roles, but members of the group would be reassigned based on the users who are members of the external SAML group that has the new SAML group UD.

Any edits made to a mirrored group will be applied to users of that group when they next log in to Looker.

### Advanced role management

If you have enabled the **Mirror SAML Groups** switch, Looker displays these settings. The options in this section determine how much flexibility Looker admins have when configuring Looker groups and users who have been mirrored from SAML.

For example, if you want your Looker group and user configuration to strictly match your SAML configuration, turn on these options. When all of the first three options are enabled, Looker admins cannot modify mirrored groups memberships and can only assign roles to users through SAML mirrored groups.

If you want to have more flexibility to customize your groups within Looker, turn off these options. Your Looker groups will still mirror your SAML configuration, but you will be able to do additional group and user management within Looker, such as adding SAML users to Looker-specific groups or assigning Looker roles directly to SAML users.

For new Looker instances, or for instances that have no previously configured mirrored groups, these options are off by default.

For existing Looker instances that have configured mirrored groups, these options are on by default.

**Warning:** Turning on more restrictive settings will cause users to **lose group membership or assigned roles that were configured in Looker directly**. This occurs the next time those users log in to Looker.

The **Advanced Role Management** section contains these options:

**Prevent Individual SAML Users from Receiving Direct Roles** : Turning this option on prevents Looker admins from assigning Looker roles directly to SAML users. SAML users will receive roles only through their group memberships. If SAML users are allowed membership in built-in (not mirrored) Looker groups, they can still inherit their roles both from mirrored SAML groups and from built-in Looker groups. Any SAML users who were previously assigned roles directly will have those roles removed when they next log in.

If this option is off, Looker admins can assign Looker roles directly to SAML users as if they were configured directly in Looker.

**Prevent Direct Membership in non-SAML Groups** : Turning this option on prevents Looker admins from adding SAML users directly to built-in Looker groups. If mirrored SAML groups are allowed to be members of built-in Looker groups, SAML users may retain membership in any parent Looker groups. Any SAML users who were previously assigned to built-in Looker groups will be removed from those groups when they next log in.

If this option is off, Looker admins can add SAML users directly to built-in Looker groups.

**Prevent Role Inheritance from non-SAML Groups** : Turning this option on prevents members of mirrored SAML groups from inheriting roles from built-in Looker groups. Any SAML users who previously inherited roles from a parent Looker group will lose those roles when they next sign in.

If this option is off, mirrored SAML groups or SAML users who are added as members of a built-in Looker group will inherit the roles assigned to the parent Looker group.

**Auth Requires Role** : If this option is on, SAML users are required to have a role assigned. Any SAML users who don't have a role assigned won't be able to sign in to Looker at all.

If this option is off, SAML users can authenticate to Looker even if they have no role assigned. A user with no assigned role won't be able to see any data or take any action in Looker, but they will be able to sign in to Looker.

### Disabling mirror SAML groups

If you want to stop mirroring your SAML groups within Looker, turn off the **Mirror SAML Groups** switch. Any empty mirror SAML groups will be deleted.

Non-empty mirror SAML groups will remain available for use in content management and role creation. However, users cannot be added to or removed from mirror SAML groups.

## Migration options

**Tip:** Looker recommends that you provide a merging strategy as explained in this section. When you're using Looker (Original), Looker also recommends that you enable **Alternate Login**.

### Alternate login for admins and specified users

**Note:** Alternate login isn't available for [Looker (Google Cloud core)](/looker/docs/looker-core-overview). By default, the backup authentication method for Looker (Google Cloud core) is [OAuth](/looker/docs/looker-core-oauth-authentication#using_oauth_as_a_backup_authentication_method).

Looker email and password logins are always disabled for regular users when SAML Auth is enabled. This option allows alternate email-based login using `/login/email` for admins and for specified users with the `login_special_email` permission.

Turning on this option is useful as a fallback during SAML Auth setup should SAML config problems occur later, or if you need to support some users who don't have accounts in your SAML directory.

**Note:** If a user has authenticated into the Looker instance using only SAML, you can enable alternate login only by using the Looker API. To learn how to enable alternate login using the Looker API, see the [Enabling the alternate login option](/looker/docs/alternate-login) documentation page.

### Specify the method used to merge SAML users to a Looker account

In the **Merge Users Using** field, specify the method to be used to merge a first-time SAML login to an existing user account. You can merge users from the following systems:

  * **Looker Email/Password** (not available for Looker (Google Cloud core))
  * **Google**
  * **LDAP** (not available for Looker (Google Cloud core))
  * **OIDC**

If you have more than one system in place, you can specify more than one system to merge by in this field. Looker will look up users from the systems listed _in the order that they are specified_. For example, assume you created some users using Looker email and password, then you enabled LDAP, and now you want to use SAML. Looker would merge by email and password first and then LDAP.

When a user logs in for the first time through SAML, this option will connect the user into their existing account by finding the account with a matching email address. If there is no existing account for the user, a new user account will be created.

#### Merging users when using Looker (Google Cloud core)

When you're using [Looker (Google Cloud core)](/looker/docs/looker-core-overview) and SAML, merging works as described in the previous section. However, it is only possible if one of the two following conditions are met:

  1. **Condition 1** : Users are authenticating into Looker (Google Cloud core) using their Google identities through the SAML protocol.
  2. **Condition 2** Before selecting the merge option, you have completed the following two steps:

     * [Federated](/architecture/redesign/identity/reference-architectures#using_an_external_idp) users' identities in Google Cloud using [Cloud Identity](/identity/docs/overview)
     * Set up [OAuth authentication](/looker/docs/looker-core-oauth-authentication) as the backup authentication method using the federated users.

If your instance doesn't meet one of these two conditions, the **Merge Users Using** option will be unavailable.

When merging, Looker (Google Cloud core) will search for user records that share the exact same email address.

## Test user authentication

Click the **Test** button to test your settings. Tests will redirect out to the server and will open a browser tab. The tab displays:

  * Whether Looker was able to talk to the server and validate.
  * The names Looker gets from the server. You need to validate that the server returns the proper results.
  * A trace to show how the info was found. Use the trace to troubleshoot if the information is incorrect. If you need additional information, you can read the raw XML server file.

**Note:** Read the results of the test carefully, as some parts of the test can succeed even if others fail.

**Tips** :

  * You can run this test any time, even if SAML is partially configured. Running a test can be helpful during configuration to see which parameters need configuration.
  * The test uses the settings entered on the **SAML Authentication** page, even if those settings haven't been saved. The test won't affect or change any of the settings on that page.
  * During the test, Looker passes information to the IdP using the SAML `RelayState` parameter. The IdP should return this `RelayState` value to Looker unmodified.

**Note:** Be sure to verify that _all_ tests are passing before clicking **Update Settings**. Saving incorrect SAML configuration information could lock yourself and others out of Looker.

## Save and apply settings

Once you are done entering your information, and the tests are all passing, check **I have confirmed the configuration above and want to enable applying it globally** and click **Update Settings** to save.

## User login behavior

When a user attempts to sign in to a Looker instance using SAML, Looker opens to the **Log In** page. The user must click the **Authenticate** button to initiate authentication through SAML.

This is the default behavior if the user doesn't already have an active Looker session.

If you want your users to sign in directly to your Looker instance after your IdP has authenticated them, and bypass the **Log In** page, turn on **Bypass Login Page** under **Login Behavior**.

If you are using Looker (Original), the **Bypass Login Page** feature needs to be enabled by Looker. To update your license for this feature, [contact a Google Cloud sales specialist](https://cloud.google.com/contact) or [open a support request](http://console.cloud.google.com/support/cases). If you are using [Looker (Google Cloud core)](/looker/docs/looker-core-overview), the **Bypass Login Page** option is available automatically if SAML is used as the primary authentication method, and defaults to disabled.

When **Bypass Login Page** is enabled, the user login sequence is as follows:

  1. The user tries to connect to a Looker URL (for example, `instance_name.looker.com`).

  2. Looker determines whether the user already has an active session enabled. To do this, Looker uses the cookie `AUTH-MECHANISM-COOKIE` to identify the authorization method used by the user in their last session. The value is always one of these: `saml`, `ldap`, `oidc`, `google`, or `email`.

  3. If the user does have an active session enabled, the user is taken to the requested URL.

  4. If the user doesn't have an active session enabled, they are redirected to the IdP. The IdP authenticates the user when they successfully sign in to the IdP. Looker then authenticates the user when the IdP sends the user back to Looker with information indicating that the user is authenticated with the IdP.

  5. If authentication at the IdP was successful, Looker then validates the SAML assertions, accepts authentication, updates user information, and forwards the user to the requested URL, bypassing the **Log In** page.

  6. If the user is unable to sign in to the IdP, or if they aren't authorized by the IdP to use Looker, then depending on the IdP, they will either remain on the IdP's site, or be redirected to the Looker **Log In** page.

## SAML response exceeding limit

If users who are trying to authenticate are receiving errors that indicate the SAML response has exceeded the maximum size, you can increase the maximum SAML response size allowed.

For Looker-hosted instances, [open a support request](http://console.cloud.google.com/support/cases) to update the maximum SAML response size.

For customer-hosted Looker instances, you can set the maximum SAML response size in number of bytes with the `MAX_SAML_RESPONSE_BYTESIZE` environment variable. For example:
    
    
    export MAX_SAML_RESPONSE_BYTESIZE=500000
    

The default for the maximum SAML response size is 250,000 bytes.