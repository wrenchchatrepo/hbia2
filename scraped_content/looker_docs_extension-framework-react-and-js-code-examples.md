# https://cloud.google.com/looker/docs/extension-framework-react-and-js-code-examples

Depth: 3

**Note:** Starting in Looker 24.0, extensions can be developed that can run in a tile on Looker dashboards. Examples and APIs that are specific to developing tile extensions can be found on the [Building tile extensions](/looker/docs/extension-framework-building-tile-extensions) documentation page.**Note:** Starting in Looker 22.20, to address potential [Content Security Policy (CSP)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP) violations, there is a new, enhanced loading mechanism for the Looker extension framework. For more information, see the [Admin settings - Extension Framework](/looker/docs/admin-panel-platform-extension-framework) documentation page.

This page provides code examples written in React and JavaScript for common functions you may want to utilize in your extensions.

## Using the Looker Extension SDK

Extensions must establish a connection with the Looker host. In React, this is done by wrapping the extension in an `ExtensionProvider40` component. This component establishes a connection with the Looker host and makes the [Looker Extension SDK](https://www.npmjs.com/package/@looker/extension-sdk) and [Looker SDK](https://github.com/looker-open-source/sdk-codegen/tree/main/packages/sdk) available to the extension.
    
    
    import React from 'react'
    import { ExtensionProvider40 } from '@looker/extension-sdk-react'
    import { DemoCoreSDK } from './DemoCoreSDK'
    
    
    export const App = () => {
     return (
       <ExtensionProvider40 chattyTimeout={-1}>
         <DemoCoreSDK />
       </ExtensionProvider40>
     )
    }
    

### Background on extension providers

Extension providers expose the Looker extension SDK and SDK API to extensions. Different versions of the extension provider have been created since the extension framework was created. This section explains the history of extension providers and why ExtensionProvider40 is the recommended provider.

The first extension provider was `ExtensionProvider`, which exposed both Looker SDKs, versions 3.1 and 4.0. The downside was that including both SDKs increased the size of the final production bundle.

`ExtensionProvider2` was then created. This was created because it did not makes sense for an extension to use both SDKs and force the developer to choose one or the other. Unfortunately, this still resulted in both SDKs being included in the size of the final production bundle.

When SDK 4.0 moved to GA, `ExtensionProvider40` was created. The advantage of `ExtensionProvider40` is that the developer does not have to choose which SDK to use, because SDK 4.0 is the only version available. Because SDK 3.1 isn't included in the final bundle, this has the advantage of reducing the size of the bundle.

To add functions from the [Looker Extension SDK](https://www.npmjs.com/package/@looker/extension-sdk), first you need to get a reference to the SDK, which can be done either from the provider or globally. Then you can call SDK functions as you would in any JavaScript application.

  * To access the SDK from the provider, follow these steps:

    
    
      import { ExtensionContext40 } from '@looker/extension-sdk-react'
    
      export const Comp1 = () => {
        const extensionContext = useContext(
          ExtensionContext40
        )
        const { extensionSDK, coreSDK } = extensionContext
    

  * To access the SDK globally (the extension _must_ be initialized before this is called), follow these steps:

    
    
        const coreSDK = getCoreSDK()
    

Now you can use the SDK as you would in any JavaScript application:
    
    
      const GetLooks = async () => {
        try {
          const looks = await sdk.ok(sdk.all_looks('id'))
          // process looks
          . . .
        } catch (error) {
          // do error handling
          . . .
        }
    }
    

## Navigating elsewhere in the Looker instance

Since the extension runs in a sandboxed iframe, you cannot navigate elsewhere within the Looker instance by updating the parent's `window.location` object. It is possible to navigate using the [Looker Extension SDK](https://www.npmjs.com/package/@looker/extension-sdk).

This function requires the [`navigation` entitlement](/looker/docs/reference/param-manifest-application#entitlements).
    
    
    import { ExtensionContext40 } from '@looker/extension-sdk-react'
    
    . . .
    
      const extensionContext = useContext(
        ExtensionContext40
      )
      const { extensionSDK } = extensionContext
    
    . . .
    
      extensionSDK.updateLocation('/browse')
    

## Opening a new browser window

Since the extension runs in a sandboxed iframe, you cannot use the parent window to open a new browser window. It is possible to open up a browser window using the [Looker Extension SDK](https://www.npmjs.com/package/@looker/extension-sdk).

This function requires either the [`new_window` entitlement](/looker/docs/reference/param-manifest-application#entitlements) to open a new window to a location in the current Looker instance, or the [`new_window_external_urls` entitlement](/looker/docs/reference/param-manifest-application#entitlements) to open a new window that runs on a different host.
    
    
    import { ExtensionContext40 } from '@looker/extension-sdk-react'
    
    . . .
    
      const extensionContext = useContext(
        ExtensionContext40
      )
      const { extensionSDK } = extensionContext
    
    . . .
      extensionSDK.openBrowserWindow('/browse', '_blank')
    . . .
      extensionSDK.openBrowserWindow('https://docs.looker.com/reference/manifest-params/application#entitlements', '_blank')
    

## Routing and deep linking

The following applies to React-based extensions.

The `ExtensionProvider`, `ExtensionProvider2`, and `ExtensionProvider40` components automatically create a React Router called `MemoryRouter` for you to use. Don't attempt to create a `BrowserRouter`, as it does not work in sandboxed iframes. Don't attempt to create a `HashRouter`, as it it does not work in sandboxed iframes for the non-Chromium-based version of the Microsoft Edge browser.

If the `MemoryRouter` is utilized and you use `react-router` in your extension, the extension framework will automatically sync your extension's router to the Looker host router. This means that the extension will be notified of browser backward and forward button clicks and of the current route when the page is reloaded. This also means that the extension should automatically support deep linking. See the extension examples for how to utilize `react-router`.

## Extension context data

Extension framework context data shouldn't be confused with React contexts.

Extensions have the ability to share context data between all users of an extension. The context data can be used for data that does not change frequently and that does not have special security requirements. Care should be taken when writing the data, as there is no data locking and the last write wins. The context data is available to the extension immediately upon startup. The [Looker Extension SDK](https://www.npmjs.com/package/@looker/extension-sdk) provides functions to allow the context data to be updated and refreshed.

The maximum size of the context data is approximately 16 MB. Context data will be serialized to a JSON string, so that also needs to be taken into account if you use context data for your extension.
    
    
    import { ExtensionContext40 } from '@looker/extension-sdk-react'
    
    . . .
    
      const extensionContext = useContext(
        ExtensionContext40
      )
      const { extensionSDK } = extensionContext
    
    . . .
    
      // Get loaded context data. This will reflect any updates that have
      // been made by saveContextData.
      let context = await extensionSDK.getContextData()
    
    . . .
    
      // Save context data to Looker server.
      context = await extensionSDK.saveContextData(context)
    
    . . .
    
      // Refresh context data from Looker server.
      context = await extensionSDK.refreshContextData()
    

## User attributes

The [Looker Extension SDK](https://www.npmjs.com/package/@looker/extension-sdk) provides an API to access Looker [user attributes](/looker/docs/admin-panel-users-user-attributes). There are two types of user attribute access:

  * Scoped — Associated with the extension. A scoped user attribute is namespaced to the extension and the user attribute must be defined in the Looker instance before it can be used. To namespace a user attribute, prefix the attribute name with the extension name. Any dash and the '::' characters in the extension name _must_ be replaced by an underscore, since dashes and colons cannot be used in user attribute names.

For example: a scoped user attribute named `my_value` used with an extension id of `my-extension::my-extension` must have a user attribute name of `my_extension_my_extension_my_value` defined. Once defined, the user attribute may be read and updated by the extension.

  * Global — These are global user attributes and are read only. An example is the `locale` user attribute.

The following is a list of user attributes API calls:

  * `userAttributeGetItem` — Reads a user attribute. A default value may be defined and will be used if a user attribute value does not exist for the user.
  * `userAttributeSetItem` — Saves a user attribute for the current user. Will fail for global user attributes. The saved value is only visible to the current user.
  * `userAttributeResetItem` — Resets a user attribute for the current user to the default value. Will fail for global user attributes.

To access user attributes, you must specify the attribute names in the [`global_user_attributes` and/or `scoped_user_attributes` entitlements](/looker/docs/reference/param-manifest-application#entitlements). For example, in the LookML [project manifest file](/looker/docs/other-project-files#project_manifest_files), you would add:
    
    
      entitlements: {
        scoped_user_attributes: ["my_value"]
        global_user_attributes: ["locale"]
      }
    
    
    
    import { ExtensionContext40 } from '@looker/extension-sdk-react'
    
    . . .
    
      const extensionContext = useContext(
        ExtensionContext40
      )
      const { extensionSDK } = extensionContext
    
      // Read global user attribute
      const locale = await extensionSDK.userAttributeGetItem('locale')
    
      // Read scoped user attribute
      const value = await extensionSDK.userAttributeGetItem('my_value')
    
      // Update scoped user attribute
      const value = await extensionSDK.userAttributeSetItem('my_value', 'abcd1234')
    
      // Reset scoped user attribute
      const value = await extensionSDK.userAttributeResetItem('my_value')
    

## Local storage

Sandboxed iframes don't allow access to browser local storage. The [Looker Extension SDK](https://www.npmjs.com/package/@looker/extension-sdk) allows an extension to read and write to the parent window's local storage. Local storage is namespaced to the extension, meaning that it cannot read local storage that is created by the parent window or other extensions.

Using local storage requires the [`local_storage` entitlement](/looker/docs/reference/param-manifest-application#entitlements).

The extension localhost API is asynchronous as opposed to the synchronous browser local storage API.
    
    
    import { ExtensionContext40 } from '@looker/extension-sdk-react'
    
    . . .
    
      const extensionContext = useContext(
        ExtensionContext40
      )
      const { extensionSDK } = extensionContext
    
      // Read from local storage
      const value = await extensionSDK.localStorageGetItem('my_storage')
    
      // Write to local storage
      await extensionSDK.localStorageSetItem('my_storage', 'abcedefh')
    
      // Delete item from local storage
      await extensionSDK.localStorageRemoveItem('my_storage')
    

## Updating the page title

Extensions may update the current page title. Entitlements are not required to perform this action.
    
    
    import { ExtensionContext40 } from '@looker/extension-sdk-react'
    
    . . .
    
      const extensionContext = useContext(
        ExtensionContext40
      )
      const { extensionSDK } = extensionContext
    
      extensionSDK.updateTitle('My Extension Title')
    

## Writing to the system clipboard

Sandboxed iframes don't allow access to the system clipboard. The [Looker Extension SDK](https://www.npmjs.com/package/@looker/extension-sdk) allows an extension to write text to the system clipboard. For security purposes, the extension is not allowed to read from the system clipboard.

To write to the system clipboard, you need the [`use_clipboard` entitlement](/looker/docs/reference/param-manifest-application#entitlements).
    
    
    import { ExtensionContext40 } from '@looker/extension-sdk-react'
    
    . . .
    
    const extensionContext = useContext(
        ExtensionContext40
      )
      const { extensionSDK } = extensionContext
    
        // Write to system clipboard
        try {
          await extensionSDK.clipboardWrite(
            'My interesting information'
          )
          . . .
        } catch (error) {
          . . .
        }
    

## Embedding dashboards, Looks, and Explores

The extension framework supports embedding of dashboards, Looks, and Explores.

The [`use_embeds` entitlement](/looker/docs/reference/param-manifest-application#entitlements) is required. We recommend that you use the [Looker JavaScript Embed SDK](https://looker-open-source.github.io/embed-sdk/) to embed content. See the [Embed SDK documentation](/looker/docs/embed-sdk) for more information.
    
    
    import { ExtensionContext40 } from '@looker/extension-sdk-react'
    
    . . .
    
      const extensionContext = useContext(
        ExtensionContext40
      )
      const { extensionSDK } = extensionContext
    
    . . .
    
      const canceller = (event: any) => {
        return { cancel: !event.modal }
      }
    
      const updateRunButton = (running: boolean) => {
        setRunning(running)
      }
    
      const setupDashboard = (dashboard: LookerEmbedDashboard) => {
        setDashboard(dashboard)
      }
    
      const embedCtrRef = useCallback(
        (el) => {
          const hostUrl = extensionContext?.extensionSDK?.lookerHostData?.hostUrl
          if (el && hostUrl) {
            el.innerHTML = ''
            LookerEmbedSDK.init(hostUrl)
            const db = LookerEmbedSDK.createDashboardWithId(id as number)
              .withNext()
              .appendTo(el)
              .on('dashboard:loaded', updateRunButton.bind(null, false))
              .on('dashboard:run:start', updateRunButton.bind(null, true))
              .on('dashboard:run:complete', updateRunButton.bind(null, false))
              .on('drillmenu:click', canceller)
              .on('drillmodal:explore', canceller)
              .on('dashboard:tile:explore', canceller)
              .on('dashboard:tile:view', canceller)
              .build()
              .connect()
              .then(setupDashboard)
              .catch((error: Error) => {
                console.error('Connection error', error)
              })
          }
        },
        []
      )
    
      return (&#60;EmbedContainer ref={embedCtrRef} /&#62;)
    

The extension examples use styled components to provide simple styling to the generated iframe. For example:
    
    
    import styled from "styled-components"
    
    export const EmbedContainer = styled.div`
      width: 100%;
      height: 95vh;
      & > iframe {
        width: 100%;
        height: 100%;
      }
    

## Accessing external API endpoints

The extension framework provides two methods for accessing external API endpoints:

  * The server proxy — Accesses the endpoint via the Looker server. This mechanism allows client IDs and secret keys to be set securely by the Looker server.
  * The fetch proxy — Accesses the endpoint from the user's browser. The proxy is the Looker UI.

In both cases you need to specify the external API endpoint in the extension [`external_api_urls` entitlement](/looker/docs/reference/param-manifest-application#entitlements).

### Server proxy

The following example demonstrates the use of the server proxy to get an access token for use by the fetch proxy. The client id and secret must be defined as user attributes for the extension. Typically, when the user attribute is set up, the default value is set to the client id or secret.
    
    
    import { ExtensionContext40 } from '@looker/extension-sdk-react'
    
    . . .
    
      const extensionContext = useContext(
        ExtensionContext40
      )
      const { extensionSDK } = extensionContext
    
    . . .
      const requestBody = {
        client_id: extensionSDK.createSecretKeyTag('my_client_id'),
        client_secret: extensionSDK.createSecretKeyTag('my_client_secret'),
      },
      try {
        const response = await extensionSDK.serverProxy(
          'https://myaccesstokenserver.com/access_token',
          {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify(requestBody),
          }
        )
        const { access_token, expiry_date } = response.body
    . . .
      } catch (error) {
        // Error handling
        . . .
      }
    

The user attribute name must be mapped to the extension. Dashes must be replaced by underscores and the `::` characters must be replaced with a single underscore.

For example, if the name of your extension is `my-extension::my-extension`, the user attributes that need to be defined for the previous example would be as follows:
    
    
    my_extension_my_extension_my_client_id
    my_extension_my_extension_'my_client_secret'
    

### Fetch proxy

The following example demonstrates the use of the fetch proxy. It uses the access token from the previous server proxy example.
    
    
    import { ExtensionContext40 } from '@looker/extension-sdk-react'
    
    . . .
    
      const extensionContext = useContext(
        ExtensionContext40
      )
      const { extensionSDK } = extensionContext
    
    . . .
    
      try {
        const response = await extensionSDK.fetchProxy(
          'https://myaccesstokenserver.com/myendpoint',
          {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
              Authorization: `Bearer ${accessToken}`,
            },
            body: JSON.stringify({
              some_value: someValue,
              another_value: anotherValue,
            }),
          }
        )
        // Handle success
    
    . . .
    
      } catch (error) {
        // Handle failure
    
    . . .
    
      }
    

## OAuth integration

The extension framework supports integration with OAuth providers. OAuth can be used to get an access token to access a particular resource, for example a Google Sheets document.

You will need to specify the OAuth server endpoint in the [`extension oauth2_urls` entitlement](/looker/docs/reference/param-manifest-application#entitlements). You may also need to specify additional URLs in the [`external_api_urls` entitlement](/looker/docs/reference/param-manifest-application#entitlements).

The extension frameworks supports the following flows:

  * Implicit flow
  * Authorization code grant type with secret key
  * PKCE code challenge and verifier

The general flow is that a child window is opened that loads an OAuth server page. The OAuth server authenticates the user and redirects back to the Looker server with additional details that can be used to get an access token.

Implicit flow:
    
    
    import { ExtensionContext40 } from '@looker/extension-sdk-react'
    
    . . .
    
      const extensionContext = useContext(
        ExtensionContext40
      )
      const { extensionSDK } = extensionContext
    
    . . .
    
        const response = await extensionSDK.oauth2Authenticate(
          'https://accounts.google.com/o/oauth2/v2/auth',
          {
            client_id: GOOGLE_CLIENT_ID!,
            scope: GOOGLE_SCOPES,
            response_type: 'token',
          }
        )
        const { access_token, expires_in } = response
    

Authorization code grant type with secret key:
    
    
      const authenticateParameters: Record&#60;string, string&#62; = {
        client_id: GITHUB_CLIENT_ID!,
        response_type: 'code',
      }
      const response = await extensionSDK.oauth2Authenticate(
        'https://github.com/login/oauth/authorize',
        authenticateParameters,
       'GET'
      )
      const exchangeParameters: Record&#60;string, string&#62; = {
        client_id: GITHUB_CLIENT_ID!,
        code: response.code,
        client_secret: extensionSDK.createSecretKeyTag('github_secret_key'),
      }
      const codeExchangeResponse = await extensionSDK.oauth2ExchangeCodeForToken(
        'https://github.com/login/oauth/access_token',
        exchangeParameters
      )
      const { access_token, error_description } = codeExchangeResponse
    

PKCE code challenge and verifier:
    
    
    import { ExtensionContext40 } from '@looker/extension-sdk-react'
    
    . . .
    
      const extensionContext = useContext(
        ExtensionContext40
      )
      const { extensionSDK } = extensionContext
    
    . . .
    
      const authRequest: Record&#60;string, string&#62; = {
        client_id: AUTH0_CLIENT_ID!,
        response_type: 'code',
        scope: AUTH0_SCOPES,
        code_challenge_method:  'S256',
      }
      const response = await extensionSDK.oauth2Authenticate(
        'https://sampleoauthserver.com/authorize',
        authRequest,
        'GET'
      )
      const exchangeRequest: Record&#60;string, string&#62; = {
        grant_type: 'authorization_code',
        client_id: AUTH0_CLIENT_ID!,
        code: response.code,
      }
      const codeExchangeResponse = await extensionSDK.oauth2ExchangeCodeForToken(
        'https://sampleoauthserver.com/login/oauth/token',
        exchangeRequest
      )
      const { access_token, expires_in } = codeExchangeResponse
    

## Spartan

Spartan refers to a method of using the Looker instance as an environment to expose extensions, and extensions only, to a designated set of users. A spartan user navigating to a Looker instance will be presented with whatever login flow the Looker admin has configured. Once the user is authenticated, an extension will be presented to the user according to their `landing_page` [user attribute](/looker/docs/admin-panel-users-user-attributes) as shown next. The user can only access extensions; they cannot access any other part of Looker. If the user has access to multiple extensions, the extensions control the user's ability to navigate to the other extensions using `extensionSDK.updateLocation`. There is one specific [Looker Extension SDK](https://www.npmjs.com/package/@looker/extension-sdk) method to allow the user to log out of the Looker instance.
    
    
    import { ExtensionContext40 } from '@looker/extension-sdk-react'
    
    . . .
    
      const extensionContext = useContext(
        ExtensionContext40
      )
      const { extensionSDK } = extensionContext
    
    . . .
      // Navigate to another extension
      extensionSDK.updateLocation('/spartan/another::extension')
    
    . . .
      // Logout
      extensionSDK.spartanLogout()
    

### Defining spartan users

In order to define a spartan user, you _must_ create a [group](/looker/docs/admin-panel-users-groups) called "Extensions Only".

Once the "Extensions Only" group has been created, navigate to the **User Attributes** page in Looker's **Admin** section and [edit the `landing_page` user attribute](/looker/docs/admin-panel-users-user-attributes#assigning_values_to_individual_users). Select the **Group Values** tab and add the "Extensions Only" group. The value should be set to `/spartan/my_extension::my_extension/` where `my_extension::my_extension` is the id of your extension. Now when that user logs in, the user will be routed to the designated extension.

## Code splitting

Code splitting is the technique where code is requested only when it is needed. Typically code chunks are associated with React routes where each route gets its own code chunk. In React this is done with the `Suspense` and `React.lazy` components. The `Suspense` component displays a fallback component while the code chunk is loaded. `React.lazy` is responsible for loading the code chunk.

Setting up to code split:
    
    
    import { AsyncComp1 as Comp1 } from './Comp1.async'
    import { AsyncComp1 as Comp2 } from './Comp2.async'
    
    . . .
    
                    <Suspense fallback={<div>Loading...</div>}>
                      <Switch>
                          <Route path="/comp1">
                            <Comp1 />
                          </Route>
                          <Route path="/comp2">
                            <Comp2 />
                          </Route>
                      </Switch>
                    <Suspense>
    

The lazy loaded component is implemented as follows:
    
    
    import { lazy } from 'react'
    
    const Comp1 = lazy(
     async () => import(/* webpackChunkName: "comp1" */ './Comp1')
    )
    
    export const AsyncComp1 = () => &#60;Home />
    

The component is implemented as follows. The component _must_ be exported as a default component:
    
    
    const Comp1 = () => {
      return (
        &#60;div&#62;Hello World&#60;/div&#62;
      )
    }
    
    export default Comp1
    

## Tree shaking

Although Looker SDKs currently support tree-shaking, this function still needs improvement. We are continually modifying our SDKs to improve tree shaking support. Some of these changes may require that you refactor your code to take advantage, but when this is required, it will be documented in the release notes.

To utilize tree-shaking, the module that you use must be exported as an esmodule and the functions that you import must be free of side effects. The [Looker SDK for TypeScript/Javascript](https://www.npmjs.com/package/@looker/sdk), [Looker SDK Runtime Library](https://www.npmjs.com/package/@looker/sdk-rtl), [Looker UI Components](https://www.npmjs.com/package/@looker/components), [Looker Extension SDK](https://www.npmjs.com/package/@looker/extension-sdk), and [Extension SDK for React](https://www.npmjs.com/package/looker-extension-sdk-react) all meet these requirements.

In an extension, use the Looker SDK 4.0, and use either the `ExtensionProvider2` or the `ExtensionProvider40` component from the [Extension SDK for React](https://www.npmjs.com/package/looker-extension-sdk-react).

The following code sets up the extension provider. You will need to tell the provider which SDK you want:
    
    
    import { MyExtension } from './MyExtension'
    import { ExtensionProvider40 } from '@looker/extension-sdk-react'
    import { Looker40SDK } from '@looker/sdk/lib/4.0/methods'
    import { hot } from 'react-hot-loader/root'
    
    export const App = hot(() => {
    
      return (
        &#60;ExtensionProvider2 type={Looker40SDK}&#62;
          &#60;MyExtension /&#62;
        &#60;/ExtensionProvider2&#62;
      )
    })
    

**Don't use the following import style in your extension:**
    
    
    import * as lookerComponents from `@looker/components`
    

The previous example brings in everything from the module. Instead, only import the components you actually need. For example:
    
    
    import { Paragraph }  from `@looker/components`
    

## Glossary

  * Code splitting — A technique for lazy loading of JavaScript until it is actually needed. Ideally, you want to keep the initially loaded JavaScript bundle as small as possible. This can be achieved by utilizing code splitting. Any functionality that is not immediately required is not loaded until it is actually needed.
  * IDE — Integrated development environment. An editor used to create and modify an extension. Examples are Visual Studio Code, Intellij, and WebStorm.
  * Scene — Generally a page view in Looker. Scenes map to major routes. Sometimes a scene will have child scenes that map to subroutes within the major route.
  * Transpile — The process of taking source code written in one language and transforming it into another language that has a similar level of abstraction. An example is TypeScript to JavaScript.