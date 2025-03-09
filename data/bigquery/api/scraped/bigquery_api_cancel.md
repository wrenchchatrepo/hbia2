# BigQuery API: cancel






    
        Home
      
  




    
        BigQuery
      
  




    
        Documentation
      
  




    
        Reference
      
  







  
    
    Send feedback
  
  


      Method: jobs.cancel
      
    



      
      Stay organized with collections
    

      
      Save and categorize content based on your preferences.
    









HTTP request
Path parameters
Query parameters
Request body
Response body

JSON representation


Authorization scopes
Try it!




Requests that a job be cancelled. This call will return immediately, and the client will need to poll for the job status to see if the cancel completed successfully. Cancelled jobs may still incur costs.



HTTP request
POST https://bigquery.googleapis.com/bigquery/v2/projects/{projectId}/jobs/{jobId}/cancelThe URL uses gRPC Transcoding syntax.


Path parameters







Parameters




projectId

string
Required. Project ID of the job to cancel



jobId

string
Required. Job ID of the job to cancel






Query parameters







Parameters




location

string
The geographic location of the job. You must specify the location to run the job for the following scenarios:

If the location to run a job is not in the us or  the eu multi-regional location
If the job's location is in a single region (for example,  us-central1)







Request body
The request body must be empty.


Response body


Describes format of a jobs cancellation response.
If successful, the response body contains data with the following structure:





JSON representation




{
  "kind": string,
  "job": {
    object (Job)
  }
}












Fields




kind

string
The resource type of the response.



job

object (Job)
The final state of the job.








Authorization scopes
Requires one of the following OAuth scopes:

https://www.googleapis.com/auth/bigquery
https://www.googleapis.com/auth/cloud-platform
For more information, see the Authentication Overview.














  
    
    Send feedback
  
  



