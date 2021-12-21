# IoXK8sClusterAddonsV1alpha3ClusterResourceSetBindingSpecResources

ResourceBinding shows the status of a resource that belongs to a ClusterResourceSet matched by the owner cluster of the ClusterResourceSetBinding object.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applied** | **bool** | Applied is to track if a resource is applied to the cluster or not. | 
**hash** | **str** | Hash is the hash of a resource&#39;s data. This can be used to decide if a resource is changed. For \&quot;ApplyOnce\&quot; ClusterResourceSet.spec.strategy, this is no-op as that strategy does not act on change. | [optional] 
**kind** | **str** | Kind of the resource. Supported kinds are: Secrets and ConfigMaps. | 
**last_applied_time** | **datetime** | LastAppliedTime identifies when this resource was last applied to the cluster. | [optional] 
**name** | **str** | Name of the resource that is in the same namespace with ClusterResourceSet object. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


