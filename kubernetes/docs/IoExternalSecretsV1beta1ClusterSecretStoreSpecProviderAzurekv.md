# IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderAzurekv

AzureKV configures this store to sync secrets using Azure Key Vault provider
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_secret_ref** | [**IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderAzurekvAuthSecretRef**](IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderAzurekvAuthSecretRef.md) |  | [optional] 
**auth_type** | **str** | Auth type defines how to authenticate to the keyvault service. Valid values are: - \&quot;ServicePrincipal\&quot; (default): Using a service principal (tenantId, kubernetes.clientId, kubernetes.clientSecret) - \&quot;ManagedIdentity\&quot;: Using Managed Identity assigned to the pod (see aad-pod-identity) | [optional] 
**environment_type** | **str** | EnvironmentType specifies the Azure cloud environment endpoints to use for connecting and authenticating with Azure. By default it points to the public cloud AAD endpoint. The following endpoints are available, also see here: https://github.com/Azure/go-autorest/blob/main/autorest/azure/environments.go#L152 PublicCloud, USGovernmentCloud, ChinaCloud, GermanCloud | [optional] 
**identity_id** | **str** | If multiple Managed Identity is assigned to the pod, you can select the one to be used | [optional] 
**service_account_ref** | [**IoExternalSecretsGeneratorsV1alpha1ACRAccessTokenSpecAuthWorkloadIdentityServiceAccountRef**](IoExternalSecretsGeneratorsV1alpha1ACRAccessTokenSpecAuthWorkloadIdentityServiceAccountRef.md) |  | [optional] 
**tenant_id** | **str** | TenantID configures the Azure Tenant to send requests to. Required for ServicePrincipal auth type. | [optional] 
**vault_url** | **str** | Vault Url from which the secrets to be fetched from. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


