# ComCoreosMonitoringV1AlertmanagerSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecution

If the affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node. If the affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to an update), the system may or may not try to eventually evict the pod from its node.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_selector_terms** | [**list[ComCoreosMonitoringV1AlertmanagerSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionNodeSelectorTerms]**](ComCoreosMonitoringV1AlertmanagerSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionNodeSelectorTerms.md) | Required. A list of node selector terms. The terms are ORed. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


