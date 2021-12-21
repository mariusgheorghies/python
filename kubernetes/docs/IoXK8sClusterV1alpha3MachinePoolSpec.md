# IoXK8sClusterV1alpha3MachinePoolSpec

MachinePoolSpec defines the desired state of MachinePool.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_name** | **str** | ClusterName is the name of the Cluster this object belongs to. | 
**failure_domains** | **list[str]** | FailureDomains is the list of failure domains this MachinePool should be attached to. | [optional] 
**min_ready_seconds** | **int** | Minimum number of seconds for which a newly created machine instances should be ready. Defaults to 0 (machine instance will be considered available as soon as it is ready) | [optional] 
**provider_id_list** | **list[str]** | ProviderIDList are the identification IDs of machine instances provided by the provider. This field must match the provider IDs as seen on the node objects corresponding to a machine pool&#39;s machine instances. | [optional] 
**replicas** | **int** | Number of desired machines. Defaults to 1. This is a pointer to distinguish between explicit zero and not specified. | [optional] 
**strategy** | [**IoXK8sClusterV1alpha3MachinePoolSpecStrategy**](IoXK8sClusterV1alpha3MachinePoolSpecStrategy.md) |  | [optional] 
**template** | [**IoXK8sClusterV1alpha3MachineDeploymentSpecTemplate**](IoXK8sClusterV1alpha3MachineDeploymentSpecTemplate.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


