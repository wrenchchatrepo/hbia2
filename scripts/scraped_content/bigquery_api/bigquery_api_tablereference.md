# BigQuery API: TableReference






    
        Home
      
  




    
        BigQuery
      
  




    
        Documentation
      
  




    
        Reference
      
  







  
    
    Send feedback
  
  


      TableReference
      
    



      
      Stay organized with collections
    

      
      Save and categorize content based on your preferences.
    









JSON representation







JSON representation




{
  "projectId": string,
  "datasetId": string,
  "tableId": string
}












Fields




projectId

string
Required. The ID of the project containing this table.



datasetId

string
Required. The ID of the dataset containing this table.



tableId

string
Required. The ID of the table. The ID can contain Unicode characters in category L (letter), M (mark), N (number), Pc (connector, including underscore), Pd (dash), and Zs (space). For more information, see General Category. The maximum length is 1,024 characters. Certain operations allow suffixing of the table ID with a partition decorator, such as sample_table$20190123.












  
    
    Send feedback
  
  



