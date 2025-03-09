# BigQuery API: getIamPolicy






    
        Home
      
  




    
        BigQuery
      
  




    
        Documentation
      
  




    
        Reference
      
  







  
    
    Send feedback
  
  


      Method: tables.getIamPolicy
      
    



      
      Stay organized with collections
    

      
      Save and categorize content based on your preferences.
    









HTTP request
Path parameters
Request body

JSON representation


Response body
Authorization scopes
Try it!




Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set.



HTTP request
POST https://bigquery.googleapis.com/bigquery/v2/{resource=projects/*/datasets/*/tables/*}:getIamPolicyThe URL uses gRPC Transcoding syntax.


Path parameters







Parameters




resource

string
REQUIRED: The resource for which the policy is being requested. See Resource names for the appropriate value for this field.






Request body
The request body contains data with the following structure:




JSON representation




{
  "options": {
    object (GetPolicyOptions)
  }
}












Fields




options

object (GetPolicyOptions)
OPTIONAL: A GetPolicyOptions object for specifying options to tables.getIamPolicy.







Response body
If successful, the response body contains an instance of Policy.


Authorization scopes
Requires one of the following OAuth scopes:

https://www.googleapis.com/auth/bigquery
https://www.googleapis.com/auth/cloud-platform
https://www.googleapis.com/auth/bigquery.readonly
https://www.googleapis.com/auth/cloud-platform.read-only
For more information, see the Authentication Overview.














  
    
    Send feedback
  
  



