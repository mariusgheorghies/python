# IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneSpecOidcIdentityProviderConfig

IdentityProviderconfig is used to specify the oidc provider config to be attached with this eks cluster
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kubernetes.client_id** | **str** | This is also known as audience. The ID for the kubernetes.client application that makes authentication requests to the OpenID identity provider. | [optional] 
**groups_claim** | **str** | The JWT claim that the provider uses to return your groups. | [optional] 
**groups_prefix** | **str** | The prefix that is prepended to group claims to prevent clashes with existing names (such as system: groups). For example, the valueoidc: will create group names like oidc:engineering and oidc:infra. | [optional] 
**identity_provider_config_name** | **str** | The name of the OIDC provider configuration.   IdentityProviderConfigName is a required field | [optional] 
**issuer_url** | **str** | The URL of the OpenID identity provider that allows the API server to discover public signing keys for verifying tokens. The URL must begin with https:// and should correspond to the iss claim in the provider&#39;s OIDC ID tokens. Per the OIDC standard, path components are allowed but query parameters are not. Typically the URL consists of only a hostname, like https://server.example.org or https://example.com. This URL should point to the level below .well-known/openid-configuration and must be publicly accessible over the internet. | [optional] 
**required_claims** | **dict(str, str)** | The key value pairs that describe required claims in the identity token. If set, each claim is verified to be present in the token with a matching value. For the maximum number of claims that you can require, see Amazon EKS service quotas (https://docs.aws.amazon.com/eks/latest/userguide/service-quotas.html) in the Amazon EKS User Guide. | [optional] 
**tags** | **dict(str, str)** | tags to apply to oidc identity provider association | [optional] 
**username_claim** | **str** | The JSON Web Token (JWT) claim to use as the username. The default is sub, which is expected to be a unique identifier of the end user. You can choose other claims, such as email or name, depending on the OpenID identity provider. Claims other than email are prefixed with the issuer URL to prevent naming clashes with other plug-ins. | [optional] 
**username_prefix** | **str** | The prefix that is prepended to username claims to prevent clashes with existing names. If you do not provide this field, and username is a value other than email, the prefix defaults to issuerurl#. You can use the value - to disable all prefixing. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


