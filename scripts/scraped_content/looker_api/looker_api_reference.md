# Looker API Reference

## API Methods

### AuthApi

#### Acquire a cookieless embed session.  The acquire session endpoint negates the need for signing the embed url and passing it as a parameter to the embed login. This endpoint accepts an embed user definition and creates or updates it. This is similar behavior to the embed SSO login as they both can create and update embed user data.  The endpoint also accepts an optional `session_reference_token`. If present and the session has not expired and the credentials match the credentials for the embed session, a new authentication token will be generated. This allows the embed session to attach a new embedded IFRAME to the embed session. Note that the session is NOT extended in this scenario. In other words the session_length parameter is ignored.  **IMPORTANT:** If the `session_reference_token` is provided and the session has NOT expired, the embed user is NOT updated. This is done for performance reasons and to support the embed SSO usecase where the first IFRAME created on a page uses a signed url and subsequently created IFRAMEs do not.  If the `session_reference_token` is provided but the session has expired, the token will be ignored and a new embed session will be created. Note that the embed user definition will be updated in this scenario.  If the credentials do not match the credentials associated with an exisiting session_reference_token, a 404 will be returned.  The endpoint returns the following: - Authentication token - a token that is passed to `/embed/login` endpoint that creates or attaches to the   embed session. This token can be used once and has a lifetime of 30 seconds. - Session reference token - a token that lives for the length of the session. This token is used to   generate new api and navigation tokens OR create new embed IFRAMEs. - Api token - lives for 10 minutes. The Looker client will ask for this token once it is loaded into the   iframe. - Navigation token - lives for 10 minutes. The Looker client will ask for this token once it is loaded into   the iframe.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Activate an app for a user  Activates a user for a given oauth client app. This indicates the user has been informed that the app will have access to the user's looker data, and that the user has accepted and allowed the app to use their Looker account.  Activating a user for an app that the user is already activated with returns a success response.

#### Example

#### Parameters

**user_id** | **string**| The id of the user to enable use of this app |
 **fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Add Support Access Allowlist Users  Adds a list of emails to the Allowlist, using the provided reason

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### List All OAuth Client Apps  Lists all applications registered to use OAuth2 login with this Looker instance, including enabled and disabled apps.  Results are filtered to include only the apps that the caller (current user) has permission to see.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get currently locked-out users.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Create an embed secret using the specified information.  The value of the `secret` field will be set by Looker and returned.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Create an Embed URL  Creates an embed URL that runs as the Looker user making this API call. (\"Embed as me\") This embed URL can then be used to instantiate a Looker embed session in a \"Powered by Looker\" (PBL) web application.  This is similar to Private Embedding (https://cloud.google.com/looker/docs/r/admin/embed/private-embed). Instead of of logging into the Web UI to authenticate, the user has already authenticated against the API to be able to make this call. However, unlike Private Embed where the user has access to any other part of the Looker UI, the embed web session created by requesting the EmbedUrlResponse.url in a browser only has access to content visible under the `/embed` context.  An embed URL can only be used once, and must be used within 5 minutes of being created. After it has been used to request a page from the Looker server, the URL is invalid. Future requests using the same URL will fail. This is to prevent 'replay attacks'.  The `target_url` property must be a complete URL of a Looker Embedded UI page - scheme, hostname, path starting with \"/embed\" and query params. To load a dashboard with id 56 and with a filter of `Date=1 years`, the looker Embed URL would look like `https://myname.looker.com/embed/dashboards/56?Date=1%20years`. The best way to obtain this target_url is to navigate to the desired Looker page in your web browser, copy the URL shown in the browser address bar, insert \"/embed\" after the host/port, and paste it into the `target_url` property as a quoted string value in this API request.  #### Security Note Protect this embed URL as you would an access token or password credentials - do not write it to disk, do not pass it to a third party, and only pass it through a secure HTTPS encrypted transport.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Create a OIDC test configuration.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Create a SAML test configuration.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Create SSO Embed URL  Creates an SSO embed URL and cryptographically signs it with an embed secret. This signed URL can then be used to instantiate a Looker embed session in a PBL web application. Do not make any modifications to this URL - any change may invalidate the signature and cause the URL to fail to load a Looker embed session.  A signed SSO embed URL can only be used once. After it has been used to request a page from the Looker server, the URL is invalid. Future requests using the same URL will fail. This is to prevent 'replay attacks'.  The `target_url` property must be a complete URL of a Looker UI page - scheme, hostname, path and query params. To load a dashboard with id 56 and with a filter of `Date=1 years`, the looker URL would look like `https:/myname.looker.com/dashboards/56?Date=1%20years`. The best way to obtain this target_url is to navigate to the desired Looker page in your web browser, copy the URL shown in the browser address bar and paste it into the `target_url` property as a quoted string value in this API request.  Permissions for the embed user are defined by the groups in which the embed user is a member (group_ids property) and the lists of models and permissions assigned to the embed user. At a minimum, you must provide values for either the group_ids property, or both the models and permissions properties. These properties are additive; an embed user can be a member of certain groups AND be granted access to models and permissions.  The embed user's access is the union of permissions granted by the group_ids, models, and permissions properties.  This function does not strictly require all group_ids, user attribute names, or model names to exist at the moment the SSO embed url is created. Unknown group_id, user attribute names or model names will be passed through to the output URL. To diagnose potential problems with an SSO embed URL, you can copy the signed URL into the Embed URI Validator text box in `<your looker instance>/admin/embed`.  The `secret_id` parameter is optional. If specified, its value must be the id of an active secret defined in the Looker instance. if not specified, the URL will be signed using the newest active secret defined in the Looker instance.  #### Security Note Protect this signed URL as you would an access token or password credentials - do not write it to disk, do not pass it to a third party, and only pass it through a secure HTTPS encrypted transport.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Deactivate an app for a user  Deactivate a user for a given oauth client app. All tokens issued to the app for this user will be invalid immediately. Before the user can use the app with their Looker account, the user will have to read and accept an account use disclosure statement for the app.  Admin users can deactivate other users, but non-admin users can only deactivate themselves.  As with most REST DELETE operations, this endpoint does not return an error if the indicated resource (app or user) does not exist or has already been deactivated.

#### Example

#### Parameters

**user_id** | **string**| The id of the user to enable use of this app |
 **fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Delete cookieless embed session  This will delete the session associated with the given session reference token. Calling this endpoint will result in the session and session reference data being cleared from the system. This endpoint can be used to log an embed user out of the Looker instance.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Delete an embed secret.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Delete OAuth Client App  Deletes the registration info of the app with the matching client_guid. All active sessions and tokens issued for this app will immediately become invalid.  As with most REST DELETE operations, this endpoint does not return an error if the indicated resource does not exist.  ### Note: this deletion cannot be undone.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Delete a OIDC test configuration.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Delete a SAML test configuration.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Delete Support Access Allowlist User  Deletes the specified Allowlist Entry Id

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Removes login lockout for the associated user.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Deregister a mobile device.

#### Example

#### Parameters

#

#### Return type

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Disable Support Access  Disables Support Access immediately

#### Example

#### Parameters

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Enable Support Access  Enables Support Access for the provided duration

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Fetch the given url and parse it as a SAML IdP metadata document and return the result. Note that this requires that the url be public or at least at a location where the Looker instance can fetch it without requiring any special authentication.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Force all credentials_email users to reset their login passwords upon their next login.

#### Example

#### Parameters

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Generate api and navigation tokens for a cookieless embed session  The generate tokens endpoint is used to create new tokens of type: - Api token. - Navigation token. The generate tokens endpoint should be called every time the Looker client asks for a token (except for the first time when the tokens returned by the acquire_session endpoint should be used).

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get Support Access Allowlist Users  Returns the users that have been added to the Support Access Allowlist

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Invalidate All Issued Tokens  Immediately invalidates all auth codes, sessions, access tokens and refresh tokens issued for this app for ALL USERS of this app.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get the LDAP configuration.  Looker can be optionally configured to authenticate users against an Active Directory or other LDAP directory server. LDAP setup requires coordination with an administrator of that directory server.  Only Looker administrators can read and update the LDAP configuration.  Configuring LDAP impacts authentication for all users. This configuration should be done carefully.  Looker maintains a single LDAP configuration. It can be read and updated.       Updates only succeed if the new state will be valid (in the sense that all required fields are populated);       it is up to you to ensure that the configuration is appropriate and correct).  LDAP is enabled or disabled for Looker using the **enabled** field.  Looker will never return an **auth_password** field. That value can be set, but never retrieved.  See the [Looker LDAP docs](https://cloud.google.com/looker/docs/r/api/ldap_setup) for additional information.

#### Example

#### Parameters

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get Oauth Client App  Returns the registered app client with matching client_guid.

#### Example

#### Parameters

**fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get the OIDC configuration.  Looker can be optionally configured to authenticate users against an OpenID Connect (OIDC) authentication server. OIDC setup requires coordination with an administrator of that server.  Only Looker administrators can read and update the OIDC configuration.  Configuring OIDC impacts authentication for all users. This configuration should be done carefully.  Looker maintains a single OIDC configuation. It can be read and updated.       Updates only succeed if the new state will be valid (in the sense that all required fields are populated);       it is up to you to ensure that the configuration is appropriate and correct).  OIDC is enabled or disabled for Looker using the **enabled** field.

#### Example

#### Parameters

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get a OIDC test configuration by test_slug.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Parse the given xml as a SAML IdP metadata document and return the result.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get password config.

#### Example

#### Parameters

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Registers a mobile device. # Required fields: [:device_token, :device_type]

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Register an OAuth2 Client App  Registers details identifying an external web app or native app as an OAuth2 login client of the Looker instance. The app registration must provide a unique client_guid and redirect_uri that the app will present in OAuth login requests. If the client_guid and redirect_uri parameters in the login request do not match the app details registered with the Looker instance, the request is assumed to be a forgery and is rejected.

#### Example

#### Parameters

**body** | [**\Swagger\Client\Model\OauthClientApp**](../Model/OauthClientApp.md)| OAuth Client App |
 **fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get the SAML configuration.  Looker can be optionally configured to authenticate users against a SAML authentication server. SAML setup requires coordination with an administrator of that server.  Only Looker administrators can read and update the SAML configuration.  Configuring SAML impacts authentication for all users. This configuration should be done carefully.  Looker maintains a single SAML configuation. It can be read and updated.       Updates only succeed if the new state will be valid (in the sense that all required fields are populated);       it is up to you to ensure that the configuration is appropriate and correct).  SAML is enabled or disabled for Looker using the **enabled** field.

#### Example

#### Parameters

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get a SAML test configuration by test_slug.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Search currently locked-out users.

#### Example

#### Parameters

**page** | **int**| DEPRECATED. Use limit and offset instead. Return only page N of paginated results | [optional]
 **per_page** | **int**| DEPRECATED. Use limit and offset instead. Return N rows of data per page | [optional]
 **limit** | **int**| Number of results to return. (used with offset and takes priority over page and per_page) | [optional]
 **offset** | **int**| Number of results to skip before returning any. (used with limit and takes priority over page and per_page) | [optional]
 **sorts** | **string**| Fields to sort by. | [optional]
 **auth_type** | **string**| Auth type user is locked out for (email, ldap, totp, api) | [optional]
 **full_name** | **string**| Match name | [optional]
 **email** | **string**| Match email | [optional]
 **remote_id** | **string**| Match remote LDAP ID | [optional]
 **filter_or** | **bool**| Combine given search criteria in a boolean OR expression | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get session config.

#### Example

#### Parameters

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Support Access Status  Returns the current Support Access Status

#### Example

