# IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderAuthAppRoleSecretRef

Reference to a key in a Secret that contains the App Role secret used to authenticate with Vault. The `key` field must be specified and denotes which entry within the Secret resource is used as the app role secret.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The key of the entry in the Secret resource&#39;s &#x60;data&#x60; field to be used. Some instances of this field may be defaulted, in others it may be required. | [optional] 
**name** | **str** | The name of the Secret resource being referred to. | [optional] 
**namespace** | **str** | Namespace of the resource being referred to. Ignored if referent is not cluster-scoped. cluster-scoped defaults to the namespace of the referent. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


