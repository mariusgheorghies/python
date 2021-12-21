# IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneSpecIamAuthenticatorConfig

IAMAuthenticatorConfig allows the specification of any additional user or role mappings for use when generating the aws-iam-authenticator configuration. If this is nil the default configuration is still generated for the cluster.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**map_roles** | [**list[IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneSpecIamAuthenticatorConfigMapRoles]**](IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneSpecIamAuthenticatorConfigMapRoles.md) | RoleMappings is a list of role mappings | [optional] 
**map_users** | [**list[IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneSpecIamAuthenticatorConfigMapUsers]**](IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneSpecIamAuthenticatorConfigMapUsers.md) | UserMappings is a list of user mappings | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


