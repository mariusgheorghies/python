# AwsK8sServicesEc2V1alpha1DHCPOptionsSpec

DhcpOptionsSpec defines the desired state of DhcpOptions.   Describes a set of DHCP options.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dhcp_configurations** | [**list[AwsK8sServicesEc2V1alpha1DHCPOptionsSpecDhcpConfigurations]**](AwsK8sServicesEc2V1alpha1DHCPOptionsSpecDhcpConfigurations.md) | A DHCP configuration option. | 
**tags** | [**list[AwsK8sServicesEc2V1alpha1DHCPOptionsSpecTags]**](AwsK8sServicesEc2V1alpha1DHCPOptionsSpecTags.md) | The tags. The value parameter is required, but if you don&#39;t want the tag to have a value, specify the parameter with no value, and we set the value to an empty string. | [optional] 
**vpc** | **list[str]** |  | [optional] 
**vpc_refs** | [**list[AwsK8sServicesEc2V1alpha1DHCPOptionsSpecVpcRefs]**](AwsK8sServicesEc2V1alpha1DHCPOptionsSpecVpcRefs.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


