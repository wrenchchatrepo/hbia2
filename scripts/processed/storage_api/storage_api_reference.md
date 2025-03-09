# Google Cloud Storage API Reference

## API Resources

## API Endpoints

### watchall

**Request Body:** In the request body, supply data with the following structure:

**Details:**

- **Required permissions:** The authenticated user must have the storage.buckets.update IAM
permission to use this method.

- **Request:** 

- **Parameters:** 

- **Response:** If successful, this method returns a response body with the following structure:

- **Try it!:** Use the APIs Explorer below to call this method on live data and see the response.

- **Why Google:** 

- **Products and pricing:** 

- **Solutions:** 

- **Resources:** 

- **Engage:** 

### cancel

**Request Body:** Do not supply a request body with this method.

**Details:**

- **Required permissions:** The authenticated user must have the following IAM permissions on the bucket to
use this method:

storage.bucketOperations.cancel


Request
HTTP request
POST https://storage.googleapis.com/storage/v1/b/bucket/operations/operationId/cancel
In addition to standard query parameters,
  the following query parameters apply to this method.
To see an example of how to include query parameters in a request, see the
  JSON API Overview page.
Parameters



Parameter name
Value
Description




Path parameters


bucket
string

          Name of a bucket.
        


operationId
string

          The ID of the operation.
        



Request body
Do not supply a request body with this method.


Response
If successful, this method returns an empty response body.
For information about status and error codes returned by this API, see the
    reference page.

- **Request:** 

- **Parameters:** 

- **Response:** If successful, this method returns an empty response body.

- **Why Google:** 

- **Products and pricing:** 

- **Solutions:** 

- **Resources:** 

- **Engage:** 

### setiampolicy

**Request Body:** In the request body, supply data with the following structure:

**Details:**

- **Required permissions:** The authenticated user must have the storage.managedfolders.setIamPolicy
IAM permission to use this method.

- **Request:** 

- **Parameters:** 

- **Response:** If successful, this method returns a response body with the following structure:

- **Why Google:** 

- **Products and pricing:** 

- **Solutions:** 

- **Resources:** 

- **Engage:** 

### rewrite

**Request Body:** In the request body, supply metadata to apply to the destination object by using an
    object resource. If the request body
    is empty, editable metadata from the source object
    is applied to the destination object, with the exception of any ACLs, object holds, or
    retention configuration set on the source object. If you want to retain these from
    the original object, they must be included in the request body.

**Details:**

- **Required permissions:** The authenticated user must have the following IAM permissions to use this method:

- **Request:** 

- **Parameters:** 

- **Response:** If successful, this method returns a response body with the following structure:

- **Try it!:** Use the APIs Explorer below to call this method on live data and see the response.

- **Why Google:** 

- **Products and pricing:** 

- **Solutions:** 

- **Resources:** 

- **Engage:** 

### listchannels

**Request Body:** Do not supply a request body with this method.

**Details:**

- **Required permissions:** The authenticated user must have the storage.buckets.get IAM
permission to use this method.

- **Request:** 

- **Parameters:** 

- **Response:** If successful, this method returns a response body with the following structure:

- **Why Google:** 

- **Products and pricing:** 

- **Solutions:** 

- **Resources:** 

- **Engage:** 

### delete

**Request Body:** Do not supply a request body with this method.

**Details:**

- **Required permissions:** In order to use this method, the authenticated user must have the
storage.hmacKeys.delete IAM permission for the project in which the
key exists.

- **Request:** 

- **Parameters:** 

- **Response:** If successful, this method returns an empty response body.

- **Try it!:** Use the APIs Explorer below to call this method on live data and see the response.

- **Why Google:** 

- **Products and pricing:** 

- **Solutions:** 

- **Resources:** 

- **Engage:** 

### stop

**Request Body:** In the request body, supply data with the following structure:

**Details:**

- **Request:** 

- **Response:** If successful, this method returns an empty response body.

- **Try it!:** Use the APIs Explorer below to call this method on live data and see the response.

- **Why Google:** 

- **Products and pricing:** 

- **Solutions:** 

- **Resources:** 

- **Engage:** 

### resource_representation

**Details:**

- **Resource representations:** 

- **Methods:** 

- **Why Google:** 

- **Products and pricing:** 

- **Solutions:** 

- **Resources:** 

- **Engage:** 

### object

**Details:**

- **Resource representations:** 

- **Methods:** Available methods for Objects resources are as follows:

- **Why Google:** 

- **Products and pricing:** 

- **Solutions:** 

- **Resources:** 

- **Engage:** 

### advancerelocatebucket

**Request Body:** In the request body, supply any one of the following properties:

**Details:**

- **Required permissions:** You must have the storage.buckets.relocate IAM permission on the bucket to initiate the final synchronization step.

- **Request:** 

- **Parameters:** 

