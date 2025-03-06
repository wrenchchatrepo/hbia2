# https://cloud.google.com/looker/docs/looker-core-admin-gemini

Depth: 3

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](/products#product-launch-stages). 

**Note:** This documentation page is for Looker (Google Cloud core) instances. Gemini in Looker can also be enabled in Looker (original) instances. For information about enabling Gemini in Looker for Looker (original) instances, see the [Admin settings – Gemini in Looker](/looker/docs/admin-panel-platform-gil) documentation page.

Gemini in Looker is a product in the [Gemini for Google Cloud](/gemini/docs/overview) portfolio that provides generative AI-powered assistance to help you analyze and gain valuable insights from your data. Gemini in Looker can provide assistance for tasks in Looker (original) instances, Looker (Google Cloud core) instances, and Looker Studio. For more information about available features, see the [Gemini in Looker overview](/looker/docs/overview-gemini) documentation page.

[Learn how and when Gemini for Google Cloud uses your data](/gemini/docs/discover/data-governance). As an early-stage technology, Gemini for Google Cloud products can generate output that seems plausible but is factually incorrect. We recommend that you validate all output from Gemini for Google Cloud products before you use it. For more information, see [Gemini for Google Cloud and responsible AI](/gemini/docs/discover/responsible-ai).

**Note:** Gemini in Looker is being made available at no additional cost for a limited time only. At the end of this limited time period, usage of Gemini in Looker may require the purchase of additional or different features. You won't be charged automatically.

## Gemini in Looker feature availability

The availability of Gemini in Looker features is summarized in the following table. Depending on the needs of your organization, you can enable the settings that grant users access to the Gemini in Looker features that are available in the appropriate Looker platform.

Enabled settings | Accessible Gemini in Looker features | Implementation  
---|---|---  
Gemini in Looker | 

  * In Looker: [Write LookML](/looker/docs/write-lookml-gemini)
  * In Looker: [Create custom Looker visualizations](/looker/docs/custom-looker-visualization-gemini)

| 

  1. Enable Gemini in Looker (Google Cloud core).
  2. Grant permissions to use Gemini in Looker.

  
Gemini in Looker, Studio in Looker | 

  * In Looker: [Write LookML](/looker/docs/write-lookml-gemini)
  * In Looker: [Create custom Looker visualizations](/looker/docs/custom-looker-visualization-gemini)
  * In Looker (through Studio in Looker): [Query data in natural language](/looker/docs/studio/query-your-data-in-natural-language-gemini)
  * In Looker (through Studio in Looker): [Generate calculated fields](/looker/docs/studio/create-calculated-fields-gemini)

| 

  1. [Enable Studio in Looker.](/looker/docs/enabling-studio-in-looker)
  2. In Looker, enable Gemini in Looker. (Gemini in Looker will be enabled automatically in Looker Studio.)
  3. Grant permissions to use Gemini in Looker.

  
Gemini in Looker (in Looker), Accept complimentary Looker Studio Pro licenses, and Gemini in Looker (in Looker Studio) | 

  * In Looker: [Write LookML](/looker/docs/write-lookml-gemini)
  * In Looker: [Create custom Looker visualizations](/looker/docs/custom-looker-visualization-gemini)
  * In Looker Studio: [Query data in natural language](/looker/docs/studio/query-your-data-in-natural-language-gemini)
  * In Looker Studio: [Generate calculated fields](/looker/docs/studio/create-calculated-fields-gemini)
  * In Looker Studio: [Export data to Slides](/looker/docs/studio/add-looker-studio-slides-gemini)

| 

  1. Enable Gemini in Looker (in Looker).
  2. [Accept Looker Studio Pro licenses](/looker/docs/looker-core-lsp).
  3. [Enable Gemini in Looker (in Looker Studio).](/looker/docs/studio/enable-and-disable-gemini-in-looker-for-looker-studio)

  
  
## Enabling and disabling Gemini

Gemini in Looker features are enabled through the Google Cloud console and are available on a per-instance basis.

To get the permissions that you need to enable Gemini for a Looker (Google Cloud core) instance, ask your administrator to grant you the [Looker Admin ](https://cloud.google.com/iam/docs/understanding-roles#looker.admin) (`roles/looker.admin`) IAM role on the project in which the instance resides. For more information about granting roles, see [Manage access to projects, folders, and organizations](/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](/iam/docs/creating-custom-roles) or other [predefined roles](/iam/docs/understanding-roles). 

In the Google Cloud console, follow these steps to enable Gemini:

  1. On the [**Instances** page](/looker/docs/looker-core-view-console), click the name of the instance for which you want to enable Gemini.
  2. Click **Edit**.
  3. Expand the **Gemini in Looker (Google Cloud core)** section.
  4. Select **Gemini**.
  5. Select **Trusted Tester features**. When this setting is enabled, users can access the Trusted Tester capabilities of Gemini in Looker. You may request access to the non-public Trusted Tester capabilities through the [Gemini in Looker preview form](https://docs.google.com/forms/d/e/1FAIpQLSefBWbxchQFyZB9EOOcRxYTRi-16TezwRExW-x-XJRfeklCiA/viewform) on a per-user basis. You must enable this setting to use Gemini during the pre-GA preview.

**Note:** Gemini in Looker is subject to the agreement under which your organization accesses Google Cloud, including the Pre-GA Offerings Terms of the Google Cloud Service Specific Terms, as supplemented by the [Gemini for Google Cloud Trusted Tester Program terms](/trusted-tester/gemini-for-google-cloud-preview).
  6. Optionally, select **Trusted Tester data use**. When this setting is enabled, you consent to your data being used by Google as described in the [Gemini for Google Cloud Trusted Tester Program terms](/trusted-tester/gemini-for-google-cloud-preview).

To disable Gemini for a Looker (Google Cloud core) instance, clear the **Gemini** setting.

## Grant the Gemini in Looker permission to users

Grant Looker users the ability to use Gemini in Looker features in the Looker (Google Cloud core) instance by assigning them the Gemini role in the instance's **Admin** settings. Additional Looker permissions may be needed to perform the tasks that Gemini assists with. For more information about these additional permissions, see the [Admin settings - Roles](/looker/docs/admin-panel-users-roles#gemini_in_looker) documentation page. For more information about adding users to a Looker (Google Cloud core) instance so that you can update their settings, see the [Manage users within Looker (Google Cloud core)](/looker/docs/looker-core-user-management) documentation page.

**Note:** In Looker 25.2, the Gemini in Looker permission is not enforced, but we recommend that you assign this permission to those who will use Gemini in Looker features. This permission will be enforced starting in Looker 25.4.

To perform the following steps to grant permissions to use Gemini in Looker features, you must be a Looker admin for the Looker instance.

To update an individual user's settings to assign the **Gemini** role, follow these steps.

  1. Navigate to the **Users** page in the **Users** section of the **Admin** panel.
  2. Select the user or group whose permissions you want to change.
  3. From the **Roles** drop-down menu, select **Gemini**.
  4. Select **Save** to retain these settings.

You can also assign the **Gemini** role to multiple users or groups from the **Roles** page in the **Users** section of the **Admin** panel by following these steps:

  1. Navigate to the **Roles** page in the **Users** section of the **Admin** panel.
  2. Next to the **Gemini** role, select **Edit**.
  3. Under **Groups** or **Users** , select the groups or users that you want to assign the **Gemini** role to.
  4. Click **Update Role** to retain these settings.

## Provide feedback

You can provide feedback about each Gemini in Looker feature. Instructions for how to submit feedback are included in each feature's documentation.

## Related resources

  * [Learn more about Gemini for Google Cloud](/gemini/docs/overview)
  * [Learn more about Gemini in Looker](/looker/docs/overview-gemini)