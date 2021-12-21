# IoXK8sClusterControlplaneV1beta1AWSManagedControlPlaneStatusBastion

Bastion holds details of the instance that is used as a bastion jump box
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addresses** | [**list[IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneStatusBastionAddresses]**](IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneStatusBastionAddresses.md) | Addresses contains the AWS instance associated addresses. | [optional] 
**availability_zone** | **str** | Availability zone of instance | [optional] 
**ebs_optimized** | **bool** | Indicates whether the instance is optimized for Amazon EBS I/O. | [optional] 
**ena_support** | **bool** | Specifies whether enhanced networking with ENA is enabled. | [optional] 
**iam_profile** | **str** | The name of the IAM instance profile associated with the instance, if applicable. | [optional] 
**id** | **str** |  | 
**image_id** | **str** | The ID of the AMI used to launch the instance. | [optional] 
**instance_state** | **str** | The current state of the instance. | [optional] 
**network_interfaces** | **list[str]** | Specifies ENIs attached to instance | [optional] 
**non_root_volumes** | [**list[IoXK8sClusterControlplaneV1beta1AWSManagedControlPlaneStatusBastionNonRootVolumes]**](IoXK8sClusterControlplaneV1beta1AWSManagedControlPlaneStatusBastionNonRootVolumes.md) | Configuration options for the non root storage volumes. | [optional] 
**private_ip** | **str** | The private IPv4 address assigned to the instance. | [optional] 
**public_ip** | **str** | The public IPv4 address assigned to the instance, if applicable. | [optional] 
**root_volume** | [**IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastionRootVolume**](IoXK8sClusterControlplaneV1alpha4AWSManagedControlPlaneStatusBastionRootVolume.md) |  | [optional] 
**security_group_ids** | **list[str]** | SecurityGroupIDs are one or more security group IDs this instance belongs to. | [optional] 
**spot_market_options** | [**IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneStatusBastionSpotMarketOptions**](IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneStatusBastionSpotMarketOptions.md) |  | [optional] 
**ssh_key_name** | **str** | The name of the SSH key pair. | [optional] 
**subnet_id** | **str** | The ID of the subnet of the instance. | [optional] 
**tags** | **dict(str, str)** | The tags associated with the instance. | [optional] 
**tenancy** | **str** | Tenancy indicates if instance should run on shared or single-tenant hardware. | [optional] 
**type** | **str** | The instance type. | [optional] 
**user_data** | **str** | UserData is the raw data script passed to the instance which is run upon bootstrap. This field must not be base64 encoded and should only be used when running a new instance. | [optional] 
**volume_i_ds** | **list[str]** | IDs of the instance&#39;s volumes | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


