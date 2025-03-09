# Google Cloud Storage API: Headers and query parameters






    
        Home
      
  




    
        Cloud Storage
      
  




    
        Documentation
      
  




    
        Reference
      
  







  
    
    Send feedback
  
  


      HTTP headers and common query string parameters for JSON
      
    



      
      Stay organized with collections
    

      
      Save and categorize content based on your preferences.
    





The Cloud Storage API uses standard HTTP headers as well as
several extension (custom) HTTP headers. This page describes:

All headers used by the JSON API
The query parameters that apply to any JSON API request

See specific methods for additional query string parameters not covered in
this page.
HTTP headers and common query string parameters summary
The JSON API uses the following standard HTTP headers:



Authorization
Cache-Control
Content-ID
Content-Length
Content-Range


Content-Type
Content-Transfer-Encoding
Date
ETag
Expires


If-Match
If-None-Match
Location
Range
Transfer-Encoding



The JSON API uses the following extension (custom) HTTP headers:



X-Goog-Allowed-Resources
X-Goog-Content-Length-Range
X-Goog-Custom-Audit-KEY
X-Goog-Encryption-Algorithm
X-Goog-Encryption-Key
X-Goog-Encryption-Key-Sha256


X-Goog-Copy-Source-Encryption-Algorithm
X-Goog-Copy-Source-Encryption-Key
X-Goog-Copy-Source-Encryption-Key-Sha256
X-Goog-Meta-KEY
X-Goog-Stored-Content-Encoding
X-Goog-Stored-Content-Length


X-Goog-User-Project
X-GUploader-UploadID
X-HTTP-Method-Override
X-Upload-Content-Length
X-Upload-Content-Type



The JSON API uses the following query string parameters:



alt
callback
fields


key
prettyPrint


quotaUser
userProject



Standard HTTP headers
Authorization
A request header that contains a string used to authenticate requests.


Valid Values
The authentication identifier Bearer followed by a valid
      OAuth 2.0 token.


Example
Authorization: Bearer ya29.AHES6ZRVmB7fkLtd1XTmq6mo0S1wqZZi3-Lh_s- ...  


Details
You must send an OAuth 2.0 token with every request that requires an
      OAuth scope. OAuth 2.0 is the
      only supported authorization protocol.
      For more information about how to use this header, see
      Authentication.
To create a sample access token for testing, use the
      OAuth 2.0 playground.
Note: If your requests are being routed
        through a proxy, you might need to check with your network administrator
        to ensure that required Authorization headers are not
        stripped out by the proxy. Without the Authorization
        header, you receive a MissingSecurityHeader error and your
        request is rejected. For more information about accessing
        Cloud Storage through a proxy server, see the
        Troubleshooting topic.
For additional details, see the specification.


Cache-Control
A response header that indicates the caching directive for the request.


Valid Values
Any valid cache-control value (see the
    specification).


Example
Cache-Control: public, max-age=6000


Details
Indicates if, and how, the response can be cached. When serving publicly
    accessible objects from Cloud Storage, the value for
    Cache-Control is determined by the
    Cache-Control
    metadata set on the object. To be considered publicly accessible,
    permission to read the object's data must be available for
    allUsers. If an object is publicly accessible and you have not
    set the object's
    Cache-Control metadata, Cloud Storage applies a
    Cache-Control setting of 3600 seconds. When serving an object
    via the JSON API that is not publicly accessible, Cloud Storage
    sets the response to Cache-Control: no-cache, regardless of the
    metadata settings for the object.

    For additional details, see the specification.


Content-ID
An optional identifier in the part-header of a multipart request.


Valid Values
An identifier that is unique within the parts of the request.


Example
Content-ID: <b29c5de2-0db4-490b-b421-6a51b598bd22+1>


Details
Content-ID is only used in the body of multipart (batch) requests and only as
    an identifier of requests within the body. If included, any response will have a
    matching Content-ID header in the corresponding part whose value will be
    response- followed by the originally supplied ID.
    For additional details, see the specification.


