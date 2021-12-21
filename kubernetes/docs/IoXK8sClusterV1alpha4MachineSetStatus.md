# IoXK8sClusterV1alpha4MachineSetStatus

MachineSetStatus defines the observed state of MachineSet.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available_replicas** | **int** | The number of available replicas (ready for at least minReadySeconds) for this MachineSet. | [optional] 
**conditions** | [**list[IoXK8sClusterAddonsV1alpha3ClusterResourceSetStatusConditions]**](IoXK8sClusterAddonsV1alpha3ClusterResourceSetStatusConditions.md) | Conditions defines current service state of the MachineSet. | [optional] 
**failure_message** | **str** |  | [optional] 
**failure_reason** | **str** | In the event that there is a terminal problem reconciling the replicas, both FailureReason and FailureMessage will be set. FailureReason will be populated with a succinct value suitable for machine interpretation, while FailureMessage will contain a more verbose string suitable for logging and human consumption.   These fields should not be set for transitive errors that a controller faces that are expected to be fixed automatically over time (like service outages), but instead indicate that something is fundamentally wrong with the MachineTemplate&#39;s spec or the configuration of the machine controller, and that manual intervention is required. Examples of terminal errors would be invalid combinations of settings in the spec, values that are unsupported by the machine controller, or the responsible machine controller itself being critically misconfigured.   Any transient errors that occur during the reconciliation of Machines can be added as events to the MachineSet object and/or logged in the controller&#39;s output. | [optional] 
**fully_labeled_replicas** | **int** | The number of replicas that have labels matching the labels of the machine template of the MachineSet. | [optional] 
**observed_generation** | **int** | ObservedGeneration reflects the generation of the most recently observed MachineSet. | [optional] 
**ready_replicas** | **int** | The number of ready replicas for this MachineSet. A machine is considered ready when the node has been created and is \&quot;Ready\&quot;. | [optional] 
**replicas** | **int** | Replicas is the most recently observed number of replicas. | [optional] 
**selector** | **str** | Selector is the same as the label selector but in the string format to avoid introspection by kubernetes.clients. The string will be in the same format as the query-param syntax. More info about label selectors: http://kubernetes.io/docs/user-guide/labels#label-selectors | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


