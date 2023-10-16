# IoExternalSecretsV1beta1ClusterExternalSecretSpecExternalSecretSpecData

ExternalSecretData defines the connection between the Kubernetes Secret key (spec.data.<key>) and the Provider data.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**remote_ref** | [**IoExternalSecretsV1beta1ClusterExternalSecretSpecExternalSecretSpecRemoteRef**](IoExternalSecretsV1beta1ClusterExternalSecretSpecExternalSecretSpecRemoteRef.md) |  | 
**secret_key** | **str** | SecretKey defines the key in which the controller stores the value. This is the key in the Kind&#x3D;Secret | 
**source_ref** | [**IoExternalSecretsV1beta1ClusterExternalSecretSpecExternalSecretSpecSourceRef**](IoExternalSecretsV1beta1ClusterExternalSecretSpecExternalSecretSpecSourceRef.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


