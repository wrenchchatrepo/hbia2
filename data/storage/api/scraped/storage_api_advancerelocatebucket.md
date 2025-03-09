# Google Cloud Storage API: advanceRelocateBucket






    
        Home
      
  




    
        Cloud Storage
      
  




    
        Documentation
      
  




    
        Reference
      
  







  
    
    Send feedback
  
  


      Operations: advanceRelocateBucket
      
    



      
      Stay organized with collections
    

      
      Save and categorize content based on your preferences.
    








Initiates the final synchronization of a bucket relocation operation that requires a write downtime. The server makes a best effort to
proceed with the operation, but success is not guaranteed.
Users can use
Operations: get to check the status of the operation.

Required permissions
You must have the storage.buckets.relocate IAM permission on the bucket to initiate the final synchronization step.
You might also need the following permissions on the bucket:

storage.bucketOperations.get You need this permission to view the status of the bucket relocation operation.
storage.bucketOperations.list You need this permission to view the list of bucket relocation operations.
storage.bucketOperations.cancel You need this permission to cancel the bucket relocation operation.
storage.bucket.getYou need this permission to view the metadata of a bucket during the final synchronization of the bucket relocation operation.
      
storage.objects.list and storage.objects.getYou need these permissions to view the list of objects in a bucket that you want to relocate to another location.
      



Request
HTTP request
POST https://storage.googleapis.com/storage/v1/b/bucket/operations/operationId/advanceRelocateBucket
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
        


operationId
string

The ID of the Buckets: relocate long-running operation that initiated the bucket relocation.
         For example, AbCJYd8jKT1n-Ciw1LCNXIcubwvij_TdqO-ZFjuF2YntK0r74




Request body
In the request body, supply any one of the following properties:



Property name
Value
Description
Notes




Optional parameters


ttl
string

        The Time to live (TTL) for the write downtime phase during a relocation process.
        It is expressed as a string, such as 12h for 12 hours. The ttl duration determines
        the maximum allowed duration for the write downtime phase. If the write downtime exceeds
        this limit, the relocation process automatically reverts to the incremental copy step,
        and write operations to the bucket are re-enabled. The value must be within the range of
        6h (6 hours) to 48h (48 hours). If not specified, the default value is 12h (12 hours).
      
Writable


expire_time
string

        If the final synchronization fails, the expire_time determines how long the process tries before
        switching back to the incremental copy step. The format of expire_time is a string in RFC 3339 format, such as 2024-08-15T01:30:15.01Z.
      
Writable





Response
If successful, this method returns an empty response body.
For information about status and error codes returned by this API, see the
    reference page.


Try it!

    Use the APIs Explorer below to call this method on live data and see the response.
  









  
    
    Send feedback
  
  



