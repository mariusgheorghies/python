# IoXK8sClusterInfrastructureV1beta1AWSMachineSpec

AWSMachineSpec defines the desired state of an Amazon EC2 instance.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_security_groups** | [**list[IoXK8sClusterInfrastructureV1beta1AWSMachineSpecAdditionalSecurityGroups]**](IoXK8sClusterInfrastructureV1beta1AWSMachineSpecAdditionalSecurityGroups.md) | AdditionalSecurityGroups is an array of references to security groups that should be applied to the instance. These security groups would be set in addition to any security groups defined at the cluster level or in the actuator. It is possible to specify either IDs of Filters. Using Filters will cause additional requests to AWS API and if tags change the attached security groups might change too. | [optional] 
**additional_tags** | **dict(str, str)** | AdditionalTags is an optional set of tags to add to an instance, in addition to the ones added by default by the AWS provider. If both the AWSCluster and the AWSMachine specify the same tag name with different values, the AWSMachine&#39;s value takes precedence. | [optional] 
**ami** | [**IoXK8sClusterInfrastructureV1alpha4AWSMachineSpecAmi**](IoXK8sClusterInfrastructureV1alpha4AWSMachineSpecAmi.md) |  | [optional] 
**cloud_init** | [**IoXK8sClusterInfrastructureV1alpha3AWSMachineSpecCloudInit**](IoXK8sClusterInfrastructureV1alpha3AWSMachineSpecCloudInit.md) |  | [optional] 
**failure_domain** | **str** | FailureDomain is the failure domain unique identifier this Machine should be attached to, as defined in Cluster API. For this infrastructure provider, the ID is equivalent to an AWS Availability Zone. If multiple subnets are matched for the availability zone, the first one returned is picked. | [optional] 
**iam_instance_profile** | **str** | IAMInstanceProfile is a name of an IAM instance profile to assign to the instance | [optional] 
**image_lookup_base_os** | **str** | ImageLookupBaseOS is the name of the base operating system to use for image lookup the AMI is not set. | [optional] 
**image_lookup_format** | **str** | ImageLookupFormat is the AMI naming format to look up the image for this machine It will be ignored if an explicit AMI is set. Supports substitutions for {{.BaseOS}} and {{.K8sVersion}} with the base OS and kubernetes version, respectively. The BaseOS will be the value in ImageLookupBaseOS or ubuntu (the default), and the kubernetes version as defined by the packages produced by kubernetes/release without v as a prefix: 1.13.0, 1.12.5-mybuild.1, or 1.17.3. For example, the default image format of capa-ami-{{.BaseOS}}-?{{.K8sVersion}}-* will end up searching for AMIs that match the pattern capa-ami-ubuntu-?1.18.0-* for a Machine that is targeting kubernetes v1.18.0 and the ubuntu base OS. See also: https://golang.org/pkg/text/template/ | [optional] 
**image_lookup_org** | **str** | ImageLookupOrg is the AWS Organization ID to use for image lookup if AMI is not set. | [optional] 
**instance_id** | **str** | InstanceID is the EC2 instance ID for this machine. | [optional] 
**instance_type** | **str** | InstanceType is the type of instance to create. Example: m4.xlarge | 
**network_interfaces** | **list[str]** | NetworkInterfaces is a list of ENIs to associate with the instance. A maximum of 2 may be specified. | [optional] 
**non_root_volumes** | [**list[IoXK8sClusterControlplaneV1beta1AWSManagedControlPlaneStatusBastionNonRootVolumes]**](IoXK8sClusterControlplaneV1beta1AWSManagedControlPlaneStatusBastionNonRootVolumes.md) | Configuration options for the non root storage volumes. | [optional] 
**provider_id** | **str** | ProviderID is the unique identifier as specified by the cloud provider. | [optional] 
**public_ip** | **bool** | PublicIP specifies whether the instance should get a public IP. Precedence for this setting is as follows: 1. This field if set 2. Cluster/flavor setting 3. Subnet default | [optional] 
**root_volume** | [**IoXK8sClusterInfrastructureV1alpha4AWSMachineSpecRootVolume**](IoXK8sClusterInfrastructureV1alpha4AWSMachineSpecRootVolume.md) |  | [optional] 
**spot_market_options** | [**IoXK8sClusterInfrastructureV1alpha3AWSMachineSpecSpotMarketOptions**](IoXK8sClusterInfrastructureV1alpha3AWSMachineSpecSpotMarketOptions.md) |  | [optional] 
**ssh_key_name** | **str** | SSHKeyName is the name of the ssh key to attach to the instance. Valid values are empty string (do not use SSH keys), a valid SSH key name, or omitted (use the default SSH key name) | [optional] 
**subnet** | [**IoXK8sClusterInfrastructureV1beta1AWSMachineSpecSubnet**](IoXK8sClusterInfrastructureV1beta1AWSMachineSpecSubnet.md) |  | [optional] 
**tenancy** | **str** | Tenancy indicates if instance should run on shared or single-tenant hardware. | [optional] 
**uncompressed_user_data** | **bool** | UncompressedUserData specify whether the user data is gzip-compressed before it is sent to ec2 instance. cloud-init has built-in support for gzip-compressed user data user data stored in aws secret manager is always gzip-compressed. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


