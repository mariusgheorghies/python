# IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderAkeyless

Akeyless configures this store to sync secrets using Akeyless Vault provider
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**akeyless_gw_api_url** | **str** | Akeyless GW API Url from which the secrets to be fetched from. | 
**auth_secret_ref** | [**IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderAkeylessAuthSecretRef**](IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderAkeylessAuthSecretRef.md) |  | 
**ca_bundle** | **str** | PEM/base64 encoded CA bundle used to validate Akeyless Gateway certificate. Only used if the AkeylessGWApiURL URL is using HTTPS protocol. If not set the system root certificates are used to validate the TLS connection. | [optional] 
**ca_provider** | [**IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderAkeylessCaProvider**](IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderAkeylessCaProvider.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


