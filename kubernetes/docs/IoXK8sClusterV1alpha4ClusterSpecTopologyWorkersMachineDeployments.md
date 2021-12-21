# IoXK8sClusterV1alpha4ClusterSpecTopologyWorkersMachineDeployments

MachineDeploymentTopology specifies the different parameters for a set of worker nodes in the topology. This set of nodes is managed by a MachineDeployment object whose lifecycle is managed by the Cluster controller.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_class** | **str** | Class is the name of the MachineDeploymentClass used to create the set of worker nodes. This should match one of the deployment classes defined in the ClusterClass object mentioned in the &#x60;Cluster.Spec.Class&#x60; field. | 
**metadata** | [**IoXK8sClusterV1alpha4ClusterSpecTopologyWorkersMetadata**](IoXK8sClusterV1alpha4ClusterSpecTopologyWorkersMetadata.md) |  | [optional] 
**name** | **str** | Name is the unique identifier for this MachineDeploymentTopology. The value is used with other unique identifiers to create a MachineDeployment&#39;s Name (e.g. cluster&#39;s name, etc). In case the name is greater than the allowed maximum length, the values are hashed together. | 
**replicas** | **int** | Replicas is the number of worker nodes belonging to this set. If the value is nil, the MachineDeployment is created without the number of Replicas (defaulting to zero) and it&#39;s assumed that an external entity (like cluster autoscaler) is responsible for the management of this value. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


