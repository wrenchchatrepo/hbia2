# Google Cloud Storage API: list






    
        Home
      
  




    
        Cloud Storage
      
  




    
        Documentation
      
  




    
        Reference
      
  







  
    
    Send feedback
  
  


      Projects.hmacKeys: list
      
    



      
      Stay organized with collections
    

      
      Save and categorize content based on your preferences.
    








Retrieves a list of HMAC keys matching the criteria..
For general information about HMAC keys in Cloud Storage, see
  HMAC Keys.

Required permissions
In order to use this method, the authenticated user must have the
storage.hmacKeys.list IAM permission for the project in which the
keys exist.


Request
HTTP request
GET https://storage.googleapis.com/storage/v1/projects/projectIdentifier/hmacKeys
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

          The project ID or project number of the project in which to look for HMAC keys.
        


Optional query parameters


maxResults
unsigned integer

          Maximum number of items to return in a single page of responses.
          
          The service may return fewer results than maxResults. If the response
          includes a nextPageToken, there are more results not included in this
          response.
        


pageToken
string

          A previously-returned page token representing part of the larger set of results to view.
        


serviceAccountEmail
string
If present, only HMAC keys for the given service account are returned.


showDeletedKeys
boolean
If true, include keys in the DELETED state. Default is false.



Request body
Do not supply a request body with this method.


Response
If successful, this method returns a response body with the following structure:

{
  "kind": "storage#hmacKeysMetadata",
  "nextPageToken": string,
  "items": [
    Metadata portion of an hmacKeys resource
  ]
}



Property name
Value
Description
Notes




kind
string
The kind of item this is. For lists of hmacKeys, this is always
          "storage#hmacKeysMetadata".



nextPageToken
string
The continuation token. Provide this value as the pageToken of a subsequent
          request in order to return the next page of results. Note that the next page may be empty.
          If this is the last page of results, then no continuation token is returned. The presence
          of this parameter in the response should always be checked to ensure a complete listing of
          all the results.



items[]
list
The list of items.




For information about status and error codes returned by this API, see the
    reference page.



Try it!
Use the APIs Explorer below to call this method on live data and see the response.









  
    
    Send feedback
  
  



