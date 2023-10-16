# IoExternalSecretsV1beta1ExternalSecretSpec

ExternalSecretSpec defines the desired state of ExternalSecret.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**list[IoExternalSecretsV1beta1ClusterExternalSecretSpecExternalSecretSpecData]**](IoExternalSecretsV1beta1ClusterExternalSecretSpecExternalSecretSpecData.md) | Data defines the connection between the Kubernetes Secret keys and the Provider data | [optional] 
**data_from** | [**list[IoExternalSecretsV1beta1ClusterExternalSecretSpecExternalSecretSpecDataFrom]**](IoExternalSecretsV1beta1ClusterExternalSecretSpecExternalSecretSpecDataFrom.md) | DataFrom is used to fetch all properties from a specific Provider data If multiple entries are specified, the Secret keys are merged in the specified order | [optional] 
**refresh_interval** | **str** | RefreshInterval is the amount of time before the values are read again from the SecretStore provider Valid time units are \&quot;ns\&quot;, \&quot;us\&quot; (or \&quot;µs\&quot;), \&quot;ms\&quot;, \&quot;s\&quot;, \&quot;m\&quot;, \&quot;h\&quot; May be set to zero to fetch and create it once. Defaults to 1h. | [optional] 
**secret_store_ref** | [**IoExternalSecretsV1alpha1ExternalSecretSpecSecretStoreRef**](IoExternalSecretsV1alpha1ExternalSecretSpecSecretStoreRef.md) |  | [optional] 
**target** | [**IoExternalSecretsV1beta1ClusterExternalSecretSpecExternalSecretSpecTarget**](IoExternalSecretsV1beta1ClusterExternalSecretSpecExternalSecretSpecTarget.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


