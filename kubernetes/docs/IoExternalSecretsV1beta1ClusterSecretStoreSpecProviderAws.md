# IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderAws

AWS configures this store to sync secrets using AWS Secret Manager provider
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_roles** | **list[str]** | AdditionalRoles is a chained list of Role ARNs which the SecretManager provider will sequentially assume before assuming Role | [optional] 
**auth** | [**IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderAwsAuth**](IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderAwsAuth.md) |  | [optional] 
**region** | **str** | AWS Region to be used for the provider | 
**role** | **str** | Role is a Role ARN which the SecretManager provider will assume | [optional] 
**service** | **str** | Service defines which service should be used to fetch the secrets | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


