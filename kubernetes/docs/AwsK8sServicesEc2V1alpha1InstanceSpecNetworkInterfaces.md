# AwsK8sServicesEc2V1alpha1InstanceSpecNetworkInterfaces

Describes a network interface.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associate_carrier_ip_address** | **bool** |  | [optional] 
**associate_public_ip_address** | **bool** |  | [optional] 
**delete_on_termination** | **bool** |  | [optional] 
**description** | **str** |  | [optional] 
**device_index** | **int** |  | [optional] 
**interface_type** | **str** |  | [optional] 
**ipv4_prefix_count** | **int** |  | [optional] 
**ipv4_prefixes** | [**list[AwsK8sServicesEc2V1alpha1InstanceSpecIpv4Prefixes]**](AwsK8sServicesEc2V1alpha1InstanceSpecIpv4Prefixes.md) |  | [optional] 
**ipv6_address_count** | **int** |  | [optional] 
**ipv6_addresses** | [**list[AwsK8sServicesEc2V1alpha1InstanceSpecIpv6Addresses]**](AwsK8sServicesEc2V1alpha1InstanceSpecIpv6Addresses.md) |  | [optional] 
**ipv6_prefix_count** | **int** |  | [optional] 
**ipv6_prefixes** | [**list[AwsK8sServicesEc2V1alpha1InstanceSpecIpv6Prefixes]**](AwsK8sServicesEc2V1alpha1InstanceSpecIpv6Prefixes.md) |  | [optional] 
**network_card_index** | **int** |  | [optional] 
**network_interface_id** | **str** |  | [optional] 
**private_ip_address** | **str** |  | [optional] 
**private_ip_addresses** | [**list[AwsK8sServicesEc2V1alpha1InstanceSpecPrivateIPAddresses]**](AwsK8sServicesEc2V1alpha1InstanceSpecPrivateIPAddresses.md) |  | [optional] 
**secondary_private_ip_address_count** | **int** |  | [optional] 
**subnet_id** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


