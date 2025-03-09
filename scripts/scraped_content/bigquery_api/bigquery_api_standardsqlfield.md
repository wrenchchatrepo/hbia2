# BigQuery API: StandardSqlField






    
        Home
      
  




    
        BigQuery
      
  




    
        Documentation
      
  




    
        Reference
      
  







  
    
    Send feedback
  
  


      StandardSqlField
      
    



      
      Stay organized with collections
    

      
      Save and categorize content based on your preferences.
    









JSON representation


A field or a column.





JSON representation




{
  "name": string,
  "type": {
    object (StandardSqlDataType)
  }
}












Fields




name

string
Optional. The name of this field. Can be absent for struct fields.



type

object (StandardSqlDataType)
Optional. The type of this parameter. Absent if not explicitly specified (e.g., CREATE FUNCTION statement can omit the return type; in this case the output parameter does not have this "type" field).












  
    
    Send feedback
  
  



