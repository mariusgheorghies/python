# IoExternalSecretsV1alpha1ExternalSecretSpecTarget

ExternalSecretTarget defines the Kubernetes Secret to be created There can be only one target per ExternalSecret.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creation_policy** | **str** | CreationPolicy defines rules on how to create the resulting Secret Defaults to &#39;Owner&#39; | [optional] 
**immutable** | **bool** | Immutable defines if the final secret will be immutable | [optional] 
**name** | **str** | Name defines the name of the Secret resource to be managed This field is immutable Defaults to the .metadata.name of the ExternalSecret resource | [optional] 
**template** | [**IoExternalSecretsV1alpha1ExternalSecretSpecTargetTemplate**](IoExternalSecretsV1alpha1ExternalSecretSpecTargetTemplate.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


