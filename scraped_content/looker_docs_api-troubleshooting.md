# https://cloud.google.com/looker/docs/api-troubleshooting

Depth: 3

**Note:** As of Looker 22.4, the [Looker API 4.0 is generally available](/looker/docs/api-4-ga). In Looker 23.18, the [Looker API 3.1 has been removed](/looker/docs/api-3x-deprecation).

This page has troubleshooting procedures for the following problems that you may encounter with the Looker API:

  * API endpoint isn't reachable
  * API result is nonsensical text
  * API calls don't respond
  * Invalid encoding errors
  * Method Not Found errors
  * Bad Request (400) errors
  * Unauthorized (401) errors
  * Forbidden (403) errors
  * Not Found (404) errors
  * Method Not Allowed (405) errors
  * Conflict (409) errors
  * Validation (422) errors
  * Too Many Requests (429) errors
  * Internal Server Error (500) errors

## API endpoint isn't reachable

If you can't reach an API endpoint:

  * Verify your API credentials
  * Verify the API host URL
  * Verify the API port
  * Verify the API call URL

### Verify your API credentials

If your Looker API endpoint isn't reachable, first verify that your API credentials are correct. To view your API credentials:

  1. In Looker, access the [**Admin** panel](/looker/docs/navigating-looker#for_admins:_accessing_the_admin_panel) by selecting the **Admin** option in the [left navigation panel](/looker/docs/navigating-looker).
  2. In the left panel of the **Admin** page, scroll down and click [**Users**](/looker/docs/admin-panel-users-users).
  3. Search for your username in the user list, and click on it to edit your user page.
  4. Click on [**Edit API Keys**](/looker/docs/admin-panel-users-users#edit_api3_keys). You can see the **Client ID** , and you can click on the eye icon to view the **Client Secret** for each API key you have configured. Verify that your API credentials match the credentials you are using in your script.

### Verify the API URL

Another common problem in reaching an API endpoint is an incorrect API host URL. Most Looker instances use the default URL for the API. However, Looker installations using an alternate API path or Looker installations located behind a load balancer (for example, a cluster configuration) or any other proxy might not use the default URL. If this is the case, the API host URL must indicate the user-facing API hostname and port.

Looker admins can see the API host URL in the API admin settings (described in more detail on the [Admin settings - API](/looker/docs/admin-panel-platform-api) documentation page). To view the API host URL:

  1. Click the Looker **Main menu** icon menu, and select **Admin** to open the **Admin** panel.
  2. Click **API** in the **Admin** panel.
  3. View the **API Host URL**.

If the **API Host URL** field is blank, your Looker instance uses the default format, which is:
    
        https://<instance_name>.cloud.looker.com:<port>
    

To test the **API Host URL** :

  1. Open a browser, and then open the browser console.
  2. Enter your **API Host URL** followed by `/alive`. For example, if your **API Host URL** is `https://company.cloud.looker.com`, enter:
    
        https://company.cloud.looker.com/alive
    

If your **API Host URL** field is blank, use the default API URL. For example, for instances hosted on Google Cloud, Microsoft Azure, and instances hosted on Amazon Web Services (AWS) that were created on or after 07/07/2020, the default Looker API path uses port `443`:
    
        https://<instance_name>.cloud.looker.com:443/alive
    

For instances hosted on AWS that were created before 07/07/2020, the default Looker API path uses port 19999:
    
        https://<instance_name>.cloud.looker.com:19999/alive
    

If the API host URL is correct, this URL will result in a blank web page, not an error page.

You can also verify that you've reached the API by looking at the network response in your browser console. The network response should be `200`.

If these checks fail, the problem may be that you are calling the API incorrectly or that you have other errors in your code. Check your API calls and the code in your script. If those are correct, see the next section about verifying your port.

### Verify the API port

If the previous checks fail and you have a [customer-hosted Looker deployment](/looker/docs/managing-customer-hosted-deployment), it is possible that the API port needs to be opened on the network infrastructure.

The API port should forward to the Looker server. For customer-hosted Looker deployments, ask your network administrator to check the API port settings. The API port is most commonly `443` or `19999`. The API port should have the same configuration settings as the Looker instance port (`9999` by default). Your network administrator should verify that the following settings are the same for the API port as they are for your Looker instance port:

  * Proxies
  * Load balancers
  * Firewalls

### Verify the API call URL

Check that you are using the correct URL for your API call. The format of an API endpoint URL is:
    
    
    <API Host URL>/api/<API version>/<API call>
    

If you are using the default API host URL, the format of an API endpoint URL is:
    
    
    https://<instance_name>:<port>/api/<API version>/<API call>
    

You can get the URL format for API endpoints from the [API Explorer](/looker/docs/api-explorer) or from the [API Reference](/looker/docs/reference/looker-api/latest) documentation.

For example, the [API 4.0 Reference](/looker/docs/reference/looker-api/latest/methods/Query/all_running_queries) gives the following relative path for the Get All Running Queries endpoint:
    
    
    /api/4.0/running_queries
    

Therefore, the full API endpoint URL for the Get All Running Queries endpoint on the `docsexamples.dev.looker.com` Looker instance would be the following:
    
    
    https://docsexamples.dev.looker.com:443/api/4.0/running_queries
    

## API result is nonsensical text

If the API returns a response of garbled text, it is likely that you're seeing the binary content of a PDF, PNG, or JPG file. Some HTTP REST libraries assume that API responses will be text files and so other types of files are displayed as binary text.

In this case, you need to be sure that your HTTP REST library handles the API response as binary data, not as text. In some cases, this might mean setting a flag on the API call to tell the HTTP REST library that it's a binary result, or it might mean handling the result in a special way, like as a stream of bytes or as an array of bytes, instead of assigning the result to a string variable.

## API calls don't respond

If you are able to open the API Explorer but your API calls don't respond, verify that your Looker instance's **API Host URL** setting is set correctly. Looker admins can see the API host URL in Looker's API admin settings (described on the [Admin settings - API](/looker/docs/admin-panel-platform-api) documentation page).

## Invalid encoding errors

If you receive an encoding error when attempting to make an API call, you may need to set the proper `Content-Type` in your header during the request. HTTP protocol standards require that any POST, PUT, or PATCH request contain a `Content-Type` header. Since the Looker API uses JSON throughout, the `Content-Type` header should be set to `application/json`.

Note that using a [Looker SDK](/looker/docs/api-sdk) will automatically handle with this concern for you.

## Method Not Found errors

If you get a Method Not Found error, such as `method not found: all_looks()`, the first thing to check is your API version. There are several API calls that are new in API 4.0 or that were removed in API 4.0. See the [Looker API 4.0 Generally Available](/looker/docs/api-4-ga) announcement for the list of updates.

## Bad Request (400) errors

A `400 Bad Request` error indicates that the data provided in an API call is unrecognizable. The culprit is often broken or invalid JSON, perhaps a parse error. For the most part, 400 errors have already passed authentication, so the error response message will provide more specific information about the error.

## Unauthorized (401) errors

A `401 Unauthorized` error on an API call means that the API call is not properly authenticated. For more troubleshooting details, refer to the [How do I troubleshoot 401 errors?](https://www.googlecloudcommunity.com/gc/Technical-Tips-Tricks/How-do-I-troubleshoot-401-errors-on-Looker-API-calls/ta-p/751111) Community article.

## Forbidden (403) errors

The Looker API does not return 403 errors every time a user tries to access a LookML object or other content for which they don't have permission. Returning a 403 error instead of a 404 error could, in some cases, verify the existence of a particular Explore, dashboard, or LookML object when the owner may prefer that this not be known. To prevent this, Looker returns a 404 in these cases and the accompanying error in the Looker UI reads: "The page you requested could not be found. It either doesn't exist or you don't have permission to view it."

Depending on the environment in which your Looker instance is hosted, and the configuration of your Looker instance, the port number and associated URL where the API can be accessed may be different. When using an incorrect port number, you may see a 403 error. For example, if your Looker instance is configured with the default API port `443`, connecting to `https://mycompany.looker.com/api/4.0/login` — instead of `https://mycompany.looker.com:443/api/4.0/login` — will return a 403 error. For customer-hosted instances, you can read more about [Looker startup options](https://docs.looker.com/setup-and-management/on-prem-install/looker-startup-options) where you can define the API port.

This can also happen when you're using an out-of-date version of the Ruby SDK gem. Make sure to keep those gems updated. You can check at `https://rubygems.org/gems/looker-sdk`.

This can also happen when you don't include the `/api/<version number>/` portion of the URL. In this case, if a user attempts to connect to `https://mycompany.looker.com:443/login`, they'll see a 403 response.

## Not Found (404) errors

A `404 Not Found` error is the default error if anything goes wrong, usually with things like permissions. The response message for a 404 error provides minimal, if any, information. This is intentional, since 404 errors are shown to people with incorrect login credentials or insufficient permissions. Looker does not want to provide specific information in 404 response messages, since this information could be used to map out the "attack surface" of the Looker API.

If API login attempts are returning 404 errors, it's most likely because your API client ID or client secret isn't valid (see Verify your API credentials earlier on this page). The API login REST endpoint is the following:

  * `https://<your-looker-hostname>:<port>/api/4.0/login`

If you're using a Swagger codegen API or a Looker SDK, ensure that your `base_url` value is correct:

  * For a Swagger codegen client, the `base_url` should be the following:

    * `https://<your-looker-hostname>:<port>/api/4.0/`
  * For Looker SDK implementations that use a `looker.ini`, the value of `api_version` should be `4.0`, and the value of `base_url` should be the same as the URL of your Looker instance API in the format `https://<your-looker-hostname>:<port>`. An example `looker.ini` file follows:
    
        # api_version should be 4.0
    api_version=4.0
    base_url=https://<your-looker-hostname>:<port>
    

You can also get a 404 error after you log in. If you're logged in and you get a 404 error, that means you don't have permissions for the API command you just called.

## Method Not Allowed (405) errors

A `405 Method Not Allowed` error indicates that the server knows the request method but the target resource doesn't support this method.

The server must generate an `Allow` header field in a 405 status code response. The field must contain a list of methods that the target resource supports.

As an example, one way you might encounter this in Looker would be if you attempted to use the `update_dashboard()` endpoint to update metadata of a LookML dashboard. Changing the `id` parameter of a LookML dashboard is not supported through the Looker API, so a 405 error would occur.

## Conflict (409) errors

The `409 Conflict` response status code indicates a request conflict with the current state of the target resource.

Conflicts are most likely to occur in response to a PUT request. A common non-Looker example of this error occurs when uploading a file that is older than the existing one on the server, resulting in a version control conflict.

You might encounter this error in Looker when trying to check out a new git branch using the API, or when using endpoints like `create_group()` or `create_dashboard()`. In these cases, check to see if the object you are trying to create already exists.

## Validation (422) errors

Validation errors occur when something in the request failed the data checks performed. The request has one or more of the following types of errors (the error response will specify the exact errors):

  * Missing fields: There's a required parameter that was not provided (the error response will say which field is missing).
  * Invalid: The value provided doesn't match an existing value or the value is not in the correct format. For example, if you try to create a Look and the query ID you provide in the API call doesn't match an existing query you will get a validation error.
  * Already exists: The API call is attempting to create an object with an ID or name that is already present on your Looker instance. For example, database connection names must be unique. If you try to create a new database connection that uses the name of an existing connection, you will get a validation error with the code `already_exists`.

See the error response message for details on which fields may have been missing or required, or which fields may have invalid values. The response message will provide all of the validation errors at the same time. So if you have missing fields and also incorrect fields, the error response will list all of the problems with your API call.

Here is an example response:
    
    
    {
      "message": "Validation Failed",
      "errors": [
        {
        "field": "dialect",
        "code": "missing_field",
        "message": "This field is required.",
        "documentation_url": "http://docs.looker.com/"
        },
        {
        "field": "db_timezone",
        "code": "invalid",
        "message": "Must specify a database timezone when user timezones are activated.",
        "documentation_url": "http://docs.looker.com/"
        }
      ],
        ...
    

In this case, the API call was missing the required `dialect` field and also had an invalid value given in the `db_timezone`.

## Too Many Requests (429) errors

The `429 Too Many Requests` response status code indicates that the user has sent too many requests in a given amount of time ("rate limiting"). You can read more about Looker's rate limiting policies in the Looker Community post [Is there a limit to the number of API requests you can send at one time?](https://www.googlecloudcommunity.com/gc/Technical-Tips-Tricks/Is-there-a-limit-to-the-number-of-API-requests-you-can-send-at/ta-p/592612)

## Internal Server Error (500) errors

The `500 Internal Server Error` response code indicates that the server encountered an unexpected condition that prevented it from fulfilling the request.

This error response is a generic "catch-all" response. Usually, this indicates that the server cannot find a more specific 5xx error code to return in response. Any 500 response from Looker is unexpected, so, if you are seeing this error consistently while trying to interact with Looker, we recommend that you [open a support request](http://console.cloud.google.com/support/cases).