Content-Length
The length (in bytes) of the request or response body.


Valid Values
Any value of zero or greater.


Example
Content-Length: 1234


Details
This is required for most POST and PUT commands used in uploading
    objects, except if you are using the header
    Transfer-Encoding: chunked.
    When making the initial request of a
    resumable upload, this header
    should be set to the number of bytes provided in that specific request.
    For more information, see Objects:insert.
    For additional details, see the specification.


Content-Range
A header used in some upload requests and download responses.


Valid Values
Any contiguous range of bytes.


Example
Content-Range: bytes 456-987/1234


Details
When appearing in a response, the Content-Range header
      indicates the range of bytes being returned as a result of a request that
      included a Range header.
When included as part of a resumable
      upload request, Content-Range is used to query for the
      current position of the upload or as an indicator of the starting point
      of the block of data being uploaded in the current request.
Byte ranges are inclusive; that is, bytes 0-999 represent
      the first 1000 bytes in a file or object.
For additional details, particularly regarding download responses, see the
      specification.


Content-Transfer-Encoding
A header used in some upload requests and download responses.


Valid Values
An optional request and response header that indicates the type of encoding that has
    been applied to the message body.


Example
Content-Transfer-Encoding: binary


Details
This header specifies the encoding of a message body in a request.
For additional details, see the specification.


Content-Type
The MIME type of the request or response.


Valid Values
Any valid MIME type.


Example
Content-Type: text/html


Details
This is required for POST and PUT commands associated with uploading objects and granting
    permissions; however, this command can alternatively be included in the body of the request
    instead of as a header (for more information, see
    Objects: insert).
    When making the initial request of a resumable
    upload that also includes metadata, use the Content-Type header to specify the metadata's
    data type.
For additional details, see the specification.


Date
The date and time of the request or response.


Valid Values
A date and time represented in conventional HTTP format (see the
    specification).


Example
Date: Wed, 16 Jun 2010 11:11:11 GMT


Details
For information about HTTP date formats, see the
    specification.


ETag
A response header that contains the entity tag of the object being accessed.


Valid Values
A string of characters enclosed by quotes. For more information, see
    Object metadata.


Example
ETag: "39a59594290b0f9a30662a56d695b71d"
ETag: "-CKicn4fknbUCEAE="


Details
See the specification.


Expires
A response header indicating the time after which the response is considered stale.


Valid Values
A date and time represented in conventional HTTP format (see the
    specification).


Example
Expires: Tue, 22 Jan 2013 18:56:00 GMT


Details
See the specification.


If-Match
A request header that specifies an entity tag (ETag).


Valid Values
A valid entity tag.


Example
If-Match: "881f7881ac1bc144a2672e45babb8839"


Details
This header is currently supported for GET requests.
      This header is supported for all resources, including buckets, objects and
      ACLs. If the ETag you specify with this header is the same as the ETag for
      the requested resource, then the request proceeds normally. If the ETag
      you specify with this header is different from the ETag for the requested
      resource, then the request fails and Cloud Storage returns a
      412
      Precondition Failed error code.
For additional details, see the specification.


If-None-Match
A request header that specifies an entity tag (ETag).


Valid Values
A valid entity tag.


Example
If-None-Match: "881f7881ac1bc144a2672e45babb8839"


Details
This header is currently supported for GET requests.
      This header is supported for all resources, including buckets, objects and
      ACLs. If the ETag you specify with this header is different than the ETag
      for the requested resource, then the request proceeds normally. If the
      ETag you specify with this header is the same as the ETag of the requested
      resource, then the request fails and Cloud Storage returns a
      304 Not
      Modified status code.
For additional details, see the specification.


Location
A response header providing a URI.


Valid Values
Any valid URI.


Example
Location: https://storage.googleapis.com/upload/storage/v1/b/example-bucket/o?uploadType=resumable&...


Details

The location header is used for several purposes:

