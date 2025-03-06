# https://cloud.google.com/looker/docs/types-of-dashboards

Depth: 3

A Looker dashboard is a collection of queries displayed as visualizations on a screen. Users can [alter filters](/looker/docs/viewing-dashboards#temporarily_changing_filter_values_on_dashboards) on dashboards, [apply alerts](/looker/docs/creating-alerts) to tiles, set up [dashboard delivery schedules](/looker/docs/scheduling-and-sending-dashboards), and [download](/looker/docs/downloading#downloading_data_from_a_dashboard) a dashboard's data, among other things.

There are two types of Looker dashboards: [user-defined dashboards](/looker/docs/dashboards) and [LookML dashboards](/looker/docs/reference/lookml-dashboard-overview).

Each type of dashboard has different benefits and constraints:

Characteristic | User-Defined Dashboard | LookML Dashboard  
---|---|---  
Generally created and edited by | Business users and Looker developers. | A select group of LookML developers.  
Defined | By adding query tiles, Look-linked tiles, or text in the user interface; arranging them using drag-and-drop operations; and adding and formatting dashboard filters and other options (as described on the [Creating user-defined dashboards](/looker/docs/creating-user-defined-dashboards) documentation page). | Written and edited in a YAML-based dashboard file, as described in the [Creating a LookML dashboard file](/looker/docs/building-lookml-dashboards#creating_a_lookml_dashboard_file) section of the [Building LookML dashboards](/looker/docs/building-lookml-dashboards) documentation page.  
Updated | When the dashboard is edited or the corresponding saved Looks are updated. | When the LookML file for the dashboard is edited.  
Stored | In a user's personal folder or in a shared folder for easy collaboration across a wider group of users. | As version-controlled files that are associated with the project in a Git repository. By default, LookML dashboards are accessible for viewing in the [**LookML dashboards**](/looker/docs/building-lookml-dashboards#lookml_dashboards_folder) folder located in the [**All folders**](/looker/docs/finding-content#top-level_folders) top-level folder. They can also be [moved to other folders](/looker/docs/building-lookml-dashboards#moving_lookml_dashboards_outside_of_the_lookml_dashboards_folder) as desired. LookML dashboards are not shown in the **Recently Viewed** tab of the homepage or on the **Recently viewed** page.  
Convertible | To LookML dashboards, as described in the [Getting dashboard LookML from a dashboard](/looker/docs/viewing-dashboards#getting_dashboard_lookml_from_a_dashboard) section of the [Viewing dashboards](/looker/docs/viewing-dashboards) documentation page. | To user-defined dashboards, as explained on the [Converting from LookML to user-defined dashboards](/looker/docs/converting-lookml-to-user-defined-dashboard) documentation page.