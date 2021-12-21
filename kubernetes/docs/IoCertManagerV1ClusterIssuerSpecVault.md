# IoCertManagerV1ClusterIssuerSpecVault

Vault configures this issuer to sign certificates using a HashiCorp Vault PKI backend.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth** | [**IoCertManagerV1ClusterIssuerSpecVaultAuth**](IoCertManagerV1ClusterIssuerSpecVaultAuth.md) |  | 
**ca_bundle** | **str** | PEM-encoded CA bundle (base64-encoded) used to validate Vault server certificate. Only used if the Server URL is using HTTPS protocol. This parameter is ignored for plain HTTP protocol connection. If not set the system root certificates are used to validate the TLS connection. | [optional] 
**namespace** | **str** | Name of the vault namespace. Namespaces is a set of features within Vault Enterprise that allows Vault environments to support Secure Multi-tenancy. e.g: \&quot;ns1\&quot; More about namespaces can be found here https://www.vaultproject.io/docs/enterprise/namespaces | [optional] 
**path** | **str** | Path is the mount path of the Vault PKI backend&#39;s &#x60;sign&#x60; endpoint, e.g: \&quot;my_pki_mount/sign/my-role-name\&quot;. | 
**server** | **str** | Server is the connection address for the Vault server, e.g: \&quot;https://vault.example.com:8200\&quot;. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