- **Response:** If successful, this method returns an empty response body.

- **Try it!:** Use the APIs Explorer below to call this method on live data and see the response.

- **Why Google:** 

- **Products and pricing:** 

- **Solutions:** 

- **Resources:** 

- **Engage:** 

### relocate

**Request Body:** In the request body, supply the following properties:

**Details:**

- **Required permissions:** You must have the storage.buckets.relocate IAM permission on the bucket to initiate the dry run or the incremental data copy step.

- **Request:** 

- **Parameters:** 

- **Response:** Initiating a bucket relocation process starts a long-running operation.
    You'll receive an operation ID and a description of the operation. To track the completion of
    the bucket relocation operation, you'll need to track its progress.
    For information about how to track the progress
    of the bucket relocation operation, see Get details of a long-running operation.

- **Try it!:** Use the APIs Explorer below to call this method on live data and see the response.

- **Why Google:** 

- **Products and pricing:** 

- **Solutions:** 

- **Resources:** 

- **Engage:** 

### lockretentionpolicy

**Request Body:** Do not supply a request body with this method.

**Details:**

- **Required permissions:** The authenticated user must have the storage.buckets.update IAM
permission to use this method.

- **Request:** 

- **Parameters:** 

- **Response:** If successful, this method returns a bucket
      resource in the response body.

- **Try it!:** Use the APIs Explorer below to call this method on live data and see the response.

- **Why Google:** 

- **Products and pricing:** 

- **Solutions:** 

- **Resources:** 

- **Engage:** 

### patch

**Request Body:** In the request body, supply the relevant portions of an
    object resource, according to the rules
    of patch semantics.

**Details:**

- **Required permissions:** The authenticated user must have the storage.objects.update IAM
  permission to use this method. If the request body includes the retention property,
  the authenticated user must also have the storage.objects.setRetention
  IAM permission, and if the request includes the query parameter
  overrideUnlockedRetention, the authenticated user must also have the
  storage.objects.overrideUnlockedRetention IAM permission.

- **Request:** 

- **Parameters:** 

- **Response:** If successful, this method returns an
    object resource in the response body.

- **Try it!:** Use the APIs Explorer below to call this method on live data and see the response.

- **Why Google:** 

- **Products and pricing:** 

- **Solutions:** 

- **Resources:** 

- **Engage:** 

### getstoragelayout

**Request Body:** Do not supply a request body with this method.

**Details:**

- **Required permissions:** The authenticated user must have the storage.objects.list IAM
  permission to use this method.

- **Request:** 

- **Parameters:** 

- **Response:** If successful, this method returns a response body with the following structure:

- **Try it!:** Use the APIs Explorer below to call this method on live data and see the response.

- **Why Google:** 

- **Products and pricing:** 

- **Solutions:** 

- **Resources:** 

- **Engage:** 

### headers_and_query_parameters

**Details:**

- **HTTP headers and common query string parameters summary:** The JSON API uses the following standard HTTP headers:

- **Standard HTTP headers:** 

- **Extension (custom) HTTP headers:** 

- **Standard Query Parameters:** Query string parameters that can be used in any JSON API request are shown in
the table below. Note that not all parameters apply to all requests. For
example, use of the fields parameter has no effect on Delete requests, since
the response body is empty. See specific methods for additional query
string parameters.

- **What's next:** 

- **Why Google:** 

- **Products and pricing:** 

- **Solutions:** 

- **Resources:** 

- **Engage:** 

### insert

**HTTP Request:** `Note: The request endpoint for this method
    differs from typical Cloud Storage JSON API endpoints.`

**Request Body:** When performing a simple upload, provide the
    object data in the request body. When performing a
    multipart upload or when
    initiating a resumable upload, both of which allow
    you to include object metadata as part of the request, supply the following properties. If you
    do not wish to provide object metadata in a resumable upload, the request body can be empty.

**Details:**

- **Required permissions:** The authenticated user must have the storage.objects.create IAM
 permission to use this method. If the object being inserted has the same name as an existing
 object, the user must also have the storage.objects.delete permission to overwrite the
 existing object. If the request body includes the retention property, the
 authenticated user must also have the storage.objects.setRetention IAM
 permission.

- **Request:** 

- **Parameters:** 

- **Response:** If successful, this method returns an
    object resource in the response
    body.

- **Why Google:** 

- **Products and pricing:** 

- **Solutions:** 

- **Resources:** 

- **Engage:** 

### bulkrestore

**Request Body:** In the request body, supply a data structure with the following properties:

**Details:**

- **Required permissions:** The authenticated user must have the following IAM permissions to use this
method:

storage.buckets.restore
storage.objects.restore
storage.objects.create
storage.objects.setIamPolicy (only required if copySourceAcl is true
  and the relevant bucket has uniform
  bucket-level access disabled)

- **Request:** 

