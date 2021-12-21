# IoXK8sClusterControlplaneV1beta1AWSManagedControlPlaneSpecIamAuthenticatorConfigMapUsers

UserMapping represents a mapping from an IAM user to Kubernetes users and groups.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**groups** | **list[str]** | Groups is a list of kubernetes RBAC groups | 
**userarn** | **str** | UserARN is the AWS ARN for the user to map | 
**username** | **str** | UserName is a kubernetes RBAC user subject | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


