# BigQuery API: testIamPermissions






    
        Home
      
  




    
        BigQuery
      
  




    
        Documentation
      
  




    
        Reference
      
  







  
    
    Send feedback
  
  


      Method: tables.testIamPermissions
      
    



      
      Stay organized with collections
    

      
      Save and categorize content based on your preferences.
    









HTTP request
Path parameters
Request body

JSON representation


Response body
Authorization scopes
Try it!




Returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a NOT_FOUND error.Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning.



HTTP request
POST https://bigquery.googleapis.com/bigquery/v2/{resource=projects/*/datasets/*/tables/*}:testIamPermissionsThe URL uses gRPC Transcoding syntax.


Path parameters







Parameters




resource

string
REQUIRED: The resource for which the policy detail is being requested. See Resource names for the appropriate value for this field.






Request body
The request body contains data with the following structure:




JSON representation




{
  "permissions": [
    string
  ]
}












Fields




permissions[]

string
The set of permissions to check for the resource. Permissions with wildcards (such as * or storage.*) are not allowed. For more information see IAM Overview.







Response body
If successful, the response body contains an instance of TestIamPermissionsResponse.


Authorization scopes
Requires one of the following OAuth scopes:

https://www.googleapis.com/auth/bigquery
https://www.googleapis.com/auth/cloud-platform
https://www.googleapis.com/auth/bigquery.readonly
https://www.googleapis.com/auth/cloud-platform.read-only
For more information, see the Authentication Overview.














  
    
    Send feedback
  
  



