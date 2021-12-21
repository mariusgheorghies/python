# IoXK8sClusterInfrastructureV1beta1AWSFargateProfileStatus

FargateProfileStatus defines the observed state of FargateProfile.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | [**list[IoXK8sClusterAddonsV1beta1ClusterResourceSetStatusConditions]**](IoXK8sClusterAddonsV1beta1ClusterResourceSetStatusConditions.md) | Conditions defines current state of the Fargate profile. | [optional] 
**failure_message** | **str** | FailureMessage will be set in the event that there is a terminal problem reconciling the FargateProfile and will contain a more verbose string suitable for logging and human consumption.   This field should not be set for transitive errors that a controller faces that are expected to be fixed automatically over time (like service outages), but instead indicate that something is fundamentally wrong with the FargateProfile&#39;s spec or the configuration of the controller, and that manual intervention is required. Examples of terminal errors would be invalid combinations of settings in the spec, values that are unsupported by the controller, or the responsible controller itself being critically misconfigured.   Any transient errors that occur during the reconciliation of FargateProfiles can be added as events to the FargateProfile object and/or logged in the controller&#39;s output. | [optional] 
**failure_reason** | **str** | FailureReason will be set in the event that there is a terminal problem reconciling the FargateProfile and will contain a succinct value suitable for machine interpretation.   This field should not be set for transitive errors that a controller faces that are expected to be fixed automatically over time (like service outages), but instead indicate that something is fundamentally wrong with the FargateProfile&#39;s spec or the configuration of the controller, and that manual intervention is required. Examples of terminal errors would be invalid combinations of settings in the spec, values that are unsupported by the controller, or the responsible controller itself being critically misconfigured.   Any transient errors that occur during the reconciliation of FargateProfiles can be added as events to the FargateProfile object and/or logged in the controller&#39;s output. | [optional] 
**ready** | **bool** | Ready denotes that the FargateProfile is available. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


