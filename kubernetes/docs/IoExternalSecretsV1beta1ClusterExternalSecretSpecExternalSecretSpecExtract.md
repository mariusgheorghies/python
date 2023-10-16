# IoExternalSecretsV1beta1ClusterExternalSecretSpecExternalSecretSpecExtract

Used to extract multiple key/value pairs from one secret Note: Extract does not support sourceRef.Generator or sourceRef.GeneratorRef.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversion_strategy** | **str** | Used to define a conversion Strategy | [optional] 
**decoding_strategy** | **str** | Used to define a decoding Strategy | [optional] 
**key** | **str** | Key is the key used in the Provider, mandatory | 
**metadata_policy** | **str** | Policy for fetching tags/labels from provider secrets, possible options are Fetch, None. Defaults to None | [optional] 
**_property** | **str** | Used to select a specific property of the Provider value (if a map), if supported | [optional] 
**version** | **str** | Used to select a specific version of the Provider value, if supported | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


