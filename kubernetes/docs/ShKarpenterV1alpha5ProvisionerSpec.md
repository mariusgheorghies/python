# ShKarpenterV1alpha5ProvisionerSpec

ProvisionerSpec is the top level provisioner specification. Provisioners launch nodes in response to pods that are unschedulable. A single provisioner is capable of managing a diverse set of nodes. Node properties are determined from a combination of provisioner and pod scheduling constraints.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kubelet_configuration** | [**ShKarpenterV1alpha5ProvisionerSpecKubeletConfiguration**](ShKarpenterV1alpha5ProvisionerSpecKubeletConfiguration.md) |  | [optional] 
**labels** | **dict(str, str)** | Labels are layered with Requirements and applied to every node. | [optional] 
**limits** | [**ShKarpenterV1alpha5ProvisionerSpecLimits**](ShKarpenterV1alpha5ProvisionerSpecLimits.md) |  | [optional] 
**provider** | [**object**](.md) | Provider contains fields specific to your cloudprovider. | [optional] 
**provider_ref** | [**ShKarpenterV1alpha5ProvisionerSpecProviderRef**](ShKarpenterV1alpha5ProvisionerSpecProviderRef.md) |  | [optional] 
**requirements** | [**list[ComCoreosMonitoringV1AlertmanagerSpecAffinityNodeAffinityPreferenceMatchExpressions]**](ComCoreosMonitoringV1AlertmanagerSpecAffinityNodeAffinityPreferenceMatchExpressions.md) | Requirements are layered with Labels and applied to every node. | [optional] 
**startup_taints** | [**list[ShKarpenterV1alpha5ProvisionerSpecStartupTaints]**](ShKarpenterV1alpha5ProvisionerSpecStartupTaints.md) | StartupTaints are taints that are applied to nodes upon startup which are expected to be removed automatically within a short period of time, typically by a DaemonSet that tolerates the taint. These are commonly used by daemonsets to allow initialization and enforce startup ordering.  StartupTaints are ignored for provisioning purposes in that pods are not required to tolerate a StartupTaint in order to have nodes provisioned for them. | [optional] 
**taints** | [**list[ShKarpenterV1alpha5ProvisionerSpecStartupTaints]**](ShKarpenterV1alpha5ProvisionerSpecStartupTaints.md) | Taints will be applied to every node launched by the Provisioner. If specified, the provisioner will not provision nodes for pods that do not have matching tolerations. Additional taints will be created that match pod tolerations on a per-node basis. | [optional] 
**ttl_seconds_after_empty** | **int** | TTLSecondsAfterEmpty is the number of seconds the controller will wait before attempting to delete a node, measured from when the node is detected to be empty. A Node is considered to be empty when it does not have pods scheduled to it, excluding daemonsets.   Termination due to underutilization is disabled if this field is not set. | [optional] 
**ttl_seconds_until_expired** | **int** | TTLSecondsUntilExpired is the number of seconds the controller will wait before terminating a node, measured from when the node is created. This is useful to implement features like eventually consistent node upgrade, memory leak protection, and disruption testing.   Termination due to expiration is disabled if this field is not set. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


