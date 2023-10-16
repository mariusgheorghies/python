# IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderDoppler

Doppler configures this store to sync secrets using the Doppler provider
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth** | [**IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderDopplerAuth**](IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderDopplerAuth.md) |  | 
**config** | **str** | Doppler config (required if not using a Service Token) | [optional] 
**format** | **str** | Format enables the downloading of secrets as a file (string) | [optional] 
**name_transformer** | **str** | Environment variable compatible name transforms that change secret names to a different format | [optional] 
**project** | **str** | Doppler project (required if not using a Service Token) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


