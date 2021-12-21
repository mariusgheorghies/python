# IoXK8sClusterControlplaneV1alpha4KubeadmControlPlaneSpecMachineTemplate

MachineTemplate contains information about how machines should be shaped when creating or updating a control plane.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**infrastructure_ref** | [**IoXK8sClusterControlplaneV1alpha4KubeadmControlPlaneSpecMachineTemplateInfrastructureRef**](IoXK8sClusterControlplaneV1alpha4KubeadmControlPlaneSpecMachineTemplateInfrastructureRef.md) |  | 
**metadata** | [**IoXK8sClusterControlplaneV1alpha4KubeadmControlPlaneSpecMachineTemplateMetadata**](IoXK8sClusterControlplaneV1alpha4KubeadmControlPlaneSpecMachineTemplateMetadata.md) |  | [optional] 
**node_drain_timeout** | **str** | NodeDrainTimeout is the total amount of time that the controller will spend on draining a controlplane node The default value is 0, meaning that the node can be drained without any time limitations. NOTE: NodeDrainTimeout is different from &#x60;kubectl drain --timeout&#x60; | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


