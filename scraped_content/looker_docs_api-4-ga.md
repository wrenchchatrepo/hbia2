# https://cloud.google.com/looker/docs/api-4-ga

Depth: 3

We are excited to announce that Looker API 4.0 is generally available in Looker 22.4. The generally available API 4.0 (API 4.0 GA) has multiple breaking and additive changes and promotes multiple endpoints from Beta to Stable. Check out our [API reference](/looker/docs/reference/looker-api/latest) for detailed API 4.0 specs. We updated our Looker-supported and Community-supported SDKs to support Looker API 4.0 GA endpoints. For more information, see [API and SDK support policies](/looker/docs/api-sdk-support-policy) and [API Versioning](/looker/docs/api-versioning). The rest of this article outlines the breaking changes, mitigations, and features you can look forward to when migrating to API 4.0 GA.

## Who should read this?

This document is for you if you use the Looker API through Looker-supported SDKs, Community-supported SDKs, or the API itself. Read the following section that maps to the Looker API version you use.

## Pre-GA API 4.0 Users

If you use API 4.0, read this section. It covers the breaking changes and available mitigations when you migrate to API 4.0 GA.

API 4.0 GA includes changing all entity ID fields from numeric `integer` type to `string` type. For example, `GET /groups/{group_id}` [endpoint](/looker/docs/reference/looker-api/latest/methods/Group/group) returns `id` as type `string` instead of type `int64`.

Please read through the following table for impact and mitigations specific to your API 4.0 endpoint usage:

**Usage** | **Potential Impact 1** | **Prevention**  
---|---|---  
**Looker mobile apps** | Outdated installations of Looker mobile apps stop working | Have users update to the latest version of the Looker mobile app(s)  
**Looker Supported 2 SDKs**  
**TypeScript SDK (4.0 API)** | No impact | No action needed  
**Python SDK (4.0 API)** | No impact | No action needed  
**Ruby SDK (4.0 API)** | No impact | No action needed  
**Community Supported 2 SDKs**  
**Swift SDK** | Runtime exceptions | Update SDK to v22.0+; then resolve resulting type errors, if any  
**Kotlin SDK** | No impact | No action needed  
**LookR SDK** | No impact | No action needed  
**C# SDK** | No impact | No action needed  
**Go SDK** | Runtime exceptions | Update SDK to v22.0+; then resolve resulting type errors, if any  
**Other**  
**Using 4.0 API without an SDK (or with externally provided libraries)** | Possible runtime errors, depending on language's type sensitivity | Review code for dependencies on the type of any ID fields and add support for string-type ID fields. Also review this [additional guidance](https://github.com/looker-open-source/sdk-codegen/blob/main/docs/json.md).  
  
1: Assuming common usage patterns that may include the use of Looker's ID fields, but not unusual usage patterns such as applying numeric operations to IDs.

2: [Looker API & SDK support](/looker/docs/api-sdk-support-policy). Community-supported libraries are not officially supported by Looker.

## API 3.1 Users

If you use API 3.1, read this section. It covers the additional features and changes that API 4.0 makes available to you. Keep in mind, all our Looker-supported and Community-supported SDKs mainly support API 4.0. See [SDK and API support policies](/looker/docs/api-sdk-support-policy) for more information.

### Additional API 4.0 GA Features

