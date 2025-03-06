# https://cloud.google.com/looker/docs/reference/rest

Depth: 3

* REST Resource: v1.projects.locations
  * REST Resource: v1.projects.locations.instances
  * REST Resource: v1.projects.locations.operations

## Service: looker.googleapis.com

To call this service, we recommend that you use the Google-provided [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery document:

  * <https://looker.googleapis.com/$discovery/rest?version=v1>

### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

  * `https://looker.googleapis.com`

## REST Resource: [v1.projects.locations](/looker/docs/reference/rest/v1/projects.locations)

Methods  
---  
`[get](/looker/docs/reference/rest/v1/projects.locations/get)` |  `GET /v1/{name=projects/*/locations/*}` Gets information about a location.  
`[list](/looker/docs/reference/rest/v1/projects.locations/list)` |  `GET /v1/{name=projects/*}/locations` Lists information about the supported locations for this service.  
  
## REST Resource: [v1.projects.locations.instances](/looker/docs/reference/rest/v1/projects.locations.instances)

Methods  
---  
`[create](/looker/docs/reference/rest/v1/projects.locations.instances/create)` |  `POST /v1/{parent=projects/*/locations/*}/instances` Creates a new Instance in a given project and location.  
`[delete](/looker/docs/reference/rest/v1/projects.locations.instances/delete)` |  `DELETE /v1/{name=projects/*/locations/*/instances/*}` Delete instance.  
`[export](/looker/docs/reference/rest/v1/projects.locations.instances/export)` |  `POST /v1/{name=projects/*/locations/*/instances/*}:export` Export instance.  
`[get](/looker/docs/reference/rest/v1/projects.locations.instances/get)` |  `GET /v1/{name=projects/*/locations/*/instances/*}` Gets details of a single Instance.  
`[import](/looker/docs/reference/rest/v1/projects.locations.instances/import)` |  `POST /v1/{name=projects/*/locations/*/instances/*}:import` Import instance.  
`[list](/looker/docs/reference/rest/v1/projects.locations.instances/list)` |  `GET /v1/{parent=projects/*/locations/*}/instances` Lists Instances in a given project and location.  
`[patch](/looker/docs/reference/rest/v1/projects.locations.instances/patch)` |  `PATCH /v1/{instance.name=projects/*/locations/*/instances/*}` Update Instance.  
`[restart](/looker/docs/reference/rest/v1/projects.locations.instances/restart)` |  `POST /v1/{name=projects/*/locations/*/instances/*}:restart` Restart instance.  
  
## REST Resource: [v1.projects.locations.operations](/looker/docs/reference/rest/v1/projects.locations.operations)

Methods  
---  
`[cancel](/looker/docs/reference/rest/v1/projects.locations.operations/cancel)` |  `POST /v1/{name=projects/*/locations/*/operations/*}:cancel` Starts asynchronous cancellation on a long-running operation.  
`[delete](/looker/docs/reference/rest/v1/projects.locations.operations/delete)` |  `DELETE /v1/{name=projects/*/locations/*/operations/*}` Deletes a long-running operation.  
`[get](/looker/docs/reference/rest/v1/projects.locations.operations/get)` |  `GET /v1/{name=projects/*/locations/*/operations/*}` Gets the latest state of a long-running operation.  
`[list](/looker/docs/reference/rest/v1/projects.locations.operations/list)` |  `GET /v1/{name=projects/*/locations/*}/operations` Lists operations that match the specified filter in the request.