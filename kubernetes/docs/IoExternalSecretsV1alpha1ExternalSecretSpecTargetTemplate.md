# IoExternalSecretsV1alpha1ExternalSecretSpecTargetTemplate

Template defines a blueprint for the created Secret resource.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **dict(str, str)** |  | [optional] 
**engine_version** | **str** | EngineVersion specifies the template engine version that should be used to compile/execute the template specified in .data and .templateFrom[]. | [optional] 
**metadata** | [**IoExternalSecretsV1alpha1ExternalSecretSpecTargetTemplateMetadata**](IoExternalSecretsV1alpha1ExternalSecretSpecTargetTemplateMetadata.md) |  | [optional] 
**template_from** | [**list[IoExternalSecretsV1alpha1ExternalSecretSpecTargetTemplateTemplateFrom]**](IoExternalSecretsV1alpha1ExternalSecretSpecTargetTemplateTemplateFrom.md) |  | [optional] 
**type** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


