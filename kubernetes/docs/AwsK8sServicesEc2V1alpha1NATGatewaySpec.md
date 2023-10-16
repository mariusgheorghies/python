# AwsK8sServicesEc2V1alpha1NATGatewaySpec

NatGatewaySpec defines the desired state of NatGateway.   Describes a NAT gateway.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allocation_id** | **str** | [Public NAT gateways only] The allocation ID of an Elastic IP address to associate with the NAT gateway. You cannot specify an Elastic IP address with a private NAT gateway. If the Elastic IP address is associated with another resource, you must first disassociate it. | [optional] 
**allocation_ref** | [**AwsK8sServicesEc2V1alpha1DHCPOptionsSpecVpcRefs**](AwsK8sServicesEc2V1alpha1DHCPOptionsSpecVpcRefs.md) |  | [optional] 
**connectivity_type** | **str** | Indicates whether the NAT gateway supports public or private connectivity. The default is public connectivity. | [optional] 
**subnet_id** | **str** | The subnet in which to create the NAT gateway. | [optional] 
**subnet_ref** | [**AwsK8sServicesEc2V1alpha1DHCPOptionsSpecVpcRefs**](AwsK8sServicesEc2V1alpha1DHCPOptionsSpecVpcRefs.md) |  | [optional] 
**tags** | [**list[AwsK8sServicesEc2V1alpha1DHCPOptionsSpecTags]**](AwsK8sServicesEc2V1alpha1DHCPOptionsSpecTags.md) | The tags. The value parameter is required, but if you don&#39;t want the tag to have a value, specify the parameter with no value, and we set the value to an empty string. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


