# https://cloud.google.com/looker/docs/custom-looker-visualization-gemini

Depth: 3

****

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](/products#product-launch-stages). 

**Note:** As an early-stage technology, Gemini can generate output that seems plausible but is factually incorrect. We recommend that you validate all output from Gemini before you use it. For more information, see [Gemini in Google Cloud and responsible AI](/gemini/docs/discover/responsible-ai).

Gemini is an AI-powered collaborator in Google Cloud. You can use Gemini to customize formatting options on Looker [visualizations that use the HighCharts API](/looker/docs/chart-config-editor). The **Visualization Assistant** generates JSON formatting options from text-based prompts to accelerate the customization of Looker visualizations.

**Note:** **Visualization Assistant** is available only for HighCharts-based visualizations.

## Before you begin

To create visualizations with Gemini assistance, note the following requirements:

  * Gemini in Looker must be enabled by a Looker admin to use **Visualization Assistant**.
  * For a [Looker (Google Cloud core)](/looker/docs/looker-core-overview) instance, follow these [Gemini in Looker enablement instructions](/looker/docs/looker-core-admin-gemini#enable-and-disable-gil-core).

    * A Looker Original instance can follow these [Gemini in Looker enablement instructions](/looker/docs/admin-panel-platform-gil#enable-and-disable-gil-original)
  * A Looker role that contains the [can_override_vis_config permission](/looker/docs/admin-panel-users-roles#can_override_vis_config) permission.

## Using the Visualization Assistant

The **Visualization Assistant** is available for visualizations that use the HighCharts API, which includes most [Cartesian charts](/looker/docs/visualization-types#cartesian_charts), such as the [column chart](/looker/docs/column-options), [bar chart](/looker/docs/bar-options), and [line chart](/looker/docs/line-options), among others. To customize a visualization with the **Visualization Assistant** , follow these steps:

  1. View a supported visualization in an Explore, or edit a visualization in a Look or dashboard.
  2. Open the **Edit** menu in the visualization.
  3. Click pen_spark **Visualization Assistant** to open the prompt menu.

![](/static/looker/docs/images/advanced-vis-assistant-2410.png)

Within the pen_spark **Visualization Assistant** prompt menu you are able to:

  * Type out a plain text prompt of changes for the visualization in the **Ask anything** field. To send send_spark your prompt press return (Mac) or Enter (PC).
  * Apply generated **Suggestions** to the visualization.
  * Open the **Edit Chart Config** to manually write and edit JSON formatting options.
  * **Clear Chart Overrides** to clear all custom changes applied to the visualization. You will be prompted to **Confirm** removing all changes before proceeding. If you cleared the changes by accident it is possible to retrieve them by navigating back in your browser history.

Once the prompt has run a preview window will open with the options to:

![](/static/looker/docs/images/apply-advanced-vis-config.png)

  * Open the **Edit Chart Config** to manually write and edit the generated JSON formatting options. Click **Visualization Assistant** to return to the prompt menu
  * **Start Over** from the pen_spark **Visualization Assistant** menu. All unapplied changes will be lost.
  * **Apply** the previewed changes to the visualization. If changes are made in the **Chart Config** menu this option will change to **Revalidate and Apply**
  * Vote to indicate whether the prompt response was helpful thumb_up or the response was not what was expected thumb_down.

An `Invalid JSON detected` error message will appear if you try to preview code containing invalid JSON. You can clean up invalid JSON using the **Autofix code** edit_fix_auto option at the bottom of the **Chart Config** pane.

**Caution:** Use caution when editing the default visualization options after making changes with the **Visualization Assistant**. Editing the default visualization options may cause unexpected behavior, including blank visualizations.

## Creating successful prompts

Writing successful prompts can take practice. Try some of the following suggestions to write prompts that successfully accomplish your goal.

### Break prompts into multiple parts

Prompts are more successful when they focus on one change at a time. For example, if you want to change both the font family and the type of visualization, it's better to make these separate prompts. Once you approve of the generated changes apply them and then begin writing the next prompt.

**Prompt** : Change the last series into a line

![The Visualization Assistant menu shows a preview of a prompt that changes one of the three series in a visualization from a column to a line.](/static/looker/docs/images/vis-assistant-line.png)

**Prompt** : Change the font to Arial and make it bold

![The Visualization Assistant menu shows a preview of a prompt that changes the font of the graph to the Arial font family, and makes text bold.](/static/looker/docs/images/vis-assistant-arial-font.png)

### Try writing a prompt multiple ways

If, while writing a prompt, you're not seeing the results that you expect, try rewording the prompt. When you apply conditional formatting, try making your prompt as unambiguous as possible. Setting specific value ranges and providing hex codes can create a more successful output. See the following examples:

**Good prompt** : Make the first series #F4B400 if it is over 350000

**Poor prompt** : Highlight the top values in yellow

![The Visualization Assistant menu shows a preview of a prompt that changes the color of the first series of values over 350,000.](/static/looker/docs/images/vis-assistant-hex.png)

If you have multiple series in a visualization, try referring to the series by name rather than by its position in the chart.

**Prompt** : Make the middle series a column

**Better prompt** : Make the users series a column

![The Visualization Assistant menu shows a preview of a prompt that changes the second of three series, called users, to a column chart](/static/looker/docs/images/vis-assistant-series-name.png)

### Use prompts as a starting point

Particularly complex customizations may require making edits directly to the JSON. Try using the **Visualization Assistant** prompts to create templates and patterns for complex customizations, and then use the **Edit Chart Config** to manually write and edit JSON formatting options. Visit the [Customizing visualizations using the Chart Config Editor](/looker/docs/chart-config-editor) documentation for more on using HighCharts JSON.

### Sample prompts

Try the following sample prompts to get ideas on how the **Visualization Assistant** can help you get started customizing your visualizations:

  * "Make this chart a column chart"
  * "Add data labels to the chart"
  * "Set the chart margin as 100px"
  * "Set the line color as Red"
  * "Set the chart background color as pink"
  * "Set the line series marker shape as triangle"

## Provide feedback

You can provide feedback for the visualization preview in the **Visualization Assistant** prompt menu. If the generated preview looks correct, click the ![Thumbs up icon indicating approval.](/static/looker/docs/studio/images/standard--chrome--thumbs-up.png) thumbs-up icon. If the generated preview looks incorrect or isn't what you expected, click the ![Thumbs down icon indicating disapproval.](/static/looker/docs/studio/images/standard--chrome--thumbs-down.png) thumbs-down icon.

You can also email your feedback.

**Note:** Gemini in Looker is in preview with limited support. We encourage you to share your feedback to help us improve. To report bugs or issues, send an email to [`gemini_looker_viz_assistant@google.com`](mailto:gemini_looker_viz_assistant@google.com) with the following details: 

  * A clear description of the problem and the expected behavior
  * Steps to reproduce the issue
  * Any additional relevant details

## Related resources

  * [Gemini for Google Cloud overview](/gemini/docs/overview)
  * [Gemini in Looker](/gemini/docs/looker/overview)