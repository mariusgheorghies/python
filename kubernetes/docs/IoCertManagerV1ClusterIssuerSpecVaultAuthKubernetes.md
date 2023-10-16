# IoCertManagerV1ClusterIssuerSpecVaultAuthKubernetes

Kubernetes authenticates with Vault by passing the ServiceAccount token stored in the named Secret resource to the Vault server.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mount_path** | **str** | The Vault mountPath here is the mount path to use when authenticating with Vault. For example, setting a value to &#x60;/v1/auth/foo&#x60;, will use the path &#x60;/v1/auth/foo/login&#x60; to authenticate with Vault. If unspecified, the default value \&quot;/v1/auth/kubernetes\&quot; will be used. | [optional] 
**role** | **str** | A required field containing the Vault Role to assume. A Role binds a Kubernetes ServiceAccount with a set of Vault policies. | 
**secret_ref** | [**IoCertManagerV1ClusterIssuerSpecVaultAuthKubernetesSecretRef**](IoCertManagerV1ClusterIssuerSpecVaultAuthKubernetesSecretRef.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


