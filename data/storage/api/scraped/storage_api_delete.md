# Google Cloud Storage API: delete






    
        Home
      
  




    
        Cloud Storage
      
  




    
        Documentation
      
  




    
        Reference
      
  







  
    
    Send feedback
  
  


      Projects.hmacKeys: delete
      
    



      
      Stay organized with collections
    

      
      Save and categorize content based on your preferences.
    








Caution: HMAC keys cannot be recovered once you delete
them.
Deletes an HMAC key.
For general information about HMAC keys in Cloud Storage, see
  HMAC Keys.

Required permissions
In order to use this method, the authenticated user must have the
storage.hmacKeys.delete IAM permission for the project in which the
key exists.


Request
HTTP request
DELETE https://storage.googleapis.com/storage/v1/projects/projectIdentifier/hmacKeys/accessId
In addition to standard query
  parameters, the following query parameters apply to this method.
To see an example of how to include query parameters in a request, see the
  JSON API Overview page.
Parameters



Parameter name
Value
Description




Path parameters


accessId
string

          The access ID of the HMAC key to be deleted.
        


projectIdentifier
string

          The project ID or project number of the project that owns the service account of the
          specified HMAC key.
        



Request body
Do not supply a request body with this method.


Response
If successful, this method returns an empty response body.
For information about status and error codes returned by this API, see the
    reference page.


Try it!
Use the APIs Explorer below to call this method on live data and see the response.









  
    
    Send feedback
  
  



