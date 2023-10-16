# IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderAuthJwt

Jwt authenticates with Vault by passing role and JWT token using the JWT/OIDC authentication method
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kubernetes_service_account_token** | [**IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderAuthJwtKubernetesServiceAccountToken**](IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderAuthJwtKubernetesServiceAccountToken.md) |  | [optional] 
**path** | **str** | Path where the JWT authentication backend is mounted in Vault, e.g: \&quot;jwt\&quot; | 
**role** | **str** | Role is a JWT role to authenticate using the JWT/OIDC Vault authentication method | [optional] 
**secret_ref** | [**IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderAuthJwtSecretRef**](IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderAuthJwtSecretRef.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


