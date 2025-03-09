# BigQuery API: patch






    
        Home
      
  




    
        BigQuery
      
  




    
        Documentation
      
  




    
        Reference
      
  







  
    
    Send feedback
  
  


      Method: tables.patch
      
    



      
      Stay organized with collections
    

      
      Save and categorize content based on your preferences.
    









HTTP request
Path parameters
Request body
Response body
Authorization scopes
Try it!




Updates information in an existing table. The update method replaces the entire table resource, whereas the patch method only replaces fields that are provided in the submitted table resource. This method supports RFC5789 patch semantics.



HTTP request
PATCH https://bigquery.googleapis.com/bigquery/v2/projects/{projectId}/datasets/{datasetId}/tables/{tableId}The URL uses gRPC Transcoding syntax.


Path parameters







Parameters




projectId

string
Required. Project ID of the table to update



datasetId

string
Required. Dataset ID of the table to update



tableId

string
Required. Table ID of the table to update






Request body
The request body contains an instance of Table.


Response body
If successful, the response body contains an instance of Table.


Authorization scopes
Requires one of the following OAuth scopes:

https://www.googleapis.com/auth/bigquery
https://www.googleapis.com/auth/cloud-platform
For more information, see the Authentication Overview.














  
    
    Send feedback
  
  



