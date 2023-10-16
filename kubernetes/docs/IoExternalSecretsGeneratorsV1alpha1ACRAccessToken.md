# IoExternalSecretsGeneratorsV1alpha1ACRAccessToken

ACRAccessToken returns a Azure Container Registry token that can be used for pushing/pulling images. Note: by default it will return an ACR Refresh Token with full access (depending on the identity). This can be scoped down to the repository level using .spec.scope. In case scope is defined it will return an ACR Access Token.   See docs: https://github.com/Azure/acr/blob/main/docs/AAD-OAuth.md
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the kubernetes.client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) |  | [optional] 
**spec** | [**IoExternalSecretsGeneratorsV1alpha1ACRAccessTokenSpec**](IoExternalSecretsGeneratorsV1alpha1ACRAccessTokenSpec.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

