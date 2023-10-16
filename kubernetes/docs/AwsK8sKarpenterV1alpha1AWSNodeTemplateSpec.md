# AwsK8sKarpenterV1alpha1AWSNodeTemplateSpec

AWSNodeTemplateSpec is the top level specification for the AWS Karpenter Provider. This will contain configuration necessary to launch instances in AWS.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_data** | **str** | UserData to be applied to the provisioned nodes. It must be in the appropriate format based on the AMIFamily in use. Karpenter will merge certain fields into this UserData to ensure nodes are being provisioned with the correct configuration. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


