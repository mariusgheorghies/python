# AwsK8sServicesEc2V1alpha1VPCEndpointStatus

VPCEndpointStatus defines the observed state of VPCEndpoint
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ack_resource_metadata** | [**AwsK8sServicesEc2V1alpha1DHCPOptionsStatusAckResourceMetadata**](AwsK8sServicesEc2V1alpha1DHCPOptionsStatusAckResourceMetadata.md) |  | [optional] 
**conditions** | [**list[AwsK8sServicesEc2V1alpha1DHCPOptionsStatusConditions]**](AwsK8sServicesEc2V1alpha1DHCPOptionsStatusConditions.md) | All CRS managed by ACK have a common &#x60;Status.Conditions&#x60; member that contains a collection of &#x60;ackv1alpha1.Condition&#x60; objects that describe the various terminal states of the CR and its backend AWS service API resource | [optional] 
**creation_timestamp** | **datetime** | The date and time that the endpoint was created. | [optional] 
**dns_entries** | [**list[AwsK8sServicesEc2V1alpha1VPCEndpointStatusDnsEntries]**](AwsK8sServicesEc2V1alpha1VPCEndpointStatusDnsEntries.md) | (Interface endpoint) The DNS entries for the endpoint. | [optional] 
**groups** | [**list[AwsK8sServicesEc2V1alpha1VPCEndpointStatusGroups]**](AwsK8sServicesEc2V1alpha1VPCEndpointStatusGroups.md) | (Interface endpoint) Information about the security groups that are associated with the network interface. | [optional] 
**last_error** | [**AwsK8sServicesEc2V1alpha1VPCEndpointStatusLastError**](AwsK8sServicesEc2V1alpha1VPCEndpointStatusLastError.md) |  | [optional] 
**network_interface_i_ds** | **list[str]** | (Interface endpoint) One or more network interfaces for the endpoint. | [optional] 
**owner_id** | **str** | The ID of the Amazon Web Services account that owns the endpoint. | [optional] 
**requester_managed** | **bool** | Indicates whether the endpoint is being managed by its service. | [optional] 
**state** | **str** | The state of the endpoint. | [optional] 
**vpc_endpoint_id** | **str** | The ID of the endpoint. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


