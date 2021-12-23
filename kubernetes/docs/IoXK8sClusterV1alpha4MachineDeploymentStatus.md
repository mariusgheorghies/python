# IoXK8sClusterV1alpha4MachineDeploymentStatus

MachineDeploymentStatus defines the observed state of MachineDeployment.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available_replicas** | **int** | Total number of available machines (ready for at least minReadySeconds) targeted by this deployment. | [optional] 
**conditions** | [**list[IoXK8sClusterAddonsV1alpha3ClusterResourceSetStatusConditions]**](IoXK8sClusterAddonsV1alpha3ClusterResourceSetStatusConditions.md) | Conditions defines current service state of the MachineDeployment. | [optional] 
**observed_generation** | **int** | The generation observed by the deployment controller. | [optional] 
**phase** | **str** | Phase represents the current phase of a MachineDeployment (ScalingUp, ScalingDown, Running, Failed, or Unknown). | [optional] 
**ready_replicas** | **int** | Total number of ready machines targeted by this deployment. | [optional] 
**replicas** | **int** | Total number of non-terminated machines targeted by this deployment (their labels match the selector). | [optional] 
**selector** | **str** | Selector is the same as the label selector but in the string format to avoid introspection by kubernetes.clients. The string will be in the same format as the query-param syntax. More info about label selectors: http://kubernetes.io/docs/user-guide/labels#label-selectors | [optional] 
**unavailable_replicas** | **int** | Total number of unavailable machines targeted by this deployment. This is the total number of machines that are still required for the deployment to have 100% available capacity. They may either be machines that are running but not yet available or machines that still have not been created. | [optional] 
**updated_replicas** | **int** | Total number of non-terminated machines targeted by this deployment that have the desired template spec. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


