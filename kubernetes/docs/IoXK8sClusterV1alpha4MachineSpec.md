# IoXK8sClusterV1alpha4MachineSpec

MachineSpec defines the desired state of Machine.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bootstrap** | [**IoXK8sClusterV1alpha4MachineSpecBootstrap**](IoXK8sClusterV1alpha4MachineSpecBootstrap.md) |  | 
**cluster_name** | **str** | ClusterName is the name of the Cluster this object belongs to. | 
**failure_domain** | **str** | FailureDomain is the failure domain the machine will be created in. Must match a key in the FailureDomains map stored on the cluster object. | [optional] 
**infrastructure_ref** | [**IoXK8sClusterControlplaneV1alpha4KubeadmControlPlaneSpecMachineTemplateInfrastructureRef**](IoXK8sClusterControlplaneV1alpha4KubeadmControlPlaneSpecMachineTemplateInfrastructureRef.md) |  | 
**node_drain_timeout** | **str** | NodeDrainTimeout is the total amount of time that the controller will spend on draining a node. The default value is 0, meaning that the node can be drained without any time limitations. NOTE: NodeDrainTimeout is different from &#x60;kubectl drain --timeout&#x60; | [optional] 
**provider_id** | **str** | ProviderID is the identification ID of the machine provided by the provider. This field must match the provider ID as seen on the node object corresponding to this machine. This field is required by higher level consumers of cluster-api. Example use case is cluster autoscaler with cluster-api as provider. Clean-up logic in the autoscaler compares machines to nodes to find out machines at provider which could not get registered as Kubernetes nodes. With cluster-api as a generic out-of-tree provider for autoscaler, this field is required by autoscaler to be able to have a provider view of the list of machines. Another list of nodes is queried from the k8s apiserver and then a comparison is done to find out unregistered machines and are marked for delete. This field will be set by the actuators and consumed by higher level entities like autoscaler that will be interfacing with cluster-api as generic provider. | [optional] 
**version** | **str** | Version defines the desired Kubernetes version. This field is meant to be optionally used by bootstrap providers. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


