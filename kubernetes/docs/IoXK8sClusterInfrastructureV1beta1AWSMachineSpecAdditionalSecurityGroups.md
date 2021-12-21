# IoXK8sClusterInfrastructureV1beta1AWSMachineSpecAdditionalSecurityGroups

AWSResourceReference is a reference to a specific AWS resource by ID, ARN, or filters. Only one of ID, ARN or Filters may be specified. Specifying more than one will result in a validation error.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arn** | **str** | ARN of resource | [optional] 
**filters** | [**list[IoXK8sClusterInfrastructureV1beta1AWSMachineSpecFilters]**](IoXK8sClusterInfrastructureV1beta1AWSMachineSpecFilters.md) | Filters is a set of key/value pairs used to identify a resource They are applied according to the rules defined by the AWS API: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Filtering.html | [optional] 
**id** | **str** | ID of resource | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


