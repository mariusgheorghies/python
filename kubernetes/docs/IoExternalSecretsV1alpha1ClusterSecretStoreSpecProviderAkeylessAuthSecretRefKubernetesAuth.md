# IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderAkeylessAuthSecretRefKubernetesAuth

Kubernetes authenticates with Akeyless by passing the ServiceAccount token stored in the named Secret resource.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_id** | **str** | the Akeyless Kubernetes auth-method access-id | 
**k8s_conf_name** | **str** | Kubernetes-auth configuration name in Akeyless-Gateway | 
**secret_ref** | [**IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderAkeylessAuthSecretRefKubernetesAuthSecretRef**](IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderAkeylessAuthSecretRefKubernetesAuthSecretRef.md) |  | [optional] 
**service_account_ref** | [**IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderAkeylessAuthSecretRefKubernetesAuthServiceAccountRef**](IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderAkeylessAuthSecretRefKubernetesAuthServiceAccountRef.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


