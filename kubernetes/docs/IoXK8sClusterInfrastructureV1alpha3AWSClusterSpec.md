# IoXK8sClusterInfrastructureV1alpha3AWSClusterSpec

AWSClusterSpec defines the desired state of AWSCluster.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_tags** | **dict(str, str)** | AdditionalTags is an optional set of tags to add to AWS resources managed by the AWS provider, in addition to the ones added by default. | [optional] 
**bastion** | [**IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneSpecBastion**](IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneSpecBastion.md) |  | [optional] 
**control_plane_endpoint** | [**IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneSpecControlPlaneEndpoint**](IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneSpecControlPlaneEndpoint.md) |  | [optional] 
**control_plane_load_balancer** | [**IoXK8sClusterInfrastructureV1alpha3AWSClusterSpecControlPlaneLoadBalancer**](IoXK8sClusterInfrastructureV1alpha3AWSClusterSpecControlPlaneLoadBalancer.md) |  | [optional] 
**identity_ref** | [**IoXK8sClusterInfrastructureV1alpha3AWSClusterSpecIdentityRef**](IoXK8sClusterInfrastructureV1alpha3AWSClusterSpecIdentityRef.md) |  | [optional] 
**image_lookup_base_os** | **str** | ImageLookupBaseOS is the name of the base operating system used to look up machine images when a machine does not specify an AMI. When set, this will be used for all cluster machines unless a machine specifies a different ImageLookupBaseOS. | [optional] 
**image_lookup_format** | **str** | ImageLookupFormat is the AMI naming format to look up machine images when a machine does not specify an AMI. When set, this will be used for all cluster machines unless a machine specifies a different ImageLookupOrg. Supports substitutions for {{.BaseOS}} and {{.K8sVersion}} with the base OS and kubernetes version, respectively. The BaseOS will be the value in ImageLookupBaseOS or ubuntu (the default), and the kubernetes version as defined by the packages produced by kubernetes/release without v as a prefix: 1.13.0, 1.12.5-mybuild.1, or 1.17.3. For example, the default image format of capa-ami-{{.BaseOS}}-?{{.K8sVersion}}-* will end up searching for AMIs that match the pattern capa-ami-ubuntu-?1.18.0-* for a Machine that is targeting kubernetes v1.18.0 and the ubuntu base OS. See also: https://golang.org/pkg/text/template/ | [optional] 
**image_lookup_org** | **str** | ImageLookupOrg is the AWS Organization ID to look up machine images when a machine does not specify an AMI. When set, this will be used for all cluster machines unless a machine specifies a different ImageLookupOrg. | [optional] 
**network_spec** | [**IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneSpecNetworkSpec**](IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneSpecNetworkSpec.md) |  | [optional] 
**region** | **str** | The AWS Region the cluster lives in. | [optional] 
**ssh_key_name** | **str** | SSHKeyName is the name of the ssh key to attach to the bastion host. Valid values are empty string (do not use SSH keys), a valid SSH key name, or omitted (use the default SSH key name) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


