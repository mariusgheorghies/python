# IoExternalSecretsGeneratorsV1alpha1ACRAccessTokenSpec

ACRAccessTokenSpec defines how to generate the access token e.g. how to authenticate and which registry to use. see: https://github.com/Azure/acr/blob/main/docs/AAD-OAuth.md#overview
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth** | [**IoExternalSecretsGeneratorsV1alpha1ACRAccessTokenSpecAuth**](IoExternalSecretsGeneratorsV1alpha1ACRAccessTokenSpecAuth.md) |  | 
**environment_type** | **str** | EnvironmentType specifies the Azure cloud environment endpoints to use for connecting and authenticating with Azure. By default it points to the public cloud AAD endpoint. The following endpoints are available, also see here: https://github.com/Azure/go-autorest/blob/main/autorest/azure/environments.go#L152 PublicCloud, USGovernmentCloud, ChinaCloud, GermanCloud | [optional] 
**registry** | **str** | the domain name of the ACR registry e.g. foobarexample.azurecr.io | 
**scope** | **str** | Define the scope for the access token, e.g. pull/push access for a repository. if not provided it will return a refresh token that has full scope. Note: you need to pin it down to the repository level, there is no wildcard available.   examples: repository:my-repository:pull,push repository:my-repository:pull   see docs for details: https://docs.docker.com/registry/spec/auth/scope/ | [optional] 
**tenant_id** | **str** | TenantID configures the Azure Tenant to send requests to. Required for ServicePrincipal auth type. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


