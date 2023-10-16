# AwsK8sServicesEc2V1alpha1VPCStatus

VPCStatus defines the observed state of VPC
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ack_resource_metadata** | [**AwsK8sServicesEc2V1alpha1DHCPOptionsStatusAckResourceMetadata**](AwsK8sServicesEc2V1alpha1DHCPOptionsStatusAckResourceMetadata.md) |  | [optional] 
**cidr_block_association_set** | [**list[AwsK8sServicesEc2V1alpha1VPCStatusCidrBlockAssociationSet]**](AwsK8sServicesEc2V1alpha1VPCStatusCidrBlockAssociationSet.md) | Information about the IPv4 CIDR blocks associated with the VPC. | [optional] 
**conditions** | [**list[AwsK8sServicesEc2V1alpha1DHCPOptionsStatusConditions]**](AwsK8sServicesEc2V1alpha1DHCPOptionsStatusConditions.md) | All CRS managed by ACK have a common &#x60;Status.Conditions&#x60; member that contains a collection of &#x60;ackv1alpha1.Condition&#x60; objects that describe the various terminal states of the CR and its backend AWS service API resource | [optional] 
**dhcp_options_id** | **str** | The ID of the set of DHCP options you&#39;ve associated with the VPC. | [optional] 
**ipv6_cidr_block_association_set** | [**list[AwsK8sServicesEc2V1alpha1VPCStatusIpv6CIDRBlockAssociationSet]**](AwsK8sServicesEc2V1alpha1VPCStatusIpv6CIDRBlockAssociationSet.md) | Information about the IPv6 CIDR blocks associated with the VPC. | [optional] 
**is_default** | **bool** | Indicates whether the VPC is the default VPC. | [optional] 
**owner_id** | **str** | The ID of the Amazon Web Services account that owns the VPC. | [optional] 
**state** | **str** | The current state of the VPC. | [optional] 
**vpc_id** | **str** | The ID of the VPC. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


