# IoXK8sClusterAddonsV1beta1ClusterResourceSetStatusConditions

Condition defines an observation of a Cluster API resource operational state.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_transition_time** | **datetime** | Last time the condition transitioned from one status to another. This should be when the underlying condition changed. If that is not known, then using the time when the API field changed is acceptable. | 
**message** | **str** | A human readable message indicating details about the transition. This field may be empty. | [optional] 
**reason** | **str** | The reason for the condition&#39;s last transition in CamelCase. The specific API may choose whether or not this field is considered a guaranteed API. This field may not be empty. | [optional] 
**severity** | **str** | Severity provides an explicit classification of Reason code, so the users or machines can immediately understand the current situation and act accordingly. The Severity field MUST be set only when Status&#x3D;False. | [optional] 
**status** | **str** | Status of the condition, one of True, False, Unknown. | 
**type** | **str** | Type of condition in CamelCase or in foo.example.com/CamelCase. Many .condition.type values are consistent across resources like Available, but because arbitrary conditions can be useful (see .node.status.conditions), the ability to deconflict is important. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


