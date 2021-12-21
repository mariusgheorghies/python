# IoXK8sHncV1alpha2HNCConfigurationSpecResources

ResourceSpec defines the desired synchronization state of a specific resource.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group** | **str** | Group of the resource defined below. This is used to unambiguously identify the resource. It may be omitted for core resources (e.g. \&quot;secrets\&quot;). | [optional] 
**mode** | **str** | Synchronization mode of the kind. If the field is empty, it will be treated as \&quot;Propagate\&quot;. | [optional] 
**resource** | **str** | Resource to be configured. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


