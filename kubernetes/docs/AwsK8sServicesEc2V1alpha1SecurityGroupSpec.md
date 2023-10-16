# AwsK8sServicesEc2V1alpha1SecurityGroupSpec

SecurityGroupSpec defines the desired state of SecurityGroup.   Describes a security group.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | A description for the security group. This is informational only.   Constraints: Up to 255 characters in length   Constraints for EC2-Classic: ASCII characters   Constraints for EC2-VPC: a-z, A-Z, 0-9, spaces, and ._-:/()#,@[]+&#x3D;&amp;;{}!$* | 
**egress_rules** | [**list[AwsK8sServicesEc2V1alpha1SecurityGroupSpecEgressRules]**](AwsK8sServicesEc2V1alpha1SecurityGroupSpecEgressRules.md) |  | [optional] 
**ingress_rules** | [**list[AwsK8sServicesEc2V1alpha1SecurityGroupSpecEgressRules]**](AwsK8sServicesEc2V1alpha1SecurityGroupSpecEgressRules.md) |  | [optional] 
**name** | **str** | The name of the security group.   Constraints: Up to 255 characters in length. Cannot start with sg-.   Constraints for EC2-Classic: ASCII characters   Constraints for EC2-VPC: a-z, A-Z, 0-9, spaces, and ._-:/()#,@[]+&#x3D;&amp;;{}!$* | 
**tags** | [**list[AwsK8sServicesEc2V1alpha1DHCPOptionsSpecTags]**](AwsK8sServicesEc2V1alpha1DHCPOptionsSpecTags.md) | The tags. The value parameter is required, but if you don&#39;t want the tag to have a value, specify the parameter with no value, and we set the value to an empty string. | [optional] 
**vpc_id** | **str** | [EC2-VPC] The ID of the VPC. Required for EC2-VPC. | [optional] 
**vpc_ref** | [**AwsK8sServicesEc2V1alpha1DHCPOptionsSpecVpcRefs**](AwsK8sServicesEc2V1alpha1DHCPOptionsSpecVpcRefs.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


