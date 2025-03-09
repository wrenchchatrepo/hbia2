# BigQuery API: JobCreationReason






    
        Home
      
  




    
        BigQuery
      
  




    
        Documentation
      
  




    
        Reference
      
  







  
    
    Send feedback
  
  


      JobCreationReason
      
    



      
      Stay organized with collections
    

      
      Save and categorize content based on your preferences.
    









JSON representation
Code


Reason about why a Job was created from a jobs.query method when used with JOB_CREATION_OPTIONAL Job creation mode.For jobs.insert method calls it will always be REQUESTED.Preview





JSON representation




{
  "code": enum (Code)
}












Fields




code

enum (Code)
Output only. Specifies the high level reason why a Job was created.






Code

Indicates the high level reason why a job was created.









Enums




CODE_UNSPECIFIED
Reason is not specified.


REQUESTED
Job creation was requested.


LONG_RUNNING
The query request ran beyond a system defined timeout specified by the timeoutMs field in the QueryRequest. As a result it was considered a long running operation for which a job was created.


LARGE_RESULTS
The results from the query cannot fit in the response.


OTHER
BigQuery has determined that the query needs to be executed as a Job.












  
    
    Send feedback
  
  