In response to initiating a resumable upload it provides you with a session URI for a
      resumable upload operation.
In response to a Cookie-based
        authentication request it provides you with a unique web origin
        response URL for the request.
In response to a JSON API download request made at a URL other than `www.googleapis.com/download`
      it provides a redirect to the JSON API URL where the download can be made.

For additional details, see the specification.


Range
A request header indicating the range of bytes that you want returned, and a
response header indicating the range of bytes that have been uploaded to the
Cloud Storage system.


Valid Values
A contiguous range of bytes.


Examples
Range: bytes=0-1999 (first 2000 bytes)
Range: bytes=-2000 (last 2000 bytes)
Range: bytes=2000- (from byte 2000 to end of file)


Details

When included as a header in a request for object data, only the
      specified range of bytes for the object gets returned, which is useful
      when downloading an object in parallel requests or when resuming an
      interrupted download. Multiple byte ranges in a single request are not
      accepted, and in certain
      circumstances the Range request header is ignored.
When returned as part of a response associated with a resumable upload,
      Range indicates the number of bytes currently uploaded. You
      can subsequently use this information to
      continue
      the upload.
Byte ranges are inclusive. For example, bytes=0-999
      represent the first 1000 bytes in a file or object. For more information
      about this header, see the
      specification.


Extension (custom) HTTP headers
X-Goog-Allowed-Resources
A request header that restricts the resources the request is allowed to act on.


Valid Values
An RFC 4648
      Base64-encoded string of the
      organization
      restriction definition.


Example
X-Goog-Allowed-Resources: ewogInJlc291cmNlcyI6IFsib3JnYW5pemF0aW9ucy8xMjM0NTY3ODkiLCAib3JnYW5pemF0aW9ucy8xMDExMTIxMzE0Il0sCiAib3B0aW9ucyI6ICJzdHJpY3QiCn0K


Details
This request header prevents a request from proceeding unless each
    resource in the request is within an organization specified by the header.
    For more information, see
    Introduction
    to organization restrictions.


Transfer-Encoding
A request and response header that specifies if transfer-encoding had been
applied to the message body.


Valid Values
chunked


Example
Transfer-Encoding: chunked


Details
This header specifies if the message body of a request or response
      has been chunked. If it is, content is received or served in a series of
      chunks, with the final chunk having a length of zero. If you specify
      Transfer-Encoding: Chunked, you don't need to specify a
      Content-Length. This can be useful if you don't know the
      length of the message body in advance, such as when performing a streaming
      upload.
For more details about Transfer-Encodings, see the
      specification.
      For more details about chunked transfer encoding, see the
      specification.


X-Goog-Content-Length-Range
A PUT request header. When used, Cloud Storage only accepts the
    request if the size of the request's content is within the header's specified range.


Valid Values
A MIN,MAX pair


Example
X-Goog-Content-Length-Range: 0,256


Details

     The values for content size are inclusive and given in bytes. If the size of the request's
    content is in the specified range, it is delivered as requested. If the size of the request's
    content is outside the specified range, the request fails and a 400 Bad Request
    code is returned in the response. If the X-Goog-Content-Length-Range is used in
    a request other than PUT, the header is silently ignored.


X-Goog-Custom-Audit-KEY
A request header that specifies custom information to include in audit logs
generated by Cloud Audit Logs.


Valid Values
A string of characters (1,200 maximum).


Examples
X-Goog-Custom-Audit-User: user ID test 1
X-Goog-Custom-Audit-Job: test-job-id-here
X-Goog-Custom-Audit-Justification: Removed customer identity record at customer request



Details
The X-Goog-Custom-Audit-KEY header can be used in any
    JSON API request. The KEY is a custom string that can contain up
    to 64 characters. The VALUE is a custom string that can contain
    up to 1,200 characters.


X-Goog-Encryption-Algorithm
A request and response header that specifies the encryption algorithm to use.


Valid Values
AES256


Example
X-Goog-Encryption-Algorithm: AES256


