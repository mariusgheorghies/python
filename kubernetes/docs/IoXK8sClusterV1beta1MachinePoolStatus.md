# IoXK8sClusterV1beta1MachinePoolStatus

MachinePoolStatus defines the observed state of MachinePool.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available_replicas** | **int** | The number of available replicas (ready for at least minReadySeconds) for this MachinePool. | [optional] 
**bootstrap_ready** | **bool** | BootstrapReady is the state of the bootstrap provider. | [optional] 
**conditions** | [**list[IoXK8sClusterAddonsV1beta1ClusterResourceSetStatusConditions]**](IoXK8sClusterAddonsV1beta1ClusterResourceSetStatusConditions.md) | Conditions define the current service state of the MachinePool. | [optional] 
**failure_message** | **str** | FailureMessage indicates that there is a problem reconciling the state, and will be set to a descriptive error message. | [optional] 
**failure_reason** | **str** | FailureReason indicates that there is a problem reconciling the state, and will be set to a token value suitable for programmatic interpretation. | [optional] 
**infrastructure_ready** | **bool** | InfrastructureReady is the state of the infrastructure provider. | [optional] 
**node_refs** | [**list[IoXK8sClusterV1alpha3MachinePoolStatusNodeRefs]**](IoXK8sClusterV1alpha3MachinePoolStatusNodeRefs.md) | NodeRefs will point to the corresponding Nodes if it they exist. | [optional] 
**observed_generation** | **int** | ObservedGeneration is the latest generation observed by the controller. | [optional] 
**phase** | **str** | Phase represents the current phase of cluster actuation. E.g. Pending, Running, Terminating, Failed etc. | [optional] 
**ready_replicas** | **int** | The number of ready replicas for this MachinePool. A machine is considered ready when the node has been created and is \&quot;Ready\&quot;. | [optional] 
**replicas** | **int** | Replicas is the most recently observed number of replicas. | [optional] 
**unavailable_replicas** | **int** | Total number of unavailable machine instances targeted by this machine pool. This is the total number of machine instances that are still required for the machine pool to have 100% available capacity. They may either be machine instances that are running but not yet available or machine instances that still have not been created. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


