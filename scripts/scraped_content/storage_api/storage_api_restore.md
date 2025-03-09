# Google Cloud Storage API: restore






    
        Home
      
  




    
        Cloud Storage
      
  




    
        Documentation
      
  




    
        Reference
      
  







  
    
    Send feedback
  
  


      Buckets: restore
      
    



      
      Stay organized with collections
    

      
      Save and categorize content based on your preferences.
    








Restores a soft-deleted bucket.
The original bucket metadata, including IAM policies, custom metadata, and tags, but excluding managed folders, is restored and the softDeleteTime and hardDeleteTime is cleared. No objects are restored. If a live bucket with the same name already exists, the bucket cannot be restored.
After the bucket is live again, the objects can be restored with the
  Objects:restore or Objects:bulkRestore APIs.


Required permissions
The authenticated user must have the storage.buckets.restore IAM permission at the project level or above to use this method. To return access control lists (ACLs) as part of the response, the authenticated user must also have the storage.buckets.getIamPolicy permission.


Request
HTTP request
POST https://storage.googleapis.com/storage/v1/b/bucket/restore
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

         Name of the bucket to be restored.
        


Required query parameters


generation
long

          The specific version of the bucket to be restored.
        


Optional query parameters


projection
string

Set of properties to return. Defaults to full.

          Acceptable values are:
          
full: Include all properties.
noAcl: Omit owner, acl, and defaultObjectAcl properties.





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
  
  



