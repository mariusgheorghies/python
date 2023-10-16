# IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderKubernetesServerCaProvider

see: https://external-secrets.io/v0.4.1/spec/#external-secrets.io/v1alpha1.CAProvider
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The key where the CA certificate can be found in the Secret or ConfigMap. | [optional] 
**name** | **str** | The name of the object located at the provider type. | 
**namespace** | **str** | The namespace the Provider type is in. Can only be defined when used in a ClusterSecretStore. | [optional] 
**type** | **str** | The type of provider to use such as \&quot;Secret\&quot;, or \&quot;ConfigMap\&quot;. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


