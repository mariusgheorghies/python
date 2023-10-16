# IoTigeraOperatorV1InstallationSpecTyphaAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecution

WARNING: Please note that if the affinity requirements specified by this field are not met at scheduling time, the pod will NOT be scheduled onto the node. There is no fallback to another affinity rules with this setting. This may cause networking disruption or even catastrophic failure! PreferredDuringSchedulingIgnoredDuringExecution should be used for affinity unless there is a specific well understood reason to use RequiredDuringSchedulingIgnoredDuringExecution and you can guarantee that the RequiredDuringSchedulingIgnoredDuringExecution will always have sufficient nodes to satisfy the requirement. NOTE: RequiredDuringSchedulingIgnoredDuringExecution is set by default for AKS nodes, to avoid scheduling Typhas on virtual-nodes. If the affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to an update), the system may or may not try to eventually evict the pod from its node.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_selector_terms** | [**list[ComCoreosMonitoringV1AlertmanagerSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionNodeSelectorTerms]**](ComCoreosMonitoringV1AlertmanagerSpecAffinityNodeAffinityRequiredDuringSchedulingIgnoredDuringExecutionNodeSelectorTerms.md) | Required. A list of node selector terms. The terms are ORed. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


