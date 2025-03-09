# Google Cloud Storage API: cancel






    
        Home
      
  




    
        Cloud Storage
      
  




    
        Documentation
      
  




    
        Reference
      
  







  
    
    Send feedback
  
  


      Operations: cancel
      
    



      
      Stay organized with collections
    

      
      Save and categorize content based on your preferences.
    








Starts asynchronous cancellation on a long-running operation. The server makes a best effort to
cancel the operation, but success is not guaranteed. If the server doesn't support this method, it
returns google.rpc.Code.UNIMPLEMENTED.
Users can use
Operations: get or other
methods to check whether the cancellation succeeded or whether the operation completed despite
cancellation. On successful cancellation, the operation is not deleted; instead, it becomes an
operation with an Operation.error value with a
google.rpc.Status.code of 1, corresponding to Code.CANCELLED. For more
information about these values, see the
Operations resource representation.

Required permissions
The authenticated user must have the following IAM permissions on the bucket to
use this method:

storage.bucketOperations.cancel


Request
HTTP request
POST https://storage.googleapis.com/storage/v1/b/bucket/operations/operationId/cancel
In addition to standard query parameters,
  the following query parameters apply to this method.
To see an example of how to include query parameters in a request, see the
  JSON API Overview page.
Parameters



Parameter name
Value
Description




Path parameters


bucket
string

          Name of a bucket.
        


operationId
string

          The ID of the operation.
        



Request body
Do not supply a request body with this method.


Response
If successful, this method returns an empty response body.
For information about status and error codes returned by this API, see the
    reference page.








  
    
    Send feedback
  
  



