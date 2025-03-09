# Google Cloud Storage API: Status and error codes






    
        Home
      
  




    
        Cloud Storage
      
  




    
        Documentation
      
  




    
        Reference
      
  







  
    
    Send feedback
  
  


      HTTP status and error codes for JSON
      
    



      
      Stay organized with collections
    

      
      Save and categorize content based on your preferences.
    





The following document provides reference information about the status codes
and error messages that are used in the Cloud Storage JSON API. For
the page specific to the Cloud Storage XML API, see
HTTP status and error codes for XML.
Error Response Format
Cloud Storage uses the standard HTTP error reporting format for the
JSON API. Successful requests return HTTP status codes in the 2xx range. Failed
requests return status codes in the 4xx and 5xx ranges. Requests that require a
redirect returns status codes in the 3xx range. Error responses usually include
a JSON document in the response body, which contains information about the
error.
The following examples show some common errors. Note that the header
information in the responses is omitted.

401 UnauthorizedThe following is an example of an error response you receive if you try to
list the buckets for a project but do not provide an authorization header.

401 Unauthorized

{
"error": {
 "errors": [
  {
   "domain": "global",
   "reason": "required",
   "message": "Login Required",
   "locationType": "header",
   "location": "Authorization"
  }
 ],
 "code": 401,
 "message": "Login Required"
 }
}

403 ForbiddenThis is an example of an error response you receive if you try to list the
buckets of a non-existent project or one in which you don't have permission
to list buckets.

403 Forbidden

{
 "error": {
  "errors": [
   {
    "domain": "global",
    "reason": "forbidden",
    "message": "Forbidden"
    }
  ],
  "code": 403,
  "message": "Forbidden"
 }
}

404 Not FoundThe following is an example of an error response you receive if you try to
retrieve an object that does not exist.

404 Not Found

{
"error": {
 "errors": [
  {
   "domain": "global",
   "reason": "notFound",
   "message": "Not Found"
  }
 ],
 "code": 404,
 "message": "Not Found"
 }
}

409 ConflictThe following is an example of an error response you receive if you try to
create a bucket using the name of a bucket you already own.

409 Conflict

{
"error": {
 "errors": [
  {
   "domain": "global",
   "reason": "conflict",
   "message": "You already own this bucket. Please select another name."
  }
 ],
 "code": 409,
 "message": "You already own this bucket. Please select another name."
 }
}


The following table describes the elements that can appear in the response body
of an error. Fields should be used together to help determine the problem.
Also, the example values given below are meant for illustration and are not an
exhaustive list of all possible values.



Element
Description




code
An HTTP status code value, without the textual description.Example values include: 400 (Bad Request), 401 (Unauthorized), and 404 (Not Found).


error
A container for the error information.


errors
A container for the error details.


errors.domain
The scope of the error. Example values include: global and push.


errors.location
The specific item within the locationType that caused the error. For example, if you specify an invalid value for a parameter, the location will be the name of the parameter.Example values include: Authorization, project, and projection.


errors.locationType
The location or part of the request that caused the error. Use with location to pinpoint the error. For example, if you specify an invalid value for a parameter, the locationType will be parameter and the location will be the name of the parameter.Example values include header and parameter.


errors.message
Description of the error.Example values include Invalid argument, Login required, and Required parameter: project.


errors.reason
Example values include invalid, invalidParameter, and required.


message
Description of the error. Same as errors.message.



HTTP Status and Error Codes
This section provides a non-exhaustive list of HTTP status and error codes that
the Cloud Storage JSON API uses. The 1xx Informational and 2xx
Success codes are not discussed here. For more information, see Response Status
Codes in RFC 7231 §6, RFC 7232 §4,
RFC 7233 §4, RFC 7235 §3, and RFC 6585.
302—Found



Reason
Description




found
Resource temporarily located elsewhere according to the Location header.



303—See Other



Reason
Description




mediaDownloadRedirect
When requesting a download using alt=media URL parameter, the direct URL path to use is prefixed by /download. If this is omitted, the service will issue this redirect with the appropriate media download path in the Location header.



304—Not Modified



Reason
Description




notModified
The conditional request would have been successful, but the condition was false, so no body was sent.



307—Temporary Redirect



Reason
Description




temporaryRedirect
Resource temporarily located elsewhere according to the Location header. Among other reasons, this can occur when cookie-based authentication is being used, e.g., when using the Storage Browser, and it receives a request to download content.



308—Resume Incomplete



Description




Indicates an incomplete resumable upload and provides the range of bytes already received by Cloud Storage. Responses with this status do not contain a body.