For convenience, we list the most notable and useful additive API 4.0 changes for you:

  * [Board, board item, and board section creation and management](/looker/docs/reference/looker-api/latest/methods/Board). See the [Board documentation page](/looker/docs/presenting-content) for more information about boards.
  * Query additional connection info such as [databases](/looker/docs/reference/looker-api/latest/methods/Metadata/connection_databases), [schemas](/looker/docs/reference/looker-api/latest/methods/Metadata/connection_schemas), [columns](/looker/docs/reference/looker-api/latest/methods/Metadata/connection_columns), and [tables](/looker/docs/reference/looker-api/latest/methods/Metadata/connection_tables). Set and update additional connection fields.
  * OAuth apps and users creation and management. See the [OAuth documentation page](/looker/docs/api-cors) for more information about OAuth.
  * Search groups with [hierarchy](/looker/docs/reference/looker-api/latest/methods/Group/search_groups_with_hierarchy) and [roles](/looker/docs/reference/looker-api/latest/methods/Group/search_groups_with_roles).
  * [Search roles with user count](/looker/docs/reference/looker-api/latest/methods/Role/search_roles_with_user_count).
  * [Get](/looker/docs/reference/looker-api/latest/methods/Config/get_setting) and [set](/looker/docs/reference/looker-api/latest/methods/Config/set_setting) Looker instance settings. See the [Settings documentation page](/looker/docs/admin-panel-general-settings) for more information about settings.
  * [Alert creation and management](/looker/docs/reference/looker-api/latest/methods/Alert). See the [Alerts documentation page](/looker/docs/alerts-overview) for more information about alerts.
  * [SSH tunnels and SSH servers creation, management, and testing](/looker/docs/reference/looker-api/latest/methods/Connection). See the [SSH documentation page](/looker/docs/using-an-ssh-tunnel) for more information about SSH.
  * [Move](/looker/docs/reference/looker-api/latest/methods/Dashboard/move_dashboard) and [copy](/looker/docs/reference/looker-api/latest/methods/Dashboard/copy_dashboard) dashboards.
  * [Get relative URLs for new dashboards](/looker/docs/reference/looker-api/latest/methods/Dashboard/create_dashboard).
  * [Move](/looker/docs/reference/looker-api/latest/methods/Look/move_look) and [copy](/looker/docs/reference/looker-api/latest/methods/Look/copy_look) Looks.
  * [Signed embed](/looker/docs/single-sign-on-embedding) and non-signed embed secret, URL, and user creation and management.
  * [Get refresh token to refresh login access token](/looker/docs/reference/looker-api/latest/methods/ApiAuth/login).
  * Limit and offset the results from getting [all LookML models](/looker/docs/reference/looker-api/latest/methods/LookmlModel/all_lookml_models) and [all users](/looker/docs/reference/looker-api/latest/methods/User/all_users).
  * Limit and offset the results from [searching users](/looker/docs/reference/looker-api/latest/methods/User/search_users).
  * [Get the Looker instance API spec in Swagger 2.x JSON](/looker/docs/reference/looker-api/latest/methods/Config/api_spec).

### API 4.0 GA Deprecation Changes

API 4.0 GA replaces several deprecated API 3.1 endpoints with improved features. The following endpoints are affected:

  * Deprecated Homepage endpoints have been removed. Please make use of [board endpoints](/looker/docs/reference/looker-api/latest/methods/Board) instead of homepages. See [Presenting content with boards](/looker/docs/presenting-content).
  * Deprecated Space endpoints have been removed. Make use of [folder endpoints](/looker/docs/reference/looker-api/latest/methods/Folder) instead of Space. See [Organizing and managing access to content](/looker/docs/organizing-spaces).

## API 3.0 Users

API 3.0 is [deprecated](/looker/docs/api-3x-deprecation), and it is recommended you migrate to API 4.0.

  * Only API 4.0 supports all Looker-supported and Community-supported SDKs to ease your development. Check out our [SDK repository](https://github.com/looker-open-source/sdk-codegen).
  * API 4.0 introduces multiple new features and enhancements as listed in the Additional API 4.0 GA Features section on this page.

## Wrap-Up

You can look forward to new features and additive changes to be added to API 4.0 and you can always find the latest changes in our [API reference](/looker/docs/reference/looker-api/latest). For more information, see [API and SDK support policies](/looker/docs/api-sdk-support-policy) and [API Versioning](/looker/docs/api-versioning). We know that breaking changes are not ideal. Unless an extreme issue arises, we will not make any breaking changes to our generally available API 4.0. We hope our generally available Looker API 4.0 helps you develop more productively and easily on the Looker platform.