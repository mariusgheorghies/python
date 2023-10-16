# AwsK8sServicesEc2V1alpha1FlowLogStatus

FlowLogStatus defines the observed state of FlowLog
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ack_resource_metadata** | [**AwsK8sServicesEc2V1alpha1DHCPOptionsStatusAckResourceMetadata**](AwsK8sServicesEc2V1alpha1DHCPOptionsStatusAckResourceMetadata.md) |  | [optional] 
**kubernetes.client_token** | **str** | Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. | [optional] 
**conditions** | [**list[AwsK8sServicesEc2V1alpha1DHCPOptionsStatusConditions]**](AwsK8sServicesEc2V1alpha1DHCPOptionsStatusConditions.md) | All CRS managed by ACK have a common &#x60;Status.Conditions&#x60; member that contains a collection of &#x60;ackv1alpha1.Condition&#x60; objects that describe the various terminal states of the CR and its backend AWS service API resource | [optional] 
**flow_log_id** | **str** |  | [optional] 
**unsuccessful** | [**list[AwsK8sServicesEc2V1alpha1FlowLogStatusUnsuccessful]**](AwsK8sServicesEc2V1alpha1FlowLogStatusUnsuccessful.md) | Information about the flow logs that could not be created successfully. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


