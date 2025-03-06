# https://cloud.google.com/looker/docs/extension-framework-building-tile-extensions

Depth: 3

Starting in Looker 24.0, extensions can be developed to run in a tile in dashboards. Extensions that support being run as a tile or visualization can be [added while the dashboard is in edit mode](/looker/docs/creating-user-defined-dashboards#adding_extensions) or [saved to a dashboard as a visualization from an Explore](/looker/docs/viewing-and-interacting-with-explores#the_explore_actions_gear_menu). Extensions can also be configured as tiles in [LookML dashboards](/looker/docs/building-lookml-dashboards).

Examples of extensions that can be used as dashboard tiles are available:

  * The [tile visualization extension](https://github.com/looker-open-source/extension-examples/tree/main/react/javascript/tile-visualization) shows how to build a custom visualization using the extension framework.
  * The [tile sdk extension](https://github.com/looker-open-source/extension-examples/tree/main/react/javascript/tile-sdk) shows the available API methods that are specific to tile extensions.

## Using the Looker Extension SDK with tile extensions

Tile extensions require the [`mount_points` parameter](/looker/docs/reference/param-manifest-application#mount_points) to be defined in the LookML [project manifest file](/looker/docs/lookml-project-files#project_manifest_files) in order for extensions to be loaded as tiles into a dashboard. There are two types of `mount_points` related to tile extensions:
    
    
      mount_points: {
        dashboard_vis: yes
        dashboard_tile: yes
        standalone: yes
      }
    

  * `dashboard_vis` — When enabled, the extension will appear in the [visualization options of an Explore](/looker/docs/creating-visualizations#choosing_a_visualization_type), where the extension can be selected as a visualization and [saved as a dashboard tile](/looker/docs/creating-user-defined-dashboards#adding_query_tiles_from_an_explore). When the dashboard is run, the dashboard will execute the query associated with the tile and make the data available to the extension. This is similar to how [custom visualizations](/looker/docs/reference/param-manifest-visualization) work. The primary difference between a custom visualization and an extension running in a dashboard tile that has `dashboard_vis` enabled, is that the extension may make [Looker API](/looker/docs/reference/looker-api/latest) calls.
  * `dashboard_tile` — When enabled, the extension will appear in the [**Extensions** panel](/looker/docs/creating-user-defined-dashboards#adding_extensions) that is displayed when a user is editing a dashboard and selects the **Extensions** option after clicking the **Add** button. This type of extension is responsible for retrieving its own data, instead of the having the tile query automatically supply the extension with data.

An additional mount point, `standalone`, causes the extension to appear under the **Applications** section of the Looker main menu. It is possible for an extension to have multiple mount points defined. At runtime, the extension is notified how it is mounted and it can adjust its behavior accordingly. For example, [`standalone` extensions may need to set their own height, while tile extensions don't](/looker/docs/extension-framework-building-tile-extensions#building_reactive_extensions).

## Tile extension additional APIs

Tile extensions are provided with additional APIs and data at runtime. These are obtained from the extension context:
    
    
    const {
      tileSDK,
      tileHostData,
      visualizationData,
      visualizationSDK,
    } = useContext(ExtensionContext40)
    

  * `tileSDK` — Provides tile-specific functions to allow the extension to interact with the Looker dashboard host. For example, to allow the extension to display and clear error messages.
  * `tileHostData` — Provides tile data to the extension. The data is automatically updated based upon interactions with the hosting dashboard. An example is the `isDashboardEditing` indicator.
  * `visualizationSDK` — Provides visualization-specific functions to allow the extension to interact with the Looker dashboard host. An example is the `updateRowLimit` function.
  * `visualizationData` — Provides visualization data to the extension. The data is automatically updated based upon interactions with the hosting dashboard. The data is similar to the data that is provided to [custom visualizations](/looker/docs/reference/param-manifest-visualization).

## Building reactive extensions

The iframes that extensions run in automatically resize as the parent Looker host window resizes. This is automatically reflected in the iframe content window. The iframe component does not have any padding or margin so it is up to the extension to provide its own padding and margin so that it looks consistent with the Looker application. For standalone extensions, it is up to the extension to control the extension height. For extensions that run in dashboard tiles or Explore visualizations, the iframe content window will automatically be set to the height that is made available by the iframe.

## Rendering considerations

It is important to note that tile extensions will be rendered when a dashboard is downloaded as a PDF or an image. The renderer expects that the tile will notify it when rendering is complete. If this is not done, the renderer will stop responding. The following is an example of how to notify the renderer that the tile has rendered.
    
    
      const { extensionSDK } = useContext(ExtensionContext40)
    
      useEffect(() => {
        extensionSDK.rendered()
      }, [])
    

Animations should also be disabled when rendering. The following is an example where animation configurations are turned off when rendering:
    
    
      const { lookerHostData} = useContext(ExtensionContext40)
      const isRendering = lookerHostData?.isRendering
    
      const config = isRendering
        ? {
            ...visConfig,
            valueCountUp: false,
            waveAnimateTime: 0,
            waveRiseTime: 0,
            waveAnimate: false,
            waveRise: false,
          }
        : visConfig
    
      if (mountPoint === MountPoint.dashboardVisualization) {
        return <VisualizationTile config={config} />
      }
    

## Tile SDK functions and properties

The tile SDK provides functions that allow a tile extension to interact with its hosting dashboard.

The available functions and properties are shown in the following table:

Function or property | Description  
---|---  
`tileHostData` (property) | Host data specific to the tile extension. See the Tile SDK data section for details.  
`addError` | When called, the dashboard or Explore will display an error message underneath the visualization.  
`clearError` | When called, the dashboard or Explore will hide any error message shown underneath the visualization.  
`openDrillMenu` | For visualization extensions, this call opens a drill menu. This call is ignored if the extension is not a tile extension visualization.  
`runDashboard` | Runs the current dashboard. This call is ignored by a tile visualization extension running in an Explore.  
`stopDashboard` | Stops a running dashboard. This call is ignored by a tile visualization extension running in an Explore.  
`updateFilters` | Updates filters in the current dashboard or Explore.  
`openScheduleDialog` | Opens the schedule dialog. This call is ignored when running in an Explore.  
`toggleCrossFilter` | Toggles cross filters. This call is ignored when running in an Explore.  
  
## Tile SDK data

The available tile SDK data properties are shown in the following table:

Property | Description  
---|---  
`isExploring` | When true, indicates that the tile is being configured as a visualization inside an Explore.  
`dashboardId` | The dashboard ID of the tile that is being rendered. If the tile is being configured as an Explore, this property won't be populated.  
`elementId` | The element ID of the tile that is being rendered. If the tile is being configured as an Explore, this property won't be populated.  
`queryId` | The query ID of the tile that is being rendered if it is associated with a visualization. If the tile is being configured as an Explore, this property won't be populated.The `queryId` is the ID of the query that is created when the visualization is built-in the Looker Explore. It does not contain any filters or cross filtering to be applied to the dashboard. To reflect the data shown in the `QueryResponse`, filters and cross filters will need to be applied and a new query generated. As a result, there may be more useful properties than `queryId`. See `filteredQuery` for a query object with filters applied.  
`querySlug` | The query [slug](/looker/docs/glossary#slug) of the tile that is being rendered if it is associated with a visualization. If the tile is being configured as an Explore, this property won't be populated.The `querySlug` is a slug of the query that is created when the visualization is built-in the Looker Explore. It does not contain any filters or cross filtering that is applied to the dashboard. To reflect the data shown in the `QueryResponse`, filters and cross filters will need to be applied and a new query generated. As a result, there may be more useful properties than `querySlug`. See `filteredQuery` for a query object with filters applied.  
`dashboardFilters` | The filters that are being applied to the dashboard. If the tile is being configured as an Explore, this property won't be populated.  
`dashboardRunState` | Indicates whether the dashboard is running. If the tile is being configured as an Explore, the state will be `UNKNOWN`.For dashboard performance reasons, the runstate may never be shown as running. This generally happens if there are no other tiles associated with a query, including the one the extension is associated with. If the extension needs to know for certain that a dashboard has been run, detecting differences in the `lastRunStartTime` is the reliable way.  
`isDashboardEditing` | When true, the dashboard is being edited. If the tile is being configured as an Explore, this property won't be populated.  
`isDashboardCrossFilteringEnabled` | When true, [cross-filtering](/looker/docs/cross-filtering-dashboards#enabling_cross-filtering_on_dashboards) is enabled on the dashboard. If the tile is being configured as an Explore, this property won't be populated.  
`filteredQuery` | A query object that matches the query ID that is associated with the underlying dashboard element that applies any dashboard filters and timezone changes that are made at the dashboard level.  
`lastRunSourceElementId` | The ID of the tile extension element that triggered the last dashboard run. The ID will be undefined if the dashboard run was triggered by the dashboard **Run** button or [autorefresh](/looker/docs/editing-user-defined-dashboards#autorefresh), or if the run was triggered using the embed SDK. If the tile is being configured as an Explore, this property won't be populated.Note that the `lastRunSourceElementId` can be the same as the element ID of the current extension instance. For example, if the extension triggers a dashboard run, it will be notified when the dashboard run starts and finishes.  
`lastRunStartTime` | Indicates the last dashboard run start time. If the tile is being configured as an Explore, this property won't be populated.Note that the start and end times reported shouldn't be used for capturing performance metrics.  
`lastRunEndTime` | Indicates the last dashboard run end time. If the tile is being configured as an Explore, this property won't be populated. If the tile is running, this property won't be populated.Note that the start and end times reported shouldn't used for capturing performance metrics.  
`lastRunSuccess` | Indicates whether the last dashboard run was successful or not. If the tile is being configured as an Explore, this property won't be populated. If the tile is running, this property won't be populated.  
  
## Visualization SDK functions and properties

The available visualization SDK functions and properties are shown in the following table:

Function or property | Description  
---|---  
`visualizationData` (property) | Visualization (combination of `visConfig` and `queryResponse` data).  
`visConfig` (property) | Visualization configuration data:

  * Measure configurations
  * Dimension configurations
  * Table calculations
  * Pivot configurations
  * Visualization configurations

These are used to customize the look and feel of a visualization in an Explore.  
`queryResponse` (property) | Response data from the query  
`configureVisualization` | Sets the default configuration for an extension visualization. The configuration will be rendered inside the Explore visualization editor. This should only be called once.  
`setVisConfig` | Updates the visualization configuration.  
`updateRowLimit` | Updates the query row limit.  
  
## Visualization SDK data

The visualization SDK consists of the following:

  * Visualization configuration data
  * Query response data

### Visualization configuration data

Property | Description  
---|---  
`queryFieldMeasures` | Measure information  
`queryFieldDimensions` | Dimension information  
`queryFieldTableCalculations` | Table calculation information  
`queryFieldPivots` | Pivot information  
`visConfig` | Visual configuration data. This should be merged with the default configuration and applied to the visualization rendered by the extension.  
      
    
    export interface VisualizationConfig {
      queryFieldMeasures: Measure[]
      queryFieldDimensions: Dimension[]
      queryFieldTableCalculations: TableCalculation[]
      queryFieldPivots: PivotConfig[]
      visConfig: RawVisConfig
    }
    

### Query response data

Property | Description  
---|---  
`data` | Array of row data  
`fieldMeasures` | Field measure information.  
`fieldDimensions` | Field dimension information.  
`fieldTableCalculations` | Field table calculations information.  
`fieldPivots` | Field pivot information.  
`fieldMeasureLike` | A concatenated array of field measure information and table calculations that behave like measures.  
`fieldDimensionLike` | A concatenated array of field dimension information and table calculations that behave like dimensions.