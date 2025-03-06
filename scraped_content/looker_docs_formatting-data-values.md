# https://cloud.google.com/looker/docs/formatting-data-values

Depth: 3

This page provides an overview of the LookML parameters that modify the appearance and behavior of the data values that are displayed in data tables and visualizations. For example, you can specify currency formatting so that a data value such as `1234` renders as `$1,234.00` in data tables and visualizations. You can also specify clickable behaviors for fields so that users can click the fields to trigger [actions](/looker/docs/reference/param-field-action) or follow [links](/looker/docs/reference/param-field-link).

## Modifying formatting for data values

This section describes LookML parameters that change how data values appear to users.

Parameter | Description | Example  
---|---|---  
[`value_format`](/looker/docs/reference/param-field-value-format) | Use `value_format` to format the output of a `type: number` field using Excel-style options.Note that `value_format` has no effect on fields that are not `type: number`. | 
    
    
    measure: total_order_amount {
      type: sum
      sql: ${order_amount} ;;
      value_format: "$#,##0.00"
     }
      
  
[`value_format_name`](/looker/docs/reference/param-field-value-format-name) | Use `value_format` to format the output of a `type: number` field using a built-in or custom [`named_value_format`](/looker/docs/reference/param-model-named-value-format).Note that `value_format` and `value_format_name` have no effect on fields that are not `type: number`.  | 
    
    
    measure: total_order_amount {
      type: sum
      sql: ${order_amount} ;;
      value_format_name: usd
    }
      
  
[`style`](/looker/docs/reference/param-dimension-filter-parameter-types#style) | Use the `style` parameter to change the formatting of fields of [`type: tier`](/looker/docs/reference/param-dimension-filter-parameter-types#tier).Note that `style` is the only LookML parameter that affects the formatting of `type: tier` fields.  | 
    
    
    dimension: age_tier {
      type: tier
      tiers: [0, 10, 20, 30, 40, 50, 60, 70, 80]
      style: classic
      sql: ${age} ;;
    }
        
  
[`html`](/looker/docs/reference/param-field-html) | Use the `html` parameter to apply HTML formatting to your field.For example, you can change the font, font size, font weight, or font color. The example in this table shows how to add emoji to a field based on its value.  | 
    
    
    dimension: status {
      sql: ${TABLE}.status ;;
      html: {% if value == 'Shipped' or value == 'Complete' %}
          <p>✅ {{value}}</p>
        {% elsif value == 'Processing' %}
          <p>⏳ {{value}}</p>
        {% else %}
          <p>❌ {{value}}</p>
        {% endif %}
       ;;
    }
      
  
[`sql`](/looker/docs/reference/param-field-sql) | Use the `sql` parameter to change your data values using SQL.Use any SQL transformations allowed by your database. The example in this table shows how to add emoji to a field based on its value.  | 
    
    
    dimension: status {
      sql: CASE WHEN (${TABLE}.status = 'Shipped' OR ${TABLE}.status = 'Complete') ;;
         THEN CONCAT('✅ ', ${TABLE}.status)
       WHEN ${TABLE}.status = 'Processing'
         THEN CONCAT('⏳ ', ${TABLE}.status)
       ELSE
         CONCAT('❌ ', ${TABLE}.status)
       END ;;
    }
      
  
## Modifying clickable actions for data values

This section describes LookML parameters that determine a field's behavior when clicking on data values in the data table or visualization.  Parameter | Description | Example  
---|---|---  
[`drill_fields`](/looker/docs/reference/param-field-drill-fields) | Use `drill_fields` to specify which fields are displayed when the user drills into the data. Note that dimensions and measures have [different drilling behavior](/looker/docs/lookml-terms-and-concepts#drill_down).For advanced options for building out a custom drill path, see [More powerful data drilling](/looker/docs/best-practices/how-to-use-more-powerful-data-drilling).  | 
    
    
    dimension: country {
      sql: ${TABLE}.country ;;
      drill_fields: [state, city]
    }
      
  
[`action`](/looker/docs/reference/param-field-action) | Use `action` to create a data action on a field, which lets users perform tasks in other tools directly from Looker.When a field has one or more actions defined, then ellipses (`...`) will appear next to the field in data tables. Clicking on the field or the ellipses will bring up a menu from which users can select an action or drill into the data.  | 
    
    
    dimension: action_example {
      action: {
        label: "Send a Thing"
        url:
          "https://example.com/ping/{{value}}"
        form_url:
          "https://example.com/ping/{{value}}/form.json"
      }
    }
      
  
[`link`](/looker/docs/reference/param-field-link) | Use `link` to create a link on a field.When a field has one or more links defined, then ellipses (`...`) will appear next to the field in data tables. Clicking on the field or the ellipses will bring up a menu from which users can select a link or drill into the data.  | 
    
    
    dimension: artist_name {
      link: {
        label: "Google"
        url: "http://www.google.com/search?q={{value}}"
        icon_url: "http://google.com/favicon.ico"
       }
    }
      
  
[`html`](/looker/docs/reference/param-field-html) | Use `html` to write custom HTML formatting for a field. With HTML tags such as the `<a>` tag, you can specify one or more hyperlinks in your field.If a field has one or more actions or links defined, then ellipses (`...`) will appear next to the field in data tables, regardless of the `html` definition. Clicking on the field or the ellipses will bring up a menu from which users can select any available links or actions.  | 
    
    
    dimension: artist_name {
      html: <p>{{value}}
        <a href="#drillmenu">Drill menu</a>,
        <a href="http://www.google.com/search?q={{value}}">
          Google search
        </a></p>;;
        sql: ${TABLE}.artist_name ;;
        type: string
    }