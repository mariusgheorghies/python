# IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderOracleAuth

Auth configures how secret-manager authenticates with the Oracle Vault. If empty, use the instance principal, otherwise the user credentials specified in Auth.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secret_ref** | [**IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderOracleAuthSecretRef**](IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderOracleAuthSecretRef.md) |  | 
**tenancy** | **str** | Tenancy is the tenancy OCID where user is located. | 
**user** | **str** | User is an access OCID specific to the account. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


