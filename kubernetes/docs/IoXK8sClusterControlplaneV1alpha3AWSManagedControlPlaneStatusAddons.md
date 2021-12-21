# IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneStatusAddons

AddonState represents the state of an addon
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arn** | **str** | ARN is the AWS ARN of the addon | 
**created_at** | **datetime** | CreatedAt is the date and time the addon was created at | [optional] 
**issues** | [**list[IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneStatusIssues]**](IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneStatusIssues.md) | Issues is a list of issue associated with the addon | [optional] 
**modified_at** | **datetime** | ModifiedAt is the date and time the addon was last modified | [optional] 
**name** | **str** | Name is the name of the addon | 
**service_account_role_arn** | **str** | ServiceAccountRoleArn is the ARN of the IAM role used for the service account | [optional] 
**status** | **str** | Status is the status of the addon | [optional] 
**version** | **str** | Version is the version of the addon to use | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