400—Bad Request



[Domain.]Reason
Description




badRequest
The request cannot be completed based on your current Cloud Storage settings. For example, you cannot lock a retention policy if the requested bucket doesn't have a retention policy, and you cannot set ACLs if the requested bucket has uniform bucket-level access enabled.


badRequestException
The retention period on a locked bucket cannot be reduced.


cloudKmsBadKey
Bad Cloud KMS key.


cloudKmsCannotChangeKeyName
Cloud KMS key name cannot be changed.


cloudKmsDecryptionKeyNotFound
Resource's Cloud KMS decryption key not found.


cloudKmsDisabledKey
Cloud KMS key is disabled, destroyed, or scheduled to be destroyed.


cloudKmsEncryptionKeyNotFound
Cloud KMS encryption key not found.


cloudKmsKeyLocationNotAllowed
Cloud KMS key location not allowed.


corsRequestWithXOrigin
CORS request contains an XD3 X-Origin header.


customerEncryptionAlgorithmIsInvalid
Missing an encryption algorithm, or the provided algorithm is not "AE256."


customerEncryptionKeyFormatIsInvalid
Missing an encryption key, or it is not Base64 encoded, or it does not meet the required length of the encryption algorithm.


customerEncryptionKeyIsIncorrect
The provided encryption key is incorrect.


customerEncryptionKeySha256IsInvalid
Missing a SHA256 hash of the encryption key, or it is not Base64 encoded, or it does not match the encryption key.


invalid
This error can occur for several reasons: The request is attempting to set a retention configuration for an object such that the mode or retainUntilTime is not defined; or the request is attempting to set the properties of an object such that it would have a retention configuration and be subject to an event-based hold at the same time; or the request is attempting to set an invalid retain-until date; or the request is attempting to set a retention configuration on an object stored in a bucket that doesn't have the feature enabled.


invalidAltValue
The value for the alt URL parameter was not recognized.


invalidArgument
The value for one of fields in the request body was invalid.


invalidParameter
The value for one of the URL parameters was invalid. In addition to normal URL parameter validation, any URL parameters that have a corresponding value in provided JSON request bodies must match if they are both specified. If using JSONP, you will get this error if you provide an alt parameter that is not json.


