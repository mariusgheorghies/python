# AwsK8sServicesEc2V1alpha1NetworkACLSpec

NetworkAclSpec defines the desired state of NetworkAcl.   Describes a network ACL.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associations** | [**list[AwsK8sServicesEc2V1alpha1NetworkACLSpecAssociations]**](AwsK8sServicesEc2V1alpha1NetworkACLSpecAssociations.md) |  | [optional] 
**entries** | [**list[AwsK8sServicesEc2V1alpha1NetworkACLSpecEntries]**](AwsK8sServicesEc2V1alpha1NetworkACLSpecEntries.md) |  | [optional] 
**tags** | [**list[AwsK8sServicesEc2V1alpha1DHCPOptionsSpecTags]**](AwsK8sServicesEc2V1alpha1DHCPOptionsSpecTags.md) | The tags. The value parameter is required, but if you don&#39;t want the tag to have a value, specify the parameter with no value, and we set the value to an empty string. | [optional] 
**vpc_id** | **str** | The ID of the VPC. | [optional] 
**vpc_ref** | [**AwsK8sServicesEc2V1alpha1DHCPOptionsSpecVpcRefs**](AwsK8sServicesEc2V1alpha1DHCPOptionsSpecVpcRefs.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


