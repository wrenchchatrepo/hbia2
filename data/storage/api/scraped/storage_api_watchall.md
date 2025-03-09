# Google Cloud Storage API: watchAll






    
        Home
      
  




    
        Cloud Storage
      
  




    
        Documentation
      
  




    
        Reference
      
  







  
    
    Send feedback
  
  


      Objects: watchAll
      
    



      
      Stay organized with collections
    

      
      Save and categorize content based on your preferences.
    








Note: This method applies to the
  Object Change Notification feature, which
  is not the recommended way to create notifications for Cloud Storage. Instead, use
  Pub/Sub Notifications for
  Cloud Storage, which are faster, more flexible, easier to set up, and more
  cost-effective.
Watch for changes on all objects in a bucket.

Required permissions
The authenticated user must have the storage.buckets.update IAM
permission to use this method.


Request
HTTP request
POST https://storage.googleapis.com/storage/v1/b/bucket/o/watch
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

          Name of the bucket in which to look for objects.
        


Optional query parameters


delimiter
string
This parameter is not implemented for the watchAll method.


endOffset
string
This parameter is not implemented for the watchAll method.


includeTrailingDelimiter
integer
This parameter is not implemented for the watchAll method.


maxResults
integer
This parameter is not implemented for the watchAll method.


pageToken
string
This parameter is not implemented for the watchAll method.


prefix
string
This parameter is not implemented for the watchAll method.


projection
string
This parameter is not implemented for the watchAll method.


startOffset
string
This parameter is not implemented for the watchAll method.


versions
boolean
This parameter is not implemented for the watchAll method.



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
Identifies this as a notification channel used to watch for changes to a resource.
          This value is always "api#channel".




id
string
A UUID or similar unique string that identifies this channel.




resourceId
string
An opaque ID that identifies the resource being watched on this channel. Stable across
          different API versions.




resourceUri
string
A version-specific identifier for the watched resource.




token
string
An arbitrary string delivered to the target address with each notification delivered
          over this channel. Optional.




expiration
long1
Date and time of notification channel expiration, expressed as a Unix timestamp, in
          milliseconds. Optional.




type
string
The type of delivery mechanism used for this channel. This value is always
          "WEBHOOK".




address
string
The address where notifications are delivered for this channel.




params
object
Additional parameters controlling delivery channel behavior. Optional.




params.(key)
string
Declares a new parameter by name.




payload
boolean
A Boolean value to indicate whether payload is wanted. Optional.





1 This property is a string formatted as the specified value type.
  


Response
If successful, this method returns a response body with the following structure:

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
Identifies this as a notification channel used to watch for changes to a resource.
          This value is always "api#channel".




id
string
A UUID or similar unique string that identifies this channel.




resourceId
string
An opaque ID that identifies the resource being watched on this channel. Stable across
          different API versions.




resourceUri
string
A version-specific identifier for the watched resource.




token
string
An arbitrary string delivered to the target address with each notification delivered
          over this channel. Optional.




expiration
long1
Date and time of notification channel expiration, expressed as a Unix timestamp, in
          milliseconds. Optional.




type
string
The type of delivery mechanism used for this channel.




address
string
The address where notifications are delivered for this channel.




params
object
Additional parameters controlling delivery channel behavior. Optional.




params.(key)
string
Declares a new parameter by name.




payload
boolean
A Boolean value to indicate whether payload is wanted. Optional.





1 This property is a string formatted as the specified value type.
      For information about status and error codes returned by this API, see the
    reference page.



Try it!
Use the APIs Explorer below to call this method on live data and see the response.









  
    
    Send feedback
  
  



