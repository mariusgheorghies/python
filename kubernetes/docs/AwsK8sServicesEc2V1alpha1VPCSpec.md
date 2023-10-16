# AwsK8sServicesEc2V1alpha1VPCSpec

VpcSpec defines the desired state of Vpc.   Describes a VPC.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amazon_provided_i_pv6_cidr_block** | **bool** | Requests an Amazon-provided IPv6 CIDR block with a /56 prefix length for the VPC. You cannot specify the range of IP addresses, or the size of the CIDR block. | [optional] 
**cidr_blocks** | **list[str]** |  | 
**enable_dns_hostnames** | **bool** | The attribute value. The valid values are true or false. | [optional] 
**enable_dns_support** | **bool** | The attribute value. The valid values are true or false. | [optional] 
**instance_tenancy** | **str** | The tenancy options for instances launched into the VPC. For default, instances are launched with shared tenancy by default. You can launch instances with any tenancy into a shared tenancy VPC. For dedicated, instances are launched as dedicated tenancy instances by default. You can only launch instances with a tenancy of dedicated or host into a dedicated tenancy VPC.   Important: The host value cannot be used with this parameter. Use the default or dedicated values only.   Default: default | [optional] 
**ipv4_ipam_pool_id** | **str** | The ID of an IPv4 IPAM pool you want to use for allocating this VPC&#39;s CIDR. For more information, see What is IPAM? (https://docs.aws.amazon.com/vpc/latest/ipam/what-is-it-ipam.html) in the Amazon VPC IPAM User Guide. | [optional] 
**ipv4_netmask_length** | **int** | The netmask length of the IPv4 CIDR you want to allocate to this VPC from an Amazon VPC IP Address Manager (IPAM) pool. For more information about IPAM, see What is IPAM? (https://docs.aws.amazon.com/vpc/latest/ipam/what-is-it-ipam.html) in the Amazon VPC IPAM User Guide. | [optional] 
**ipv6_cidr_block** | **str** | The IPv6 CIDR block from the IPv6 address pool. You must also specify Ipv6Pool in the request.   To let Amazon choose the IPv6 CIDR block for you, omit this parameter. | [optional] 
**ipv6_cidr_block_network_border_group** | **str** | The name of the location from which we advertise the IPV6 CIDR block. Use this parameter to limit the address to this location.   You must set AmazonProvidedIpv6CidrBlock to true to use this parameter. | [optional] 
**ipv6_ipam_pool_id** | **str** | The ID of an IPv6 IPAM pool which will be used to allocate this VPC an IPv6 CIDR. IPAM is a VPC feature that you can use to automate your IP address management workflows including assigning, tracking, troubleshooting, and auditing IP addresses across Amazon Web Services Regions and accounts throughout your Amazon Web Services Organization. For more information, see What is IPAM? (https://docs.aws.amazon.com/vpc/latest/ipam/what-is-it-ipam.html) in the Amazon VPC IPAM User Guide. | [optional] 
**ipv6_netmask_length** | **int** | The netmask length of the IPv6 CIDR you want to allocate to this VPC from an Amazon VPC IP Address Manager (IPAM) pool. For more information about IPAM, see What is IPAM? (https://docs.aws.amazon.com/vpc/latest/ipam/what-is-it-ipam.html) in the Amazon VPC IPAM User Guide. | [optional] 
**ipv6_pool** | **str** | The ID of an IPv6 address pool from which to allocate the IPv6 CIDR block. | [optional] 
**tags** | [**list[AwsK8sServicesEc2V1alpha1DHCPOptionsSpecTags]**](AwsK8sServicesEc2V1alpha1DHCPOptionsSpecTags.md) | The tags. The value parameter is required, but if you don&#39;t want the tag to have a value, specify the parameter with no value, and we set the value to an empty string. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


