# Google Cloud Storage API: create






    
        Home
      
  




    
        Cloud Storage
      
  




    
        Documentation
      
  




    
        Reference
      
  







  
    
    Send feedback
  
  


      Projects.hmacKeys: create
      
    



      
      Stay organized with collections
    

      
      Save and categorize content based on your preferences.
    








Creates a new HMAC key for the specified service account.
For general information about HMAC keys in Cloud Storage, see
  HMAC Keys.

Required permissions
In order to use this method, the authenticated user must have the
storage.hmacKeys.create IAM permission on the project in which the key
will be created.


Request
HTTP request
POST https://storage.googleapis.com/storage/v1/projects/projectIdentifier/hmacKeys
In addition to standard query
  parameters, the following query parameters apply to this method.
To see an example of how to include query parameters in a request, see the
  JSON API Overview page.
Parameters



Parameter name
Value
Description




Path parameters


projectIdentifier
string

          The project ID or project number of the project that owns the service account.
        


Required query parameters


serviceAccountEmail
string

          The email address of the service account.
        



Request body
Do not supply a request body with this method.


Response
If successful, this method returns a
    Projects.hmacKeys resource
    in the response body.
For information about status and error codes returned by this API, see the
    reference page.


Try it!
Use the APIs Explorer below to call this method on live data and see the response.









  
    
    Send feedback
  
  



