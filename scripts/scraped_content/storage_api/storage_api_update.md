# Google Cloud Storage API: update






    
        Home
      
  




    
        Cloud Storage
      
  




    
        Documentation
      
  




    
        Reference
      
  







  
    
    Send feedback
  
  


      Projects.hmacKeys: update
      
    



      
      Stay organized with collections
    

      
      Save and categorize content based on your preferences.
    








Updates the state of an HMAC key. See the HMAC
  Key resource descriptor for valid states.
For general information about HMAC keys in Cloud Storage, see
  HMAC Keys.

Required permissions
In order to use this method, the authenticated user must have the
storage.hmacKeys.update IAM permission for the project in which the
key exists.


Request
HTTP request
PUT https://storage.googleapis.com/storage/v1/projects/projectIdentifier/hmacKeys/accessId
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

          The access ID of the HMAC key being updated.
        


projectIdentifier
string

          The project ID or project number of the project that owns the service account of the
          specified HMAC key.
        



Request body
In the request body, supply the metadata portion of a
    Projects.hmacKeys resource
    with the following properties:



Property name
Value
Description
Notes




Optional Properties


etag
string
HTTP 1.1 Entity tag for
            the HMAC key. Inclusion of an etag makes the operation's success conditional on
            the HMAC key's current etag matching the given value.



state
string
The state of the key. Can be updated to ACTIVE or INACTIVE. To set the state of the
          key to DELETED, use the `hmacKeys.delete` method.
writable





Response
If successful, this method returns the metadata portion of a
    Projects.hmacKeys resource
    in the response body.
For information about status and error codes returned by this API, see the
    reference page.


Try it!
Use the APIs Explorer below to call this method on live data and see the response.









  
    
    Send feedback
  
  



