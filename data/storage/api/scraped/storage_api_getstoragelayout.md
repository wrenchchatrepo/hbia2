# Google Cloud Storage API: getStorageLayout






    
        Home
      
  




    
        Cloud Storage
      
  




    
        Documentation
      
  




    
        Reference
      
  







  
    
    Send feedback
  
  


      Buckets: getStorageLayout
      
    



      
      Stay organized with collections
    

      
      Save and categorize content based on your preferences.
    








Returns the storage layout of the specified bucket.

Required permissions
The authenticated user must have the storage.objects.list IAM
  permission to use this method.


Request
HTTP request
GET https://storage.googleapis.com/storage/v1/b/bucket/storageLayout
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
        


Optional query parameters


prefix
string

          If set, the storage.objects.list permission is checked for the specified prefix.
        



Request body
Do not supply a request body with this method.


Response
If successful, this method returns a response body with the following structure:

    {
      "kind": "storage#storageLayout",
      "bucket": string,
      "location": string,
      "locationType": string,
      "hierarchicalNamespace":
        {
        "enabled": boolean
        },
    }



Property name
Value
Description




kind
string
The The kind of item this is. For buckets, this is always storage#storageLayout.


bucket
string
The name of the bucket.


location
string
The location of the bucket. Object data for objects in the bucket resides in physical
          storage within this location. See Cloud Storage
          bucket locations for the authoritative list.


locationType
string
This property has a value of region.


hierarchicalNamespace.enabled
boolean
Whether or not 
          hierarchical namespace is enabled for this bucket.



For information about status and error codes returned by this API, see the
  reference page.


Try it!

    Use the APIs Explorer below to call this method on live data and see the response.
  









  
    
    Send feedback
  
  



