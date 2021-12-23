# IoCertManagerV1ClusterIssuerStatusConditions

IssuerCondition contains condition information for an Issuer.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_transition_time** | **datetime** | LastTransitionTime is the timestamp corresponding to the last status change of this condition. | [optional] 
**message** | **str** | Message is a human readable description of the details of the last transition, complementing reason. | [optional] 
**observed_generation** | **int** | If set, this represents the .metadata.generation that the condition was set based upon. For instance, if .metadata.generation is currently 12, but the .status.condition[x].observedGeneration is 9, the condition is out of date with respect to the current state of the Issuer. | [optional] 
**reason** | **str** | Reason is a brief machine readable explanation for the condition&#39;s last transition. | [optional] 
**status** | **str** | Status of the condition, one of (&#x60;True&#x60;, &#x60;False&#x60;, &#x60;Unknown&#x60;). | 
**type** | **str** | Type of the condition, known values are (&#x60;Ready&#x60;). | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


