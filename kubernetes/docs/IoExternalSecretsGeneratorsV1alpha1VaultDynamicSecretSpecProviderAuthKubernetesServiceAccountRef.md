# IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderAuthKubernetesServiceAccountRef

Optional service account field containing the name of a kubernetes ServiceAccount. If the service account is specified, the service account secret token JWT will be used for authenticating with Vault. If the service account selector is not supplied, the secretRef will be used instead.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audiences** | **list[str]** | Audience specifies the &#x60;aud&#x60; claim for the service account token If the service account uses a well-known annotation for e.g. IRSA or GCP Workload Identity then this audiences will be appended to the list | [optional] 
**name** | **str** | The name of the ServiceAccount resource being referred to. | 
**namespace** | **str** | Namespace of the resource being referred to. Ignored if referent is not cluster-scoped. cluster-scoped defaults to the namespace of the referent. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


