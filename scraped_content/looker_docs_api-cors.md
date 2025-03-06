# https://cloud.google.com/looker/docs/api-cors

Depth: 3

Looker uses [OAuth](https://en.wikipedia.org/wiki/OAuth) to let OAuth client applications authenticate into the Looker API without exposing client IDs and client secrets to the browser that is running the OAuth client application.

Web applications using OAuth must meet the following requirements:

  * Authentication using OAuth is available only with the [Looker API 4.0](/looker/docs/reference/looker-api/latest).
  * OAuth client applications must first be registered with Looker using the API before users of the application can authenticate into Looker.
  * Client applications must use HTTPS for all requests to the Looker API. Client applications that want to use the [`SubtleCrypto` APIs](https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto) provided by the browser must be HTTPS hosted.

## Looker API CORS support

The Looker API supports being called in browser and across origins using the [Cross-Origin Resource Sharing (CORS)](https://en.wikipedia.org/wiki/Cross-origin_resource_sharing) protocol. Looker CORS support has the following requirements:

  * Only origins listed in the [embedded domain allowlist](/looker/docs/admin-panel-platform-embed#embedded_domain_allowlist) can call the API using CORS.
  * Only access tokens obtained from OAuth, or from calling the `/login` API endpoint, can be used to make calls to the Looker API using CORS.

> The `/login` API endpoint cannot be called using CORS requests. Client applications wanting to call the Looker API using CORS requests must either use the OAuth login process described in Performing User Login Using OAuth, or retrieve a token from your application server or from non-CORS API calls.

## OAuth authentication overview

An overview of the OAuth authentication process is as follows:

  1. Register the OAuth client application with the Looker API.
  2. Add the origin of your OAuth client application to your [embedded domain allowlist](/looker/docs/admin-panel-platform-embed#embedded_domain_allowlist) for the code exchange API call and any subsequent CORS API calls.
  3. Redirect the browser URL to the `/auth` endpoint on the Looker UI hostname (not the Looker API hostname) when the OAuth client application attempts to authenticate a user. For example, `https://instance_name.looker.com`.
  4. If the user is successfully authenticated and logged in to Looker, Looker returns an OAuth redirect to the OAuth client application immediately. If the user is not already logged in to Looker on the device and browser, the Looker login screen is displayed and the user is prompted to log in to their Looker user account using their regular authentication protocol.
  5. Using the authorization code returned in the OAuth redirect, your OAuth client application should next make a call to the `/token` endpoint on the Looker API hostname, for example, `https://instance_name.looker.com:19999`. The API hostname might be the same as or different from the Looker UI hostname. The `/token` endpoint exists only on the Looker API host, and the `/auth` endpoint exists only on the Looker UI host.
  6. If the authorization code passed to the `/token` endpoint is valid, Looker returns an API `access_token` that is enabled for CORS API requests from the OAuth client application's domain.

## Registering an OAuth client application

Every OAuth client application that attempts to authenticate into the Looker API using OAuth must first be registered with the Looker instance before Looker will authorize access. To register an OAuth client application:

  1. Open the [API Explorer](/looker/docs/api-explorer) on your Looker instance.
  2. Using the version drop-down menu, choose the **4.0 - stable** version of the API.
  3. Under the **Auth** method, find the [`register_oauth_client_app()`](/looker/docs/reference/looker-api/latest/methods/Auth/register_oauth_client_app) API endpoint. You can also search for "oauth app" in the **Search** field. You can use `register_oauth_client_app()` to register your OAuth client application with Looker. Click the **Run It** button, and enter the parameters in the API Explorer and click **Run It** again to register the OAuth client application, or use the `register_oauth_client_app()` API endpoint programmatically. The required `register_oauth_client_app()` parameters are:

     * `client_guid`: A globally unique ID for the application
     * `redirect_uri`: The URI where the application will receive an OAuth redirect that includes an authorization code
     * `display_name`: The name of the application that is displayed to users of the application
     * `description`: A description of the application that is displayed to users on a disclosure and confirmation page when a user first logs in from the application

The values in the `client_guid` and `redirect_uri` parameters must match the values the OAuth client application will provide _exactly_ , or authentication will be denied.

## Performing user login using OAuth

  1. Navigate the user to the [`/auth`](/looker/docs/reference/looker-api/latest) endpoint on the UI host. For example:
    
        async function oauth_login() {
      const code_verifier = secure_random(32)
      const code_challenge = await sha256_hash(code_verifier)
      const params = {
        response_type: 'code',
        client_id: '123456',
        redirect_uri: 'https://mywebapp.com:3000/authenticated',
        scope: 'cors_api',
        state: '1235813',
        code_challenge_method: 'S256',
        code_challenge: code_challenge,
      }
      const url = `${base_url}?${new URLSearchParams(params).toString()}` // Replace base_url with your full Looker instance's UI host URL, plus the `/auth` endpoint.
      log(url)
    
      // Stash the code verifier we created in sessionStorage, which
      // will survive page loads caused by login redirects
      // The code verifier value is needed after the login redirect
      // to redeem the auth_code received for an access_token
      //
      sessionStorage.setItem('code_verifier', code_verifier)
    
      document.location = url
    }
    
    function array_to_hex(array) {
      return Array.from(array).map(b => b.toString(16).padStart(2,'0')).join('')
    }
    
    function secure_random(byte_count) {
      const array = new Uint8Array(byte_count);
      crypto.getRandomValues(array);
      return array_to_hex(array)
    }
    
    async function sha256_hash(message) {
      const msgUint8 = new TextEncoder().encode(message)
      const hashBuffer = await crypto.subtle.digest('SHA-256', msgUint8)
      return base64.urlEncode(hashBuffer))  // Refers to the implementation of base64.encode stored at https://gist.github.com/jhurliman/1250118
    }
    

**Tip:** The preceding sample code relies on [`SubtleCrypto` APIs](https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto) provided by the browser, but the browser will allow use of these functions only from secure (HTTPS) webpages.

Looker will attempt to authenticate the user using the [authentication](/looker/docs/admin-panel-authentication-pages) system for which the Looker instance is configured.

     * If the user is already logged in to Looker in the current browser (meaning there is a live login cookie state), the user won't be prompted to enter their login credentials.
     * If this is the first time this user has logged in using this OAuth client application, Looker will show a disclosure and confirmation page for the user to acknowledge and accept. The text from the `description` parameter used when the application was registered will be displayed. The description should indicate what the application intends to do with the user's Looker account. When the user clicks **accept** , the page will redirect to the application `redirect_uri`.
     * If the user is already logged in to Looker in the current browser and has already acknowledged the disclosure page, then the OAuth login is instantaneous with no visual interruption.
  2. The Looker API will return an OAuth redirect to the OAuth client application. Save the authorization code listed in the URI parameter. The following is an example OAuth redirect URI:
    
        https://mywebapp.com:3000/authenticated?&code=asdfasdfassdf&state=...
    

The authorization code is shown after `&code=` in the URI. In this example, the authorization code is `asdfasdfassdf`.

  3. Make a web request to the `/token` endpoint in the Looker API, passing the authorization code and your application information. For example:
    
        async function redeem_auth_code(response_str) {
      const params = new URLSearchParams(response_str)
      const auth_code = params.get('code')
    
      if (!auth_code) {
        log('ERROR: No authorization code in response')
        return
      }
      log(`auth code received: ${auth_code}`)
      log(`state: ${params.get('state')}`)
    
      const code_verifier = sessionStorage.getItem('code_verifier')
      if (!code_verifier) {
        log('ERROR: Missing code_verifier in session storage')
        return
      }
      sessionStorage.removeItem('code_verifier')
      const response = await
      fetch('https://mycompany.looker.com:19999/api/token', {  // This is the URL of your Looker instance's API web service
        method: 'POST',
        mode: 'cors',    // This line is required so that the browser will attempt a CORS request.
        body: stringify({
          grant_type: 'authorization_code',
          client_id: '123456',
          redirect_uri: 'https://mywebapp.com:3000/authenticated',
          code: auth_code,
          code_verifier: code_verifier,
        }),
        headers: {
          'x-looker-appid': 'Web App Auth & CORS API Demo', // This header is optional.
          'Content-Type': 'application/json;charset=UTF-8'  // This header is required.
        },
      }).catch((error) => {
        log(`Error: ${error.message}`)
      })
    
      const info = await response.json()
      log(`/api/token response: ${stringify(info)}`)
    
      // Store the access_token and other info,
      // which in this example is done in sessionStorage
    
      const expires_at = new Date(Date.now() + (info.expires_in * 1000))
      info.expires_at = expires_at
      log(`Access token expires at ${expires_at.toLocaleTimeString()} local time.`)
      sessionStorage.setItem('access_info', stringify(info))
      access_info = info
    }
    

A successful response will provide the OAuth client application with an API `access_token`. The response will also contain a `refresh_token`, which you can use later to get a new `access_token` without user interaction. A `refresh_token` has a one-month lifetime. Store the `refresh_token` securely.

All tokens in this system can be revoked by the Looker admin at any time.