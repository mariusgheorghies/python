# IoExternalSecretsV1beta1ClusterExternalSecretSpec

ClusterExternalSecretSpec defines the desired state of ClusterExternalSecret.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_secret_name** | **str** | The name of the external secrets to be created defaults to the name of the ClusterExternalSecret | [optional] 
**external_secret_spec** | [**IoExternalSecretsV1beta1ClusterExternalSecretSpecExternalSecretSpec**](IoExternalSecretsV1beta1ClusterExternalSecretSpecExternalSecretSpec.md) |  | 
**namespace_selector** | [**IoExternalSecretsV1beta1ClusterExternalSecretSpecNamespaceSelector**](IoExternalSecretsV1beta1ClusterExternalSecretSpecNamespaceSelector.md) |  | 
**refresh_time** | **str** | The time in which the controller should reconcile it&#39;s objects and recheck namespaces for labels. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


