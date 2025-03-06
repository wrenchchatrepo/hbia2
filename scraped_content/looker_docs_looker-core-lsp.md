# https://cloud.google.com/looker/docs/looker-core-lsp

Depth: 3

**Note:** Complimentary Looker Studio Pro licenses are also available for Looker (original) instances. For instructions about accepting complimentary Looker Studio Pro licenses for a Looker (original) instance, see the [Looker Studio Pro](/looker/docs/admin-panel-platform-lsp) documentation page.

This page describes how to accept the complimentary Looker Studio Pro licenses that have been allocated to your Looker (Google Cloud core) instance, how to select the Google Cloud project that hosts your Looker Studio Pro content, and how to complete setup for your Looker Studio Pro subscription.

Looker Studio Pro licenses are available at no cost to users of a Looker (Google Cloud core) instance. To get started using Looker Studio Pro, accept and assign your complimentary licenses as part of a new or an existing Looker Studio Pro subscription. For more information about the terms of this offer, see [Complimentary Looker Studio Pro licenses offer details](/looker/docs/studio/complimentary-looker-studio-pro-licenses-offer-details) page.

## Before you begin

A Looker (Google Cloud core) instance is associated with a Looker Studio Pro subscription through the Google Cloud project that hosts Looker Studio Pro content. We recommend that you use a Google Cloud project that is dedicated to your Looker Studio Pro content, rather than the Google Cloud project that hosts your Looker (Google Cloud core) instance. We also recommend that you [set up a Google Cloud project](/resource-manager/docs/creating-managing-projects) for your Looker Studio content _before_ you accept your instance's allotted complimentary licenses, so that you can complete the setup process for your Looker Studio Pro subscription more expeditiously. For more information about Google Cloud project requirements, see the [Start a new Pro subscription](/looker/docs/studio/start-a-new-pro-subscription) documentation page.

