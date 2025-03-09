# BigQuery API: undelete






    
        Home
      
  




    
        BigQuery
      
  




    
        Documentation
      
  




    
        Reference
      
  







  
    
    Send feedback
  
  


      Method: datasets.undelete
      
    



      
      Stay organized with collections
    

      
      Save and categorize content based on your preferences.
    









HTTP request
Path parameters
Request body
Response body
Authorization scopes
Try it!




Undeletes a dataset which is within time travel window based on datasetId. If a time is specified, the dataset version deleted at that time is undeleted, else the last live version is undeleted.



HTTP request
POST https://bigquery.googleapis.com/bigquery/v2/projects/{projectId}/datasets/{datasetId}:undeleteThe URL uses gRPC Transcoding syntax.


Path parameters







Parameters




projectId

string
Required. Project ID of the dataset to be undeleted



datasetId

string
Required. Dataset ID of dataset being deleted






Request body
The request body must be empty.


Response body
If successful, the response body contains an instance of Dataset.


Authorization scopes
Requires one of the following OAuth scopes:

https://www.googleapis.com/auth/bigquery
https://www.googleapis.com/auth/cloud-platform
For more information, see the Authentication Overview.














  
    
    Send feedback
  
  



