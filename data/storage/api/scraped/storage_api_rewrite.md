# Google Cloud Storage API: rewrite






    
        Home
      
  




    
        Cloud Storage
      
  




    
        Documentation
      
  




    
        Reference
      
  







  
    
    Send feedback
  
  


      Objects: rewrite
      
    



      
      Stay organized with collections
    

      
      Save and categorize content based on your preferences.
    








Rewrites a source object to a destination object. The source file is not modified, unless the
  source and destination objects are the same. Optionally overrides metadata.
For large objects, this method requires the use of multiple requests, which avoids having one
  very long timeout for a single request. In such cases, the method responds with the
  done flag set to false and also returns a rewriteToken. To
  complete the rewrite, you must keep calling the endpoint using the rewriteToken
  returned in the prior response until the done flag is true. You must
  complete rewrite operations within 1 week of when the rewriteToken was created.
  Attempts to use the token after it has expired fail with a
  410 error.
Keep the following in mind when using the rewrite method:

A rewrite completes in a single request, and you do not need to make additional calls
    specifying a rewriteToken if the following conditions are true:
    
The storage class of the object is not
        changing
The source and destination are in the same
        location
If the location is a dual-region, either the source bucket must have
        turbo replication
        enabled or the source object must have completed its
        replication across
        regions


Rewriting an object is charged as a single Class A operation, even when it requires the usage
    of a rewriteToken. However, depending on the storage classes and locations
    involved, a rewrite might incur other charges. For more information, see
    Cloud Storage pricing.
When you rewrite a composite object where the
    source and destination are different locations or storage classes, the result is a
    composite object that has a component count of 1.
Any timeout logic that you set in conjunction with using this method should be at least 30
    seconds.


Required permissions
The authenticated user must have the following IAM permissions to use this method:

storage.objects.create on the destination bucket
storage.objects.delete on the destination bucket, if overwriting an existing object
storage.objects.setRetention on the destination bucket, if the request body
    includes the retention property.
storage.objects.get on the source bucket



Request
HTTP request
POST https://storage.googleapis.com/storage/v1/b/sourceBucket/o/sourceObject/rewriteTo/b/destinationBucket/o/destinationObject
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
          metadata's bucket value, if any.
        


destinationObject
string

          Name of the new object. Required when the object metadata is not otherwise provided.
          Overrides the object metadata's name value, if any. For information about how
          to URL encode object names to be path safe, see
          Encoding URI path parts.
        


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
        


maxBytesRewrittenPerCall
long

          
          The maximum number of bytes that will be rewritten per rewrite request. Most callers
          shouldn't need to specify this parameter - it is primarily in place to support testing.
          If specified the value must be an integral multiple of 1 MiB (1048576). Also, this only
          applies to requests where the source and destination span locations or storage
          classes. Finally, this value must not change across rewrite calls else you'll get an error
          that the rewriteToken is invalid.
          
        


projection
string

          Set of properties to return. Defaults to noAcl, unless the object resource
          specifies the acl property, when it defaults to full.
          Acceptable values are:
          
full: Include all properties.
            
noAcl: Omit the owner, acl property.
            




rewriteToken
string

          Include this field (from the previous rewrite response) on each rewrite request after the
          first one, until the rewrite response 'done' flag is true. Calls that provide a
          rewriteToken can omit all other request fields, but if included those fields must match
          the values provided in the first rewrite request.
        


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
If successful, this method returns a response body with the following structure:

{
  "kind": "storage#rewriteResponse",
  "totalBytesRewritten": "unsigned long",
  "objectSize": "unsigned long",
  "done": boolean,
  "rewriteToken": string,
  "resource": objects Resource
}



Property name
Value
Description
Notes




kind
string
The kind of item this is.




totalBytesRewritten
unsigned long1
The total bytes written so far, which can be used to provide a waiting user with a
          progress indicator. This property is always present in the response.




objectSize
unsigned long1
The total size of the object being copied in bytes. This property is always present in
          the response.




done
boolean
true if the copy is finished; otherwise, false if the copy is
          in progress. This property is always present in the response.




rewriteToken
string
A token to use in subsequent requests to continue copying data. This token is present
          in the response only when there is more data to copy.




resource
nested object
A resource containing the metadata for the copied-to object. This property is present
          in the response only when copying completes.





1 This property is a string formatted as the specified value type.
      For information about status and error codes returned by this API, see the
    reference page.



Try it!
Use the APIs Explorer below to call this method on live data and see the response.









  
    
    Send feedback
  
  



