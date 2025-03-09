# Google Cloud Storage API: testIamPermissions






    
        Home
      
  




    
        Cloud Storage
      
  




    
        Documentation
      
  




    
        Reference
      
  







  
    
    Send feedback
  
  


      ManagedFolder: testIamPermissions
      
    



      
      Stay organized with collections
    

      
      Save and categorize content based on your preferences.
    








Tests a set of permissions on the given
managed folder to see which, if any, are held by the
caller.

Required permissions
Permissions are not required for using this method.


Request
HTTP request
GET https://storage.googleapis.com/storage/v1/b/bucket/managedFolders/managedFolder/iam/testPermissions
In addition to standard query parameters,
  the following parameters apply to this method.
To see an example of how to include query parameters in a request, see the
  JSON API Overview page.
Parameters



Parameter name
Value
Description




Path parameters


bucket
string

          The parent bucket of the managed folder.
        


managedFolder
string

          The name of the managed folder, expressed as a path. For example,
        example-dir. If the managed folder is nested (for example,
        example-dir1/example-dir2), the / character in the managed folder
        path must be escaped. For example, example-dir1%2Fexample-dir2.
        


Required query parameters


permissions
string

          Permissions to test.
        



Request body
Do not supply a request body with this method.


Response
If successful, this method returns a response body with the following structure:

{
  "kind": "storage#testIamPermissionsResponse",
  "permissions": [
    string
  ]
}



Property name
Value
Description
Notes




kind
string
The kind of item this is.




permissions[]
list
The permissions held by the caller. Permissions are always of the format
          "storage.resource.capability", where
          resource is one of buckets, objects, or
          managedfolders.
          See Cloud Storage IAM
          Permissions for a list of supported permissions.





For information about status and error codes returned by this API, see the
    reference page.









  
    
    Send feedback
  
  



