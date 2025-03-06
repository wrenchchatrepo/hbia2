# https://cloud.google.com/looker/docs/blocks

Depth: 3

Looker Blocks™ are prebuilt data models for common analytical patterns and data sources. Reuse the work others have already done rather than starting from scratch, then customize the blocks to your exact specifications. From optimized SQL patterns to fully built-out data models, Looker Blocks can be used as a starting point for quick and flexible data modeling in Looker.

## Available blocks

There are many Looker Blocks to choose from. To see what blocks are available, check out the **Blocks** section of the [Looker Marketplace](https://marketplace.looker.com/marketplace/directory?Type=tools).

**Note:** Looker Blocks were created to make analyzing data easier and more efficient. They are available on an "as is" basis, meaning there won't be updates moving forward. Looker cannot represent or warrant that this data will be accurate, reliable, or error-free. Consult the documented data source sites for details on how their data is being collected and how to interpret it.

Click a block that interests you to see its specific usage instructions.

Some Looker Blocks can be installed quickly using the [Looker Marketplace](/looker/docs/marketplace). Before you can deploy a block through the Looker Marketplace, a Looker admin must have enabled the [**Marketplace**](/looker/docs/admin-panel-platform-marketplace) feature. See the [Looker Marketplace](/looker/docs/marketplace) documentation page for more information about installing and customizing Looker Blocks, available from the Looker Marketplace.

## Standardization and customization

The ease of using the different blocks will vary, depending on the degree to which your database schema is standardized. Most Looker Blocks require some customization to fit your data schema, with the exception of data blocks, which are the simplest to implement but are not customizable.

  * Data blocks, which include both public datasets and full LookML models, simply require copying the LookML model from the GitHub repo to access the modeled tables. See Using data blocks on this page for detailed instructions.

  * Data collection applications, such as Segment and Snowplow, track events in a relatively standardized format. This makes it possible to create templatized design patterns — capable of data cleansing, transformation, and analytics — that can be used by any customer using these applications.

  * Other web applications — such as Salesforce — let you add custom fields for your internal users. Naturally, this creates data in a less standardized format. As a result, we can templatize some of the data model to get the analytics up and running, but you'll need to customize the non-standardized portion.

  * Finally, we have blocks for general business insights. These are optimized SQL or LookML design patterns that are data-source agnostic. For example, many companies will want to analyze the lifetime value of a customer over time. There are some assumptions baked into these patterns, but they can be customized to match your specific business needs. These patterns reflect Looker's point of view on the best way to conduct certain types of analysis.

If you're new to Looker, your Looker analyst can help you get the most from these models.

### Adding blocks to your LookML

  * Some blocks demonstrate both Explores and views in the same file. This is for ease of viewing, but in general you'll want to copy the appropriate sections of LookML into the appropriate places in your data model. See the [Understanding model and view files](/looker/docs/model-and-view-files#creating_model_files) documentation page for more information.
  * In some cases you'll probably want to create new LookML files in your data model to house the examples.

## Using data blocks

Data blocks are a special type of Looker Block that provide the dataset as well as the data model. Looker Data Blocks include public data sources, such as:

  * **Demographic data** : Common demographic metrics from the American Community Survey at the state, county, zip code tabulation area, and even census block group level.
  * **Weather data** : Weather reporting in the United States at the zip code level from 1920 through the previous day. This block is updated nightly.

To see the full list available blocks, see the **Blocks** section of the [Looker Marketplace](https://marketplace.looker.com/marketplace/directory?Type=tools).

### Accessing datasets on different databases

The procedure for accessing a data block's dataset varies depending on your database schema. The following sections contain instructions for accessing datasets on these databases:

  * Google BigQuery
  * Additional databases

#### Accessing datasets on Google BigQuery

If you have an existing Google BigQuery account, you can access Looker's BigQuery-hosted datasets. Skip ahead to the Adding data blocks to projects section on this page.

If you don't already have a Google BigQuery account, you can set up a free trial and then access Looker's public datasets on BigQuery.

**Caution:** Google BigQuery does not support project sharing across regions. To directly access data blocks in Google BigQuery from outside the US region, you can: 

  * Import Looker's public data from [Google Cloud Services or Amazon S3](/looker/docs/blocks#accessing_datasets_on_other_databases). 
  * Create a new Google BigQuery connection based in the US region. 

#### Accessing datasets on other databases

Are you on Amazon Redshift, MySQL, PostgreSQL, or Oracle?

We've made the transformed data for each of these datasets publicly available in both Google Cloud Service and S3 so that you can directly import them into the database of your choice.

We've also made the Data Definition Language (DDL) available for each of the datasets in the GitHub Repo. The DDL statements might need to be modified for the datatypes in your selected database, but should provide an idea of the column types for each table.

Download data directly from one of these locations:

  * **Google Cloud Service** : `_gs://looker-datablocks/_`
  * **S3** : `_s3://looker-datablocks/_`
  * **S3 Bucket Web Link** : <http://looker-datablocks.s3-website-us-east-1.amazonaws.com/>

### Accessing the LookML model

Fork one of our GitHub repositories into a new GitHub repository (either hosted by Looker or by your company) that you can then [extend](/looker/docs/reusing-code-with-extends) or [refine](/looker/docs/lookml-refinements) within your instance:

  * Demographic Data (American Community Survey) - <https://github.com/llooker/datablocks-acs>
  * Weather (GSOD) - <https://github.com/llooker/datablocks-gsod>

### Adding data blocks to projects

In addition to the method described in this section, you can also use [LookML refinements](/looker/docs/lookml-refinements) to build on the LookML of views and Explores in your projects.

To add a data block to your project:

  1. [Add a new project](/looker/docs/generating-a-model) to your Looker instance.

  2. [Fork](https://guides.github.com/activities/forking/) or copy the GitHub repositories mentioned previously to access prebuilt LookML. Be sure to create a new GitHub repo.

  3. Remove other database dialect files from the repo. Looker Blocks will typically contain files for Google BigQuery, Amazon Redshift, and Snowflake. For example, if you are setting up data blocks on Google BigQuery, you will _only_ need the Google BigQuery view files, Google BigQuery Explore file, and Google BigQuery model file.

  4. Replace the connection name in your model file with your database connection where the data for data blocks lives. If you are using Google BigQuery or Snowflake, use the database connection from which you will be extending or refining.

All join logic exists in an `.explore` file in each of the repositories. This is the file you will be including in the following steps, after you have set up your project manifest.

  5. In your main Looker project where you will be extending or refining data blocks, [create a project manifest file](/looker/docs/importing-projects#creating_a_project_manifest_file).

  6. Add the following LookML to the project manifest file to reference data blocks in your main Looker project:

    
    
        project_name: "<your_project_name\>"
    
        local_dependency: {
          project: "<project_name_of_datablock\>"
        }
    

#### Setup considerations and options

**Google BigQuery** : Be sure to use the correct set of modeled files. If you are on Google BigQuery, you may want to reference all files with `_bq_` in the filename. You may have to adapt our Google BigQuery model dialects to your own database dialect.

**Caution:** Google BigQuery does not support project sharing across regions. To directly access data blocks in Google BigQuery from outside the US region, you can: 

  * Import Looker's public data from [Google Cloud Services or Amazon S3](/looker/docs/blocks#accessing_datasets_on_other_databases). 
  * Create a new Google BigQuery connection based in the US region. 

**Extensions** : All our projects have been set up to allow for extensions from Explore files, since model extensions could cause issues with multiple connections.

**Joining Derived Tables** : You may want to take a look at our documentation for [native derived tables](/looker/docs/creating-ndts). You can let Looker write SQL for you at different levels of aggregation on our publicly available datasets and join them into your model.

**Merging Result Sets** : You can also choose to [merge result sets](/looker/docs/merged-results) from our datasets with your data by combining query result sets.

### Example setup of the demographic dataset

  1. Get access to data by either downloading raw data from our S3 or Google Cloud Service buckets or by connecting to a Looker database.

  2. Import the **Demographic Data Block** model from LookML as a separate project in your Looker instance.

  3. Use the [`include`](/looker/docs/reference/param-model-include) parameter to bring in the view file.

  4. Then either [extend](/looker/docs/reusing-code-with-extends) or [refine](/looker/docs/lookml-refinements) the view file, or make use of [native derived tables](/looker/docs/creating-ndts) to get data at the level of aggregation that is necessary for Explores.

In our example, since the demographic data is at a different level of aggregation than our e-commerce dataset (block group vs. zip code) we use native derived tables to aggregate stats up to the zip code level. This eliminates messy many-to-many joins:
    
          include: "/american_community_survey/bq.explore"
    
      view: zipcode_income_facts {
        derived_table: {
          persist_for: "10000 hours"
          explore_source: fast_facts {
            column: ZCTA5 { field: tract_zcta_map.ZCTA5 }
            column: income_household { field: bg_facts.avg_income_house }
            column: total_population { field: bg_facts.total_population }
          }
        }
        dimension: ZCTA5 {}
        dimension: income_household {
          hidden: yes
        }
    

  5. Join view files into the model:
    
          include: "acs*.view"
    
      explore: order_items {
        join: users {
          sql_on: ${users.id} = ${order_items.user_id} ;;
          type: left_outer
          relationship: many_to_one
        }
    
        join: zipcode_income_facts {
          sql_on: ${users.zip} = ${zipcode_income_facts.ZCTA5} ;;
          type: left_outer
          relationship: many_to_one
        }
      }
    

  6. [Explore](/looker/docs/creating-and-editing-explores) and [visualize](/looker/docs/creating-visualizations) the data.

## Using viz blocks

Looker includes a variety of built-in [visualization types](/looker/docs/visualization-types). However, if, you have charting needs that are not covered by Looker's built-in visualization types, you can also add your own [custom visualization](/looker/docs/admin-panel-platform-visualizations) types. You can also [develop a custom visualization](/looker/docs/marketplace-develop-visualization) and make it available to all Looker users from the Looker Marketplace.

Viz blocks are prebuilt JavaScript visualization types that are hosted by Looker. You can add the Viz blocks to your Looker instance, and they will act similarly to any of Looker's built-in visualization types: they appear on the visualization menu bar, and they include core functionality such as drilling, downloading, embedding, and scheduling.

To learn more about a viz block, select the visualization type in the [**Plug-ins** section of the Looker Marketplace](https://marketplace.looker.com/marketplace/directory?Type=visualizations), then click **See the Code** and navigate to the viz block's `READ.ME` file. The `READ.ME` file shows an example of the visualization and gives more information about the viz block. For some visualizations, the `READ.ME` file also provides a URL and instructions for adding the viz block.

To add the visualization type to your instance, see the instructions in the `READ.ME` file (if any) and the information on our [Visualizations](/looker/docs/admin-panel-platform-visualizations) documentation page.