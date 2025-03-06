# https://cloud.google.com/looker/docs/choosing-hosting-option

Depth: 3

You have the option to host your own Looker (original) instance or deployment, or Looker can host it for you. Throughout our documentation, we refer to instances or deployments that are hosted by Looker as "[Looker-hosted](/looker/docs/glossary#looker-hosted)" and to instances or deployments that are hosted on-premises as "[customer-hosted](/looker/docs/glossary#customer-hosted)" or "self-hosted."

When Looker hosts your deployment, Looker manages all necessary IT functions that are related to the Looker application on your behalf, based on resource utilization and business requirements, greatly reducing the effort required to install, configure, and maintain the Looker application. Conversely, when you host your own deployment, you are responsible for managing many of these processes and functions. A customer-hosted deployment includes the in-product services, meaning the services that are hosted by Looker and accessible through the product, specifically licensing data, configuration backups, system error reports, data actions, and support tickets, as further described in the **Application Data Shared by Looker** section of [Looker's security page.](https://looker.com/product/security)

**Note:** A customer-hosted option is offered only for Looker (original) instances. This option is not available for Looker (Google Cloud core) instances.

Choosing between the two hosting options is a trade-off between convenience and control. Opting for Looker-hosted lets you focus on integrating Looker into your business workloads without the demands of infrastructure administration. Conversely, hosting your own Looker deployment gives you complete control over the infrastructure administration, but increases your overhead for the initial launch and ongoing maintenance.

This page presents the following information to assist you in choosing the most appropriate hosting option for your needs:

  * Comparative advantages of each hosting option
  * Benefits and limits of the Looker-hosted option
  * Benefits and limits of the customer-hosted option
  * Sample use cases for customer-hosted deployments

## Comparative advantages of each hosting option

The following table compares the advantages of each hosting option.

**Benefit** |  **Looker-hosted** |  **Customer-hosted**  
---|---|---  
Default access to all Looker features |  **X** |   
No hardware setup or maintenance required |  **X** |   
Automatic software updates and maintenance (monthly or quarterly) |  **X** |   
Scale hardware at no additional cost:

  * Vertical scaling (more CPU)
  * Horizontal scaling (more nodes)

|  **X** |   
Application and host monitoring |  **X** |   
Automatic Looker instance backups |  **X** |   
Backend database migration, if necessary |  **X** |   
Uptime SLA 99.9% (Advanced & Elite) |  **X** |   
S1 Response SLA 1 hour |  **X** |   
Use of the Looker API |  **X** |  **X**  
Multi-instance migrations |  **X** |  **X**  
Direct access to and export of servers and logs |  |  **X**  
  
## Benefits and limits of the Looker-hosted option

The following tables list the benefits and limits of using a Looker-hosted deployment.

### Benefits of Looker-hosted deployments

The following table lists the benefits of using a Looker-hosted deployment.

Active management of Looker instance  |  Leave the performance monitoring to the Looker team and focus on making decisions with actionable data insights from Looker.  
---|---  
Always get the latest features and updates |  You will never have to manually download another update. Your Looker instance is tested, updated, and optimized by Looker.  
Consistent performance |  Looker monitors performance and adjusts capacity as needed. You don't have to decide how many servers you need to support your users.   
Deployment security |  Looker manages your platform infrastructure. Your Looker deployment is discrete, secure, and monitored continuously to keep your data safe.  
Connected services |  Every Looker deployment includes essential connected services that allow you to access more relevant data, increase insights, simplify and scale data modeling, and integrate with third-party systems, all while Looker provides support.  
Secure database connections |  Connect Looker to your database using SSH.  
SAML/LDAP integration |  Looker can integrate with your existing authentication methods.  
  
### Limits of Looker-hosted deployments

Before you opt to use a Looker-hosted deployment, consider the limits that are listed in the following table.

Specific security/compliance requirements |  The Looker-hosted environment infrastructure may not align with your company's individual security/compliance requirements.   
---|---  
Requirement to have ability to export logs/monitoring information |  Because Looker manages the infrastructure for your instance, you cannot export logs for your instance's usage. Looker manages all monitoring. **Note:** Although logs from Looker-hosted instances cannot be exported, you can access the same information in a System Activity report.   
Custom SLAs |  Looker updates and maintenance take place during the pre-defined [maintenance windows](/looker/docs/google-maintenance-policy-for-looker-hosted-services). Some customers may require additional control over when this maintenance occurs.  
Custom JDBC Drivers |  Custom [JDBC drivers](/looker/docs/unpackaged-jdbc-drivers) must be installed to connect to databases that have [lower levels of support](/looker/docs/dialects).  
  
## Benefits and limits of the customer-hosted option

The following tables list the benefits and limits to using a customer-hosted deployment.

### Benefits of customer-hosted deployments

The following table lists the benefits of using a customer-hosted deployment.

Direct control over infrastructure and scaling decisions |  You are able to implement infrastructure and architecture configurations that may not be offered with a Looker-hosted deployment.  
---|---  
Access to logging/monitoring |  By managing your own infrastructure, you can directly access and export Looker application logs and set up instance monitoring that suits your individual requirements.   
Bespoke security model |  Hosting Looker in your own deployment allows you complete control over the security of the application environment, which you can align to your company/industry specific security standards.   
  
### Limits of customer-hosted deployments

Before you opt to use a customer-hosted deployment, consider the limits that are listed in the following table.

Support limitations |  Troubleshooting issues can be challenging when the Looker support team is unfamiliar with custom deployment architecture. Certain issues may require more involvement from your organization.  
---|---  
Monthly update requirements |  You are responsible for creating and maintaining processes that ensure that users are getting the latest features and security patches from Looker.  
Human capital requirements |  Looker deployments can require significant headcount and site reliability engineering expertise. Your organization must [manage the various components](/looker/docs/best-practices/customer-hosted-component-walkthroughs) of a Looker deployment.  
Cost |  Your organization must manage time, human capital, and cloud/datacenter costs.  
Challenges using connected services |  Looker has the benefit of connected services, which allow you to to access relevant industry data, increase insights, simplify and scale data modeling, and integrate with third-party systems. In a self-hosted Looker deployment, you may need to deploy ancillary services in your cloud to access these features.  
Disaster recovery and elasticity |  You will be responsible for maintaining uptime and service resilience.  
Some Looker features are not available |  The following Looker features are not available for customer-hosted deployments:

  * Looker (Google Cloud core) instances and any [features that appear only in Looker (Google Cloud core)](/looker/docs/looker-core-feature-differences#core_original_features)
  * [BI Connectors](/looker/docs/bi-connectors)
    * [Looker Studio](/looker/docs/admin-panel-platform-lsp). Likewise, the complimentary licenses to use Looker Studio Pro are not available.
    * [Connected Sheets for Looker](/looker/docs/connected-sheets)
    * [Looker — Power BI Connector](/looker/docs/powerbi-connector)
  * [Studio in Looker](/looker/docs/enabling-studio-in-looker)
  * [Export](/looker/docs/admin-panel-export) — this feature is required to migrate from Looker (original) to Looker (Google Cloud core)
  * [IP Allowlist](/looker/docs/admin-panel-server-ip-allowlist)
  * Looker's built-in [Slack integration](/looker/docs/scheduling-slack)
  * [Importing Looker visualizations into Google Slides](/looker/docs/import-vis-into-google-slides)

  
Additional feature configuration |  Customer-hosted instances may require [additional configuration](/looker/docs/customer-hosted-installation-steps) to use certain Looker features.  
  
## Sample use cases for customer-hosted deployments

A customer-hosted option may be right for your deployment if it aligns with any of the following use cases:

  * Your organization has bespoke security requirements: Some organizations' security policies mandate that they cannot use cloud services. Looker (original) is designed to be multi-cloud, and Looker-hosted Looker (original) deployments reside on various Cloud providers such as Google Cloud, AWS, and Azure. If your security policy is incompatible with using Cloud services with your data, customer-hosting is designed to be the alternative.
  * Your organization prefers a fully customizable deployment model: When Looker hosts your environments, Looker assumes that these environments are intended to be stable. Your organization's requirements may not be compatible with this assumption, such as in the following situations: 
    * Your deployment landscape is a large expanse of numerous instances for each of your user groups or customers, which may only be required for an ephemeral period.
    * Your organization requires the ability to frequently build new environments or tear down existing environments.
    * Your organization requires multiple Looker instances, each requiring custom configurations for the startup flags, model, or connection information.
  * Your organization requires more direct access to integration and configuration capabilities: In a Looker-hosted environment, your direct access to your deployment is limited. Customer-hosted deployments allow for full access to the file system, metadata database, and JVM configurations of your instance. Direct access may be beneficial in the following situations: 
    * Your LookML models and configurations for each instance are frequently updated by using scripts that are synchronized with your development process.
    * Your organization is unable to use certain core technologies that Looker uses to deploy, such as Git. With full control of your instance's backend, you can substitute any core component of Looker with your preferred solution.