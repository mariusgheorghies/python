# IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecJoinConfigurationDiscovery

Discovery specifies the options for the kubelet to use during the TLS Bootstrap process TODO: revisit when there is defaulting from k/k
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bootstrap_token** | [**IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecJoinConfigurationDiscoveryBootstrapToken**](IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecJoinConfigurationDiscoveryBootstrapToken.md) |  | [optional] 
**file** | [**IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecJoinConfigurationDiscoveryFile**](IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecJoinConfigurationDiscoveryFile.md) |  | [optional] 
**timeout** | **str** | Timeout modifies the discovery timeout | [optional] 
**tls_bootstrap_token** | **str** | TLSBootstrapToken is a token used for TLS bootstrapping. If .BootstrapToken is set, this field is defaulted to .BootstrapToken.Token, but can be overridden. If .File is set, this field **must be set** in case the KubeConfigFile does not contain any other authentication information TODO: revisit when there is defaulting from k/k | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


