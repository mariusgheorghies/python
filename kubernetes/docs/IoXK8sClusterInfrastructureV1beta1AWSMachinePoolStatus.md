# IoXK8sClusterInfrastructureV1beta1AWSMachinePoolStatus

AWSMachinePoolStatus defines the observed state of AWSMachinePool.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asg_status** | **str** | ASGStatus is a status string returned by the autoscaling API. | [optional] 
**conditions** | [**list[IoXK8sClusterAddonsV1beta1ClusterResourceSetStatusConditions]**](IoXK8sClusterAddonsV1beta1ClusterResourceSetStatusConditions.md) | Conditions defines current service state of the AWSMachinePool. | [optional] 
**failure_message** | **str** | FailureMessage will be set in the event that there is a terminal problem reconciling the Machine and will contain a more verbose string suitable for logging and human consumption.   This field should not be set for transitive errors that a controller faces that are expected to be fixed automatically over time (like service outages), but instead indicate that something is fundamentally wrong with the Machine&#39;s spec or the configuration of the controller, and that manual intervention is required. Examples of terminal errors would be invalid combinations of settings in the spec, values that are unsupported by the controller, or the responsible controller itself being critically misconfigured.   Any transient errors that occur during the reconciliation of Machines can be added as events to the Machine object and/or logged in the controller&#39;s output. | [optional] 
**failure_reason** | **str** | FailureReason will be set in the event that there is a terminal problem reconciling the Machine and will contain a succinct value suitable for machine interpretation.   This field should not be set for transitive errors that a controller faces that are expected to be fixed automatically over time (like service outages), but instead indicate that something is fundamentally wrong with the Machine&#39;s spec or the configuration of the controller, and that manual intervention is required. Examples of terminal errors would be invalid combinations of settings in the spec, values that are unsupported by the controller, or the responsible controller itself being critically misconfigured.   Any transient errors that occur during the reconciliation of Machines can be added as events to the Machine object and/or logged in the controller&#39;s output. | [optional] 
**instances** | [**list[IoXK8sClusterInfrastructureV1alpha3AWSMachinePoolStatusInstances]**](IoXK8sClusterInfrastructureV1alpha3AWSMachinePoolStatusInstances.md) | Instances contains the status for each instance in the pool | [optional] 
**launch_template_id** | **str** | The ID of the launch template | [optional] 
**ready** | **bool** | Ready is true when the provider resource is ready. | [optional] 
**replicas** | **int** | Replicas is the most recently observed number of replicas | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


