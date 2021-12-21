# IoXK8sClusterV1beta1ClusterStatus

ClusterStatus defines the observed state of Cluster.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | [**list[IoXK8sClusterAddonsV1beta1ClusterResourceSetStatusConditions]**](IoXK8sClusterAddonsV1beta1ClusterResourceSetStatusConditions.md) | Conditions defines current service state of the cluster. | [optional] 
**control_plane_ready** | **bool** | ControlPlaneReady defines if the control plane is ready. | [optional] 
**failure_domains** | [**dict(str, IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneStatusFailureDomains)**](IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneStatusFailureDomains.md) | FailureDomains is a slice of failure domain objects synced from the infrastructure provider. | [optional] 
**failure_message** | **str** | FailureMessage indicates that there is a fatal problem reconciling the state, and will be set to a descriptive error message. | [optional] 
**failure_reason** | **str** | FailureReason indicates that there is a fatal problem reconciling the state, and will be set to a token value suitable for programmatic interpretation. | [optional] 
**infrastructure_ready** | **bool** | InfrastructureReady is the state of the infrastructure provider. | [optional] 
**observed_generation** | **int** | ObservedGeneration is the latest generation observed by the controller. | [optional] 
**phase** | **str** | Phase represents the current phase of cluster actuation. E.g. Pending, Running, Terminating, Failed etc. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


