# IoCertManagerV1CertificateRequestStatusConditions

CertificateRequestCondition contains condition information for a CertificateRequest.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_transition_time** | **datetime** | LastTransitionTime is the timestamp corresponding to the last status change of this condition. | [optional] 
**message** | **str** | Message is a human readable description of the details of the last transition, complementing reason. | [optional] 
**reason** | **str** | Reason is a brief machine readable explanation for the condition&#39;s last transition. | [optional] 
**status** | **str** | Status of the condition, one of (&#x60;True&#x60;, &#x60;False&#x60;, &#x60;Unknown&#x60;). | 
**type** | **str** | Type of the condition, known values are (&#x60;Ready&#x60;, &#x60;InvalidRequest&#x60;, &#x60;Approved&#x60;, &#x60;Denied&#x60;). | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


