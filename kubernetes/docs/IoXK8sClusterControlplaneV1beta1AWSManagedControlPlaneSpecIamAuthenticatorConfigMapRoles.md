# IoXK8sClusterControlplaneV1beta1AWSManagedControlPlaneSpecIamAuthenticatorConfigMapRoles

RoleMapping represents a mapping from a IAM role to Kubernetes users and groups.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**groups** | **list[str]** | Groups is a list of kubernetes RBAC groups | 
**rolearn** | **str** | RoleARN is the AWS ARN for the role to map | 
**username** | **str** | UserName is a kubernetes RBAC user subject | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


