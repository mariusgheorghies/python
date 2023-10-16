# IoQuestdbCrdV1alpha1QuestDBSpecAws

AWS-Specific configuration
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iam_instance_profile_arn** | **str** | IAM instance profile ARN that each database node is running under | 
**image_id** | **str** | AMI ID used for each database instance | 
**instance_type** | **str** | AWS Instance Type | 
**key_name** | **str** | SSH key used to launch each database instance | 
**region** | **str** | AWS Region (example: eu-west-1) | 
**region_az** | **str** | AWS Region Availability Zone (example: eu-west-1a) | 
**security_group_ids** | **list[str]** | Security group IDs to be attached to each database node | 
**subnet_id** | **str** | AWS Subnet ID of the kubernetes cluster | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


