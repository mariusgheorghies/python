# IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneStatusNetworkIngressRule

IngressRule defines an AWS ingress rule for security groups.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cidr_blocks** | **list[str]** | List of CIDR blocks to allow access from. Cannot be specified with SourceSecurityGroupID. | [optional] 
**description** | **str** |  | 
**from_port** | **int** |  | 
**protocol** | **str** | SecurityGroupProtocol defines the protocol type for a security group rule. | 
**source_security_group_ids** | **list[str]** | The security group id to allow access from. Cannot be specified with CidrBlocks. | [optional] 
**to_port** | **int** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


