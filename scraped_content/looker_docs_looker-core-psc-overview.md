# https://cloud.google.com/looker/docs/looker-core-psc-overview

Depth: 3

You can use [Private Service Connect](/vpc/docs/private-service-connect) to access a private IP Looker (Google Cloud core) instance or connect a private IP Looker (Google Cloud core) instance to other internal or external services. In order to use Private Service Connect, your Looker (Google Cloud core) instance must meet the following criteria:

  * [Instance editions](/looker/docs/looker-core-overview#looker_\(google_cloud_core\)_editions) must be Enterprise (`core-enterprise-annual`) or Embed (`core-embed-annual`).
  * Instance network configuration must use private IP only.
  * [Private Service Connect](/looker/docs/looker-core-create-psc) must be enabled upon instance creation.

Private Service Connect allows northbound access to Looker (Google Cloud core) using endpoints or backends. Network endpoint groups (NEGs), once exposed as Private Service Connect service producers, enable Looker (Google Cloud core) to access southbound on-premises resources, multi-cloud environments, VPC workloads, or internet services.

To learn more about Private Service Connect, watch the [What is Private Service Connect?](https://www.youtube.com/watch?v=JAFagcQBV08) and [Private Service Connect and Service Directory: A revolution to connect your application in Cloud](https://www.youtube.com/watch?v=TYumathiFRI) videos.

## Service attachment

When you [create a Looker (Google Cloud core) instance](/looker/docs/looker-core-create-psc) that is enabled to use Private Service Connect, Looker (Google Cloud core) creates a service attachment for the instance automatically. A [_service attachment_](/vpc/docs/about-vpc-hosted-services#service-attachments) is an attachment point that VPC networks use to access the instance. The service attachment has a URI, which is used for making connections. You can find that URI on the [**Details** tab](/looker/docs/looker-core-view-console#details_tab) of the instance configuration page of the Google Cloud console.

You next create a Private Service Connect endpoint or backend that another VPC network uses to connect to the service attachment. This enables the network to access the Looker (Google Cloud core) instance.

## Northbound access to Looker (Google Cloud core) using Private Service Connect

[_Northbound_](/looker/docs/glossary#northbound-traffic) access concerns configuring routing from clients to Looker (Google Cloud core). Looker (Google Cloud core) deployed with Private Service Connect supports [endpoint](/vpc/docs/private-service-connect#endpoints) and [backend](/vpc/docs/private-service-connect#backends) connections for northbound access.

![Private Service Connect lets you send traffic to endpoints and backends that forward the traffic to Looker \(Google Cloud core\).](/static/looker/docs/images/psc-endpoint-backend.png)

Looker (Google Cloud core) Private Service Connect instances can be accessed by service consumers through an external regional application load balancer or privately through a Private Service Connect endpoint or backend. However, Looker (Google Cloud core) supports a single custom domain, so northbound access to a Looker (Google Cloud core) instance must be either public or private, not both public and private.

### Endpoints

Endpoints are deployed by using forwarding rules that provide the service consumer an IP address that is mapped to the Private Service Connect service, which offers passthrough network performance and a streamlined setup.

Private Service Connect endpoints can connect to published services in a separate VPC network or organization.

### Backends

Backends are deployed by using [network endpoint groups (NEGs)](/load-balancing/docs/negs), which let consumers direct public and private traffic to their load balancer before the traffic reaches a Private Service Connect service, and also offer certificate termination. With a load balancer, backends provide the following options:

  * Observability (every connection is logged)
  * [Cloud Armor integration](/armor/docs/cloud-armor-overview)
  * URL private labeling and client-side certificates
  * Request decoration (adding custom request headers)

**Note:** For information about setting up northbound access using hybrid networking, see the [Northbound access to a Looker (Google Cloud core) instance using Private Service Connect](/looker/docs/looker-core-psc-access) documentation page.

## Access southbound Looker (Google Cloud core) services using Private Service Connect

Looker (Google Cloud core) acts as a service consumer when establishing communication to other services in your VPC, multi-cloud network, or the internet. Connecting to these services from Looker (Google Cloud core) is considered [_southbound traffic_](/looker/docs/glossary#southbound-traffic).

To connect to these services, perform the following steps:

  1. Ensure that the service [is published](/vpc/docs/about-vpc-hosted-services). Some Google Cloud services may take care of this for you; for example, Cloud SQL offers a way to [create an instance with Private Service Connect enabled](/sql/docs/mysql/configure-private-service-connect). Otherwise, follow [the instructions for publishing a service by using Private Service Connect](/vpc/docs/configure-private-service-connect-producer) and refer to the additional guidance in the [Looker (Google Cloud core) instructions](/looker/docs/looker-core-psc#set_up_psc_for_external_services).
  2. Specify the [southbound (egress) connection](/looker/docs/looker-core-create-psc#specify_southbound_connections) from Looker (Google Cloud core) to the service.

You can use hybrid connectivity NEGs or internet NEGs when accessing services with Private Service Connect:

![Private Service Connect connects Looker \(Google Cloud core\) to services through load balancers and hybrid or internet NEGs.](/static/looker/docs/images/psc-service-consumer.png)

  * A [hybrid connectivity NEG](/load-balancing/docs/negs/hybrid-neg-concepts#regional-internal-https) provides access to private endpoints, such as on-premises or multi-cloud endpoints. A hybrid connectivity NEG is a combination of an IP address and port configured as a backend to a load balancer. It is deployed within the same VPC as the Cloud Router. This deployment enables services in your VPC to reach routable endpoints through hybrid connectivity, such as Cloud VPN or Cloud Interconnect.

  * An [internet NEG](/load-balancing/docs/negs/internet-neg-concepts) provides access to public endpoints, for example, a GitHub endpoint. An internet NEG specifies an external backend for the load balancer. This external backend referenced by the internet NEG is accessible through the internet.

You can establish a southbound connection from Looker (Google Cloud core) to service producers in any region. For example, if you have Cloud SQL Private Service Connect instances in regions `us-west1` and `us-east4`, you can create a southbound connection from a Looker (Google Cloud core) Private Service Connect instance deployed in `us-central1`.

![](/static/looker/docs/images/psc-southbound-multi-region.png)

The two regional service attachments with unique domain names would be specified as follows. The `--region` flags refer to the region of the Looker (Google Cloud core) Private Service Connect instance, while the regions of the Cloud SQL instances are included in their service attachment URIs:
    
    
    gcloud looker instances update looker-psc-instance \
    --psc-service-attachment domain=sql.database1.com,attachment=projects/123/regions/us-west1/serviceAttachments/sql-database1-svc-attachment --region=us-central1 \
    --psc-service-attachment domain=sql.database2.com,attachment=projects/123/regions/us-east4/serviceAttachment/sql-database2-svc-attachment --region=us-central1
    

Southbound access to non-Google managed services requires that you enable [global access](/vpc/docs/about-accessing-vpc-hosted-services-endpoints#global-access) on the producer load balancer to allow inter-region communication.

## What's next

  * [Create a Looker (Google Cloud core) Private Service Connect instance](/looker/docs/looker-core-create-psc)
  * [Access a Looker (Google Cloud core) instance using Private Service Connect](/looker/docs/looker-core-psc-access)