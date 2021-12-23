# IoXK8sClusterInfrastructureV1alpha3AWSMachinePoolSpecMixedInstancesPolicyInstancesDistribution

InstancesDistribution to configure distribution of On-Demand Instances and Spot Instances.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**on_demand_allocation_strategy** | **str** | OnDemandAllocationStrategy indicates how to allocate instance types to fulfill On-Demand capacity. | [optional] 
**on_demand_base_capacity** | **int** |  | [optional] 
**on_demand_percentage_above_base_capacity** | **int** |  | [optional] 
**spot_allocation_strategy** | **str** | SpotAllocationStrategy indicates how to allocate instances across Spot Instance pools. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