- **Parameters:** 

- **Response:** If successful, this method returns an instance of
    operation
    in the response body:

- **Try it!:** Use the APIs Explorer below to call this method on live data and see the response.

- **Why Google:** 

- **Products and pricing:** 

- **Solutions:** 

- **Resources:** 

- **Engage:** 

### compose

**Request Body:** In the request body, supply data with the following structure:

**Details:**

- **Required permissions:** The authenticated user must have the storage.objects.create and
 storage.objects.get IAM permissions to use this method. If the new
  composite object overwrites an existing object, the authenticated user must also have the
  storage.objects.delete permission. If the request body includes the
  retention property, the authenticated user must also have the
  storage.objects.setRetention IAM permission.

- **Request:** 

- **Parameters:** 

- **Response:** If successful, this method returns an object
    resource in the response body, with the owner and acl
    properties omitted.

- **Try it!:** Use the APIs Explorer below to call this method on live data and see the response.

- **Why Google:** 

- **Products and pricing:** 

- **Solutions:** 

- **Resources:** 

- **Engage:** 

### update

**Request Body:** In the request body, supply the metadata portion of a
    Projects.hmacKeys resource
    with the following properties:

**Details:**

- **Required permissions:** In order to use this method, the authenticated user must have the
storage.hmacKeys.update IAM permission for the project in which the
key exists.

- **Request:** 

- **Parameters:** 

- **Response:** If successful, this method returns the metadata portion of a
    Projects.hmacKeys resource
    in the response body.

- **Try it!:** Use the APIs Explorer below to call this method on live data and see the response.

- **Why Google:** 

- **Products and pricing:** 

- **Solutions:** 

- **Resources:** 

- **Engage:** 

### list

**Request Body:** Do not supply a request body with this method.

**Details:**

- **Required permissions:** In order to use this method, the authenticated user must have the
storage.hmacKeys.list IAM permission for the project in which the
keys exist.

- **Request:** 

- **Parameters:** 

- **Response:** If successful, this method returns a response body with the following structure:

- **Try it!:** Use the APIs Explorer below to call this method on live data and see the response.

- **Why Google:** 

- **Products and pricing:** 

- **Solutions:** 

- **Resources:** 

- **Engage:** 

### move

**Request Body:** Do not supply a request body with this method.

**Details:**

- **Required permissions:** The authenticated user must have the following IAM permissions to use this method:

- **Request:** 

- **Parameters:** 

- **Response:** If successful, this method returns the destination object's
    resource in the response
    body.

- **Try it!:** Use the APIs Explorer below to call this method on live data and see the response.

- **Why Google:** 

- **Products and pricing:** 

- **Solutions:** 

- **Resources:** 

- **Engage:** 

### getiampolicy

**Request Body:** Do not supply a request body with this method.

**Details:**

- **Required permissions:** The authenticated user must have the storage.managedfolders.getIamPolicy
IAM permission to use this method.

- **Request:** 

- **Parameters:** 

- **Response:** If successful, this method returns a response body with the following structure:

- **Why Google:** 

- **Products and pricing:** 

- **Solutions:** 

- **Resources:** 

- **Engage:** 

### testiampermissions

**Request Body:** Do not supply a request body with this method.

**Details:**

- **Required permissions:** Permissions are not required for using this method.

- **Request:** 

- **Parameters:** 

- **Response:** If successful, this method returns a response body with the following structure:

- **Why Google:** 

- **Products and pricing:** 

- **Solutions:** 

- **Resources:** 

- **Engage:** 

### create

**Request Body:** Do not supply a request body with this method.

**Details:**

- **Required permissions:** In order to use this method, the authenticated user must have the
storage.hmacKeys.create IAM permission on the project in which the key
will be created.

- **Request:** 

- **Parameters:** 

- **Response:** If successful, this method returns a
    Projects.hmacKeys resource
    in the response body.

- **Try it!:** Use the APIs Explorer below to call this method on live data and see the response.

- **Why Google:** 

- **Products and pricing:** 

- **Solutions:** 

- **Resources:** 

- **Engage:** 

### overview

**Details:**

- **Resource representations:** 

- **Methods:** 

- **Why Google:** 

- **Products and pricing:** 

- **Solutions:** 

- **Resources:** 

- **Engage:** 

### get

**Request Body:** Do not supply a request body with this method.

**Details:**

- **Required permissions:** In order to use this method, the authenticated user must have the
resourcemanager.projects.get IAM permission on the project.

- **Request:** 

- **Parameters:** 

- **Response:** If successful, this method returns a
    Projects.serviceAccount
    resource in the response body.

- **Try it!:** Use the APIs Explorer below to call this method on live data and see the response.

- **Why Google:** 

- **Products and pricing:** 

- **Solutions:** 

- **Resources:** 

- **Engage:** 

### restore

