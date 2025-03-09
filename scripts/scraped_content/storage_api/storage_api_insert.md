# Google Cloud Storage API: insert






    
        Home
      
  




    
        Cloud Storage
      
  




    
        Documentation
      
  




    
        Reference
      
  







  
    
    Send feedback
  
  


      Objects: insert
      
    



      
      Stay organized with collections
    

      
      Save and categorize content based on your preferences.
    








Stores a new object and metadata. The uploaded object replaces any existing object
with the same name. For an overview of uploading to Cloud Storage, see
  Uploads and downloads. For examples of performing
  object uploads with different Cloud Storage tools and client libraries, see the
  Uploading Objects guide.
This method accepts uploaded object data with the following characteristics:

Maximum file size: 5 TiB
Accepted Media MIME types: */*

This method generally requires the following headers be included in a request:

Content-Length
Content-Type

Note: Metadata-only requests are not allowed. To change an object's metadata,
  use the patch method.

Required permissions
The authenticated user must have the storage.objects.create IAM
 permission to use this method. If the object being inserted has the same name as an existing
 object, the user must also have the storage.objects.delete permission to overwrite the
 existing object. If the request body includes the retention property, the
 authenticated user must also have the storage.objects.setRetention IAM
 permission.


Request
HTTP request
Note: The request endpoint for this method
    differs from typical Cloud Storage JSON API endpoints.
POST https://storage.googleapis.com/upload/storage/v1/b/bucket/o
In addition to standard query parameters,
  the following query parameters apply to this method. Note that for
  resumable uploads, these headers can be used in the
  initial POST request but are ignored in the subsequent PUT requests.
To see an example of how to include query parameters in a request, see the
  JSON API Overview page.
Parameters



Parameter name
Value
Description




Path parameters


bucket
string

          Name of the bucket in which to store the new object. Overrides the provided object
          metadata's bucket value, if any.
        


Required query parameters


name
string

          Name of the object. Not required if the request body contains object metadata that
          includes a name value. Overrides the object metadata's name
          value, if any. For information about how to URL encode object names to be path safe, see
          Encoding URI path parts.
        


uploadType
string
The type of upload request to the
          /upload URI. Acceptable values are:
          
media - Data-only upload. Upload the object data only, without any
              metadata.
multipart - Multipart upload. Upload both the object data and its
              metadata, in a single request.
resumable - Resumable upload. Upload the object data in a resumable
              fashion, using a series of at least two requests where the first request includes the
              metadata.




Optional query parameters


contentEncoding
string

          If set, sets the contentEncoding property of the final object to this value.
          Setting this parameter is equivalent to setting the contentEncoding metadata
          property. This can be useful when uploading an object with uploadType=media
          to indicate the encoding of the content being uploaded.
        


ifGenerationMatch
long

          Makes the operation conditional on whether the object's current generation matches the
          given value. Setting to 0 makes the operation succeed only if there are no live versions
          of the object. For more information, see
          Request preconditions.
        


ifGenerationNotMatch
long

          Makes the operation conditional on whether the object's current generation does not match
          the given value. If no live object exists, the precondition fails. Setting to 0 makes the
          operation succeed only if there is a live version of the object. For more information, see
          Request preconditions.
        


ifMetagenerationMatch
long

          Makes the operation conditional on whether the object's current metageneration matches
          the given value. For more information, see
          Request preconditions.
        


ifMetagenerationNotMatch
long

          Makes the operation conditional on whether the object's current metageneration does not
          match the given value. For more information, see
          Request preconditions.
        


kmsKeyName
string

Resource name of
          the Cloud KMS key that will be used to encrypt the object. If not specified,
          the request uses the bucket's default Cloud KMS key, if any, or else it uses
          standard Cloud Storage
          encryption.
        


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

          Set of properties to return. Defaults to noAcl, unless the object resource
          specifies the acl property, when it defaults to full.
          Acceptable values are:
          
full: Include all properties.
            
noAcl: Omit the owner, acl property.
            




Optional extension headers


X-Goog-Encryption-Algorithm
string

          The encryption algorithm to use, which must be AES256. Used when encrypting
          the uploaded object with a customer-supplied
          encryption key.
        


X-Goog-Encryption-Key
string

          An RFC 4648
          Base64-encoded string of your AES-256 encryption key. Used when encrypting the uploaded
          object with a customer-supplied
          encryption key.
        


X-Goog-Encryption-Key-Sha256
string

          An RFC 4648
          Base64-encoded string of the SHA256 hash of your encryption key. Used when encrypting the
          uploaded object with a customer-supplied
          encryption key.
        


X-Goog-Meta-KEY
string

          Applicable only when used the final request of a
          resumable upload. An optional way to set
          custom metadata for the uploaded
          object.
        



Request body
When performing a simple upload, provide the
    object data in the request body. When performing a
    multipart upload or when
    initiating a resumable upload, both of which allow
    you to include object metadata as part of the request, supply the following properties. If you
    do not wish to provide object metadata in a resumable upload, the request body can be empty.



Property name
Value
Description
Notes




Optional Properties


acl[]
list
Access controls on the object, containing one or more
          objectAccessControls
          Resources. Do not supply this field if
          iamConfiguration.uniformBucketLevelAccess.enabled is true for
          the bucket to which you are uploading the object.
        

          writable
        


cacheControl
string
Cache-Control
          directive for the object data. If omitted, and the object is accessible to all anonymous
          users, the default will be "public, max-age=3600".

          writable
        


contentDisposition
string
Content-Disposition
          of the object data.

          writable
        


contentEncoding
string
Content-Encoding
          of the object data.

          writable
        


contentLanguage
string
Content-Language
          of the object data.

          writable
        


contentType
string
Content-Type
          of the object data. If an object is stored without a Content-Type, it is served as
          application/octet-stream.

          writable
        


crc32c
string
CRC32c checksum, as described in
          RFC 4960,
          Appendix B; encoded using
          base64 in
          big-endian byte order. For more information about using the CRC32c checksum, see
          Data validation.

          writable
        


customTime
datetime1
A user-specified timestamp for the object in
          RFC 3339 format.

          writable
        


eventBasedHold
boolean
Whether or not the object is subject to an
          event-based hold.

          writable
        


md5Hash
string
MD5 hash of the data; encoded using
          base64.
          For more information about using the MD5 hash, see
          Data validation.

          writable
        


metadata
object
User-provided metadata, in key/value pairs.

          writable
        


metadata.(key)
string
An individual metadata entry.

          writable
        


name
string
The name of the object. Required if not specified by URL parameter.

          writable
        


retention
object
The object's retention configuration, which
          defines the earliest datetime that the object can be deleted or replaced.

          writable
        


retention.mode
string
The mode of the retention configuration, which can be either Unlocked or
          Locked. If set to Locked, retention.mode cannot be
          changed, the retention configuration cannot be removed, and
          retention.retainUntilTime cannot be reduced.

          writable
        


retention.retainUntilTime
datetime1
The earliest time that the object can be deleted or replaced,
          in RFC 3339
          format. This property has a maximum value of 3,155,760,000 seconds (100 years) from the
          current date and time.

          writable
        


storageClass
string
Storage class of the object.

          writable
        


temporaryHold
boolean
Whether or not the object is subject to a
          temporary hold.

          writable
        



1 This property is a string formatted as the specified value type.


Response
If successful, this method returns an
    object resource in the response
    body.
For information about status and error codes returned by this API, see the
    reference page.








  
    
    Send feedback
  
  



