# IoXK8sClusterBootstrapV1alpha4KubeadmConfigSpecInitConfiguration

InitConfiguration along with ClusterConfiguration are the configurations necessary for the init command
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**bootstrap_tokens** | [**list[IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecInitConfigurationBootstrapTokens]**](IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecInitConfigurationBootstrapTokens.md) | BootstrapTokens is respected at &#x60;kubeadm init&#x60; time and describes a set of Bootstrap Tokens to create. This information IS NOT uploaded to the kubeadm cluster configmap, partly because of its sensitive nature | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the kubernetes.client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**local_api_endpoint** | [**IoXK8sClusterBootstrapV1alpha4KubeadmConfigSpecInitConfigurationLocalAPIEndpoint**](IoXK8sClusterBootstrapV1alpha4KubeadmConfigSpecInitConfigurationLocalAPIEndpoint.md) |  | [optional] 
**node_registration** | [**IoXK8sClusterBootstrapV1alpha4KubeadmConfigSpecInitConfigurationNodeRegistration**](IoXK8sClusterBootstrapV1alpha4KubeadmConfigSpecInitConfigurationNodeRegistration.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


