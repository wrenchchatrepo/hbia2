# https://cloud.google.com/looker/docs/embed-sdk-intro

Depth: 3

Looker's Embed SDK is a library of functions that you can add to the code of your browser-based web application to manage embedded dashboards, Looks, and Explores in your web app. The Embed SDK facilitates embedding in the following ways:

  * Providing the encapsulation of the embedded content without the need to manually create HTML elements.
  * Providing point-to-point communication so there's no cross-frame communication. The Embed SDK handles cross-domain message passing between your host webpage and your embedded Looker content, making use of a dedicated message channel.

Without the Embed SDK, you can invoke or respond to events in embedded Looker content using JavaScript events such as [`dashboard:run:start`](/looker/docs/embedded-javascript-events#dashboard:run:start) or [`page:changed`](/looker/docs/embedded-javascript-events#page:changed), which are described on the [Embedded JavaScript events](/looker/docs/embedded-javascript-events#event_type_reference) documentation page. Developers who embed Looker content with JavaScript events must create the HTML elements to house the embedded content and rely on window broadcast events for communications between the web app and the embedded content.

Note that the Looker Embed SDK is different from the Looker API and the Looker API SDK:

  * The Looker Embed SDK lives in the client-side code of your web application and manages the Looker embed context and content. (The Embed SDK does not provide access to the Looker API).
  * The [Looker API](/looker/docs/api-getting-started) lives on the server with your Looker instance and executes commands on the Looker server.
  * [Looker API client SDKs](/looker/docs/api-sdk) reside in the code of non-browser applications to provide easy access to Looker API functions.

Be aware that Looker does not control the order in which browsers dispatch events to web applications. This means that the order of events is not guaranteed across browsers or platforms. Be sure to write your JavaScript appropriately to account for the event handling of different browsers.

## Quick example

This example constructs a Looker embed context, inserts it into a DOM element with an ID of `dashboard`, and then displays a dashboard with an ID of `11` in the Looker embed context. The [`dashboard:run:start`](/looker/docs/embedded-javascript-events#dashboard:run:start) and [`dashboard:run:complete`](/looker/docs/embedded-javascript-events#dashboard:run:complete) events are used to update the state of the embedding window's UI, and a button with an ID of `run` is scripted to send a `dashboard:run` message to the dashboard.
    
    
    LookerEmbedSDK.init('looker.example.com', '/auth')
    
    const setupDashboard = (dashboard) => {
      document.querySelector('#run').addEventListener('click', () => {
        dashboard.send('dashboard:run')
      })
    }
    
    LookerEmbedSDK.createDashboardWithId(11)
      .appendTo('#dashboard')
      .on('dashboard:run:start',
          () => updateState('#dashboard-state', 'Running')
      )
      .on('dashboard:run:complete',
          () => updateState('#dashboard-state', 'Done')
      )
      .build()
      .connect()
      .then(setupDashboard)
      .catch((error: Error) => {
        console.error('An unexpected error occurred', error)
      })
    

A more complete example is described on the [Embed SDK demo](/looker/docs/embed-sdk-demo) documentation page.

## Setting up the Looker Embed SDK

The Looker Embed SDK uses a fluent interface pattern. Once you install the Embed SDK, you then construct the embedded content and connect to the embedded content.

### Installing the Embed SDK

You can get Looker's Embed SDK library through the node package manager (NPM) at <https://www.npmjs.com/package/@looker/embed-sdk>. However, if you want to see the sample code or the [demo](/looker/docs/embed-sdk-demo), you should instead use the Looker Embed SDK repository.

To install the Looker Embed SDK using the Looker Embed SDK repo:

  1. Install [Node.js](https://nodejs.org/en/download/), if you don't already have it.
  2. Download or clone the [`/looker-open-source/embed-sdk`](https://github.com/looker-open-source/embed-sdk) repository.
  3. In a terminal window, navigate to the `/embed-sdk` directory and run these commands:

    
    
    npm install
    npm start
    

### Constructing the embedded content

First, initialize the SDK with address of your web server and, optionally, the endpoint on your server that will perform authentication. These are used by all the embedded content.

> Include the port number if it is required to reach the Looker server from browser clients. For example: `looker.example.com:443`
    
    
    LookerEmbedSDK.init('looker.example.com', '/auth')
    

Then the embedded content is built using a series of steps to define its parameters. Some of these parameters are optional, and some are mandatory.

The process starts with creating the builder either with a dashboard `id` or with a `url` that refers to a dashboard (created by the process that is described on the [Signed embedding](/looker/docs/single-sign-on-embedding) documentation page).
    
    
    LookerEmbedSDK.createDashboardWithId(id)
    

or
    
    
    LookerEmbedSDK.createDashboardWithUrl(url)
    

You can then add additional attributes to the builder to complete your setup. For example, you can specify where in your web page to insert the Looker embed UI. The following call places the Looker embed UI inside an HTML element with an ID value of `dashboard`:
    
    
    .appendTo('#dashboard')
    

You can add event handlers:
    
    
    .on('dashboard:run:start',
      () => updateState('#dashboard-state', 'Running')
    )
    .on('dashboard:run:complete',
      () => updateState('#dashboard-state', 'Done')
    )
    

You finish by building the embedded element:
    
    
    .build()
    

### Connecting to the embedded content

If you want to send messages to and receive messages from the embedded element, you need to call `connect()`, which returns a Promise that resolves to the communication interface of the given element:
    
    
    .connect()
    .then(setupDashboard)
    .catch(console.error)
    

## Building URLs for the SDK

The main documentation for Looker signed embed URLs is on the [Signed embedding](/looker/docs/single-sign-on-embedding) documentation page. The only difference when creating URLs for the SDK is that you will need to add an `sdk=2` parameter to the embed URL alongside other parameters, such as filters and the `embed_domain` parameter. This parameter allows Looker to determine that the SDK is present and take advantage of additional features that are provided by the SDK. For example:
    
    
    /embed/looks/4?embed_domain=https://mywebsite.com&sdk=2
                                                     ^^^^^^
    

The SDK cannot add this parameter itself because the parameter is part of the signed embed URL.

## The auth endpoint

Because the embed secret needs to be carefully guarded, signed embed URLs cannot be created in the browser. To make the process easier and more secure, you can instead follow these steps:

  1. Implement a URL signing function in your web server. The server should return a signed URL using one of the processes documented in the [Looker Embed SSO Examples](https://github.com/looker/looker_embed_sso_examples) GitHub repository.
  2. Pass the signed embed URL to that signing endpoint in the Embed SDK. The location of the endpoint is specified by the `authUrl` parameter in [`LookerEmbedSDK.init()`](/looker/docs/embed-sdk-reference).

If specified, whenever an embed element is created using just an ID, its embed URL is generated using the type of the element, the provided Looker host, and any provided parameters. For example:
    
    
    LookerEmbedSDK.init('looker.example.com', '/looker_auth')
    LookerEmbedSDK.createcreateDashboardWithId(11)
      .build()
    

The previous example will call the `/looker_auth` endpoint and return a signed embed URL that can be used to create the embedded content:
    
    
    src=https://looker.example.com/embed/dashboards/11?sdk=2&embed_host=https://yourhost.example.com
    

### Advanced auth configuration

The auth endpoint can be configured further to allow custom request headers as well as CORS support. You can do this by passing an options object to the `init` method:
    
    
    LookerEmbedSDK.init('looker.example.com',
      {
        url: 'https://api.acme.com/looker/auth',
        headers: [{'name': 'Foo Header', 'value': 'Foo'}],
        params: [{'name': 'foo', 'value': 'bar'}],
        withCredentials: true // Needed for CORS requests to Auth endpoint include Http Only cookie headers
      })
    
    

### Node helper

A signing helper method `createSignedUrl()` is provided in `server_utils/auth_utils.ts`. Its usage is as follows:
    
    
    import { createSignedUrl } from './auth_utils'
    
    app.get('/looker_auth', function(req, res) {
      // TO DO: Add your code here to authenticate that the request is from a valid user
      const src = req.query.src;
      const host = 'https://looker.example.com'
      const secret = YOUR_EMBED_SECRET
      const user = authenticatedUser
      const url = createSignedUrl(src, user, host, secret);
      res.json({ url });
    });
    

This is the user data structure:
    
    
    interface LookerEmbedUser {
      external_user_id: string
      first_name?: string
      last_name?: string
      session_length: number
      force_logout_login?: boolean,
      permissions: LookerUserPermission[]
      models: string[]
      group_ids?: number[]
      external_group_id?: string
      user_attributes?: {[key: string]: any}
      access_filters: {}
    }
    

> The `access_filters` parameter was removed in Looker 3.10, but it is still required with an empty placeholder in the embed URL.

## Troubleshooting

### Logging

The Embed SDK is built on top of [chatty](https://github.com/looker-open-source/chatty). Chatty uses [debug](https://github.com/visionmedia/debug) for logging. You can enable logging in a browser console with this command:
    
    
    localStorage.debug = 'looker:chatty:*'
    ```none
    
    Note that both the parent window and the embedded content have separate local storage, so you can enable logging on one, the other, or both. You can disable logging with this command:
    
    ```javascript
    localStorage.debug = ''