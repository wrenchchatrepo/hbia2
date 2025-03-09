# Google Cloud Storage API: relocate






    
        Home
      
  




    
        Cloud Storage
      
  




    
        Documentation
      
  




    
        Reference
      
  







  
    
    Send feedback
  
  


      Buckets: relocate
      
    



      
      Stay organized with collections
    

      
      Save and categorize content based on your preferences.
    








Initiates the dry run or the incremental data copy step of a bucket relocation operation.
Users can use
Operations: get to check the status of the operation.

Required permissions
You must have the storage.buckets.relocate IAM permission on the bucket to initiate the dry run or the incremental data copy step.
You might also need the following permissions on the bucket:

storage.bucketOperations.get You need this permission to view the status of the bucket relocation operation.
storage.bucketOperations.list You need this permission to view the list of bucket relocation operations.
storage.bucketOperations.cancel You need this permission to cancel the bucket relocation operation.
storage.bucket.getYou need this permission to view the metadata of a bucket during the dry run and the incremental data copy of the bucket relocation operation.
    
storage.objects.list and storage.objects.getYou need these permissions to view the list of objects in a bucket that you want to relocate to another location.
    



Request
HTTP request
POST https://storage.googleapis.com/storage/v1/b/bucket/relocate
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

          Name of the bucket that you want to relocate.
        



Request body
In the request body, supply the following properties:



Property name
Value
Description
Notes




Required parameters


destinationLocation
string

        The destination location of the bucket.
      
Writable


Optional parameters


destinationCustomPlacementConfig
object

       The bucket's destination placement configuration if relocating to a configurable dual-region.
      
Writable


destinationCustomPlacementConfig.dataLocations
list of strings

        The list of configurable dual-region locations where you want to relocate the bucket.
      
Writable


validateOnly
boolean

        When set to true, the dry run of the bucket relocation operation starts.
      
Writable





Response
Initiating a bucket relocation process starts a long-running operation.
    You'll receive an operation ID and a description of the operation. To track the completion of
    the bucket relocation operation, you'll need to track its progress.
    For information about how to track the progress
    of the bucket relocation operation, see Get details of a long-running operation.
For information about status and error codes returned by this API, see the
    reference page.


Try it!

    Use the APIs Explorer below to call this method on live data and see the response.
  









  
    
    Send feedback
  
  



