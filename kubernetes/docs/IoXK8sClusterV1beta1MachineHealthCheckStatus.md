# IoXK8sClusterV1beta1MachineHealthCheckStatus

Most recently observed status of MachineHealthCheck resource
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | [**list[IoXK8sClusterAddonsV1beta1ClusterResourceSetStatusConditions]**](IoXK8sClusterAddonsV1beta1ClusterResourceSetStatusConditions.md) | Conditions defines current service state of the MachineHealthCheck. | [optional] 
**current_healthy** | **int** | total number of healthy machines counted by this machine health check | [optional] 
**expected_machines** | **int** | total number of machines counted by this machine health check | [optional] 
**observed_generation** | **int** | ObservedGeneration is the latest generation observed by the controller. | [optional] 
**remediations_allowed** | **int** | RemediationsAllowed is the number of further remediations allowed by this machine health check before maxUnhealthy short circuiting will be applied | [optional] 
**targets** | **list[str]** | Targets shows the current list of machines the machine health check is watching | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


