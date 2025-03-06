# https://cloud.google.com/looker/docs/mobile-app-sign-in

Depth: 3

**Note:** The Looker application doesn't support biometrics or signing in with a QR code. To use these features, install the [Looker Mobile (Legacy) application](/looker/docs/mobile-app-legacy) instead.

If mobile application access is [enabled](/looker/docs/mobile-app-enablement) for your instance and you have [installed](/looker/docs/mobile-app-installation) the app on your mobile device, you can sign in to the app using the same authentication method that you use to sign in to your Looker instance (Google OAuth, SAML, LDAP, OpenID Connect, or email and password).

The first time you sign in to the app, an onboarding screen is displayed. Select **Next** , or swipe left on each onboarding screen, and then select **Let's go!** on the final screen. You can also select **Skip** to navigate directly to the [**Recently Viewed** screen](/looker/docs/mobile-app-navigating-to-content#viewing_your_most_recently_viewed_or_favorite_content).

## Signing in with Google Auth, SAML, LDAP, OpenID Connect, or email address

You can sign in using the same authentication method as your Looker instance by following these steps:

  1. Open the Looker mobile application.
  2. When prompted to choose between Looker and Looker Studio Pro, choose Looker.
  3. Enter the URL for your Looker instance in the format `instance_name.looker.com` (don't use `http://www.` or `https://www.`), and then select **Continue**.
  4. The mobile application will direct you to sign in using your Google Auth, SAML, LDAP, OpenID Connect, or email credentials.

When you sign in to the Looker app for the first time, the app displays the **Authorization Request** screen. To confirm that you want to authorize the app to access data through your Looker account, select **Approve**.

Once you have signed in, you can navigate to your [favorite and most recently viewed Looks and dashboards](/looker/docs/mobile-app-navigating-to-content#viewing_your_most_recently_viewed_or_favorite_content), view [boards](/looker/docs/mobile-app-navigating-to-content#navigating_to_content_from_boards), and browse [content in folders](/looker/docs/mobile-app-navigating-to-content#browsing_content_in_folders).

## Signing out of the app

To sign out of the Looker mobile app, follow these steps:

  1. Select **More** from the app's [navigation menu](/looker/docs/mobile-app-navigating-to-content#using_the_navigation_menu).
  2. Select **Sign out**.

## Troubleshooting

If you are unable to sign in, ensure that the Looker mobile app is [enabled for your instance](/looker/docs/mobile-app-enablement).