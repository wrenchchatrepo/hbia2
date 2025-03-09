# Google Cloud Storage API: listChannels






    
        Home
      
  




    
        Cloud Storage
      
  




    
        Documentation
      
  




    
        Reference
      
  







  
    
    Send feedback
  
  


      Buckets: listChannels
      
    



      
      Stay organized with collections
    

      
      Save and categorize content based on your preferences.
    








Note: This method applies to the
    Object Change Notification feature,
    which is not the recommended way to create notifications for Cloud Storage. Instead, use
    Pub/Sub Notifications for Cloud Storage,
    which are faster, more flexible, easier to set up, and more cost-effective.
Retrieves a list of active Object Change Notification channels for a bucket, ordered in the
  list lexicographically by name.

Required permissions
The authenticated user must have the storage.buckets.get IAM
permission to use this method.


Request
HTTP request
GET https://storage.googleapis.com/storage/v1/b/bucket/channels
In addition to standard query parameters,
  the following query parameters apply to this method:
Parameters



Parameter name
Value
Description




Path parameters


bucket
string

          Name of the bucket to list active channels for.
        



Request body
Do not supply a request body with this method.


Response
If successful, this method returns a response body with the following structure:

{
  "kind": "storage#channels",
  "items": [
    channel information
  ]
}



Property name
Value
Description
Notes




kind
string
The kind of item this is. For lists of active channels for buckets, this is always
          "storage#channels".




items[]
list
The list of channels.





For information about status and error codes returned by this API, see the
    reference page.









  
    
    Send feedback
  
  



