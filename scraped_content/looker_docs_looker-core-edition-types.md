# https://cloud.google.com/looker/docs/looker-core-edition-types

Depth: 3

The following table details the features and entitlements that are available for each Looker (Google Cloud core) edition. The features and entitlements apply to both production and [non-production instances](/looker/docs/looker-core-overview#staging_environments_and_testing).

**Feature** | **Edition**  
---|---  
| **Standard** | **Enterprise** | **Embed**  
Production resource | 1 | 1 | 1  
Standard users | 10 | 10 | 10  
Developer users | 2 | 2 | 2  
Maximum number of users (including basic entitlements listed previously) | 50 | No maximum | No maximum  
Free upgrades to releases | Yes | Yes | Yes  
API calls per month [(query-based)](/looker/docs/looker-core-overview#types_of_looker_api_calls) | 1,000 | 100,000 | 500,000  
[Administrative API calls](/looker/docs/looker-core-overview#types_of_looker_api_calls) (per month) | 1,000 | 10,000 | 100,000  
VPC-SC support | No | Yes1 | Yes1  
Private IP available | No | Yes | Yes  
Customer-managed encryption keys | No | Yes | Yes  
Elite System Activity logs | No | Yes | Yes  
Custom themes | No | Yes | Yes  
Signed embedding | No | No | Yes  
Private labeling | No | Yes | Yes  
  
1 Must have Private IP usage configured to deploy VPC-SC.

**End user entitlements**  
---  
**Access to:** | **Developer user** | **Standard user** | **Viewer user**  
Administration interface for the instance within the Looker resource | Yes2 | No | No  
Administrative access for the instance within the Looker resource | Yes2 | No | No  
Full (read and write) access to LookML model | Yes | No | No  
View access to LookML models | Yes | Yes | Yes  
Development Mode | Yes | No | No  
Folders | Yes | Yes | Yes  
Dashboards | Yes | Yes | Yes  
Individual reports and charts | Yes | Yes | Yes  
Explores | Yes | Yes | No  
SQL Runner | Yes | Yes | No  
Scheduling | Yes | Yes | Yes  
Data filtering | Yes | Yes | Yes  
Drill to row-level detail | Yes | Yes | Yes  
Data downloading and exporting capability | Yes | Yes | Yes  
Dashboard or Look creation | Yes | Yes | No  
Looker API interfaces | Yes | No | No  
  
2 Each developer user must be authorized by the customer for administrative access via the admin interface of the Looker (Google Cloud core) instance.