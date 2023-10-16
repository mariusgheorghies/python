# IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderVault

Vault configures this store to sync secrets using Hashi provider
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth** | [**IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderVaultAuth**](IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderVaultAuth.md) |  | 
**ca_bundle** | **str** | PEM encoded CA bundle used to validate Vault server certificate. Only used if the Server URL is using HTTPS protocol. This parameter is ignored for plain HTTP protocol connection. If not set the system root certificates are used to validate the TLS connection. | [optional] 
**ca_provider** | [**IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderVaultCaProvider**](IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderVaultCaProvider.md) |  | [optional] 
**forward_inconsistent** | **bool** | ForwardInconsistent tells Vault to forward read-after-write requests to the Vault leader instead of simply retrying within a loop. This can increase performance if the option is enabled serverside. https://www.vaultproject.io/docs/configuration/replication#allow_forwarding_via_header | [optional] 
**namespace** | **str** | Name of the vault namespace. Namespaces is a set of features within Vault Enterprise that allows Vault environments to support Secure Multi-tenancy. e.g: \&quot;ns1\&quot;. More about namespaces can be found here https://www.vaultproject.io/docs/enterprise/namespaces | [optional] 
**path** | **str** | Path is the mount path of the Vault KV backend endpoint, e.g: \&quot;secret\&quot;. The v2 KV secret engine version specific \&quot;/data\&quot; path suffix for fetching secrets from Vault is optional and will be appended if not present in specified path. | [optional] 
**read_your_writes** | **bool** | ReadYourWrites ensures isolated read-after-write semantics by providing discovered cluster replication states in each request. More information about eventual consistency in Vault can be found here https://www.vaultproject.io/docs/enterprise/consistency | [optional] 
**server** | **str** | Server is the connection address for the Vault server, e.g: \&quot;https://vault.example.com:8200\&quot;. | 
**version** | **str** | Version is the Vault KV secret engine version. This can be either \&quot;v1\&quot; or \&quot;v2\&quot;. Version defaults to \&quot;v2\&quot;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


