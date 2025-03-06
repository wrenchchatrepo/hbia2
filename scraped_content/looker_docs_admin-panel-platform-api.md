# https://cloud.google.com/looker/docs/admin-panel-platform-api

Depth: 3

The **API** page in the **Platform** section of the **Admin** menu lets you manage access to the Looker API server endpoint. The page also provides a link to the [API Explorer](/looker/docs/api-explorer) documentation.  
  
## Accessing the API page

To access the API page:

  1. Click the Looker **Main menu** icon menu.
  2. Click **Admin** to open the **Admin** menu.
  3. Select **API**.
  4. View the **API Host URL**.

**Note:** To access all the admin pages in Looker, you must have the [Admin role](/looker/docs/admin-panel-users-roles#default_roles). If you have a permission that enables only parts of the **Admin** panel, such as [`manage_schedules`](/looker/docs/admin-panel-users-roles#manage_schedules) or [`manage_themes`](/looker/docs/admin-panel-users-roles#manage_themes), but you don't have the Admin role, then Looker may not display the page or pages described in this article in the **Admin** panel. Also, the `see_admin` permission grants read-only permission to most (but not all) Admin pages. See the [`see_admin`](/looker/docs/admin-panel-users-roles#see_admin) description for more information.

## API Host URL

The **API Host URL** is the user-facing domain name (and port) that users need to reach the Looker API server endpoint. To specify a URL, enter your API path in the **API Host URL** field in the following format:
    
    
    https://<instance_name>.cloud.looker.com
    

For Looker installations behind a load balancer (for example, a [cluster](/looker/docs/clustering-looker) configuration) or other proxy, the user-facing domain name may be different from the actual Looker server machine name. If this is the case, the **API Host URL** must indicate the user-facing API host name and port.

If the **API Host URL** field is empty, Looker uses the default API path. For Looker instances hosted on Google Cloud, Microsoft Azure, and instances hosted on Amazon Web Service (AWS) that were created on or after 07/07/2020, the default Looker API path uses port `443`. For Looker instances hosted on AWS that were created before 07/07/2020, the default Looker API path uses port `19999`. The default API URL is in the following format:
    
    
    https://<instance_name>.cloud.looker.com:<port>
    

## API Documentation

If you have installed the [API Explorer extension](/looker/docs/api-explorer) from the [Looker Marketplace](/looker/docs/marketplace), you can click **Use API Explorer** to open the API Explorer and view current API documentation.

If you have not installed the API Explorer extension, you can click **Install API Explorer from the Marketplace** to install the API Explorer on your Looker instance.