# https://cloud.google.com/looker/docs/embedded-javascript-events

Depth: 3

After you've created an embed — which can be done [publicly](/looker/docs/publishing-looks-with-public-urls#public_embedding_with_iframes), [privately](/looker/docs/private-embedding), with [signed embedding](/looker/docs/single-sign-on-embedding), or through the [API](/looker/docs/api-getting-started) — you can interact with those iframes using JavaScript. You can make your page more dynamic based on the status of the embedded item, and you can even make changes to the embedded item from your web page.

Be aware that Looker doesn't control the order in which browsers dispatch events to web applications. This means that the order of events is not guaranteed across browsers or platforms. Be sure to write your JavaScript appropriately to account for the event handling of different browsers.

You can use JavaScript in one of the following ways for Looker embedded content:

  * Using Looker's embed Software Development Kit (SDK), described on the [Embed SDK](/looker/docs/embed-sdk) documentation page
  * Using JavaScript events, described in the [Accessing events in JavaScript](/looker/docs/embedded-javascript-events#event_type_reference) section on this page

## Preparation

Before you can interact with the embedded iframe, follow these steps:

  * Add an ID to the iframe.
  * Add the embed domain to the iframe `src` attribute.
  * Add the embed domain to the allowlist.

### Adding an ID to the iframe

Later, when you retrieve data from the iframe, you'll need to validate that the information you're working with has actually come from Looker's iframe. To facilitate this, be sure to add an ID to your iframe, if you haven't done so already. In the following example, you set the ID to `looker` by adding `id="looker"` to the iframe:
    
    
    <iframe id="looker" src="https://instance_name.looker.com/embed/dashboards/1"></iframe>
    

### Adding the embed domain to the iframe `src` attribute

In the iframe's `src` attribute, include the domain where the iframe is being used. In the following example, you can specify `myownpersonaldomain.com` as the domain by adding `?embed_domain=https://myownpersonaldomain.com"` to the end of the URL in the `src` attribute:
    
    
    <iframe
      id="looker"
      src="https://instance_name.looker.com/embed/dashboards/1?embed_domain=https://myownpersonaldomain.com">
    </iframe>
    

If you're using [signed embedding](/looker/docs/single-sign-on-embedding), make sure you add the `embed_domain` to the [embed URL](/looker/docs/single-sign-on-embedding#embed_url_2).

**Tip:** Don't include a trailing slash (`/`) in the value that you provide for the `embed_domain` parameter.

If you're using the [Embed SDK](/looker/docs/embed-sdk), add `sdk=2` to the end of the embed URL. The `sdk=2` parameter indicates that the SDK is present and that Looker can take advantage of additional features that the SDK provides, such as passing JavaScript events between the Looker iframe and your domain. The SDK cannot add this parameter itself because it is part of the signed URL. For example:
    
    
    <iframe
      id="looker"
      src="https://instance_name.looker.com/embed/dashboards/1?embed_domain=https://myownpersonaldomain.com&sdk=2">
    </iframe>
    

### Adding the embed domain to the allowlist

Finally, you'll need to add the domain where the iframe is being used to the allowlist on the [**Embed** page of Looker's **Admin** panel](/looker/docs/admin-panel-platform-embed) by following these steps:

  1. In the **Embedded Domain Allowlist** field, enter the domain where the iframe is being used, and then press the Tab key so that the domain appears in a box within the field.

**Important:** Don't include a trailing slash (`/`) in the domain URL.
  2. Click **Update**.

You can use the `*` wildcard in the allowlist to create a domain pattern. For example, `https://*.myownpersonaldomain.com` would allow both `https://analytics.myownpersonaldomain.com` and `https://data.myownpersonaldomain.com`.

If you're using [cookieless embedding](/looker/docs/cookieless-embed) with Looker 23.8 or later, the embed domain can be specified when the cookieless session is acquired. This is an alternative to adding the embed domain to the allowlist using the **Admin > Embed** panel. Review the [security best practices](/looker/docs/security-best-practices-embedded-analytics) if you decide to take advantage of this feature.

## Retrieving data from the iframe

