# IoArgoprojV1alpha1ApplicationOperationSyncSourceHelm

Helm holds helm specific options
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_parameters** | [**list[IoArgoprojV1alpha1ApplicationOperationSyncSourceHelmFileParameters]**](IoArgoprojV1alpha1ApplicationOperationSyncSourceHelmFileParameters.md) | FileParameters are file parameters to the helm template | [optional] 
**ignore_missing_value_files** | **bool** | IgnoreMissingValueFiles prevents helm template from failing when valueFiles do not exist locally by not appending them to helm template --values | [optional] 
**parameters** | [**list[IoArgoprojV1alpha1ApplicationOperationSyncSourceHelmParameters]**](IoArgoprojV1alpha1ApplicationOperationSyncSourceHelmParameters.md) | Parameters is a list of Helm parameters which are passed to the helm template command upon manifest generation | [optional] 
**pass_credentials** | **bool** | PassCredentials pass credentials to all domains (Helm&#39;s --pass-credentials) | [optional] 
**release_name** | **str** | ReleaseName is the Helm release name to use. If omitted it will use the application name | [optional] 
**skip_crds** | **bool** | SkipCrds skips custom resource definition installation step (Helm&#39;s --skip-crds) | [optional] 
**value_files** | **list[str]** | ValuesFiles is a list of Helm value files to use when generating a template | [optional] 
**values** | **str** | Values specifies Helm values to be passed to helm template, typically defined as a block | [optional] 
**version** | **str** | Version is the Helm version to use for templating (\&quot;3\&quot;) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