Complimentary Looker Studio Pro licenses are available for Looker (Google Cloud core) instances that fulfill the following requirements:

  * The instance uses Looker 23.6 or later.
  * The instance uses a [public IP network connection](/looker/docs/looker-core-instance-create#create_network).

Each user with a [Looker Viewer](/iam/docs/understanding-roles#looker.viewer) (`roles/looker.viewer`) role who will use Looker Studio Pro must also be a Google Workspace or Cloud Identity user with a [Managed Google account](https://support.google.com/work/android/answer/6371476).

**Note:** Each Looker (Google Cloud core) instance can be associated with only one Looker Studio Pro subscription.

### Required roles

Different permissions are required to perform the following tasks:

  * Accept complimentary Looker Studio Pro licenses
  * Set up a self-service subscription to Looker Studio Pro

To get the permission that you need to accept complimentary Looker Studio Pro licenses and update Looker (Google Cloud core) instance information, ask your administrator to grant you an IAM role containing the `looker.instances.update` permission for the Google Cloud project that your Looker (Google Cloud core) instance resides in. The [Looker Admin](/iam/docs/understanding-roles#looker.admin) (`roles/looker.admin`) IAM role contains this permission by default, but you may be able to get this permission with [custom roles](/iam/docs/creating-custom-roles) or other [predefined roles](/iam/docs/understanding-roles).

To get the permission that you need to set up a self-service subscription to Looker Studio Pro, ask your administrator to grant you an IAM role containing the `lookerstudio.pro.manage` permission for the Google Cloud project that your Looker (Google Cloud core) instance resides in. The [Owner](/iam/docs/understanding-roles#owner) (`roles/owner`) IAM role and the [Looker Studio Pro Manager](/iam/docs/understanding-roles#lookerstudio.proManager) (`roles/lookerstudio.proManager`) role contain this permission by default, but you may be able to get this permission with [custom roles](/iam/docs/creating-custom-roles) or other [predefined roles](/iam/docs/understanding-roles).

## Accept Looker Studio Pro licenses

The default number of complimentary licenses allocated to your instance is determined by its [edition](/looker/docs/looker-core-overview#editions) type.

  * Enterprise and Embed editions are granted 50 complimentary Looker Studio Pro licenses.
  * The Standard edition is granted 12 licenses for its allotted 10 Standard users and 2 Developer users.

To accept these licenses, follow these steps in the Google Cloud console:

  1. Navigate to the [**Instances**](/looker/docs/looker-core-view-console#the_instances_page) page for the Google Cloud project in which your Looker (Google Cloud core) instance resides.
  2. Select the name of the Looker (Google Cloud core) instance that you want to use with Looker Studio Pro.
  3. Select the **Looker Studio Pro** tab.
  4. Select **Accept Looker Studio Pro licenses**.

## Select a Google Cloud project

After you have accepted the complimentary Looker Studio Pro licenses, you must associate your Looker (Google Cloud core) instance with a Google Cloud project.

**Important:** Once you've associated your Looker (Google Cloud core) instance with a Google Cloud project, disabling **Accept Looker Studio Pro licenses** automatically and immediately converts the complimentary Looker Studio Pro licenses to paid licenses, subject to [Looker Studio Pro pricing](/looker-studio#pricing).

To select your Looker Studio Pro Google Cloud project, follow these steps in the [**Looker Studio Pro** tab](/looker/docs/looker-core-view-console#tabs) of your Looker (Google Cloud core) instance settings:

  1. Click **Select project**.
  2. In the **Select a resource** dialog, select your project from the list, and click **Select project**.
  3. In the **Looker Studio Pro** tab of your Looker (Google Cloud core) instance settings, click **Save**.

The **Project name** field now displays the selected Google Cloud project ID.

**Important:** You can't change the project that is associated with an existing Looker Studio Pro subscription. Instead, you can create a new subscription based on a different project, add licenses and users, move any Pro content to the new project, and then cancel the old subscription. To learn more about what happens when you cancel a Looker Studio Pro subscription, see Effects of canceling a Looker Studio Pro subscription.

## Add users to your Looker Studio Pro subscription

You can finish setting up your new Looker Studio Pro subscription by adding users to your subscription and assigning them licenses. You can complete this step in the following ways, per your preference:

  * In the Google Cloud console
  * In Looker Studio

If you have an existing Looker Studio Pro subscription, your complimentary licenses have been applied automatically to your existing Looker Studio Pro users, and they can now use [Looker Studio Pro](/looker/docs/studio/about-looker-studio-pro).

### Add users in the Google Cloud console

To finish setting up your new Looker Studio Pro subscription in the Google Cloud console, follow these steps from the [**Looker Studio Pro** tab](/looker/docs/looker-core-view-console#tabs) of your Looker (Google Cloud core) instance settings:

  1. Click **Add users** , which opens the Looker Studio Pro homepage within the Google Cloud console.
  2. Click **Subscribe** to open the **Buy Looker Studio Pro licenses** panel.
  3. In the **Add users/groups** field, add the email addresses of users or groups to your subscription.

     * The **Total licenses** field displays the total number of licenses that are required to support the number of users that you have added.
     * The **Current no-cost Pro licenses** line item displays the number of complimentary Looker Studio Pro licenses that have been allocated to your Looker (Google Cloud core) instance.
     * Select **Auto assign available licenses to subscribed groups** to automatically assign available licenses to new users who join or who are added to Google Groups that are part of the subscription.
**Note:** If the number of users that you have added exceeds the number of complimentary Looker Studio Pro licenses that are allocated to your Looker (Google Cloud core) instance, the **Total monthly cost** line item displays the cost of the additional licenses that you are purchasing.
  4. Click **Buy**.

If you need to decrease the number of licenses that are consumed by your Looker Studio Pro subscription, select **Manage access** to remove users from your subscription, and then select **Add/remove licenses**. For more information, see [Remove users from a Pro subscription](/looker/docs/studio/edit-a-looker-studio-pro-subscription#remove_users_or_groups_from_the_subscription).

### Add users in Looker Studio

To finish setting up your new Looker Studio Pro subscription in Looker Studio, follow these steps from the [**Looker Studio Pro** tab](/looker/docs/looker-core-view-console#tabs) of your Looker (Google Cloud core) instance settings:

  1. Click **add users in Looker Studio Pro**.
  2. Set up a new Looker Studio Pro subscription by following the steps that are outlined in [Start a new Pro subscription](/looker/docs/studio/start-a-new-pro-subscription).

## Transfer complimentary Looker Studio Pro licenses to a different subscription

You can transfer complimentary Looker Studio Pro licenses from one Pro subscription to another Pro subscription. Set up the new subscription first, then follow these steps in the **Looker Studio Pro** tab of your Looker (Google Cloud core) instance settings to associate your instance with the new Looker Studio Pro subscription:

  1. Click **Select project**.
  2. In the **Select a resource** dialog, choose your new selection from the list, and click **Select project**.
  3. Select a Google Cloud project that is associated with the new Looker Studio Pro subscription.
  4. In the **Looker Studio Pro** tab of your Looker (Google Cloud core) instance settings, click **Save**.

The **Project name** field now displays the Google Cloud project ID that is associated with the new Looker Studio Pro subscription..

**Important:** Looker Studio Pro licenses in the original project will be converted to paid licenses, subject to [Looker Studio Pro pricing](/looker-studio#pricing). To avoid being charged for these licenses, cancel the original subscription.

## Effects of canceling a Looker Studio Pro subscription

If the Looker Studio Pro subscription is canceled, Looker will no longer recognize the subscription. Although the Google Cloud console will continue to reflect that the Looker (Google Cloud core) instance and the Looker Studio Pro subscription are linked, you will no longer be billed for Looker Studio Pro usage on the Google Cloud project. Your Looker (Google Cloud core) instance's Looker Studio Pro licenses are still available if you reinstate your subscription (within the [30-day grace period](/looker/docs/studio/cancel-a-looker-studio-pro-subscription#30-day_grace_period)) or if you initiate a new subscription. The no-cost version of Looker Studio is also available for use.

For more information about the effects of canceling a Looker Studio Pro subscription or deleting a Google Cloud project that is associated with a canceled subscription, see [Cancel a Looker Studio Pro subscription](/looker/docs/studio/cancel-a-looker-studio-pro-subscription).

## Troubleshooting complimentary licenses

Errors may occur when accepting complimentary Looker Studio Pro licenses or when adding users to a Looker Studio Pro subscription.

### Error: You have reached your license limit

There is a discrepancy between the number of users assigned to a Looker Studio Pro subscription and the number of complimentary licenses that are available for the subscription, and your subscription is incurring an unexpected cost.

**Example error message**

> `You have reached your license limit. To add more users, either delete some existing users/groups or purchase additional licenses.`

**Steps to resolve**

  1. In Looker Studio select **Pro subscriptions** from the left navigation to open the list of Looker Studio Pro subscriptions.
  2. Looker Studio displays the number of complimentary licenses that are available for the Google Cloud project that hosts your Looker (Google Cloud core) instance. For that project, under **Actions** , select **Manage subscription**.
  3. Navigate to the **Review and confirm Looker Studio Pro licenses** step and review the number of licenses in the **Number of licenses to buy** field.
  4. Enter the total number of licenses that you want to use, _including_ the number of complimentary licenses that are available for the subscription.

For example, if there are 10 complimentary licenses available, add 10 users to your subscription to use all licenses. If you add 11 users, you will be charged for 1 additional license. If you increase the **Number of licenses to buy** field to 11, you will be charged for 1 additional license.