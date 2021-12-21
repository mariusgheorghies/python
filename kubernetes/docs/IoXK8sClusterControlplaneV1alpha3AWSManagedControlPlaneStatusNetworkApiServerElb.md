# IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneStatusNetworkApiServerElb

APIServerELB is the Kubernetes api server classic load balancer.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneStatusNetworkApiServerElbAttributes**](IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneStatusNetworkApiServerElbAttributes.md) |  | [optional] 
**availability_zones** | **list[str]** | AvailabilityZones is an array of availability zones in the VPC attached to the load balancer. | [optional] 
**dns_name** | **str** | DNSName is the dns name of the load balancer. | [optional] 
**health_checks** | [**IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneStatusNetworkApiServerElbHealthChecks**](IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneStatusNetworkApiServerElbHealthChecks.md) |  | [optional] 
**listeners** | [**list[IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneStatusNetworkApiServerElbListeners]**](IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneStatusNetworkApiServerElbListeners.md) | Listeners is an array of classic elb listeners associated with the load balancer. There must be at least one. | [optional] 
**name** | **str** | The name of the load balancer. It must be unique within the set of load balancers defined in the region. It also serves as identifier. | [optional] 
**scheme** | **str** | Scheme is the load balancer scheme, either internet-facing or private. | [optional] 
**security_group_ids** | **list[str]** | SecurityGroupIDs is an array of security groups assigned to the load balancer. | [optional] 
**subnet_ids** | **list[str]** | SubnetIDs is an array of subnets in the VPC attached to the load balancer. | [optional] 
**tags** | **dict(str, str)** | Tags is a map of tags associated with the load balancer. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


