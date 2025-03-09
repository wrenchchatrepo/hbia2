# Google Cloud Storage API: stop






    
        Home
      
  




    
        Cloud Storage
      
  




    
        Documentation
      
  




    
        Reference
      
  







  
    
    Send feedback
  
  


      Channels: stop
      
    



      
      Stay organized with collections
    

      
      Save and categorize content based on your preferences.
    








Note: This method applies to the
    Object Change Notification feature,
    which is not the recommended way to create notifications for Cloud Storage. Instead, use
    Pub/Sub Notifications for Cloud Storage,
    which are faster, more flexible, easier to set up, and more cost-effective.
Stop receiving object change notifications through this channel.
While this method accepts a full channel resource, only the id and resourceId
fields are necessary. Other elements of a channel resource are legal but ignored. This allows
retaining the results of an objects.watchAll call and passing that result in its
entirety to channels.stop. For more, see our guide on
Object Change Notifications.

Request
HTTP request
POST https://storage.googleapis.com/storage/v1/channels/stop
This method accepts standard query parameters.
Request body
In the request body, supply data with the following structure:

{
  "kind": "api#channel",
  "id": string,
  "resourceId": string,
  "resourceUri": string,
  "token": string,
  "expiration": "long",
  "type": string,
  "address": string,
  "payload": boolean,
  "params": {
    (key): string
  }
}



Property name
Value
Description
Notes




kind
string
Ignored.




id
string
A UUID or similar unique string that identifies this channel.




resourceId
string
An opaque ID that identifies the resource being watched on this channel. Stable across different API versions.




resourceUri
string
Ignored.




token
string
Ignored.




expiration
long1
Ignored.




type
string
Ignored.




address
string
Ignored.




params
object
Ignored.




params.(key)
string
Ignored.




payload
boolean
Ignored.





1 This property is a string formatted as the specified value type.
  


Response
If successful, this method returns an empty response body.


Try it!

    Use the APIs Explorer below to call this method on live data and see the response.
  









  
    
    Send feedback
  
  



