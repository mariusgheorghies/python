# IoXK8sClusterV1alpha3MachineSetSpecSelector

Selector is a label query over machines that should match the replica count. Label keys and values that must match in order to be controlled by this MachineSet. It must match the machine template's labels. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**match_expressions** | [**list[ComCoreosMonitoringV1AlertmanagerSpecAffinityPodAffinityPodAffinityTermLabelSelectorMatchExpressions]**](ComCoreosMonitoringV1AlertmanagerSpecAffinityPodAffinityPodAffinityTermLabelSelectorMatchExpressions.md) | matchExpressions is a list of label selector requirements. The requirements are ANDed. | [optional] 
**match_labels** | **dict(str, str)** | matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is \&quot;key\&quot;, the operator is \&quot;In\&quot;, and the values array contains only \&quot;value\&quot;. The requirements are ANDed. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


