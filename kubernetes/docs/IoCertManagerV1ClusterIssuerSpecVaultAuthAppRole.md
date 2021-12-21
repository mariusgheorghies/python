# IoCertManagerV1ClusterIssuerSpecVaultAuthAppRole

AppRole authenticates with Vault using the App Role auth mechanism, with the role and secret stored in a Kubernetes Secret resource.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | Path where the App Role authentication backend is mounted in Vault, e.g: \&quot;approle\&quot; | 
**role_id** | **str** | RoleID configured in the App Role authentication backend when setting up the authentication backend in Vault. | 
**secret_ref** | [**IoCertManagerV1ClusterIssuerSpecVaultAuthAppRoleSecretRef**](IoCertManagerV1ClusterIssuerSpecVaultAuthAppRoleSecretRef.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


