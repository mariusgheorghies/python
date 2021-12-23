# IoXK8sClusterControlplaneV1alpha4KubeadmControlPlaneSpec

KubeadmControlPlaneSpec defines the desired state of KubeadmControlPlane.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kubeadm_config_spec** | [**IoXK8sClusterControlplaneV1alpha4KubeadmControlPlaneSpecKubeadmConfigSpec**](IoXK8sClusterControlplaneV1alpha4KubeadmControlPlaneSpecKubeadmConfigSpec.md) |  | 
**machine_template** | [**IoXK8sClusterControlplaneV1alpha4KubeadmControlPlaneSpecMachineTemplate**](IoXK8sClusterControlplaneV1alpha4KubeadmControlPlaneSpecMachineTemplate.md) |  | 
**replicas** | **int** | Number of desired machines. Defaults to 1. When stacked etcd is used only odd numbers are permitted, as per [etcd best practice](https://etcd.io/docs/v3.3.12/faq/#why-an-odd-number-of-cluster-members). This is a pointer to distinguish between explicit zero and not specified. | [optional] 
**rollout_after** | **datetime** | RolloutAfter is a field to indicate a rollout should be performed after the specified time even if no changes have been made to the KubeadmControlPlane. | [optional] 
**rollout_strategy** | [**IoXK8sClusterControlplaneV1alpha3KubeadmControlPlaneSpecRolloutStrategy**](IoXK8sClusterControlplaneV1alpha3KubeadmControlPlaneSpecRolloutStrategy.md) |  | [optional] 
**version** | **str** | Version defines the desired Kubernetes version. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


