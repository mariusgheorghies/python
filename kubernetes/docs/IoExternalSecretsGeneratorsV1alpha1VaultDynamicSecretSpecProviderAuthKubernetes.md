# IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderAuthKubernetes

Kubernetes authenticates with Vault by passing the ServiceAccount token stored in the named Secret resource to the Vault server.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mount_path** | **str** | Path where the Kubernetes authentication backend is mounted in Vault, e.g: \&quot;kubernetes\&quot; | 
**role** | **str** | A required field containing the Vault Role to assume. A Role binds a Kubernetes ServiceAccount with a set of Vault policies. | 
**secret_ref** | [**IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderAuthKubernetesSecretRef**](IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderAuthKubernetesSecretRef.md) |  | [optional] 
**service_account_ref** | [**IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderAuthKubernetesServiceAccountRef**](IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderAuthKubernetesServiceAccountRef.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