notDownload
Uploads or normal API request was sent to a /download/* path. Use the same path, but without the /download prefix.


notUpload
Downloads or normal API request was sent to a /upload/* path. Use the same path, but without the /upload prefix.


parseError
Couldn't parse the body of the request according to the provided Content-Type.


push.channelIdInvalid
Channel ID must match the following regular expression: [A-Za-z0-9\\-_\\+/=]+


push.channelIdNotUnique
storage.objects.watchAll's id property must be unique across channels.


push.webhookUrlNoHostOrAddress
storage.objects.watchAll's address property must contain a valid URL.


push.webhookUrlNotHttps
storage.objects.watchAll's address property must be an HTTPS URL.


required
A required URL parameter or required request body JSON property is missing.


resourceIsEncryptedWithCustomerEncryptionKey
The resource is encrypted with a customer-supplied encryption key, but the request did not provide one.


resourceNotEncryptedWithCustomerEncryptionKey
The resource is not encrypted with a customer-supplied encryption key, but the request provided one.


turnedDown
A request was made to an API version that has been turned down. Clients will need to update to a supported version.


userProjectInvalid
The user project specified in the request is invalid, either because it is a malformed project id or because it refers to a non-existent project.


userProjectMissing
The requested bucket has Requester Pays enabled, the requester is not an owner of the bucket, and no user project was present in the request.


wrongUrlForUpload
storage.objects.insert must be invoked as an upload rather than a metadata.



401—Unauthorized



[Domain.]Reason
Description




AuthenticationRequiredRequesterPays
Access to a Requester Pays bucket requires authentication.


authError
This error indicates a problem with the authorization provided in the request to Cloud Storage. The following are some situations where that will occur:The OAuth access token has expired and needs to be refreshed. This can be avoided by refreshing the access token early, but code can also catch this error, refresh the token and retry automatically.Multiple non-matching authorizations were provided; choose one mode only.The OAuth access token's bound project does not match the project associated with the provided developer key.The Authorization header was of an unrecognized format or uses an unsupported credential type.


lockedDomainExpired
When downloading content from a cookie-authenticated site, e.g., using the Storage Browser, the response will redirect to a temporary domain. This error will occur if access to said domain occurs after the domain expires. Issue the original request again, and receive a new redirect.


required
Access to a non-public method that requires authorization was made, but none was provided in the Authorization header or through other means.



403—Forbidden



[Domain.]Reason
Description




accountDisabled
The account associated with the project that owns the bucket or object has been disabled. Check the Google Cloud console to see if there is a problem with billing, and if not, contact account support.


countryBlocked
The Cloud Storage JSON API is restricted by law from operating with certain countries.


forbidden
This error can occur for several reasons: According to access control policy, the current user does not have access to perform the requested action, and this can occur even if the resource being acted on doesn't exist; or the request is missing the overrideUnlockedRetention query parameter but is attempting to change an object's existing retention configuration in a way that requires the parameter; or the request is attempting to change a locked object's retention configuration in a way that requires the object to be unlocked.


insufficientPermissions
According to access control policy, the current user does not have access to perform the requested action. This code applies even if the resource being acted on doesn't exist.


objectUnderActiveHold
Object replacement or deletion is not allowed due to an active hold on the object.


retentionPolicyNotMet
The object is under retention and cannot be replaced or deleted until the date and time indicated. The retention might be due to a retention configuration on the object, a retention policy on the bucket, or both.


sslRequired
Requests to this API require SSL.


stopChannelCallerNotOwner
Calls to storage.channels.stop require that the caller own the channel.


UserProjectAccessDenied
The requester is not authorized to use the project specified in the userProject portion of the request. The requester must have the serviceusage.services.use permission for the specified project.


UserProjectAccountProblem
There is a problem with the project used in the request that prevents the operation from completing successfully. One issue could be billing. Check the billing page to see if you have a past due balance or if the credit card (or other payment mechanism) on your account is expired. For project creation, see the Projects page in the Google Cloud console.



404—Not Found



Reason
Description




notFound
Either there is no API method associated with the URL path of the request, or the request refers to one or more resources that were not found.



405—Method Not Allowed



Reason
Description




methodNotAllowed
The HTTP verb is not supported by the URL endpoint used in the request. This can happen, for example, when using the wrong verb with the /upload or /download URLs.



408—Request Timeout



Reason
Description




uploadBrokenConnection
The request timed out. You should retry the request using truncated exponential backoff.



409—Conflict



Reason
Description




conflict
A request to change a resource, usually a storage.*.update or storage.*.patch method, failed to commit the change due to a conflicting concurrent change to the same resource. The request can be retried, though care should be taken to consider the new state of the resource to avoid blind replacement of another agent's changes.



410—Gone



Description




You have attempted to use a resumable upload session or rewrite token that is no longer available. If the reported status code was not successful and you still wish to complete the upload or rewrite, you must start a new session.



411—Length Required



Description




You must provide the Content-Length HTTP header. This error has no response body.



412—Precondition Failed



Reason
Description




conditionNotMet
At least one of the pre-conditions you specified did not hold.


orgPolicyConstraintFailed
Request violates an OrgPolicy constraint.


softDeletePolicyNotSet
Bucket does not have a soft delete policy.


objectNotSoftDeleted
Object is not soft deleted and is either live or noncurrent.



413—Payload Too Large



Reason
Description




uploadTooLarge
This error arises if you:Attempt to upload an object larger than 5 TiB.Attempt a Copy request that does not complete within 30 seconds and involves an object larger than 2.5 GiB. In this case, use the Rewrite method instead.



416—Requested Range Not Satisfiable



Reason
Description




requestedRangeNotSatisfiable
The requested Range cannot be satisfied.



429—Too Many Requests



[Domain.]Reason
Description




usageLimits.rateLimitExceeded
A Cloud Storage JSON API usage limit was exceeded. If your application tries to use more than its limit, additional requests will fail. Throttle your client's requests, and/or retry requests using truncated exponential backoff.



499—Client Closed Request



Description




The resumable upload was cancelled at the client's request prior to completion. This error has no response body.



500—Internal Server Error



Reason
Description




backendError
We encountered an internal error. You should retry the request using truncated exponential backoff.


internalError
We encountered an internal error. You should retry the request using truncated exponential backoff.



502—Bad Gateway
This error is generated when there was difficulty reaching an internal service.
It is not formatted with a JSON document. You should retry the request
using truncated exponential backoff.
503—Service Unavailable



Reason
Description




backendError
We encountered an internal error. You should retry the request using truncated exponential backoff.



504—Gateway Timeout
This error is generated when there was difficulty reaching an internal service.
It is not formatted with a JSON document. You should retry the request
using truncated exponential backoff.






  
    
    Send feedback
  
  



