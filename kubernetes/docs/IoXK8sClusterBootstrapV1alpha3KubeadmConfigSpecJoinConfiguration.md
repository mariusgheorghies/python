# IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecJoinConfiguration

JoinConfiguration is the kubeadm configuration for the join command
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**ca_cert_path** | **str** | CACertPath is the path to the SSL certificate authority used to secure comunications between node and control-plane. Defaults to \&quot;/etc/kubernetes/pki/ca.crt\&quot;. TODO: revisit when there is defaulting from k/k | [optional] 
**control_plane** | [**IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecJoinConfigurationControlPlane**](IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecJoinConfigurationControlPlane.md) |  | [optional] 
**discovery** | [**IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecJoinConfigurationDiscovery**](IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecJoinConfigurationDiscovery.md) |  | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the kubernetes.client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**node_registration** | [**IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecInitConfigurationNodeRegistration**](IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecInitConfigurationNodeRegistration.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


