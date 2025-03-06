# https://cloud.google.com/looker/docs/accessing-project-files

Depth: 3

The Looker IDE displays project files in the [file browser side panel of the Looker IDE](/looker/docs/ide-folders#file_browser). LookML developers can customize the file organization to match your project, as described on the [Working with the IDE file browser](/looker/docs/ide-folders) documentation page.

You can access [project files](/looker/docs/lookml-project-files) in the following ways:

  * From the **Develop** panel
  * By searching for and jumping to existing files
  * From an Explore
  * From the object browser panel

## Accessing project files from the Develop panel

You can access project files from the **Develop** section of the navigation panel. The projects you see in the **Develop** panel depend on the following settings:

  * Your permissions: To see a project, you must have the [`develop`](/looker/docs/admin-panel-users-roles#develop) permission for at least one model in the project.
  * Your current mode: You may see additional entries in the **Develop** panel when you are in [Development Mode versus Production Mode](/looker/docs/dev-mode-prod-mode). For example, if you created a new project in Development Mode that you have not yet pushed to production, then that project would be visible in the menu only when you are in Development Mode.

To access project files from the **Develop** panel:

![](/static/looker/docs/images/dev-open-project-2120.png)

  1. Select **Develop** in the navigation panel to open the **Develop** panel.
  2. In the **Develop** panel, select the name of the project that you want to access. ![](/static/looker/docs/images/dev-open-project-a-2120.png)
  3. When you open a LookML project from the **Develop** panel, the Looker IDE opens the project to one of the LookML files in that project: 
     * If the project contains a [document file](/looker/docs/other-project-files#document_files) named `readme.md`, the IDE will open that file.
     * If there's no `readme.md` document file, the IDE will open the first alphabetical document file.
     * If there are no document files in the project, the IDE will open the first alphabetical [model file](/looker/docs/lookml-project-files#model_files).
     * If there are no model files in the project, the IDE will open the first alphabetical file of any type.
  4. To open a different project file, select the filename in the side panel of the Looker IDE. See the [Working with the IDE file browser](/looker/docs/ide-folders) documentation page for more information about the organization of the Looker IDE.

## Searching for and jumping to LookML objects or project files

In the Looker IDE, you can do a quick search to navigate directly to LookML objects and project files. Use the [keyboard shortcut](/looker/docs/keyboard-shortcuts) Command-J (Mac) or Ctrl+J (Windows), or select the **Jump to object or file** icon search from the [file browser](/looker/docs/ide-folders) or the [object browser](/looker/docs/object-browser).

A text field opens where you can enter a search term, which can be a word or any part of a word. As you type, the search results show all matching objects and files.

The results show all files and objects whose names include your search term:

  * For LookML objects, the search results show the project file where the object is defined.
  * For project files, the search results show the [IDE folder](/looker/docs/ide-folders) where the file is located.

Select a file from the search results to open the file, or select an object to navigate to the object's definition.

## Accessing LookML from an Explore

You can also directly access the LookML for an Explore or for a field from an Explore.

![](/static/looker/docs/images/explore-go-lookml-718.png)

  1. To access the LookML for an Explore, select the Looker icon near the Explore name.
  2. To access the LookML for a field in the field picker, open the field's gear menu on the [**All Fields**](/looker/docs/creating-and-editing-explores#explore_summary) or [**In Use**](/looker/docs/creating-and-editing-explores#in_use_tab) and select **Go to LookML**.
  3. To access the LookML for a field in the results table, open the field's gear menu in the table header and select **Go to LookML**.

After you select a field, you are taken directly to the field definition in the corresponding LookML file.

## Accessing LookML from the object browser panel

You can use the object browser panel to [view all the objects in your project](/looker/docs/object-browser#viewing_the_objects_in_a_project) or to [navigate to the LookML](/looker/docs/object-browser#navigating_to_the_lookml_for_an_object) for a specific object. To use the object browser panel:

  1. Select the object browser icon in the Looker IDE.
  2. Navigate to the LookML for an object by selecting the name of the object in the object browser panel.

When you select an object, the IDE displays the file in which the object is defined and positions your cursor on the first line of the object's declaration.

![](/static/looker/docs/images/dev-object-browser-select-718.png)

For more information, see the [Navigating projects with the object browser panel](/looker/docs/object-browser) documentation page.