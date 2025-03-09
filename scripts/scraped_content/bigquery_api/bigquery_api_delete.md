# BigQuery API: delete






    
        Home
      
  




    
        BigQuery
      
  




    
        Documentation
      
  




    
        Reference
      
  







  
    
    Send feedback
  
  


      Method: tables.delete
      
    



      
      Stay organized with collections
    

      
      Save and categorize content based on your preferences.
    









HTTP request
Path parameters
Request body
Response body
Authorization scopes
Try it!




Deletes the table specified by tableId from the dataset. If the table contains data, all the data will be deleted.



HTTP request
DELETE https://bigquery.googleapis.com/bigquery/v2/projects/{projectId}/datasets/{datasetId}/tables/{tableId}The URL uses gRPC Transcoding syntax.


Path parameters







Parameters




projectId

string
Required. Project ID of the table to delete



datasetId

string
Required. Dataset ID of the table to delete



tableId

string
Required. Table ID of the table to delete






Request body
The request body must be empty.


Response body
If successful, the response body is an empty JSON object.


Authorization scopes
Requires one of the following OAuth scopes:

https://www.googleapis.com/auth/bigquery
https://www.googleapis.com/auth/cloud-platform
For more information, see the Authentication Overview.














  
    
    Send feedback
  
  



