# Google Cloud Storage API: bulkRestore






    
        Home
      
  




    
        Cloud Storage
      
  




    
        Documentation
      
  




    
        Reference
      
  







  
    
    Send feedback
  
  


      Objects: bulkRestore
      
    



      
      Stay organized with collections
    

      
      Save and categorize content based on your preferences.
    








Initiates a long-running operation to bulk restore multiple
soft-deleted objects in a bucket. Soft-deleted objects that
meet the criteria defined in the request body parameters are restored to the bucket.
When a soft-deleted object is restored, a new copy of that object is created in the same bucket
and inherits the same metadata as the soft-deleted object. The inherited metadata is the metadata
that existed when the original object became soft deleted, with the following exceptions:

The createTime of the new object is set to the time at which the soft-deleted
object was restored.
The softDeleteTime and hardDeleteTime values are cleared.
A new generation is assigned and the metageneration is reset to 1.
If the soft-deleted object was in a bucket that had Autoclass enabled, the new object is
restored to Standard storage.
The restored object inherits the bucket's default object ACL, unless copySourceAcl
is true.


If a live object using the same name already exists in the bucket and becomes overwritten,
the live object becomes a noncurrent object if
Object Versioning is enabled on the bucket. If
Object Versioning is not enabled, the live object becomes soft deleted.
The specified bucket must have a soft delete policy. Otherwise, the request fails with a
400 Bad Request error with the reason SoftDeletePolicyRequired.


Required permissions
The authenticated user must have the following IAM permissions to use this
method:

storage.buckets.restore
storage.objects.restore
storage.objects.create
storage.objects.setIamPolicy (only required if copySourceAcl is true
  and the relevant bucket has uniform
  bucket-level access disabled)



Request
HTTP request
POST https://storage.googleapis.com/storage/v1/b/bucket/o/bulkRestore
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

          Name of the bucket in which objects will be restored.
        



Request body
In the request body, supply a data structure with the following properties:



Property name
Value
Description
Notes




allowOverwrite
boolean
If false (default), the bulk restore operation will not overwrite
        live objects that have the same name as the soft-deleted objects to be restored. This means
        that some soft-deleted objects might not get restored.
If true, live objects
        that have the same name as the soft-deleted objects will be overwritten. If
        Object Versioning
        is enabled on the bucket, the live objects will become noncurrent when overwritten. If
        Object Versioning is not enabled, the live object will become soft-deleted when
        overwritten. Noncurrent objects that have the same name as the soft-deleted objects to be
        restored do not get overwritten.


          writable
        


matchGlob
string
Restores only the soft-deleted objects that match the specified glob. If this parameter
        is not specified, all soft-deleted objects that match the specified time range are
        restored. For more information about glob syntax, see the
        match glob documentation.

          writable
        


softDeletedAfterTime
string
Restores only the soft-deleted objects that were soft deleted after the specified
        time.

          writable
        


softDeletedBeforeTime
string
Restores only the soft-deleted objects that were soft deleted before the specified
        time.

          writable
        


copySourceAcl
boolean

          Applicable only for buckets that don't have
          uniform bucket-level access
          enabled. If true, copies the soft-deleted object's ACL and applies it to the
          restored object. If false or not specified, the restored object inherits
          the bucket's default object ACL.
        

          writable
        





Response
If successful, this method returns an instance of
    operation
    in the response body:
{
  "name": "string",
  "metadata": { object (BulkRestoreObjectsMetadata)},
  "done": "boolean",
  // Union field result can be only one of the following:
  "error": { object (Status)},
  "response": {}
  // End of list of possible types for union field result
}



Property name
Value
Description
Notes




name
string
The server-assigned name of the operation.




metadata
object
An object of type BulkRestoreObjectsMetadata:
{
  "allowOverwrite": boolean,
  "matchGlobs": "string",
  "deleteAfterTime": "datetime",
  "deleteBeforeTime": "datetime",
  "copySourceAcl": boolean,
  "succeededCount": "long",
  "skippedCount": "long",
  "failedCount": "long",
}
Where:
      
succeededCount is the number of successfully restored objects.
skippedCount is the number of objects skipped as a result of the specified
      deletedAfterTime, deletedBeforeTime, and matchGlobs
      parameters. If multiple generations of an object match the criteria, only the latest
      generation is restored and the rest are skipped.
failedCount is the number of objects that failed to be restored. Objects
      can fail to be restored if, for example, a live object with the same name cannot be rewritten.
      






done
boolean
If false, indicates that the operation is still in progress, and neither
        error nor response is set. If
        true, the operation is completed and either error or
        response is set.




error
object
Indicates that the operation is considered to be successful, unless it failed to
        start because of invalid parameters, or because of an access denied error. For information
        about status and error codes returned by this API, see the
        reference page.




response
object
Empty. Detailed error information can be obtained from
        Cloud Audit Logs.







Try it!
Use the APIs Explorer below to call this method on live data and see the response.









  
    
    Send feedback
  
  



