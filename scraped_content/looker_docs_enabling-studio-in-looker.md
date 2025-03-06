# https://cloud.google.com/looker/docs/enabling-studio-in-looker

Depth: 3

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](/products#product-launch-stages). 

This document provides guidance for enabling the Studio in Looker feature within your Looker (original) or Looker (Google Cloud core) instance.

**Important:** By enabling Studio in Looker, you agree to the [Google Cloud Platform Terms of Service](https://cloud.google.com/terms). Use of Studio in Looker is subject to the agreement under which you use Google Cloud, not your Looker agreement.

## Requirements and limitations

Before you enable Studio in Looker, ensure that your Looker (original) or Looker (Google Cloud core) instance meets the following requirements:

  * Your Looker instance must be running Looker 24.18 or later and be Looker-hosted.

  * You must have the [Admin Looker role](/looker/docs/admin-panel-users-roles#default_roles) within your Looker instance.

**Note:** Studio in Looker is in preview with limited support. We encourage you to share your feedback to help us improve. To report bugs or issues, send an email to [`studio-in-looker-feedback@google.com`](mailto:studio-in-looker-feedback@google.com) with the following details: 

  * A clear description of the problem and the expected behavior
  * Steps to reproduce the issue
  * Any additional relevant details

### Additional requirements for Google OAuth

**Note:** While Studio in Looker is in preview, we are no longer onboarding new instances that use Google OAuth for authentication.

If your Looker instance uses Google OAuth for authentication, then you'll also need to create a new Google Cloud project that meets the following requirements:

  * The project must be a new Google Cloud project.
  * The project can't be linked to an existing Looker Studio Pro subscription.
  * The project must belong to your organization.
  * You must have the [Looker Studio Pro Manager](/iam/docs/understanding-roles#lookerstudio.proManager) Identity and Access Management (IAM) role on the project.

**Warning:** To avoid losing any Studio in Looker reports, don't change the Google Cloud project once you've enabled Studio in Looker with Google OAuth. If you change the project, then all reports that are associated with the original Google Cloud project will be permanently deleted.

### Limitations

Studio in Looker is in preview, and the following limitations apply:

  * Studio in Looker isn't compatible with Looker (Google Cloud core) instances that are configured to use CMEK, VPC-SC, or private IP.
  * Users won't be able to use Studio in Looker if they log in to their Looker instance by using secondary authentication.

## Enabling Studio in Looker

To enable Studio in Looker, follow the instructions for Looker (original) or Looker (Google Cloud core), depending on your authentication method:

  * Looker (original) with Google OAuth
  * Looker (original) with all other authentication methods
  * Looker (Google Cloud core) with Google OAuth
  * Looker (Google Cloud core) with all other authentication methods

### Looker (original) with Google OAuth

**Note:** While Studio in Looker is in preview, we are no longer onboarding new instances that use Google OAuth for authentication.

To enable Studio in Looker for a Looker (original) instance that uses Google OAuth for authentication, follow these steps:

  1. In Looker, navigate to **Admin** > **Labs** , and enable the **Access Studio in Looker** [Labs feature](/looker/docs/admin-panel-general-labs).
  2. In Looker, navigate to **Admin** > **Platform** > **Studio in Looker** , and enable the **Studio in Looker** option.
  3. On the **Studio in Looker** page, fill in the following fields: 
    1. **Customer ID** : Enter the [customer ID for your Google Workspace or Cloud Identity account](https://support.google.com/a/answer/10070793). This is the unique identifier that was assigned to your account when you signed up for Google Workspace or Cloud Identity.
    2. **Service account email ID** : Enter the service account email ID that was created during the pre-setup process for Studio in Looker. You can find this email ID in the welcome email that you received after you signed up for the preview.
    3. **Google Cloud project number** : Enter the [Google Cloud project number](/resource-manager/docs/creating-managing-projects#identifying_projects) for the Google Cloud project that you created for use with Studio in Looker. This is a unique identifier for that specific project.

### Looker (original) with all other authentication methods

To enable Studio in Looker for a Looker (original) instance that uses any authentication method aside from Google OAuth, follow these steps:

  1. In Looker, navigate to **Admin** > **Labs** , and enable the **Studio in Looker** [Labs feature](/looker/docs/admin-panel-general-labs).
  2. In Looker, navigate to **Admin** > **Platform** > **Studio in Looker** , and enable the **Studio in Looker** option.

### Looker (Google Cloud core) with Google OAuth

**Note:** While Studio in Looker is in preview, we are no longer onboarding new instances that use Google OAuth for authentication.

To enable Studio in Looker for a Looker (Google Cloud core) instance that uses Google OAuth for authentication, follow these steps:

  1. In Looker, navigate to **Admin** > **Platform** > **Studio in Looker** , and enable the **Studio in Looker** option.
  2. On the **Studio in Looker** page, fill in the following fields: 
    1. **Customer ID** : Enter the [customer ID for your Google Workspace or Cloud Identity account](https://support.google.com/a/answer/10070793). This is a unique identifier that was assigned to your account when you signed up for Google Workspace or Cloud Identity.
    2. **Service account email ID** : Enter the service account email ID that was created during the pre-setup process for Studio in Looker. You can find this email ID in the welcome email that you received after you signed up for the preview.
    3. **Google Cloud project number** : Enter the [Google Cloud project number](/resource-manager/docs/creating-managing-projects#identifying_projects) for the Google Cloud project that you created for use with Studio in Looker. This is a unique identifier for that specific project.

### Looker (Google Cloud core) with all other authentication methods

To enable Studio in Looker for a Looker (Google Cloud core) instance that uses any authentication method aside from Google OAuth, follow these steps:

  1. Submit the [sign-up form for the preview](https://docs.google.com/forms/d/195CrnEOa0nlW9OBg2-QaWooZczPLBLoNfTg3QuMW_6Y/viewform), and Looker will enable the feature for your instance.
  2. In Looker, navigate to **Admin** > **Platform** > **Studio in Looker** , and enable the **Studio in Looker** option.

## Using Studio in Looker with Gemini in Looker

When Studio in Looker and [Gemini in Looker](/looker/docs/overview-gemini) are enabled for a Looker instance, Looker users who have the appropriate permissions can query Looker Explore data in natural language by accessing [Conversational Analytics](/looker/docs/studio/query-your-data-in-natural-language-gemini).

  * For Looker (original), the instance must be running Looker 25.2 or later, and the instance must be enabled for Gemini in Looker in the Admin settings. For detailed enablement instructions, see the [Admin settings — Gemini in Looker](/looker/docs/admin-panel-platform-gil) documentation page.
  * For [Looker (Google Cloud core)](/looker/docs/overview-gemini), the instance must be enabled for Gemini in Looker in the Google Cloud console. For detailed enablement instructions, see the [Administer Gemini on your Looker (Google Cloud core) instance](/looker/docs/looker-core-admin-gemini) documentation page.

## Disabling Studio in Looker

**Warning:** Disabling Studio in Looker permanently deletes all the Studio in Looker reports that were created on this Looker instance. This action cannot be undone.

To disable Studio in Looker, follow these steps:

  1. Navigate to **Admin** > **Platform** > **Studio in Looker**.
  2. Disable the **Enable Studio in Looker** option.
  3. Confirm your understanding of the data loss by selecting the box.
  4. Click **Disable Studio in Looker**.