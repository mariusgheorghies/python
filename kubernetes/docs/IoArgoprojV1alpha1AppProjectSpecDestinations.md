# IoArgoprojV1alpha1AppProjectSpecDestinations

ApplicationDestination holds information about the application's destination
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name is an alternate way of specifying the target cluster by its symbolic name | [optional] 
**namespace** | **str** | Namespace specifies the target namespace for the application&#39;s resources. The namespace will only be set for namespace-scoped resources that have not set a value for .metadata.namespace | [optional] 
**server** | **str** | Server specifies the URL of the target cluster and must be set to the Kubernetes control plane API | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


