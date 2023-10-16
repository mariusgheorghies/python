# IoCertManagerAcmeV1ChallengeSpecSolverHttp01IngressPodTemplateSpec

PodSpec defines overrides for the HTTP01 challenge solver pod. Only the 'priorityClassName', 'nodeSelector', 'affinity', 'serviceAccountName' and 'tolerations' fields are supported currently. All other fields will be ignored.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affinity** | [**IoCertManagerAcmeV1ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinity**](IoCertManagerAcmeV1ChallengeSpecSolverHttp01IngressPodTemplateSpecAffinity.md) |  | [optional] 
**node_selector** | **dict(str, str)** | NodeSelector is a selector which must be true for the pod to fit on a node. Selector which must match a node&#39;s labels for the pod to be scheduled on that node. More info: https://kubernetes.io/docs/concepts/configuration/assign-pod-node/ | [optional] 
**priority_class_name** | **str** | If specified, the pod&#39;s priorityClassName. | [optional] 
**service_account_name** | **str** | If specified, the pod&#39;s service account | [optional] 
**tolerations** | [**list[ComCoreosMonitoringV1AlertmanagerSpecTolerations]**](ComCoreosMonitoringV1AlertmanagerSpecTolerations.md) | If specified, the pod&#39;s tolerations. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


