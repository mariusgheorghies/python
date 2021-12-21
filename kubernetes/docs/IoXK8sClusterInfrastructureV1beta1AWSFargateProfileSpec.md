# IoXK8sClusterInfrastructureV1beta1AWSFargateProfileSpec

FargateProfileSpec defines the desired state of FargateProfile.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_tags** | **dict(str, str)** | AdditionalTags is an optional set of tags to add to AWS resources managed by the AWS provider, in addition to the ones added by default. | [optional] 
**cluster_name** | **str** | ClusterName is the name of the Cluster this object belongs to. | 
**profile_name** | **str** | ProfileName specifies the profile name. | [optional] 
**role_name** | **str** | RoleName specifies the name of IAM role for this fargate pool If the role is pre-existing we will treat it as unmanaged and not delete it on deletion. If the EKSEnableIAM feature flag is true and no name is supplied then a role is created. | [optional] 
**selectors** | [**list[IoXK8sClusterInfrastructureV1beta1AWSFargateProfileSpecSelectors]**](IoXK8sClusterInfrastructureV1beta1AWSFargateProfileSpecSelectors.md) | Selectors specify fargate pod selectors. | [optional] 
**subnet_i_ds** | **list[str]** | SubnetIDs specifies which subnets are used for the auto scaling group of this nodegroup. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


