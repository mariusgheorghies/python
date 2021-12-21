# IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneSpec

AWSManagedControlPlaneSpec defines the desired state of AWSManagedControlPlane
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_tags** | **dict(str, str)** | AdditionalTags is an optional set of tags to add to AWS resources managed by the AWS provider, in addition to the ones added by default. | [optional] 
**addons** | [**list[IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneSpecAddons]**](IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneSpecAddons.md) | Addons defines the EKS addons to enable with the EKS cluster. | [optional] 
**associate_oidc_provider** | **bool** | AssociateOIDCProvider can be enabled to automatically create an identity provider for the controller for use with IAM roles for service accounts | [optional] 
**bastion** | [**IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneSpecBastion**](IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneSpecBastion.md) |  | [optional] 
**control_plane_endpoint** | [**IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneSpecControlPlaneEndpoint**](IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneSpecControlPlaneEndpoint.md) |  | [optional] 
**disable_vpccni** | **bool** | DisableVPCCNI indcates the the Amazon VPC CNI should be disabled. With EKS clusters that the Amazon VPC CNI is automatically installed into the cluster. For clusters where you want to use an alternate CNI this option provides a way to specify that the Amazon VPC CNI should be deleted. You cannot set this to true if you are using the Amazon VPC CNI addon or if you have specified a secondary CIDR block. | [optional] 
**eks_cluster_name** | **str** | EKSClusterName allows you to specify the name of the EKS cluster in AWS. If you don&#39;t specify a name then a default name will be created based on the namespace and name of the managed control plane. | [optional] 
**encryption_config** | [**IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneSpecEncryptionConfig**](IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneSpecEncryptionConfig.md) |  | [optional] 
**endpoint_access** | [**IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneSpecEndpointAccess**](IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneSpecEndpointAccess.md) |  | [optional] 
**iam_authenticator_config** | [**IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneSpecIamAuthenticatorConfig**](IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneSpecIamAuthenticatorConfig.md) |  | [optional] 
**identity_ref** | [**IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneSpecIdentityRef**](IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneSpecIdentityRef.md) |  | [optional] 
**image_lookup_base_os** | **str** | ImageLookupBaseOS is the name of the base operating system used to look up machine images when a machine does not specify an AMI. When set, this will be used for all cluster machines unless a machine specifies a different ImageLookupBaseOS. | [optional] 
**image_lookup_format** | **str** | ImageLookupFormat is the AMI naming format to look up machine images when a machine does not specify an AMI. When set, this will be used for all cluster machines unless a machine specifies a different ImageLookupOrg. Supports substitutions for {{.BaseOS}} and {{.K8sVersion}} with the base OS and kubernetes version, respectively. The BaseOS will be the value in ImageLookupBaseOS or ubuntu (the default), and the kubernetes version as defined by the packages produced by kubernetes/release without v as a prefix: 1.13.0, 1.12.5-mybuild.1, or 1.17.3. For example, the default image format of capa-ami-{{.BaseOS}}-?{{.K8sVersion}}-* will end up searching for AMIs that match the pattern capa-ami-ubuntu-?1.18.0-* for a Machine that is targeting kubernetes v1.18.0 and the ubuntu base OS. See also: https://golang.org/pkg/text/template/ | [optional] 
**image_lookup_org** | **str** | ImageLookupOrg is the AWS Organization ID to look up machine images when a machine does not specify an AMI. When set, this will be used for all cluster machines unless a machine specifies a different ImageLookupOrg. | [optional] 
**logging** | [**IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneSpecLogging**](IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneSpecLogging.md) |  | [optional] 
**network_spec** | [**IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneSpecNetworkSpec**](IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneSpecNetworkSpec.md) |  | [optional] 
**region** | **str** | The AWS Region the cluster lives in. | [optional] 
**role_additional_policies** | **list[str]** | RoleAdditionalPolicies allows you to attach additional polices to the control plane role. You must enable the EKSAllowAddRoles feature flag to incorporate these into the created role. | [optional] 
**role_name** | **str** | RoleName specifies the name of IAM role that gives EKS permission to make API calls. If the role is pre-existing we will treat it as unmanaged and not delete it on deletion. If the EKSEnableIAM feature flag is true and no name is supplied then a role is created. | [optional] 
**secondary_cidr_block** | **str** | SecondaryCidrBlock is the additional CIDR range to use for pod IPs. Must be within the 100.64.0.0/10 or 198.19.0.0/16 range. | [optional] 
**ssh_key_name** | **str** | SSHKeyName is the name of the ssh key to attach to the bastion host. Valid values are empty string (do not use SSH keys), a valid SSH key name, or omitted (use the default SSH key name) | [optional] 
**token_method** | **str** | TokenMethod is used to specify the method for obtaining a kubernetes.client token for communicating with EKS iam-authenticator - obtains a kubernetes.client token using iam-authentictor aws-cli - obtains a kubernetes.client token using the AWS CLI Defaults to iam-authenticator | [optional] 
**version** | **str** | Version defines the desired Kubernetes version. If no version number is supplied then the latest version of Kubernetes that EKS supports will be used. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


