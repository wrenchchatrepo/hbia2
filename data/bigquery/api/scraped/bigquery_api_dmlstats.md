# BigQuery API: DmlStats






    
        Home
      
  




    
        BigQuery
      
  




    
        Documentation
      
  




    
        Reference
      
  







  
    
    Send feedback
  
  


      DmlStats
      
    



      
      Stay organized with collections
    

      
      Save and categorize content based on your preferences.
    









JSON representation


Detailed statistics for DML statements





JSON representation




{
  "insertedRowCount": string,
  "deletedRowCount": string,
  "updatedRowCount": string
}












Fields




insertedRowCount

string (Int64Value format)
Output only. Number of inserted Rows. Populated by DML INSERT and MERGE statements



deletedRowCount

string (Int64Value format)
Output only. Number of deleted Rows. populated by DML DELETE, MERGE and TRUNCATE statements.



updatedRowCount

string (Int64Value format)
Output only. Number of updated Rows. Populated by DML UPDATE and MERGE statements.












  
    
    Send feedback
  
  