After completing the preparation steps, you can access the events that are passed between the Looker iframe and your domain by listening for [`postMessage`](https://developer.mozilla.org/en-US/docs/Web/API/Window/postMessage) events.

**Important:** Be sure to check that the events have come from the Looker iframe and domain to avoid [malicious messages](https://developer.mozilla.org/en-US/docs/Web/API/Window/postMessage#Security_concerns).

The embedded iframe can create a few event types, as described in the Event type reference section on this page.

### Accessing events in JavaScript

Here is an example of listening for these events in native JavaScript, then logging them to the console:
    
    
    window.addEventListener("message", function(event) {
      if (event.source === document.getElementById("looker").contentWindow) {
        if (event.origin === "https://instance_name.looker.com") {
          console.log(JSON.parse(event.data));
        }
      }
    });
    

Here is an example of listening for these events in jQuery, then logging them to the console:
    
    
    $(window).on("message", function(event) {
      if (event.originalEvent.source === $("#looker")[0].contentWindow) {
        if (event.origin === "https://instance_name.looker.com") {
          console.log(JSON.parse(event.data));
        }
      }
    });
    

### Event type summary table

The following table summarizes event types. Select an event type to see the details about that event.

Event Type | Event Cause  
---|---  
`dashboard:loaded` | On dashboards where the tiles are not set to auto-run, a dashboard and its elements have loaded but queries are not yet running.  
`dashboard:run:start` | A dashboard has begun loading, and its tiles have started loading and querying for data.  
`dashboard:run:complete` | A dashboard has finished running and all tiles have finished loading and querying.  
`dashboard:download` | A PDF of a dashboard has started downloading.  
`dashboard:edit:start` |  ADDED 22.20  A dashboard has been switched to edit mode. The `dashboard:save:complete` event will be fired when the dashboard is successfully saved.  
`dashboard:edit:cancel` |  ADDED 22.20  A dashboard that is in edit mode has been exited from edit mode without saving.  
`dashboard:save:complete` | A dashboard has been edited and saved.  
`dashboard:delete:complete` | A dashboard has been deleted.  
`dashboard:tile:start` | A tile has started loading or querying for data.  
`dashboard:tile:complete` | A tile has finished running the query.  
`dashboard:tile:download` | A tile's data has started downloading.  
`dashboard:tile:explore` | A user has clicked the **Explore From Here** option in a dashboard tile.  
`dashboard:tile:view` | A user has clicked the **View Original Look** option in a dashboard tile.  
`dashboard:filters:changed` | A dashboard's filters have been applied or changed.  
`look:ready` | A Look has begun to load query data, whether the query will run or not.  
`look:run:start` | A Look has begun to load query data and the query has begun to run.  
`look:run:complete` | A Look has finished running the query.  
`look:save:complete` | A Look has been edited and saved.  
`look:delete:complete` | A Look has been moved into the [**Trash** folder](/looker/docs/admin-spaces).  
`drillmenu:click` | A user has clicked on a drill menu in a dashboard that was created with the [`link` LookML parameter](/looker/docs/reference/param-field-link).  
`drillmodal:download` | A user has opened a drill dialog box from a dashboard tile and clicked the **Download** option.  
`drillmodal:explore` | A user has clicked the **Explore From Here** option in a drill dialog box.  
`explore:ready` | An Explore has begun to load query data, whether the query will run or not.  
`explore:run:start` | An Explore has begun to load query data and the query has begun to run.  
`explore:run:complete` | An Explore has finished running the query.  
`explore:state:changed` | An Explore page URL has changed as a result of the user's actions.  
`page:changed` | A user has navigated to a new page within the iframe.  
`page:properties:changed` | The height of a dashboard iframe has changed.  
`session:tokens` | The Looker client requires tokens to continue.  
`session:status` | Sends information about the status of a session.  
`env:client:dialog` | A dialog box has been opened that may partially be out of view, such as a drill dialog box. This event enables the hosting application to scroll the dialog box into view.  
  
### Event type reference

The embedded iframe can create many different types of events:

#### `dashboard:loaded`

On dashboards where the tiles are not set to auto-run, this event is created after a dashboard and its elements have loaded but before queries are run.
    
    
    type: "dashboard:loaded",
    status: "complete",
    dashboard: {
      id: 1,
      title: "Business Pulse",
      canEdit: true,
      dashboard_filters: {
        "date": "Last 6 Years",
        "state": ""
      },
      absoluteUrl: "https://self-signed.looker.com:9999/embed/dashboards/1?embed_domain=https%3A%2F%2Fself-signed.looker.com%3A9999&date=Last+6+Years&state=",
      url: "/embed/dashboards/1?embed_domain=https%3A%2F%2Fself-signed.looker.com%3A9999&date=Last+6+Years&state=",
      options: {
        layouts: [
          {
            id: 1,
            dashboard_id: 1,
            type: "newspaper",
            active: true,
            column_width: null,
            width: null,
            deleted: false,
            dashboard_layout_components: [
              {
                id: 1,
                dashboard_layout_id: 1,
                dashboard_element_id: 1,
                row: 0,
                column: 0,
                width: 8,
                height: 4,
                deleted: false
              },
              {
                id: 2,
                dashboard_layout_id: 1,
                dashboard_element_id: 2,
                row: 0,
                column: 8,
                width: 8,
                height: 4,
                deleted: false
              }
            ]
          }
        ],
        elements: {
          1: {
            title: "Total Orders",
            title_hidden: false,
            vis_config: {
              type: "single_value",
              font_size: "medium",
              title: "Total Orders"
            }
          },
          2: {
            title: "Average Order Profit",
            title_hidden: false,
            vis_config: {
              type: "single_value",
              title: "Average Order Profit"
            }
          }
        }
      }
    }
    

Attribute | Format | Description  
---|---|---  
`status` | String | Indicates whether the dashboard and its elements have successfully loaded.  
`dashboard.id` | Number/String | The ID of the dashboard.  
`dashboard.title` | String | The title, as shown at the top of the dashboard.  
`dashboard.canEdit` | Boolean |  ADDED 22.20  When `true`, the user can edit the dashboard.  
`dashboard.dashboard_filters` | Object | The filters applied to the dashboard. This object has the format: `{"Filter name 1": "value 1", "Filter name 2": "value 2", ...}`  
`dashboard.absoluteUrl` | String | The full dashboard URL.  
`dashboard.url` | String | The relative dashboard URL (just the path).  
`dashboard.options` | Object | The [dashboard layout](/looker/docs/reference/looker-api/latest/methods/Dashboard/dashboard_layout), [dashboard layout component](/looker/docs/reference/looker-api/latest/methods/Dashboard/dashboard_layout_component), and [dashboard element](/looker/docs/reference/looker-api/latest/methods/Dashboard/dashboard_element) properties and values. All properties returned in the `options` object can be given updated values using the `dashboard:options:set` event.  
  
#### `dashboard:run:start`

This event is created when a dashboard has begun loading, when its tiles will start loading and querying for data.
    
    
    type: "dashboard:run:start",
    dashboard: {
      id: 23,
      title: "My Dashboard",
      canEdit: true,
      url: "/embed/dashboards/...",
      absoluteUrl: "https://instance_name.looker.com/embed/dashboards/...",
      dashboard_filters: {
        "Date": "Last 28 days",
        "Total Orders": "Greater than 100"
      }
    }
    

Attribute | Format | Description  
---|---|---  
`dashboard.id` | Number/String | The ID of the dashboard.  
`dashboard.title` | String | The title, as shown at the top of the dashboard.  
`dashboard.canEdit` | Boolean |  ADDED 22.20  When `true`, the user can edit the dashboard.  
`dashboard.url` | String | The relative dashboard URL (just the path).  
`dashboard.absoluteUrl` | String | The full dashboard URL.  
`dashboard.dashboard_filters` | Object | The filters applied to the dashboard. This object has the format: `{"Filter name 1": "value 1", "Filter name 2": "value 2", ...}`  
  
#### `dashboard:run:complete`

This event is created when a dashboard has finished running and all tiles have finished loading and querying. This event is created whether or not all tiles load successfully.
    
    
    type: "dashboard:run:complete",
    status: "complete",
    dashboard: {
      id: 23,
      title: "My Dashboard",
      canEdit: true,
      url: "/embed/dashboards/...",
      absoluteUrl: "https://my.looker.com/embed/dashboards/...",
      dashboard_filters: {
        "Date": "Last 28 days",
        "Total Orders": "Greater than 100"
      }
      options: {
        layouts: [
          {
            id: 1,
            dashboard_id: 1,
            type: "newspaper",
            active: true,
            column_width: null,
            width: null,
            deleted: false,
            dashboard_layout_components: [
              {
                id: 1,
                dashboard_layout_id: 1,
                dashboard_element_id: 1,
                row: 0,
                column: 0,
                width: 8,
                height: 4,
                deleted: false
              },
              {
                id: 2,
                dashboard_layout_id: 1,
                dashboard_element_id: 2,
                row: 0,
                column: 8,
                width: 8,
                height: 4,
                deleted: false
              }
            ]
          }
        ],
        elements: {
          1: {
            title: "Total Orders",
            title_hidden: false,
            vis_config: {
              type: "single_value",
              font_size: "medium",
              title: "Total Orders"
            }
          },
          2: {
            title: "Average Order Profit",
            title_hidden: false,
            vis_config: {
              type: "single_value",
              title: "Average Order Profit"
            }
          }
        }
      }
    }
    

Attribute | Format | Description  
---|---|---  
`status` | String | Indicates whether the dashboard and its elements have successfully run. If the dashboard and its elements were successfully run, `status` returns `"complete"`; otherwise, `status` returns `"error"`. If the running dashboard was stopped, either from the user interface or with the `dashboard:stop` action, `status` will return `"stopped"`.  
`dashboard.id` | Number/String | The ID of the dashboard.  
`dashboard.title` | String | The title, as shown at the top of the dashboard.  
`dashboard.canEdit` | Boolean |  ADDED 22.20  When `true`, the user can edit the dashboard.  
`dashboard.url` | String | The relative dashboard URL (just the path).  
`dashboard.absoluteUrl` | String | The full dashboard URL.  
`dashboard.dashboard_filters` | Object | The filters applied to the dashboard. This object has the format: `{"Filter name 1": "value 1", "Filter name 2": "value 2", ...}`  
`dashboard.options` | Object | The [dashboard layout](/looker/docs/reference/looker-api/latest/methods/Dashboard/dashboard_layout), [dashboard layout component](/looker/docs/reference/looker-api/latest/methods/Dashboard/dashboard_layout_component), and [dashboard element](/looker/docs/reference/looker-api/latest/methods/Dashboard/dashboard_element) properties and values. All properties returned in the `options` object can be given updated values using the `dashboard:options:set` action.  
`dashboard.tileStatuses` | Object array | An array of objects providing tile statuses. Object properties are:

  * `tileId` — the ID number of tile.
  * `status` — If the tile query was successfully run, `status` returns `"complete"`; otherwise, `status` returns `"error"`.
  * `errors` — Populated when the `status` property is `"error"`. An array of objects providing details of the error, including the error message text, a more detailed description of the error, and the tile's SQL query that produced the error.

  
  
#### `dashboard:download`

This event is created when a PDF of a dashboard has started downloading.
    
    
    type: "dashboard:download",
    dashboard: {
      id: 23,
      title: "My Dashboard",
      canEdit: true,
      url: "/embed/dashboards/...",
      absoluteUrl: "https://instance_name.looker.com/embed/dashboards/...",
      dashboard_filters: {
        "Date": "Last 28 days",
        "Total Orders": "Greater than 100"
      }
    }
    fileFormat: "pdf"
    

Attribute | Format | Description  
---|---|---  
`dashboard.id` | Number/String | The ID of the dashboard.  
`dashboard.title` | String | The title, as shown at the top of the dashboard.  
`dashboard.canEdit` | Boolean |  ADDED 22.20  When `true`, the user can edit the dashboard.  
`dashboard.url` | String | The relative dashboard URL (just the path).  
`dashboard.absoluteUrl` | String | The full dashboard URL.  
`dashboard.dashboard_filters` | Object | The filters applied to the dashboard. This object has the format: `{"Filter name 1": "value 1", "Filter name 2": "value 2", ...}`  
`fileFormat` | String | The format of the downloaded dashboard (only `"pdf"` at this time).  
  
#### `dashboard:edit:start`

ADDED 22.20  This event is created when a dashboard is [switched into edit mode](/looker/docs/editing-user-defined-dashboards#entering_edit_mode_in_dashboards).
    
    
    type: "dashboard:edit:start",
    dashboard: {
      id: 23,
      title: "My Dashboard",
      canEdit: true,
      url: "/embed/dashboards/...",
      absoluteUrl: "https://instance_name.looker.com/embed/dashboards/...",
      dashboard_filters: {
        "Date": "Last 28 days",
        "Total Orders": "Greater than 100"
      }
    }
    

Attribute | Format | Description  
---|---|---  
`dashboard.id` | Number/String | The ID of the dashboard.  
`dashboard.title` | String | The title, as shown at the top of the dashboard.  
`dashboard.canEdit` | Boolean |  ADDED 22.20  When `true`, the user can edit the dashboard.  
`dashboard.url` | String | The relative dashboard URL (just the path).  
`dashboard.absoluteUrl` | String | The full dashboard URL.  
`dashboard.dashboard_filters` | Object | The filters applied to the dashboard. This object has the format: `{"Filter name 1": "value 1", "Filter name 2": "value 2", ...}`  
  
#### `dashboard:edit:cancel`

ADDED 22.20  This event is created when a dashboard that is in [edit mode](/looker/docs/editing-user-defined-dashboards#entering_edit_mode_in_dashboards) is exited from edit mode without saving.
    
    
    type: "dashboard:edit:cancel",
    dashboard: {
      id: 23,
      title: "My Dashboard",
      canEdit: true,
      url: "/embed/dashboards/...",
      absoluteUrl: "https://instance_name.looker.com/embed/dashboards/...",
      dashboard_filters: {
        "Date": "Last 28 days",
        "Total Orders": "Greater than 100"
      }
    }
    

Attribute | Format | Description  
---|---|---  
`dashboard.id` | Number/String | The ID of the dashboard.  
`dashboard.title` | String | The title, as shown at the top of the dashboard.  
`dashboard.canEdit` | Boolean |  ADDED 22.20  When `true`, the user can edit the dashboard.  
`dashboard.url` | String | The relative dashboard URL (just the path).  
`dashboard.absoluteUrl` | String | The full dashboard URL.  
`dashboard.dashboard_filters` | Object | The filters applied to the dashboard. This object has the format: `{"Filter name 1": "value 1", "Filter name 2": "value 2", ...}`  
  
#### `dashboard:save:complete`

This event is created when a dashboard is [edited and then saved](/looker/docs/editing-user-defined-dashboards#entering_edit_mode_in_dashboards).
    
    
    type: "dashboard:save:complete",
    dashboard: {
      id: 23,
      title: "My Dashboard",
      canEdit: true,
      dashboard_filters: {
        "Date": "Last 28 days",
        "Total Orders": "Greater than 100"
      }
      absoluteUrl: "https://instance_name.looker.com/embed/dashboards/...",
      url: "/embed/dashboards/...",
      options: {
        layouts: [
          {
            id: 1,
            dashboard_id: 1,
            type: "newspaper",
            active: true,
            column_width: null,
            width: null,
            deleted: false,
            dashboard_layout_components: [
              {
                id: 1,
                dashboard_layout_id: 1,
                dashboard_element_id: 1,
                row: 0,
                column: 0,
                width: 8,
                height: 4,
                deleted: false
              },
              {
                id: 2,
                dashboard_layout_id: 1,
                dashboard_element_id: 2,
                row: 0,
                column: 8,
                width: 8,
                height: 4,
                deleted: false
              }
            ]
          }
        ],
        elements: {
          1: {
            title: "Total Orders",
            title_hidden: false,
            vis_config: {
              type: "single_value",
              font_size: "medium",
              title: "Total Orders"
            }
          },
          2: {
            title: "Average Order Profit",
            title_hidden: false,
            vis_config: {
              type: "single_value",
              title: "Average Order Profit"
            }
          }
        }
      }
    }
    

Attribute | Format | Description  
---|---|---  
`dashboard.id` | Number/String | The ID of the dashboard.  
`dashboard.title` | String | The title, as shown at the top of the dashboard.  
`dashboard.canEdit` | Boolean |  ADDED 22.20  When `true`, the user can edit the dashboard.  
`dashboard.dashboard_filters` | Object | The filters applied to the dashboard. This object has the format: `{"Filter name 1": "value 1", "Filter name 2": "value 2", ...}`  
`dashboard.absoluteUrl` | String | The full dashboard URL.  
`dashboard.url` | String | The relative dashboard URL (just the path).  
`dashboard.options` | Object | The [dashboard layout](/looker/docs/reference/looker-api/latest/methods/Dashboard/dashboard_layout), [dashboard layout component](/looker/docs/reference/looker-api/latest/methods/Dashboard/dashboard_layout_component), and [dashboard element](/looker/docs/reference/looker-api/latest/methods/Dashboard/dashboard_element) properties and values. All properties returned in the `options` object can be given updated values using the `dashboard:options:set` event.  
  
#### `dashboard:delete:complete`

This event is created when a [dashboard is deleted](https://docs.looker.com/dashboards/editing-dashboards-beta#deleting_dashboards).
    
    
    type: "dashboard:delete:complete",
    dashboard: {
      id: 23,
      title: "My Dashboard",
      canEdit: true,
      dashboard_filters: {
        "Date": "Last 28 days",
        "Total Orders": "Greater than 100"
      }
      absoluteUrl: "https://instance_name.looker.com/embed/dashboards/...",
      url: "/embed/dashboards/...",
      options: {
        layouts: [
          {
            id: 1,
            dashboard_id: 1,
            type: "newspaper",
            active: true,
            column_width: null,
            width: null,
            deleted: false,
            dashboard_layout_components: [
              {
                id: 1,
                dashboard_layout_id: 1,
                dashboard_element_id: 1,
                row: 0,
                column: 0,
                width: 8,
                height: 4,
                deleted: false
              },
              {
                id: 2,
                dashboard_layout_id: 1,
                dashboard_element_id: 2,
                row: 0,
                column: 8,
                width: 8,
                height: 4,
                deleted: false
              }
            ]
          }
        ],
        elements: {
          1: {
            title: "Total Orders",
            title_hidden: false,
            vis_config: {
              type: "single_value",
              font_size: "medium",
              title: "Total Orders"
            }
          },
          2: {
            title: "Average Order Profit",
            title_hidden: false,
            vis_config: {
              type: "single_value",
              title: "Average Order Profit"
            }
          }
        }
      }
    }
    

Attribute | Format | Description  
---|---|---  
`dashboard.id` | Number/String | The ID of the dashboard.  
`dashboard.title` | String | The title, as shown at the top of the dashboard.  
`dashboard.canEdit` | Boolean |  ADDED 22.20  When `true`, the user can edit the dashboard.  
`dashboard.dashboard_filters` | Object | The filters applied to the dashboard. This object has the format: `{"Filter name 1": "value 1", "Filter name 2": "value 2", ...}`  
`dashboard.absoluteUrl` | String | The full dashboard URL.  
`dashboard.url` | String | The relative dashboard URL (just the path).  
`dashboard.options` | Object | The [dashboard layout](/looker/docs/reference/looker-api/latest/methods/Dashboard/dashboard_layout), [dashboard layout component](/looker/docs/reference/looker-api/latest/methods/Dashboard/dashboard_layout_component), and [dashboard element](/looker/docs/reference/looker-api/latest/methods/Dashboard/dashboard_element) properties and values. All properties returned in the `options` object can be given updated values using the `dashboard:options:set` event.  
  
#### `dashboard:tile:start`

This event is created when a tile starts loading or querying for data.
    
    
    type: "dashboard:tile:start",
    dashboard: {
      id: 23,
      title: "My Dashboard",
      canEdit: true,
      url: "/embed/dashboards/...",
      absoluteUrl: "https://instance_name.looker.com/embed/dashboards/...",
      dashboard_filters: {
        "Date": "Last 28 days",
        "Total Orders": "Greater than 100"
      }
    }
    tile: {
      id: 123,
      title: "Quarterly Sales",
      listen: {
        "Date": "order.date",
        "Total Orders": "order.count"
      }
    }
    

Attribute | Format | Description  
---|---|---  
`dashboard.id` | Number/String | The ID of the dashboard to which the tile belongs.  
`dashboard.title` | String | The dashboard title, as shown at the top of the dashboard to which the tile belongs.  
`dashboard.canEdit` | Boolean |  ADDED 22.20  When `true`, the user can edit the dashboard.  
`dashboard.url` | String | The relative dashboard URL (just the path) to which the tile belongs.  
`dashboard.absoluteUrl` | String | The full dashboard URL to which the tile belongs.  
`dashboard.dashboard_filters` | Object | The filters applied to the dashboard to which the tile belongs. This object has the format: `{"Filter name 1": "value 1", "Filter name 2": "value 2", ...}`  
`tile.id` | Integer | The ID number of the event, not the tile.  
`tile.title` | String | The tile title, as shown at the top of the tile.  
`tile.listen` | Object | The global dashboard filters this tile is listening for. This object has the format: `{"Filter Label": "Filter Field", ...}`  
  
#### `dashboard:tile:complete`

This event is created when a tile has finished running the query.
    
    
    type: "dashboard:tile:complete",
    dashboard: {
      id: 23,
      title: "My Dashboard",
      canEdit: true,
      url: "/embed/dashboards/...",
      absoluteUrl: "https://instance_name.looker.com/embed/dashboards/...",
      dashboard_filters: {
        "Date": "Last 28 days",
        "Total Orders": "Greater than 100"
      }
    }
    status: "complete",
    truncated: false,
    tile: {
      id: 123,
      title: "Quarterly Sales",
      listen: {
        "Date": "order.date",
        "Total Orders": "order.count"
      }
    }
    

Attribute | Format | Description  
---|---|---  
`dashboard.id` | Number/String | The ID of the dashboard to which the tile belongs.  
`dashboard.title` | String | The dashboard title, as shown at the top of the dashboard to which the tile belongs.  
`dashboard.canEdit` | Boolean |  ADDED 22.20  When `true`, the user can edit the dashboard.  
`dashboard.url` | String | The relative dashboard URL (just the path) to which the tile belongs.  
`dashboard.absoluteUrl` | String | The full dashboard URL to which the tile belongs.  
`dashboard.dashboard_filters` | Object | The filters applied to the dashboard to which the tile belongs. This object has the format: `{"Filter name 1": "value 1", "Filter name 2": "value 2", ...}`  
`status` | String | Whether the tile query completed successfully. Possible values are `"complete"` or `"error"`.  
`truncated` | Boolean | Whether the tile query results were truncated as a result of the query returning more rows than the query row limit. The row limit could be either a user-specified row limit or the Looker default row limit of 5,000.  
`tile.id` | Integer | The ID number of the event, not the tile.  
`tile.title` | String | The tile title, as shown at the top of the tile.  
`tile.listen` | Object | The global dashboard filters this tile is listening for. This object has the format: `{"Filter Label": "Filter Field", ...}`  
`tile.errors` | Object array | Populated when the `status` property is `"error"`. An array of objects providing details of the error, including the error message text, a more detailed description of the error, and the tile's SQL query that produced the error.  
  
#### `dashboard:tile:download`

This event is created when a tile's data has started downloading.
    
    
    type: "dashboard:tile:download",
    dashboard: {
      id: 23,
      title: "My Dashboard",
      canEdit: true,
      url: "/embed/dashboards/...",
      absoluteUrl: "https://instance_name.looker.com/embed/dashboards/...",
      dashboard_filters: {
        "Date": "Last 28 days",
        "Total Orders": "Greater than 100"
      }
    }
    tile: {
      id: 123,
      title: "Quarterly Sales"
      listen: {
        "Date": "order.date",
        "Total Orders": "order.count"
      }
    }
    fileFormat: "pdf"
    

Attribute | Format | Description  
---|---|---  
`dashboard.id` | Number/String | The ID of the dashboard to which the tile belongs.  
`dashboard.title` | String | The dashboard title, as shown at the top of the dashboard to which the tile belongs.  
`dashboard.canEdit` | Boolean |  ADDED 22.20  When `true`, the user can edit the dashboard.  
`dashboard.url` | String | The relative dashboard URL (just the path) to which the tile belongs.  
`dashboard.absoluteUrl` | String | The full dashboard URL to which the tile belongs.  
`dashboard.dashboard_filters` | Object | The filters applied to the dashboard to which the tile belongs. This object has the format: `{"Filter name 1": "value 1", "Filter name 2": "value 2", ...}`  
`tile.id` | Integer | The ID number of the event, not the tile.  
`tile.title` | String | The tile title, as shown at the top of the tile.  
`tile.listen` | Object | The global dashboard filters this tile is listening for. This object has the format: `{"Filter Label": "Filter Field", ...}`  
`fileFormat` | String | The format of the downloaded tile (only `"pdf"` at this time).  
  
#### `dashboard:tile:explore`

This event is created when a user clicks the **Explore From Here** option in a dashboard tile.
    
    
    type: "dashboard:tile:explore",
    label: 'Explore From Here',
    url: '/embed/explore/model/view...',
    dashboard: {
      id: 23,
      title: "My Dashboard",
      canEdit: true,
      url: "/embed/dashboards/...",
      absoluteUrl: "https://instance_name.looker.com/embed/dashboards/...",
      dashboard_filters: {
        "Date": "Last 28 days",
        "Total Orders": "Greater than 100"
      }
    }
    tile: {
      id: 123,
      title: "Quarterly Sales",
      listen: {
        "Date": "order.date",
        "Total Orders": "order.count"
      }
    }
    

Attribute | Format | Description  
---|---|---  
`label` | String | The button label.  
`url` | String | The relative URL (just the path) of the Explore to be viewed.  
`dashboard.id` | Number/String | The ID of the dashboard to which the tile belongs.  
`dashboard.title` | String | The dashboard title, as shown at the top of the dashboard to which the tile belongs.  
`dashboard.canEdit` | Boolean |  ADDED 22.20  When `true`, the user can edit the dashboard.  
`dashboard.url` | String | The relative dashboard URL (just the path) to which the tile belongs.  
`dashboard.absoluteUrl` | String | The full dashboard URL to which the tile belongs.  
`dashboard.dashboard_filters` | Object | The filters applied to the dashboard to which the tile belongs. This object has the format: `{"Filter name 1": "value 1", "Filter name 2": "value 2", ...}`  
`tile.id` | Integer | The ID number of the event, not the tile.  
`tile.title` | String | The tile title, as shown at the top of the tile.  
`tile.listen` | Object | The global dashboard filters this tile is listening for. This object has the format: `{"Filter Label": "Filter Field", ...}`  
  
#### `dashboard:tile:view`

This event is created when a user clicks the **View Original Look** option in a dashboard tile.
    
    
    type: "dashboard:tile:view",
    label: 'View Original Look',
    url: '/embed/look/...',
    dashboard: {
      id: 23,
      title: "My Dashboard",
      canEdit: true,
      url: "/embed/dashboards/...",
      absoluteUrl: "https://instance_name.looker.com/embed/dashboards/...",
      dashboard_filters: {
        "Date": "Last 28 days",
        "Total Orders": "Greater than 100"
      }
    }
    tile: {
      id: 123,
      title: "Quarterly Sales",
      listen: {
        "Date": "order.date",
        "Total Orders": "order.count"
      }
    }
    

Attribute | Format | Description  
---|---|---  
`label` | String | The button label.  
`url` | String | The relative URL (just the path) of the Look to be viewed.  
`dashboard.id` | Number/String | The ID of the dashboard to which the tile belongs.  
`dashboard.title` | String | The dashboard title, as shown at the top of the dashboard to which the tile belongs.  
`dashboard.canEdit` | Boolean |  ADDED 22.20  When `true`, the user can edit the dashboard.  
`dashboard.url` | String | The relative dashboard URL (just the path) to which the tile belongs.  
`dashboard.absoluteUrl` | String | The full dashboard URL to which the tile belongs.  
`dashboard.dashboard_filters` | Object | The filters applied to the dashboard to which the tile belongs. This object has the format: `{"Filter name 1": "value 1", "Filter name 2": "value 2", ...}`  
`tile.id` | Integer | The ID number of the event, not the tile.  
`tile.title` | String | The tile title, as shown at the top of the tile.  
`tile.listen` | Object | The global dashboard filters this tile is listening for. This object has the format: `{"Filter Label": "Filter Field", ...}`  
  
#### `dashboard:filters:changed`

This event is created when a dashboard's filters have been applied or changed.
    
    
    type: "dashboard:filters:changed",
    dashboard: {
      id: 23,
      title: "My Dashboard",
      canEdit: true,
      url: "/embed/dashboards/...",
      absoluteUrl: "https://instance_name.looker.com/embed/dashboards/...",
      dashboard_filters: {
        "Date": "Last 28 days",
        "Total Orders": "Greater than 100"
      }
      options: {
        layouts: [
          {
            id: 1,
            dashboard_id: 1,
            type: "newspaper",
            active: true,
            column_width: null,
            width: null,
            deleted: false,
            dashboard_layout_components: [
              {
                id: 1,
                dashboard_layout_id: 1,
                dashboard_element_id: 1,
                row: 0,
                column: 0,
                width: 8,
                height: 4,
                deleted: false
              },
              {
                id: 2,
                dashboard_layout_id: 1,
                dashboard_element_id: 2,
                row: 0,
                column: 8,
                width: 8,
                height: 4,
                deleted: false
              }
            ]
          }
        ],
        elements: {
          1: {
            title: "Total Orders",
            title_hidden: false,
            vis_config: {
              type: "single_value",
              font_size: "medium",
              title: "Total Orders"
            }
          },
          2: {
            title: "Average Order Profit",
            title_hidden: false,
            vis_config: {
              type: "single_value",
              title: "Average Order Profit"
            }
          }
        }
      }
    }
    

Attribute | Format | Description  
---|---|---  
`dashboard.id` | Number/String | The ID of the dashboard.  
`dashboard.title` | String | The title, as shown at the top of the dashboard.  
`dashboard.canEdit` | Boolean |  ADDED 22.20  When `true`, the user can edit the dashboard.  
`dashboard.url` | String | The relative dashboard URL (just the path).  
`dashboard.absoluteUrl` | String | The full dashboard URL.  
`dashboard.dashboard_filters` | Object | The filters applied to the dashboard. This object has the format: `{"Filter name 1": "value 1", "Filter name 2": "value 2", ...}`  
`dashboard.options` | Object | The [dashboard layout](/looker/docs/reference/looker-api/latest/methods/Dashboard/dashboard_layout), [dashboard layout component](/looker/docs/reference/looker-api/latest/methods/Dashboard/dashboard_layout_component), and [dashboard element](/looker/docs/reference/looker-api/latest/methods/Dashboard/dashboard_element) properties and values. All properties returned in the `options` object can be given updated values using the `dashboard:options:set` event.  
  
#### `look:ready`

This event is created when a Look begins to load query data, whether the query runs or not.
    
    
    type: "look:ready",
    look: {
      url: "/embed/looks/...",
      absoluteUrl: "https://instance_name.looker.com/embed/looks/...",
      }
    }
    

Attribute | Format | Description  
---|---|---  
`look.url` | String | The relative Look URL (just the path)  
`look.absoluteUrl` | String | The full Look URL  
  
#### `look:run:start`

This event is created when a Look begins to load query data and the query begins to run.
    
    
    type: "look:run:start",
    look: {
      url: "/embed/looks/...",
      absoluteUrl: "https://instance_name.looker.com/embed/looks/...",
      }
    }
    

Attribute | Format | Description  
---|---|---  
`look.url` | String | The relative Look URL (just the path)  
`look.absoluteUrl` | String | The full Look URL  
  
#### `look:run:complete`

This event is created when a Look has finished running the query.
    
    
    type: look:run:complete
    look: {
      url: "/embed/looks/...",
      absoluteUrl: "https://instance_name.looker.com/embed/looks/...",
      }
    }
    

Attribute | Format | Description  
---|---|---  
`look.url` | String | The relative Look URL (just the path)  
`look.absoluteUrl` | String | The full Look URL  
  
#### `look:save:complete`

This event is created when a Look is edited and saved. This event is created when a user performs one of the following tasks:

  * [Clicks the **Edit** button to edit the Look](/looker/docs/saving-and-editing-looks#editing_looks) and then clicks **Save**
  * Saves a Look with the **Save** > **Save As…** menu option
  * Moves a Look from one folder to another

This event is not created if the Look is saved with the **Save** > **To existing dashboard** or **Edit Settings** menu option.
    
    
    type: look:save:complete
    look: {
      url: "/embed/looks/...",
      absoluteUrl: "https://instance_name.looker.com/embed/looks/...",
      folderid: 123
      }
    }
    

Attribute | Format | Description  
---|---|---  
`look.url` | String | The relative Look URL (just the path)  
`look.absoluteUrl` | String | The full Look URL  
`look.folderid` | Integer | The folder ID where the Look is stored  
  
#### `look:delete:complete`

This event is created when a Look is [moved to the **Trash** folder](/looker/docs/saving-and-editing-looks#deleting_a_look).
    
    
    type: look:delete:complete
    look: {
      url: "/embed/looks/...",
      absoluteUrl: "https://instance_name.looker.com/embed/looks/...",
      }
    }
    

Attribute | Format | Description  
---|---|---  
`look.url` | String | The relative Look URL (just the path)  
`look.absoluteUrl` | String | The full Look URL  
  
#### `drillmenu:click`

This event is created when a user clicks on a drill menu in a dashboard created with the [`link` LookML parameter](/looker/docs/reference/param-field-link). For example, the following LookML creates a drill menu where a user can view data filtered by the `state` dimension:
    
    
    dimension: state {
      type: string
      sql: ${TABLE}.state ;;
      link: {
        label: "Filter by {{ state | encode_uri }}"
        url: "filter::q={{ state | encode_uri }}"
        icon_url: "https://google.com/favicon.ico"
      }
    }
    
    

When the `state` filter is set to `Illinois`, the `drillmenu:click` event returns the following to the host of the iframe:
    
    
    type: "drillmenu:click",
    label: "Filter by Illinois",
    link_type: "url",
    modal: false,
    target: '_self',
    url: "#filter::state=Illinois"
    context: ' '
    

Attribute | Format | Description  
---|---|---  
`label` | String | The link label as shown on the drill menu  
`link_type` | String | The type of object at the link destination  
`modal` | Boolean | Whether the drill dialog box will be used instead of browser navigation  
`target` | String | Is `_self` if the link destination will replace the current iframe, `_blank` if the link destination will open a new window  
`url` | String | The URL of the link destination  
`context` | String | Internal attribute used by some types of visualizations  
  
[Sandboxing](https://www.w3schools.com/tags/att_iframe_sandbox.asp) the iframe will prevent drill menu clicks from opening in a new window. Use these sandboxing values inside the iframe tag:
    
    
    sandbox = "allow-same-origin allow-scripts"
    

#### `drillmodal:download`

This event is created when a user opens a drill dialog box from a dashboard tile and clicks the **Download** option.
    
    
    {
    type: "drillmodal:download",
    dashboard: {
      id: 23,
      title: "My Dashboard",
      url: "/embed/dashboards/…",
      absoluteUrl: "https://instance_name.looker.com/embed/dashboards/…",
      dashboard_filters: {
        "Date": "Last 28 days",
        "Total Orders": "Greater than 100"
      }
    }
    drillExploreUrl: "/embed...",
    fileFormat: "pdf"
    }
    

Attribute | Format | Description  
---|---|---  
`dashboard.id` | Number/String | The ID of the dashboard to which the tile belongs.  
`dashboard.title` | String | The dashboard title, as shown at the top of the dashboard to which the tile belongs.  
`dashboard.url` | String | The relative dashboard URL (just the path) to which the tile belongs.  
`dashboard.absoluteUrl` | String | The full dashboard URL to which the tile belongs.  
`dashboard.dashboard_filters` | Object | The filters applied to the dashboard to which the tile belongs. This object has the format: `{"Filter name 1": "value 1", "Filter name 2": "value 2", ...}`  
`drillExploreUrl` | String | The relative Explore URL (just the path) to be downloaded.  
`fileFormat` | String | The file format of the data download.  
  
#### `drillmodal:explore`

This event is created when a user clicks the **Explore From Here** option in a drill dialog box.
    
    
    type: "drillmodal:explore",
    label: "Explore From Here",
    url: "/embed/explore/model/view..."
    

Attribute | Format | Description  
---|---|---  
`label` | String | The button label as shown on the drill menu  
`url` | String | The relative Explore URL (just the path) to be viewed  
  
#### `explore:ready`

This event is created when an Explore begins to load query data, whether the query runs or not.
    
    
    type: "explore:ready",
    explore: {
      url: "/embed/explore/...",
      absoluteUrl: "https://instance_name.looker.com/embed/explore/...",
      }
    }
    

Attribute | Format | Description  
---|---|---  
`explore.url` | String | The relative Explore URL (just the path)  
`explore.absoluteUrl` | String | The full Explore URL  
  
#### `explore:run:start`

This event is created when an Explore begins to load query data and the query begins to run.
    
    
    type: "explore:run:start",
    explore: {
      url: "/embed/explore/...",
      absoluteUrl: "https://instance_name.looker.com/embed/explore/...",
      }
    }
    

Attribute | Format | Description  
---|---|---  
`explore.url` | String | The relative Explore URL (just the path)  
`explore.absoluteUrl` | String | The full Explore URL  
  
#### `explore:run:complete`

This event is created when an Explore has finished running the query.
    
    
    type: "explore:run:complete",
    explore: {
      url: "/embed/explore/...",
      absoluteUrl: "https://instance_name.looker.com/embed/explore/...",
      }
    }
    

Attribute | Format | Description  
---|---|---  
`explore.url` | String | The relative Explore URL (just the path)  
`explore.absoluteUrl` | String | The full Explore URL  
  
#### `explore:state:changed`

This event is created when an Explore page URL changes as a result of the user's actions.
    
    
    type: "explore:state:changed",
    explore: {
      url: "/embed/explore/...",
      absoluteUrl: "https://instance_name.looker.com/embed/explore/..."
    }
    

Attribute | Format | Description  
---|---|---  
`explore.url` | String | The relative Explore URL (just the path)  
`explore.absoluteUrl` | String | The full Explore URL  
  
#### `page:changed`

This event is created when a user navigates to a new page within the iframe.
    
    
    type: "page:changed",
    page: {
      type: "dashboard",
      url: "/embed/dashboards/...",
      absoluteUrl: "https://instance_name.looker.com/embed/dashboards/..."
    }
    

Attribute | Format | Description  
---|---|---  
`page.type` | String | The type of page that has just been navigated to, such as `"dashboard"`, `"look"`, or `"explore"`  
`page.url` | String | The relative URL (just the path) of the page that has just been navigated to  
`page.absoluteUrl` | String | The full URL of the page that has just been navigated to  
  
#### `page:properties:changed`

This event is created when the height of a dashboard iframe changes. It is not available for Looks or Explores because those items automatically adjust their height to the size of the iframe.
    
    
    type: "page:properties:changed",
    height: 1000
    

Attribute | Format | Description  
---|---|---  
`height` | Integer | The height of the dashboard iframe in pixels  
  
#### `session:tokens`

This event indicates that the Looker client requires tokens to continue. This event is created immediately on creation of the iframe and periodically afterwards for the duration of the session.
    
    
    {
      "type": "session:tokens",
      "api_token": "eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3NlbGYtc2lnbmVkLmxvb2tlci5jb206OTk5OSIsImV4cCI6MTY3MDYyNjMzMCwic3ViIjoiYVdrNWFGUzM4RnRwNzFFWXhuS3ZaMXdKRmV3ZjB2VzYtTV9zLWtCcHE1dXIiLCJ0b2tlbl90eXBlIjoiYXBpX3Rva2VuIiwicmFuZG9taXplciI6IkxjYnpOeDNTVjNOb3o3UVlqTVJjNmhlMkdodjh1a2UwWUhiZWNRMHVCYm1KIn0.CBv1__QGc_H7bKNe31SHMMQCsc5ya1xOiEv1UDWAyxM",
      "api_token_ttl": 463,
      "navigation_token": "eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3NlbGYtc2lnbmVkLmxvb2tlci5jb206OTk5OSIsImV4cCI6MTY3MDYyNjMzMCwic3ViIjoiYVdrNWFGUzM4RnRwNzFFWXhuS3ZaMXdKRmV3ZjB2VzYtTV9zLWtCcHE1dXIiLCJ0b2tlbl90eXBlIjoibmF2aWdhdGlvbl90b2tlbiIsInJhbmRvbWl6ZXIiOiJHVVNlc00tdTRPRDlNdktodFJDU2pEcVFhUkJNeTh5dm42Q1FDUXhuLTNxMiJ9.sWo7LUEI5LeragVmeDamUR7u2myXpFJ0aqK_IIALUqI",
      "navigation_token_ttl": 463,
      "session_reference_token_ttl": 2924
    }
    

Attribute | Format | Description  
---|---|---  
`authentication_token` | String | Authentication token. Included when the iframe is created. Not included with a response to a request to generate tokens or if the session has expired.  
`authentication_token_ttl` | Number | Authentication token time to live in seconds. Included when the iframe is created. Not included with a response to a request to generate tokens or if the session has expired.  
`api_token` | String | API token. Not included if the session has expired.  
`api_token_ttl` | Number | API token time to live in seconds. Not included if the session has expired.  
`navigation_token` | String | Navigation token. Not included if the session has expired.  
`navigation_token_ttl` | Number | Navigation token time to live in seconds. Not included if the session has expired.  
`session_references_token_ttl` | Number | Session time to live in seconds. The value will be 0 when the session has expired. To recover, the embedding application must acquire a new session.  
  
#### `session:status`

The event is generated when the embedded Looker application handles requests for session tokens.
    
    
    {
      "type": "session:status",
      "session_ttl": 0,
      "expired": true,
      "interrupted": false
    }
    

Attribute | Format | Description  
---|---|---  
`session_ttl` | Number | Session time to live in seconds.  
`expired` | Boolean | When `true`, indicates the session has expired.  
`interrupted` | Boolean | When `true`, indicates that a request for session tokens was not responded to. This could indicate that a server is temporarily unavailable.  
`recoverable` | Boolean | Only populated when interrupted is `true`. Indicates whether the session can be recovered or not. A value of `false` likely means there is a problem with the embedding application.  
  
#### `env:client:dialog`

The event is generated when a dialog box has been opened that may partially be out of view, such as a drill dialog box. This event enables the hosting application to scroll the dialog box into view with the `env:host:scroll` action.
    
    
    {
      type: "env:client:dialog",
      dialogType: 'drilling',
      placement: 'cover',
      open: true
    }
    

Attribute | Format | Description  
---|---|---  
`type` | String | `env:client:dialog` indicates that a dialog box has been opened or closed. Currently, only the drill dialog box is supported, but other dialog boxes may be added in the future. It is possible that the top of the drill dialog box is not in view since the dialog box covers the iframe viewport. This event allows the host application to scroll the top of the dialog box into view.  
`dialogType` | String | The type of dialog box. Currently only the opening or closing of the "drilling" dialog type triggers this event.  
`placement` | String | The placement of the dialog. Dialog boxes of type "drilling" always use a `placement` of "cover".  
`open` | Boolean | Indicates whether the dialog is opened or scrolled.  
  
## Making changes to the iframe

After you've prepped your iframe for data retrieval, you can make changes to the iframe with the following steps:

  1. Write your request in JSON.
  2. Post the request to the iframe's `contentWindow`.

### Writing your request in JSON

You can make several changes to the iframe, which you'll submit in JSON form. The available options are described in the Action reference section on this page. Don't forget to use `JSON.stringify` to turn your action into JSON, like this:
    
    
    var my_request = JSON.stringify(
      {
        type: "dashboard:run"
      }
    );
    

### Posting the request to the iframe's `contentWindow` property

Finally, post your message to the iframe's `contentWindow`, like this:
    
    
    var my_iframe = document.getElementById("my_iframe_id");
    
    my_iframe.contentWindow.postMessage(my_request, 'https://instance_name.looker.com');
    

### Action summary table

The following table summarizes actions. Select an action to see the details about that action.

Action | Action Description  
---|---  
`dashboard:load` | Loads a new dashboard in the iframe, replacing an existing dashboard.  
`dashboard:run` | Runs the dashboard in the iframe.  
`dashboard:edit` |  ADDED 22.20  Switches the dashboard into [edit mode](/looker/docs/editing-user-defined-dashboards#entering_edit_mode_in_dashboards).  
`dashboard:filters:update` | Updates an existing dashboard filter in the iframe.  
`dashboard:options:set` | Writes new values to dashboard layout and dashboard element properties.  
`dashboard:schedule_modal:open` | Opens the Scheduler, which lets users deliver Looker content to various destinations.  
`dashboard:stop` | Stops a dashboard that is running or reloading data.  
`look:run` | Runs the Look in the iframe.  
`look:filters:update` | Updates an existing Look filter in the iframe.  
`explore:run` | Runs the Explore in the iframe.  
`explore:filters:update` | Updates or removes an existing Explore filter in the iframe.  
`session:tokens:request` | Sends tokens in response to a `session:tokens:request` event.  
`env:host:scroll` | Sends information about the current scroll position of the host iframe to the embedded Looker application.  
  
### Action reference

These are the available actions you can post to the embedded iframe:

#### `dashboard:load`

Use this action to load a new dashboard in the iframe, replacing an existing dashboard. The new dashboard will begin executing queries as if a new dashboard page had been opened.
    
    
    {
      type: "dashboard:load",
      id: "101",
      pushHistory: false
    }
    

Attribute | Format | Description  
---|---|---  
`type` | String | Using the type `dashboard:load` indicates that you want to load a new dashboard into the iframe.  
`id` | String | The ID of the dashboard to load.  
`pushHistory` | Boolean | If `true`, the dashboard loaded creates a new browser history entry, and the user can use the browser's back button to return to the previous dashboard. If `false`, the current dashboard is replaced and browser navigation cannot be used to return to it.  
  
#### `dashboard:run`

Use this action to run the dashboard in the iframe. This is the same action as hitting the **Run** or **Reload Data** button on the dashboard.
    
    
    {
      type: "dashboard:run"
    }
    

Attribute | Format | Description  
---|---|---  
`type` | String | Using the type `dashboard:run` indicates that you want to run the dashboard.  
  
#### `dashboard:edit`

ADDED 22.20  Use this action to switch an existing dashboard in the iframe to [edit mode](/looker/docs/editing-user-defined-dashboards#entering_edit_mode_in_dashboards). This is the same action as selecting **Edit dashboard** from the dashboard menu.
    
    
    {
      type: "dashboard:edit"
    }
    

Attribute | Format | Description  
---|---|---  
`type` | String | Using the type `dashboard:edit` indicates that you want to switch the dashboard into [edit mode](/looker/docs/editing-user-defined-dashboards#entering_edit_mode_in_dashboards).  
  
#### `dashboard:filters:update`

Use this action to update an existing dashboard filter in the iframe. You cannot add a new filter to the dashboard by using this method.
    
    
    {
      type: "dashboard:filters:update",
      filters: {
        "Sale date": "Last 28 days",
        "Sale amount": "Greater than 100"
      }
    }
    

Attribute | Format | Description  
---|---|---  
`type` | String | Using the type `dashboard:filters:update` indicates that you want to update the filters used by the dashboard.  
`filters` | Object | The new filters you want to apply to the dashboard. This object has the format: `{"Filter name 1": "value 1", "Filter name 2": "value 2", ...}`  
  
#### `dashboard:options:set`

This action is available after the `dashboard:run:complete` event occurs.

The embedder creates the message and sends it to the iframe, but the dashboard does not respond until after `dashboard:run:complete` occurs. The `dashboard:options:set` action writes new values to dashboard layout and dashboard element properties. Only properties that have been returned in the `options` attribute of the `dashboard:run:complete` event can be updated using `dashboard:options:set`. Any properties set that were not previously returned by the `options` attribute of the `dashboard:run:complete` event are ignored.
    
    
    {
      type: "dashboard:options:set",
      layouts: [
        {
          id: 1,
          dashboard_id: 1,
          type: "newspaper",
          active: true,
          column_width: null,
          width: null,
          deleted: false,
          dashboard_layout_components: [
            {
              id: 1,
              dashboard_layout_id: 1,
              dashboard_element_id: 1,
              row: 0,
              column: 0,
              width: 8,
              height: 4,
              deleted: false
            },
            {
              id: 2,
              dashboard_layout_id: 1,
              dashboard_element_id: 2,
              row: 0,
              column: 8,
              width: 8,
              height: 4,
              deleted: false
            }
          ]
        }
      ],
      elements: {
        1: {
          title: "Total Orders",
          title_hidden: false,
          vis_config: {
            type: "single_value",
            font_size: "medium",
            title: "Total Orders"
          }
        },
        2: {
          title: "Average Order Profit",
          title_hidden: false,
          vis_config: {
            type: "single_value",
            title: "Average Order Profit"
          }
        }
      }
    }
    

Attribute | Format | Description  
---|---|---  
`type` | String | Using the type `dashboard:options:set` indicates that you want to write new values to dashboard layout and dashboard element properties.  
`layouts` | Object | The [dashboard layout](/looker/docs/reference/looker-api/latest/methods/Dashboard/dashboard_layout) properties returned by the `options` attribute in the `dashboard:run:complete` event. These will be in a format similar to: 

  * `id: "string",`
  * dashboard_id: "string",
  * type: "newspaper",
  * active: boolean,
  * column_width: number,
  * width: number

  
`layouts.dashboard_layout_components` | Object | One or more [dashboard layout component](/looker/docs/reference/looker-api/latest/methods/Dashboard/dashboard_layout_component) objects returned by the `options` attribute in the `dashboard:run:complete` event. These will be in a format similar to:

  * `id: "string",`
  * dashboard_layout_id: "string",
  * dashboard_element_id: "string",
  * row: number,
  * column: number,
  * width: number,
  * height: number,
  * deleted: boolean,

  
`elements` | Object | One or more [dashboard element](/looker/docs/reference/looker-api/latest/methods/Dashboard/dashboard_element) objects returned by the `options` attribute in the `dashboard:run:complete` event. These will be in a format similar to:`id: { title: "string", title_hidden: boolean, vis_config: { type: "string", title: "string" }}`  
  
#### `dashboard:schedule_modal:open`

Use this action to open the Scheduler, which lets users [deliver Looker content](/looker/docs/scheduling) to various destinations.
    
    
    {
      type: "dashboard:schedule_modal:open"
    }
    

Attribute | Format | Description  
---|---|---  
`type` | String | Using the type `dashboard:schedule_modal:open` indicates that you want to open the **Schedule** dialog box.  
  
#### `dashboard:stop`

Use this action to stop a dashboard that is running or reloading data. This is the same action as clicking the **Cancel** button on the dashboard. A dashboard stopped using `dashboard:stop` sends a `dashboard:run:complete` event with `status:` set to `"stopped"`.
    
    
    {
      type: "dashboard:stop"
    }
    

Attribute | Format | Description  
---|---|---  
`type` | String | Using the type `dashboard:stop` indicates that you want to stop the running dashboard.  
  
#### `look:run`

Use this action to run the query on which the Look is based in the iframe. This action is similar to hitting the **Run** button on the Look, with the exception that `look:run` always queries the database directly and does not retrieve data from the [Looker cache](/looker/docs/caching-and-datagroups).
    
    
    {
      type: "look:run"
    }
    

Attribute | Format | Description  
---|---|---  
`type` | String | Using the type `look:run` indicates that you want to run the Look.  
  
#### `look:filters:update`

Use this action to update an existing Look filter in the iframe. You cannot add a new filter to the Look by using this method.
    
    
    {
      type: "look:filters:update",
      filters: {
        "orders.created_at": "90 days",
        "products.department": "sweaters"
      }
    }
    

Attribute | Format | Description  
---|---|---  
`type` | String | Using the type `look:filters:update` indicates that you want to update the filters used by the Look.  
`filters` | Object | The new filters you want to apply to the Look. This object has the format: `{"view_name.field_name_1": "value 1", "view_name.field_name_1": "value 2", ...}`  
  
#### `explore:run`

Use this action to run the Explore in the iframe. This action is similar to hitting the **Run** button on the Explore, with the exception that `explore:run` always queries the database directly and does not retrieve data from the [Looker cache](/looker/docs/caching-and-datagroups).
    
    
    {
      type: "explore:run"
    }
    

Attribute | Format | Description  
---|---|---  
`type` | String | Using the type `explore:run` indicates that you want to run the Explore.  
  
#### `explore:filters:update`

Use this action to update or remove an existing Explore filter in the iframe. Including a new filter that references a valid field will add the new filter to the Explore.
    
    
    {
      type: "explore:filters:update",
      filters: {
        "orders.created_at": "90 days",
        "orders.status": "complete"
      }
      deleteFilters:  ["products.department"]
    }
    

Attribute | Format | Description  
---|---|---  
`type` | String | Using the type `explore:filters:update` indicates that you want to update the filters used by the Explore.  
`filters` | Object | The new filters you want to apply to the Explore. If `filters` includes a filter that does not currently exist in the Explore but that does reference a valid field, that filter will be added to the Explore. This object has the format: `{"view_name.field_name_1": "value 1", "view_name.field_name_1": "value 2", ...}`  
`deleteFilters` | Array | The existing filters you want remove from the Explore. The array has the format: `["view_name.field_name_1", "view_name.field_name_2", ...]`  
  
#### `session:tokens:request`

Use this action to send tokens in response to a `session:tokens:request` request.
    
    
    {
      type: "session:tokens:request",
    }
    

Attribute | Format | Description  
---|---|---  
`type` | String | Using the type `session:tokens:request` indicates that you want to send tokens in response to a `session:tokens:request` event.  
  
#### `env:host:scroll`

Use this action to send information about the current scroll position of the host iframe to the embedded Looker application.
    
    
    {
      type: "env:host:scroll",
      offsetTop: 10,
      offsetLeft: 10,
      scrollX: 5,
      scrollY: 5
    }
    

Attribute | Format | Description  
---|---|---  
`type` | String | Using the type `env:host:scroll` indicates that you want to send information about the current scroll position of the host iframe to the embedded Looker application.  
`offsetTop` | Number | The offset top of the iframe.  
`offsetLeft` | Number | The offset left of the iframe.  
`scrollX` | Number | The scrollX position of the application host.  
`scrollY` | Number | The scrollY position of the application host.