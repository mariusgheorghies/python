# AwsK8sServicesEc2V1alpha1InstanceStatus

InstanceStatus defines the observed state of Instance
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ack_resource_metadata** | [**AwsK8sServicesEc2V1alpha1DHCPOptionsStatusAckResourceMetadata**](AwsK8sServicesEc2V1alpha1DHCPOptionsStatusAckResourceMetadata.md) |  | [optional] 
**ami_launch_index** | **int** | The AMI launch index, which can be used to find this instance in the launch group. | [optional] 
**architecture** | **str** | The architecture of the image. | [optional] 
**boot_mode** | **str** | The boot mode of the instance. For more information, see Boot modes (https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ami-boot.html) in the Amazon EC2 User Guide. | [optional] 
**capacity_reservation_id** | **str** | The ID of the Capacity Reservation. | [optional] 
**conditions** | [**list[AwsK8sServicesEc2V1alpha1DHCPOptionsStatusConditions]**](AwsK8sServicesEc2V1alpha1DHCPOptionsStatusConditions.md) | All CRS managed by ACK have a common &#x60;Status.Conditions&#x60; member that contains a collection of &#x60;ackv1alpha1.Condition&#x60; objects that describe the various terminal states of the CR and its backend AWS service API resource | [optional] 
**elastic_gpu_associations** | [**list[AwsK8sServicesEc2V1alpha1InstanceStatusElasticGPUAssociations]**](AwsK8sServicesEc2V1alpha1InstanceStatusElasticGPUAssociations.md) | The Elastic GPU associated with the instance. | [optional] 
**elastic_inference_accelerator_associations** | [**list[AwsK8sServicesEc2V1alpha1InstanceStatusElasticInferenceAcceleratorAssociations]**](AwsK8sServicesEc2V1alpha1InstanceStatusElasticInferenceAcceleratorAssociations.md) | The elastic inference accelerator associated with the instance. | [optional] 
**ena_support** | **bool** | Specifies whether enhanced networking with ENA is enabled. | [optional] 
**hypervisor** | **str** | The hypervisor type of the instance. The value xen is used for both Xen and Nitro hypervisors. | [optional] 
**instance_id** | **str** | The ID of the instance. | [optional] 
**instance_lifecycle** | **str** | Indicates whether this is a Spot Instance or a Scheduled Instance. | [optional] 
**ipv6_address** | **str** | The IPv6 address assigned to the instance. | [optional] 
**launch_time** | **datetime** | The time the instance was launched. | [optional] 
**licenses** | [**list[AwsK8sServicesEc2V1alpha1InstanceSpecLicenseSpecifications]**](AwsK8sServicesEc2V1alpha1InstanceSpecLicenseSpecifications.md) | The license configurations for the instance. | [optional] 
**outpost_arn** | **str** | The Amazon Resource Name (ARN) of the Outpost. | [optional] 
**platform** | **str** | The value is Windows for Windows instances; otherwise blank. | [optional] 
**platform_details** | **str** | The platform details value for the instance. For more information, see AMI billing information fields (https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/billing-info-fields.html) in the Amazon EC2 User Guide. | [optional] 
**private_dns_name** | **str** | (IPv4 only) The private DNS hostname name assigned to the instance. This DNS hostname can only be used inside the Amazon EC2 network. This name is not available until the instance enters the running state.   [EC2-VPC] The Amazon-provided DNS server resolves Amazon-provided private DNS hostnames if you&#39;ve enabled DNS resolution and DNS hostnames in your VPC. If you are not using the Amazon-provided DNS server in your VPC, your custom domain name servers must resolve the hostname as appropriate. | [optional] 
**product_codes** | [**list[AwsK8sServicesEc2V1alpha1InstanceStatusProductCodes]**](AwsK8sServicesEc2V1alpha1InstanceStatusProductCodes.md) | The product codes attached to this instance, if applicable. | [optional] 
**public_dns_name** | **str** | (IPv4 only) The public DNS name assigned to the instance. This name is not available until the instance enters the running state. For EC2-VPC, this name is only available if you&#39;ve enabled DNS hostnames for your VPC. | [optional] 
**public_ip_address** | **str** | The public IPv4 address, or the Carrier IP address assigned to the instance, if applicable.   A Carrier IP address only applies to an instance launched in a subnet associated with a Wavelength Zone. | [optional] 
**root_device_name** | **str** | The device name of the root device volume (for example, /dev/sda1). | [optional] 
**root_device_type** | **str** | The root device type used by the AMI. The AMI can use an EBS volume or an instance store volume. | [optional] 
**source_dest_check** | **bool** | Indicates whether source/destination checking is enabled. | [optional] 
**spot_instance_request_id** | **str** | If the request is a Spot Instance request, the ID of the request. | [optional] 
**sriov_net_support** | **str** | Specifies whether enhanced networking with the Intel 82599 Virtual Function interface is enabled. | [optional] 
**state** | [**AwsK8sServicesEc2V1alpha1InstanceStatusState**](AwsK8sServicesEc2V1alpha1InstanceStatusState.md) |  | [optional] 
**state_reason** | [**AwsK8sServicesEc2V1alpha1InstanceStatusStateReason**](AwsK8sServicesEc2V1alpha1InstanceStatusStateReason.md) |  | [optional] 
**state_transition_reason** | **str** | The reason for the most recent state transition. This might be an empty string. | [optional] 
**tpm_support** | **str** | If the instance is configured for NitroTPM support, the value is v2.0. For more information, see NitroTPM (https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/nitrotpm.html) in the Amazon EC2 User Guide. | [optional] 
**usage_operation** | **str** | The usage operation value for the instance. For more information, see AMI billing information fields (https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/billing-info-fields.html) in the Amazon EC2 User Guide. | [optional] 
**usage_operation_update_time** | **datetime** | The time that the usage operation was last updated. | [optional] 
**virtualization_type** | **str** | The virtualization type of the instance. | [optional] 
**vpc_id** | **str** | [EC2-VPC] The ID of the VPC in which the instance is running. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