Details
This request and response header is used when you provide
    customer-supplied
      encryption keys. When used specifically in a rewrite operation, this header applies to the
      destination object.


X-Goog-Encryption-Key
A request header that specifies an encryption key.


Valid Values
An RFC 4648 Base64-encoded string
    of a valid AES-256 encryption key


Example
X-Goog-Encryption-Key: NwbyGGmcKAX4FxGpOERG2Ap33m5NVOgmXznSGTEvG0I=


Details
This request header is used when you provide
    customer-supplied encryption keys.
      When used specifically in a rewrite operation, this header applies to the destination
      object.


X-Goog-Encryption-Key-Sha256
A request and response header that specifies the SHA256 hash of the encryption key.


Valid Values
An RFC 4648 Base64-encoded string
    of a valid SHA256 hash for an encryption key


Example
X-Goog-Encryption-Key-Sha256: +eBzkZBt1Mj2CZx69L3c8yXoZB6DtRLlSvXMJB9JGIQ=


Details
This request header is used when you provide
    customer-supplied encryption keys.
      When used specifically in a rewrite operation, this header applies to the destination
      object.


X-Goog-Copy-Source-Encryption-Algorithm
A request and response header that specifies the encryption algorithm to use on the source
      object when performing a rewrite.


Valid Values
AES256


Example
X-Goog-Copy-Source-Encryption-Algorithm: AES256


Details
This request and response header is used in rewrite operations when you provide
    customer-supplied encryption keys.
    This header applies to the source object used in the rewrite.


X-Goog-Copy-Source-Encryption-Key
A request header that specifies an encryption key to use to decrypt the source object
      when performing a rewrite.


Valid Values
An RFC 4648 Base64-encoded string
    of a valid AES-256 encryption key


Example
X-Goog-Copy-Source-Encryption-Key: NwbyGGmcKAX4FxGpOERG2Ap33m5NVOgmXznSGTEvG0I=


Details
This request header is used in rewrite operations when you provide
    customer-supplied encryption keys.
    This header applies to the source object in the rewrite.


X-Goog-Copy-Source-Encryption-Key-Sha256
A request and response header that specifies the SHA256 hash of the encryption key that is
      used to decrypt the source object when performing a rewrite.


Valid Values
An RFC 4648 Base64-encoded string
    of a valid SHA256 hash for an encryption key.


Example
X-Goog-Copy-Source-Encryption-Key-Sha256: +eBzkZBt1Mj2CZx69L3c8yXoZB6DtRLlSvXMJB9JGIQ=


Details
This request header is in rewrite operations when you provide
    customer-supplied encryption keys. This header applies
    to the source object in the rewrite.


X-Goog-Meta-KEY
A request header used to set
custom metadata in the
final request of a resumable
upload.


Valid Values
Any valid header name and value, with a maximum combined size of 8 KiB.


Example
X-Goog-Meta-foo: bar


Details

    The X-Goog-Meta- header is an optional header in the final
    request of a resumable upload. The KEY and the
    header's value are added to the custom metadata of the uploaded object. Any
    custom metadata set in the initial
    request that uses the same KEY string is
    overwritten using the value provided in the X-Goog-Meta-
    header. Keys specified using the X-Goog-Meta- header are always
    added to the object's metadata using lowercase characters because HTTP
    headers are case-insensitive.
    


X-Goog-Stored-Content-Encoding
A response header that indicates the content encoding value stored as part of
the object's metadata. This value is independent of any transcoding
that might be performed by the server during individual requests for the object.


Valid Values
The content-encoding specified in the stored object's metadata or
      identity.


Example
X-Goog-Stored-Content-Encoding: gzip


Details
If the object has no stored metadata value for
      content-encoding, then the value of this header is
      identity.


X-Goog-Stored-Content-Length
A response header that indicates the content length (in bytes) of the object as
stored in Cloud Storage, independent of any server-driven negotiation that
might occur for individual requests for the object.


