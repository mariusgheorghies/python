# AwsK8sServicesEc2V1alpha1RouteTableStatus

RouteTableStatus defines the observed state of RouteTable
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ack_resource_metadata** | [**AwsK8sServicesEc2V1alpha1DHCPOptionsStatusAckResourceMetadata**](AwsK8sServicesEc2V1alpha1DHCPOptionsStatusAckResourceMetadata.md) |  | [optional] 
**associations** | [**list[AwsK8sServicesEc2V1alpha1RouteTableStatusAssociations]**](AwsK8sServicesEc2V1alpha1RouteTableStatusAssociations.md) | The associations between the route table and one or more subnets or a gateway. | [optional] 
**conditions** | [**list[AwsK8sServicesEc2V1alpha1DHCPOptionsStatusConditions]**](AwsK8sServicesEc2V1alpha1DHCPOptionsStatusConditions.md) | All CRS managed by ACK have a common &#x60;Status.Conditions&#x60; member that contains a collection of &#x60;ackv1alpha1.Condition&#x60; objects that describe the various terminal states of the CR and its backend AWS service API resource | [optional] 
**owner_id** | **str** | The ID of the Amazon Web Services account that owns the route table. | [optional] 
**propagating_vg_ws** | [**list[AwsK8sServicesEc2V1alpha1RouteTableStatusPropagatingVGWs]**](AwsK8sServicesEc2V1alpha1RouteTableStatusPropagatingVGWs.md) | Any virtual private gateway (VGW) propagating routes. | [optional] 
**route_statuses** | [**list[AwsK8sServicesEc2V1alpha1RouteTableStatusRouteStatuses]**](AwsK8sServicesEc2V1alpha1RouteTableStatusRouteStatuses.md) | The routes in the route table. | [optional] 
**route_table_id** | **str** | The ID of the route table. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


