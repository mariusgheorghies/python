# AwsK8sServicesEc2V1alpha1NATGatewayStatus

NATGatewayStatus defines the observed state of NATGateway
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ack_resource_metadata** | [**AwsK8sServicesEc2V1alpha1DHCPOptionsStatusAckResourceMetadata**](AwsK8sServicesEc2V1alpha1DHCPOptionsStatusAckResourceMetadata.md) |  | [optional] 
**conditions** | [**list[AwsK8sServicesEc2V1alpha1DHCPOptionsStatusConditions]**](AwsK8sServicesEc2V1alpha1DHCPOptionsStatusConditions.md) | All CRS managed by ACK have a common &#x60;Status.Conditions&#x60; member that contains a collection of &#x60;ackv1alpha1.Condition&#x60; objects that describe the various terminal states of the CR and its backend AWS service API resource | [optional] 
**create_time** | **datetime** | The date and time the NAT gateway was created. | [optional] 
**delete_time** | **datetime** | The date and time the NAT gateway was deleted, if applicable. | [optional] 
**failure_code** | **str** | If the NAT gateway could not be created, specifies the error code for the failure. (InsufficientFreeAddressesInSubnet | Gateway.NotAttached | InvalidAllocationID.NotFound | Resource.AlreadyAssociated | InternalError | InvalidSubnetID.NotFound) | [optional] 
**failure_message** | **str** | If the NAT gateway could not be created, specifies the error message for the failure, that corresponds to the error code.   * For InsufficientFreeAddressesInSubnet: \&quot;Subnet has insufficient free addresses to create this NAT gateway\&quot;   * For Gateway.NotAttached: \&quot;Network vpc-xxxxxxxx has no Internet gateway attached\&quot;   * For InvalidAllocationID.NotFound: \&quot;Elastic IP address eipalloc-xxxxxxxx could not be associated with this NAT gateway\&quot;   * For Resource.AlreadyAssociated: \&quot;Elastic IP address eipalloc-xxxxxxxx is already associated\&quot;   * For InternalError: \&quot;Network interface eni-xxxxxxxx, created and used internally by this NAT gateway is in an invalid state. Please try again.\&quot;   * For InvalidSubnetID.NotFound: \&quot;The specified subnet subnet-xxxxxxxx does not exist or could not be found.\&quot; | [optional] 
**nat_gateway_addresses** | [**list[AwsK8sServicesEc2V1alpha1NATGatewayStatusNatGatewayAddresses]**](AwsK8sServicesEc2V1alpha1NATGatewayStatusNatGatewayAddresses.md) | Information about the IP addresses and network interface associated with the NAT gateway. | [optional] 
**nat_gateway_id** | **str** | The ID of the NAT gateway. | [optional] 
**provisioned_bandwidth** | [**AwsK8sServicesEc2V1alpha1NATGatewayStatusProvisionedBandwidth**](AwsK8sServicesEc2V1alpha1NATGatewayStatusProvisionedBandwidth.md) |  | [optional] 
**state** | **str** | The state of the NAT gateway.   * pending: The NAT gateway is being created and is not ready to process traffic.   * failed: The NAT gateway could not be created. Check the failureCode and failureMessage fields for the reason.   * available: The NAT gateway is able to process traffic. This status remains until you delete the NAT gateway, and does not indicate the health of the NAT gateway.   * deleting: The NAT gateway is in the process of being terminated and may still be processing traffic.   * deleted: The NAT gateway has been terminated and is no longer processing traffic. | [optional] 
**vpc_id** | **str** | The ID of the VPC in which the NAT gateway is located. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


