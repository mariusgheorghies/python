# IoXK8sClusterV1alpha3MachineStatus

MachineStatus defines the observed state of Machine.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addresses** | [**list[IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneStatusBastionAddresses]**](IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneStatusBastionAddresses.md) | Addresses is a list of addresses assigned to the machine. This field is copied from the infrastructure provider reference. | [optional] 
**bootstrap_ready** | **bool** | BootstrapReady is the state of the bootstrap provider. | [optional] 
**conditions** | [**list[IoXK8sClusterAddonsV1alpha3ClusterResourceSetStatusConditions]**](IoXK8sClusterAddonsV1alpha3ClusterResourceSetStatusConditions.md) | Conditions defines current service state of the Machine. | [optional] 
**failure_message** | **str** | FailureMessage will be set in the event that there is a terminal problem reconciling the Machine and will contain a more verbose string suitable for logging and human consumption.   This field should not be set for transitive errors that a controller faces that are expected to be fixed automatically over time (like service outages), but instead indicate that something is fundamentally wrong with the Machine&#39;s spec or the configuration of the controller, and that manual intervention is required. Examples of terminal errors would be invalid combinations of settings in the spec, values that are unsupported by the controller, or the responsible controller itself being critically misconfigured.   Any transient errors that occur during the reconciliation of Machines can be added as events to the Machine object and/or logged in the controller&#39;s output. | [optional] 
**failure_reason** | **str** | FailureReason will be set in the event that there is a terminal problem reconciling the Machine and will contain a succinct value suitable for machine interpretation.   This field should not be set for transitive errors that a controller faces that are expected to be fixed automatically over time (like service outages), but instead indicate that something is fundamentally wrong with the Machine&#39;s spec or the configuration of the controller, and that manual intervention is required. Examples of terminal errors would be invalid combinations of settings in the spec, values that are unsupported by the controller, or the responsible controller itself being critically misconfigured.   Any transient errors that occur during the reconciliation of Machines can be added as events to the Machine object and/or logged in the controller&#39;s output. | [optional] 
**infrastructure_ready** | **bool** | InfrastructureReady is the state of the infrastructure provider. | [optional] 
**last_updated** | **datetime** | LastUpdated identifies when the phase of the Machine last transitioned. | [optional] 
**node_ref** | [**IoXK8sClusterV1alpha3MachineStatusNodeRef**](IoXK8sClusterV1alpha3MachineStatusNodeRef.md) |  | [optional] 
**observed_generation** | **int** | ObservedGeneration is the latest generation observed by the controller. | [optional] 
**phase** | **str** | Phase represents the current phase of machine actuation. E.g. Pending, Running, Terminating, Failed etc. | [optional] 
**version** | **str** | Version specifies the current version of Kubernetes running on the corresponding Node. This is meant to be a means of bubbling up status from the Node to the Machine. It is entirely optional, but useful for end-user UX if it’s present. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


