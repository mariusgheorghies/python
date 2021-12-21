# IoXK8sClusterV1alpha4MachineSetSpec

MachineSetSpec defines the desired state of MachineSet.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_name** | **str** | ClusterName is the name of the Cluster this object belongs to. | 
**delete_policy** | **str** | DeletePolicy defines the policy used to identify nodes to delete when downscaling. Defaults to \&quot;Random\&quot;.  Valid values are \&quot;Random, \&quot;Newest\&quot;, \&quot;Oldest\&quot; | [optional] 
**min_ready_seconds** | **int** | MinReadySeconds is the minimum number of seconds for which a newly created machine should be ready. Defaults to 0 (machine will be considered available as soon as it is ready) | [optional] 
**replicas** | **int** | Replicas is the number of desired replicas. This is a pointer to distinguish between explicit zero and unspecified. Defaults to 1. | [optional] 
**selector** | [**IoXK8sClusterV1alpha3MachineSetSpecSelector**](IoXK8sClusterV1alpha3MachineSetSpecSelector.md) |  | 
**template** | [**IoXK8sClusterV1alpha4MachineSetSpecTemplate**](IoXK8sClusterV1alpha4MachineSetSpecTemplate.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


