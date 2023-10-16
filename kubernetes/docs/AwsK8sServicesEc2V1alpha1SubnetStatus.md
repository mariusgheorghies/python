# AwsK8sServicesEc2V1alpha1SubnetStatus

SubnetStatus defines the observed state of Subnet
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ack_resource_metadata** | [**AwsK8sServicesEc2V1alpha1DHCPOptionsStatusAckResourceMetadata**](AwsK8sServicesEc2V1alpha1DHCPOptionsStatusAckResourceMetadata.md) |  | [optional] 
**available_ip_address_count** | **int** | The number of unused private IPv4 addresses in the subnet. The IPv4 addresses for any stopped instances are considered unavailable. | [optional] 
**conditions** | [**list[AwsK8sServicesEc2V1alpha1DHCPOptionsStatusConditions]**](AwsK8sServicesEc2V1alpha1DHCPOptionsStatusConditions.md) | All CRS managed by ACK have a common &#x60;Status.Conditions&#x60; member that contains a collection of &#x60;ackv1alpha1.Condition&#x60; objects that describe the various terminal states of the CR and its backend AWS service API resource | [optional] 
**default_for_az** | **bool** | Indicates whether this is the default subnet for the Availability Zone. | [optional] 
**enable_lni_at_device_index** | **int** | Indicates the device position for local network interfaces in this subnet. For example, 1 indicates local network interfaces in this subnet are the secondary network interface (eth1). | [optional] 
**ipv6_cidr_block_association_set** | [**list[AwsK8sServicesEc2V1alpha1SubnetStatusIpv6CIDRBlockAssociationSet]**](AwsK8sServicesEc2V1alpha1SubnetStatusIpv6CIDRBlockAssociationSet.md) | Information about the IPv6 CIDR blocks associated with the subnet. | [optional] 
**map_customer_owned_ip_on_launch** | **bool** | Indicates whether a network interface created in this subnet (including a network interface created by RunInstances) receives a customer-owned IPv4 address. | [optional] 
**owner_id** | **str** | The ID of the Amazon Web Services account that owns the subnet. | [optional] 
**private_dns_name_options_on_launch** | [**AwsK8sServicesEc2V1alpha1SubnetStatusPrivateDNSNameOptionsOnLaunch**](AwsK8sServicesEc2V1alpha1SubnetStatusPrivateDNSNameOptionsOnLaunch.md) |  | [optional] 
**state** | **str** | The current state of the subnet. | [optional] 
**subnet_id** | **str** | The ID of the subnet. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


