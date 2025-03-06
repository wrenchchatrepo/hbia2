# https://cloud.google.com/looker/docs/studio/enable-and-disable-gemini-in-looker-for-looker-studio

Depth: 3

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](/products#product-launch-stages). 

This page discusses how to enable and disable Gemini in Looker in Looker Studio as part of a Looker Studio Pro subscription. Looker Studio Pro licenses are available at no cost to Looker users on instances that meet [offer requirements](/looker/docs/studio/complimentary-looker-studio-pro-licenses-offer-details).

When Gemini in Looker is enabled for a Looker Studio Pro subscription, users under that subscription can use these Gemini in Looker capabilities:

  * [**Ask questions about your data with Conversational Analytics**](/looker/docs/studio/query-your-data-in-natural-language-gemini) (Preview): Use Gemini in Looker assistance to find answers, explore data, and share insights using natural language.
  * [**Add Looker Studio content to your Google Slides presentation**](/looker/docs/studio/add-looker-studio-slides-gemini) (Preview): Use Gemini in Looker to help you import components from your Looker Studio Pro reports into your Slides presentations.
  * [**Create calculated fields**](/looker/docs/studio/create-calculated-fields-gemini) (Preview): Use Gemini in Looker assistance to create custom fields and calculations in Looker Studio Pro reports without prerequisite knowledge or experience with Looker Studio formula language.

See the [Gemini in Looker overview](/looker/docs/overview-gemini) for more information.

**Warning:** As an early-stage technology, Gemini can generate output that seems plausible but is factually incorrect. We recommend that you validate all output from Gemini before you use it. For more information, see [Gemini for Google Cloud and responsible AI](/gemini/docs/discover/responsible-ai).**Note:** Gemini in Looker is being made available at no additional cost for a limited time only. At the end of this limited time period, usage of Gemini in Looker may require the purchase of additional or different features. You won't be charged automatically.

## Before you begin

Before Gemini in Looker can be enabled in Looker Studio, the following requirements must be met:

  * Your organization must have a Looker Studio Pro subscription

  * To view and modify Gemini in Looker settings in Looker Studio:

    * For a standard self-service subscription, you must be assigned a role that contains the `lookerstudio.pro.manage` IAM permission for the Google Cloud project that you use for your Looker Studio Pro subscription. The `lookerstudio.pro.manage` permission is included in the [Owner](/iam/docs/understanding-roles#owner) (`roles/owner`) IAM role and the [Looker Studio Pro Manager](/iam/docs/understanding-roles#lookerstudio.proManager) (`roles/lookerstudio.proManager`) IAM role. You may also be able to get this permission with [custom roles](/iam/docs/creating-custom-roles) or other [predefined roles](/iam/docs/understanding-roles).
    * For a "whole organization, active user" subscription, you must be assigned a role that contains the `Manage Looker Studio Settings` Workspace privilege, which is included in the [Workspace Services Admin](https://support.google.com/a/answer/2405986#services_admin) and the [Workspace Super Admin](https://support.google.com/a/answer/2405986#super_admin) roles. You may also be able to get this privilege with a [custom admin role](https://support.google.com/a/answer/2406043).

For more information about Looker Studio Pro subscription types, see the [Looker Studio Pro subscription overview](/looker/docs/studio/looker-studio-pro-subscription-overview).

## Gemini in Looker enablement options

You can enable Gemini in Looker for a Google Cloud project that is associated with any of your organization's Looker Studio Pro subscriptions. There are several toggles to control Gemini in Looker enablement:

  * **Enabled** : When this toggle is enabled, users of the selected Looker Studio Pro subscription can access and use the Gemini in Looker features that appear in Looker Studio.
  * **Trusted Tester features** : When this toggle is enabled, users of the selected Looker Studio Pro subscription can access Trusted Tester capabilities of Gemini in Looker. You may request access to non-public Trusted Tester capabilities through the [Gemini in Looker preview form](https://docs.google.com/forms/d/e/1FAIpQLSefBWbxchQFyZB9EOOcRxYTRi-16TezwRExW-x-XJRfeklCiA/viewform) on a per-user basis.

**Warning:** Gemini in Looker is subject to the agreement under which your organization accesses Google Cloud Platform, including the Pre-GA Offerings Terms of the Google Cloud Platform Service Specific Terms, as supplemented by the [Gemini for Google Cloud Trusted Tester Program terms](/trusted-tester/duet-preview). Data Use settings for Gemini in Looker in the Trusted Tester Program can be adjusted at any time. [Learn More](/trusted-tester/gemini-for-google-cloud-preview).

  * **Trusted Tester data use** : When this toggle is enabled, you consent to your data being used by Google as described in the [Gemini for Google Cloud Trusted Tester Program terms](/trusted-tester/duet-preview). This includes using data submitted to Google to: (i) ensure that the results are contextually relevant and high quality; (ii) diagnose issues and validate model performance; and (iii) to use aggregated, de-identified, or pseudonymized data to improve and develop the TTP Services and any Google Cloud Platform Services.

## Enable and disable Gemini in Looker

To make Gemini in Looker features available to users of a Looker Studio Pro subscription, enable Gemini in Looker for the Google Cloud project that is associated with that subscription. Gemini in Looker is disabled by default for new Google Cloud projects and for Google Cloud projects that are associated with a canceled Looker Studio Pro subscription.

To enable Gemini in Looker for Looker Studio features, follow these steps:

  1. [Sign in to Looker Studio.](https://lookerstudio.google.com)
  2. Click the **User settings** icon ![User settings.](/static/looker/docs/studio/images/gmsettingsgmgrey50024dp-2022-03-02.png) and select the **Gemini in Looker** tab.
  3. Turn on the **Enabled** toggle for the Google Cloud project that is associated with the Looker Studio Pro subscription for which you would like to make Gemini in Looker features available. When this toggle is enabled, you can also choose to enable the **Trusted Tester features** , the **Trusted Tester data use** toggle, or both toggles.

To disable Gemini in Looker for Looker Studio features, follow these steps:

  1. [Sign in to Looker Studio.](https://lookerstudio.google.com)
  2. Click the **User settings** icon ![User settings.](/static/looker/docs/studio/images/gmsettingsgmgrey50024dp-2022-03-02.png) and select the **Gemini in Looker** tab.
  3. Turn off the **Enabled** toggle for the Google Cloud project that is associated with the Looker Studio Pro subscription for which you would like to disable Gemini in Looker features. If you turn off the **Enabled** toggle, the **Trusted Tester features** and **Trusted Tester data use** toggles, if enabled, are disabled automatically.

> Enabling the **Trusted Tester features** toggle automatically enables the **Trusted Tester data use** toggle. You can manually disable the **Trusted Tester data use** toggle, if desired.
> 
> By enabling **Trusted Tester data use** , you consent to your prompt data being shared with Google to help improve Gemini services. Gemini doesn't use your prompts or its responses as data to train its model. For more information, see [How Gemini in Google Cloud uses your data](/gemini/docs/discover/data-governance?sjid=2544169332415475819-NA).

## Provide feedback

You can provide feedback about each Gemini in Looker feature. Instructions for how to submit feedback are included in each feature's documentation.

## Related resources

  * [Gemini in Looker](/looker/docs/overview-gemini)
  * [Gemini for Google Cloud overview](/gemini/docs/overview)