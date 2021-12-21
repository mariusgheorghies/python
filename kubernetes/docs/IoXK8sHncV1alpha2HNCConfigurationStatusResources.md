# IoXK8sHncV1alpha2HNCConfigurationStatusResources

ResourceStatus defines the actual synchronization state of a specific resource.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group** | **str** | The API group of the resource being synchronized. | 
**mode** | **str** | Mode describes the synchronization mode of the kind. Typically, it will be the same as the mode in the spec, except when the reconciler has fallen behind or for resources with an enforced default synchronization mode, such as RBAC objects. | [optional] 
**num_propagated_objects** | **int** | Tracks the number of objects that are being propagated to descendant namespaces. The propagated objects are created by HNC. | [optional] 
**num_source_objects** | **int** | Tracks the number of objects that are created by users. | [optional] 
**resource** | **str** | The resource being synchronized. | 
**version** | **str** | The API version used by HNC when propagating this resource. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