**Request Body:** Do not supply a request body with this method.

**Details:**

- **Required permissions:** The authenticated user must have the storage.buckets.restore IAM permission at the project level or above to use this method. To return access control lists (ACLs) as part of the response, the authenticated user must also have the storage.buckets.getIamPolicy permission.

- **Request:** 

- **Parameters:** 

- **Response:** If successful, this method returns a bucket
    resource in the response body.

- **Try it!:** Use the APIs Explorer below to call this method on live data and see the response.

- **Why Google:** 

- **Products and pricing:** 

- **Solutions:** 

- **Resources:** 

- **Engage:** 

### status_and_error_codes

**Details:**

- **Error Response Format:** Cloud Storage uses the standard HTTP error reporting format for the
JSON API. Successful requests return HTTP status codes in the 2xx range. Failed
requests return status codes in the 4xx and 5xx ranges. Requests that require a
redirect returns status codes in the 3xx range. Error responses usually include
a JSON document in the response body, which contains information about the
error.

- **401 Unauthorized:** The following is an example of an error response you receive if you try to
list the buckets for a project but do not provide an authorization header.

- **403 Forbidden:** This is an example of an error response you receive if you try to list the
buckets of a non-existent project or one in which you don't have permission
to list buckets.

- **404 Not Found:** The following is an example of an error response you receive if you try to
retrieve an object that does not exist.

- **409 Conflict:** The following is an example of an error response you receive if you try to
create a bucket using the name of a bucket you already own.

- **HTTP Status and Error Codes:** This section provides a non-exhaustive list of HTTP status and error codes that
the Cloud Storage JSON API uses. The 1xx Informational and 2xx
Success codes are not discussed here. For more information, see Response Status
Codes in RFC 7231 §6, RFC 7232 §4,
RFC 7233 §4, RFC 7235 §3, and RFC 6585.

- **302—Found:** 

- **303—See Other:** 

- **304—Not Modified:** 

- **307—Temporary Redirect:** 

- **308—Resume Incomplete:** 

- **400—Bad Request:** 

- **401—Unauthorized:** 

- **403—Forbidden:** 

- **404—Not Found:** 

- **405—Method Not Allowed:** 

- **408—Request Timeout:** 

- **409—Conflict:** 

- **410—Gone:** 

- **411—Length Required:** 

- **412—Precondition Failed:** 

- **413—Payload Too Large:** 

- **416—Requested Range Not Satisfiable:** 

- **429—Too Many Requests:** 

- **499—Client Closed Request:** 

- **500—Internal Server Error:** 

- **502—Bad Gateway:** This error is generated when there was difficulty reaching an internal service.
It is not formatted with a JSON document. You should retry the request
using truncated exponential backoff.

- **503—Service Unavailable:** 

- **504—Gateway Timeout:** This error is generated when there was difficulty reaching an internal service.
It is not formatted with a JSON document. You should retry the request
using truncated exponential backoff.

- **Why Google:** 

- **Products and pricing:** 

- **Solutions:** 

- **Resources:** 

- **Engage:** 

### rename

**Request Body:** Do not supply a request body with this method.

**Details:**

- **Required permissions:** The authenticated user must have the following IAM permissions to use this method:
  
storage.folders.rename

This permission is needed to rename the source folder.

storage.folders.create

This permission is needed to create the destination folder.

- **Request:** 

- **Parameters:** 

- **Response:** If successful, this method returns an instance of the
    long-running operation
    in the response body:

- **Try it!:** Use the APIs Explorer below to call this method on live data and see the response.

- **Why Google:** 

- **Products and pricing:** 

- **Solutions:** 

- **Resources:** 

- **Engage:** 

### bucket

**Details:**

- **Resource representations:** 

- **Methods:** Available methods for Buckets resources are as follows:

- **Try it for yourself:** If you're new to Google Cloud, create an account to evaluate how
        Cloud Storage performs in real-world
        scenarios. New customers also get $300 in free credits to run, test, and
        deploy workloads.

- **Why Google:** 

- **Products and pricing:** 

- **Solutions:** 

- **Resources:** 

- **Engage:** 

### copy

**Request Body:** In the request body, supply metadata to apply to the destination object by using an
    object resource. If the request body
    is empty, editable metadata from the source object
    is applied to the destination object, with the exception of any ACLs, object holds, or
    retention configuration set on the source object. If you want to retain these from
    the original object, they must be included in the request body.

**Details:**

- **Required permissions:** The authenticated user must have the following IAM permissions to use this method:

- **Request:** 

- **Parameters:** 

- **Response:** If successful, this method returns an
    object resource in the response
    body.

- **Try it!:** Use the APIs Explorer below to call this method on live data and see the response.

- **Why Google:** 

- **Products and pricing:** 

- **Solutions:** 

- **Resources:** 

- **Engage:** 

