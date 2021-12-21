# IoXK8sClusterInfrastructureV1alpha4AWSClusterRoleIdentitySpec

Spec for this AWSClusterRoleIdentity.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_namespaces** | [**object**](.md) | AllowedNamespaces is used to identify which namespaces are allowed to use the identity from. Namespaces can be selected either using an array of namespaces or with label selector. An empty allowedNamespaces object indicates that AWSClusters can use this identity from any namespace. If this object is nil, no namespaces will be allowed (default behaviour, if this field is not provided) A namespace should be either in the NamespaceList or match with Selector to use the identity. | [optional] 
**duration_seconds** | **int** | The duration, in seconds, of the role session before it is renewed. | [optional] 
**external_id** | **str** | A unique identifier that might be required when you assume a role in another account. If the administrator of the account to which the role belongs provided you with an external ID, then provide that value in the ExternalId parameter. This value can be any string, such as a passphrase or account number. A cross-account role is usually set up to trust everyone in an account. Therefore, the administrator of the trusting account might send an external ID to the administrator of the trusted account. That way, only someone with the ID can assume the role, rather than everyone in the account. For more information about the external ID, see How to Use an External ID When Granting Access to Your AWS Resources to a Third Party in the IAM User Guide. | [optional] 
**inline_policy** | **str** | An IAM policy as a JSON-encoded string that you want to use as an inline session policy. | [optional] 
**policy_ar_ns** | **list[str]** | The Amazon Resource Names (ARNs) of the IAM managed policies that you want to use as managed session policies. The policies must exist in the same account as the role. | [optional] 
**role_arn** | **str** | The Amazon Resource Name (ARN) of the role to assume. | 
**session_name** | **str** | An identifier for the assumed role session | [optional] 
**source_identity_ref** | [**IoXK8sClusterInfrastructureV1alpha3AWSClusterRoleIdentitySpecSourceIdentityRef**](IoXK8sClusterInfrastructureV1alpha3AWSClusterRoleIdentitySpecSourceIdentityRef.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


