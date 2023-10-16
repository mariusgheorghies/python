# IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderWebhook

Webhook configures this store to sync secrets using a generic templated webhook
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** | Body | [optional] 
**ca_bundle** | **str** | PEM encoded CA bundle used to validate webhook server certificate. Only used if the Server URL is using HTTPS protocol. This parameter is ignored for plain HTTP protocol connection. If not set the system root certificates are used to validate the TLS connection. | [optional] 
**ca_provider** | [**IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderWebhookCaProvider**](IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderWebhookCaProvider.md) |  | [optional] 
**headers** | **dict(str, str)** | Headers | [optional] 
**method** | **str** | Webhook Method | [optional] 
**result** | [**IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderWebhookResult**](IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderWebhookResult.md) |  | 
**secrets** | [**list[IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderWebhookSecrets]**](IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderWebhookSecrets.md) | Secrets to fill in templates These secrets will be passed to the templating function as key value pairs under the given name | [optional] 
**timeout** | **str** | Timeout | [optional] 
**url** | **str** | Webhook url to call | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


