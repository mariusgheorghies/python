# IoExternalSecretsV1alpha1ClusterSecretStoreSpec

SecretStoreSpec defines the desired state of SecretStore.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**controller** | **str** | Used to select the correct KES controller (think: ingress.ingressClassName) The KES controller is instantiated with a specific controller name and filters ES based on this property | [optional] 
**provider** | [**IoExternalSecretsV1alpha1ClusterSecretStoreSpecProvider**](IoExternalSecretsV1alpha1ClusterSecretStoreSpecProvider.md) |  | 
**retry_settings** | [**IoExternalSecretsV1alpha1ClusterSecretStoreSpecRetrySettings**](IoExternalSecretsV1alpha1ClusterSecretStoreSpecRetrySettings.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


