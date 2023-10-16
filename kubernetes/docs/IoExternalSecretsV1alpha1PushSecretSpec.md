# IoExternalSecretsV1alpha1PushSecretSpec

PushSecretSpec configures the behavior of the PushSecret.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**list[IoExternalSecretsV1alpha1PushSecretSpecData]**](IoExternalSecretsV1alpha1PushSecretSpecData.md) | Secret Data that should be pushed to providers | [optional] 
**deletion_policy** | **str** | Deletion Policy to handle Secrets in the provider. Possible Values: \&quot;Delete/None\&quot;. Defaults to \&quot;None\&quot;. | [optional] 
**refresh_interval** | **str** | The Interval to which External Secrets will try to push a secret definition | [optional] 
**secret_store_refs** | [**list[IoExternalSecretsV1alpha1PushSecretSpecSecretStoreRefs]**](IoExternalSecretsV1alpha1PushSecretSpecSecretStoreRefs.md) |  | 
**selector** | [**IoExternalSecretsV1alpha1PushSecretSpecSelector**](IoExternalSecretsV1alpha1PushSecretSpecSelector.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


