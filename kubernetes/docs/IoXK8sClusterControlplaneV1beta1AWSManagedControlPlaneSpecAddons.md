# IoXK8sClusterControlplaneV1beta1AWSManagedControlPlaneSpecAddons

Addon represents a EKS addon.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conflict_resolution** | **str** | ConflictResolution is used to declare what should happen if there are parameter conflicts. Defaults to none | [optional] 
**name** | **str** | Name is the name of the addon | 
**service_account_role_arn** | **str** | ServiceAccountRoleArn is the ARN of an IAM role to bind to the addons service account | [optional] 
**version** | **str** | Version is the version of the addon to use | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


