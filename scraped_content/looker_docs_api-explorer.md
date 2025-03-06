# https://cloud.google.com/looker/docs/api-explorer

Depth: 3

**Note:** As of Looker 22.4, the [Looker API 4.0 is generally available](/looker/docs/api-4-ga). In Looker 23.18, the [Looker API 3.1 has been removed](/looker/docs/api-3x-deprecation).

The Looker API Explorer is an extension — a web application that is built using Looker components — that is developed using the Looker [extension framework](/looker/docs/intro-to-extension-framework) and that is deployed through the [Looker Marketplace](/looker/docs/marketplace).

The API Explorer provides the following assets for use with the [Looker API](/looker/docs/reference/looker-api/latest):

  * Documentation for all Looker API methods and types
  * Method and type declarations in all supported SDK languages
  * Links to example SDK functions that use API methods
  * Links to API Explorer pages for referenced methods and types
  * A **Run It** function that lets you execute API calls directly and provides the code for the API calls, API responses, and SDK functions
  * A comparison tool that shows the differences in Looker API versions

There is no need for the user to log in for the extension version of API Explorer, because API Explorer uses the active user's account for API requests. This ensures that the user can only perform the API calls to which they are entitled while also eliminating the need for them to provide API credentials.

Looker's [sudo as another user](/looker/docs/admin-panel-users-users#impersonating-users) feature can also be used to make API requests as a different user to help diagnose access issues.

## Installing the API Explorer

The API Explorer is available on the Looker [Marketplace](/looker/docs/marketplace).

Before installing the API Explorer from the Marketplace, a Looker admin must enable the [**Extension Framework**](/looker/docs/admin-panel-platform-extension-framework) feature.

