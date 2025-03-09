# Google Cloud Storage API: Overview






    
        Home
      
  




    
        Cloud Storage
      
  




    
        Documentation
      
  




    
        Reference
      
  







  
    
    Send feedback
  
  


      Projects.serviceAccount
      
    



      
      Stay organized with collections
    

      
      Save and categorize content based on your preferences.
    








The Projects.serviceAccount resource represents the
    Cloud Storage service agent of a
    project. The service agent is a special service account that allows Cloud Storage to
    perform actions on behalf of the user. A project can have multiple service accounts, but only
    one service agent that is specifically associated with Cloud Storage.
For a list of methods for this resource, see the end of this page.


Resource representations

{
  "email_address": string,
  "kind": "storage#serviceAccount"
}



Property name
Value
Description
Notes




email_address
string
The email address of a project's Cloud Storage service agent.




kind
string
The kind of item this is. For a Project.serviceAccounts resource, this is always
          "storage#serviceAccount".








Methods

get
Get a project's Cloud Storage service agent.

For information about status and error codes returned by these APIs, see the
  reference page.








  
    
    Send feedback
  
  



