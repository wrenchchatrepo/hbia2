# https://cloud.google.com/looker/docs/looker-core-custom-domain-private-ip-overview

Depth: 3

When using a private IP only Looker (Google Cloud core) instance, you must set up a custom domain to access the instance. Additionally, you must configure your network to provide access to the private IP custom domain. The type of configuration depends on the origins of the instance's traffic as well as other organizational constraints, such as the need for a user-managed certificate.

To understand what type of network configuration a private IP only Looker (Google Cloud core) instance requires, refer to the following table:

**Requirements** | **Topology** | **Documentation**  
---|---|---  
Traffic comes from the same region as the Looker (Google Cloud core) instance or through hybrid networking.  | Cloud Interconnect, Cloud DNS, and Private Services Access  | [Custom domain for a private IP Looker (Google Cloud core) instance: Traffic originating from the same region](/looker/docs/looker-core-custom-domain-private-ip-same-region)  
Traffic comes from a different region than the Looker (Google Cloud core) instance or through hybrid networking.  | Cloud Interconnect, Cloud DNS, TCP load balancer, Private Services Access  | [Custom domain for a private IP Looker (Google Cloud core) instance: Traffic originating from different regions](/looker/docs/looker-core-custom-domain-private-ip)  
Organization requires a user-managed certificate.  | Cloud Interconnect, Cloud DNS, TCP load balancer, Private Services Access  | [Custom domain for a private IP Looker (Google Cloud core) instance: Traffic originating from different regions](/looker/docs/looker-core-custom-domain-private-ip)