# IoExternalSecretsV1beta1ClusterSecretStoreSpec

SecretStoreSpec defines the desired state of SecretStore.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | [**list[IoExternalSecretsV1beta1ClusterSecretStoreSpecConditions]**](IoExternalSecretsV1beta1ClusterSecretStoreSpecConditions.md) | Used to constraint a ClusterSecretStore to specific namespaces. Relevant only to ClusterSecretStore | [optional] 
**controller** | **str** | Used to select the correct KES controller (think: ingress.ingressClassName) The KES controller is instantiated with a specific controller name and filters ES based on this property | [optional] 
**provider** | [**IoExternalSecretsV1beta1ClusterSecretStoreSpecProvider**](IoExternalSecretsV1beta1ClusterSecretStoreSpecProvider.md) |  | 
**refresh_interval** | **int** | Used to configure store refresh interval in seconds. Empty or 0 will default to the controller config. | [optional] 
**retry_settings** | [**IoExternalSecretsV1alpha1ClusterSecretStoreSpecRetrySettings**](IoExternalSecretsV1alpha1ClusterSecretStoreSpecRetrySettings.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


