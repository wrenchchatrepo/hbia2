# https://cloud.google.com/looker/docs/admin-panel-platform-actions

Depth: 3

The **Actions** page in the **Platform** section of the **Admin** menu lets you enable services that are integrated with Looker. For information on how to build and test actions to request to add to the Looker Action Hub _or_ to add to your own private action hub server, see the [Sharing data through an action hub](/looker/docs/action-hub) documentation page.

## Requirements

**Note:** To use Looker integrations, the Looker Action Hub must be able to communicate with the Looker instance and fulfill these [Looker Action Hub requirements](/looker/docs/action-hub#looker_action_hub_requirements). Admins of customer-hosted instances may need to consider [additional factors](/looker/docs/action-hub#considerations_for_customer-hosted_instances) when choosing to enable Looker integrations from the Looker Action Hub, especially integrations that [support streamed results](/looker/docs/action-hub#uses_streaming) or that use [OAuth](/looker/docs/action-hub#configuring_an_action_for_oauth).

To access the **Actions** page in the **Platform** section of the **Admin** menu, your user must have the [Admin role](/looker/docs/admin-panel-users-roles#default_roles).

## Enabling an action

> Prompt Looker to check the Looker Action Hub server for new actions by selecting **Refresh** at the top of the actions list.

Each service that is integrated into Looker's **Actions** page has its own requirements. The list of integrations later on this page has a table of all the available services. See the **How to use this integration** column for links to articles about setting up and using each service.

First perform any setup steps required on the integrated service. Then enable the integration in Looker, specifying any required information for that service.

To enable an integration, perform the following steps:

  1. On the **Platform** page of the **Admin** , select **Actions**.

  2. Find the service that you want to enable, and select the **Enable** button to the right of the service.

Looker then displays the enablement page for the selected service.

![](/static/looker/docs/images/admin-actions-enable-2308.png)

If applicable, enter the required information to configure this action. You should be able to gather this information from your account with the service that you're enabling.

  3. Turn on the **Enabled** switch. Looker automatically tests the action's configuration and displays an error if the action is configured incorrectly. Once you've made changes, select **Test Again** to retest the action's configuration.

  4. Select **Save** to save the action's configuration and close the action enablement page. The action is now available as a destination in the [Looker Scheduler](/looker/docs/scheduling).

## List of integrated services

The following list shows the services that are are available in the Looker Action Hub.

**Caution:** Individual Actions shown on the following list are not officially supported Google products.

Here is how to use the list:

  * The URLs that are shown in the **Link to README file** column provide instructions for enabling and configuring the integrated service to work with Looker.
  * The URLs that are shown in the **How to use this integration** column provide instructions for how to send data from Looker to the integrated service. Some of these articles also contain enablement instructions.
  * **Required LookML tags** lists any required tags that must be used with the [`tags`](/looker/docs/reference/param-field-tags) parameter in the content's underlying model.
  * **Action type** indicates what level of data the integrated service is sending: field, query, or dashboard. A field-level action sends the value of a single, specified cell in a data table. A query-level action sends the results of an entire query, such as all rows in an Explore or a Look. A dashboard-level action sends an image of a dashboard.
  * **Content available for scheduled deliveries** indicates what type of Looker content this integrated service can send as an ad hoc or scheduled [content delivery](/looker/docs/scheduling).
  * **Uses Google OAuth authentication** indicates whether the integrated service uses Google OAuth credentials for authentication. Customer-hosted instances may be unable to enable actions from the Looker Action Hub that use Google OAuth. See the [Sharing data through an action hub](/looker/docs/action-hub#considerations_for_customer-hosted_instances) documentation page for suggested solutions to this potential issue.
  * **Uses data streaming** indicates whether the integrated service supports streamed query results. Customer-hosted instances may be unable to enable actions from the Looker Action Hub that stream results. See the [Sharing data through an action hub](/looker/docs/action-hub#considerations_for_customer-hosted_instances) documentation page for suggested solutions to this potential issue.
  * **Minimum supported Looker version** provides the earliest Looker version that your instance must be using in order to use this integration.

Integrated service | Description | Link to README file | How to use this integration | Required LookML tags | Action type | Content available for scheduled deliveries | Uses Google OAuth authentication (Yes/No) | Uses data streaming (Yes/No) | Minimum supported Looker version  
---|---|---|---|---|---|---|---|---|---  
Airtable | Add records to a table in Airtable. | [View README on GitHub](https://github.com/looker/actions/blob/master/src/actions/airtable/README.md) | [View Community article](https://www.googlecloudcommunity.com/gc/Exploring-Curating-Data/Looker-Actions-Airtable/td-p/566854) | None | Query | Look, Explore | No | No | 5.6  
Amazon SageMaker Infer | Perform an inference using Amazon SageMaker. | No README available | No article available | None | Query | Look, Explore | No | Yes | 5.6  
Amazon SageMaker Train: Linear Learner | Start a training job on Amazon SageMaker, using the Linear Learner algorithm. | No README available | No article available | None | Query | Look, Explore | No | Yes | 5.6  
Amazon SageMaker Train: Xgboost | Start a training job on Amazon SageMaker, using the Xgboost algorithm. | No README available | No article available | None | Query | Look, Explore | No | Yes | 5.6  
Amazon Web Services EC2 Stop Instance | Stop an EC2 Instance using the Amazon EC2 API. | [View README on GitHub](https://github.com/looker/actions/blob/master/src/actions/amazon/README.md) | [View Community article](https://www.googlecloudcommunity.com/gc/Exploring-Curating-Data/Looker-Actions-AWS-EC2-Stop-Instance/td-p/583735) | aws_resource_id | Field, query | Look, Explore | No | No | 5.6  
Auger | Use query result to build a predictive model. | [View README on GitHub](https://github.com/looker/actions/blob/master/src/actions/auger/README.md) | See README | None | Query | Look, Explore | No | Yes | 5.24  
Azure Storage | Send and store a data file on Azure Storage. | [View README on GitHub](https://github.com/looker/actions/blob/master/src/actions/azure/README.md) | [View Community article](https://www.googlecloudcommunity.com/gc/Exploring-Curating-Data/Looker-Actions-Azure-Storage/td-p/565929) | None | Query, dashboard | Look, Explore, dashboard | No | Yes (for queries), No (for dashboards) | 5.6  
Braze | The Braze action lets you flag users within Braze using the REST API Endpoint from a Look. Ensure there's a `braze_id` field tagged in the results. MAX EXPORT: 10000. | [View README on GitHub](https://github.com/looker/actions/blob/master/src/actions/braze/README.md) | See README | braze_id | Query | Look, Explore | No | Yes | 5.6  
DataRobot | Send data to DataRobot and create a new project. | [View README on GitHub](https://github.com/looker-open-source/actions/blob/master/src/actions/datarobot/README.md) | See README | None | Query | Look, Explore | No | Yes | 5.24  
DigitalOcean — Stop Droplet | Stop DigitalOcean process using the DigitalOcean API. | [View README on GitHub](https://github.com/looker/actions/blob/master/src/actions/digitalocean/README.md) | [View Community article](https://www.googlecloudcommunity.com/gc/Exploring-Curating-Data/Looker-Actions-Digital-Ocean-Stop-Droplet/td-p/583753) | digitalocean_droplet_id | Field, query | Look, Explore | No | No | 5.6  
DigitalOcean Spaces | Send to and store a data file in DigitalOcean Storage. | [View README on GitHub](https://github.com/looker/actions/blob/master/src/actions/digitalocean/README.md) | [View Community article](https://www.googlecloudcommunity.com/gc/Exploring-Curating-Data/Looker-Actions-Digital-Ocean-Storage/td-p/583736) | None | Query, dashboard | Look, Explore, dashboard | No | Yes (for Looks and Explores), No (for dashboards) | 5.6  
Dropbox | Send and store a data file on Dropbox. | No README available | [View documentation](/looker/docs/delivering-dropbox) | None | Query, dashboard | Look, Explore, dashboard | Yes | No | 6.8  
Facebook Custom Audiences | Upload data to Facebook Ads Custom Audiences from Customer List. | [View README on GitHub](https://github.com/looker-open-source/actions/blob/master/src/actions/facebook/README.md) | See README | None | Query | Look, Explore | Yes | Yes | 6.10  
Firebase | Use Firebase to send push notifications to mobile. | No README available | No article available | None | Query | Look, Explore | No | No | 22.4  
Google Ads Customer Match | Upload data to Google Ads Customer Match. | [View README on GitHub](https://github.com/looker-open-source/actions/blob/master/src/actions/google/ads/README.md) | [View documentation](/looker/docs/best-practices/how-to-use-the-google-ads-integration) | None | Query | Look, Explore | Yes | Yes | 6.10  
Google Analytics Data Import | Upload data to a Google Analytics dataset. | [View README on GitHub](https://github.com/looker-open-source/actions/blob/master/src/actions/google/analytics/README.md) | See README | None | Query | Look, Explore | Yes | Yes | 6.10  
Google Cloud Storage | Write data files to a Google Cloud Storage bucket. | [View README on GitHub](https://github.com/looker-open-source/actions/blob/master/src/actions/google/gcs/README.md) | [View Community article](https://www.googlecloudcommunity.com/gc/Administering-Looker/Looker-Actions-Google-Cloud-Storage/td-p/591972) | None | Query, dashboard | Look, Explore, dashboard | No | Yes (for Looks and Explores), No (for dashboards) | 5.6  
Google Drive | Send data to Google Drive. | No README available | [View documentation](/looker/docs/best-practices/how-to-use-the-google-drive-integration) | None | Query, dashboard | Look, Explore, dashboard | Yes | Yes (for Looks and Explores), No (for dashboards) | 7.4  
Google Sheets | Send CSV data to a Google Sheet. | No README available | [View documentation](/looker/docs/best-practices/how-to-use-the-google-sheets-integration) | None | Query | Look, Explore | Yes | Yes | 7.4  
Hubspot Companies | Add properties to your Companies using the Hubspot V3 API. | [View README on GitHub](https://github.com/looker/actions/blob/master/src/actions/hubspot/README.md) | See README | hubspot_company_id | Query | Look, Explore | No | Yes | 5.6  
Hubspot Contacts | Add properties to your Contacts using the Hubspot V3 API. | [View README on GitHub](https://github.com/looker/actions/blob/master/src/actions/hubspot/README.md) | See README | hubspot_contact_id | Query | Look, Explore | No | Yes | 5.6  
Kloudio | Add data to a Google Sheet. | [View README on GitHub](https://github.com/looker/actions/blob/master/src/actions/kloudio/README.md) | See README | None | Query | Look, Explore | No | No | 5.6  
mParticle | Bulk export your user or event data from Looker to mParticle. | [View README on GitHub](https://github.com/looker/actions/blob/master/src/actions/mparticle/README.md) | See README | See README | Query | Look, Explore | No | Yes | 5.6  
Salesforce Campaigns | Add contacts or leads to Salesforce campaign. | [View README on GitHub](https://github.com/looker-open-source/actions/tree/master/src/actions/salesforce/campaigns/README.md) | See README | sfdc_contact_id or sfdc_lead_id | Query | Look, Explore | Yes | No | 22.6  
Segment Group | Add traits and/or users to your Segment groups. | [View README on GitHub](https://github.com/looker/actions/blob/master/src/actions/segment/README.md) | [View documentation](/looker/docs/segment) | segment_group_id and user_id, or segment_group_id and segment_anonymous_id | Query | Look, Explore | No | Yes | 4.20  
Segment Identify | Add traits to your Segment users using Identify. | [View README on GitHub](https://github.com/looker/actions/blob/master/src/actions/segment/README.md) | [View documentation](/looker/docs/segment) | email or user_id or segment_anonymous_id or segment_group_id | Query | Look, Explore | No | Yes | 4.20  
Segment Track | Connect to a number of integrations provided by Segment to identify and target users for marketing workflows. | [View README on GitHub](https://github.com/looker/actions/blob/master/src/actions/segment/README.md) | [View documentation](/looker/docs/segment) | email or user_id or segment_anonymous_id or segment_group_id | Query | Look, Explore | No | Yes | 4.20  
SendGrid | Send data and schedule results to send to an email address using SendGrid's API. | [View README on GitHub](https://github.com/looker/actions/blob/master/src/actions/sendgrid/README.md) | [View Community article](https://www.googlecloudcommunity.com/gc/Exploring-Curating-Data/Looker-Actions-Sendgrid/td-p/591971) | None | Query, dashboard | Look, Explore, dashboard | No | No | 5.6  
Slack | Send Looker content in direct messages, public channels, and private channels in Slack using OAuth. It is available for Looker-hosted deployments on 6.24+ with the [IP Allowlist](/looker/docs/admin-panel-server-ip-allowlist\)) feature disabled. | No README available | [View documentation](/looker/docs/scheduling-slack) | None | Query, dashboard | Look, Explore, dashboard | Yes | Yes (for Looks and Explores), No (for dashboards) | 6.24  
Slack Attachment (API Token) | Send data directly into a Slack channel along with user credentials. You may also want to reference [Lookerbot documentation](/looker/docs/best-practices/how-to-use-lookerbot-for-slack) for additional Slack functionality. | [View README on GitHub](https://github.com/looker/actions/blob/master/src/actions/slack/legacy_slack/README.md) | [View documentation](/looker/docs/best-practices/how-to-use-the-looker-slack-attachment-api-token-action) | None | Query, dashboard | Look, Explore, dashboard | No | No | 5.6  
Teams — Incoming Webhook | Send data to Microsoft Teams using an incoming webhook. | [View README on GitHub](https://github.com/looker/actions/blob/master/src/actions/teams/README.md) | See README | None | Query, dashboard | Look, Explore, dashboard | No | No | 5.6  
Tray | Connect to a number of integrations provided by Tray.io to automate workflows. | [View README on GitHub](https://github.com/looker/actions/blob/master/src/actions/tray/README.md) | [View Community article](https://www.googlecloudcommunity.com/gc/Exploring-Curating-Data/Looker-Actions-Tray/td-p/563164) | None | Query | Look, Explore | No | Yes | 5.6  
Twilio — Send Data | Send data from a Look or schedule results to send to a phone number using Twilio's API. | [View README on GitHub](https://github.com/looker/actions/blob/master/src/actions/twilio/README.md) | [View Community article](https://www.googlecloudcommunity.com/gc/Exploring-Curating-Data/Looker-Actions-Twilio-Send-Data/td-p/583749) | None | Query | Look, Explore | No | No | 5.6  
Twilio — Send Message | Send a message to a series of phone numbers (data columns that are tagged as phone numbers) in a Look. | [View README on GitHub](https://github.com/looker/actions/blob/master/src/actions/twilio/README.md) | See README | phone | Field, query | Look, Explore | No | No | 5.6  
Zapier | Connect to a number of integrations that are provided by Zapier to automate workflows. | [View README on GitHub](https://github.com/looker/actions/blob/master/src/actions/zapier/README.md) | [View Community article](https://www.googlecloudcommunity.com/gc/Exploring-Curating-Data/Looker-Actions-Zapier/td-p/583750) | None | Query | Look, Explore | No | Yes | 5.6