Valid Values
Any byte value of zero or greater.


Example
X-Goog-Stored-Content-Length: 350


Details
None


X-Goog-User-Project
A request header that specifies a user project to bill for access charges associated with the request.


Valid Values
The Project ID for an existing Google Cloud project


Example
X-Goog-User-Project: my-project


Details
The project specified in the header is billed for charges associated with the request.
    This header is used, for example, when making requests to buckets that have
    Requester Pays enabled.
Generally, JSON requests that require a project ID should supply one in the request URL
    with the userProject parameter instead of with the X-Goog-User-Project
    header.


X-GUploader-UploadID
A response header returned for Cloud Storage requests.


Valid Values
A string of characters.


Example
X-GUploader-UploadID: ADPycdvYczN-TgGGp1mvqlCLVKg2m0Cp9niWTV2kc8MLJG6W6Xw7aPMYj1YU8Pxskb5C9lUM8hVEtBG6DubMif3xhXkgTpfhpg


Details
The X-GUploader-UploadID header is a unique identifier provided in
      Cloud Storage responses. This value can be helpful when
      troubleshooting with Google Cloud support.


X-HTTP-Method-Override
An alternative notation for sending PATCH commands.


Valid Values
PATCH


Example
X-HTTP-Method-Override: PATCH


Details
The X-HTTP-Method-Override header can be sent with a POST command in order to make the command behave as
      a PATCH command. This is useful when your firewall does not allow explicit PATCH
      commands to be sent.


X-Upload-Content-Length
A request header used in resumable uploads.


Valid Values
Any value of 0 or greater.


Example
X-Upload-Content-Length: 2000000


Details
The X-Upload-Content-Length header is used in the initial request of a
      resumable upload. It
      specifies the total size in bytes of the object to be uploaded. If the
      length is unknown at the time of the request, the header can be omitted.


X-Upload-Content-Type
A request header used in resumable uploads.


Valid Values
Any valid MIME type (see the
    specification).


Example
X-Upload-Content-Type: image/jpeg


Details
The X-Upload-Content-Type header is used in the initial request of a
      resumable upload. It
      specifies the MIME media type of the data that will be transferred in the
      resumable upload. If a MIME type is not specified in metadata or through
      this header, the object is served as
      application/octet-stream.


Standard Query Parameters
Query string parameters that can be used in any JSON API request are shown in
the table below. Note that not all parameters apply to all requests. For
example, use of the fields parameter has no effect on Delete requests, since
the response body is empty. See specific methods for additional query
string parameters.
In the examples of query parameters described in this section, the URIs are not
shown but are assumed to be relative to
https://storage.googleapis.com/storage/v1/PATH_TO_RESOURCE,
with the exception of object uploads and batched requests. For more information
about the URIs you should use when making requests to the JSON API, see
Request endpoints.
All parameters are optional except where noted.


Parameter
Meaning
Notes


alt
Data format for the response.

Valid values: json, media
Default value: json



callback
Callback function.

Name of the JavaScript callback function that handles the response.
Used in JavaScript JSON-P requests.



fields
Selector specifying a subset of fields to include in the response.

For more information, see the partial response
        documentation.
Use for better performance.



prettyPrint
Returns response with indentations and line breaks.

Returns the response in a human-readable format if true. 
Default value: true.
When this  is  false, it can  reduce the response payload size, which might
        lead to better performance in some environments.



quotaUser
IP address of the end user for whom the API call is being made.

Lets you enforce per-user quotas from a server-side application even in cases when the
        user's IP address is unknown. This can occur, for example, with applications that run cron
        jobs on App Engine on a user's behalf.
You can choose any arbitrary string that uniquely identifies a user, but it is limited to
        40 characters.
Learn more about Capping API usage.



userProject
The project to be billed for the request.

Required for requests to buckets that have
        Requester Pays enabled.



What's next

See an example JSON API request used to create a Cloud Storage
bucket.







  
    
    Send feedback
  
  



