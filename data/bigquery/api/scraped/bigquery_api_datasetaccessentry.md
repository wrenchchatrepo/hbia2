# BigQuery API: DatasetAccessEntry






    
        Home
      
  




    
        BigQuery
      
  




    
        Documentation
      
  




    
        Reference
      
  







  
    
    Send feedback
  
  


      DatasetAccessEntry
      
    



      
      Stay organized with collections
    

      
      Save and categorize content based on your preferences.
    









JSON representation


Grants all resources of particular types in a particular dataset read access to the current dataset.Similar to how individually authorized views work, updates to any resource granted through its dataset (including creation of new resources) requires read permission to referenced resources, plus write permission to the authorizing dataset.





JSON representation




{
  "dataset": {
    object (DatasetReference)
  },
  "targetTypes": [
    enum (TargetType)
  ]
}












Fields




dataset

object (DatasetReference)
The dataset this entry applies to



targetTypes[]

enum (TargetType)
Which resources in the dataset this entry applies to. Currently, only views are supported, but additional target types may be added in the future.












  
    
    Send feedback
  
  



