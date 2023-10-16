# IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderVaultAuthJwtKubernetesServiceAccountToken

Optional ServiceAccountToken specifies the Kubernetes service account for which to request a token for with the `TokenRequest` API.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audiences** | **list[str]** | Optional audiences field that will be used to request a temporary Kubernetes service account token for the service account referenced by &#x60;serviceAccountRef&#x60;. Defaults to a single audience &#x60;vault&#x60; it not specified. | [optional] 
**expiration_seconds** | **int** | Optional expiration time in seconds that will be used to request a temporary Kubernetes service account token for the service account referenced by &#x60;serviceAccountRef&#x60;. Defaults to 10 minutes. | [optional] 
**service_account_ref** | [**IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderAuthJwtKubernetesServiceAccountTokenServiceAccountRef**](IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderAuthJwtKubernetesServiceAccountTokenServiceAccountRef.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


