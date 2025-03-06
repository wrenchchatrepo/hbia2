# https://cloud.google.com/looker/docs/action-hub

Depth: 3

In addition to delivering content to Looker's built-in destinations, you can use _actions_ — also called _integrations_ — to deliver content to third-party services that are integrated with Looker through an action hub server.

**Note:** Actions that are served through an action hub server differ from [data actions](/looker/docs/reference/param-field-action), which are defined by the `action` LookML parameter.

This page will walk you through your options for building custom actions that you can request to add to the Looker Action Hub _or_ add to your own private action hub server. This page also describes how to spin up a local action hub server to test your custom actions or run a private action hub server.

To get started using actions, you can either:

  * Use Looker's existing [actions](/looker/docs/admin-panel-platform-actions#list_of_integrated_services) available from the Looker Action Hub.
  * Build and publish a custom action to the [Looker Action Hub](https://github.com/looker-open-source/actions) for public use.
  * Build and publish a custom action to a private action hub server for private use.

![](/static/looker/docs/images/develop-action-hub-workflow-612.png)

Once the action is added to the action hub, a Looker admin can [enable](/looker/docs/admin-panel-platform-actions) the action for use in [delivering Looker content](/looker/docs/scheduling) to those services.

You can also set up multiple action hubs if you would like to use Looker's integrations through the Looker Action Hub and also host your own private or custom actions. The actions for each action hub would appear on the **Actions** page of the **Admin** panel.

## The Looker Action Hub

Looker hosts and provides the Looker Action Hub, a stateless server that implements [Looker's Action API](https://github.com/looker-open-source/actions/blob/master/docs/action_api.md) and exposes popular actions. Any data that your users send using an action will be processed temporarily on the Looker Action Hub server rather than in your Looker instance.

Looker is already [integrated with several services](/looker/docs/admin-panel-platform-actions#list_of_integrated_services). See the [Admin settings - Actions](/looker/docs/admin-panel-platform-actions) documentation page to learn how to enable these existing services.

### Looker Action Hub requirements

**Note:** To use Looker integrations, the Looker Action Hub must be able to communicate with the Looker instance and fulfill the Looker Action Hub requirements. Admins of customer-hosted instances may need to consider [additional factors](/looker/docs/action-hub#considerations_for_customer-hosted_instances) when choosing to enable Looker integrations from the Looker Action Hub, especially integrations that [support streamed results](/looker/docs/action-hub#uses_streaming) or that use [OAuth](/looker/docs/action-hub#configuring_an_action_for_oauth).

The Looker Action Hub must be able to send and receive API requests in the following ways:

  * From the Looker instance to the Looker Action Hub network
  * From the Looker user's browser to the Looker Action Hub network
  * From the Looker Action Hub network to the Looker instance

If your Looker deployment cannot accommodate these requests or if the [IP Allowlist](/looker/docs/admin-panel-server-ip-allowlist) feature is enabled on your Looker instance, consider setting up a local action hub server to serve private [Looker integrations](/looker/docs/admin-panel-platform-actions#list_of_integrated_services) or custom actions. Admins of customer-hosted instances can also [deploy a local action server specifically for OAuth and streaming actions](/looker/docs/best-practices/action-hub-oauth-actions).

**Important:** Actions can return up to 7 MB of data.

#### Requests from the Looker instance to the Looker Action Hub network

Requests to `actions.looker.com` resolve to a dynamic IP address. Outgoing requests from the Looker instance must be able to reach the following endpoints:
    
    
    actions.looker.com/
    actions.looker.com/actions/<name>/execute
    actions.looker.com/actions/<name>/form
    

where `name` is the programmatic name of the action.

#### Requests from the Looker user's browser to the Looker Action Hub network

The Looker user's browser must be able to make requests to the following Looker Action Hub endpoints (for OAuth):
    
    
    actions.looker.com/actions/<name>/oauth
    

where `name` is the programmatic name of the action.

#### Requests from the Looker Action Hub network to the Looker instance

The Looker Action Hub must make requests to the Looker instance for actions that support streamed results or that use OAuth.

A streaming action enables the action to consume queries that deliver **All Results**. OAuth-enabled actions use per-user authentication through OAuth 2.0 flows. OAuth actions must store user credentials in their source Looker instance because the Looker Action Hub is stateless and multi-tenant, and it will not store user-specific credentials of any kind.

The requests from the Looker Action Hub to a Looker instance take the following forms:
    
    
    GET <host_looker_url>/downloads/<random_40_char_token>
    POST <host_looker_url>/action_hub_state/<random_40_char_token>
    

These URLs are generated on the spot in the Looker instance before being sent to the Looker Action Hub. For this reason, the Looker Action Hub needs to be able to both resolve the `<host_looker_url>` to an IP address _and_ make requests into the network in which your Looker instance resides.

The Looker Action Hub has static egress IP addresses that the requests will always come from: `35.153.89.114`, `104.196.138.163`, and `35.169.42.87`. Admins of Looker-hosted instances who have enabled the [IP allowlist](/looker/docs/admin-panel-server-ip-allowlist) must add these IP addresses to use any actions that support streamed results or that use OAuth.

#### Considerations for customer-hosted instances

To use [Looker integrations](/looker/docs/admin-panel-platform-actions#list_of_integrated_services), the Looker Action Hub must be able to communicate with the Looker instance and fulfill the Looker Action hub requirements. This is not always possible with customer-hosted Looker instances, for various reasons. If bi-directional communication between the Looker Action Hub and the Lookerinstance is not possible, the Looker Action Hub may exhibit unexpected or undesirable behavior, such as [hanging queries](/looker/docs/managing-business-user-features#send-schedule-streaming-action-hub) or unavailable actions.

To address the potential issue of the Looker Action Hub not being able to communicate with the Looker instance, Looker admins can implement one of the solutions shown later on this page. The appropriate solution or combination of solutions will depend on the architecture of the Looker instance:

  * If the customer-hosted instance _is not_ resolvable by the Looker Action Hub — that is, the Looker Action Hub cannot receive requests from the Looker instance — Looker admins can [contact a Google Cloud sales specialist](https://cloud.google.com/contact) to enable the `public_host_url` license feature. That license feature reveals the [`--public-host-url` startup option](/looker/docs/startup-options#public_host_url), which lets admins specify a resolvable `<public_host_url>` hostname that is different from the instance `<host_looker_url>`. The `public_host_url` overrides the hostname for some specific Looker Action Hub callback URLs and routes those callback URLs through a reverse proxy that has the `public_host_url` as a publicly resolvable name. This reverse proxy accepts requests only from the static egress IP addresses for the Looker Action Hub; Looker admins who use this method must add to the allowlist the egress IP addresses from which the Looker Action Hub makes requests to the Looker instance: `35.153.89.114`, `104.196.138.163`, and `35.169.42.87`.

  * If the customer-hosted instance URL _is_ resolvable by the Looker instance but the Looker Action Hub cannot send requests to the Looker instance, users may be unable to configure or use actions that support streamed results or that use OAuth. To solve this, Looker admins must add to the allowlist the egress IP addresses from which the Looker Action Hub makes requests to the Looker instance: `35.153.89.114`, `104.196.138.163`, and `35.169.42.87`.

  * If neither of the aforementioned solutions is appropriate for the Looker instance architecture, Looker admins can [deploy a customer-hosted action hub](/looker/docs/action-hub#setting_up_a_local_action_hub_server) for all actions or just for actions that [support streamed results or that use OAuth](/looker/docs/best-practices/action-hub-oauth-actions).

  * To deploy a customer-hosted action hub, you must ensure that the JAR file is hosted on a public server so that the Looker Action Hub can communicate with it. This solution is not recommended, however.

Additionally, the OAuth and streaming actions might not be usable on a customer-hosted Looker instance if the instance uses an SSL certificate that is issued by a Certificate Authority (CA) that is not on this [list of root certificates](https://github.com/nodejs/node/blob/v12.13.0/src/node_root_certs.h).

## Building a custom action

This section describes the steps to follow to write and test a custom action using the Looker Action Hub source code. To see functional code examples, check the existing actions in the [`looker-open-source/actions` repo](https://github.com/looker-open-source/actions/tree/master/src/actions) in GitHub.

You can create a custom action by:

  1. Setting up a development repo
  2. Writing your action
  3. Testing your action
  4. Publishing and enabling your action, either in the Looker Action Hub or on your own private action hub server

As with any action, you may need to configure your LookML models with specific parameters before you can use the action to deliver your data.

### Setting up a development repo

The Looker Action Hub is a Node.js server written in TypeScript, a small layer on top of modern JavaScript that adds type information to help catch programming errors. If you're familiar with JavaScript, most of the TypeScript language should be familiar to you.

Running the Looker Action Hub requires the following software:

  * [Node.js](https://nodejs.org/)
  * Node Version Manager ([NVM](https://github.com/creationix/nvm) — to select the proper Node.js version)
  * [Yarn](https://yarnpkg.com/en/) (to manage dependencies)

Once you've installed the required software, you're ready to set up your development environment. The following example uses Git.

  1. Clone the `looker-open-source/actions` repo locally:
    
        git clone git@github.com:looker-open-source/actions.git
    

  2. Create a directory with the name of your action in the `actions/src/actions` directory. For example:
    
        mkdir actions/src/actions/my_action
    

  3. Start populating your directory with the files you'll need to execute your action. See the [actions GitHub repo](https://github.com/looker-open-source/actions/tree/fd4ce4e63f44554c7257584df380f8a4e4adfc03/src/framework) for an example file structure.

Looker recommends that you also add the following:

  * A README to explain the purpose and means of authentication for your action
  * A PNG icon to display in the Looker Action Hub (or private action hub on your Looker instance) and in the Looker data delivery windows
  * Any files for tests you want to run on your action code — this is different from testing your action

### Writing an action

A design requirement for the Looker Action Hub server is that it remain completely stateless, so storing any information in the action application or service is not allowed. Any information needed to fulfill the action must be provided within the action file's request calls.

The exact contents of the action file will vary depending on the service, the type or level at which the action operates, and what data or visualization formats need to be specified. The action can also be configured for OAuth 2.0 authorization flows.

Action files are based on the `/execute` API method. Looker API requests are passed a [`DataActionRequest`](https://github.com/looker-open-source/actions/blob/fd4ce4e63f44554c7257584df380f8a4e4adfc03/src/framework/data_action_request.ts) each time a user executes the action within Looker. The `DataActionRequest` contains all the data and metadata that are needed to execute your action. A `/form` method is also available, which can be used to collect additional information from the user before they execute the action. The fields that you specify in the `/form` will appear in the **Send** or **Schedule** pop-up when users select the action as a destination for their data delivery.

**Note:** If you're using the [Looker Action API](https://github.com/looker-open-source/actions/blob/master/docs/action_api.md), the format of these parameters may appear different.

When writing your action file, include at least the following parameters marked **Required** in your action definition:

Parameter | Required | Description | Data type  
---|---|---|---  
`name` | Yes | A unique name for the action. This should be unique across all actions in the Looker Action Hub. | string  
`url` | Yes | An absolute URL of the `/execute` endpoint for this action. | string  
`label` | Yes | A human-readable label for the action. | string  
`supportedActionTypes` | Yes | A list of action types the action supports. Valid values are `"cell"`, `"query"`, and `"dashboard"`. | string | `formURL` | No | An absolute URL of the `/form` endpoint for this action. | string  
`description` | No | Description of the action. | string  
`params` | No | Array of `parameters` for the action. Include the name, label, and description in string format for each parameter. These are the fields that appear on the action's enablement page in the **Admin** panel. To manage how users can deliver data to an action destination, you can specify a [user attribute](/looker/docs/admin-panel-users-user-attributes) for which a user must have a defined value. | `parameters`  
`supportedFormats` | No | A list of data formats the action supports. Valid values are `"txt"`, `"csv"`, `"inline_json"`, `"json"`, `"json_detail"`, `"json_detail_lite_stream"`, `"xlsx"`, `"html"`, `"wysiwyg_pdf"`, `"assembled_pdf"`, and `"wysiwyg_png"`.`` | string  
`supportedFormattings` | No | A list of formatting options the action supports. Valid values are `"formatted"` and `"unformatted"`. | string  
`supportedVisualizationFormattings` | No | A list of visualization formatting options the action supports. Valid values are `"apply"` and `"noapply"`. | string  
`iconName` | No | A Data URI representing an icon image for the action. | string  
`requiredFields` | No | A list of descriptions of required fields that this action is compatible with. If there are multiple entries in this list, the action requires more than one field. | `RequiredField`  
`supportedDownloadSettings` | No | A Boolean that determines whether the action will be sent a one-time-use download URL to facilitate unlimited streaming of data. The parameter is set by the `usesStreaming` parameter, which is a `true/false` Boolean. If `usesStreaming = true`, then `supportedDownloadSettings = url`. If `usesStreaming = false`, then `supportedDownloadSettings = push`. | Boolean  
`usesOAuth` | No | A Boolean that determines whether the action is an OAuth action. This will determine whether the action will be sent a one-time-use link to be able to set `state` for a specific user for this action. | Boolean  
`usesStreaming` | No | A Boolean that determines whether the action supports streamed query results. Check the **Uses data streaming (Yes/No)** column in the [list of integrated services](/looker/docs/admin-panel-platform-actions#list_of_integrated_services). Actions that stream results may require configuration of a local action hub server — see the [Setting up a local action hub for actions that use OAuth or streaming](/looker/docs/best-practices/action-hub-oauth-actions) Best Practices page for more information. | Boolean  
`minimumSupportedVersion` | No | The minimum Looker version in which the action will appear in the **Admin** panel Action Hub list. | string  
  
Examples from the Looker Action Hub actions are [on GitHub](https://github.com/looker-open-source/actions/tree/master/src/actions) for reference.

#### Supported action types

Looker supports three types of actions, as specified in the `supportedActionTypes` parameter of your action: query, cell, and dashboard.

  * **A query-level action:** This is an action that sends an entire query. The [Segment action](https://github.com/looker-open-source/actions/tree/master/src/actions/segment), for example, is a query-level action.
  * **A cell-level action:** A cell-level action sends the value of a single, specific cell in a data table. This action type is different from [data actions](/looker/docs/reference/param-field-action), which can be defined for dimensions or measures using the `action` parameter. To send information from a specific cell within a table, Looker uses tags to map actions to the corresponding cells. Actions need to specify which tags they support in `requiredFields`. To map actions and fields, fields in LookML need to specify which tags they are mapped to with the LookML [`tags` parameter](/looker/docs/reference/param-field-tags). For example, the [Twilio Message action](https://github.com/looker-open-source/actions/tree/master/src/actions/twilio) uses a `phone` tag so that LookML developers can control on which phone number fields the Twilio action will appear.
  * **A dashboard-level action:** A dashboard-level action supports sending an image of a dashboard. For example, the [SendGrid action](https://github.com/looker-open-source/actions/tree/master/src/actions/sendgrid) sends dashboard images through email.

##### Adding user attributes to custom actions

For custom actions, you can add user attributes in the `params` parameter of your action file. If the parameter is required, then each user must have a value for this attribute defined in [their user account](/looker/docs/admin-panel-users-user-attributes#assigning_values_to_individual_users) or for a [user group](/looker/docs/admin-panel-users-user-attributes#assigning_values_to_user_groups) they belong to, in addition to the `send_to_integration` [permission](/looker/docs/admin-panel-users-roles#send_to_integration), to see the action as a destination option when sending or scheduling content.

To add a user attribute to your action:

  1. A Looker admin may need to [create the user attribute](/looker/docs/admin-panel-users-user-attributes#creating_user_attributes) that corresponds to the `user_attribute_param` if it does not already exist.
  2. Define a valid value for the user attribute for the users or user groups that need to deliver content to your action destination. (These users must also have `send_to_integration` permissions.)
  3. The `params` parameter represents the form fields that a Looker admin must configure on the action's enablement page from the **Actions** list in the **Admin** panel. In the `params` parameter of your action file, include the following:

    
    
      params = [{
        description: "A description of the param.",
        label: "A label for the param.",
        name: "action_param_name",
        user_attribute_name: "user_attribute_name",
        required: true,
        sensitive: true,
      }]
    

where `user_attribute_name` is the user attribute that is defined in the **Name** field on the **User Attributes** page in the **Users** section of the **Admin** panel, `required: true` means that a user must have a non-null and valid value defined for that user attribute to see the action when data is being delivered, and `sensitive: true` means that the user attribute is encrypted and never displayed in the Looker UI once it is entered. You can specify multiple user attribute subparameters.

  1. Deploy your updates to the action hub server. 
     * If you are adding a new action, a Looker admin will need to enable the action by clicking the **Enable** button next to the action on the **Actions** page in the **Admin** panel.
     * If you are updating an existing action, refresh your list of actions by clicking the **Refresh** button. Next, click the **Settings** button.
  2. On the action settings/enablement page, a Looker admin must configure the action's form fields to pull information from the user attribute by clicking the user attribute icon ![](/static/looker/docs/images/admin-actions-user-attribute-icon-712.png) to the right of the appropriate field and selecting the desired user attribute.

##### `requiredField` parameters in cell-level actions

For cell-level actions, you can configure your model's LookML fields to deliver data to that action destination by specifying which [tags](/looker/docs/reference/param-field-tags) your action supports in the `requiredFields` parameter of your action file.

Parameter | Required | Description | Data Type  
---|---|---|---  
`tag` | No | If present, matches a field that has this tag. | string  
`any_tag` | No | If present, supersedes `tag` and matches a field that has any of the provided tags. | string  
`all_tags` | No | If present, supersedes `tag` and matches a field that has all the provided tags. | string  
  
#### Supported data formats

The `DataActionRequest` class defines what data delivery format is available for the action to work with. For query-level actions, the request will contain an attachment that can be in several formats. The action can either specify one or more `supportedFormats` or let the user choose the format by specifying all possible formats. For cell-level actions, the value of the cell will be present on `DataActionRequest`.

### Configuring an action for OAuth

**Note:** OAuth-enabled actions cannot be configured from the Looker Action Hub for Looker instances that have the [IP Allowlist](/looker/docs/admin-panel-server-ip-allowlist) feature enabled or that cannot accommodate the Looker Action Hub requirements. See the [Setting up a local action hub for actions that use OAuth or streaming](/looker/docs/best-practices/action-hub-oauth-actions) Best Practices page for more information about configuring an action for OAuth.

You can configure your action so that users can authenticate into the action with OAuth. Even though the Looker Action Hub must remain stateless, you can enforce a state through a form request from the [Looker Action API](https://github.com/looker-open-source/actions/blob/master/docs/action_api.md).

#### Looker action OAuth flow

For actions in the Looker Action Hub, you can extend an `OAuthAction` instead of a `Hub.Action` to set a Boolean that indicates which OAuth methods are needed to authenticate a user into an action. For every OAuth-enabled or state-enabled action, Looker stores a per-user, per-action state, so that each action and user combination has an independent OAuth event.

The flow for creating actions typically involves a `/form` request followed by a `/execute` request. For OAuth, the `/form` request should have a method to determine if the user is authenticated within the target service. If the user is already authenticated, the action should return a normal `/form` in accordance with whatever the `/execute` request requires. If the user is not authenticated, the action returns a link that will initialize an OAuth flow.

#### Saving state with the OAuth URL

Looker will send an HTTP POST request with an empty body to the [`ActionList` endpoint](https://github.com/looker-open-source/actions/blob/master/docs/action_api.md). If the action returns `uses_oauth: true` in its definition, then the action will be sent a one-time-use `state_url` in every `/form` request from Looker. The `state_url` is a special one-time-use URL that sets a user's state for a given action.

If the user is not authenticated with the endpoint, the `/form` returned should contain a `form_field` of type `oauth_link` that goes to the `/oauth` endpoint of an action. The `state_url` should be encrypted and saved as a `state` param in the `oauth_url` that is returned. For example:
    
    
    {
            "name": "login",
            "type": "oauth_link",
            "label": "Log in",
            "description": "OAuth Link",
            "oauth_url": "ACTIONHUB_URL/actions/my_action/oauth?state=encrypted_state_url"
    }
    

In this example, the `/oauth` endpoint redirects the user to the authentication server. The `/oauth` endpoint constructs the redirect in the `oauthUrl(...)` method on an OAuth action, as shown in the [Dropbox OauthUrl](https://github.com/looker-open-source/actions/blob/2d38b8aab8d7596f385c33c815699180eabbde86/src/actions/dropbox/dropbox.ts#L111-L121).

The `state` param containing that encrypted `state_url` should be passed to the Looker Action Hub.

#### Saving state with the action hub redirect URI

In the `/oauth` endpoint, a `redirect_uri` for the action hub is also created and passed to the action's `oauthUrl(...)` method. This `redirect_uri` is of the form `/actions/src/actions/my_maction/oauth_redirect` and is the endpoint used if the authentication returns a result.

This endpoint will call the `oauthFetchInfo(...)` method, which should be implemented by the `OauthAction` method to extract the necessary information and attempt to receive or save any state or `auth` received from the authentication server.

The `state` decrypts the encrypted `state_url` and uses it to POST `state` back to Looker. The next time that a user makes a request to that action, the newly saved state will be sent to the Looker Action Hub.

### Adding your action files to the Looker Action Hub repo

Once your action file is written, in the Looker Action Hub repo:

  1. Add the action file (for example, `my_action.ts`) to `actions/src/actions/index.ts`.
    
        import "./my_action/my_action.ts"
    

  2. Add any Node.js package requirements that you utilized in the writing of your action. For example:
    
        yarn add aws-sdk
    yarn add express
    

  3. Install the Node.js dependencies of the Looker Action Hub server.
    
        yarn install
    

  4. Run any tests you wrote.

    
    
    yarn test
    

## Testing an action

For complete testing, you can try your action against your Looker instance by hosting a private action hub server. This server needs to be on the public internet with a valid SSL certificate and must be able to initiate and receive connections or HTTPS requests to and from Looker. For this, you can use a cloud-based platform such as Heroku, as shown in the following example. Alternatively, you can use any platform that satisfies the aforementioned requirements.

### Setting up a local action hub server

In this example, we will take the action we developed in the `looker-open-source/actions/src/actions` GitHub repo and will be committing the code to a new Git branch. We recommend that you work on features using branches so that you can easily track your code and, if desired, easily create a PR with Looker.

  1. To get started, create your branch and then stage and commit your work. For example:
    
        git checkout -b my-branch-name
    git add file-names
    git commit -m commit-message
    

  2. For this example, to push a branch to Heroku, configure your Git repo with Heroku as a remote option in your command line:
    
        heroku login
    heroku create
    git push heroku
    

  3. Heroku will return the public URL now hosting the action hub for your use. Visit the URL or run `heroku logs` to confirm that the action hub is running. If you forget the public URL, you can run the following in your command line:
    
        heroku info -s | grep web_url
    

Heroku will return your public URL. For example: `https://my-heroku-action-server-1234.herokuapp.com`

  4. In your command line, set your action hub base URL:
    
        heroku config:set ACTION_HUB_BASE_URL="https://my-heroku-action-server-1234.herokuapp.com"
    

  5. Set your action hub label:
    
        heroku config:set ACTION_HUB_LABEL="Your Action Hub"
    

  6. Looker uses an authorization token to connect to the action hub. Generate the token in your command line:
    
        heroku run yarn generate-api-key
    

If you are not using Heroku, as we are in this example, instead use:
    
        yarn generate-api-key
    

Heroku will return your authorization token. For example: `Authorization: Token token="abcdefg123456789"`

  7. Set your action hub secret using the secret key:
    
        heroku config:set ACTION_HUB_SECRET="abcdefg123456789"
    

> Customer-hosted deployments may require configuration of additional environment variables not documented here.

  8. Add your action on your local Looker instance by going to **Admin** > **Actions**.

     * At the bottom of the list of actions, click **Add Action Hub**.
     * Enter the **Action Hub URL** and, optionally, a **Secret Key**.
     * Find your action in the **Actions** list within Looker's **Admin** menu.
     * Click **Enable**.

If your action requires that specific kinds of data be passed from Looker, be sure to configure any models to include the appropriate [`tags`](/looker/docs/reference/param-field-tags) parameter.

Now you're ready to test your action!

### Testing dashboard-level and query-level actions

In your Looker instance, configure your LookML model with tags, if necessary. Create and [save a Look](/looker/docs/saving-and-editing-looks#saving_looks_from_an_explore). On the saved Look, click the upper-right menu and select **Send** with your action as the destination. If you have a form for delivery, Looker will render it in the **Sent** window.

Click **Send Test** to deliver the data. The status of the action will appear in the **Scheduler History** in the **Admin** panel. If your action encounters an error, it will be shown in the **Admin** panel, and Looker will send an email with the error message to the user who sent the action.

### Testing cell-level actions

Set up a LookML field with the proper tags for your action. In your Looker instance, run a query that includes that field. Find the field in the data table. Click the **…** in the cell and select **Send** from the drop-down menu. If you receive errors, you'll need to do a full refresh on the data table after you address those errors.

  * If your action is delivered without any errors, you're ready to publish your action!
  * If you want to keep hosting your action privately, you can publish to your private action hub.
  * If you want to publish your action for use by all Looker customers, see the section on Publishing to the Looker Action Hub.

## Publishing and enabling a custom action

There are two publication options for custom actions:

  * Publishing to the Looker Action Hub: This makes your action available to anyone who uses Looker.
  * Publishing to a private action hub server: This makes your action available on your Looker instance only.

Once your action is published, you can [enable it](/looker/docs/admin-panel-platform-actions#enabling_an_action) from the **Actions** page in the **Admin** panel.

### Publishing to the Looker Action Hub

This approach is the easiest and works for any action that you'd like to make available to anyone who uses Looker.

After your action has been tested, you can submit a PR to the `looker-open-source/actions` repo in GitHub.

  1. Enter the following command:
    
        git push <your fork> <your development branch>
    

  2. Create your pull request with the [`looker-open-source/actions` repo](https://github.com/looker-open-source/actions) as your target.

  3. Fill out the [Looker Marketplace & Action Hub Submission Form](https://docs.google.com/forms/d/e/1FAIpQLSe-ERN2X9_5E9g06eYjiq4ea4s7tgrc_yjN0ZQDxfY_Y2JT2A/viewform). For more information about the form requirements, see [Submitting content to the Looker Marketplace](https://docs.looker.com/data-modeling/marketplace/submit-content).

Looker will review your action code. We reserve the right to decline your PR but can help you with any issues that you have and offer suggestions for improvement. We then merge the code into the `looker-open-source/actions` repo and deploy it to `actions.looker.com`. Once the code is deployed, it will be available to all Looker customers.

  4. [Enable the action](/looker/docs/admin-panel-platform-actions) in your Looker instance, so that it will appear as an option for data delivery.

### Publishing to a private action hub server

If you have custom actions that are private to your company or use case, you should _not_ add your action to the `looker-open-source/actions` repo. Instead, create a private action hub using the same Node.js framework you used to test your action.

You can set up your internal action hub server on your own infrastructure or using a cloud-based application platform (our example used Heroku). Don't forget to fork the Looker Action Hub to your private action hub server before deployment.

## Configuring a LookML model for use with an action

For both custom actions and actions that are available from the Looker Action Hub, you must identify the relevant data fields by using the [`tags`](/looker/docs/reference/param-field-tags) parameter in your LookML model. The **Actions** page in the **Admin** panel will provide information about the tags that are required for the service, if any.

For example, a **Twilio Send Message** integration sends a message to a list of phone numbers. On the **Actions** page in the **Admin** panel, the integration displays the subtext "Action can be used with queries that have a field tagged `phone`".

This means that the **Twilio Send Message** service requires a query that includes a phone number field and that uses the `tags` parameter to identify which field in the query contains phone numbers. You identify a phone number field in LookML by specifying `tags: ["phone"]` for that field. Your LookML for a phone number field might look like this:
    
    
    dimension: phone {
      tags: ["phone"]
      type: string
      sql: ${TABLE}.phone ;;
    }
    

An integration that does not require tags will display the subtext "Action can be used with any query" on the **Actions** page in the **Admin** panel.

Be sure to identify any required fields in your LookML model with the [`tags`](/looker/docs/reference/param-field-tags) parameter so that your users can use the service to send data.

### What's next

Learn how to deliver the contents of [a Look or an Explore](/looker/docs/delivering-looks-explores) or of a [dashboard](/looker/docs/scheduling-and-sending-dashboards) to an integrated service.