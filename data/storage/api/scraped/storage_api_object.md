# Google Cloud Storage API: object






    
        Home
      
  




    
        Cloud Storage
      
  




    
        Documentation
      
  




    
        Reference
      
  







  
    
    Send feedback
  
  


      Objects
      
    



      
      Stay organized with collections
    

      
      Save and categorize content based on your preferences.
    








The Objects resource represents an object within Cloud Storage. Objects are
    pieces of data that you have uploaded to Cloud Storage. For more information, see
    Object Name Requirements.
Every object in Cloud Storage resides in a
    bucket. The object is owned by its
    original uploader, who will always retain OWNER permission on it.
In addition to the acl property, objects contain
    objectAccessControls, for use in
    fine-grained manipulation of an existing object's access controls.
To try out the methods for this resource, see Methods.


Resource representations


{
  "kind": "storage#object",
  "id": string,
  "selfLink": string,
  "mediaLink": string,
  "name": string,
  "bucket": string,
  "generation": "long",
  "metageneration": "long",
  "contentType": string,
  "storageClass": string,
  "size": "unsigned long",
  "softDeleteTime": "datetime",
  "restoreToken": string,
  "hardDeleteTime": "datetime",
  "md5Hash": string,
  "contentEncoding": string,
  "contentDisposition": string,
  "contentLanguage": string,
  "cacheControl": string,
  "crc32c": string,
  "componentCount": integer,
  "etag": string,
  "kmsKeyName": string,
  "temporaryHold": boolean,
  "eventBasedHold": boolean,
  "retentionExpirationTime": "datetime",
  "retention": {
    "retainUntilTime": "datetime",
    "mode": string
  }
  "timeCreated": "datetime",
  "timeFinalized": "datetime",
  "updated": "datetime",
  "timeDeleted": "datetime",
  "timeStorageClassUpdated": "datetime",
  "customTime": "datetime",
  "metadata": {
    (key): string
  },
  "acl": [
    objectAccessControls Resource
  ],
  "owner": {
    "entity": string,
    "entityId": string
  },
  "customerEncryption": {
    "encryptionAlgorithm": string,
    "keySha256": string
  }
}



Property name
Value
Description
Notes




acl[]
list
Access controls on the object, containing one or more
          objectAccessControls
          Resources. Only requests that use the "projection=full" query parameter
          return this field in the response.
If iamConfiguration.uniformBucketLevelAccess.enabled is set to
            true, this field does not apply, and requests that specify it fail.


          writable
        


bucket
string
The name of the bucket containing this object.



cacheControl
string
Cache-Control
          directive for the object data. If omitted, and the object is accessible to all anonymous
          users, the default will be "public, max-age=3600".

          writable
        


componentCount
integer
Returned for composite objects only.
          Number of non-composite objects in the composite object. componentCount
          includes non-composite objects that were part of any composite objects used to
          compose the current object.



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
          RFC 4960, Appendix B;
          encoded using base64
          in big-endian byte order. For more information about using the CRC32c checksum, see
          Data validation.

          writable
        


customerEncryption
object
Metadata of customer-supplied encryption key, if the object is encrypted by such a
          key.



customerEncryption.encryptionAlgorithm
string
The encryption algorithm.



customerEncryption.keySha256
string
SHA256 hash value of the encryption key; encoded using base64.



customTime
datetime1
A user-specified timestamp for the object in
          RFC 3339 format. Once
          set on an object, customTime cannot be removed and cannot be set to an
          earlier datetime. For more information, see
          custom time metadata.

          writable
        


etag
string
HTTP 1.1 Entity
          tag for the object.



eventBasedHold
boolean
Whether or not the object is subject to an
          event-based hold.

          writable
        


generation
long1
The content generation of this object. Used for
          object versioning and
          soft delete.



id
string
The ID of the object, including the bucket name, object name, and generation number.



kind
string
The kind of item this is. For objects, this is always "storage#object".



kmsKeyName
string
Cloud KMS key used to
          encrypt this object, if the object is encrypted by such a key.



md5Hash
string
MD5 hash of the data, encoded using
          base64. This
          field is not present for composite objects.
          For more information about using the MD5 hash, see
          Data validation.

          writable
        


