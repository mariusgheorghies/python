# IoXK8sClusterBootstrapV1alpha3EKSConfigStatus

EKSConfigStatus defines the observed state of EKSConfig
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | [**list[IoXK8sClusterAddonsV1alpha3ClusterResourceSetStatusConditions]**](IoXK8sClusterAddonsV1alpha3ClusterResourceSetStatusConditions.md) | Conditions defines current service state of the EKSConfig. | [optional] 
**data_secret_name** | **str** | DataSecretName is the name of the secret that stores the bootstrap data script. | [optional] 
**failure_message** | **str** | FailureMessage will be set on non-retryable errors | [optional] 
**failure_reason** | **str** | FailureReason will be set on non-retryable errors | [optional] 
**observed_generation** | **int** | ObservedGeneration is the latest generation observed by the controller. | [optional] 
**ready** | **bool** | Ready indicates the BootstrapData secret is ready to be consumed | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


