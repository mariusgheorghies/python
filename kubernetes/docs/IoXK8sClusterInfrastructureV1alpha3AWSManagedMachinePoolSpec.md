# IoXK8sClusterInfrastructureV1alpha3AWSManagedMachinePoolSpec

AWSManagedMachinePoolSpec defines the desired state of AWSManagedMachinePool
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_tags** | **dict(str, str)** | AdditionalTags is an optional set of tags to add to AWS resources managed by the AWS provider, in addition to the ones added by default. | [optional] 
**ami_type** | **str** | AMIType defines the AMI type | [optional] 
**ami_version** | **str** | AMIVersion defines the desired AMI release version. If no version number is supplied then the latest version for the Kubernetes version will be used | [optional] 
**availability_zones** | **list[str]** | AvailabilityZones is an array of availability zones instances can run in | [optional] 
**disk_size** | **int** | DiskSize specifies the root disk size | [optional] 
**eks_nodegroup_name** | **str** | EKSNodegroupName specifies the name of the nodegroup in AWS corresponding to this MachinePool. If you don&#39;t specify a name then a default name will be created based on the namespace and name of the managed machine pool. | [optional] 
**instance_type** | **str** | InstanceType specifies the AWS instance type | [optional] 
**labels** | **dict(str, str)** | Labels specifies labels for the Kubernetes node objects | [optional] 
**provider_id_list** | **list[str]** | ProviderIDList are the provider IDs of instances in the autoscaling group corresponding to the nodegroup represented by this machine pool | [optional] 
**remote_access** | [**IoXK8sClusterInfrastructureV1alpha3AWSManagedMachinePoolSpecRemoteAccess**](IoXK8sClusterInfrastructureV1alpha3AWSManagedMachinePoolSpecRemoteAccess.md) |  | [optional] 
**role_name** | **str** | RoleName specifies the name of IAM role for the node group. If the role is pre-existing we will treat it as unmanaged and not delete it on deletion. If the EKSEnableIAM feature flag is true and no name is supplied then a role is created. | [optional] 
**scaling** | [**IoXK8sClusterInfrastructureV1alpha3AWSManagedMachinePoolSpecScaling**](IoXK8sClusterInfrastructureV1alpha3AWSManagedMachinePoolSpecScaling.md) |  | [optional] 
**subnet_i_ds** | **list[str]** | SubnetIDs specifies which subnets are used for the auto scaling group of this nodegroup | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


