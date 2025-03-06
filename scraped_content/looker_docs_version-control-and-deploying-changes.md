# https://cloud.google.com/looker/docs/version-control-and-deploying-changes

Depth: 3

> This page assumes that your project has already been set up for version control. If you see a **Configure Git** button instead of the choices described on this page, you need to first [set up Git for your project](/looker/docs/setting-up-git-connection#integrating_looker_with_git).

Looker uses Git to record changes and manage file versions. Each LookML project corresponds to a Git repository, and each developer branch correlates to a Git branch.

Looker can be configured to work with many Git providers, such as GitHub, GitLab, and Bitbucket. See the [Setting up and testing a Git connection](/looker/docs/setting-up-git-connection#integrating_looker_with_git) documentation page for information on setting up Git for your Looker project.

## Working with Git branches

One of the main benefits of Git is that a Looker developer can work in a _branch_ , an isolated version of a file repository. You can develop and test without affecting other users. As a developer in Looker, you are using a Git branch whenever you are in [Development Mode](/looker/docs/dev-mode-prod-mode).

Another major feature of Git is the ease of collaborating with other developers that it provides. You can create a branch and (if desired) make changes, and then other developers can switch to that branch to review or make changes to the branch. If another developer has committed changes to the branch, Looker displays the **Pull Remote Changes** button. You should pull those committed changes to the branch before making additional changes.

You can also [delete a branch](/looker/docs/version-control-and-deploying-changes#deleting_git_branches) other than the master branch, your current branch, or a developer's personal branch.

### Personal branches

The first time you go into [Development Mode](/looker/docs/dev-mode-prod-mode), Looker automatically creates your personal Git branch. Your personal branch starts with `dev-` and includes your name.

![](/static/looker/docs/images/dev-git-default-personal-branch-2206.png)

Your personal branch is specific to you, and it _cannot_ be deleted. Your personal branch is read-only to all other developers. If you are collaborating with other developers on a project, you may want to create a new branch so that others can switch to that branch and contribute changes as well.

**Note:** You can't make changes to another developer's personal branch. To build on work in somebody else's personal branch, create a new branch starting from their branch.

### Creating a new Git branch

If you are working on a simple fix and not collaborating with other developers, your personal branch is usually a good place to work. You can use your personal branch to make quick updates, and then commit the changes and push them to production.

However, you may also want to create new Git branches in addition to your personal branch. A new Git branch makes sense in these situations:

  * **You are working with other developers**. Since your personal branch is read-only to other developers, if you want to collaborate with others, you should create a new Git branch so that other developers can write to the branch. When you're collaborating with others, be sure to pull changes each time you resume work. That way, you'll have the latest updates from all developers before continuing work.
  * **You are working on multiple sets of features at once**. Sometimes you may be in the middle of a major project, but want to resolve a minor issue or make a quick fix. In this case, you can commit your changes to the branch you're on and then create or switch to another branch to work on a separate set of features. You can make your fix in the new branch, and then deploy that branch's changes to production — before resuming work in your original branch.

Before creating a new branch:

  * If you have a merge conflict on your current branch, you must resolve the conflict before you can create a new branch.
  * If you have any uncommitted changes on the current branch, you must [commit the changes](/looker/docs/git-command-reference#commit) on your current branch before creating a new branch.
  * If you want to create a branch starting from an existing development branch (and not the production branch), first get the latest version of the development branch by switching to that development branch, and then [pull remote changes](/looker/docs/git-command-reference#pull_dev) to sync your local version of that branch.

To create a new Git branch:

![](/static/looker/docs/images/dev-open-project-b-2402.png)

  1. Verify that you have [Development Mode turned on](/looker/docs/dev-mode-prod-mode#switching_in_and_out_of_development_mode).
  2. [Navigate to your project files](/looker/docs/accessing-project-files) in the **Develop** menu.

![](/static/looker/docs/images/dev-git-new-branch-2120.png)

  3. Select the **Git** icon in the left-hand icon menu to open the **Git Actions** panel.

  4. Select the **View Branches** drop-down menu.

  5. Select **New Branch**.

![](/static/looker/docs/images/dev-git-new-branch-dialog-2120.png)

  6. In the **New Branch** window, enter a name for your branch. Note that there are limitations for Git branch names; for naming requirements, see Rules for naming a Git branch on this page.

  7. Select the **Create From** drop-down menu and select an existing branch to use as the starting point for your new branch.

  8. Select **Create** to create your branch.

Alternatively, you can create Git branches from the **Branch Management** tab of the project's settings.

#### Rules for naming a Git branch

Looker uses the branch-naming-convention requirements specified by Git.

Git branch names must _not_ :

  * Contain a space character
  * Contain a double period: `..`
  * Contain a backslash: `\`
  * Contain the sequence: `@{`
  * Contain a question mark: `?`
  * Contain an opening square bracket: `[`
  * Contain an ASCII control character: `~` or `\^` or `:`
  * Begin with a period: `.`
  * Begin with the prefix: `dev-` (reserved for the personal branches of Looker developers)
  * End with a forward slash: `/`
  * End with the extension: `.lock`

In addition, the branch name can only contain an asterisk (`*`) if the asterisk represents an entire path component (for example, `foo/*` or `bar/*/baz`), in which case it is interpreted as a wildcard and not as part of the actual branch name.

### Switching to another Git branch

> If you have a merge conflict on your current branch, you must resolve the conflict before you can switch to a different branch. 
> 
> Also, if you have uncommitted changes on your current branch, you cannot switch to an existing branch until you [commit the changes](/looker/docs/git-command-reference#commit) on your current branch.

To switch to a different Git branch, follow these steps:

![](/static/looker/docs/images/dev-git-switch-branch-2120.png)

  1. In the project, navigate to the **Git Actions** panel by selecting the **Git** icon in the left-hand icon menu.
  2. In the **Git Actions** panel, select the Git branch drop-down menu to the right of your current Git branch name.
  3. Select the branch you want to switch to by selecting it in the menu, or by typing the branch name into the search box. Branch name search is case-insensitive. For example, you can search for "DEV" and see all branches with names that include "dev", "DEV", "Dev", and so on.

### Managing Git branches

The **Branch Management** tab of the [project settings](/looker/docs/git-options#project_settings) shows a table of all the Git branches for the Looker project. To open the **Branch Management** tab, first navigate to the project settings by selecting the **Settings** icon from the left-hand icon menu. Next, select the **Branch Management** tab.

![](/static/looker/docs/images/develop-branch-mgmt-2206.png)

On the **Branch Management** tab, you can:

  1. Create a new branch by selecting the **New Branch** button. See the Creating a new Git branch section on this page for more information.
  2. Search for branch names in the **Search Bar**.
  3. Refresh the table by selecting the **Refresh** button.
  4. Sort the table by selecting a column name.

The table includes the following information:

  * **Name** : Name of the Git branch. Looker developers' personal branches start with `dev-` and include the first and last name of the developer.
  * **Status** : The difference between your local version of the branch and the remote version of the branch. For example, a status of `3 commits behind` means that your local version of the branch is behind the remote version of the branch by three commits. Because Looker always uses the remote version of master, the **Branch Management** tab doesn't show the status of the local version of the master branch. The master branch can always be considered to be up to date.
  * **Last Updated** : Amount of time since a Looker developer made a commit to the branch.
  * **Actions** : A button to delete the branch, or the reason that the branch is not eligible for deletion.

### Deleting Git branches

From the **Branch Management** tab, you can delete branches that have a **Delete** button in the table. You cannot delete the following branches:

  * The master branch
  * Your current branch
  * A Looker developer's personal branch

In the table, these branches don't have a **Delete** button. Instead, the **Action** column of the table shows the reason that the branch can't be deleted.

> You cannot restore a branch once it's been deleted. When you delete a branch, Looker removes both your local version of the branch and the remote version of the branch. 
> 
> However, if the branch was created by another Looker developer, or if other developers have checked out the branch, those developers will still have their local version of the branch. If a Looker developer makes commits to their local version of the branch and pushes it to production, you will once again see a remote version of the branch. This can be handy if you _do_ want to restore the branch. Otherwise, when you delete a branch, all other Looker developers should delete the same branch to ensure that it can't be accidentally resurfaced by someone pushing it to remote.

To delete one or more Git branches from your project, first navigate to the project settings by selecting the **Settings** icon from the left-hand icon menu. Then select the **Branch Management** tab. In the **Branch Management** tab, you can delete branches in two ways:

![](/static/looker/docs/images/develop-branch-delete-2206.png)

  1. Delete multiple branches by first selecting the branch checkboxes and then selecting **Delete Selected Branches**.
  2. Delete a single branch by selecting **Delete** next to the branch name.

## Executing Git commands in Looker

Looker has a built-in interface that integrates with your Git service. Looker displays the **Git button** in the upper right corner of the LookML IDE.

![](/static/looker/docs/images/dev-git-button-718.png)

The Git button shows different options depending on where you are in the process of making changes and deploying to production. In general, the option shown on the button is the best guide for your next action.

If your developer branch is in sync with the production branch, the Git button displays the **Up to Date** message and is not selectable.

![](/static/looker/docs/images/dev-git-button-uptodate-718.png)

Once your project is [configured for Git](/looker/docs/setting-up-git-connection#integrating_looker_with_git), you can select the **Git Actions** button to open the **Git Actions** panel.

![](/static/looker/docs/images/git-actions-menu-git-actions-718.png)

The commands available on the **Git Actions** panel depend on where you are in the process of making changes and deploying to production.

## Getting your changes to production

With the default Looker Git integration, Looker prompts developers through the following Git workflow:

  * Committing changes to the developer's current development branch (and running data tests if your project is set up to [require tests before deploying](/looker/docs/git-options#require-data-tests))
  * Merging the development branch into the production branch, which by default is called `master`
  * Deploying the production branch to the Looker production environment that will be presented to your Looker end users

This means that, with the default Git integration, all developers merge their changes into a branch called `master`, and the latest commit on the `master` branch is what is used for the production environment of Looker.

For advanced Git implementations, you can customize this workflow:

  * You can have your developers submit pull requests for your Git production branch, instead of allowing developers to merge their changes through the Looker IDE. See the [Configuring project version control settings](/looker/docs/git-options#integrating_pull_requests_for_your_project) documentation page for details.
  * You can use the **Git Production Branch Name** field to specify which branch from your Git repository Looker should use as the target branch into which your Looker developers' branches are merged. See the [Configuring project version control settings](/looker/docs/git-options#git_production_branch_name) documentation page for details.
  * You can use [advanced deploy mode](/looker/docs/advanced-deploy-mode) for specifying a different commit SHA or tag name to deploy to your Looker production environment, instead of using the latest commit on the production branch. (If you want to deploy a commit from a different branch, you can use the advanced deploy mode [webhook](/looker/docs/advanced-deploy-mode#deploying_with_webhooks) or [API endpoint](/looker/docs/advanced-deploy-mode#deploying_with_the_api).) See the [Advanced deploy mode](/looker/docs/advanced-deploy-mode) documentation page for details.

> If you see a **Configure Git** button instead of the choices described in this section, you need to first [set up Git for your project](/looker/docs/setting-up-git-connection#integrating_looker_with_git).

### Viewing uncommitted changes

The LookML IDE has several indicators that are displayed when you are in Development Mode and have uncommitted changes, as described in the [Marking additions, changes, and deletions](/looker/docs/looker-ide#marking_additions,_changes,_and_deletions) section of the [Looker IDE overview](/looker/docs/looker-ide) documentation page.

You can get a difference summary for all files by selecting the **View Uncommitted Changes** option from the **Git Actions** panel.

![](/static/looker/docs/images/dev-git-view-uncommitted-718.png)

In the **Uncommitted Changes to Project** window, Looker displays a summary of all the uncommitted, saved changes in all the project's files. For each change, Looker shows the following:

  * The name of the replaced file and the name of the added file. 
    * The name of the replaced file (indicated with `---`) and the name of the added file (indicated with `+++`). In many cases, this may show different versions of the same file, with revisions identified by `--- a/` and `+++ b/`.
    * Deleted files are shown as replacing a null file (`+++ /dev/null`).
    * Added files are shown as replacing a null file (`--- /dev/null`).
  * The line number where the change begins.

For example, `-101,4 +101,4` indicates that, at the 101st line in the file, 4 lines were removed and 4 lines were added. A deleted file with 20 lines would show `-1,20 +0,0` to indicate that, at the first line in the file, 20 lines were removed and replaced by zero lines.
  * The text that was updated: 
    * Deleted lines are displayed in red.
    * Added lines are displayed in green.

To display a difference summary for a single file, select the **View Changes** option from the file's menu.

![](/static/looker/docs/images/dev-git-view-uncommitted-file-718.png)

### Committing changes

After you have made and saved any changes to your LookML project, the IDE may require you to validate your LookML. The Git button displays the text **Validate LookML** in this scenario.

![](/static/looker/docs/images/dev-git-validate-718.png)

Whether this is required depends on your project's setting for [code quality](/looker/docs/git-command-reference#code_quality). For more information on the Content Validator, see the [Validating your LookML](/looker/docs/lookml-validation#validating_your_changes) documentation page.

If another developer has made changes to the production branch since you last updated your local branch, Looker requires you to pull those updates from the production branch. The Git button displays the text **Pull from Production** in this scenario.

![](/static/looker/docs/images/dev-git-pull-718.png)

> If your project is enabled for [advanced deploy mode](/looker/docs/advanced-deploy-mode), the Git button instead displays the text **Pull from Primary Branch**.

Once you save your changes (and fix any LookML warnings or errors, [if required](/looker/docs/git-command-reference#code_quality)) and pull from production (if required), the Git button displays the text **Commit Changes & Push**.

![](/static/looker/docs/images/dev-git-commit-changes-718.png)

If desired, you can first review your uncommitted changes before committing.

When you are ready to commit the changes, use the Git button to commit these changes to your current branch. Looker displays the **Commit** dialog box, which lists the files that have been added, changed, or deleted.

![](/static/looker/docs/images/dev-git-commit-dialog-718.png)

Enter a message that briefly describes your changes, and clear the checkboxes next to any files that you don't want to include in the sync. Then select **Commit** to commit the changes.

### Checking for unbuilt PDTs

If you have made changes to any PDTs in your project, it is optimal that all of your PDTs be built when you deploy to production so that the tables can be used immediately as the production versions. To check the status of PDTs in the project, select the **Project Health** icon to open the **Project Health** panel, and then select the **Validate PDT Status** button.

![](/static/looker/docs/images/dev-check-unbuilt-pdts-2300.png)

See the [Derived tables in Looker](/looker/docs/derived-tables#checking_for_unbuilt_pdts_in_development_mode) documentation page for more information about checking for unbuilt PDTs in your LookML project and about working with derived tables in Development Mode.

### Running data tests

Your project may include one or more [`test`](/looker/docs/reference/param-model-test) parameters that define data tests to verify the logic of your LookML model. See the [`test`](/looker/docs/reference/param-model-test) parameter documentation page for information on setting up data tests in your project.

**Note:** By default, new LookML projects [require data tests to pass](/looker/docs/git-options#require-data-tests). If your project has one or more `test` parameters, the data tests must pass before you can deploy the project to production.

If your project contains data tests and you are in [Development Mode](/looker/docs/dev-mode-prod-mode), you can initiate your project's data tests in several ways:

![](/static/looker/docs/images/dev-git-data-tests-run-2112.png)

  1. If your project settings are configured to [require data tests to pass before deploying your files to production](/looker/docs/git-options#require-data-tests), the IDE will present the **Run Tests** button after you commit changes to the project to run all the tests for your project, no matter which file defines the test. You must pass the data tests before you can deploy your changes to production.
  2. Select the **Run Data Tests** button in the **Project Health** panel. Looker will run all data tests in your project, no matter which file defines the test.
  3. Select the **Run LookML Tests** option from the file's menu. Looker will run only the tests defined in the current file.

Once you run the data tests, the **Project Health** panel will display the progress and results.

![](/static/looker/docs/images/dev-git-data-tests-results-2112.png)

  * A data test passes when the test's assertion is true for every row in the test's query. See the [`test`](/looker/docs/reference/param-model-test) parameter documentation page for details on setting up test assertions and queries.
  * If a data test fails, the **Project Health** panel will provide information about why the test failed, whether the test found errors in your model's logic or if it was the test itself that was invalid.
  * From the data test results, you can select the name of a data test to go directly to the LookML for the data test, or you can select the **Explore Query** button to open an Explore with the query defined in the data test.

### Deploying to production

Once you have committed changes to your branch, the Looker IDE will prompt you to merge your changes to the primary branch. The type of prompt you'll see in the IDE will depend on your project's configuration:

  * If your project is configured for [advanced deploy mode](/looker/docs/advanced-deploy-mode), the IDE will prompt you to merge your changes into the primary branch. Once you merge your commit, a Looker developer with the [`deploy` permission](/looker/docs/admin-panel-users-roles#deploy) can deploy your commit to production by using the Looker IDE [deployment manager](/looker/docs/advanced-deploy-mode#deployment_manager), or by using a [webhook](/looker/docs/advanced-deploy-mode#deploying_with_webhooks) or an [API endpoint](/looker/docs/advanced-deploy-mode#deploying_with_the_api).
  * If your project is configured for Git integration using [pull requests](/looker/docs/git-options#integrating_pull_requests_for_your_project), you will be prompted to open a pull request using your Git provider's interface.
  * Otherwise, with the default Looker Git integration, if you have [`deploy` permission](/looker/docs/admin-panel-users-roles#deploy), the Looker IDE will prompt you to merge your changes to the production branch and deploy your changes to the production version of your Looker instance.

## Advanced deploy mode

With the default Looker Git integration, Looker developers commit their changes to their development branch, then merge their development branch into the production branch. Then, when you deploy to the Looker environment, Looker uses the latest commit on the production branch. (See the Getting your changes to production section on this page for the default Git workflow and other options for advanced Git implementations.)

For cases where you don't want the to always use the latest commit on the production branch for your Looker environment, a developer with [`deploy` permission](/looker/docs/admin-panel-users-roles#deploy) can use advanced deploy mode to specify the exact commit to be used for your Looker environment. This is useful in multi-environment developer workflows, where each environment points to a different version of a codebase. It also gives one or several developers or administrators greater control over the changes that are deployed to production.

When advanced deploy mode is enabled, the Looker IDE does not prompt developers to deploy their changes to production. Instead, the IDE prompts developers to merge their changes into the production branch. From there, changes can be deployed only in the following ways:

  * Using the [deployment manager](/looker/docs/advanced-deploy-mode#deployment_manager) in the Looker IDE
  * Triggering a [webhook](/looker/docs/advanced-deploy-mode#deploying_with_webhooks)
  * Using an [API endpoint](/looker/docs/advanced-deploy-mode#deploying_with_the_api)

**Note:** For projects with advanced deploy mode enabled, if the project has never been deployed to production, the initial deployment to production must be made using the [deployment manager](/looker/docs/advanced-deploy-mode#deployment_manager) in the Looker IDE. You cannot use the API or the webhook for the initial deployment of a project that uses advanced deploy mode. After the initial deployment to production (even if it was initially deployed without advanced deployment mode), you can use the webhook or the API to deploy subsequent changes to production using advanced deploy mode.

See the [Advanced deploy mode](/looker/docs/advanced-deploy-mode) documentation page for details.

## Checking the impact of your changes

After making your changes available to the organization, you can use [content validation](/looker/docs/content-validation) to make sure you have not invalidated any dashboards or saved Looks. You'll have the opportunity to fix them if you have.

## Handling typical issues

While working on your model, you may need to:

  * Abandon your changes

Occasionally you may want to abandon your data-modeling changes. If they are not yet saved, you can simply refresh or navigate away from the page and then accept the warning prompt. If you have saved the changes, you can revert the uncommitted changes as described in the Reverting uncommitted changes section.

  * Handle merge conflicts with other developers' work

If you have more than one developer working on your data model, Git typically handles the situation. However, occasionally Git needs a human to resolve merge conflicts.

Some changes, such as changing the name of a field, can affect existing dashboards and Looks. As mentioned earlier, after making your changes available to the organization, you can use [content validation](/looker/docs/content-validation) to check your content and fix any issues.

### Reverting uncommitted changes

When working on your personal development branch, you can revert uncommitted changes that you have saved if you do not want to deploy them. You can revert all the uncommitted changes for all files in the project or just the changes in a single file.

To revert uncommitted changes for _all files_ :

![](/static/looker/docs/images/dev-git-revert-all-changes-718.png)

  1. Select the **Revert to...** option in the **Git Actions** panel.
  2. Select a revert option: 
     * To revert only _uncommitted_ changes, select **Revert uncommitted changes**. You can also select the **View changes** link to view the changes that would be reverted.
     * To revert all changes, including uncommitted and committed changes, select **Revert to Production**
  3. To complete the revert process, select **Confirm**.

To revert any additions or deletions in the contents of a single file, select the **Revert Changes** option from that file's menu:

![](/static/looker/docs/images/dev-git-revert-single-file-718.png)

> When you rename a file, you are essentially deleting the original file and creating a new file with a new name. Because this involves more than one file, you can't use the **Revert File** option to undo the renaming of a file. If you want to undo a file rename, use the **Revert to...** option from the **Git Actions** panel.
> 
> Also, if you have deleted a file, the file is no longer displayed in the IDE file browser. If you want to revert the deletion of a file, use the **Revert to...** option from the **Git Actions** panel.

### Resolving merge conflicts

Typically, Git can automatically merge your new changes with the production version of your LookML files. A merge conflict occurs when Git encounters conflicting changes and cannot identify which changes should be kept, usually when another developer has made changes since you last pulled and you have made changes in the same area. If you have a merge conflict in your code, Looker displays a **Merge conflicts** warning after you commit changes and pull from production.

![](/static/looker/docs/images/develop-merge-conflict-warning-718.png)

When Looker shows the merge-conflict warning, we recommend that you resolve the merge conflict before making any further changes. Pushing a merge conflict to production will cause parse errors that may prevent exploration of your data. If you are an advanced Git user and you want to move forward with pushing changes, select the **Don't Resolve** button.

In the LookML file itself, the lines with conflicts are marked like this:
    
    
    <<<<<<< HEAD
    Your code
    &#61;&#61;&#61;&#61;&#61;&#61;&#61;
    Production code
    >>>>>>> branch 'master'
    

Looker shows the following _merge markers_ to indicate the merge conflicts:

  * **< <<<<<< `HEAD`** marks the beginning of the conflicting lines.
  * **> >>>>>> `branch 'master'`** marks the end of the conflicting lines.
  * **=======** separates each version of the code so you can compare them.

In the preceding example, `your code` represents the changes you committed, and `production code` represents the code into which Git could not automatically merge your changes.

To resolve a merge conflict:

![](/static/looker/docs/images/develop-merge-conflict-718.png)

  1. Find the files with merge conflicts. Looker marks these files in red, or you can also [search your project](/looker/docs/looker-ide#find-and-replace) for merge markers, such as <<<< or `HEAD`, to find all the conflicts in your project. You can also find affected files by selecting the **files** link in the merge warning that appears in the **Git Actions** panel.
  2. In the file, go to the lines with merge conflicts and delete the version of the text that you do **NOT** want to keep, and also delete all the merge conflict markers.
  3. Save the file, and repeat the preceding steps for any other files marked with merge conflicts.

**Tip:** [Search your project](/looker/docs/looker-ide#find-and-replace) for each of the merge markers to verify that you have resolved all conflicts and deleted all the merge markers. Make sure to remove all instances of merge markers in your LookML files. These markers will cause parse errors that can prevent users from exploring your data.
  4. After you have resolved all merge conflicts and deleted all merge markers from your project, [commit the changes](/looker/docs/version-control-and-deploying-changes#committing_changes) and [deploy them to production](/looker/docs/version-control-and-deploying-changes#deploying_to_production).

Now that you have resolved the merge conflict and pushed your resolution to production, other developers can pull from production and continue work as usual.

## Git garbage collection

[Git garbage collection](https://git-scm.com/docs/git-gc) cleans up unnecessary files and compresses file revisions to optimize your Git repository. Git garbage collection (`git gc`) is run automatically when your Looker instance is updated or rebooted. To keep from running `git gc` too often, Looker waits 30 days since the last `git gc` and then runs `git gc` on the next reboot.

In rare cases, you might try to [**Push Changes to Remote**](/looker/docs/git-command-reference#push_changes_remote) or [**Push Branch to Remote**](/looker/docs/git-command-reference#push_branch) while `git gc` is running. If Looker displays an error, wait for a minute or two and then try again to push your changes.