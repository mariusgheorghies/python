# IoXK8sClusterInfrastructureV1alpha3AWSMachineStatus

AWSMachineStatus defines the observed state of AWSMachine
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addresses** | [**list[IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneStatusBastionAddresses]**](IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneStatusBastionAddresses.md) | Addresses contains the AWS instance associated addresses. | [optional] 
**conditions** | [**list[IoXK8sClusterAddonsV1alpha3ClusterResourceSetStatusConditions]**](IoXK8sClusterAddonsV1alpha3ClusterResourceSetStatusConditions.md) | Conditions defines current service state of the AWSMachine. | [optional] 
**failure_message** | **str** | FailureMessage will be set in the event that there is a terminal problem reconciling the Machine and will contain a more verbose string suitable for logging and human consumption.   This field should not be set for transitive errors that a controller faces that are expected to be fixed automatically over time (like service outages), but instead indicate that something is fundamentally wrong with the Machine&#39;s spec or the configuration of the controller, and that manual intervention is required. Examples of terminal errors would be invalid combinations of settings in the spec, values that are unsupported by the controller, or the responsible controller itself being critically misconfigured.   Any transient errors that occur during the reconciliation of Machines can be added as events to the Machine object and/or logged in the controller&#39;s output. | [optional] 
**failure_reason** | **str** | FailureReason will be set in the event that there is a terminal problem reconciling the Machine and will contain a succinct value suitable for machine interpretation.   This field should not be set for transitive errors that a controller faces that are expected to be fixed automatically over time (like service outages), but instead indicate that something is fundamentally wrong with the Machine&#39;s spec or the configuration of the controller, and that manual intervention is required. Examples of terminal errors would be invalid combinations of settings in the spec, values that are unsupported by the controller, or the responsible controller itself being critically misconfigured.   Any transient errors that occur during the reconciliation of Machines can be added as events to the Machine object and/or logged in the controller&#39;s output. | [optional] 
**instance_state** | **str** | InstanceState is the state of the AWS instance for this machine. | [optional] 
**interruptible** | **bool** | Interruptible reports that this machine is using spot instances and can therefore be interrupted by CAPI when it receives a notice that the spot instance is to be terminated by AWS. This will be set to true when SpotMarketOptions is not nil (i.e. this machine is using a spot instance). | [optional] 
**ready** | **bool** | Ready is true when the provider resource is ready. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