#### Parameters

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Test the connection authentication settings for an LDAP configuration.  This tests that the connection is possible and that a 'server' account to be used by Looker can       authenticate to the LDAP server given connection and authentication information.  **connection_host**, **connection_port**, and **auth_username**, are required.       **connection_tls** and **auth_password** are optional.  Example: ```json {   \"connection_host\": \"ldap.example.com\",   \"connection_port\": \"636\",   \"connection_tls\": true,   \"auth_username\": \"cn=looker,dc=example,dc=com\",   \"auth_password\": \"secret\" } ```  Looker will never return an **auth_password**. If this request omits the **auth_password** field, then       the **auth_password** value from the active config (if present) will be used for the test.  The active LDAP settings are not modified.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Test the connection settings for an LDAP configuration.  This tests that the connection is possible given a connection_host and connection_port.  **connection_host** and **connection_port** are required. **connection_tls** is optional.  Example: ```json {   \"connection_host\": \"ldap.example.com\",   \"connection_port\": \"636\",   \"connection_tls\": true } ```  No authentication to the LDAP server is attempted.  The active LDAP settings are not modified.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Test the user authentication settings for an LDAP configuration.  This test accepts a full LDAP configuration along with a username/password pair and attempts to       authenticate the user with the LDAP server. The configuration is validated before attempting the       authentication.  Looker will never return an **auth_password**. If this request omits the **auth_password** field, then       the **auth_password** value from the active config (if present) will be used for the test.  **test_ldap_user** and **test_ldap_password** are required.  The active LDAP settings are not modified.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Test the user authentication settings for an LDAP configuration without authenticating the user.  This test will let you easily test the mapping for user properties and roles for any user without      needing to authenticate as that user.  This test accepts a full LDAP configuration along with a username and attempts to find the full info      for the user from the LDAP server without actually authenticating the user. So, user password is not      required.The configuration is validated before attempting to contact the server.  **test_ldap_user** is required.  The active LDAP settings are not modified.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Update the LDAP configuration.  Configuring LDAP impacts authentication for all users. This configuration should be done carefully.  Only Looker administrators can read and update the LDAP configuration.  LDAP is enabled or disabled for Looker using the **enabled** field.  It is **highly** recommended that any LDAP setting changes be tested using the APIs below before being set globally.  See the [Looker LDAP docs](https://cloud.google.com/looker/docs/r/api/ldap_setup) for additional information.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Updates the mobile device registration

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Update OAuth2 Client App Details  Modifies the details a previously registered OAuth2 login client app.

#### Example

#### Parameters

**body** | [**\Swagger\Client\Model\OauthClientApp**](../Model/OauthClientApp.md)| OAuth Client App |
 **fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Update the OIDC configuration.  Configuring OIDC impacts authentication for all users. This configuration should be done carefully.  Only Looker administrators can read and update the OIDC configuration.  OIDC is enabled or disabled for Looker using the **enabled** field.  It is **highly** recommended that any OIDC setting changes be tested using the APIs below before being set globally.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Update password config.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Update the SAML configuration.  Configuring SAML impacts authentication for all users. This configuration should be done carefully.  Only Looker administrators can read and update the SAML configuration.  SAML is enabled or disabled for Looker using the **enabled** field.  It is **highly** recommended that any SAML setting changes be tested using the APIs below before being set globally.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Update session config.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

### DataActionApi

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

### UserApi

#### API login information for the specified user. This is for the newer API keys that can be added for any user.

#### Example

#### Parameters

**fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Embed login information for the specified user.

#### Example

#### Parameters

**fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Web login session for the specified user.

#### Example

#### Parameters

**fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get information about all users.

#### Example

#### Parameters

**page** | **int**| DEPRECATED. Use limit and offset instead. Return only page N of paginated results | [optional]
 **per_page** | **int**| DEPRECATED. Use limit and offset instead. Return N rows of data per page | [optional]
 **limit** | **int**| Number of results to return. (used with offset and takes priority over page and per_page) | [optional]
 **offset** | **int**| Number of results to skip before returning any. (used with limit and takes priority over page and per_page) | [optional]
 **sorts** | **string**| Fields to sort by. | [optional]
 **ids** | [**string[]**](../Model/string.md)| Optional list of ids to get specific users. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Create a user with the specified information.

#### Example

#### Parameters

**fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### API login information for the specified user. This is for the newer API keys that can be added for any user.

#### Example

#### Parameters

**fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Email/password login information for the specified user.

#### Example

#### Parameters

**body** | [**\Swagger\Client\Model\CredentialsEmail**](../Model/CredentialsEmail.md)| Email/Password Credential |
 **fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Create a password reset token. This will create a cryptographically secure random password reset token for the user. If the user already has a password reset token then this invalidates the old token and creates a new one. The token is expressed as the 'password_reset_url' of the user's email/password credential object. This takes an optional 'expires' param to indicate if the new token should be an expiring token. Tokens that expire are typically used for self-service password resets for existing users. Invitation emails for new users typically are not set to expire. The expire period is always 60 minutes when expires is enabled. This method can be called with an empty body.

#### Example

#### Parameters

**expires** | **bool**| Expiring token. | [optional]
 **fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Two-factor login information for the specified user.

#### Example

#### Parameters

**body** | [**\Swagger\Client\Model\CredentialsTotp**](../Model/CredentialsTotp.md)| Two-Factor Credential | [optional]
 **fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Delete the user with a specific id.  **DANGER** this will delete the user and all looks and other information owned by the user.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Delete a user attribute value from a user's account settings.  After the user attribute value is deleted from the user's account settings, subsequent requests for the user attribute value for this user will draw from the user's groups or the default value of the user attribute. See [Get User Attribute Values](#!/User/user_attribute_user_values) for more information about how user attribute values are resolved.

#### Example

#### Parameters

**user_attribute_id** | **string**| Id of user attribute |

#### Return type

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### API login information for the specified user. This is for the newer API keys that can be added for any user.

#### Example

#### Parameters

**credentials_api3_id** | **string**| Id of API Credential |

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Email/password login information for the specified user.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Embed login information for the specified user.

#### Example

#### Parameters

**credentials_embed_id** | **string**| Id of Embedding Credential |

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Google authentication login information for the specified user.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### LDAP login information for the specified user.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Looker Openid login information for the specified user. Used by Looker Analysts.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### OpenID Connect (OIDC) authentication login information for the specified user.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Saml authentication login information for the specified user.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Two-factor login information for the specified user.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Web login session for the specified user.

#### Example

#### Parameters

**session_id** | **string**| Id of Web Login Session |

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get information about the current user; i.e. the user account currently calling the API.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Search email credentials  Returns all credentials_email records that match the given search criteria.  If multiple search params are given and `filter_or` is FALSE or not specified, search params are combined in a logical AND operation. Only rows that match *all* search param criteria will be returned.  If `filter_or` is TRUE, multiple search params are combined in a logical OR operation. Results will include rows that match **any** of the search criteria.  String search params use case-insensitive matching. String search params can contain `%` and '_' as SQL LIKE pattern match wildcard expressions. example=\"dan%\" will match \"danger\" and \"Danzig\" but not \"David\" example=\"D_m%\" will match \"Damage\" and \"dump\"  Integer search params can accept a single value or a comma separated list of values. The multiple values will be combined under a logical OR operation - results will match at least one of the given values.  Most search params can accept \"IS NULL\" and \"NOT NULL\" as special expressions to match or exclude (respectively) rows where the column is null.  Boolean search params accept only \"true\" and \"false\" as values.

#### Example

#### Parameters

**limit** | **int**| Number of results to return (used with &#x60;offset&#x60;). | [optional]
 **offset** | **int**| Number of results to skip before returning any (used with &#x60;limit&#x60;). | [optional]
 **sorts** | **string**| Fields to sort by. | [optional]
 **id** | **string**| Match credentials_email id. | [optional]
 **email** | **string**| Match credentials_email email. | [optional]
 **emails** | **string**| Find credentials_email that match given emails. | [optional]
 **filter_or** | **bool**| Combine given search criteria in a boolean OR expression. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Search users  Returns all<sup>*</sup> user records that match the given search criteria.  If multiple search params are given and `filter_or` is FALSE or not specified, search params are combined in a logical AND operation. Only rows that match *all* search param criteria will be returned.  If `filter_or` is TRUE, multiple search params are combined in a logical OR operation. Results will include rows that match **any** of the search criteria.  String search params use case-insensitive matching. String search params can contain `%` and '_' as SQL LIKE pattern match wildcard expressions. example=\"dan%\" will match \"danger\" and \"Danzig\" but not \"David\" example=\"D_m%\" will match \"Damage\" and \"dump\"  Integer search params can accept a single value or a comma separated list of values. The multiple values will be combined under a logical OR operation - results will match at least one of the given values.  Most search params can accept \"IS NULL\" and \"NOT NULL\" as special expressions to match or exclude (respectively) rows where the column is null.  Boolean search params accept only \"true\" and \"false\" as values.   (<sup>*</sup>) Results are always filtered to the level of information the caller is permitted to view. Looker admins can see all user details; normal users in an open system can see names of other users but no details; normal users in a closed system can only see names of other users who are members of the same group as the user.

#### Example

#### Parameters

**page** | **int**| DEPRECATED. Use limit and offset instead. Return only page N of paginated results | [optional]
 **per_page** | **int**| DEPRECATED. Use limit and offset instead. Return N rows of data per page | [optional]
 **limit** | **int**| Number of results to return. (used with offset and takes priority over page and per_page) | [optional]
 **offset** | **int**| Number of results to skip before returning any. (used with limit and takes priority over page and per_page) | [optional]
 **sorts** | **string**| Fields to sort by. | [optional]
 **id** | **string**| Match User Id. | [optional]
 **first_name** | **string**| Match First name. | [optional]
 **last_name** | **string**| Match Last name. | [optional]
 **verified_looker_employee** | **bool**| Search for user accounts associated with Looker employees | [optional]
 **embed_user** | **bool**| Search for only embed users | [optional]
 **email** | **string**| Search for the user with this email address | [optional]
 **is_disabled** | **bool**| Search for disabled user accounts | [optional]
 **filter_or** | **bool**| Combine given search criteria in a boolean OR expression | [optional]
 **content_metadata_id** | **string**| Search for users who have access to this content_metadata item | [optional]
 **group_id** | **string**| Search for users who are direct members of this group | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Search for user accounts by name  Returns all user accounts where `first_name` OR `last_name` OR `email` field values match a pattern. The pattern can contain `%` and `_` wildcards as in SQL LIKE expressions.  Any additional search params will be combined into a logical AND expression.

#### Example

#### Parameters

**fields** | **string**| Include only these fields in the response | [optional]
 **page** | **int**| DEPRECATED. Use limit and offset instead. Return only page N of paginated results | [optional]
 **per_page** | **int**| DEPRECATED. Use limit and offset instead. Return N rows of data per page | [optional]
 **limit** | **int**| Number of results to return. (used with offset and takes priority over page and per_page) | [optional]
 **offset** | **int**| Number of results to skip before returning any. (used with limit and takes priority over page and per_page) | [optional]
 **sorts** | **string**| Fields to sort by | [optional]
 **id** | **string**| Match User Id | [optional]
 **first_name** | **string**| Match First name | [optional]
 **last_name** | **string**| Match Last name | [optional]
 **verified_looker_employee** | **bool**| Match Verified Looker employee | [optional]
 **email** | **string**| Match Email Address | [optional]
 **is_disabled** | **bool**| Include or exclude disabled accounts in the results | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Send a password reset token. This will send a password reset email to the user. If a password reset token does not already exist for this user, it will create one and then send it. If the user has not yet set up their account, it will send a setup email to the user. The URL sent in the email is expressed as the 'password_reset_url' of the user's email/password credential object. Password reset URLs will expire in 60 minutes. This method can be called with an empty body.

#### Example

#### Parameters

**fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Store a custom value for a user attribute in a user's account settings.  Per-user user attribute values take precedence over group or default values.

#### Example

#### Parameters

**user_attribute_id** | **string**| Id of user attribute |
 **body** | [**\Swagger\Client\Model\UserAttributeWithValue**](../Model/UserAttributeWithValue.md)| New attribute value for user. |

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Set roles of the user with a specific id.

#### Example

#### Parameters

**body** | **string[]**| array of roles ids for user |
 **fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Update information about the user with a specific id.

#### Example

#### Parameters

**body** | [**\Swagger\Client\Model\User**](../Model/User.md)| User |
 **fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Email/password login information for the specified user.

#### Example

#### Parameters

**body** | [**\Swagger\Client\Model\CredentialsEmail**](../Model/CredentialsEmail.md)| Email/Password Credential |
 **fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get information about the user with a specific id.  If the caller is an admin or the caller is the user being specified, then full user information will be returned. Otherwise, a minimal 'public' variant of the user information will be returned. This contains The user name and avatar url, but no sensitive information.

#### Example

#### Parameters

**fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get user attribute values for a given user.  Returns the values of specified user attributes (or all user attributes) for a certain user.  A value for each user attribute is searched for in the following locations, in this order:  1. in the user's account information 1. in groups that the user is a member of 1. the default value of the user attribute  If more than one group has a value defined for a user attribute, the group with the lowest rank wins.  The response will only include user attributes for which values were found. Use `include_unset=true` to include empty records for user attributes with no value.  The value of all hidden user attributes will be blank.

#### Example

#### Parameters

**fields** | **string**| Requested fields. | [optional]
 **user_attribute_ids** | [**string[]**](../Model/string.md)| Specific user attributes to request. Omit or leave blank to request all user attributes. | [optional]
 **all_values** | **bool**| If true, returns all values in the search path instead of just the first value found. Useful for debugging group precedence. | [optional]
 **include_unset** | **bool**| If true, returns an empty record for each requested attribute that has no user, group, or default value. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### API login information for the specified user. This is for the newer API keys that can be added for any user.

#### Example

#### Parameters

**credentials_api3_id** | **string**| Id of API Credential |
 **fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Email/password login information for the specified user.

#### Example

#### Parameters

**fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Embed login information for the specified user.

#### Example

#### Parameters

**credentials_embed_id** | **string**| Id of Embedding Credential |
 **fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Google authentication login information for the specified user.

#### Example

#### Parameters

**fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### LDAP login information for the specified user.

#### Example

#### Parameters

**fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Looker Openid login information for the specified user. Used by Looker Analysts.

#### Example

#### Parameters

**fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### OpenID Connect (OIDC) authentication login information for the specified user.

#### Example

#### Parameters

**fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Saml authentication login information for the specified user.

#### Example

#### Parameters

**fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Two-factor login information for the specified user.

#### Example

#### Parameters

**fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get information about the user with a credential of given type with specific id.  This is used to do things like find users by their embed external_user_id. Or, find the user with a given api3 client_id, etc. The 'credential_type' matches the 'type' name of the various credential types. It must be one of the values listed in the table below. The 'credential_id' is your unique Id for the user and is specific to each type of credential.  An example using the Ruby sdk might look like:  `sdk.user_for_credential('embed', 'customer-4959425')`  This table shows the supported 'Credential Type' strings. The right column is for reference; it shows which field in the given credential type is actually searched when finding a user with the supplied 'credential_id'.  | Credential Types | Id Field Matched | | ---------------- | ---------------- | | email            | email            | | google           | google_user_id   | | saml             | saml_user_id     | | oidc             | oidc_user_id     | | ldap             | ldap_id          | | api              | token            | | api3             | client_id        | | embed            | external_user_id | | looker_openid    | email            |  **NOTE**: The 'api' credential type was only used with the legacy Looker query API and is no longer supported. The credential type for API you are currently looking at is 'api3'.

#### Example

#### Parameters

**credential_id** | **string**| Id of credential |
 **fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get information about roles of a given user

#### Example

#### Parameters

**fields** | **string**| Requested fields. | [optional]
 **direct_association_only** | **bool**| Get only roles associated directly with the user: exclude those only associated through groups. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Web login session for the specified user.

#### Example

#### Parameters

**session_id** | **string**| Id of Web Login Session |
 **fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Change a disabled user's email addresses  Allows the admin to change the email addresses for all the user's associated credentials.  Will overwrite all associated email addresses with the value supplied in the 'email' body param. The user's 'is_disabled' status must be true.

#### Example

#### Parameters

**body** | [**\Swagger\Client\Model\UserEmailOnly**](../Model/UserEmailOnly.md)| null |
 **fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

### IntegrationApi

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get information about all Integration Hubs.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get information about all Integrations.

#### Example

#### Parameters

**integration_hub_id** | **string**| Filter to a specific provider | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Create a new Integration Hub.  This API is rate limited to prevent it from being used for SSRF attacks

#### Example

#### Parameters

**fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Delete a Integration Hub.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Example

#### Parameters

**body** | **object**| Integration Form Request | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get information about a Integration.

#### Example

#### Parameters

**fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get information about a Integration Hub.

#### Example

#### Parameters

**fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Update parameters on a Integration.

#### Example

#### Parameters

**body** | [**\Swagger\Client\Model\Integration**](../Model/Integration.md)| Integration |
 **fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Update a Integration Hub definition.  This API is rate limited to prevent it from being used for SSRF attacks

#### Example

#### Parameters

**body** | [**\Swagger\Client\Model\IntegrationHub**](../Model/IntegrationHub.md)| Integration Hub |
 **fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

### FolderApi

#### Get information about all folders.  In API 3.x, this will not return empty personal folders, unless they belong to the calling user, or if they contain soft-deleted content.  In API 4.0+, all personal folders will be returned.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Create a folder with specified information.  Caller must have permission to edit the parent folder and to create folders, otherwise the request returns 404 Not Found.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Delete the folder with a specific id including any children folders. **DANGER** this will delete all looks and dashboards in the folder.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get information about the folder with a specific id.

#### Example

#### Parameters

**fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get the ancestors of a folder

#### Example

#### Parameters

**fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get the children of a folder.

#### Example

#### Parameters

**fields** | **string**| Requested fields. | [optional]
 **page** | **int**| DEPRECATED. Use limit and offset instead. Return only page N of paginated results | [optional]
 **per_page** | **int**| DEPRECATED. Use limit and offset instead. Return N rows of data per page | [optional]
 **limit** | **int**| Number of results to return. (used with offset and takes priority over page and per_page) | [optional]
 **offset** | **int**| Number of results to skip before returning any. (used with limit and takes priority over page and per_page) | [optional]
 **sorts** | **string**| Fields to sort by. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Search the children of a folder

#### Example

#### Parameters

**fields** | **string**| Requested fields. | [optional]
 **sorts** | **string**| Fields to sort by. | [optional]
 **name** | **string**| Match folder name. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get the dashboards in a folder

#### Example

#### Parameters

**fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get all looks in a folder. In API 3.x, this will return all looks in a folder, including looks in the trash. In API 4.0+, all looks in a folder will be returned, excluding looks in the trash.

#### Example

#### Parameters

**fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get the parent of a folder

#### Example

#### Parameters

**fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Example

#### Parameters

**page** | **int**| DEPRECATED. Use limit and offset instead. Return only page N of paginated results | [optional]
 **per_page** | **int**| DEPRECATED. Use limit and offset instead. Return N rows of data per page | [optional]
 **limit** | **int**| Number of results to return. (used with offset and takes priority over page and per_page) | [optional]
 **offset** | **int**| Number of results to skip before returning any. (used with limit and takes priority over page and per_page) | [optional]
 **sorts** | **string**| Fields to sort by. | [optional]
 **name** | **string**| Match Space title. | [optional]
 **id** | **string**| Match Space id | [optional]
 **parent_id** | **string**| Filter on a children of a particular folder. | [optional]
 **creator_id** | **string**| Filter on folder created by a particular user. | [optional]
 **filter_or** | **bool**| Combine given search criteria in a boolean OR expression | [optional]
 **is_shared_root** | **bool**| Match is shared root | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Update the folder with a specific id.

#### Example

#### Parameters

**body** | [**\Swagger\Client\Model\UpdateFolder**](../Model/UpdateFolder.md)| Folder parameters |

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

### DashboardApi

#### Get information about all active dashboards.  Returns an array of **abbreviated dashboard objects**. Dashboards marked as deleted are excluded from this list.  Get the **full details** of a specific dashboard by id with [dashboard()](#!/Dashboard/dashboard)  Find **deleted dashboards** with [search_dashboards()](#!/Dashboard/search_dashboards)

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Copy an existing dashboard  Creates a copy of an existing dashboard, in a specified folder, and returns the copied dashboard.  `dashboard_id` is required, `dashboard_id` and `folder_id` must already exist if specified. `folder_id` will default to the existing folder.  If a dashboard with the same title already exists in the target folder, the copy will have '(copy)'   or '(copy <# of copies>)' appended.

#### Example

#### Parameters

**folder_id** | **string**| Folder id to copy to. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Create a new dashboard  Creates a new dashboard object and returns the details of the newly created dashboard.  `Title` and `space_id` are required fields. `Space_id` must contain the id of an existing space. A dashboard's `title` must be unique within the space in which it resides.  If you receive a 422 error response when creating a dashboard, be sure to look at the response body for information about exactly which fields are missing or contain invalid data.  You can **update** an existing dashboard with [update_dashboard()](#!/Dashboard/update_dashboard)  You can **permanently delete** an existing dashboard with [delete_dashboard()](#!/Dashboard/delete_dashboard)

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Create a dashboard element on the dashboard with a specific id.

#### Example

#### Parameters

**fields** | **string**| Requested fields. | [optional]
 **apply_filters** | **bool**| Apply relevant filters on dashboard to this tile | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Create a dashboard filter on the dashboard with a specific id.

#### Example

#### Parameters

**fields** | **string**| Requested fields | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Create a dashboard layout on the dashboard with a specific id.

#### Example

#### Parameters

**fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get information about a dashboard  Returns the full details of the identified dashboard object  Get a **summary list** of all active dashboards with [all_dashboards()](#!/Dashboard/all_dashboards)  You can **Search** for dashboards with [search_dashboards()](#!/Dashboard/search_dashboards)

#### Example

#### Parameters

**fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get Aggregate Table LookML for Each Query on a Dahboard  Returns a JSON object that contains the dashboard id and Aggregate Table lookml

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get information about all the dashboard elements on a dashboard with a specific id.

#### Example

#### Parameters

**fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get information about all the dashboard filters on a dashboard with a specific id.

#### Example

#### Parameters

**fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get information about all the dashboard elements on a dashboard with a specific id.

#### Example

#### Parameters

**fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get information about the dashboard element with a specific id.

#### Example

#### Parameters

**fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get information about the dashboard filters with a specific id.

#### Example

#### Parameters

**fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get information about the dashboard layouts with a specific id.

#### Example

#### Parameters

**fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get information about the dashboard elements with a specific id.

#### Example

#### Parameters

**fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get information about all the dashboard layout components for a dashboard layout with a specific id.

#### Example

#### Parameters

**fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get lookml of a UDD  Returns a JSON object that contains the dashboard id and the full lookml

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Delete the dashboard with the specified id  Permanently **deletes** a dashboard. (The dashboard cannot be recovered after this operation.)  \"Soft\" delete or hide a dashboard by setting its `deleted` status to `True` with [update_dashboard()](#!/Dashboard/update_dashboard).  Note: When a dashboard is deleted in the UI, it is soft deleted. Use this API call to permanently remove it, if desired.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Delete a dashboard element with a specific id.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Delete a dashboard filter with a specific id.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Delete a dashboard layout with a specific id.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Creates a dashboard object based on LookML Dashboard YAML, and returns the details of the newly created dashboard.  If a dashboard exists with the YAML-defined \"preferred_slug\", the new dashboard will overwrite it. Otherwise, a new dashboard will be created. Note that when a dashboard is overwritten, alerts will not be maintained.  If a folder_id is specified: new dashboards will be placed in that folder, and overwritten dashboards will be moved to it If the folder_id isn't specified: new dashboards will be placed in the caller's personal folder, and overwritten dashboards will remain where they were  LookML must contain valid LookML YAML code. It's recommended to use the LookML format returned from [dashboard_lookml()](#!/Dashboard/dashboard_lookml) as the input LookML (newlines replaced with  ).  Note that the created dashboard is not linked to any LookML Dashboard, i.e. [sync_lookml_dashboard()](#!/Dashboard/sync_lookml_dashboard) will not update dashboards created by this method.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Import a LookML dashboard to a space as a UDD Creates a UDD (a dashboard which exists in the Looker database rather than as a LookML file) from the LookML dashboard and places it in the space specified. The created UDD will have a lookml_link_id which links to the original LookML dashboard.  To give the imported dashboard specify a (e.g. title: \"my title\") in the body of your request, otherwise the imported dashboard will have the same title as the original LookML dashboard.  For this operation to succeed the user must have permission to see the LookML dashboard in question, and have permission to create content in the space the dashboard is being imported to.  **Sync** a linked UDD with [sync_lookml_dashboard()](#!/Dashboard/sync_lookml_dashboard) **Unlink** a linked UDD by setting lookml_link_id to null with [update_dashboard()](#!/Dashboard/update_dashboard)

#### Example

#### Parameters

**space_id** | **string**| Id of space to import the dashboard to |
 **body** | [**\Swagger\Client\Model\Dashboard**](../Model/Dashboard.md)| Dashboard | [optional]
 **raw_locale** | **bool**| If true, and this dashboard is localized, export it with the raw keys, not localized. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Move an existing dashboard  Moves a dashboard to a specified folder, and returns the moved dashboard.  `dashboard_id` and `folder_id` are required. `dashboard_id` and `folder_id` must already exist, and `folder_id` must be different from the current `folder_id` of the dashboard.

#### Example

#### Parameters

**folder_id** | **string**| Folder id to move to. |

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Search Dashboard Elements  Returns an **array of DashboardElement objects** that match the specified search criteria.  If multiple search params are given and `filter_or` is FALSE or not specified, search params are combined in a logical AND operation. Only rows that match *all* search param criteria will be returned.  If `filter_or` is TRUE, multiple search params are combined in a logical OR operation. Results will include rows that match **any** of the search criteria.  String search params use case-insensitive matching. String search params can contain `%` and '_' as SQL LIKE pattern match wildcard expressions. example=\"dan%\" will match \"danger\" and \"Danzig\" but not \"David\" example=\"D_m%\" will match \"Damage\" and \"dump\"  Integer search params can accept a single value or a comma separated list of values. The multiple values will be combined under a logical OR operation - results will match at least one of the given values.  Most search params can accept \"IS NULL\" and \"NOT NULL\" as special expressions to match or exclude (respectively) rows where the column is null.  Boolean search params accept only \"true\" and \"false\" as values.

#### Example

#### Parameters

**look_id** | **string**| Select elements that refer to a given look id | [optional]
 **title** | **string**| Match the title of element | [optional]
 **deleted** | **bool**| Select soft-deleted dashboard elements | [optional]
 **fields** | **string**| Requested fields. | [optional]
 **filter_or** | **bool**| Combine given search criteria in a boolean OR expression | [optional]
 **sorts** | **string**| Fields to sort by. Sortable fields: [:look_id, :dashboard_id, :deleted, :title] | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Search Dashboards  Returns an array of **user-defined dashboard** objects that match the specified search criteria. Note, [search_dashboards()](#!/Dashboard/search_dashboards) does not return LookML dashboard objects.  If multiple search params are given and `filter_or` is FALSE or not specified, search params are combined in a logical AND operation. Only rows that match *all* search param criteria will be returned.  If `filter_or` is TRUE, multiple search params are combined in a logical OR operation. Results will include rows that match **any** of the search criteria.  String search params use case-insensitive matching. String search params can contain `%` and '_' as SQL LIKE pattern match wildcard expressions. example=\"dan%\" will match \"danger\" and \"Danzig\" but not \"David\" example=\"D_m%\" will match \"Damage\" and \"dump\"  Integer search params can accept a single value or a comma separated list of values. The multiple values will be combined under a logical OR operation - results will match at least one of the given values.  Most search params can accept \"IS NULL\" and \"NOT NULL\" as special expressions to match or exclude (respectively) rows where the column is null.  Boolean search params accept only \"true\" and \"false\" as values.   The parameters `limit`, and `offset` are recommended for fetching results in page-size chunks.  Get a **single dashboard** by id with [dashboard()](#!/Dashboard/dashboard)

#### Example

#### Parameters

**slug** | **string**| Match dashboard slug. | [optional]
 **title** | **string**| Match Dashboard title. | [optional]
 **description** | **string**| Match Dashboard description. | [optional]
 **content_favorite_id** | **string**| Filter on a content favorite id. | [optional]
 **folder_id** | **string**| Filter on a particular space. | [optional]
 **deleted** | **string**| Filter on dashboards deleted status. | [optional]
 **user_id** | **string**| Filter on dashboards created by a particular user. | [optional]
 **view_count** | **string**| Filter on a particular value of view_count | [optional]
 **content_metadata_id** | **string**| Filter on a content favorite id. | [optional]
 **curate** | **bool**| Exclude items that exist only in personal spaces other than the users | [optional]
 **last_viewed_at** | **string**| Select dashboards based on when they were last viewed | [optional]
 **fields** | **string**| Requested fields. | [optional]
 **page** | **int**| DEPRECATED. Use limit and offset instead. Return only page N of paginated results | [optional]
 **per_page** | **int**| DEPRECATED. Use limit and offset instead. Return N rows of data per page | [optional]
 **limit** | **int**| Number of results to return. (used with offset and takes priority over page and per_page) | [optional]
 **offset** | **int**| Number of results to skip before returning any. (used with limit and takes priority over page and per_page) | [optional]
 **sorts** | **string**| One or more fields to sort by. Sortable fields: [:title, :user_id, :id, :created_at, :space_id, :folder_id, :description, :view_count, :favorite_count, :slug, :content_favorite_id, :content_metadata_id, :deleted, :deleted_at, :last_viewed_at, :last_accessed_at] | [optional]
 **filter_or** | **bool**| Combine given search criteria in a boolean OR expression | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Update all linked dashboards to match the specified LookML dashboard.  Any UDD (a dashboard which exists in the Looker database rather than as a LookML file) which has a `lookml_link_id` property value referring to a LookML dashboard's id (model::dashboardname) will be updated so that it matches the current state of the LookML dashboard.  For this operation to succeed the user must have permission to view the LookML dashboard, and only linked dashboards that the user has permission to update will be synced.  To **link** or **unlink** a UDD set the `lookml_link_id` property with [update_dashboard()](#!/Dashboard/update_dashboard)

#### Example

#### Parameters

**body** | [**\Swagger\Client\Model\Dashboard**](../Model/Dashboard.md)| Dashboard |
 **raw_locale** | **bool**| If true, and this dashboard is localized, export it with the raw keys, not localized. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Update a dashboard  You can use this function to change the string and integer properties of a dashboard. Nested objects such as filters, dashboard elements, or dashboard layout components cannot be modified by this function - use the update functions for the respective nested object types (like [update_dashboard_filter()](#!/3.1/Dashboard/update_dashboard_filter) to change a filter) to modify nested objects referenced by a dashboard.  If you receive a 422 error response when updating a dashboard, be sure to look at the response body for information about exactly which fields are missing or contain invalid data.

#### Example

#### Parameters

**body** | [**\Swagger\Client\Model\Dashboard**](../Model/Dashboard.md)| Dashboard |

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Update the dashboard element with a specific id.

#### Example

#### Parameters

**body** | [**\Swagger\Client\Model\DashboardElement**](../Model/DashboardElement.md)| DashboardElement |
 **fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Update the dashboard filter with a specific id.

#### Example

#### Parameters

**body** | [**\Swagger\Client\Model\DashboardFilter**](../Model/DashboardFilter.md)| Dashboard Filter |
 **fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Update the dashboard layout with a specific id.

#### Example

#### Parameters

**body** | [**\Swagger\Client\Model\DashboardLayout**](../Model/DashboardLayout.md)| DashboardLayout |
 **fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Update the dashboard element with a specific id.

#### Example

#### Parameters

**body** | [**\Swagger\Client\Model\DashboardLayoutComponent**](../Model/DashboardLayoutComponent.md)| DashboardLayoutComponent |
 **fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

### ConfigApi

#### Get all legacy features.

#### Example

#### Parameters

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get a list of locales that Looker supports.

#### Example

#### Parameters

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get a list of timezones that Looker supports (e.g. useful for scheduling tasks).

#### Example

#### Parameters

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get an API specification for this Looker instance.  The specification is returned as a JSON document in Swagger 2.x format

#### Example

#### Parameters

**specification** | **string**| Specification name. Typically, this is \&quot;swagger.json\&quot; |

#### Return type

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Example

#### Parameters

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Trigger the generation of digest email records and send them to Looker's internal system. This does not send any actual emails, it generates records containing content which may be of interest for users who have become inactive. Emails will be sent at a later time from Looker's internal system if the Digest Emails feature is enabled in settings.

#### Example

#### Parameters

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get the current status and content of custom welcome emails

#### Example

#### Parameters

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Retrieve the value for whether or not digest emails is enabled

#### Example

#### Parameters

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get Looker Settings  Available settings are:  - allow_user_timezones  - custom_welcome_email  - data_connector_default_enabled  - extension_framework_enabled  - extension_load_url_enabled  - marketplace_auto_install_enabled  - marketplace_enabled  - onboarding_enabled  - privatelabel_configuration  - timezone  - host_url  - email_domain_allowlist

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get and set the options for internal help resources

#### Example

#### Parameters

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Set the menu item name and content for internal help resources

#### Example

#### Parameters

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get information about the legacy feature with a specific id.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get all mobile settings.

#### Example

#### Parameters

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get Egress IP Addresses  Returns the list of public egress IP Addresses for a hosted customer's instance

#### Example

#### Parameters

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Configure Looker Settings  Available settings are:  - allow_user_timezones  - custom_welcome_email  - data_connector_default_enabled  - extension_framework_enabled  - extension_load_url_enabled  - marketplace_auto_install_enabled  - marketplace_enabled  - onboarding_enabled  - privatelabel_configuration  - timezone  - host_url  - email_domain_allowlist  See the `Setting` type for more information on the specific values that can be configured.

#### Example

#### Parameters

**fields** | **string**| Requested fields | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Configure SMTP Settings   This API allows users to configure the SMTP settings on the Looker instance.   This API is only supported in the OEM jar. Additionally, only admin users are authorised to call this API.

#### Example

#### Parameters

#

#### Return type

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get current SMTP status.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Example

#### Parameters

**send_test_welcome_email** | **bool**| If true a test email with the content from the request will be sent to the current user after saving | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Update the setting for enabling/disabling digest emails

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Update information about the legacy feature with a specific id.

#### Example

#### Parameters

**body** | [**\Swagger\Client\Model\LegacyFeature**](../Model/LegacyFeature.md)| Legacy Feature |

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Update the whitelabel configuration

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get information about all API versions supported by this Looker instance.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### This feature is enabled only by special license. ### Gets the whitelabel configuration, which includes hiding documentation links, custom favicon uploading, etc.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

### LookApi

#### Get information about all active Looks  Returns an array of **abbreviated Look objects** describing all the looks that the caller has access to. Soft-deleted Looks are **not** included.  Get the **full details** of a specific look by id with [look(id)](#!/Look/look)  Find **soft-deleted looks** with [search_looks()](#!/Look/search_looks)

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Copy an existing look  Creates a copy of an existing look, in a specified folder, and returns the copied look.  `look_id` and `folder_id` are required.  `look_id` and `folder_id` must already exist, and `folder_id` must be different from the current `folder_id` of the dashboard.

#### Example

#### Parameters

**folder_id** | **string**| Folder id to copy to. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Create a Look  To create a look to display query data, first create the query with [create_query()](#!/Query/create_query) then assign the query's id to the `query_id` property in the call to `create_look()`.  To place the look into a particular space, assign the space's id to the `space_id` property in the call to `create_look()`.

#### Example

#### Parameters

**fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Permanently Delete a Look  This operation **permanently** removes a look from the Looker database.  NOTE: There is no \"undo\" for this kind of delete.  For information about soft-delete (which can be undone) see [update_look()](#!/Look/update_look).

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get a Look.  Returns detailed information about a Look and its associated Query.

#### Example

#### Parameters

**fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Move an existing look  Moves a look to a specified folder, and returns the moved look.  `look_id` and `folder_id` are required. `look_id` and `folder_id` must already exist, and `folder_id` must be different from the current `folder_id` of the dashboard.

#### Example

#### Parameters

**folder_id** | **string**| Folder id to move to. |

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Run a Look  Runs a given look's query and returns the results in the requested format.  Supported formats:  | result_format | Description | :-----------: | :--- | | json | Plain json | json_detail | Row data plus metadata describing the fields, pivots, table calcs, and other aspects of the query | csv | Comma separated values with a header | txt | Tab separated values with a header | html | Simple html | md | Simple markdown | xlsx | MS Excel spreadsheet | sql | Returns the generated SQL rather than running the query | png | A PNG image of the visualization of the query | jpg | A JPG image of the visualization of the query

#### Example

#### Parameters

**result_format** | **string**| Format of result |
 **limit** | **int**| Row limit (may override the limit in the saved query). | [optional]
 **apply_formatting** | **bool**| Apply model-specified formatting to each result. | [optional]
 **apply_vis** | **bool**| Apply visualization options to results. | [optional]
 **cache** | **bool**| Get results from cache if available. | [optional]
 **image_width** | **int**| Render width for image formats. | [optional]
 **image_height** | **int**| Render height for image formats. | [optional]
 **generate_drill_links** | **bool**| Generate drill links (only applicable to &#39;json_detail&#39; format. | [optional]
 **force_production** | **bool**| Force use of production models even if the user is in development mode. Note that this flag being false does not guarantee development models will be used. | [optional]
 **cache_only** | **bool**| Retrieve any results from cache even if the results have expired. | [optional]
 **path_prefix** | **string**| Prefix to use for drill links (url encoded). | [optional]
 **rebuild_pdts** | **bool**| Rebuild PDTS used in query. | [optional]
 **server_table_calcs** | **bool**| Perform table calculations on query results | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: text, application/json, image/png, image/jpeg

#### Search Looks  Returns an **array of Look objects** that match the specified search criteria.  If multiple search params are given and `filter_or` is FALSE or not specified, search params are combined in a logical AND operation. Only rows that match *all* search param criteria will be returned.  If `filter_or` is TRUE, multiple search params are combined in a logical OR operation. Results will include rows that match **any** of the search criteria.  String search params use case-insensitive matching. String search params can contain `%` and '_' as SQL LIKE pattern match wildcard expressions. example=\"dan%\" will match \"danger\" and \"Danzig\" but not \"David\" example=\"D_m%\" will match \"Damage\" and \"dump\"  Integer search params can accept a single value or a comma separated list of values. The multiple values will be combined under a logical OR operation - results will match at least one of the given values.  Most search params can accept \"IS NULL\" and \"NOT NULL\" as special expressions to match or exclude (respectively) rows where the column is null.  Boolean search params accept only \"true\" and \"false\" as values.   Get a **single look** by id with [look(id)](#!/Look/look)

#### Example

#### Parameters

**title** | **string**| Match Look title. | [optional]
 **description** | **string**| Match Look description. | [optional]
 **content_favorite_id** | **string**| Select looks with a particular content favorite id | [optional]
 **folder_id** | **string**| Select looks in a particular folder. | [optional]
 **user_id** | **string**| Select looks created by a particular user. | [optional]
 **view_count** | **string**| Select looks with particular view_count value | [optional]
 **deleted** | **bool**| Select soft-deleted looks | [optional]
 **query_id** | **string**| Select looks that reference a particular query by query_id | [optional]
 **curate** | **bool**| Exclude items that exist only in personal spaces other than the users | [optional]
 **last_viewed_at** | **string**| Select looks based on when they were last viewed | [optional]
 **fields** | **string**| Requested fields. | [optional]
 **page** | **int**| DEPRECATED. Use limit and offset instead. Return only page N of paginated results | [optional]
 **per_page** | **int**| DEPRECATED. Use limit and offset instead. Return N rows of data per page | [optional]
 **limit** | **int**| Number of results to return. (used with offset and takes priority over page and per_page) | [optional]
 **offset** | **int**| Number of results to skip before returning any. (used with limit and takes priority over page and per_page) | [optional]
 **sorts** | **string**| One or more fields to sort results by. Sortable fields: [:title, :user_id, :id, :created_at, :space_id, :folder_id, :description, :updated_at, :last_updater_id, :view_count, :favorite_count, :content_favorite_id, :deleted, :deleted_at, :last_viewed_at, :last_accessed_at, :query_id] | [optional]
 **filter_or** | **bool**| Combine given search criteria in a boolean OR expression | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Modify a Look  Use this function to modify parts of a look. Property values given in a call to `update_look` are applied to the existing look, so there's no need to include properties whose values are not changing. It's best to specify only the properties you want to change and leave everything else out of your `update_look` call. **Look properties marked 'read-only' will be ignored.**  When a user deletes a look in the Looker UI, the look data remains in the database but is marked with a deleted flag (\"soft-deleted\"). Soft-deleted looks can be undeleted (by an admin) if the delete was in error.  To soft-delete a look via the API, use [update_look()](#!/Look/update_look) to change the look's `deleted` property to `true`. You can undelete a look by calling `update_look` to change the look's `deleted` property to `false`.  Soft-deleted looks are excluded from the results of [all_looks()](#!/Look/all_looks) and [search_looks()](#!/Look/search_looks), so they essentially disappear from view even though they still reside in the db. In API 3.1 and later, you can pass `deleted: true` as a parameter to [search_looks()](#!/3.1/Look/search_looks) to list soft-deleted looks.  NOTE: [delete_look()](#!/Look/delete_look) performs a \"hard delete\" - the look data is removed from the Looker database and destroyed. There is no \"undo\" for `delete_look()`.

#### Example

#### Parameters

**body** | [**\Swagger\Client\Model\LookWithQuery**](../Model/LookWithQuery.md)| Look |
 **fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

### WorkspaceApi

#### Get All Workspaces  Returns all workspaces available to the calling user.

#### Example

#### Parameters

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get A Workspace  Returns information about a workspace such as the git status and selected branches of all projects available to the caller's user account.  A workspace defines which versions of project files will be used to evaluate expressions and operations that use model definitions - operations such as running queries or rendering dashboards. Each project has its own git repository, and each project in a workspace may be configured to reference particular branch or revision within their respective repositories.  There are two predefined workspaces available: \"production\" and \"dev\".  The production workspace is shared across all Looker users. Models in the production workspace are read-only. Changing files in production is accomplished by modifying files in a git branch and using Pull Requests to merge the changes from the dev branch into the production branch, and then telling Looker to sync with production.  The dev workspace is local to each Looker user. Changes made to project/model files in the dev workspace only affect that user, and only when the dev workspace is selected as the active workspace for the API session. (See set_session_workspace()).  The dev workspace is NOT unique to an API session. Two applications accessing the Looker API using the same user account will see the same files in the dev workspace. To avoid collisions between API clients it's best to have each client login with API credentials for a different user account.  Changes made to files in a dev workspace are persistent across API sessions. It's a good idea to commit any changes you've made to the git repository, but not strictly required. Your modified files reside in a special user-specific directory on the Looker server and will still be there when you login in again later and use update_session(workspace_id: \"dev\") to select the dev workspace for the new API session.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

### RenderTaskApi

#### Create a new task to render a dashboard element to an image.  Returns a render task object. To check the status of a render task, pass the render_task.id to [Get Render Task](#!/RenderTask/get_render_task). Once the render task is complete, you can download the resulting document or image using [Get Render Task Results](#!/RenderTask/get_render_task_results).

#### Example

#### Parameters

**result_format** | **string**| Output type: png or jpg |
 **width** | **int**| Output width in pixels |
 **height** | **int**| Output height in pixels |
 **fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Create a new task to render a dashboard to a document or image.  Returns a render task object. To check the status of a render task, pass the render_task.id to [Get Render Task](#!/RenderTask/get_render_task). Once the render task is complete, you can download the resulting document or image using [Get Render Task Results](#!/RenderTask/get_render_task_results).

#### Example

#### Parameters

**result_format** | **string**| Output type: pdf, png, or jpg |
 **body** | [**\Swagger\Client\Model\CreateDashboardRenderTask**](../Model/CreateDashboardRenderTask.md)| Dashboard render task parameters |
 **width** | **int**| Output width in pixels |
 **height** | **int**| Output height in pixels |
 **fields** | **string**| Requested fields. | [optional]
 **pdf_paper_size** | **string**| Paper size for pdf. Value can be one of: [\&quot;letter\&quot;,\&quot;legal\&quot;,\&quot;tabloid\&quot;,\&quot;a0\&quot;,\&quot;a1\&quot;,\&quot;a2\&quot;,\&quot;a3\&quot;,\&quot;a4\&quot;,\&quot;a5\&quot;] | [optional]
 **pdf_landscape** | **bool**| Whether to render pdf in landscape paper orientation | [optional]
 **long_tables** | **bool**| Whether or not to expand table vis to full length | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Create a new task to render a look to an image.  Returns a render task object. To check the status of a render task, pass the render_task.id to [Get Render Task](#!/RenderTask/get_render_task). Once the render task is complete, you can download the resulting document or image using [Get Render Task Results](#!/RenderTask/get_render_task_results).

#### Example

#### Parameters

**result_format** | **string**| Output type: png, or jpg |
 **width** | **int**| Output width in pixels |
 **height** | **int**| Output height in pixels |
 **fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Create a new task to render an existing query to an image.  Returns a render task object. To check the status of a render task, pass the render_task.id to [Get Render Task](#!/RenderTask/get_render_task). Once the render task is complete, you can download the resulting document or image using [Get Render Task Results](#!/RenderTask/get_render_task_results).

#### Example

#### Parameters

**result_format** | **string**| Output type: png or jpg |
 **width** | **int**| Output width in pixels |
 **height** | **int**| Output height in pixels |
 **fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get information about a render task.  Returns a render task object. To check the status of a render task, pass the render_task.id to [Get Render Task](#!/RenderTask/get_render_task). Once the render task is complete, you can download the resulting document or image using [Get Render Task Results](#!/RenderTask/get_render_task_results).

#### Example

#### Parameters

**fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get the document or image produced by a completed render task.  Note that the PDF or image result will be a binary blob in the HTTP response, as indicated by the Content-Type in the response headers. This may require specialized (or at least different) handling than text responses such as JSON. You may need to tell your HTTP client that the response is binary so that it does not attempt to parse the binary data as text.  If the render task exists but has not finished rendering the results, the response HTTP status will be **202 Accepted**, the response body will be empty, and the response will have a Retry-After header indicating that the caller should repeat the request at a later time.  Returns 404 if the render task cannot be found, if the cached result has expired, or if the caller does not have permission to view the results.  For detailed information about the status of the render task, use [Render Task](#!/RenderTask/render_task). Polling loops waiting for completion of a render task would be better served by polling **render_task(id)** until the task status reaches completion (or error) instead of polling **render_task_results(id)** alone.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: image/jpeg, image/png, application/pdf

### ConnectionApi

#### Get information about all connections.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get information about all dialects.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get all External OAuth Applications.  This is an OAuth Application which Looker uses to access external systems.

#### Example

#### Parameters

**client_id** | **string**| Application Client ID | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get information about all SSH Servers.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get information about all SSH Tunnels.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get information about a connection.

#### Example

#### Parameters

**fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Create a connection using the specified configuration.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Create an OAuth Application using the specified configuration.  This is an OAuth Application which Looker uses to access external systems.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Create OAuth User state.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Create an SSH Server.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Create an SSH Tunnel

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Delete a connection.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Delete a connection override.

#### Example

#### Parameters

**override_context** | **string**| Context of connection override |

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Delete an SSH Server.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Delete an SSH Tunnel

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get the SSH public key  Get the public key created for this instance to identify itself to a remote SSH server.

#### Example

#### Parameters

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get information about an SSH Server.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get information about an SSH Tunnel.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Test an existing connection.  Note that a connection's 'dialect' property has a 'connection_tests' property that lists the specific types of tests that the connection supports.  This API is rate limited.  Unsupported tests in the request will be ignored.

#### Example

#### Parameters

**tests** | [**string[]**](../Model/string.md)| Array of names of tests to run | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Test a connection configuration.  Note that a connection's 'dialect' property has a 'connection_tests' property that lists the specific types of tests that the connection supports.  This API is rate limited.  Unsupported tests in the request will be ignored.

#### Example

#### Parameters

**tests** | [**string[]**](../Model/string.md)| Array of names of tests to run | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Test the SSH Server

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Test the SSH Tunnel

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Update a connection using the specified configuration.

#### Example

#### Parameters

**body** | [**\Swagger\Client\Model\DBConnection**](../Model/DBConnection.md)| Connection |

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Update an SSH Server.

#### Example

#### Parameters

**body** | [**\Swagger\Client\Model\SshServer**](../Model/SshServer.md)| SSH Server |

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Update an SSH Tunnel

#### Example

#### Parameters

**body** | [**\Swagger\Client\Model\SshTunnel**](../Model/SshTunnel.md)| SSH Tunnel |

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

### QueryApi

#### Example

#### Parameters

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Create Merge Query  Creates a new merge query object.  A merge query takes the results of one or more queries and combines (merges) the results according to field mapping definitions. The result is similar to a SQL left outer join.  A merge query can merge results of queries from different SQL databases.  The order that queries are defined in the source_queries array property is significant. The first query in the array defines the primary key into which the results of subsequent queries will be merged.  Like model/view query objects, merge queries are immutable and have structural identity - if you make a request to create a new merge query that is identical to an existing merge query, the existing merge query will be returned instead of creating a duplicate. Conversely, any change to the contents of a merge query will produce a new object with a new id.

#### Example

#### Parameters

**fields** | **string**| Requested fields | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Create a query.  This allows you to create a new query that you can later run. Looker queries are immutable once created and are not deleted. If you create a query that is exactly like an existing query then the existing query will be returned and no new query will be created. Whether a new query is created or not, you can use the 'id' in the returned query with the 'run' method.  The query parameters are passed as json in the body of the request.

#### Example

#### Parameters

**fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Create an async query task  Creates a query task (job) to run a previously created query asynchronously. Returns a Query Task ID.  Use [query_task(query_task_id)](#!/Query/query_task) to check the execution status of the query task. After the query task status reaches \"Complete\", use [query_task_results(query_task_id)](#!/Query/query_task_results) to fetch the results of the query.

#### Example

#### Parameters

**limit** | **int**| Row limit (may override the limit in the saved query). | [optional]
 **apply_formatting** | **bool**| Apply model-specified formatting to each result. | [optional]
 **apply_vis** | **bool**| Apply visualization options to results. | [optional]
 **cache** | **bool**| Get results from cache if available. | [optional]
 **generate_drill_links** | **bool**| Generate drill links (only applicable to &#39;json_detail&#39; format. | [optional]
 **force_production** | **bool**| Force use of production models even if the user is in development mode. Note that this flag being false does not guarantee development models will be used. | [optional]
 **cache_only** | **bool**| Retrieve any results from cache even if the results have expired. | [optional]
 **path_prefix** | **string**| Prefix to use for drill links (url encoded). | [optional]
 **rebuild_pdts** | **bool**| Rebuild PDTS used in query. | [optional]
 **server_table_calcs** | **bool**| Perform table calculations on query results | [optional]
 **image_width** | **int**| DEPRECATED. Render width for image formats. Note that this parameter is always ignored by this method. | [optional]
 **image_height** | **int**| DEPRECATED. Render height for image formats. Note that this parameter is always ignored by this method. | [optional]
 **fields** | **string**| Requested fields | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Create a SQL Runner Query  Either the `connection_name` or `model_name` parameter MUST be provided.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get Merge Query  Returns a merge query object given its id.

#### Example

#### Parameters

**fields** | **string**| Requested fields | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get a previously created query by id.  A Looker query object includes the various parameters that define a database query that has been run or could be run in the future. These parameters include: model, view, fields, filters, pivots, etc. Query *results* are not part of the query object.  Query objects are unique and immutable. Query objects are created automatically in Looker as users explore data. Looker does not delete them; they become part of the query history. When asked to create a query for any given set of parameters, Looker will first try to find an existing query object with matching parameters and will only create a new object when an appropriate object can not be found.  This 'get' method is used to get the details about a query for a given id. See the other methods here to 'create' and 'run' queries.  Note that some fields like 'filter_config' and 'vis_config' etc are specific to how the Looker UI builds queries and visualizations and are not generally useful for API use. They are not required when creating new queries and can usually just be ignored.

#### Example

#### Parameters

**fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get the query for a given query slug.  This returns the query for the 'slug' in a query share URL.  The 'slug' is a randomly chosen short string that is used as an alternative to the query's id value for use in URLs etc. This method exists as a convenience to help you use the API to 'find' queries that have been created using the Looker UI.  You can use the Looker explore page to build a query and then choose the 'Share' option to show the share url for the query. Share urls generally look something like 'https://looker.yourcompany/x/vwGSbfc'. The trailing 'vwGSbfc' is the share slug. You can pass that string to this api method to get details about the query. Those details include the 'id' that you can use to run the query. Or, you can copy the query body (perhaps with your own modification) and use that as the basis to make/run new queries.  This will also work with slugs from Looker explore urls like 'https://looker.yourcompany/explore/ecommerce/orders?qid=aogBgL6o3cKK1jN3RoZl5s'. In this case 'aogBgL6o3cKK1jN3RoZl5s' is the slug.

#### Example

#### Parameters

**fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get Query Task details  Use this function to check the status of an async query task. After the status reaches \"Complete\", you can call [query_task_results(query_task_id)](#!/Query/query_task_results) to retrieve the results of the query.  Use [create_query_task()](#!/Query/create_query_task) to create an async query task.

#### Example

#### Parameters

**fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Fetch results of multiple async queries  Returns the results of multiple async queries in one request.  For Query Tasks that are not completed, the response will include the execution status of the Query Task but will not include query results. Query Tasks whose results have expired will have a status of 'expired'. If the user making the API request does not have sufficient privileges to view a Query Task result, the result will have a status of 'missing'

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get Async Query Results  Returns the results of an async query task if the query has completed.  If the query task is still running or waiting to run, this function returns 204 No Content.  If the query task ID is invalid or the cached results of the query task have expired, this function returns 404 Not Found.  Use [query_task(query_task_id)](#!/Query/query_task) to check the execution status of the query task Call query_task_results only after the query task status reaches \"Complete\".  You can also use [query_task_multi_results()](#!/Query/query_task_multi_results) retrieve the results of multiple async query tasks at the same time.  #### SQL Error Handling: If the query fails due to a SQL db error, how this is communicated depends on the result_format you requested in `create_query_task()`.  For `json_detail` result_format: `query_task_results()` will respond with HTTP status '200 OK' and db SQL error info will be in the `errors` property of the response object. The 'data' property will be empty.  For all other result formats: `query_task_results()` will respond with HTTP status `400 Bad Request` and some db SQL error info will be in the message of the 400 error response, but not as detailed as expressed in `json_detail.errors`. These data formats can only carry row data, and error info is not row data.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: text, application/json

#### Run the query that is specified inline in the posted body.  This allows running a query as defined in json in the posted body. This combines the two actions of posting & running a query into one step.  Here is an example body in json: ``` {   \"model\":\"thelook\",   \"view\":\"inventory_items\",   \"fields\":[\"category.name\",\"inventory_items.days_in_inventory_tier\",\"products.count\"],   \"filters\":{\"category.name\":\"socks\"},   \"sorts\":[\"products.count desc 0\"],   \"limit\":\"500\",   \"query_timezone\":\"America/Los_Angeles\" } ```  When using the Ruby SDK this would be passed as a Ruby hash like: ``` {  :model=>\"thelook\",  :view=>\"inventory_items\",  :fields=>   [\"category.name\",    \"inventory_items.days_in_inventory_tier\",    \"products.count\"],  :filters=>{:\"category.name\"=>\"socks\"},  :sorts=>[\"products.count desc 0\"],  :limit=>\"500\",  :query_timezone=>\"America/Los_Angeles\", } ```  This will return the result of running the query in the format specified by the 'result_format' parameter.  Supported formats:  | result_format | Description | :-----------: | :--- | | json | Plain json | json_detail | Row data plus metadata describing the fields, pivots, table calcs, and other aspects of the query | csv | Comma separated values with a header | txt | Tab separated values with a header | html | Simple html | md | Simple markdown | xlsx | MS Excel spreadsheet | sql | Returns the generated SQL rather than running the query | png | A PNG image of the visualization of the query | jpg | A JPG image of the visualization of the query

#### Example

#### Parameters

**body** | [**\Swagger\Client\Model\Query**](../Model/Query.md)| inline query |
 **limit** | **int**| Row limit (may override the limit in the saved query). | [optional]
 **apply_formatting** | **bool**| Apply model-specified formatting to each result. | [optional]
 **apply_vis** | **bool**| Apply visualization options to results. | [optional]
 **cache** | **bool**| Get results from cache if available. | [optional]
 **image_width** | **int**| Render width for image formats. | [optional]
 **image_height** | **int**| Render height for image formats. | [optional]
 **generate_drill_links** | **bool**| Generate drill links (only applicable to &#39;json_detail&#39; format. | [optional]
 **force_production** | **bool**| Force use of production models even if the user is in development mode. Note that this flag being false does not guarantee development models will be used. | [optional]
 **cache_only** | **bool**| Retrieve any results from cache even if the results have expired. | [optional]
 **path_prefix** | **string**| Prefix to use for drill links (url encoded). | [optional]
 **rebuild_pdts** | **bool**| Rebuild PDTS used in query. | [optional]
 **server_table_calcs** | **bool**| Perform table calculations on query results | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: text, application/json, image/png, image/jpeg

#### Run a saved query.  This runs a previously saved query. You can use this on a query that was generated in the Looker UI or one that you have explicitly created using the API. You can also use a query 'id' from a saved 'Look'.  The 'result_format' parameter specifies the desired structure and format of the response.  Supported formats:  | result_format | Description | :-----------: | :--- | | json | Plain json | json_detail | Row data plus metadata describing the fields, pivots, table calcs, and other aspects of the query | csv | Comma separated values with a header | txt | Tab separated values with a header | html | Simple html | md | Simple markdown | xlsx | MS Excel spreadsheet | sql | Returns the generated SQL rather than running the query | png | A PNG image of the visualization of the query | jpg | A JPG image of the visualization of the query

#### Example

#### Parameters

**result_format** | **string**| Format of result |
 **limit** | **int**| Row limit (may override the limit in the saved query). | [optional]
 **apply_formatting** | **bool**| Apply model-specified formatting to each result. | [optional]
 **apply_vis** | **bool**| Apply visualization options to results. | [optional]
 **cache** | **bool**| Get results from cache if available. | [optional]
 **image_width** | **int**| Render width for image formats. | [optional]
 **image_height** | **int**| Render height for image formats. | [optional]
 **generate_drill_links** | **bool**| Generate drill links (only applicable to &#39;json_detail&#39; format. | [optional]
 **force_production** | **bool**| Force use of production models even if the user is in development mode. Note that this flag being false does not guarantee development models will be used. | [optional]
 **cache_only** | **bool**| Retrieve any results from cache even if the results have expired. | [optional]
 **path_prefix** | **string**| Prefix to use for drill links (url encoded). | [optional]
 **rebuild_pdts** | **bool**| Rebuild PDTS used in query. | [optional]
 **server_table_calcs** | **bool**| Perform table calculations on query results | [optional]
 **source** | **string**| Specifies the source of this call. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: text, application/json, image/png, image/jpeg

#### Example

#### Parameters

**result_format** | **string**| Format of result, options are: [\&quot;inline_json\&quot;, \&quot;json\&quot;, \&quot;json_detail\&quot;, \&quot;json_fe\&quot;, \&quot;csv\&quot;, \&quot;html\&quot;, \&quot;md\&quot;, \&quot;txt\&quot;, \&quot;xlsx\&quot;, \&quot;gsxml\&quot;, \&quot;json_label\&quot;] |
 **download** | **string**| Defaults to false. If set to true, the HTTP response will have content-disposition and other headers set to make the HTTP response behave as a downloadable attachment instead of as inline content. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: text, application/json, image/png, image/jpeg

#### Run an URL encoded query.  This requires the caller to encode the specifiers for the query into the URL query part using Looker-specific syntax as explained below.  Generally, you would want to use one of the methods that takes the parameters as json in the POST body for creating and/or running queries. This method exists for cases where one really needs to encode the parameters into the URL of a single 'GET' request. This matches the way that the Looker UI formats 'explore' URLs etc.  The parameters here are very similar to the json body formatting except that the filter syntax is tricky. Unfortunately, this format makes this method not currently callable via the 'Try it out!' button in this documentation page. But, this is callable when creating URLs manually or when using the Looker SDK.  Here is an example inline query URL:  ``` https://looker.mycompany.com:19999/api/3.0/queries/models/thelook/views/inventory_items/run/json?fields=category.name,inventory_items.days_in_inventory_tier,products.count&f[category.name]=socks&sorts=products.count+desc+0&limit=500&query_timezone=America/Los_Angeles ```  When invoking this endpoint with the Ruby SDK, pass the query parameter parts as a hash. The hash to match the above would look like:  ```ruby query_params = {   fields: \"category.name,inventory_items.days_in_inventory_tier,products.count\",   :\"f[category.name]\" => \"socks\",   sorts: \"products.count desc 0\",   limit: \"500\",   query_timezone: \"America/Los_Angeles\" } response = ruby_sdk.run_url_encoded_query('thelook','inventory_items','json', query_params)  ```  Again, it is generally easier to use the variant of this method that passes the full query in the POST body. This method is available for cases where other alternatives won't fit the need.  Supported formats:  | result_format | Description | :-----------: | :--- | | json | Plain json | json_detail | Row data plus metadata describing the fields, pivots, table calcs, and other aspects of the query | csv | Comma separated values with a header | txt | Tab separated values with a header | html | Simple html | md | Simple markdown | xlsx | MS Excel spreadsheet | sql | Returns the generated SQL rather than running the query | png | A PNG image of the visualization of the query | jpg | A JPG image of the visualization of the query

#### Example

#### Parameters

**view_name** | **string**| View name |
 **result_format** | **string**| Format of result |

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: text, application/json, image/png, image/jpeg

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

### MetadataApi

#### Get the columns (and therefore also the tables) in a specific schema

#### Example

#### Parameters

**database** | **string**| For dialects that support multiple databases, optionally identify which to use | [optional]
 **schema_name** | **string**| Name of schema to use. | [optional]
 **cache** | **bool**| True to fetch from cache, false to load fresh | [optional]
 **table_limit** | **int**| limits the tables per schema returned | [optional]
 **table_names** | **string**| only fetch columns for a given (comma-separated) list of tables | [optional]
 **fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Connection cost estimating  Assign a `sql` statement to the body of the request. e.g., for Ruby, `{sql: 'select * from users'}`  **Note**: If the connection's dialect has no support for cost estimates, an error will be returned

#### Example

#### Parameters

**body** | [**\Swagger\Client\Model\CreateCostEstimate**](../Model/CreateCostEstimate.md)| SQL statement to estimate |
 **fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### List databases available to this connection  Certain dialects can support multiple databases per single connection. If this connection supports multiple databases, the database names will be returned in an array.  Connections using dialects that do not support multiple databases will return an empty array.  **Note**: [Connection Features](#!/Metadata/connection_features) can be used to determine if a connection supports multiple databases.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Retrieve metadata features for this connection  Returns a list of feature names with `true` (available) or `false` (not available)

#### Example

#### Parameters

**fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get the list of schemas and tables for a connection

#### Example

#### Parameters

**database** | **string**| For dialects that support multiple databases, optionally identify which to use | [optional]
 **cache** | **bool**| True to use fetch from cache, false to load fresh | [optional]
 **fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Search a connection for columns matching the specified name  **Note**: `column_name` must be a valid column name. It is not a search pattern.

#### Example

#### Parameters

**column_name** | **string**| Column name to find | [optional]
 **fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get the list of tables for a schema  For dialects that support multiple databases, optionally identify which to use. If not provided, the default database for the connection will be used.  For dialects that do **not** support multiple databases, **do not use** the database parameter

#### Example

#### Parameters

**database** | **string**| Optional. Name of database to use for the query, only if applicable | [optional]
 **schema_name** | **string**| Optional. Return only tables for this schema | [optional]
 **cache** | **bool**| True to fetch from cache, false to load fresh | [optional]
 **fields** | **string**| Requested fields. | [optional]
 **table_filter** | **string**| Optional. Return tables with names that contain this value | [optional]
 **table_limit** | **int**| Optional. Return tables up to the table_limit | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get a single model

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Field name suggestions for a model and view  `filters` is a string hash of values, with the key as the field name and the string value as the filter expression:  ```ruby {'users.age': '>=60'} ```  or  ```ruby {'users.age': '<30'} ```  or  ```ruby {'users.age': '=50'} ```

#### Example

#### Parameters

**view_name** | **string**| Name of view |
 **field_name** | **string**| Name of field to use for suggestions |
 **term** | **string**| Search term pattern (evaluated as as &#x60;%term%&#x60;) | [optional]
 **filters** | [**map[string,string]**](../Model/string.md)| Suggestion filters with field name keys and comparison expressions | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

### AlertApi

#### Example

#### Parameters

**offset** | **int**| (Optional) Number of results to skip before returning any (used with &#x60;limit&#x60;). | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Create a new alert and return details of the newly created object  Required fields: `field`, `destinations`, `comparison_type`, `threshold`, `cron`  Example Request: Run alert on dashboard element '103' at 5am every day. Send an email to 'test@test.com' if inventory for Los Angeles (using dashboard filter `Warehouse Name`) is lower than 1,000 ``` {   \"cron\": \"0 5 * * *\",   \"custom_title\": \"Alert when LA inventory is low\",   \"dashboard_element_id\": 103,   \"applied_dashboard_filters\": [     {       \"filter_title\": \"Warehouse Name\",       \"field_name\": \"distribution_centers.name\",       \"filter_value\": \"Los Angeles CA\",       \"filter_description\": \"is Los Angeles CA\"     }   ],   \"comparison_type\": \"LESS_THAN\",   \"destinations\": [     {       \"destination_type\": \"EMAIL\",       \"email_address\": \"test@test.com\"     }   ],   \"field\": {     \"title\": \"Number on Hand\",     \"name\": \"inventory_items.number_on_hand\"   },   \"is_disabled\": false,   \"is_public\": true,   \"threshold\": 1000 } ```

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Delete an alert by a given alert ID

#### Example

#### Parameters

#

#### Return type

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Enqueue an Alert by ID

#### Example

#### Parameters

**force** | **bool**| Whether to enqueue an alert again if its already running. | [optional]

#### Return type

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Example

#### Parameters

#

#### Return type

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get an alert by a given alert ID

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Search Alerts

#### Example

#### Parameters

**offset** | **int**| (Optional) Number of results to skip before returning any (used with &#x60;limit&#x60;). | [optional]
 **group_by** | **string**| (Optional) Dimension by which to order the results(&#x60;dashboard&#x60; | &#x60;owner&#x60;) | [optional]
 **fields** | **string**| (Optional) Requested fields. | [optional]
 **disabled** | **bool**| (Optional) Filter on returning only enabled or disabled alerts. | [optional]
 **frequency** | **string**| (Optional) Filter on alert frequency, such as: monthly, weekly, daily, hourly, minutes | [optional]
 **condition_met** | **bool**| (Optional) Filter on whether the alert has met its condition when it last executed | [optional]
 **last_run_start** | **string**| (Optional) Filter on the start range of the last time the alerts were run. Example: 2021-01-01T01:01:01-08:00. | [optional]
 **last_run_end** | **string**| (Optional) Filter on the start range of the last time the alerts were run. Example: 2021-01-01T01:01:01-08:00. | [optional]
 **all_owners** | **bool**| (Admin only) (Optional) Filter for all owners. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Example

#### Parameters

#

#### Return type

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Update an alert # Required fields: `owner_id`, `field`, `destinations`, `comparison_type`, `threshold`, `cron` #

#### Example

#### Parameters

**body** | [**\Swagger\Client\Model\Alert**](../Model/Alert.md)| Alert |

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Update select alert fields # Available fields: `owner_id`, `is_disabled`, `disabled_reason`, `is_public`, `threshold` #

#### Example

#### Parameters

**body** | [**\Swagger\Client\Model\AlertPatch**](../Model/AlertPatch.md)| Alert |

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

### SpaceApi

#### Get information about all spaces.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Create a space with specified information.  Caller must have permission to edit the parent space and to create spaces, otherwise the request returns 404 Not Found.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Delete the space with a specific id including any children spaces. **DANGER** this will delete all looks and dashboards in the space.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Search Spaces    Returns an **array of space objects** that match the given search criteria.    If multiple search params are given and `filter_or` is FALSE or not specified, search params are combined in a logical AND operation. Only rows that match *all* search param criteria will be returned.  If `filter_or` is TRUE, multiple search params are combined in a logical OR operation. Results will include rows that match **any** of the search criteria.  String search params use case-insensitive matching. String search params can contain `%` and '_' as SQL LIKE pattern match wildcard expressions. example=\"dan%\" will match \"danger\" and \"Danzig\" but not \"David\" example=\"D_m%\" will match \"Damage\" and \"dump\"  Integer search params can accept a single value or a comma separated list of values. The multiple values will be combined under a logical OR operation - results will match at least one of the given values.  Most search params can accept \"IS NULL\" and \"NOT NULL\" as special expressions to match or exclude (respectively) rows where the column is null.  Boolean search params accept only \"true\" and \"false\" as values.     The parameters `limit`, and `offset` are recommended for fetching results in page-size chunks.    Get a **single space** by id with [Space](#!/Space/space)

#### Example

#### Parameters

**page** | **int**| Requested page. | [optional]
 **per_page** | **int**| Results per page. | [optional]
 **limit** | **int**| Number of results to return. (used with offset and takes priority over page and per_page) | [optional]
 **offset** | **int**| Number of results to skip before returning any. (used with limit and takes priority over page and per_page) | [optional]
 **sorts** | **string**| Fields to sort by. | [optional]
 **name** | **string**| Match Space title. | [optional]
 **id** | **int**| Match Space id | [optional]
 **parent_id** | **string**| Filter on a children of a particular space. | [optional]
 **creator_id** | **string**| Filter on spaces created by a particular user. | [optional]
 **filter_or** | **bool**| Combine given search criteria in a boolean OR expression | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get information about the space with a specific id.

#### Example

#### Parameters

**fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get the ancestors of a space

#### Example

#### Parameters

**fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get the children of a space.

#### Example

#### Parameters

**fields** | **string**| Requested fields. | [optional]
 **page** | **int**| Requested page. | [optional]
 **per_page** | **int**| Results per page. | [optional]
 **sorts** | **string**| Fields to sort by. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Search the children of a space

#### Example

#### Parameters

**fields** | **string**| Requested fields. | [optional]
 **sorts** | **string**| Fields to sort by. | [optional]
 **name** | **string**| Match Space name. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get the dashboards in a space

#### Example

#### Parameters

**fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get the looks in a space

#### Example

#### Parameters

**fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get the parent of a space

#### Example

#### Parameters

**fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Update the space with a specific id.

#### Example

#### Parameters

**body** | [**\Swagger\Client\Model\Space**](../Model/Space.md)| Space |

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

### RoleApi

#### Get information about all model sets.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get information about all permission sets.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get all supported permissions.

#### Example

#### Parameters

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get information about all roles.

#### Example

#### Parameters

**ids** | [**string[]**](../Model/string.md)| Optional list of ids to get specific roles. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Create a model set with the specified information. Model sets are used by Roles.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Create a permission set with the specified information. Permission sets are used by Roles.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Create a role with the specified information.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Delete the model set with a specific id.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Delete the permission set with a specific id.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Delete the role with a specific id.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get information about the model set with a specific id.

#### Example

#### Parameters

**fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get information about the permission set with a specific id.

#### Example

#### Parameters

**fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get information about the role with a specific id.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get information about all the groups with the role that has a specific id.

#### Example

#### Parameters

**fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get information about all the users with the role that has a specific id.

#### Example

#### Parameters

**fields** | **string**| Requested fields. | [optional]
 **direct_association_only** | **bool**| Get only users associated directly with the role: exclude those only associated through groups. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Search model sets Returns all model set records that match the given search criteria. If multiple search params are given and `filter_or` is FALSE or not specified, search params are combined in a logical AND operation. Only rows that match *all* search param criteria will be returned.  If `filter_or` is TRUE, multiple search params are combined in a logical OR operation. Results will include rows that match **any** of the search criteria.  String search params use case-insensitive matching. String search params can contain `%` and '_' as SQL LIKE pattern match wildcard expressions. example=\"dan%\" will match \"danger\" and \"Danzig\" but not \"David\" example=\"D_m%\" will match \"Damage\" and \"dump\"  Integer search params can accept a single value or a comma separated list of values. The multiple values will be combined under a logical OR operation - results will match at least one of the given values.  Most search params can accept \"IS NULL\" and \"NOT NULL\" as special expressions to match or exclude (respectively) rows where the column is null.  Boolean search params accept only \"true\" and \"false\" as values.

#### Example

#### Parameters

**limit** | **int**| Number of results to return (used with &#x60;offset&#x60;). | [optional]
 **offset** | **int**| Number of results to skip before returning any (used with &#x60;limit&#x60;). | [optional]
 **sorts** | **string**| Fields to sort by. | [optional]
 **id** | **string**| Match model set id. | [optional]
 **name** | **string**| Match model set name. | [optional]
 **all_access** | **bool**| Match model sets by all_access status. | [optional]
 **built_in** | **bool**| Match model sets by built_in status. | [optional]
 **filter_or** | **bool**| Combine given search criteria in a boolean OR expression. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Search permission sets Returns all permission set records that match the given search criteria. If multiple search params are given and `filter_or` is FALSE or not specified, search params are combined in a logical AND operation. Only rows that match *all* search param criteria will be returned.  If `filter_or` is TRUE, multiple search params are combined in a logical OR operation. Results will include rows that match **any** of the search criteria.  String search params use case-insensitive matching. String search params can contain `%` and '_' as SQL LIKE pattern match wildcard expressions. example=\"dan%\" will match \"danger\" and \"Danzig\" but not \"David\" example=\"D_m%\" will match \"Damage\" and \"dump\"  Integer search params can accept a single value or a comma separated list of values. The multiple values will be combined under a logical OR operation - results will match at least one of the given values.  Most search params can accept \"IS NULL\" and \"NOT NULL\" as special expressions to match or exclude (respectively) rows where the column is null.  Boolean search params accept only \"true\" and \"false\" as values.

#### Example

#### Parameters

**limit** | **int**| Number of results to return (used with &#x60;offset&#x60;). | [optional]
 **offset** | **int**| Number of results to skip before returning any (used with &#x60;limit&#x60;). | [optional]
 **sorts** | **string**| Fields to sort by. | [optional]
 **id** | **string**| Match permission set id. | [optional]
 **name** | **string**| Match permission set name. | [optional]
 **all_access** | **bool**| Match permission sets by all_access status. | [optional]
 **built_in** | **bool**| Match permission sets by built_in status. | [optional]
 **filter_or** | **bool**| Combine given search criteria in a boolean OR expression. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Search roles  Returns all role records that match the given search criteria.  If multiple search params are given and `filter_or` is FALSE or not specified, search params are combined in a logical AND operation. Only rows that match *all* search param criteria will be returned.  If `filter_or` is TRUE, multiple search params are combined in a logical OR operation. Results will include rows that match **any** of the search criteria.  String search params use case-insensitive matching. String search params can contain `%` and '_' as SQL LIKE pattern match wildcard expressions. example=\"dan%\" will match \"danger\" and \"Danzig\" but not \"David\" example=\"D_m%\" will match \"Damage\" and \"dump\"  Integer search params can accept a single value or a comma separated list of values. The multiple values will be combined under a logical OR operation - results will match at least one of the given values.  Most search params can accept \"IS NULL\" and \"NOT NULL\" as special expressions to match or exclude (respectively) rows where the column is null.  Boolean search params accept only \"true\" and \"false\" as values.

#### Example

#### Parameters

**limit** | **int**| Number of results to return (used with &#x60;offset&#x60;). | [optional]
 **offset** | **int**| Number of results to skip before returning any (used with &#x60;limit&#x60;). | [optional]
 **sorts** | **string**| Fields to sort by. | [optional]
 **id** | **string**| Match role id. | [optional]
 **name** | **string**| Match role name. | [optional]
 **built_in** | **bool**| Match roles by built_in status. | [optional]
 **filter_or** | **bool**| Combine given search criteria in a boolean OR expression. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Search roles include user count  Returns all role records that match the given search criteria, and attaches associated user counts.  If multiple search params are given and `filter_or` is FALSE or not specified, search params are combined in a logical AND operation. Only rows that match *all* search param criteria will be returned.  If `filter_or` is TRUE, multiple search params are combined in a logical OR operation. Results will include rows that match **any** of the search criteria.  String search params use case-insensitive matching. String search params can contain `%` and '_' as SQL LIKE pattern match wildcard expressions. example=\"dan%\" will match \"danger\" and \"Danzig\" but not \"David\" example=\"D_m%\" will match \"Damage\" and \"dump\"  Integer search params can accept a single value or a comma separated list of values. The multiple values will be combined under a logical OR operation - results will match at least one of the given values.  Most search params can accept \"IS NULL\" and \"NOT NULL\" as special expressions to match or exclude (respectively) rows where the column is null.  Boolean search params accept only \"true\" and \"false\" as values.

#### Example

#### Parameters

**limit** | **int**| Number of results to return (used with &#x60;offset&#x60;). | [optional]
 **offset** | **int**| Number of results to skip before returning any (used with &#x60;limit&#x60;). | [optional]
 **sorts** | **string**| Fields to sort by. | [optional]
 **id** | **string**| Match role id. | [optional]
 **name** | **string**| Match role name. | [optional]
 **built_in** | **bool**| Match roles by built_in status. | [optional]
 **filter_or** | **bool**| Combine given search criteria in a boolean OR expression. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Set all groups for a role, removing all existing group associations from that role.

#### Example

#### Parameters

**body** | **string[]**| Array of Group Ids |

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Set all the users of the role with a specific id.

#### Example

#### Parameters

**body** | **string[]**| array of user ids for role |

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Update information about the model set with a specific id.

#### Example

#### Parameters

**body** | [**\Swagger\Client\Model\ModelSet**](../Model/ModelSet.md)| ModelSet |

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Update information about the permission set with a specific id.

#### Example

#### Parameters

**body** | [**\Swagger\Client\Model\PermissionSet**](../Model/PermissionSet.md)| Permission Set |

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Update information about the role with a specific id.

#### Example

#### Parameters

**body** | [**\Swagger\Client\Model\Role**](../Model/Role.md)| Role |

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

### SessionApi

#### Get API Session  Returns information about the current API session, such as which workspace is selected for the session.

#### Example

#### Parameters

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Update API Session  #### API Session Workspace  You can use this endpoint to change the active workspace for the current API session.  Only one workspace can be active in a session. The active workspace can be changed any number of times in a session.  The default workspace for API sessions is the \"production\" workspace.  All Looker APIs that use projects or lookml models (such as running queries) will use the version of project and model files defined by this workspace for the lifetime of the current API session or until the session workspace is changed again.  An API session has the same lifetime as the access_token used to authenticate API requests. Each successful API login generates a new access_token and a new API session.  If your Looker API client application needs to work in a dev workspace across multiple API sessions, be sure to select the dev workspace after each login.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

### ColorCollectionApi

#### Get an array of all existing Color Collections Get a **single** color collection by id with [ColorCollection](#!/ColorCollection/color_collection)  Get all **standard** color collections with [ColorCollection](#!/ColorCollection/color_collections_standard)  Get all **custom** color collections with [ColorCollection](#!/ColorCollection/color_collections_custom)  **Note**: Only an API user with the Admin role can call this endpoint. Unauthorized requests will return `Not Found` (404) errors.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get a Color Collection by ID  Use this to retrieve a specific Color Collection. Get a **single** color collection by id with [ColorCollection](#!/ColorCollection/color_collection)  Get all **standard** color collections with [ColorCollection](#!/ColorCollection/color_collections_standard)  Get all **custom** color collections with [ColorCollection](#!/ColorCollection/color_collections_custom)  **Note**: Only an API user with the Admin role can call this endpoint. Unauthorized requests will return `Not Found` (404) errors.

#### Example

#### Parameters

**fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get an array of all existing **Custom** Color Collections Get a **single** color collection by id with [ColorCollection](#!/ColorCollection/color_collection)  Get all **standard** color collections with [ColorCollection](#!/ColorCollection/color_collections_standard)  **Note**: Only an API user with the Admin role can call this endpoint. Unauthorized requests will return `Not Found` (404) errors.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get an array of all existing **Standard** Color Collections Get a **single** color collection by id with [ColorCollection](#!/ColorCollection/color_collection)  Get all **custom** color collections with [ColorCollection](#!/ColorCollection/color_collections_custom)  **Note**: Only an API user with the Admin role can call this endpoint. Unauthorized requests will return `Not Found` (404) errors.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Create a custom color collection with the specified information  Creates a new custom color collection object, returning the details, including the created id.  **Update** an existing color collection with [Update Color Collection](#!/ColorCollection/update_color_collection)  **Permanently delete** an existing custom color collection with [Delete Color Collection](#!/ColorCollection/delete_color_collection)  **Note**: Only an API user with the Admin role can call this endpoint. Unauthorized requests will return `Not Found` (404) errors.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get the default color collection  Use this to retrieve the default Color Collection.  Set the default color collection with [ColorCollection](#!/ColorCollection/set_default_color_collection)

#### Example

#### Parameters

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Delete a custom color collection by id  This operation permanently deletes the identified **Custom** color collection.  **Standard** color collections cannot be deleted  Because multiple color collections can have the same label, they must be deleted by ID, not name. **Note**: Only an API user with the Admin role can call this endpoint. Unauthorized requests will return `Not Found` (404) errors.

#### Example

#### Parameters

#

#### Return type

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Set the global default Color Collection by ID  Returns the new specified default Color Collection object. **Note**: Only an API user with the Admin role can call this endpoint. Unauthorized requests will return `Not Found` (404) errors.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Update a custom color collection by id. **Note**: Only an API user with the Admin role can call this endpoint. Unauthorized requests will return `Not Found` (404) errors.

#### Example

#### Parameters

**body** | [**\Swagger\Client\Model\ColorCollection**](../Model/ColorCollection.md)| ColorCollection |

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

### BoardApi

#### Get information about all board items.

#### Example

#### Parameters

**sorts** | **string**| Fields to sort by. | [optional]
 **board_section_id** | **string**| Filter to a specific board section | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get information about all board sections.

#### Example

#### Parameters

**sorts** | **string**| Fields to sort by. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get information about all boards.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get information about a board.

#### Example

#### Parameters

**fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get information about a board item.

#### Example

#### Parameters

**fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get information about a board section.

#### Example

#### Parameters

**fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Create a new board.

#### Example

#### Parameters

**fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Create a new board item.

#### Example

#### Parameters

**fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Create a new board section.

#### Example

#### Parameters

**fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Delete a board.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Delete a board item.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Delete a board section.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Search Boards  If multiple search params are given and `filter_or` is FALSE or not specified, search params are combined in a logical AND operation. Only rows that match *all* search param criteria will be returned.  If `filter_or` is TRUE, multiple search params are combined in a logical OR operation. Results will include rows that match **any** of the search criteria.  String search params use case-insensitive matching. String search params can contain `%` and '_' as SQL LIKE pattern match wildcard expressions. example=\"dan%\" will match \"danger\" and \"Danzig\" but not \"David\" example=\"D_m%\" will match \"Damage\" and \"dump\"  Integer search params can accept a single value or a comma separated list of values. The multiple values will be combined under a logical OR operation - results will match at least one of the given values.  Most search params can accept \"IS NULL\" and \"NOT NULL\" as special expressions to match or exclude (respectively) rows where the column is null.  Boolean search params accept only \"true\" and \"false\" as values.

#### Example

#### Parameters

**created_at** | **string**| Matches the timestamp for when the board was created. | [optional]
 **first_name** | **string**| The first name of the user who created this board. | [optional]
 **last_name** | **string**| The last name of the user who created this board. | [optional]
 **fields** | **string**| Requested fields. | [optional]
 **favorited** | **bool**| Return favorited boards when true. | [optional]
 **creator_id** | **string**| Filter on boards created by a particular user. | [optional]
 **sorts** | **string**| The fields to sort the results by | [optional]
 **page** | **int**| The page to return. DEPRECATED. Use offset instead. | [optional]
 **per_page** | **int**| The number of items in the returned page. DEPRECATED. Use limit instead. | [optional]
 **offset** | **int**| The number of items to skip before returning any. (used with limit and takes priority over page and per_page) | [optional]
 **limit** | **int**| The maximum number of items to return. (used with offset and takes priority over page and per_page) | [optional]
 **filter_or** | **bool**| Combine given search criteria in a boolean OR expression | [optional]
 **permission** | **string**| Filter results based on permission, either show (default) or update | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Update a board definition.

#### Example

#### Parameters

**body** | [**\Swagger\Client\Model\Board**](../Model/Board.md)| Board |
 **fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Update a board item definition.

#### Example

#### Parameters

**body** | [**\Swagger\Client\Model\BoardItem**](../Model/BoardItem.md)| Board Item |
 **fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Update a board section definition.

#### Example

#### Parameters

**body** | [**\Swagger\Client\Model\BoardSection**](../Model/BoardSection.md)| Board section |
 **fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

### LookmlModelApi

#### Get information about all lookml models.

#### Example

#### Parameters

**limit** | **int**| Number of results to return. (can be used with offset) | [optional]
 **offset** | **int**| Number of results to skip before returning any. (Defaults to 0 if not set when limit is used) | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Create a lookml model using the specified configuration.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Delete a lookml model.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get information about a lookml model.

#### Example

#### Parameters

**fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get information about a lookml model explore.

#### Example

#### Parameters

**explore_name** | **string**| Name of explore. |
 **fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Update a lookml model using the specified configuration.

#### Example

#### Parameters

**body** | [**\Swagger\Client\Model\LookmlModel**](../Model/LookmlModel.md)| LookML Model |

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

### ApiAuthApi

#### Present client credentials to obtain an authorization token  Looker API implements the OAuth2 [Resource Owner Password Credentials Grant](https://cloud.google.com/looker/docs/r/api/outh2_resource_owner_pc) pattern. The client credentials required for this login must be obtained by creating an API key on a user account in the Looker Admin console. The API key consists of a public `client_id` and a private `client_secret`.  The access token returned by `login` must be used in the HTTP Authorization header of subsequent API requests, like this: ``` Authorization: token 4QDkCyCtZzYgj4C2p2cj3csJH7zqS5RzKs2kTnG4 ``` Replace \"4QDkCy...\" with the `access_token` value returned by `login`. The word `token` is a string literal and must be included exactly as shown.  This function can accept `client_id` and `client_secret` parameters as URL query params or as www-form-urlencoded params in the body of the HTTP request. Since there is a small risk that URL parameters may be visible to intermediate nodes on the network route (proxies, routers, etc), passing credentials in the body of the request is considered more secure than URL params.  Example of passing credentials in the HTTP request body: ```` POST HTTP /login Content-Type: application/x-www-form-urlencoded  client_id=CGc9B7v7J48dQSJvxxx&client_secret=nNVS9cSS3xNpSC9JdsBvvvvv ````  ### Best Practice: Always pass credentials in body params. Pass credentials in URL query params **only** when you cannot pass body params due to application, tool, or other limitations.  For more information and detailed examples of Looker API authorization, see [How to Authenticate to Looker API](https://github.com/looker/looker-sdk-ruby/blob/master/authentication.md).

#### Example

#### Parameters

**client_secret** | **string**| client_secret part of API Key. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Create an access token that runs as a given user.  This can only be called by an authenticated admin user. It allows that admin to generate a new authentication token for the user with the given user id. That token can then be used for subsequent API calls - which are then performed *as* that target user.  The target user does *not* need to have a pre-existing API client_id/client_secret pair. And, no such credentials are created by this call.  This allows for building systems where api user authentication for an arbitrary number of users is done outside of Looker and funneled through a single 'service account' with admin permissions. Note that a new access token is generated on each call. If target users are going to be making numerous API calls in a short period then it is wise to cache this authentication token rather than call this before each of those API calls.  See 'login' for more detail on the access token and how to use it.

#### Example

#### Parameters

**associative** | **bool**| When true (default), API calls using the returned access_token are attributed to the admin user who created the access_token. When false, API activity is attributed to the user the access_token runs as. False requires a looker license. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Logout of the API and invalidate the current access token.

#### Example

#### Parameters

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

### ThemeApi

#### Get active themes  Returns an array of active themes.  If the `name` parameter is specified, it will return an array with one theme if it's active and found.  The optional `ts` parameter can specify a different timestamp than \"now.\"  **Note**: Custom themes needs to be enabled by Looker. Unless custom themes are enabled, only the automatically generated default theme can be used. Please contact your Account Manager or help.looker.com to update your license for this feature.

#### Example

#### Parameters

**ts** | **\DateTime**| Timestamp representing the target datetime for the active period. Defaults to &#39;now&#39; | [optional]
 **fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get an array of all existing themes  Get a **single theme** by id with [Theme](#!/Theme/theme)  This method returns an array of all existing themes. The active time for the theme is not considered.  **Note**: Custom themes needs to be enabled by Looker. Unless custom themes are enabled, only the automatically generated default theme can be used. Please contact your Account Manager or help.looker.com to update your license for this feature.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Create a theme  Creates a new theme object, returning the theme details, including the created id.  If `settings` are not specified, the default theme settings will be copied into the new theme.  The theme `name` can only contain alphanumeric characters or underscores. Theme names should not contain any confidential information, such as customer names.  **Update** an existing theme with [Update Theme](#!/Theme/update_theme)  **Permanently delete** an existing theme with [Delete Theme](#!/Theme/delete_theme)  For more information, see [Creating and Applying Themes](https://cloud.google.com/looker/docs/r/admin/themes).  **Note**: Custom themes needs to be enabled by Looker. Unless custom themes are enabled, only the automatically generated default theme can be used. Please contact your Account Manager or help.looker.com to update your license for this feature.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get the default theme  Returns the active theme object set as the default.  The **default** theme name can be set in the UI on the Admin|Theme UI page  The optional `ts` parameter can specify a different timestamp than \"now.\" If specified, it returns the default theme at the time indicated.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Delete a specific theme by id  This operation permanently deletes the identified theme from the database.  Because multiple themes can have the same name (with different activation time spans) themes can only be deleted by ID.  All IDs associated with a theme name can be retrieved by searching for the theme name with [Theme Search](#!/Theme/search).  **Note**: Custom themes needs to be enabled by Looker. Unless custom themes are enabled, only the automatically generated default theme can be used. Please contact your Account Manager or help.looker.com to update your license for this feature.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Search all themes for matching criteria.  Returns an **array of theme objects** that match the specified search criteria.  | Search Parameters | Description | :-------------------: | :------ | | `begin_at` only | Find themes active at or after `begin_at` | `end_at` only | Find themes active at or before `end_at` | both set | Find themes with an active inclusive period between `begin_at` and `end_at`  Note: Range matching requires boolean AND logic. When using `begin_at` and `end_at` together, do not use `filter_or`=TRUE  If multiple search params are given and `filter_or` is FALSE or not specified, search params are combined in a logical AND operation. Only rows that match *all* search param criteria will be returned.  If `filter_or` is TRUE, multiple search params are combined in a logical OR operation. Results will include rows that match **any** of the search criteria.  String search params use case-insensitive matching. String search params can contain `%` and '_' as SQL LIKE pattern match wildcard expressions. example=\"dan%\" will match \"danger\" and \"Danzig\" but not \"David\" example=\"D_m%\" will match \"Damage\" and \"dump\"  Integer search params can accept a single value or a comma separated list of values. The multiple values will be combined under a logical OR operation - results will match at least one of the given values.  Most search params can accept \"IS NULL\" and \"NOT NULL\" as special expressions to match or exclude (respectively) rows where the column is null.  Boolean search params accept only \"true\" and \"false\" as values.   Get a **single theme** by id with [Theme](#!/Theme/theme)  **Note**: Custom themes needs to be enabled by Looker. Unless custom themes are enabled, only the automatically generated default theme can be used. Please contact your Account Manager or help.looker.com to update your license for this feature.

#### Example

#### Parameters

**name** | **string**| Match theme name. | [optional]
 **begin_at** | **\DateTime**| Timestamp for activation. | [optional]
 **end_at** | **\DateTime**| Timestamp for expiration. | [optional]
 **limit** | **int**| Number of results to return (used with &#x60;offset&#x60;). | [optional]
 **offset** | **int**| Number of results to skip before returning any (used with &#x60;limit&#x60;). | [optional]
 **sorts** | **string**| Fields to sort by. | [optional]
 **fields** | **string**| Requested fields. | [optional]
 **filter_or** | **bool**| Combine given search criteria in a boolean OR expression | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Set the global default theme by theme name  Only Admin users can call this function.  Only an active theme with no expiration (`end_at` not set) can be assigned as the default theme. As long as a theme has an active record with no expiration, it can be set as the default.  [Create Theme](#!/Theme/create) has detailed information on rules for default and active themes  Returns the new specified default theme object.  **Note**: Custom themes needs to be enabled by Looker. Unless custom themes are enabled, only the automatically generated default theme can be used. Please contact your Account Manager or help.looker.com to update your license for this feature.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get a theme by ID  Use this to retrieve a specific theme, whether or not it's currently active.  **Note**: Custom themes needs to be enabled by Looker. Unless custom themes are enabled, only the automatically generated default theme can be used. Please contact your Account Manager or help.looker.com to update your license for this feature.

#### Example

#### Parameters

**fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get the named theme if it's active. Otherwise, return the default theme  The optional `ts` parameter can specify a different timestamp than \"now.\" Note: API users with `show` ability can call this function  **Note**: Custom themes needs to be enabled by Looker. Unless custom themes are enabled, only the automatically generated default theme can be used. Please contact your Account Manager or help.looker.com to update your license for this feature.

#### Example

#### Parameters

**ts** | **\DateTime**| Timestamp representing the target datetime for the active period. Defaults to &#39;now&#39; | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Update the theme by id.  **Note**: Custom themes needs to be enabled by Looker. Unless custom themes are enabled, only the automatically generated default theme can be used. Please contact your Account Manager or help.looker.com to update your license for this feature.

#### Example

#### Parameters

**body** | [**\Swagger\Client\Model\Theme**](../Model/Theme.md)| Theme |

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Validate a theme with the specified information  Validates all values set for the theme, returning any errors encountered, or 200 OK if valid  See [Create Theme](#!/Theme/create_theme) for constraints  **Note**: Custom themes needs to be enabled by Looker. Unless custom themes are enabled, only the automatically generated default theme can be used. Please contact your Account Manager or help.looker.com to update your license for this feature.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

### ArtifactApi

#### Get one or more artifacts  Returns an array of artifacts matching the specified key value(s).  **Note**: The artifact storage API can only be used by Looker-built extensions.

#### Example

#### Parameters

**key** | **string**| Comma-delimited list of keys. Wildcards not allowed. |
 **fields** | **string**| Comma-delimited names of fields to return in responses. Omit for all fields | [optional]
 **limit** | **int**| Number of results to return. (used with offset) | [optional]
 **offset** | **int**| Number of results to skip before returning any. (used with limit) | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Example

#### Parameters

**limit** | **int**| Number of results to return. (used with offset) | [optional]
 **offset** | **int**| Number of results to skip before returning any. (used with limit) | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Return the value of an artifact  The MIME type for the API response is set to the `content_type` of the value  **Note**: The artifact storage API can only be used by Looker-built extensions.

#### Example

#### Parameters

**key** | **string**| Artifact storage key. Namespace + Key must be unique | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Delete one or more artifacts  To avoid rate limiting on deletion requests, multiple artifacts can be deleted at the same time by using a comma-delimited list of artifact keys.  **Note**: The artifact storage API can only be used by Looker-built extensions.

#### Example

#### Parameters

**key** | **string**| Comma-delimited list of keys. Wildcards not allowed. |

#### Return type

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Example

#### Parameters

#

#### Return type

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Search all key/value pairs in a namespace for matching criteria.  Returns an array of artifacts matching the specified search criteria.  Key search patterns use case-insensitive matching and can contain `%` and `_` as SQL LIKE pattern match wildcard expressions.  The parameters `min_size` and `max_size` can be used individually or together.  - `min_size` finds artifacts with sizes greater than or equal to its value - `max_size` finds artifacts with sizes less than or equal to its value - using both parameters restricts the minimum and maximum size range for artifacts  **NOTE**: Artifacts are always returned in alphanumeric order by key.  Get a **single artifact** by namespace and key with [`artifact`](#!/Artifact/artifact)  **Note**: The artifact storage API can only be used by Looker-built extensions.

#### Example

#### Parameters

**fields** | **string**| Comma-delimited names of fields to return in responses. Omit for all fields | [optional]
 **key** | **string**| Key pattern to match | [optional]
 **user_ids** | **string**| Ids of users who created or updated the artifact (comma-delimited list) | [optional]
 **min_size** | **int**| Minimum storage size of the artifact | [optional]
 **max_size** | **int**| Maximum storage size of the artifact | [optional]
 **limit** | **int**| Number of results to return. (used with offset) | [optional]
 **offset** | **int**| Number of results to skip before returning any. (used with limit) | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Create or update one or more artifacts  Only `key` and `value` are required to _create_ an artifact. To _update_ an artifact, its current `version` value must be provided.  In the following example `body` payload, `one` and `two` are existing artifacts, and `three` is new:  ```json [   { \"key\": \"one\", \"value\": \"[ \\\"updating\\\", \\\"existing\\\", \\\"one\\\" ]\", \"version\": 10, \"content_type\": \"application/json\" },   { \"key\": \"two\", \"value\": \"updating existing two\", \"version\": 20 },   { \"key\": \"three\", \"value\": \"creating new three\" }, ] ```  Notes for this body:  - The `value` for `key` **one** is a JSON payload, so a `content_type` override is needed. This override must be done **every** time a JSON value is set. - The `version` values for **one** and **two** mean they have been saved 10 and 20 times, respectively. - If `version` is **not** provided for an existing artifact, the entire request will be refused and a `Bad Request` response will be sent. - If `version` is provided for an artifact, it is only used for helping to prevent inadvertent data overwrites. It cannot be used to **set** the version of an artifact. The Looker server controls `version`. - We suggest encoding binary values as base64. Because the MIME content type for base64 is detected as plain text, also provide `content_type` to correctly indicate the value's type for retrieval and client-side processing.  Because artifacts are stored encrypted, the same value can be written multiple times (provided the correct `version` number is used). Looker does not examine any values stored in the artifact store, and only decrypts when sending artifacts back in an API response.  **Note**: The artifact storage API can only be used by Looker-built extensions.

#### Example

#### Parameters

**body** | [**\Swagger\Client\Model\UpdateArtifact[]**](../Model/UpdateArtifact.md)| Artifacts to create or update |
 **fields** | **string**| Comma-delimited names of fields to return in responses. Omit for all fields | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

### DatagroupApi

#### Get information about all datagroups.

#### Example

#### Parameters

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get information about a datagroup.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Update a datagroup using the specified params.

#### Example

#### Parameters

**body** | [**\Swagger\Client\Model\Datagroup**](../Model/Datagroup.md)| Datagroup |

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

### ProjectApi

#### Get All Git Branches  Returns a list of git branches in the project repository

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get All Git Connection Tests  dev mode required.   - Call `update_session` to select the 'dev' workspace.  Returns a list of tests which can be run against a project's (or the dependency project for the provided remote_url) git connection. Call [Run Git Connection Test](#!/Project/run_git_connection_test) to execute each test in sequence.  Tests are ordered by increasing specificity. Tests should be run in the order returned because later tests require functionality tested by tests earlier in the test list.  For example, a late-stage test for write access is meaningless if connecting to the git server (an early test) is failing.

#### Example

#### Parameters

**remote_url** | **string**| (Optional: leave blank for root project) The remote url for remote dependency to test. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get All LookML Tests  Returns a list of tests which can be run to validate a project's LookML code and/or the underlying data, optionally filtered by the file id. Call [Run LookML Test](#!/Project/run_lookml_test) to execute tests.

#### Example

#### Parameters

**file_id** | **string**| File Id | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get All Project Files  Returns a list of the files in the project

#### Example

#### Parameters

**fields** | **string**| Requested fields | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get All Projects  Returns all projects visible to the current user

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Create and Checkout a Git Branch  Creates and checks out a new branch in the given project repository Only allowed in development mode   - Call `update_session` to select the 'dev' workspace.  Optionally specify a branch name, tag name or commit SHA as the start point in the ref field.   If no ref is specified, HEAD of the current branch will be used as the start point for the new branch.

#### Example

#### Parameters

**body** | [**\Swagger\Client\Model\GitBranch**](../Model/GitBranch.md)| Git Branch |

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Create Git Deploy Key  Create a public/private key pair for authenticating ssh git requests from Looker to a remote git repository for a particular Looker project.  Returns the public key of the generated ssh key pair.  Copy this public key to your remote git repository's ssh keys configuration so that the remote git service can validate and accept git requests from the Looker server.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: text/plain

#### Create A Project  dev mode required. - Call `update_session` to select the 'dev' workspace.  `name` is required. `git_remote_url` is not allowed. To configure Git for the newly created project, follow the instructions in `update_project`.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Delete the specified Git Branch  Delete git branch specified in branch_name path param from local and remote of specified project repository

#### Example

#### Parameters

**branch_name** | **string**| Branch Name |

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Repository Credential for a remote dependency  Admin required.  `root_project_id` is required. `credential_id` is required.

#### Example

#### Parameters

**credential_id** | **string**| Credential Id |

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Deploy a Remote Branch or Ref to Production  Git must have been configured and deploy permission required.  Deploy is a one/two step process 1. If this is the first deploy of this project, create the production project with git repository. 2. Pull the branch or ref into the production project.  Can only specify either a branch or a ref.

#### Example

#### Parameters

**branch** | **string**| Branch to deploy to production | [optional]
 **ref** | **string**| Ref to deploy to production | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Deploy LookML from this Development Mode Project to Production  Git must have been configured, must be in dev mode and deploy permission required  Deploy is a two / three step process:  1. Push commits in current branch of dev mode project to the production branch (origin/master).    Note a. This step is skipped in read-only projects.    Note b. If this step is unsuccessful for any reason (e.g. rejected non-fastforward because production branch has              commits not in current branch), subsequent steps will be skipped. 2. If this is the first deploy of this project, create the production project with git repository. 3. Pull the production branch into the production project.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get the specified Git Branch  Returns the git branch specified in branch_name path param if it exists in the given project repository

#### Example

#### Parameters

**branch_name** | **string**| Branch Name |

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get all Repository Credentials for a project  `root_project_id` is required.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get the Current Git Branch  Returns the git branch currently checked out in the given project repository

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Git Deploy Key  Returns the ssh public key previously created for a project's git repository.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: text/plain

#### Generate Lockfile for All LookML Dependencies        Git must have been configured, must be in dev mode and deploy permission required        Install_all is a two step process       1. For each remote_dependency in a project the dependency manager will resolve any ambiguous ref.       2. The project will then write out a lockfile including each remote_dependency with its resolved ref.

#### Example

#### Parameters

**fields** | **string**| Requested fields | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get A Projects Manifest object  Returns the project with the given project id

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get A Project  Returns the project with the given project id

#### Example

#### Parameters

**fields** | **string**| Requested fields | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get Project File Info  Returns information about a file in the project

#### Example

#### Parameters

**file_id** | **string**| File Id |
 **fields** | **string**| Requested fields | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get Cached Project Validation Results  Returns the cached results of a previous project validation calculation, if any. Returns http status 204 No Content if no validation results exist.  Validating the content of all the files in a project can be computationally intensive for large projects. Use this API to simply fetch the results of the most recent project validation rather than revalidating the entire project from scratch.  A value of `\"stale\": true` in the response indicates that the project has changed since the cached validation results were computed. The cached validation results may no longer reflect the current state of the project.

#### Example

#### Parameters

**fields** | **string**| Requested fields | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get Project Workspace  Returns information about the state of the project files in the currently selected workspace

#### Example

#### Parameters

**fields** | **string**| Requested fields | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Reset a project to the revision of the project that is in production.  **DANGER** this will delete any changes that have not been pushed to a remote repository.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Reset a project development branch to the revision of the project that is on the remote.  **DANGER** this will delete any changes that have not been pushed to a remote repository.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Run a git connection test  Run the named test on the git service used by this project (or the dependency project for the provided remote_url) and return the result. This is intended to help debug git connections when things do not work properly, to give more helpful information about why a git url is not working with Looker.  Tests should be run in the order they are returned by [Get All Git Connection Tests](#!/Project/all_git_connection_tests).

#### Example

#### Parameters

**test_id** | **string**| Test Id |
 **remote_url** | **string**| (Optional: leave blank for root project) The remote url for remote dependency to test. | [optional]
 **use_production** | **string**| (Optional: leave blank for dev credentials) Whether to use git production credentials. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Run LookML Tests  Runs all tests in the project, optionally filtered by file, test, and/or model.

#### Example

#### Parameters

**file_id** | **string**| File Name | [optional]
 **test** | **string**| Test Name | [optional]
 **model** | **string**| Model Name | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Creates a tag for the most recent commit, or a specific ref is a SHA is provided  This is an internal-only, undocumented route.

#### Example

#### Parameters

**body** | [**\Swagger\Client\Model\Project**](../Model/Project.md)| Project |
 **commit_sha** | **string**| (Optional): Commit Sha to Tag | [optional]
 **tag_name** | **string**| Tag Name | [optional]
 **tag_message** | **string**| (Optional): Tag Message | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Checkout and/or reset --hard an existing Git Branch  Only allowed in development mode   - Call `update_session` to select the 'dev' workspace.  Checkout an existing branch if name field is different from the name of the currently checked out branch.  Optionally specify a branch name, tag name or commit SHA to which the branch should be reset.   **DANGER** hard reset will be force pushed to the remote. Unsaved changes and commits may be permanently lost.

#### Example

#### Parameters

**body** | [**\Swagger\Client\Model\GitBranch**](../Model/GitBranch.md)| Git Branch |

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Update Project Configuration  Apply changes to a project's configuration.   #### Configuring Git for a Project  To set up a Looker project with a remote git repository, follow these steps:  1. Call `update_session` to select the 'dev' workspace. 1. Call `create_git_deploy_key` to create a new deploy key for the project 1. Copy the deploy key text into the remote git repository's ssh key configuration 1. Call `update_project` to set project's `git_remote_url` ()and `git_service_name`, if necessary).  When you modify a project's `git_remote_url`, Looker connects to the remote repository to fetch metadata. The remote git repository MUST be configured with the Looker-generated deploy key for this project prior to setting the project's `git_remote_url`.  To set up a Looker project with a git repository residing on the Looker server (a 'bare' git repo):  1. Call `update_session` to select the 'dev' workspace. 1. Call `update_project` setting `git_remote_url` to null and `git_service_name` to \"bare\".

#### Example

#### Parameters

**body** | [**\Swagger\Client\Model\Project**](../Model/Project.md)| Project |
 **fields** | **string**| Requested fields | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Configure Repository Credential for a remote dependency  Admin required.  `root_project_id` is required. `credential_id` is required.

#### Example

#### Parameters

**credential_id** | **string**| Credential Id |
 **body** | [**\Swagger\Client\Model\RepositoryCredential**](../Model/RepositoryCredential.md)| Remote Project Information |

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Validate Project  Performs lint validation of all lookml files in the project. Returns a list of errors found, if any.  Validating the content of all the files in a project can be computationally intensive for large projects. For best performance, call `validate_project(project_id)` only when you really want to recompute project validation. To quickly display the results of the most recent project validation (without recomputing), use `project_validation_results(project_id)`

#### Example

#### Parameters

**fields** | **string**| Requested fields | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

### HomepageApi

#### Get information about the primary homepage's sections.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

### DerivedTableApi

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Discover information about derived tables

#### Example

#### Parameters

**format** | **string**| The format of the graph. Valid values are [dot]. Default is &#x60;dot&#x60; | [optional]
 **color** | **string**| Color denoting the build status of the graph. Grey &#x3D; not built, green &#x3D; built, yellow &#x3D; building, red &#x3D; error. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get the subgraph representing this derived table and its dependencies.

#### Example

#### Parameters

**models** | **string**| The models where this derived table is defined. | [optional]
 **workspace** | **string**| The model directory to look in, either &#x60;dev&#x60; or &#x60;production&#x60;. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Example

#### Parameters

**view_name** | **string**| The view name of the PDT to start building. |
 **force_rebuild** | **string**| Force rebuild of required dependent PDTs, even if they are already materialized. | [optional]
 **force_full_incremental** | **string**| Force involved incremental PDTs to fully re-materialize. | [optional]
 **workspace** | **string**| Workspace in which to materialize selected PDT (&#39;dev&#39; or default &#39;production&#39;). | [optional]
 **source** | **string**| The source of this request. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Example

#### Parameters

**source** | **string**| The source of this request. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

### UserAttributeApi

#### Returns all values of a user attribute defined by user groups, in precedence order.  A user may be a member of multiple groups which define different values for a given user attribute. The order of group-values in the response determines precedence for selecting which group-value applies to a given user.  For more information, see [Set User Attribute Group Values](#!/UserAttribute/set_user_attribute_group_values).  Results will only include groups that the caller's user account has permission to see.

#### Example

#### Parameters

**fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get information about all user attributes.

#### Example

#### Parameters

**sorts** | **string**| Fields to order the results by. Sortable fields include: name, label | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Create a new user attribute  Permission information for a user attribute is conveyed through the `can` and `user_can_edit` fields. The `user_can_edit` field indicates whether an attribute is user-editable _anywhere_ in the application. The `can` field gives more granular access information, with the `set_value` child field indicating whether an attribute's value can be set by [Setting the User Attribute User Value](#!/User/set_user_attribute_user_value).  Note: `name` and `label` fields must be unique across all user attributes in the Looker instance. Attempting to create a new user attribute with a name or label that duplicates an existing user attribute will fail with a 422 error.

#### Example

#### Parameters

**fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Delete a user attribute (admin only).

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Define values for a user attribute across a set of groups, in priority order.  This function defines all values for a user attribute defined by user groups. This is a global setting, potentially affecting all users in the system. This function replaces any existing group value definitions for the indicated user attribute.  The value of a user attribute for a given user is determined by searching the following locations, in this order:  1. the user's account settings 2. the groups that the user is a member of 3. the default value of the user attribute, if any  The user may be a member of multiple groups which define different values for that user attribute. The order of items in the group_values parameter determines which group takes priority for that user. Lowest array index wins.  An alternate method to indicate the selection precedence of group-values is to assign numbers to the 'rank' property of each group-value object in the array. Lowest 'rank' value wins. If you use this technique, you must assign a rank value to every group-value object in the array.    To set a user attribute value for a single user, see [Set User Attribute User Value](#!/User/set_user_attribute_user_value). To set a user attribute value for all members of a group, see [Set User Attribute Group Value](#!/Group/update_user_attribute_group_value).

#### Example

#### Parameters

**body** | [**\Swagger\Client\Model\UserAttributeGroupValue[]**](../Model/UserAttributeGroupValue.md)| Array of group values. |

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Update a user attribute definition.

#### Example

#### Parameters

**body** | [**\Swagger\Client\Model\UserAttribute**](../Model/UserAttribute.md)| User Attribute |
 **fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get information about a user attribute.

#### Example

#### Parameters

**fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

### ContentApi

#### All content metadata access records for a content metadata item.

#### Example

#### Parameters

**fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get information about all content metadata in a space.

#### Example

#### Parameters

**fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get favorite content by its id

#### Example

#### Parameters

**fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get information about an individual content metadata record.

#### Example

#### Parameters

**fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get an image representing the contents of a dashboard or look.  The returned thumbnail is an abstract representation of the contents of a dashbord or look and does not reflect the actual data displayed in the respective visualizations.

#### Example

#### Parameters

**resource_id** | **string**| ID of the dashboard or look to render |
 **reload** | **string**| Whether or not to refresh the rendered image with the latest content | [optional]
 **theme** | **string**| Light or dark background. Default is \&quot;light\&quot; | [optional]
 **format** | **string**| A value of png produces a thumbnail in PNG format instead of SVG (default) | [optional]
 **width** | **int**| The width of the image if format is supplied | [optional]
 **height** | **int**| The height of the image if format is supplied | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: image/svg+xml, image/png

#### Validate All Content  Performs validation of all looks and dashboards Returns a list of errors found as well as metadata about the content validation run.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Create favorite content

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Create content metadata access.

#### Example

#### Parameters

**send_boards_notification_email** | **bool**| Optionally sends notification email when granting access to a board. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Delete favorite content

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Remove content metadata access.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Search across looks, dashboards, and lookml dashboards. The terms field will be matched against the title and description of the content and the closest results are returned. Content that has been frequently viewed and those pieces of content stored in public folders will be ranked more highly in the results.  This endpoint does not return a full description of these content types. For more specific information about each type please refer to the individual content specific API endpoints.  Get the **full details** of a specific dashboard (or lookml dashboard) by id with [dashboard()](#!/Dashboard/dashboard) Get the **full details** of a specific look by id with [look()](#!/Look/look)

#### Example

#### Parameters

**fields** | **string**| Requested fields. | [optional]
 **types** | **string**| Content types requested (dashboard, look, lookml_dashboard). | [optional]
 **limit** | **int**| Number of results to return. (used with offset and takes priority over page and per_page) | [optional]
 **offset** | **int**| Number of results to skip before returning any. (used with limit and takes priority over page and per_page) | [optional]
 **page** | **int**| Requested page. | [optional]
 **per_page** | **int**| Results per page. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Search Favorite Content  If multiple search params are given and `filter_or` is FALSE or not specified, search params are combined in a logical AND operation. Only rows that match *all* search param criteria will be returned.  If `filter_or` is TRUE, multiple search params are combined in a logical OR operation. Results will include rows that match **any** of the search criteria.  String search params use case-insensitive matching. String search params can contain `%` and '_' as SQL LIKE pattern match wildcard expressions. example=\"dan%\" will match \"danger\" and \"Danzig\" but not \"David\" example=\"D_m%\" will match \"Damage\" and \"dump\"  Integer search params can accept a single value or a comma separated list of values. The multiple values will be combined under a logical OR operation - results will match at least one of the given values.  Most search params can accept \"IS NULL\" and \"NOT NULL\" as special expressions to match or exclude (respectively) rows where the column is null.  Boolean search params accept only \"true\" and \"false\" as values.

#### Example

#### Parameters

**user_id** | **string**| Match user id(s).To create a list of multiple ids, use commas as separators | [optional]
 **content_metadata_id** | **string**| Match content metadata id(s).To create a list of multiple ids, use commas as separators | [optional]
 **dashboard_id** | **string**| Match dashboard id(s).To create a list of multiple ids, use commas as separators | [optional]
 **look_id** | **string**| Match look id(s).To create a list of multiple ids, use commas as separators | [optional]
 **board_id** | **string**| Match board id(s).To create a list of multiple ids, use commas as separators | [optional]
 **limit** | **int**| Number of results to return. (used with offset) | [optional]
 **offset** | **int**| Number of results to skip before returning any. (used with limit) | [optional]
 **sorts** | **string**| Fields to sort by. | [optional]
 **fields** | **string**| Requested fields. | [optional]
 **filter_or** | **bool**| Combine given search criteria in a boolean OR expression | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Search Content Views  If multiple search params are given and `filter_or` is FALSE or not specified, search params are combined in a logical AND operation. Only rows that match *all* search param criteria will be returned.  If `filter_or` is TRUE, multiple search params are combined in a logical OR operation. Results will include rows that match **any** of the search criteria.  String search params use case-insensitive matching. String search params can contain `%` and '_' as SQL LIKE pattern match wildcard expressions. example=\"dan%\" will match \"danger\" and \"Danzig\" but not \"David\" example=\"D_m%\" will match \"Damage\" and \"dump\"  Integer search params can accept a single value or a comma separated list of values. The multiple values will be combined under a logical OR operation - results will match at least one of the given values.  Most search params can accept \"IS NULL\" and \"NOT NULL\" as special expressions to match or exclude (respectively) rows where the column is null.  Boolean search params accept only \"true\" and \"false\" as values.

#### Example

#### Parameters

**group_id** | **string**| Match Group Id | [optional]
 **look_id** | **string**| Match look_id | [optional]
 **dashboard_id** | **string**| Match dashboard_id | [optional]
 **content_metadata_id** | **string**| Match content metadata id | [optional]
 **start_of_week_date** | **string**| Match start of week date (format is \&quot;YYYY-MM-DD\&quot;) | [optional]
 **all_time** | **bool**| True if only all time view records should be returned | [optional]
 **user_id** | **string**| Match user id | [optional]
 **fields** | **string**| Requested fields | [optional]
 **limit** | **int**| Number of results to return. Use with &#x60;offset&#x60; to manage pagination of results | [optional]
 **offset** | **int**| Number of results to skip before returning data | [optional]
 **sorts** | **string**| Fields to sort by | [optional]
 **filter_or** | **bool**| Combine given search criteria in a boolean OR expression | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Move a piece of content.

#### Example

#### Parameters

**body** | [**\Swagger\Client\Model\ContentMeta**](../Model/ContentMeta.md)| Content Metadata |

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Update type of access for content metadata.

#### Example

#### Parameters

**body** | [**\Swagger\Client\Model\ContentMetaGroupUser**](../Model/ContentMetaGroupUser.md)| Content Metadata Access |

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get a vector image representing the contents of a dashboard or look.  # DEPRECATED:  Use [content_thumbnail()](#!/Content/content_thumbnail)  The returned thumbnail is an abstract representation of the contents of a dashbord or look and does not reflect the actual data displayed in the respective visualizations.

#### Example

#### Parameters

**resource_id** | **string**| ID of the dashboard or look to render |
 **reload** | **string**| Whether or not to refresh the rendered image with the latest content | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: image/svg+xml

### ScheduledPlanApi

#### List All Scheduled Plans  Returns all scheduled plans which belong to the caller or given user.  If no user_id is provided, this function returns the scheduled plans owned by the caller.   To list all schedules for all users, pass `all_users=true`.   The caller must have `see_schedules` permission to see other users' scheduled plans.

#### Example

#### Parameters

**fields** | **string**| Comma delimited list of field names. If provided, only the fields specified will be included in the response | [optional]
 **all_users** | **bool**| Return scheduled plans belonging to all users (caller needs see_schedules permission) | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Create a Scheduled Plan  Create a scheduled plan to render a Look or Dashboard on a recurring schedule.  To create a scheduled plan, you MUST provide values for the following fields: `name` and `look_id`, `dashboard_id`, `lookml_dashboard_id`, or `query_id` and `cron_tab` or `datagroup` and at least one scheduled_plan_destination  A scheduled plan MUST have at least one scheduled_plan_destination defined.  When `look_id` is set, `require_no_results`, `require_results`, and `require_change` are all required.  If `create_scheduled_plan` fails with a 422 error, be sure to look at the error messages in the response which will explain exactly what fields are missing or values that are incompatible.  The queries that provide the data for the look or dashboard are run in the context of user account that owns the scheduled plan.  When `run_as_recipient` is `false` or not specified, the queries that provide the data for the look or dashboard are run in the context of user account that owns the scheduled plan.  When `run_as_recipient` is `true` and all the email recipients are Looker user accounts, the queries are run in the context of each recipient, so different recipients may see different data from the same scheduled render of a look or dashboard. For more details, see [Run As Recipient](https://cloud.google.com/looker/docs/r/admin/run-as-recipient).  Admins can create and modify scheduled plans on behalf of other users by specifying a user id. Non-admin users may not create or modify scheduled plans by or for other users.  #### Email Permissions:  For details about permissions required to schedule delivery to email and the safeguards Looker offers to protect against sending to unauthorized email destinations, see [Email Domain Allow List for Scheduled Looks](https://cloud.google.com/looker/docs/r/api/embed-permissions).   #### Scheduled Plan Destination Formats  Scheduled plan destinations must specify the data format to produce and send to the destination.  Formats:  | format | Description | :-----------: | :--- | | json | A JSON object containing a `data` property which contains an array of JSON objects, one per row. No metadata. | json_detail | Row data plus metadata describing the fields, pivots, table calcs, and other aspects of the query | inline_json | Same as the JSON format, except that the `data` property is a string containing JSON-escaped row data. Additional properties describe the data operation. This format is primarily used to send data to web hooks so that the web hook doesn't have to re-encode the JSON row data in order to pass it on to its ultimate destination. | csv | Comma separated values with a header | txt | Tab separated values with a header | html | Simple html | xlsx | MS Excel spreadsheet | wysiwyg_pdf | Dashboard rendered in a tiled layout to produce a PDF document | assembled_pdf | Dashboard rendered in a single column layout to produce a PDF document | wysiwyg_png | Dashboard rendered in a tiled layout to produce a PNG image ||  Valid formats vary by destination type and source object. `wysiwyg_pdf` is only valid for dashboards, for example.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Delete a Scheduled Plan  Normal users can only delete their own scheduled plans. Admins can delete other users' scheduled plans. This delete cannot be undone.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get Information About a Scheduled Plan  Admins can fetch information about other users' Scheduled Plans.

#### Example

#### Parameters

**fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Run a Scheduled Plan Immediately  Create a scheduled plan that runs only once, and immediately.  This can be useful for testing a Scheduled Plan before committing to a production schedule.  Admins can create scheduled plans on behalf of other users by specifying a user id.  This API is rate limited to prevent it from being used for relay spam or DoS attacks  #### Email Permissions:  For details about permissions required to schedule delivery to email and the safeguards Looker offers to protect against sending to unauthorized email destinations, see [Email Domain Allow List for Scheduled Looks](https://cloud.google.com/looker/docs/r/api/embed-permissions).   #### Scheduled Plan Destination Formats  Scheduled plan destinations must specify the data format to produce and send to the destination.  Formats:  | format | Description | :-----------: | :--- | | json | A JSON object containing a `data` property which contains an array of JSON objects, one per row. No metadata. | json_detail | Row data plus metadata describing the fields, pivots, table calcs, and other aspects of the query | inline_json | Same as the JSON format, except that the `data` property is a string containing JSON-escaped row data. Additional properties describe the data operation. This format is primarily used to send data to web hooks so that the web hook doesn't have to re-encode the JSON row data in order to pass it on to its ultimate destination. | csv | Comma separated values with a header | txt | Tab separated values with a header | html | Simple html | xlsx | MS Excel spreadsheet | wysiwyg_pdf | Dashboard rendered in a tiled layout to produce a PDF document | assembled_pdf | Dashboard rendered in a single column layout to produce a PDF document | wysiwyg_png | Dashboard rendered in a tiled layout to produce a PNG image ||  Valid formats vary by destination type and source object. `wysiwyg_pdf` is only valid for dashboards, for example.

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Run a Scheduled Plan By Id Immediately This function creates a run-once schedule plan based on an existing scheduled plan, applies modifications (if any) to the new scheduled plan, and runs the new schedule plan immediately. This can be useful for testing modifications to an existing scheduled plan before committing to a production schedule.  This function internally performs the following operations:  1. Copies the properties of the existing scheduled plan into a new scheduled plan 2. Copies any properties passed in the JSON body of this request into the new scheduled plan (replacing the original values) 3. Creates the new scheduled plan 4. Runs the new scheduled plan  The original scheduled plan is not modified by this operation. Admins can create, modify, and run scheduled plans on behalf of other users by specifying a user id. Non-admins can only create, modify, and run their own scheduled plans.  #### Email Permissions:  For details about permissions required to schedule delivery to email and the safeguards Looker offers to protect against sending to unauthorized email destinations, see [Email Domain Allow List for Scheduled Looks](https://cloud.google.com/looker/docs/r/api/embed-permissions).   #### Scheduled Plan Destination Formats  Scheduled plan destinations must specify the data format to produce and send to the destination.  Formats:  | format | Description | :-----------: | :--- | | json | A JSON object containing a `data` property which contains an array of JSON objects, one per row. No metadata. | json_detail | Row data plus metadata describing the fields, pivots, table calcs, and other aspects of the query | inline_json | Same as the JSON format, except that the `data` property is a string containing JSON-escaped row data. Additional properties describe the data operation. This format is primarily used to send data to web hooks so that the web hook doesn't have to re-encode the JSON row data in order to pass it on to its ultimate destination. | csv | Comma separated values with a header | txt | Tab separated values with a header | html | Simple html | xlsx | MS Excel spreadsheet | wysiwyg_pdf | Dashboard rendered in a tiled layout to produce a PDF document | assembled_pdf | Dashboard rendered in a single column layout to produce a PDF document | wysiwyg_png | Dashboard rendered in a tiled layout to produce a PNG image ||  Valid formats vary by destination type and source object. `wysiwyg_pdf` is only valid for dashboards, for example.    This API is rate limited to prevent it from being used for relay spam or DoS attacks

#### Example

#### Parameters

**body** | [**\Swagger\Client\Model\WriteScheduledPlan**](../Model/WriteScheduledPlan.md)| Property values to apply to the newly copied scheduled plan before running it | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get Scheduled Plans for a Dashboard  Returns all scheduled plans for a dashboard which belong to the caller or given user.  If no user_id is provided, this function returns the scheduled plans owned by the caller.   To list all schedules for all users, pass `all_users=true`.   The caller must have `see_schedules` permission to see other users' scheduled plans.

#### Example

#### Parameters

**user_id** | **string**| User Id (default is requesting user if not specified) | [optional]
 **all_users** | **bool**| Return scheduled plans belonging to all users for the dashboard | [optional]
 **fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get Scheduled Plans for a Look  Returns all scheduled plans for a look which belong to the caller or given user.  If no user_id is provided, this function returns the scheduled plans owned by the caller.   To list all schedules for all users, pass `all_users=true`.   The caller must have `see_schedules` permission to see other users' scheduled plans.

#### Example

#### Parameters

**user_id** | **string**| User Id (default is requesting user if not specified) | [optional]
 **fields** | **string**| Requested fields. | [optional]
 **all_users** | **bool**| Return scheduled plans belonging to all users for the look | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get Scheduled Plans for a LookML Dashboard  Returns all scheduled plans for a LookML Dashboard which belong to the caller or given user.  If no user_id is provided, this function returns the scheduled plans owned by the caller.   To list all schedules for all users, pass `all_users=true`.   The caller must have `see_schedules` permission to see other users' scheduled plans.

#### Example

#### Parameters

**user_id** | **string**| User Id (default is requesting user if not specified) | [optional]
 **fields** | **string**| Requested fields. | [optional]
 **all_users** | **bool**| Return scheduled plans belonging to all users for the dashboard | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get Scheduled Plans for a Space  Returns scheduled plans owned by the caller for a given space id.

#### Example

#### Parameters

**fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Update a Scheduled Plan  Admins can update other users' Scheduled Plans.  Note: Any scheduled plan destinations specified in an update will **replace** all scheduled plan destinations currently defined for the scheduled plan.  For Example: If a scheduled plan has destinations A, B, and C, and you call update on this scheduled plan specifying only B in the destinations, then destinations A and C will be deleted by the update.  Updating a scheduled plan to assign null or an empty array to the scheduled_plan_destinations property is an error, as a scheduled plan must always have at least one destination.  If you omit the scheduled_plan_destinations property from the object passed to update, then the destinations defined on the original scheduled plan will remain unchanged.  #### Email Permissions:  For details about permissions required to schedule delivery to email and the safeguards Looker offers to protect against sending to unauthorized email destinations, see [Email Domain Allow List for Scheduled Looks](https://cloud.google.com/looker/docs/r/api/embed-permissions).   #### Scheduled Plan Destination Formats  Scheduled plan destinations must specify the data format to produce and send to the destination.  Formats:  | format | Description | :-----------: | :--- | | json | A JSON object containing a `data` property which contains an array of JSON objects, one per row. No metadata. | json_detail | Row data plus metadata describing the fields, pivots, table calcs, and other aspects of the query | inline_json | Same as the JSON format, except that the `data` property is a string containing JSON-escaped row data. Additional properties describe the data operation. This format is primarily used to send data to web hooks so that the web hook doesn't have to re-encode the JSON row data in order to pass it on to its ultimate destination. | csv | Comma separated values with a header | txt | Tab separated values with a header | html | Simple html | xlsx | MS Excel spreadsheet | wysiwyg_pdf | Dashboard rendered in a tiled layout to produce a PDF document | assembled_pdf | Dashboard rendered in a single column layout to produce a PDF document | wysiwyg_png | Dashboard rendered in a tiled layout to produce a PNG image ||  Valid formats vary by destination type and source object. `wysiwyg_pdf` is only valid for dashboards, for example.

#### Example

#### Parameters

**body** | [**\Swagger\Client\Model\ScheduledPlan**](../Model/ScheduledPlan.md)| Scheduled Plan |

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

### GroupApi

#### Adds a new group to a group.

#### Example

#### Parameters

**body** | [**\Swagger\Client\Model\GroupIdForGroupInclusion**](../Model/GroupIdForGroupInclusion.md)| Group id to add |

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Adds a new user to a group.

#### Example

#### Parameters

**body** | [**\Swagger\Client\Model\GroupIdForGroupUserInclusion**](../Model/GroupIdForGroupUserInclusion.md)| User id to add |

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get information about all the groups in a group

#### Example

#### Parameters

**fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get information about all the users directly included in a group.

#### Example

#### Parameters

**fields** | **string**| Requested fields. | [optional]
 **page** | **int**| DEPRECATED. Use limit and offset instead. Return only page N of paginated results | [optional]
 **per_page** | **int**| DEPRECATED. Use limit and offset instead. Return N rows of data per page | [optional]
 **limit** | **int**| Number of results to return. (used with offset and takes priority over page and per_page) | [optional]
 **offset** | **int**| Number of results to skip before returning any. (used with limit and takes priority over page and per_page) | [optional]
 **sorts** | **string**| Fields to sort by. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get information about all groups.

#### Example

#### Parameters

**page** | **int**| DEPRECATED. Use limit and offset instead. Return only page N of paginated results | [optional]
 **per_page** | **int**| DEPRECATED. Use limit and offset instead. Return N rows of data per page | [optional]
 **limit** | **int**| Number of results to return. (used with offset and takes priority over page and per_page) | [optional]
 **offset** | **int**| Number of results to skip before returning any. (used with limit and takes priority over page and per_page) | [optional]
 **sorts** | **string**| Fields to sort by. | [optional]
 **ids** | [**string[]**](../Model/string.md)| Optional of ids to get specific groups. | [optional]
 **content_metadata_id** | **string**| Id of content metadata to which groups must have access. | [optional]
 **can_add_to_content_metadata** | **bool**| Select only groups that either can/cannot be given access to content. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Creates a new group (admin only).

#### Example

#### Parameters

**fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Deletes a group (admin only).

#### Example

#### Parameters

#

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Removes a group from a group.

#### Example

#### Parameters

**deleting_group_id** | **string**| Id of group to delete |

#### Return type

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Removes a user from a group.

#### Example

#### Parameters

**user_id** | **string**| Id of user to remove from group |

#### Return type

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Remove a user attribute value from a group.

#### Example

#### Parameters

**user_attribute_id** | **string**| Id of user attribute |

#### Return type

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Get information about a group.

#### Example

#### Parameters

**fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Search groups  Returns all group records that match the given search criteria.  If multiple search params are given and `filter_or` is FALSE or not specified, search params are combined in a logical AND operation. Only rows that match *all* search param criteria will be returned.  If `filter_or` is TRUE, multiple search params are combined in a logical OR operation. Results will include rows that match **any** of the search criteria.  String search params use case-insensitive matching. String search params can contain `%` and '_' as SQL LIKE pattern match wildcard expressions. example=\"dan%\" will match \"danger\" and \"Danzig\" but not \"David\" example=\"D_m%\" will match \"Damage\" and \"dump\"  Integer search params can accept a single value or a comma separated list of values. The multiple values will be combined under a logical OR operation - results will match at least one of the given values.  Most search params can accept \"IS NULL\" and \"NOT NULL\" as special expressions to match or exclude (respectively) rows where the column is null.  Boolean search params accept only \"true\" and \"false\" as values.

#### Example

#### Parameters

**limit** | **int**| Number of results to return (used with &#x60;offset&#x60;). | [optional]
 **offset** | **int**| Number of results to skip before returning any (used with &#x60;limit&#x60;). | [optional]
 **sorts** | **string**| Fields to sort by. | [optional]
 **filter_or** | **bool**| Combine given search criteria in a boolean OR expression | [optional]
 **id** | **string**| Match group id. | [optional]
 **name** | **string**| Match group name. | [optional]
 **external_group_id** | **string**| Match group external_group_id. | [optional]
 **externally_managed** | **bool**| Match group externally_managed. | [optional]
 **externally_orphaned** | **bool**| Match group externally_orphaned. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Search groups include hierarchy  Returns all group records that match the given search criteria, and attaches associated role_ids and parent group_ids.  If multiple search params are given and `filter_or` is FALSE or not specified, search params are combined in a logical AND operation. Only rows that match *all* search param criteria will be returned.  If `filter_or` is TRUE, multiple search params are combined in a logical OR operation. Results will include rows that match **any** of the search criteria.  String search params use case-insensitive matching. String search params can contain `%` and '_' as SQL LIKE pattern match wildcard expressions. example=\"dan%\" will match \"danger\" and \"Danzig\" but not \"David\" example=\"D_m%\" will match \"Damage\" and \"dump\"  Integer search params can accept a single value or a comma separated list of values. The multiple values will be combined under a logical OR operation - results will match at least one of the given values.  Most search params can accept \"IS NULL\" and \"NOT NULL\" as special expressions to match or exclude (respectively) rows where the column is null.  Boolean search params accept only \"true\" and \"false\" as values.

#### Example

#### Parameters

**limit** | **int**| Number of results to return (used with &#x60;offset&#x60;). | [optional]
 **offset** | **int**| Number of results to skip before returning any (used with &#x60;limit&#x60;). | [optional]
 **sorts** | **string**| Fields to sort by. | [optional]
 **filter_or** | **bool**| Combine given search criteria in a boolean OR expression | [optional]
 **id** | **string**| Match group id. | [optional]
 **name** | **string**| Match group name. | [optional]
 **external_group_id** | **string**| Match group external_group_id. | [optional]
 **externally_managed** | **bool**| Match group externally_managed. | [optional]
 **externally_orphaned** | **bool**| Match group externally_orphaned. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Search groups include roles  Returns all group records that match the given search criteria, and attaches any associated roles.  If multiple search params are given and `filter_or` is FALSE or not specified, search params are combined in a logical AND operation. Only rows that match *all* search param criteria will be returned.  If `filter_or` is TRUE, multiple search params are combined in a logical OR operation. Results will include rows that match **any** of the search criteria.  String search params use case-insensitive matching. String search params can contain `%` and '_' as SQL LIKE pattern match wildcard expressions. example=\"dan%\" will match \"danger\" and \"Danzig\" but not \"David\" example=\"D_m%\" will match \"Damage\" and \"dump\"  Integer search params can accept a single value or a comma separated list of values. The multiple values will be combined under a logical OR operation - results will match at least one of the given values.  Most search params can accept \"IS NULL\" and \"NOT NULL\" as special expressions to match or exclude (respectively) rows where the column is null.  Boolean search params accept only \"true\" and \"false\" as values.

#### Example

#### Parameters

**limit** | **int**| Number of results to return (used with &#x60;offset&#x60;). | [optional]
 **offset** | **int**| Number of results to skip before returning any (used with &#x60;limit&#x60;). | [optional]
 **sorts** | **string**| Fields to sort by. | [optional]
 **filter_or** | **bool**| Combine given search criteria in a boolean OR expression | [optional]
 **id** | **string**| Match group id. | [optional]
 **name** | **string**| Match group name. | [optional]
 **external_group_id** | **string**| Match group external_group_id. | [optional]
 **externally_managed** | **bool**| Match group externally_managed. | [optional]
 **externally_orphaned** | **bool**| Match group externally_orphaned. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Updates the a group (admin only).

#### Example

#### Parameters

**body** | [**\Swagger\Client\Model\Group**](../Model/Group.md)| Group |
 **fields** | **string**| Requested fields. | [optional]

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

#### Set the value of a user attribute for a group.  For information about how user attribute values are calculated, see [Set User Attribute Group Values](#!/UserAttribute/set_user_attribute_group_values).

#### Example

#### Parameters

**user_attribute_id** | **string**| Id of user attribute |
 **body** | [**\Swagger\Client\Model\UserAttributeGroupValue**](../Model/UserAttributeGroupValue.md)| New value for group. |

#### Return type

#

#### Authorization

#### HTTP request headers

- **Accept**: application/json

## Type Definitions

### MergeFields

### UserAttribute

### LDAPUserAttributeWrite

### LookmlTestResult

### LookmlModelExploreFieldEnumeration

### BoardItem

### EmbedSsoParams

### EmbedCookielessSessionAcquire

### RepositoryCredential

### MergeQuerySourceQuery

### GroupHierarchy

### LookmlModelExploreAlwaysFilter

### LookmlModelExploreFieldMeasureFilters

### LookmlModelExploreSupportedMeasureType

### AlertDestination

### PermissionSet

### AlertNotifications

### ImportedProject

### DataActionUserState

### SamlUserAttributeRead

### CreateOAuthApplicationUserStateRequest

### ContentMetaGroupUser

### LookmlModelExploreSet

### DataActionResponse

### DialectInfoOptions

### Locale

### MergeQuery

### ContentView

### LDAPConfigTestResult

### Group

### UserAttributeWithValue

### MaterializePDT

### ContentValidationSpace

### ContentValidationLookMLDashboardElement

### UserEmailOnly

### AlertAppliedDashboardFilter

### LocalizationSettings

### HomepageSection

### Dashboard

### LookmlModelExplore

### CreateQueryTask

### ContentValidationAlert

### DashboardFilter

### CreateDashboardRenderTask

### OIDCUserAttributeWrite

### Model

### SamlUserAttributeWrite

### CredentialsApi3

### Integration

### SessionConfig

### WhitelabelConfiguration

### ThemeSettings

### DashboardLookml

### ContentValidatorError

### ProjectValidation

### ContentValidationDashboard

### AccessToken

### GitConnectionTest

### SamlGroupRead

### RenderTask

### ScheduledPlan

### ModelSet

### RunningQueries

### QueryTask

### IntegrationTestResult

### IntegrationRequiredField

### ProjectWorkspace

### GitStatus

### CreateEmbedUserRequest

### UserAttributeGroupValue

### LDAPGroupRead

### OIDCConfig

### SqlQuery

### ProjectValidationCache

### SamlGroupWrite

### EmbedCookielessSessionGenerateTokens

### Alert

### SupportAccessEnable

### Schema

### GroupIdForGroupUserInclusion

### SqlQueryCreate

### SamlMetadataParseResult

### SupportAccessAllowlistEntry

### Project

### RoleSearch

### DashboardAggregateTableLookml

### BackupConfiguration

### CredentialsEmail

### ContentValidationFolder

### ColorStop

### Workspace

### ContentValidationLook

### EmbedParams

### Space

### ApiVersionElement

### UserPublic

### ContentSearch

### Homepage

### SpaceBase

### SamlConfig

### ModelsNotValidated

### ScheduledPlanDestination

### CustomWelcomeEmail

### ResultMakerWithIdVisConfigAndDynamicFields

### SupportAccessStatus

### ContentValidation

### LookmlTest

### ContentMeta

### ModelNamedValueFormats

### Timezone

### OIDCUserAttributeRead

### DashboardAppearance

### ResultMakerFilterablesListen

### PrivatelabelConfiguration

### WriteScheduledPlan

### EmbedCookielessSessionGenerateTokensResponse

### LookWithDashboards

### LDAPUserAttributeRead

### Artifact

### Error

### DialectInfo

### SchemaColumns

### LookmlModelExploreFieldMapLayer

### LookmlModelExploreJoins

### LookBasic

### LookmlModelExploreFieldTimeInterval

### SchemaColumn

### ResultMakerFilterables

### OIDCGroupRead

### CredentialsEmailSearch

### LDAPConfig

### CredentialsSaml

### CostEstimate

### WelcomeEmailTest

### CreateDashboardFilter

### GroupIdForGroupInclusion

### DBConnection

### HomepageItem

### DataActionFormField

### Permission

### CreateCredentialsApi3

### ContentValidationLookMLDashboard

### Manifest

### CredentialsLookerOpenid

### LookModel

### UpdateFolder

### ConnectionFeatures

### Query

### CreateOAuthApplicationUserStateResponse

### DataActionForm

### Theme

### EmbedCookielessSessionAcquireResponse

### ExternalOauthApplication

### OauthClientApp

### LDAPGroupWrite

### DiscretePalette

### DBConnectionTestResult

### LookmlModelExploreAccessFilter

### DependencyGraph

### ContentValidationDashboardElement

### Board

### SmtpNodeStatus

### InternalHelpResourcesContent

### SshTunnel

### UpdateArtifact

### ContinuousPalette

### IntegrationParam

### ApiSession

### DashboardBase

### User

### LookmlModelExploreConditionallyFilter

### DataActionRequest

### DelegateOauthTest

### LookmlModelExploreField

### SchemaTables

### DBConnectionOverride

### UserLoginLockout

### OIDCGroupWrite

### ArtifactUsage

### ProjectError

### CredentialsGoogle

### DigestEmailSend

### ContentFavorite

### Session

### ColumnSearch

### EgressIpAddresses

### CredentialsTotp

### SupportAccessAddEntries

### SchemaTable

### ArtifactNamespace

### IntegrationHub

### SshServer

### GitConnectionTestResult

### ValidationError

### SmtpStatus

### CredentialsOIDC

### Setting

### AlertConditionState

### LDAPUser

### ContentValidationDashboardFilter

### DashboardElement

### MobileToken

### Role

### AlertFieldFilter

### ContentValidationScheduledPlan

### GitBranch

### LookmlModel

### ProjectFile

### InternalHelpResources

### Snippet

### DigestEmails

### DashboardLayout

### EmbedSecret

### LookmlModelExploreFieldSqlCase

### AlertField

### PasswordConfig

### DBConnectionBase

### DashboardLayoutComponent

### LookmlModelExploreError

### Folder

### SshPublicKey

### SmtpSettings

### Dialect

### MobileFeatureFlags

### CreateCostEstimate

### LookmlModelExploreAlias

### ModelFieldSuggestions

### BoardSection

### LookmlModelNavExplore

### AlertPatch

### CreateFolder

### LegacyFeature

### ValidationErrorDetail

### Look

### ApiVersion

### UserIdOnly

### CredentialsEmbed

### MobilePayload

### LookmlModelExploreFieldset

### Datagroup

### LDAPConfigTestIssue

### CredentialsLDAP

### ColorCollection

### ContentValidationError

### GroupSearch

### DataActionFormSelectOption

### FolderBase

### LookWithQuery

### MobileSettings

### EmbedUrlResponse

