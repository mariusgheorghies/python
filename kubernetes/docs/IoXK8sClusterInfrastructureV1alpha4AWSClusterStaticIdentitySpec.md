# IoXK8sClusterInfrastructureV1alpha4AWSClusterStaticIdentitySpec

Spec for this AWSClusterStaticIdentity
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_namespaces** | [**object**](.md) | AllowedNamespaces is used to identify which namespaces are allowed to use the identity from. Namespaces can be selected either using an array of namespaces or with label selector. An empty allowedNamespaces object indicates that AWSClusters can use this identity from any namespace. If this object is nil, no namespaces will be allowed (default behaviour, if this field is not provided) A namespace should be either in the NamespaceList or match with Selector to use the identity. | [optional] 
**secret_ref** | **str** | Reference to a secret containing the credentials. The secret should contain the following data keys:  AccessKeyID: AKIAIOSFODNN7EXAMPLE  SecretAccessKey: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY  SessionToken: Optional | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


