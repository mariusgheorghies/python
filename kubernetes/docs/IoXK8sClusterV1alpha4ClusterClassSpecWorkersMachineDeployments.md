# IoXK8sClusterV1alpha4ClusterClassSpecWorkersMachineDeployments

MachineDeploymentClass serves as a template to define a set of worker nodes of the cluster provisioned using the `ClusterClass`.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_class** | **str** | Class denotes a type of worker node present in the cluster, this name MUST be unique within a ClusterClass and can be referenced in the Cluster to create a managed MachineDeployment. | 
**template** | [**IoXK8sClusterV1alpha4ClusterClassSpecWorkersTemplate**](IoXK8sClusterV1alpha4ClusterClassSpecWorkersTemplate.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


