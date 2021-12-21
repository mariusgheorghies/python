# IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecClusterConfigurationApiServer

APIServer contains extra settings for the API server control plane component
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cert_sa_ns** | **list[str]** | CertSANs sets extra Subject Alternative Names for the API Server signing cert. | [optional] 
**extra_args** | **dict(str, str)** | ExtraArgs is an extra set of flags to pass to the control plane component. TODO: This is temporary and ideally we would like to switch all components to use ComponentConfig + ConfigMaps. | [optional] 
**extra_volumes** | [**list[IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecClusterConfigurationApiServerExtraVolumes]**](IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecClusterConfigurationApiServerExtraVolumes.md) | ExtraVolumes is an extra set of host volumes, mounted to the control plane component. | [optional] 
**timeout_for_control_plane** | **str** | TimeoutForControlPlane controls the timeout that we use for API server to appear | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


