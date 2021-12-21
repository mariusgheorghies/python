# IoXK8sClusterInfrastructureV1alpha4AWSMachinePoolSpec

AWSMachinePoolSpec defines the desired state of AWSMachinePool
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_tags** | **dict(str, str)** | AdditionalTags is an optional set of tags to add to an instance, in addition to the ones added by default by the AWS provider. | [optional] 
**availability_zones** | **list[str]** | AvailabilityZones is an array of availability zones instances can run in | [optional] 
**aws_launch_template** | [**IoXK8sClusterInfrastructureV1alpha4AWSMachinePoolSpecAwsLaunchTemplate**](IoXK8sClusterInfrastructureV1alpha4AWSMachinePoolSpecAwsLaunchTemplate.md) |  | 
**capacity_rebalance** | **bool** | Enable or disable the capacity rebalance autoscaling group feature | [optional] 
**default_cool_down** | **str** | The amount of time, in seconds, after a scaling activity completes before another scaling activity can start. If no value is supplied by user a default value of 300 seconds is set | [optional] 
**max_size** | **int** | MaxSize defines the maximum size of the group. | 
**min_size** | **int** | MinSize defines the minimum size of the group. | 
**mixed_instances_policy** | [**IoXK8sClusterInfrastructureV1alpha3AWSMachinePoolSpecMixedInstancesPolicy**](IoXK8sClusterInfrastructureV1alpha3AWSMachinePoolSpecMixedInstancesPolicy.md) |  | [optional] 
**provider_id** | **str** | ProviderID is the ARN of the associated ASG | [optional] 
**provider_id_list** | **list[str]** | ProviderIDList are the identification IDs of machine instances provided by the provider. This field must match the provider IDs as seen on the node objects corresponding to a machine pool&#39;s machine instances. | [optional] 
**refresh_preferences** | [**IoXK8sClusterInfrastructureV1alpha3AWSMachinePoolSpecRefreshPreferences**](IoXK8sClusterInfrastructureV1alpha3AWSMachinePoolSpecRefreshPreferences.md) |  | [optional] 
**subnets** | [**list[IoXK8sClusterInfrastructureV1alpha3AWSMachineSpecAdditionalSecurityGroups]**](IoXK8sClusterInfrastructureV1alpha3AWSMachineSpecAdditionalSecurityGroups.md) | Subnets is an array of subnet configurations | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


