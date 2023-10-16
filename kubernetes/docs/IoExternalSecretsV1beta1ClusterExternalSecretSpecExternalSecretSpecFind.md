# IoExternalSecretsV1beta1ClusterExternalSecretSpecExternalSecretSpecFind

Used to find secrets based on tags or regular expressions Note: Find does not support sourceRef.Generator or sourceRef.GeneratorRef.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversion_strategy** | **str** | Used to define a conversion Strategy | [optional] 
**decoding_strategy** | **str** | Used to define a decoding Strategy | [optional] 
**name** | [**IoExternalSecretsV1beta1ClusterExternalSecretSpecExternalSecretSpecFindName**](IoExternalSecretsV1beta1ClusterExternalSecretSpecExternalSecretSpecFindName.md) |  | [optional] 
**path** | **str** | A root path to start the find operations. | [optional] 
**tags** | **dict(str, str)** | Find secrets based on tags. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


