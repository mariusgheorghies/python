# IoXK8sClusterV1alpha4ClusterSpecTopology

This encapsulates the topology for the cluster. NOTE: It is required to enable the ClusterTopology feature gate flag to activate managed topologies support; this feature is highly experimental, and parts of it might still be not implemented.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_class** | **str** | The name of the ClusterClass object to create the topology. | 
**control_plane** | [**IoXK8sClusterV1alpha4ClusterSpecTopologyControlPlane**](IoXK8sClusterV1alpha4ClusterSpecTopologyControlPlane.md) |  | [optional] 
**rollout_after** | **datetime** | RolloutAfter performs a rollout of the entire cluster one component at a time, control plane first and then machine deployments. | [optional] 
**version** | **str** | The Kubernetes version of the cluster. | 
**workers** | [**IoXK8sClusterV1alpha4ClusterSpecTopologyWorkers**](IoXK8sClusterV1alpha4ClusterSpecTopologyWorkers.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


