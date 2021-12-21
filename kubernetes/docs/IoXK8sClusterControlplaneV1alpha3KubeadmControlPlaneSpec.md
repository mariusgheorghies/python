# IoXK8sClusterControlplaneV1alpha3KubeadmControlPlaneSpec

KubeadmControlPlaneSpec defines the desired state of KubeadmControlPlane.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**infrastructure_template** | [**IoXK8sClusterControlplaneV1alpha3KubeadmControlPlaneSpecInfrastructureTemplate**](IoXK8sClusterControlplaneV1alpha3KubeadmControlPlaneSpecInfrastructureTemplate.md) |  | 
**kubeadm_config_spec** | [**IoXK8sClusterControlplaneV1alpha3KubeadmControlPlaneSpecKubeadmConfigSpec**](IoXK8sClusterControlplaneV1alpha3KubeadmControlPlaneSpecKubeadmConfigSpec.md) |  | 
**node_drain_timeout** | **str** | NodeDrainTimeout is the total amount of time that the controller will spend on draining a controlplane node The default value is 0, meaning that the node can be drained without any time limitations. NOTE: NodeDrainTimeout is different from &#x60;kubectl drain --timeout&#x60; | [optional] 
**replicas** | **int** | Number of desired machines. Defaults to 1. When stacked etcd is used only odd numbers are permitted, as per [etcd best practice](https://etcd.io/docs/v3.3.12/faq/#why-an-odd-number-of-cluster-members). This is a pointer to distinguish between explicit zero and not specified. | [optional] 
**rollout_strategy** | [**IoXK8sClusterControlplaneV1alpha3KubeadmControlPlaneSpecRolloutStrategy**](IoXK8sClusterControlplaneV1alpha3KubeadmControlPlaneSpecRolloutStrategy.md) |  | [optional] 
**upgrade_after** | **datetime** | UpgradeAfter is a field to indicate an upgrade should be performed after the specified time even if no changes have been made to the KubeadmControlPlane | [optional] 
**version** | **str** | Version defines the desired Kubernetes version. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


