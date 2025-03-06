# https://cloud.google.com/looker/docs/looker-cicd-usage

Depth: 3

This page explains how to use a CI/CD workflow in Looker after such a workflow has been [installed and configured](/looker/docs/looker-cicd-installation).

These instructions use a three-tier system that comprises development, QA, and production. However, you can apply the same principles to a two-tier or four-tier system.

These instructions also assume the use of GitHub as your Git provider. You _can_ use other Git providers to create a CI/CD workflow; however, you must possess the expertise to modify these instructions for your provider.

## Workflow overview

LookML developers begin by writing code in their development branch, which is normally named something like `dev-my-user-ydnv`, test their changes with [Spectacles](/looker/docs/looker-cicd-installation#installing_spectacles), and commit their code. Finally, they open a pull request to merge their code with the `main` branch.

When the Pull Request is opened, it brings the developer to GitHub. The developer should write a meaningful PR title using conventional commits style and add a comment to the description that will be included in the changelog. The results of the Spectacles tests should be added as comments to the PR.

Next, the developer should select a reviewer in GitHub. The reviewer will receive a notification and can add their review to the PR. If the reviewer approves the change, the PR is merged with the `main` branch. A WebHook is called and the development environment now sees the change.

Automatically, the [Release Please automation](/looker/docs/looker-cicd-installation#release_please) will run and open a second PR to create a new tagged release. Or, if there is already a PR open for this purpose, Release Please updates that PR. The release PR has a version number associated with it, as well as a changelog that includes the titles and descriptions of the included changes.

When the Release Please generated PR is approved and merged, a new version tag is generated and the changelog is merged with the `main` branch. The QA and production instances of Looker can select this version using [Advanced Deploy Mode](/looker/docs/advanced-deploy-mode).

## Best practices for numbering releases and naming commits

The releases and their associated tags can be named and numbered in any way that makes sense in your environment. However, [Semantic Versioning](https://semver.org/) is used here, and is highly suggested because it works well with the [Release Please plugin](/looker/docs/looker-cicd-installation#release_please).

In Semantic Versioning the version consists of three numbers separated by periods: `MAJOR.MINOR.PATCH`

  * `PATCH` is incremented every time a release fixes a bug
  * `MINOR` is incremented and `PATCH` is set back to zero every time the release adds or refines a feature while being backward compatible
  * `MAJOR` is incremented and both `MINOR` and `PATCH` are set to zero when a feature is added that is _not_ backward compatible

[Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) is a system of naming commits by the impact they have on end users. While not required, the use of conventional commit naming is also useful for the Release Please plugin.

In conventional commit naming, each commit message is prepended with an indicator of the scope of the change:

  * A bug fix is indicated with `fix:` like `fix: set proper currency symbol on sale_amt format`
  * A new feature is indicated with `feat:` like `feat: added explore for sales by territory`
  * A feature with a breaking change is indicated by `feat!:` like `feat!: rewrote sales explore to use the new calendar view`
  * When docs are updated, but LookML is not changed, the commit message starts with `doc:`

If conventional commits are used consistently, determining the semantic number to be used next is generally straightforward. If the commit log only consists of `fix:` and `doc:` commits, the `PATCH` should be incremented. If there is a `feat:` commit then `MINOR` should be incremented. If there is a `feat!:` then `MAJOR` should be incremented. The Release Please plugin can even generate a CHANGELOG file and tag the release automatically.

## Using Advanced Deploy Mode

After changes are made and submitted as a PR on the development instance the [Release Please plugin](/looker/docs/looker-cicd-installation#release_please) will tag the changes with a version tag like `v1.2.3`. Looker's [Advanced Deploy Mode](/looker/docs/advanced-deploy-mode) then makes these versions available in the Looker UI for the QA and production instances.

To deploy a change, choose the Deployment Manager from the Looker IDE:

![Looker Deployment Manager location in IDE.](/static/looker/docs/images/cicd-deployment-manager.png)

Click the **Select Commit** link in the upper right of the Deployment Manager. Next, select the three-dot menu that is associated with the tag that you want to deploy, and choose **Deploy to Environment** :

![Looker Deployment Manager UI for deploying to environment.](/static/looker/docs/images/cicd-deployment-mgr-a.png)

You don't need to tag the deployment again, so choose **Deploy without tagging** and press the **Deploy to Environment** button:

![Looker Deployment Manager UI for deploying without tagging.](/static/looker/docs/images/cicd-deployment-mgr-b.png)

Finally, push to production using the Deployment Manager.

## Using Spectacles

Spectacles can be used by each developer to verify their changes while they are still in their development branch. Spectacles offers four different validators:

  * SQL
  * LookML
  * Content
  * Assert

When a developer submits a pull request, it's good practice to run these tests and copy the results to a comment in the PR.

### SQL Validator

The SQL Validator tests each Explore to ensure that all the fields defined in LookML Views correspond to actual SQL columns or valid SQL expressions in the database. The SQL Validator is called as shown next:
    
    
    $ spectacles sql --config-file config-dev.yaml \
        --project PROJECT_NAME \
        --explores MODEL_NAME/EXPLORE_NAME \
        --branch DEV_BRANCH_NAME
    

For example:
    
    
    $ spectacles sql --config-file config-dev.yaml \
        --project thelook_cicd \
        --explores thelook_cicd/users \
        --branch dev-my-user-ydnv
    
    Connected to Looker version 23.18.60 using Looker API 4.0
    
    =================== Testing 1/1 explores [concurrency = 10] ===================
    
    ✓ thelook_cicd.users passed
    
    Completed SQL validation in 1 minute and 7 seconds.
    

### LookML Validator

The LookML Validator ensures that LookML changes are valid and have no syntax errors. It is called as shown next:
    
    
    $ spectacles lookml --config-file config-dev.yaml \
        --project PROJECT_NAME \
        --branch DEV_BRANCH_NAME
    

For example:
    
    
    $ spectacles lookml --config-file config-dev.yaml \
        --project thelook_cicd \
        --branch dev-my-user-ydnv
    
    Connected to Looker version 23.18.60 using Looker API 4.0
    
    ============= Validating LookML in project thelook_cicd [warning] ==============
    
    ✗ thelook_cicd/business_pulse.dashboard.lookml failed
    ✗ thelook_cicd/thelook_cicd.model.lkml failed
    
    ================ thelook_cicd/business_pulse.dashboard.lookml:28 ===============
    
    [Error] Unknown field "users.state" in explore "users" for field_filter.
    
    LookML: https://gcpl2318.cloud.looker.com/projects/thelook_cicd/files/business_pulse.dashboard.lookml?line=28
    
    ================ thelook_cicd/business_pulse.dashboard.lookml:36 ===============
    
    [Warning] Unknown field "users.state" (for explore "orders" in model
    "thelook_cicd") referenced in dashboard element.
    
    LookML: https://gcpl2318.cloud.looker.com/projects/thelook_cicd/files/business_pulse.dashboard.lookml?line=36
    
    [Additional errors snipped]
    
    Completed validation in 6 seconds.
    

### Content Validator

The Content Validator tests that any saved content like Looks and user-defined dashboards (UDDs) still function after changes are made. In order to make the job run faster and provide manageable results, validation is only done for content that is based on Explores you specify. The Content Validator is called as follows:
    
    
    $ spectacles content --config-file config-dev.yaml \
        --project PROJECT_NAME \
        --explores MODEL_NAME/EXPLORE_NAME \
        --branch DEV_BRANCH_NAME
    

For example:
    
    
    $ spectacles content --config-file config-dev.yaml \
        --project thelook_cicd \
        --explores thelook_cicd/users \
        --branch dev-my-user-ydnv
    
    Connected to Looker version 23.18.60 using Looker API 4.0
    Building LookML project hierarchy for project 'thelook_cicd' @ dev-my-user-ydnv
    
    ==================== Validating content based on 5 explores ====================
    
    ✗ thelook_cicd.users failed
    
    ================= test dashboard for spectacles [TheLook_CICD] =================
    
    Tile 'test dashboard for spectacles' failed validation.
    
    Error in thelook_cicd/users: Unknown field "users.state".
    
    Dashboard: https://gcpl2318.cloud.looker.com/dashboards/223
    
    ========================= Business Pulse [TheLook_CICD] ========================
    
    Filter 'State / Region' failed validation.
    
    Error in thelook_cicd/users: Unknown field "users.state".
    
    Dashboard: https://gcpl2318.cloud.looker.com/dashboards/190
    
    Completed content validation in 27 seconds.
    

### Assert Validation

Assert Validation tests data assertions that you have [added to your LookML](/looker/docs/reference/param-model-test) to ensure that data is being read properly. For example, a data test in your LookML may look like this:
    
    
    test: historic_revenue_is_accurate {
      explore_source: orders {
        column: total_revenue { field: orders.total_revenue }
        filters: [orders.created_date: "2019"]
      }
      assert: revenue_is_expected_value {
        expression: ${orders.total_revenue} = 626000 ;;
      }
    }
    

Assert validation is called as shown next:
    
    
    $ spectacles assert --config-file config-dev.yaml \
        --project PROJECT_NAME \
        --explores MODEL_NAME/EXPLORE_NAME \
        --branch DEV_BRANCH_NAME
    

For example:
    
    
    $ spectacles assert --config-file config-dev.yaml \
        --project thelook_cicd \
        --explores thelook_cicd/users \
        --branch dev-my-user-ydnv
    
    Connected to Looker version 23.18.60 using Looker API 4.0
    Building LookML project hierarchy for project 'thelook_cicd' @ dev-my-user-ydnv
    
    ==================== Running data tests based on 1 explore =====================
    
    ✗ thelook_cicd.users failed
    
    ================ thelook_cicd/users/california_users_is_accurate ===============
    
    Unknown filter field "users.state" in lookml test "california_users_is_accurate"
    declaration.
    
    LookML: https://gcpl2318.cloud.looker.com/projects/thelook_cicd/files/thelook_cicd.model.lkml?line=55
    
    ================ thelook_cicd/users/california_users_is_accurate ===============
    
    Invalid filter: users.state
    
    LookML: https://gcpl2318.cloud.looker.com/projects/thelook_cicd/files/thelook_cicd.model.lkml?line=55
    
    ================ thelook_cicd/users/california_users_is_accurate ===============
    
    Assertion "count_is_expected_value" failed: expression evaluated to "No".
    
    LookML: https://gcpl2318.cloud.looker.com/projects/thelook_cicd/files/thelook_cicd.model.lkml?line=55
    
    Completed data test validation in 14 seconds.
    

## Link stability for Looks and dashboards

By default, Looks and dashboards are given ascending numeric IDs that are used in the URL for the Look or dashboard. However, there is no way to keep these in sync across systems. Therefore, a URL for a specific dashboard in development won't point to the same dashboard in QA or production.

For UDDs there is an option to use a slug instead of an ID as part of the URL. The slug is a semi-random set of characters rather than a number. The slug can be set as part of the import and so that a similar URL can point to the same UDD on development, QA, and production. Using slugs instead of IDs is a best practice, particularly when "clicking through" to a UDD from Look or another UDD.

The slug can be found by inspecting the output of `gzr dashboard cat`. The slug can be used in the dashboard URL in place of the numeric ID.

## Migrating user content with Gazer

Copying content such as Looks and dashboards between the development, QA, and production is often useful. You may want to produce content that showcases new LookML additions, or ensure that saved content still functions correctly after LookML changes. In these situations [Gazer](https://github.com/looker-open-source/gzr) can be used to copy content between instances.

### LookML dashboards

LookML dashboards are synced between instances during the regular LookML CI/CD workflow. However, if any UDDs are synced with LookML dashboards, they can be updated with Gazer by using the following command:
    
    
    gzr dashboard sync_lookml DASHBOARD_ID --host TARGET_SYSTEM_URL
    

### User-defined dashboards

User Defined Dashboards (UDDs) can be migrated with Gazer by referencing the dashboard's ID and the URL of the Looker instance where the UDD resides. Gazer saves the dashboard configuration to a JSON file which is then imported into the target Looker instance.

The command to extract the UDD configuration is as follows:
    
    
    gzr dashboard cat DASHBOARD_ID --host TARGET_SYSTEM_URL --dir .
    

This will generate a file named `Dashboard_DASHBOARD_ID_DASHBOARD_NAME.json` that contains the dashboard's configuration.

The UDD can be imported into the target system using the following command:
    
    
    gzr dashboard import Dashboard_DASHBOARD_ID_DASHBOARD_NAME.json FOLDER_ID \
        --host TARGET_SYSTEM_URL
    

### Looks

Look migration works very similarly to UDD migration. First, use Gazer to save the Look configuration to a JSON file:
    
    
    gzr look cat LOOK_ID --host SOURCE_SYSTEM_URL --dir .
    

Then, import the Look into the target instance:
    
    
    gzr look import Look_LOOK_ID_LOOK_NAME.json FOLDER_ID \
        --host TARGET_SYSTEM_URL