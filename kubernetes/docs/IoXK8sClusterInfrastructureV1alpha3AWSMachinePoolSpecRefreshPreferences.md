# IoXK8sClusterInfrastructureV1alpha3AWSMachinePoolSpecRefreshPreferences

RefreshPreferences describes set of preferences associated with the instance refresh request.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instance_warmup** | **int** | The number of seconds until a newly launched instance is configured and ready to use. During this time, the next replacement will not be initiated. The default is to use the value for the health check grace period defined for the group. | [optional] 
**min_healthy_percentage** | **int** | The amount of capacity as a percentage in ASG that must remain healthy during an instance refresh. The default is 90. | [optional] 
**strategy** | **str** | The strategy to use for the instance refresh. The only valid value is Rolling. A rolling update is an update that is applied to all instances in an Auto Scaling group until all instances have been updated. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


