# IoExternalSecretsV1beta1ClusterExternalSecretSpecExternalSecretSpecSourceRef1

SourceRef points to a store or generator which contains secret values ready to use. Use this in combination with Extract or Find pull values out of a specific SecretStore. When sourceRef points to a generator Extract or Find is not supported. The generator returns a static map of values
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**generator_ref** | [**IoExternalSecretsV1beta1ClusterExternalSecretSpecExternalSecretSpecSourceRefGeneratorRef**](IoExternalSecretsV1beta1ClusterExternalSecretSpecExternalSecretSpecSourceRefGeneratorRef.md) |  | [optional] 
**store_ref** | [**IoExternalSecretsV1alpha1ExternalSecretSpecSecretStoreRef**](IoExternalSecretsV1alpha1ExternalSecretSpecSecretStoreRef.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


