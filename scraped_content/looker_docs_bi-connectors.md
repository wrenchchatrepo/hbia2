# https://cloud.google.com/looker/docs/bi-connectors

Depth: 3

The **BI Connectors** page in the **Platform** section of the **Admin** menu lets you enable or disable connections from Looker to other business intelligence (BI) applications.

In [Looker (Google Cloud core)](/looker/docs/looker-core-overview) instances that use public IP or both public IP and private IP, the ability for Looker users to connect to other BI applications is enabled by default. Those with the Admin Looker role can use this page to disable any or all of these connectors.

In Looker (original), this ability is disabled by default. Looker admins can use this page to enable any or all of these connectors.

## Requirements

To view the **BI Connectors** page, the following requirements must be met:

  * Your Looker instance must be Looker-hosted.
  * Your Looker instance must be running Looker 22.20 or later. If your Looker instance is not hosted on Google Cloud, your instance must be running Looker 23.4 or later.
  * Your Looker instance must not use private IP only (either with private services access or Private Service Connect).
  * You must have the [Admin role](/looker/docs/admin-panel-users-roles#default_roles) on your Looker instance.

## All Looker BI Connectors

Enable or disable the **All Looker BI Connectors** option to control connections to all BI applications to which Looker has a connection. When enabled, this option automatically enables all of the connectors on the Looker instance.

## Connected Sheets

Enable or disable this option to allow or disallow [connections to Looker from Google Sheets](/looker/docs/connected-sheets). This option is automatically enabled if the **All Looker BI Connectors** option is enabled.

## Looker Studio

Enable or disable this option to allow or disallow [connecting to Looker Studio from Looker Explores](/looker/docs/looker-studio-connector), monitoring System Activity information from Looker Studio [data sources](https://support.google.com/looker-studio/answer/6268208), and [allowing connections from Looker Studio](https://support.google.com/looker-studio/answer/12388266). This option is automatically enabled if the **All Looker BI Connectors** option is enabled.

## Microsoft Power BI

Enable or disable this option to allow or disallow [connections to Looker from Microsoft Power BI](/looker/docs/powerbi-connector). This option is automatically enabled if the **All Looker BI Connectors** option is enabled.

## Tableau Desktop

Enable or disable this option to allow or disallow [connections to Looker from Tableau Desktop](/looker/docs/tableau-connector). This option is automatically enabled if the **All Looker BI Connectors** option is enabled.