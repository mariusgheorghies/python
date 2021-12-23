# IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneSpecNetworkSpecSubnets

SubnetSpec configures an AWS Subnet.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**availability_zone** | **str** | AvailabilityZone defines the availability zone to use for this subnet in the cluster&#39;s region. | [optional] 
**cidr_block** | **str** | CidrBlock is the CIDR block to be used when the provider creates a managed VPC. | [optional] 
**id** | **str** | ID defines a unique identifier to reference this resource. | [optional] 
**is_public** | **bool** | IsPublic defines the subnet as a public subnet. A subnet is public when it is associated with a route table that has a route to an internet gateway. | [optional] 
**nat_gateway_id** | **str** | NatGatewayID is the NAT gateway id associated with the subnet. Ignored unless the subnet is managed by the provider, in which case this is set on the public subnet where the NAT gateway resides. It is then used to determine routes for private subnets in the same AZ as the public subnet. | [optional] 
**route_table_id** | **str** | RouteTableID is the routing table id associated with the subnet. | [optional] 
**tags** | **dict(str, str)** | Tags is a collection of tags describing the resource. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


