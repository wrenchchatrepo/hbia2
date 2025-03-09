# BigQuery API: v2.rowAccessPolicies






    
        Home
      
  




    
        BigQuery
      
  




    
        Documentation
      
  




    
        Reference
      
  







  
    
    Send feedback
  
  


      REST Resource: rowAccessPolicies
      
    



      
      Stay organized with collections
    

      
      Save and categorize content based on your preferences.
    









Resource: RowAccessPolicy

JSON representation


RowAccessPolicyReference

JSON representation


Methods


Resource: RowAccessPolicy

Represents access on a subset of rows on the specified table, defined by its filter predicate. Access to the subset of rows is controlled by its IAM policy.





JSON representation




{
  "etag": string,
  "rowAccessPolicyReference": {
    object (RowAccessPolicyReference)
  },
  "filterPredicate": string,
  "creationTime": string,
  "lastModifiedTime": string
}












Fields




etag

string
Output only. A hash of this resource.



rowAccessPolicyReference

object (RowAccessPolicyReference)
Required. Reference describing the ID of this row access policy.



filterPredicate

string
Required. A SQL boolean expression that represents the rows defined by this row access policy, similar to the boolean expression in a WHERE clause of a SELECT query on a table. References to other tables, routines, and temporary functions are not supported.Examples: region="EU"  date_field = CAST('2019-9-27' as DATE)  nullable_field is not NULL  numeric_field BETWEEN 1.0 AND 5.0



creationTime

string (Timestamp format)
Output only. The time when this row access policy was created, in milliseconds since the epoch.



lastModifiedTime

string (Timestamp format)
Output only. The time when this row access policy was last modified, in milliseconds since the epoch.







RowAccessPolicyReference

Id path of a row access policy.





JSON representation




{
  "projectId": string,
  "datasetId": string,
  "tableId": string,
  "policyId": string
}












Fields




projectId

string
Required. The ID of the project containing this row access policy.



datasetId

string
Required. The ID of the dataset containing this row access policy.



tableId

string
Required. The ID of the table containing this row access policy.



policyId

string
Required. The ID of the row access policy. The ID must contain only letters (a-z, A-Z), numbers (0-9), or underscores (_). The maximum length is 256 characters.














Methods





getIamPolicy

                Gets the access control policy for a resource.



list

                Lists all row access policies on the specified table.



testIamPermissions

                Returns permissions that a caller has on the specified resource.











  
    
    Send feedback
  
  



