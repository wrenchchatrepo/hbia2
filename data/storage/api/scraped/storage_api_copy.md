# Google Cloud Storage API: copy






    
        Home
      
  




    
        Cloud Storage
      
  




    
        Documentation
      
  




    
        Reference
      
  







  
    
    Send feedback
  
  


      Objects: copy
      
    



      
      Stay organized with collections
    

      
      Save and categorize content based on your preferences.
    








Copies a source object to a destination object. Optionally overrides metadata.
Generally, you should use the rewrite
  method instead of the copy method: the copy method uses the
  rewrite method, but calls it exactly once. Larger objects can require multiple
  rewrite calls, so copy attempts of such objects can lead to
  Payload too large errors.
Note: The copied object does not retain the ACLs of the
  original object. Instead, it gains any ACLs you specify in the copy method or, if
  you don't specify any ACLs, the default object ACLs of the bucket it is stored in.

Required permissions
The authenticated user must have the following IAM permissions to use this method:

storage.objects.create on the destination bucket
storage.objects.delete on the destination bucket, if overwriting an existing object
storage.objects.setRetention on the destination bucket, if the request body
    includes the retention property.
storage.objects.get on the source bucket



Request
HTTP request
POST https://storage.googleapis.com/storage/v1/b/sourceBucket/o/sourceObject/copyTo/b/destinationBucket/o/destinationObject
In addition to standard query parameters,
  the following query parameters apply to this method.
To see an example of how to include query parameters in a request, see the
  JSON API Overview page.
Parameters



Parameter name
Value
Description




Path parameters


destinationBucket
string

          Name of the bucket in which to store the new object. Overrides the provided object
          metadata's bucket value, if any. For information about how to URL encode
          object names to be path safe,
          see Encoding URI path parts.
        


destinationObject
string

          Name of the new object. Required when the object metadata is not otherwise provided.
          Overrides the object metadata's name value, if any.
        


sourceBucket
string

          Name of the bucket in which to find the source object.
        


sourceObject
string

          Name of the source object. For information about how to URL encode object names to be path
          safe, see Encoding URI path parts.
        


Optional query parameters


destinationKmsKeyName
string

Resource name of the
          Cloud KMS key that will be used to encrypt the object. The Cloud KMS
          key must be located in same location as the object.
          If the parameter is not specified, the request uses the destination bucket's
          default encryption key, if any, or else it uses
          standard Cloud Storage
          encryption.
          If the object is large, re-encryption with the key may take too long and result
          in a Deadline exceeded error. For large objects, consider using the
          rewrite method instead.
        


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
        


ifGenerationNotMatch
long

          Makes the operation conditional on there being a live destination object with a generation
          number that does not match the given value. If no live destination object exists, the
          precondition fails. Setting ifGenerationNotMatch to 0 makes the operation
          succeed if there is a live version of the object.
        


ifMetagenerationMatch
long

          Makes the operation conditional on there being a live destination object with a
          metageneration number that matches the given value.
        


ifMetagenerationNotMatch
long

          Makes the operation conditional on there being a live destination object with a
          metageneration number that does not match the given value.
        


ifSourceGenerationMatch
long

          Makes the operation conditional on whether the source object's generation matches the
          given value.
        


ifSourceGenerationNotMatch
long

          Makes the operation conditional on whether the source object's generation does not match
          the given value.
        


ifSourceMetagenerationMatch
long

          Makes the operation conditional on whether the source object's current metageneration
          matches the given value.
        


ifSourceMetagenerationNotMatch
long

          Makes the operation conditional on whether the source object's current metageneration
          does not match the given value.
        


projection
string

          Set of properties to return. Defaults to noAcl, unless the object resource
          specifies the acl property, when it defaults to full.
          Acceptable values are:
          
full: Include all properties.
noAcl: Omit the owner, acl property.




sourceGeneration
long

          If present, selects a specific revision of the source object (as opposed to the latest
          version, the default).
        


Optional extension headers

X-Goog-Copy-Source-Encryption-Algorithm
string

          The encryption algorithm to use, which must be AES256. Used if the source
          object was encrypted with a customer-supplied
          encryption key.
        


X-Goog-Copy-Source-Encryption-Key
string

          An RFC 4648
          Base64-encoded string of the AES-256 encryption key used to encrypt the source object, if
          it was encrypted with a customer-supplied
          encryption key.
        


X-Goog-Copy-Source-Encryption-Key-Sha256
string

          An RFC 4648
          Base64-encoded string of the SHA256 hash of the encryption key used to encrypt the source
          object, if it was encrypted with a
          customer-supplied encryption
          key.
        


X-Goog-Encryption-Algorithm
string

          The encryption algorithm to use, which must be AES256. Used for encrypting
          the destination object with a
          customer-supplied encryption
          key.
        


X-Goog-Encryption-Key
string

          An RFC 4648
          Base64-encoded string of your AES-256 encryption key. Used for encrypting the destination
          object with a customer-supplied
          encryption key.
        


X-Goog-Encryption-Key-Sha256
string

          An RFC 4648
          Base64-encoded string of the SHA256 hash of your encryption key. Used for encrypting the
          destination object with a customer-supplied
          encryption key.
        



Request body
In the request body, supply metadata to apply to the destination object by using an
    object resource. If the request body
    is empty, editable metadata from the source object
    is applied to the destination object, with the exception of any ACLs, object holds, or
    retention configuration set on the source object. If you want to retain these from
    the original object, they must be included in the request body.


Response
If successful, this method returns an
    object resource in the response
    body.
For information about status and error codes returned by this API, see the
    reference page.


Try it!
Use the APIs Explorer below to call this method on live data and see the response.









  
    
    Send feedback
  
  



