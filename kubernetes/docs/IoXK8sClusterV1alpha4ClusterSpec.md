# IoXK8sClusterV1alpha4ClusterSpec

ClusterSpec defines the desired state of Cluster.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_network** | [**IoXK8sClusterV1alpha3ClusterSpecClusterNetwork**](IoXK8sClusterV1alpha3ClusterSpecClusterNetwork.md) |  | [optional] 
**control_plane_endpoint** | [**IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneSpecControlPlaneEndpoint**](IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneSpecControlPlaneEndpoint.md) |  | [optional] 
**control_plane_ref** | [**IoXK8sClusterV1alpha3ClusterSpecControlPlaneRef**](IoXK8sClusterV1alpha3ClusterSpecControlPlaneRef.md) |  | [optional] 
**infrastructure_ref** | [**IoXK8sClusterV1alpha3ClusterSpecInfrastructureRef**](IoXK8sClusterV1alpha3ClusterSpecInfrastructureRef.md) |  | [optional] 
**paused** | **bool** | Paused can be used to prevent controllers from processing the Cluster and all its associated objects. | [optional] 
**topology** | [**IoXK8sClusterV1alpha4ClusterSpecTopology**](IoXK8sClusterV1alpha4ClusterSpecTopology.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


