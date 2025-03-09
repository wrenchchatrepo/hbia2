# Google Cloud Storage API: patch






    
        Home
      
  




    
        Cloud Storage
      
  




    
        Documentation
      
  




    
        Reference
      
  







  
    
    Send feedback
  
  


      Objects: patch
      
    



      
      Stay organized with collections
    

      
      Save and categorize content based on your preferences.
    








Updates a data blob's associated metadata. This method supports
  patch semantics.

Required permissions
The authenticated user must have the storage.objects.update IAM
  permission to use this method. If the request body includes the retention property,
  the authenticated user must also have the storage.objects.setRetention
  IAM permission, and if the request includes the query parameter
  overrideUnlockedRetention, the authenticated user must also have the
  storage.objects.overrideUnlockedRetention IAM permission.
To update object access control lists (ACLs), which only apply to objects stored in buckets with
  uniform bucket-level access disabled, the
  authenticated user must also have the storage.objects.setIamPolicy permission. To
  return ACLs as part of the response, the authenticated user must also have the
  storage.objects.getIamPolicy permission.


Request
HTTP request
PATCH https://storage.googleapis.com/storage/v1/b/bucket/o/object
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

          Name of the bucket in which the object resides.
        


object
string

          Name of the object. For information about how to URL encode object names to be path safe,
          see Encoding URI path parts.
        


Optional query parameters


generation
long

          If present, selects a specific revision of this object (as opposed to the latest version,
          the default).
        


ifGenerationMatch
long

          Makes the operation conditional on whether the object's current generation matches the
          given value. Setting to 0 makes the operation succeed only if there are no live versions
          of the object.
        


ifGenerationNotMatch
long

          Makes the operation conditional on whether the object's current generation does not match
          the given value. If no live object exists, the precondition fails. Setting to 0 makes the
          operation succeed only if there is a live version of the object.
        


ifMetagenerationMatch
long

          Makes the operation conditional on whether the object's current metageneration matches
          the given value.
        


ifMetagenerationNotMatch
long

          Makes the operation conditional on whether the object's current metageneration does not
          match the given value.
        


overrideUnlockedRetention
boolean

          Applicable for object's that have an unlocked
          retention configuration: Required to be set to
          true if the operation includes a retention property that changes
          the mode to Locked, reduces the retainUntilTime,
          or removes the retention configuration from the object.
        


predefinedAcl
string

          Apply a predefined set of access controls to this object.
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
        


projection
string

          Set of properties to return. Defaults to noAcl.NOTE: Currently only
          works if you override the default and specify full.
          Acceptable values are:
          
full: Include all properties.
            
noAcl: Omit the owner, acl property.
            




Optional extension headers


X-Goog-Encryption-Algorithm
string

          The encryption algorithm to use, which must be AES256. Use this header if the
          object is encrypted with a customer-supplied
          encryption key and you want the object's content hashes returned in the response.
        


X-Goog-Encryption-Key
string

          An RFC 4648
          Base64-encoded string of your AES-256 encryption key. Use this header if the object is
          encrypted with a customer-supplied
          encryption key and you want the object's content hashes returned in the response.
        


X-Goog-Encryption-Key-Sha256
string

          An RFC 4648
          Base64-encoded string of the SHA256 hash of your encryption key. Use this header if the
          object is encrypted with a customer-supplied
          encryption key and you want the object's content hashes returned in the response.
        



Request body
In the request body, supply the relevant portions of an
    object resource, according to the rules
    of patch semantics.


Response
If successful, this method returns an
    object resource in the response body.
For information about status and error codes returned by this API, see the
    reference page.


Try it!
Use the APIs Explorer below to call this method on live data and see the response.









  
    
    Send feedback
  
  



