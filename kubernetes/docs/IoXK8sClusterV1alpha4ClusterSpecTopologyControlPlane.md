# IoXK8sClusterV1alpha4ClusterSpecTopologyControlPlane

ControlPlane describes the cluster control plane.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**IoXK8sClusterV1alpha4ClusterSpecTopologyControlPlaneMetadata**](IoXK8sClusterV1alpha4ClusterSpecTopologyControlPlaneMetadata.md) |  | [optional] 
**replicas** | **int** | Replicas is the number of control plane nodes. If the value is nil, the ControlPlane object is created without the number of Replicas and it&#39;s assumed that the control plane controller does not implement support for this field. When specified against a control plane provider that lacks support for this field, this value will be ignored. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


