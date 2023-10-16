# AwsK8sServicesEc2V1alpha1TransitGatewayStatus

TransitGatewayStatus defines the observed state of TransitGateway
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ack_resource_metadata** | [**AwsK8sServicesEc2V1alpha1DHCPOptionsStatusAckResourceMetadata**](AwsK8sServicesEc2V1alpha1DHCPOptionsStatusAckResourceMetadata.md) |  | [optional] 
**conditions** | [**list[AwsK8sServicesEc2V1alpha1DHCPOptionsStatusConditions]**](AwsK8sServicesEc2V1alpha1DHCPOptionsStatusConditions.md) | All CRS managed by ACK have a common &#x60;Status.Conditions&#x60; member that contains a collection of &#x60;ackv1alpha1.Condition&#x60; objects that describe the various terminal states of the CR and its backend AWS service API resource | [optional] 
**creation_time** | **datetime** | The creation time. | [optional] 
**owner_id** | **str** | The ID of the Amazon Web Services account that owns the transit gateway. | [optional] 
**state** | **str** | The state of the transit gateway. | [optional] 
**transit_gateway_id** | **str** | The ID of the transit gateway. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


