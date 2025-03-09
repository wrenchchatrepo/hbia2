# Google Cloud Storage API: lockRetentionPolicy






    
        Home
      
  




    
        Cloud Storage
      
  




    
        Documentation
      
  




    
        Reference
      
  







  
    
    Send feedback
  
  


      Buckets: lockRetentionPolicy
      
    



      
      Stay organized with collections
    

      
      Save and categorize content based on your preferences.
    








Permanently locks the retention policy that is
currently applied to the specified bucket.
Caution: Locking a bucket is an irreversible action. Once
  you lock a bucket:
  You cannot remove the retention policy from the bucket.
You cannot decrease the retention period for the policy.
Once locked, you must delete the entire bucket in order to "remove" the bucket's
    retention policy. However, before you can delete the bucket, you must be
    able to delete all the objects in the bucket, which itself is only possible
    if the all objects have reached the retention period set by the retention policy.

Required permissions
The authenticated user must have the storage.buckets.update IAM
permission to use this method.


Request
HTTP request
POST https://storage.googleapis.com/storage/v1/b/bucket/lockRetentionPolicy
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
        


Required query parameters


ifMetagenerationMatch
long

          Makes the success of the request conditional on whether the bucket's current
          metageneration matches the given value.
        




Request body
Do not supply a request body with this method.

Response
If successful, this method returns a bucket
      resource in the response body.
For information about status and error codes returned by this API, see the
    reference page.


Try it!

    Use the APIs Explorer below to call this method on live data and see the response.
  









  
    
    Send feedback
  
  



