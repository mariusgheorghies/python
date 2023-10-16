# AwsK8sServicesEc2V1alpha1SubnetSpec

SubnetSpec defines the desired state of Subnet.   Describes a subnet.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assign_i_pv6_address_on_creation** | **bool** |  | [optional] 
**availability_zone** | **str** | The Availability Zone or Local Zone for the subnet.   Default: Amazon Web Services selects one for you. If you create more than one subnet in your VPC, we do not necessarily select a different zone for each subnet.   To create a subnet in a Local Zone, set this value to the Local Zone ID, for example us-west-2-lax-1a. For information about the Regions that support Local Zones, see Available Regions (https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-available-regions) in the Amazon Elastic Compute Cloud User Guide.   To create a subnet in an Outpost, set this value to the Availability Zone for the Outpost and specify the Outpost ARN. | [optional] 
**availability_zone_id** | **str** | The AZ ID or the Local Zone ID of the subnet. | [optional] 
**cidr_block** | **str** | The IPv4 network range for the subnet, in CIDR notation. For example, 10.0.0.0/24. We modify the specified CIDR block to its canonical form; for example, if you specify 100.68.0.18/18, we modify it to 100.68.0.0/18.   This parameter is not supported for an IPv6 only subnet. | [optional] 
**customer_owned_i_pv4_pool** | **str** |  | [optional] 
**enable_dns64** | **bool** |  | [optional] 
**enable_resource_name_dnsaaaa_record** | **bool** |  | [optional] 
**enable_resource_name_dnsa_record** | **bool** |  | [optional] 
**hostname_type** | **str** |  | [optional] 
**ipv6_cidr_block** | **str** | The IPv6 network range for the subnet, in CIDR notation. The subnet size must use a /64 prefix length.   This parameter is required for an IPv6 only subnet. | [optional] 
**ipv6_native** | **bool** | Indicates whether to create an IPv6 only subnet. | [optional] 
**map_public_ip_on_launch** | **bool** |  | [optional] 
**outpost_arn** | **str** | The Amazon Resource Name (ARN) of the Outpost. If you specify an Outpost ARN, you must also specify the Availability Zone of the Outpost subnet. | [optional] 
**route_table_refs** | [**list[AwsK8sServicesEc2V1alpha1DHCPOptionsSpecVpcRefs]**](AwsK8sServicesEc2V1alpha1DHCPOptionsSpecVpcRefs.md) |  | [optional] 
**route_tables** | **list[str]** |  | [optional] 
**tags** | [**list[AwsK8sServicesEc2V1alpha1DHCPOptionsSpecTags]**](AwsK8sServicesEc2V1alpha1DHCPOptionsSpecTags.md) | The tags. The value parameter is required, but if you don&#39;t want the tag to have a value, specify the parameter with no value, and we set the value to an empty string. | [optional] 
**vpc_id** | **str** | The ID of the VPC. | [optional] 
**vpc_ref** | [**AwsK8sServicesEc2V1alpha1DHCPOptionsSpecVpcRefs**](AwsK8sServicesEc2V1alpha1DHCPOptionsSpecVpcRefs.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


