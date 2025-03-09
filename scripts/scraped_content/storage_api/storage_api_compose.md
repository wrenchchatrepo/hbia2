# Google Cloud Storage API: compose






    
        Home
      
  




    
        Cloud Storage
      
  




    
        Documentation
      
  




    
        Reference
      
  







  
    
    Send feedback
  
  


      Objects: compose
      
    



      
      Stay organized with collections
    

      
      Save and categorize content based on your preferences.
    








Concatenates a list of existing objects into a new object in the same bucket. The existing source
  objects are unaffected by this operation.
See Composite objects for a general discussion of
  object composition, and see Compose objects for
  tool-specific guides to performing a composition.

Required permissions
The authenticated user must have the storage.objects.create and
 storage.objects.get IAM permissions to use this method. If the new
  composite object overwrites an existing object, the authenticated user must also have the
  storage.objects.delete permission. If the request body includes the
  retention property, the authenticated user must also have the
  storage.objects.setRetention IAM permission.


Request
HTTP request
POST https://storage.googleapis.com/storage/v1/b/bucket/o/destinationObject/compose
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

          Name of the bucket containing the source objects. The destination object is stored in
          this bucket.
        


destinationObject
string

          Name of the new object. For information about how to URL encode object names to be path
          safe, see Encoding URI path parts.
        


Optional query parameters


destinationPredefinedAcl
string

          Apply a predefined set of access controls to the destination object.
          Acceptable values are:
          
authenticatedRead: Object owner gets OWNER access, and
              allAuthenticatedUsers get READER access.
bucketOwnerFullControl: Object owner gets OWNER access,
              and project team owners get OWNER access.
bucketOwnerRead: Object owner gets OWNER access, and
              project team owners get READER access.
private: Object owner gets OWNER access.
projectPrivate: Object owner gets OWNER access, and
              project team members get access according to their roles.
publicRead: Object owner gets OWNER access, and
              allUsers get READER access.

          If iamConfiguration.uniformBucketLevelAccess.enabled is set to
          true, requests that include this parameter fail with a
          400 Bad Request response.
        


ifGenerationMatch
long

          Makes the operation conditional on there being a live destination object with a generation
          number that matches the given value. Setting ifGenerationMatch to 0 makes the
          operation succeed only if there is no live destination object.
        


ifMetagenerationMatch
long

          Makes the operation conditional on there being a live destination object with a
          metageneration number that matches the given value.
        


kmsKeyName
string

Resource name of the Cloud
          KMS key that will be used to encrypt the composed object. If not specified, the
          request uses the bucket's default Cloud KMS key, if any, or else it uses
          standard Cloud Storage
          encryption.
        


Optional extension headers


X-Goog-Encryption-Algorithm
string

          The encryption algorithm to use, which must be AES256. Used when encrypting
          the composed object with a customer-supplied
          encryption key.
        


X-Goog-Encryption-Key
string

          An RFC 4648
          Base64-encoded string of your AES-256 encryption key. Used when encrypting the composed
          object with a customer-supplied
          encryption key.
        


X-Goog-Encryption-Key-Sha256
string

          An RFC 4648
          Base64-encoded string of the SHA256 hash of your encryption key. Used when encrypting the
          composed object with a customer-supplied
          encryption key.
        



Request body
In the request body, supply data with the following structure:

{
  "kind": "storage#composeRequest",
  "sourceObjects": [
    {
      "name": string,
      "generation": "long",
      "objectPreconditions": {
        "ifGenerationMatch": "long"
      }
    }
  ],
  "destination": objects Resource
}



Property name
Value
Description
Notes




kind
string
The kind of item this is.




destination
nested object
Properties of the resulting object.

          writable
        


sourceObjects[]
list
The list of source objects that will be concatenated into a single object. There is a
          limit of 32 components that can be composed in a single operation.




sourceObjects[].name
string
The source object's name. All source objects must reside in the same bucket and use the
          same storage class.

          writable
        


sourceObjects[].generation
long1
The generation of this object to use as the source.

          writable
        


sourceObjects[].objectPreconditions
object
Conditions that must be met for this operation to execute.




sourceObjects[].objectPreconditions.ifGenerationMatch
long1
Only perform the composition if the generation of the source object that would be used
          matches this value.  If this value and a generation are both specified, they must be the
          same value or the call will fail.

          writable
        



1 This property is a string formatted as the specified value type.
  


Response
If successful, this method returns an object
    resource in the response body, with the owner and acl
    properties omitted.
For information about status and error codes returned by this API, see the
    reference page.


Try it!

    Use the APIs Explorer below to call this method on live data and see the response.
  









  
    
    Send feedback
  
  



