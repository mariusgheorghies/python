# IoExternalSecretsV1beta1ClusterExternalSecretStatus

ClusterExternalSecretStatus defines the observed state of ClusterExternalSecret.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | [**list[IoExternalSecretsV1beta1ClusterExternalSecretStatusConditions]**](IoExternalSecretsV1beta1ClusterExternalSecretStatusConditions.md) |  | [optional] 
**failed_namespaces** | [**list[IoExternalSecretsV1beta1ClusterExternalSecretStatusFailedNamespaces]**](IoExternalSecretsV1beta1ClusterExternalSecretStatusFailedNamespaces.md) | Failed namespaces are the namespaces that failed to apply an ExternalSecret | [optional] 
**provisioned_namespaces** | **list[str]** | ProvisionedNamespaces are the namespaces where the ClusterExternalSecret has secrets | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


