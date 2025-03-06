# https://cloud.google.com/looker/docs/studio/about-data-sources

Depth: 3

A data source acts as a conduit between the data in an external platform or product, such as a database or spreadsheet, and the charts and controls in a Looker Studio report. When you create a new report in Looker Studio, you either add an existing _data source_ , or create and add a new one. You can add more data to the report at any time.

The following sections explain how data sources fit into the big picture of Looker Studio.

## Data model

Having a consistent definition for the metrics and dimensions that are shared across your business provides a common platform for data analysis.

Data sources provide the structure (schema) of the fields you or other report editors can use to create your reports. The data source is where you [model your data](/looker/docs/studio/model-your-data): for example, by creating calculated fields, adding parameters, and adjusting data types.

## Data sources and connectors

Data sources use _connectors_ to fetch your data from a specific platform, system, or product. You can use free connectors built by Google to access data such as Google Sheets, Google Ads, Google Analytics, and other Google Marketing Platform products, and more. You can also use connectors built by Looker Studio partners through the [Community Connectors developer program](https://developers.google.com/looker-studio/connector/).

**Note:** Community connectors may cost money to use. If you have issues using a community connector, please contact that connector's developer directly.

Visit the [Connector Gallery](https://lookerstudio.google.com/data).

## How (and when) data sources fetch data

Most data sources maintain a **live connection** to your data. Your data remains in the underlying dataset and is not imported into Looker Studio except as needed to answer a specific request. That data is kept only temporarily.

**Note:** The data freshness option lets you set how often a particular data source will request fresh data. Until that threshold is reached, Looker Studio will try to answer queries that are issued by the report from the data in memory. Answering queries with data that's already in memory can be much faster than fetching the data from the underlying dataset. Learn more about [managing data freshness](/looker/docs/studio/manage-data-freshness).

For even faster performance, you can use an **extracted data source**. The [Extract data connector](/looker/docs/studio/extract-data-for-faster-performance) creates a static snapshot of your data. The extracted data is stored securely in Looker Studio, and you can update the snapshot whenever you want.

**File upload data sources** let you import CSV data into Looker Studio. By using a file upload data source, you can visualize information not otherwise supported by the other connectors. File upload data sources behave in many ways like extracted data sources, except you can't update them automatically. You must import new data manually.

## Control access to the data

Access to the data that is provided by a data source is handled by **data credentials** :

  * **Owner's credentials** uses the credentials of the data source owner to authorize access to the dataset. This option lets you share reports that use this data source without requiring report viewers to have their own access to the underlying dataset.

**Important:** Before sharing a report or data source that uses Owner's credentials, be sure that you trust the person or persons with whom you share them.
  * **Viewer's credentials** require anyone who attempts to view the data that is provided by this data source to have their own access to the dataset.

  * **Service account credentials** use a special type of Google account that is intended to represent a non-human user that can authenticate and be authorized to access your data.

Learn more about [data credentials](/looker/docs/studio/data-credentials).

### Filter data by email address of the viewer

Filtering a data source by viewer email address lets you provide "row-level" security over the data. Only the records in your data containing the signed-in viewer's email appear in the report.

[Learn more](/looker/docs/studio/filter-by-email-address).

## Embedded versus reusable data sources

Data sources can be either _embedded_ or _reusable._ Reports can include both embedded and reusable data sources.

**Data sources that you create while editing a report are embedded** in the report. To edit an embedded data source, you do so within that report. Embedded data sources make collaborating on reports and data sources easier. Anyone who can edit the report can also edit the data source as well as modify its connection. When you share or copy the report, any embedded data sources are shared or copied as well.

**Data sources that you create from the home page are reusable**. You can reuse these data sources in different reports. Reusable data sources let you create and share a consistent data model across your organization. Only people with whom you share the reusable data source can edit it. Only the owner of the data source's credentials can modify the connection.

> To see whether the data sources in a report are embedded or reusable:
> 
>   1. [Edit your report](/looker/docs/studio/edit-a-report).
>   2. In the menus, select **Resource > Manage added data sources**.
> 

## Share and copy data sources

When you share or copy a report, all of its embedded data sources are shared or copied along with it. You don't need to share embedded data sources separately from the report. This means that other report editors can modify the data source.

Reusable data sources aren't copied or shared when you copy or share a report. If you want someone else to be able to modify a reusable data source, then you must share it with them explicitly.

Note that you don't need to share a reusable data source in order for viewers of the report to see the data, or for editors to use the fields provided by the data source to create charts and controls in the report.

[Learn more about sharing reports and data sources](/looker/docs/studio/invite-others-to-your-reports).

## Related resources

  * [Share with viewers and editors](/looker/docs/studio/invite-others-to-your-reports)
  * [Blend multiple data sources in a chart](/looker/docs/studio/how-blends-work-in-looker-studio)