# IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneSpecBastion

Bastion contains options to configure the bastion host.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_cidr_blocks** | **list[str]** | AllowedCIDRBlocks is a list of CIDR blocks allowed to access the bastion host. They are set as ingress rules for the Bastion host&#39;s Security Group (defaults to 0.0.0.0/0). | [optional] 
**ami** | **str** | AMI will use the specified AMI to boot the bastion. If not specified, the AMI will default to one picked out in public space. | [optional] 
**disable_ingress_rules** | **bool** | DisableIngressRules will ensure there are no Ingress rules in the bastion host&#39;s security group. Requires AllowedCIDRBlocks to be empty. | [optional] 
**enabled** | **bool** | Enabled allows this provider to create a bastion host instance with a public ip to access the VPC private network. | [optional] 
**instance_type** | **str** | InstanceType will use the specified instance type for the bastion. If not specified, Cluster API Provider AWS will use t3.micro for all regions except us-east-1, where t2.micro will be the default. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


