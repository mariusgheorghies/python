# IoCertManagerV1CertificateRequestStatus

Status of the CertificateRequest. This is set and managed automatically.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ca** | **str** | The PEM encoded x509 certificate of the signer, also known as the CA (Certificate Authority). This is set on a best-effort basis by different issuers. If not set, the CA is assumed to be unknown/not available. | [optional] 
**certificate** | **str** | The PEM encoded x509 certificate resulting from the certificate signing request. If not set, the CertificateRequest has either not been completed or has failed. More information on failure can be found by checking the &#x60;conditions&#x60; field. | [optional] 
**conditions** | [**list[IoCertManagerV1CertificateRequestStatusConditions]**](IoCertManagerV1CertificateRequestStatusConditions.md) | List of status conditions to indicate the status of a CertificateRequest. Known condition types are &#x60;Ready&#x60; and &#x60;InvalidRequest&#x60;. | [optional] 
**failure_time** | **datetime** | FailureTime stores the time that this CertificateRequest failed. This is used to influence garbage collection and back-off. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


