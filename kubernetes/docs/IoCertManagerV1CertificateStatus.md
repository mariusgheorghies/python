# IoCertManagerV1CertificateStatus

Status of the Certificate. This is set and managed automatically.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | [**list[IoCertManagerV1CertificateStatusConditions]**](IoCertManagerV1CertificateStatusConditions.md) | List of status conditions to indicate the status of certificates. Known condition types are &#x60;Ready&#x60; and &#x60;Issuing&#x60;. | [optional] 
**last_failure_time** | **datetime** | LastFailureTime is the time as recorded by the Certificate controller of the most recent failure to complete a CertificateRequest for this Certificate resource. If set, cert-manager will not re-request another Certificate until 1 hour has elapsed from this time. | [optional] 
**next_private_key_secret_name** | **str** | The name of the Secret resource containing the private key to be used for the next certificate iteration. The keymanager controller will automatically set this field if the &#x60;Issuing&#x60; condition is set to &#x60;True&#x60;. It will automatically unset this field when the Issuing condition is not set or False. | [optional] 
**not_after** | **datetime** | The expiration time of the certificate stored in the secret named by this resource in &#x60;spec.secretName&#x60;. | [optional] 
**not_before** | **datetime** | The time after which the certificate stored in the secret named by this resource in spec.secretName is valid. | [optional] 
**renewal_time** | **datetime** | RenewalTime is the time at which the certificate will be next renewed. If not set, no upcoming renewal is scheduled. | [optional] 
**revision** | **int** | The current &#39;revision&#39; of the certificate as issued.   When a CertificateRequest resource is created, it will have the &#x60;cert-manager.io/certificate-revision&#x60; set to one greater than the current value of this field.   Upon issuance, this field will be set to the value of the annotation on the CertificateRequest resource used to issue the certificate.   Persisting the value on the CertificateRequest resource allows the certificates controller to know whether a request is part of an old issuance or if it is part of the ongoing revision&#39;s issuance by checking if the revision value in the annotation is greater than this field. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


