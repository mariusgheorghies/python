# IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderAws

AWS configures this store to sync secrets using AWS Secret Manager provider
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth** | [**IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderAwsAuth**](IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderAwsAuth.md) |  | [optional] 
**region** | **str** | AWS Region to be used for the provider | 
**role** | **str** | Role is a Role ARN which the SecretManager provider will assume | [optional] 
**service** | **str** | Service defines which service should be used to fetch the secrets | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


