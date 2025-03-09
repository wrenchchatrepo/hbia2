# Google Cloud Storage API: move






    
        Home
      
  




    
        Cloud Storage
      
  




    
        Documentation
      
  




    
        Reference
      
  







  
    
    Send feedback
  
  


      Objects: move
      
    



      
      Stay organized with collections
    

      
      Save and categorize content based on your preferences.
    








Moves an object within a bucket with hierarchical namespace enabled.
This operation moves a source object to a destination object in the same bucket by renaming the object.
  The move object operation is only supported for buckets with hierarchical namespace enabled. The
move itself is an atomic transaction, ensuring all steps either
complete successfully or no changes are made.
The move operation performs the following actions:

The source object is deleted as follows:

No early deletion fee is incurred.
Soft delete retention period is not applied.
Audit logs and notification messages are generated for the
    object.


The destination object is created with the same data and metadata as the
  source object except for the following changes:

A new object name
A new generation number
A new metageneration number, set to 1
New create and update timestamps


If a destination folder doesn't exist, the move operation creates the folder along with
    the destination object. The move operation also automatically creates any necessary parent folders.


Consider the following points when using the move method:

The source and destination must have different object names.
The source object must exist. You can only move existing objects.
If an object already exists at the destination, the move operation replaces the existing object.
  You can disable the replacement behavior using preconditions on the
    request.


Required permissions
The authenticated user must have the following IAM permissions to use this method:

Permissions required on the source object:

storage.objects.delete and storage.objects.get or
storage.objects.move (required only to move an object without
     allowing read or delete access)
Permissions required on the destination object:

storage.objects.create
storage.objects.delete (required only for replacing an object)
storage.folders.create (required only
      for automatically creating any missing parent folders)




Request
HTTP request
POST https://storage.googleapis.com/storage/v1/b/bucket/o/sourceObject/moveTo/o/destinationObject
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

          Name of the bucket containing the object you want to move.
        


sourceObject
string

          Name of the source object. For information about how to URL encode object names to be path
          safe, see Encoding URI path parts.
        


destinationObject
string

          Name of the new object. Required when the object metadata is not otherwise provided.
          Overrides the object metadata's name value, if any. For information about how
          to URL encode object names to be path safe, see
          Encoding URI path parts.
        


Optional query parameters


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
          succeed if there is a live version of the object. The ifGenerationMatch and
          ifGenerationNotMatch parameters are mutually exclusive.
          Specifying both parameters in a single request results in an error.
        


ifMetagenerationMatch
long

          Makes the operation conditional on there being a live destination object with a
          metageneration number that matches the given value.
        


ifMetagenerationNotMatch
long

          Makes the operation conditional on there being a live destination object with a
          metageneration number that does not match the given value. The ifMetagenerationMatch and
          ifMetagenerationNotMatch parameters are mutually exclusive.
          Specifying both parameters in a single request result in an error.
        


ifSourceGenerationMatch
long

          Makes the operation conditional on whether the source object's generation matches the
          given value.
        


ifSourceGenerationNotMatch
long

          Makes the operation conditional on whether the source object's generation does not match
          the given value. The ifSourceGenerationMatch and
          ifSourceGenerationNotMatch parameters are mutually exclusive.
          Specifying both parameters in a single request result in an error.
        


ifSourceMetagenerationMatch
long

          Makes the operation conditional on whether the source object's current metageneration
          matches the given value.
        


ifSourceMetagenerationNotMatch
long

          Makes the operation conditional on whether the source object's current metageneration
          does not match the given value. The ifSourceMetagenerationMatch and
          ifSourceMetagenerationNotMatch parameters are mutually exclusive.
          Specifying both parameters in a single request result in an error.
        



Request body
Do not supply a request body with this method.


Response
If successful, this method returns the destination object's
    resource in the response
    body.
For information about status and error codes returned by this API, see the
    reference page.


Try it!
Use the APIs Explorer below to call this method on live data and see the response.









  
    
    Send feedback
  
  



