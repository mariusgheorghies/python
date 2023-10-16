# AwsK8sServicesEc2V1alpha1SecurityGroupSpecEgressRules

Describes a set of permissions for a security group rule.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_port** | **int** |  | [optional] 
**ip_protocol** | **str** |  | [optional] 
**ip_ranges** | [**list[AwsK8sServicesEc2V1alpha1SecurityGroupSpecIpRanges]**](AwsK8sServicesEc2V1alpha1SecurityGroupSpecIpRanges.md) |  | [optional] 
**ipv6_ranges** | [**list[AwsK8sServicesEc2V1alpha1SecurityGroupSpecIpv6Ranges]**](AwsK8sServicesEc2V1alpha1SecurityGroupSpecIpv6Ranges.md) |  | [optional] 
**prefix_list_i_ds** | [**list[AwsK8sServicesEc2V1alpha1SecurityGroupSpecPrefixListIDs]**](AwsK8sServicesEc2V1alpha1SecurityGroupSpecPrefixListIDs.md) |  | [optional] 
**to_port** | **int** |  | [optional] 
**user_id_group_pairs** | [**list[AwsK8sServicesEc2V1alpha1SecurityGroupSpecUserIDGroupPairs]**](AwsK8sServicesEc2V1alpha1SecurityGroupSpecUserIDGroupPairs.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


