# https://cloud.google.com/looker/docs/thoughtspot-connector

Depth: 3

The Looker–ThoughtSpot BI Connector lets you use Thoughtspot Cloud to connect to data from a Looker Explore. The Looker–ThoughtSpot BI Connector is built upon the Looker Open SQL Interface, which allows access to LookML models and Explores for applications that use JDBC to connect to data sources. See the [Open SQL Interface](/looker/docs/sql-interface) documentation for more details.

## Before you begin

Your Looker instance must meet the following requirements to make use of the Looker–ThoughtSpot BI Connector:

  * Running Looker 24.14 or later.
  * Has a LookML project that uses data from a Google BigQuery connection. (The LookML project must have a model file that specifies a Google BigQuery connection in its `connection` parameter.)

The user creating the Thoughtspot connection must meet the following requirements:

  * Has a Looker [user role](/looker/docs/admin-panel-users-roles#roles) that includes the [`explore`](/looker/docs/admin-panel-users-roles#explore) permission on the LookML model that you want to access from Thoughtspot.
  * Use the same email address for both Looker and Thoughtspot.

See the [Add a Looker connection](https://docs.thoughtspot.com/cloud/latest/connections-looker-add) page in the Thoughtspot documentation for additional requirements to configure and use this connector.

## Setting up ThoughtSpot authentication to your Looker instance

The Looker–ThoughtSpot BI Connector requires that you set up authentication for your Looker instance.

Although we prefer using OAuth authentication, you can also use a service account to configure authentication. To learn how to set up service account authentication, see Connecting to Looker from Thoughtspot Cloud.

### Setting up OAuth for the Looker–ThoughtSpot BI Connector

You can use the Looker [API Explorer](/looker/docs/api-explorer) to set up OAuth integration for the Looker–ThoughtSpot BI Connector.

If your Looker instance already has API Explorer installed, you can access it with this URL format:
    
    
    https://LOOKER_INSTANCE_URL/extensions/marketplace_extension_api_explorer::api-explorer/
    

If your Looker instance doesn't have the API Explorer, you can install it from the Looker Marketplace. See the [Using the API Explorer](/looker/docs/api-explorer#installing_the_api_explorer) page for information.

To use the API Explorer to set up OAuth integration on your Looker instance, perform the following steps:

  1. Open the Looker API Explorer (see the [Using the API Explorer](/looker/docs/api-explorer#starting_the_api_explorer) page for information).
  2. In the API Explorer's **Search** field, enter **Register OAuth App**.
  3. In the search results, click **Register OAuth App**.
  4. On the **Register OAuth App** page, click the **Run It** button.
  5. In the **Request** tab of the **Run It** dialog, enter the following information into the corresponding fields:

     * **client_guid** :
    
        looker-thoughtspot
    

     * **body** :
    
        {
      "redirect_uri": THOUGHTSPOT_INSTANCE_URL/callosum/v1/connection/generateTokens,
      "display_name": "Looker-ThoughtSpot (manual)",
      "description": "Client for Looker-ThoughtSpot integration (manually added)",
      "enabled": true,
      "group_id": ""
    }
    

**Note:** Your ThoughtSpot instance has a URL that is similar to `https://thoughtspot.cloud/`.
  6. Select the checkbox for **I understand that this API endpoint will change data.**

  7. Click **Run**.

  8. You can verify that you successfully set up authentication by using the `Get OAuth Client App` method in the API Explorer:

     * In the API Explorer's **Search** field, enter **Get OAuth Client App**.
     * Click **Run It**.
     * In the **client_guid** field, enter the value: `looker-thoughtspot`

If you set up OAuth successfully, the **Response** tab will return the values you entered when you registered the app.

## Connecting to Looker from Thoughtspot Cloud

See the Looker connector pages in the [ThoughtSpot documentation](https://docs.thoughtspot.com/cloud/latest/connections-looker) to learn more about how to perform the following tasks:

  * Add a connection to Looker
  * Edit a connection to Looker
  * Edit the source mapping of a connection to Looker
  * Delete a table from a connection to Looker
  * Delete a table with dependent objects
  * Delete a connection to Looker

When performing the steps to [Add a connection to Looker](https://docs.thoughtspot.com/cloud/latest/connections-looker-add), use the following values to set up OAuth authentication:

  * **Host** : `LOOKER_INSTANCE_URL`
  * **OAuth Client ID** : `looker-thoughtspot`
  * **Scope** : `thoughtspot`
  * **Auth Url** : `LOOKER_INSTANCE_URL/auth`
  * **Access token Url** : `LOOKER_INSTANCE_URL/token`

When performing the steps to [Add a connection to Looker](https://docs.thoughtspot.com/cloud/latest/connections-looker-add), use the following values to set up service account authentication:

  * **Host** : `LOOKER_INSTANCE_URL`
  * **Password** : `API_CLIENT_SECRET_ASSOCIATED_WITH_THE_LOOKER_USER_ACCOUNT`
  * **User** : `API_CLIENT_ID_ASSOCIATED_WITH_THE_LOOKER_USER_ACCOUNT`