# https://cloud.google.com/looker/docs/mobile-app-legacy

Depth: 3

**Note:** Consider using the [Looker application](/looker/docs/looker-core-mobile-app) for an updated experience.

The Looker Mobile (Legacy) application lets users view recently viewed and favorite Looks and dashboards, view the boards that they follow, browse content that is stored in folders, and share content on a mobile device.

## Downloading the app

To download the Looker Mobile (Legacy) app, use the following links:

  * [App Store](https://apps.apple.com/us/app/looker-mobile/id1533498070) (for iOS)
  * [Play Store](https://play.google.com/store/apps/details?id=com.google.looker) (for Android)

## Enabling and using the app

The following documentation pages walk you through setting up and using the Looker mobile application:

  * [Enabling the Looker Mobile (Legacy) app](/looker/docs/mobile-app-legacy-enablement): For admins: Enabling users to sign in to your instance using the app
  * [Installing the Looker Mobile (Legacy) app on your mobile device](/looker/docs/mobile-app-legacy-installation): Installing the app on an Android or iOS device
  * [Signing in to the Looker Mobile (Legacy) app](/looker/docs/mobile-app-legacy-sign-in): Signing in to the app with email or with a QR code, and signing out of the app
  * [Navigating to content in the Looker Mobile (Legacy) app](/looker/docs/mobile-app-legacy-navigating-to-content): Accessing your most recently viewed and favorite Looks and dashboards, viewing content on boards, navigating to content from folders, searching recently viewed and favorite content, sorting lists of content, and using the three-dot menu of a Look or a dashboard
  * [Viewing Looks in the Looker Mobile (Legacy) app](/looker/docs/mobile-app-legacy-viewing-looks): Opening and viewing Looks, switching between portrait and landscape mode, adding or removing a Look from your favorites, sharing or copying the link to a Look, and viewing information about a Look
  * [Viewing dashboards in the Looker Mobile (Legacy) app](/looker/docs/mobile-app-legacy-viewing-dashboards): Opening and viewing dashboards, switching between portrait and landscape mode, temporarily changing filter values, adding or removing a dashboard from your favorites, sharing or copying the link to a dashboard, and viewing information about a dashboard 

## Differences between the Looker and Looker Mobile (Legacy) applications

You can also access Looker content using the [Looker application](/looker/docs/looker-core-mobile-app). The key differences between the two apps are as follows:

  * The Looker app supports Google OAuth, SAML, LDAP, and OpenID Connect. The Looker Mobile (Legacy) app supports only email and QR authentication.
  * You can't access content from a Looker (Google Cloud core) instance on the Looker Mobile (Legacy) app.
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