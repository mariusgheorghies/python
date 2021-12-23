# IoXK8sClusterInfrastructureV1alpha3AWSClusterSpecControlPlaneLoadBalancer

ControlPlaneLoadBalancer is optional configuration for customizing control plane behavior.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_security_groups** | **list[str]** | AdditionalSecurityGroups sets the security groups used by the load balancer. Expected to be security group IDs This is optional - if not provided new security groups will be created for the load balancer | [optional] 
**cross_zone_load_balancing** | **bool** | CrossZoneLoadBalancing enables the classic ELB cross availability zone balancing.   With cross-zone load balancing, each load balancer node for your Classic Load Balancer distributes requests evenly across the registered instances in all enabled Availability Zones. If cross-zone load balancing is disabled, each load balancer node distributes requests evenly across the registered instances in its Availability Zone only.   Defaults to false. | [optional] 
**scheme** | **str** | Scheme sets the scheme of the load balancer (defaults to internet-facing) | [optional] 
**subnets** | **list[str]** | Subnets sets the subnets that should be applied to the control plane load balancer (defaults to discovered subnets for managed VPCs or an empty set for unmanaged VPCs) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


