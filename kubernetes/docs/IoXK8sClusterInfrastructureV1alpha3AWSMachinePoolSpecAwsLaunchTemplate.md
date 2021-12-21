# IoXK8sClusterInfrastructureV1alpha3AWSMachinePoolSpecAwsLaunchTemplate

AWSLaunchTemplate specifies the launch template and version to use when an instance is launched.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_security_groups** | [**list[IoXK8sClusterInfrastructureV1alpha3AWSMachineSpecAdditionalSecurityGroups]**](IoXK8sClusterInfrastructureV1alpha3AWSMachineSpecAdditionalSecurityGroups.md) | AdditionalSecurityGroups is an array of references to security groups that should be applied to the instances. These security groups would be set in addition to any security groups defined at the cluster level or in the actuator. | [optional] 
**ami** | [**IoXK8sClusterInfrastructureV1alpha3AWSMachineSpecAmi**](IoXK8sClusterInfrastructureV1alpha3AWSMachineSpecAmi.md) |  | [optional] 
**iam_instance_profile** | **str** | The name or the Amazon Resource Name (ARN) of the instance profile associated with the IAM role for the instance. The instance profile contains the IAM role. | [optional] 
**image_lookup_base_os** | **str** | ImageLookupBaseOS is the name of the base operating system to use for image lookup the AMI is not set. | [optional] 
**image_lookup_format** | **str** | ImageLookupFormat is the AMI naming format to look up the image for this machine It will be ignored if an explicit AMI is set. Supports substitutions for {{.BaseOS}} and {{.K8sVersion}} with the base OS and kubernetes version, respectively. The BaseOS will be the value in ImageLookupBaseOS or ubuntu (the default), and the kubernetes version as defined by the packages produced by kubernetes/release without v as a prefix: 1.13.0, 1.12.5-mybuild.1, or 1.17.3. For example, the default image format of capa-ami-{{.BaseOS}}-?{{.K8sVersion}}-* will end up searching for AMIs that match the pattern capa-ami-ubuntu-?1.18.0-* for a Machine that is targeting kubernetes v1.18.0 and the ubuntu base OS. See also: https://golang.org/pkg/text/template/ | [optional] 
**image_lookup_org** | **str** | ImageLookupOrg is the AWS Organization ID to use for image lookup if AMI is not set. | [optional] 
**instance_type** | **str** | InstanceType is the type of instance to create. Example: m4.xlarge | [optional] 
**name** | **str** | The name of the launch template. | [optional] 
**root_volume** | [**IoXK8sClusterInfrastructureV1alpha3AWSMachineSpecRootVolume**](IoXK8sClusterInfrastructureV1alpha3AWSMachineSpecRootVolume.md) |  | [optional] 
**ssh_key_name** | **str** | SSHKeyName is the name of the ssh key to attach to the instance. Valid values are empty string (do not use SSH keys), a valid SSH key name, or omitted (use the default SSH key name) | [optional] 
**version_number** | **int** | VersionNumber is the version of the launch template that is applied. Typically a new version is created when at least one of the following happens: 1) A new launch template spec is applied. 2) One or more parameters in an existing template is changed. 3) A new AMI is discovered. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


