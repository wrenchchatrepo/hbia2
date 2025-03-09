# BigQuery API: insert






    
        Home
      
  




    
        BigQuery
      
  




    
        Documentation
      
  




    
        Reference
      
  







  
    
    Send feedback
  
  


      Method: tables.insert
      
    



      
      Stay organized with collections
    

      
      Save and categorize content based on your preferences.
    









HTTP request
Path parameters
Request body
Response body
Authorization scopes
Try it!




Creates a new, empty table in the dataset.



HTTP request
POST https://bigquery.googleapis.com/bigquery/v2/projects/{projectId}/datasets/{datasetId}/tablesThe URL uses gRPC Transcoding syntax.


Path parameters







Parameters




projectId

string
Required. Project ID of the new table



datasetId

string
Required. Dataset ID of the new table






Request body
The request body contains an instance of Table.


Response body
If successful, the response body contains a newly created instance of Table.


Authorization scopes
Requires one of the following OAuth scopes:

https://www.googleapis.com/auth/bigquery
https://www.googleapis.com/auth/cloud-platform
For more information, see the Authentication Overview.














  
    
    Send feedback
  
  



