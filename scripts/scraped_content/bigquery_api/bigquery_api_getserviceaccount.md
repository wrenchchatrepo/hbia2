# BigQuery API: getServiceAccount






    
        Home
      
  




    
        BigQuery
      
  




    
        Documentation
      
  




    
        Reference
      
  







  
    
    Send feedback
  
  


      Method: projects.getServiceAccount
      
    



      
      Stay organized with collections
    

      
      Save and categorize content based on your preferences.
    









HTTP request
Path parameters
Request body
Response body

JSON representation


Authorization scopes
Try it!




RPC to get the service account for a project used for interactions with Google Cloud KMS



HTTP request
GET https://bigquery.googleapis.com/bigquery/v2/projects/{projectId}/serviceAccountThe URL uses gRPC Transcoding syntax.


Path parameters







Parameters




projectId

string
Required. ID of the project.






Request body
The request body must be empty.


Response body


Response object of projects.getServiceAccount
If successful, the response body contains data with the following structure:





JSON representation




{
  "kind": string,
  "email": string
}












Fields




kind

string
The resource type of the response.



email

string
The service account email address.








Authorization scopes
Requires one of the following OAuth scopes:

https://www.googleapis.com/auth/bigquery
https://www.googleapis.com/auth/cloud-platform
https://www.googleapis.com/auth/bigquery.readonly
https://www.googleapis.com/auth/cloud-platform.read-only
For more information, see the Authentication Overview.














  
    
    Send feedback
  
  



