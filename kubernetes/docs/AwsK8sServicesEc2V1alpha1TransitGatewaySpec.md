# AwsK8sServicesEc2V1alpha1TransitGatewaySpec

TransitGatewaySpec defines the desired state of TransitGateway.   Describes a transit gateway.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | A description of the transit gateway. | [optional] 
**options** | [**AwsK8sServicesEc2V1alpha1TransitGatewaySpecOptions**](AwsK8sServicesEc2V1alpha1TransitGatewaySpecOptions.md) |  | [optional] 
**tags** | [**list[AwsK8sServicesEc2V1alpha1DHCPOptionsSpecTags]**](AwsK8sServicesEc2V1alpha1DHCPOptionsSpecTags.md) | The tags. The value parameter is required, but if you don&#39;t want the tag to have a value, specify the parameter with no value, and we set the value to an empty string. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


