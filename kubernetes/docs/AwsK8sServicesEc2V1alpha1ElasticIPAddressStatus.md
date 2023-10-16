# AwsK8sServicesEc2V1alpha1ElasticIPAddressStatus

ElasticIPAddressStatus defines the observed state of ElasticIPAddress
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ack_resource_metadata** | [**AwsK8sServicesEc2V1alpha1DHCPOptionsStatusAckResourceMetadata**](AwsK8sServicesEc2V1alpha1DHCPOptionsStatusAckResourceMetadata.md) |  | [optional] 
**allocation_id** | **str** | [EC2-VPC] The ID that Amazon Web Services assigns to represent the allocation of the Elastic IP address for use with instances in a VPC. | [optional] 
**carrier_ip** | **str** | The carrier IP address. This option is only available for network interfaces which reside in a subnet in a Wavelength Zone (for example an EC2 instance). | [optional] 
**conditions** | [**list[AwsK8sServicesEc2V1alpha1DHCPOptionsStatusConditions]**](AwsK8sServicesEc2V1alpha1DHCPOptionsStatusConditions.md) | All CRS managed by ACK have a common &#x60;Status.Conditions&#x60; member that contains a collection of &#x60;ackv1alpha1.Condition&#x60; objects that describe the various terminal states of the CR and its backend AWS service API resource | [optional] 
**customer_owned_ip** | **str** | The customer-owned IP address. | [optional] 
**public_ip** | **str** | The Elastic IP address. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