Installing applications — such as the API Explorer extension — from the Marketplace requires that you have the [`develop`](/looker/docs/admin-panel-users-roles#develop), [`manage_models`](/looker/docs/admin-panel-users-roles#manage-models), and [`deploy`](/looker/docs/admin-panel-users-roles#deploy) permissions. Once the API Explorer has been installed, any user with at least the `access_data` permission on the `extension_api_explorer` model can use the API Explorer. Each user can view all API endpoints in the API Explorer, but can only run those allowed by their permissions.

If your Looker admin has enabled the [**Auto Install**](/looker/docs/admin-panel-platform-marketplace#auto_install) option in the [**Marketplace**](/looker/docs/admin-panel-platform-marketplace) page in the **Platform** section of Looker's **Admin** menu, the API Explorer will be automatically installed on your instance. In addition, any time updates are available, those updates will be applied automatically, ensuring the version of the API Explorer on your instance is the most current.

If your Looker admin has not enabled the **Auto Install** option, you will need to install the API Explorer from the Looker Marketplace.

See the [Using the Looker Marketplace](/looker/docs/marketplace#installing_a_tool_from_the_marketplace) documentation page for instructions on installing an extension from the Looker Marketplace. You can ensure that you always have the most updated version of the API Explorer by going to the Looker Marketplace, selecting **Manage** , and selecting the **Update** button next to the extension.

**Note:** If you are installing the API Explorer on a customer-hosted Looker instance, for users to view API examples the server running the Looker instance must be configured to access the public internet server running at the URL `https://githubusercontent.com`.

## Starting the API Explorer

Once the API Explorer is installed, you can navigate to it from the **Applications** section of the left sidebar.

**Note:** If you are a Looker admin, you can also access the API Explorer by selecting the **Use API Explorer** link on Looker's [**API** Admin page](/looker/docs/admin-panel-platform-api).

## Navigating in the API Explorer

From the API Explorer home page you can perform the following tasks:

![](/static/looker/docs/images/api-explorer-nav-2220.png)

  1. Use the SDK language selector drop-down to choose the programming language in which the API Explorer will display API method and type declarations and code results. The selector defaults to Python on initial load. If you choose **All** from the language selector, the API Explorer displays a tabbed view for each supported language.

  2. Use the version drop-down to choose a version of the API:

     * **4.0 - current**
  3. Select the **Compare Specifications** button to open the API version comparison page.

  4. Enter a search term in the **Search** field to limit the listed **Methods** and **Types** to only those that include text that matches your search term.

![](/static/looker/docs/images/api-explorer-search-2416.png)

When you select a method or type returned by the search, the search term will be highlighted in the method or type summary.

  5. Select the **Methods** tab to display API method categories. You can expand or contract a method category to view the individual methods in the category.

  6. Select the **Types** tab to display API types. Types are not categorized and are listed in alphabetical order.

  7. Select the **Main Menu** button to hide or show the API Explorer navigation panel.

## Viewing API method and type documentation

When you select a method category in the **Method** tab, the method category expands and shows you all the methods that are in that category.

![](/static/looker/docs/images/api-explorer-choose-method-2216.png)

  1. All the methods that are in that category are shown in the main panel. You can choose to display all the methods that are in the category, or you can select the tab for a particular method type to filter the list to just that method type.

  2. To view the documentation for a specific method, either choose the method name in the navigation panel, or select the method in the main panel.

Once you have selected a specific method, the API Explorer displays the documentation for that method.

![](/static/looker/docs/images/api-explorer-get-color-collections-2218.png)

When you select a type from the **Type** tab, the documentation for that type is displayed in the main panel.

![](/static/looker/docs/images/api-explorer-color-collection-2302.png)

### Method and type declarations

API Explorer renders the SDK method and type declarations in the SDK language that is chosen in the SDK language selector drop-down. If the SDK language selector is set to **All** , the method and type declarations are displayed in all supported SDK languages, separated by tabs.

![](/static/looker/docs/images/api-explorer-all-langs-2312.png)

### SDK examples

The Looker [`sdk-codegen` repository](https://github.com/looker-open-source/sdk-codegen) has a folder that contains Looker SDK examples. If the `sdk-codegen` repository has examples for a method, the method's API Explorer page will display an **SDK Examples** section with links to the examples.

If a specific SDK language is selected, examples for that language are listed first.

There may also be Ruby and Java examples displayed, although these are not SDK languages.

### References

The **References** section for each method and type includes links to the API Explorer pages for each method or type that is referenced by the original method or type.

## Using Run It to request and display API calls

The API Explorer includes a **Run It** button that opens a panel from which you can request API calls and display the responses in a variety of supported formats.

![](/static/looker/docs/images/api-explorer-runit-2108.png)

When you select the **Run It** button, the API Explorer displays a **Request** tab, where you can provide the inputs to the API method.

![](/static/looker/docs/images/api-explorer-request-2108.png)

Enter the desired input, and select **Run** to execute the API call.

> Whenever the API method can change data (for any REST call that is a `POST`, a `PATCH`, an `UPDATE`, or a `DELETE`), the data change confirmation checkbox appears and must be checked before the request can be run.

When the request is run, the **Response** tab shows the results.

In addition, the **Code** tab shows the SDK call syntax for the SDK that is chosen in the language selector drop-down. If the SDK language selector is set to **All** , the SDK call syntax is displayed in all supported SDK languages, separated by tabs.

### Response display types

API Explorer responses include a [MIME type](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types) that is used to determine how to display the results.

#### CSV and other tabular data

For CSV and JSON data, Looker performs a shape test to determine whether the data meets the criteria of a table. If Looker determines that the payload data is tabular, then the default display for the response is a data grid.

![](/static/looker/docs/images/api-explorer-tabular-output-2108.png)

Select the **Raw** tab to display the untransformed data.

![](/static/looker/docs/images/api-explorer-raw-output-2108.png)

#### JSON

JSON payloads may be tabular, in which case they will be displayed in a grid. The column headers for the LookML query are displayed in the form `<view_name>.<field_name>`, rather than displaying the field's label.

![](/static/looker/docs/images/api-explorer-json-table-output-2108.png)

Complex JSON payloads omit the grid display and show only the raw JSON.

#### PNG and JPEG

The PNG and JPEG formats display the visualization that is selected for the query and include any applied visualization settings. The next example is PNG output of the same query shown previously but using a table visualization. JPEG is handled similarly.

![An example PNG download.](/static/looker/docs/images/api-explorer-png-output-2108.png)

#### SVG

Some Looker endpoints return SVG, which is also directly supported. Following is an example of the `content_thumbnail` endpoint in SVG format, which returns an abstracted thumbnail image of a dashboard.

![An example SVG download.](/static/looker/docs/images/api-explorer-svg-output-2108.png)

#### HTML

Requests that return HTML source code display the source HTML in the **Response** tab.

![](/static/looker/docs/images/api-explorer-html-output-2108.png)

#### Text

Requests that return SQL or other formats that are MIME typed as plain text are displayed as plain text in the **Response** tab.

![](/static/looker/docs/images/api-explorer-sql-output-2108.png)

## Comparing API versions

The API Explorer includes a page that lets you compare different versions of the Looker API to see what has changed between versions. Select the triangular **Compare Specifications** button, located at the upper right corner of the page, to open the API Explorer comparison page.

![](/static/looker/docs/images/api-explorer-comparison-2108.png)

  1. Select the base version of the API and the version of the API you want to compare to the base version.

  2. Select the API options that you want to include in the comparison to filter the methods to only those that have differences in the options you select. The options are:

     * **Missing** — Shows all the methods that exist in one version of the API and that are missing in the other.
     * **Status** — Shows all methods where the method status has changed. For example, a method where the status has changed from `beta` to `stable`.
     * **Parameters** — Shows all methods where one or more of the method parameters has changed.
     * **Type** — Shows types that have new, removed, or changed properties.
     * **Body** — Shows changes to body parameters.
     * **Response** — Shows all methods where there has been a change in the method response.
  3. The comparison page shows you the number of methods where there is a difference and lists the methods where there is a difference.

  4. Select a method to expand it, and the comparison page displays a diff that shows how the method has changed between versions.