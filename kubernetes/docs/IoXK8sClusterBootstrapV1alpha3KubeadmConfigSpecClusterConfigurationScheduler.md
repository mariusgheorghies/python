# IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecClusterConfigurationScheduler

Scheduler contains extra settings for the scheduler control plane component
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extra_args** | **dict(str, str)** | ExtraArgs is an extra set of flags to pass to the control plane component. TODO: This is temporary and ideally we would like to switch all components to use ComponentConfig + ConfigMaps. | [optional] 
**extra_volumes** | [**list[IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecClusterConfigurationApiServerExtraVolumes]**](IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecClusterConfigurationApiServerExtraVolumes.md) | ExtraVolumes is an extra set of host volumes, mounted to the control plane component. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


