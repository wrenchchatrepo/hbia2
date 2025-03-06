# https://cloud.google.com/looker/docs/looker-core-mobile-app

Depth: 3

The Looker mobile application lets users access content from a Looker (Google Cloud core) instance or Looker (original) instance. Users can view Looks and dashboards, view boards they follow, browse content that is stored in folders, and share content on their mobile devices.  
  
## Download the app

To download the Looker mobile app, search for **Looker** in the Apple App Store or the Google Play Store, or use the following links:

  * [App Store](https://apps.apple.com/us/app/looker-studio/id1644381985) (for iOS)
  * [Play Store](https://play.google.com/store/apps/details?id=com.google.android.apps.cloud.cloudbi) (for Android)

The Looker mobile application lets you access your Looker and Looker Studio Pro content from a single app. You can view Looks and dashboards on a mobile device.

## Enable and use the app

Note that while you can access content from a Looker (original) instance using either the Looker app or [Looker Mobile (Legacy) app](/looker/docs/mobile-app-legacy), you can only access content from a Looker (Google Cloud core) instance using the Looker app. Also, the app is only available for Public IP instances.

The following documentation pages walk you through setting up and using the Looker mobile application:

  * [Enabling the mobile application](/looker/docs/mobile-app-enablement): For admins: Enabling users to sign in to your instance using the app
  * [Installing the mobile application on your mobile device](/looker/docs/mobile-app-installation): Installing the app on an Android or iOS device
  * [Signing in to the mobile application](/looker/docs/mobile-app-sign-in): Signing in to the app with email or with a QR code, and signing out of the app
  * [Navigating to content in the mobile application](/looker/docs/mobile-app-navigating-to-content): Accessing your most recently viewed and favorite Looks and dashboards, viewing content on boards, navigating to content from folders, searching recently viewed and favorite content, sorting lists of content, and using the three-dot menu of a Look or a dashboard
  * [Viewing Looks in the mobile application](/looker/docs/mobile-app-viewing-looks): Opening and viewing Looks, switching between portrait and landscape mode, adding or removing a Look from your favorites, sharing or copying the link to a Look, and viewing information about a Look
  * [Viewing dashboards in the mobile application](/looker/docs/mobile-app-viewing-dashboards): Opening and viewing dashboards, switching between portrait and landscape mode, temporarily changing filter values, adding or removing a dashboard from your favorites, sharing or copying the link to a dashboard, and viewing information about a dashboard

## Differences between the Looker and Looker Mobile (Legacy) apps

You can also access Looker content using the [Looker Mobile (Legacy) application](/looker/docs/mobile-app-legacy). The key differences between the two apps are as follows:

  * The Looker app supports Google OAuth, SAML, LDAP, and OpenID Connect. The Looker Mobile (Legacy) app supports only email and QR authentication.
  * The Looker Mobile (Legacy) doesn't support accessing content from a Looker (Google Cloud core) instance or from Looker Studio.
  * The Looker app does not support drilling or alerts.

Feature | Looker app support | Looker Mobile (Legacy) app support  
---|---|---  
Supported Looker instance types | 

  * Looker (Google Cloud core)
  * Looker Original

| 

  * Looker Original

  
Access Looker Studio Pro content | Supported | Not supported  
Authentication methods | 

  * Google OAuth
  * SAML
  * LDAP
  * OpenID Connect
  * Email

| 

  * Email
  * QR code

  
Biometric verification | Not supported | Supported  
Drilling | Not supported | Supported on iOS devices only  
Alerts | Not supported | Supported on iOS devices only  
Content search | Not supported | Supported  
Mobile friendly rendering of dashboards and Looks | Supported | Supported  
Restrict access by IP address | Not supported | Not supported