mediaLink
string
A URL for downloading the object's data. You should generally use one of the other
        JSON API endpoints instead.



metadata
object
User-provided metadata, in key/value pairs.

          writable
        


metadata.(key)
string
An individual metadata entry.

          writable
        


metageneration
long1
The version of the metadata for this object at this generation. Used for preconditions
          and for detecting changes in metadata. A metageneration number is only meaningful in the
          context of a particular generation of a particular object.



name
string
The name of the object. Required if not specified by URL parameter.

          writable
        


owner
object
The owner of the object. This is always the uploader of the object. Only requests
          that use the "projection=full" query parameter return this field in the
          response.
If iamConfiguration.uniformBucketLevelAccess.enabled is set to
            true, this field does not apply.



owner.entity
string
The entity, in the form "user-emailAddress".



owner.entityId
string
The ID for the entity.



restoreToken
string
Applicable in buckets with hierarchical namespace
          enabled. The restoreToken is a universally unique identifier (UUID)
          associated with each soft-deleted object and can
          be used in requests to restore a soft-deleted object or retrieve its metadata.
          The restoreToken is only required when the name and
          generation values of an object
          do not uniquely
          identify it. Otherwise, including a restoreToken is optional.



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
        


retentionExpirationTime
datetime1
The earliest time that the object can be deleted, which depends on any
          retention configuration set for the object and
          any retention policy set for
          the bucket that contains the object. The value for retentionExpirationTime
          is given in RFC
          3339 format.



selfLink
string
A URL for this object. You should generally use one of the other
        JSON API endpoints instead.



size
unsigned long1
Content-Length
          of the data in bytes.



softDeleteTime
datetime
The time at which the object was soft deleted.
        Only available for objects in buckets with a soft delete policy.



hardDeleteTime
datetime
The time at which a soft-deleted object will be permanently deleted and can no longer
        be restored. The value is the sum of the softDeleteTime value and the
        softDeletePolicy.retentionDurationSeconds value of the bucket. Only available
        for objects in buckets with a soft delete policy. Note that the hardDeleteTime
        value is permanent once set and does not change in response to
        softDeletePolicy.retentionDurationSeconds changes.



storageClass
string
Storage class of the object. To change an
        object's storage class, use objects rewrite.

          writable
        


temporaryHold
boolean
Whether or not the object is subject to a
          temporary hold.

          writable
        


timeCreated
datetime1
The creation time of the object in
          RFC 3339 format.



timeFinalized
datetime1
The finalization time of the object in
          RFC 3339 format.



timeDeleted
datetime1
The deletion time of the object in
          RFC 3339 format.
          Returned if and only if this version of the object is no longer a live version, but
          remains in the bucket as a
          noncurrent version.



timeStorageClassUpdated
datetime1
The time at which the object's storage class was last changed. When the object is
          initially created, it will be set to timeCreated.



updated
datetime1
The modification time of the
          object metadata in
          RFC 3339
          format. Set initially to object creation time and then updated whenever any metadata of
          the object changes. This includes changes made by a requester, such as modifying custom
          metadata, as well as changes made by Cloud Storage on behalf of a requester, such
          as changing the storage class based on an Object Lifecycle Configuration.





1 This property is a string formatted as the specified value type.
  


Methods
Available methods for Objects resources are as follows:

bulkRestore
Asynchronously restores the soft-deleted objects in a bucket.
compose
Concatenates a list of existing objects into a new object in the same bucket.
copy
Copies a source object to a destination object. Optionally overrides metadata.
delete
Deletes an object and its metadata. Deletions are permanent if versioning is not enabled
      for the bucket, or if the generation parameter is used.
get
Retrieves an object or its metadata.
insert
Stores a new object and metadata. For more information about writing data to Cloud Storage,
      see Uploads and downloads.
list
Retrieves a list of objects matching the criteria.
move
Moves an object within a bucket with hierarchical namespace enabled.
patch
Updates a data blob's associated metadata. This method supports
      patch semantics.
restore
Restores a soft-deleted object.
rewrite
Rewrites a source object to a destination object. Optionally overrides metadata.
update
Updates an object's metadata.
watchAll
Watch for changes on all objects in a bucket.

For information about status and error codes returned by these APIs, see the
  reference page.








  
    
    Send feedback
  
  



