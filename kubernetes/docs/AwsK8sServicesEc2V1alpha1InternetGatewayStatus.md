# AwsK8sServicesEc2V1alpha1InternetGatewayStatus

InternetGatewayStatus defines the observed state of InternetGateway
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ack_resource_metadata** | [**AwsK8sServicesEc2V1alpha1DHCPOptionsStatusAckResourceMetadata**](AwsK8sServicesEc2V1alpha1DHCPOptionsStatusAckResourceMetadata.md) |  | [optional] 
**attachments** | [**list[AwsK8sServicesEc2V1alpha1InternetGatewayStatusAttachments]**](AwsK8sServicesEc2V1alpha1InternetGatewayStatusAttachments.md) | Any VPCs attached to the internet gateway. | [optional] 
**conditions** | [**list[AwsK8sServicesEc2V1alpha1DHCPOptionsStatusConditions]**](AwsK8sServicesEc2V1alpha1DHCPOptionsStatusConditions.md) | All CRS managed by ACK have a common &#x60;Status.Conditions&#x60; member that contains a collection of &#x60;ackv1alpha1.Condition&#x60; objects that describe the various terminal states of the CR and its backend AWS service API resource | [optional] 
**internet_gateway_id** | **str** | The ID of the internet gateway. | [optional] 
**owner_id** | **str** | The ID of the Amazon Web Services account that owns the internet gateway. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


