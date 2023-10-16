# AwsK8sServicesEc2V1alpha1ElasticIPAddressSpec

ElasticIPAddressSpec defines the desired state of ElasticIPAddress.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | [EC2-VPC] The Elastic IP address to recover or an IPv4 address from an address pool. | [optional] 
**customer_owned_i_pv4_pool** | **str** | The ID of a customer-owned address pool. Use this parameter to let Amazon EC2 select an address from the address pool. Alternatively, specify a specific address from the address pool. | [optional] 
**network_border_group** | **str** | A unique set of Availability Zones, Local Zones, or Wavelength Zones from which Amazon Web Services advertises IP addresses. Use this parameter to limit the IP address to this location. IP addresses cannot move between network border groups.   Use DescribeAvailabilityZones (https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeAvailabilityZones.html) to view the network border groups.   You cannot use a network border group with EC2 Classic. If you attempt this operation on EC2 Classic, you receive an InvalidParameterCombination error. | [optional] 
**public_i_pv4_pool** | **str** | The ID of an address pool that you own. Use this parameter to let Amazon EC2 select an address from the address pool. To specify a specific address from the address pool, use the Address parameter instead. | [optional] 
**tags** | [**list[AwsK8sServicesEc2V1alpha1DHCPOptionsSpecTags]**](AwsK8sServicesEc2V1alpha1DHCPOptionsSpecTags.md) | The tags. The value parameter is required, but if you don&#39;t want the tag to have a value, specify the parameter with no value, and we set the value to an empty string. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


