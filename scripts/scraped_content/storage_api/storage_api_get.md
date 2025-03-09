# Google Cloud Storage API: get






    
        Home
      
  




    
        Cloud Storage
      
  




    
        Documentation
      
  




    
        Reference
      
  







  
    
    Send feedback
  
  


      Projects.serviceAccount: get
      
    



      
      Stay organized with collections
    

      
      Save and categorize content based on your preferences.
    








Get the email address of this project's
  Cloud Storage service account, also known
  as the service agent.

Required permissions
In order to use this method, the authenticated user must have the
resourcemanager.projects.get IAM permission on the project.


Request
HTTP request
GET https://storage.googleapis.com/storage/v1/projects/projectIdentifier/serviceAccount
In addition to standard query
  parameters, the following query parameters apply to this method.
To see an example of how to include query parameters in a request, see the
  JSON API Overview page.
Parameters



Parameter name
Value
Description




Path parameters


projectIdentifier
string

          Project ID or project number.
        



Request body
Do not supply a request body with this method.


Response
If successful, this method returns a
    Projects.serviceAccount
    resource in the response body.
For information about status and error codes returned by this API, see the
    reference page.


Try it!
Use the APIs Explorer below to call this method on live data and see the response.









  
    
    Send feedback
  
  



