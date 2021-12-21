# IoXK8sClusterAddonsV1alpha3ClusterResourceSetSpec

ClusterResourceSetSpec defines the desired state of ClusterResourceSet.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_selector** | [**IoXK8sClusterAddonsV1alpha3ClusterResourceSetSpecClusterSelector**](IoXK8sClusterAddonsV1alpha3ClusterResourceSetSpecClusterSelector.md) |  | 
**resources** | [**list[IoXK8sClusterAddonsV1alpha3ClusterResourceSetSpecResources]**](IoXK8sClusterAddonsV1alpha3ClusterResourceSetSpecResources.md) | Resources is a list of Secrets/ConfigMaps where each contains 1 or more resources to be applied to remote clusters. | [optional] 
**strategy** | **str** | Strategy is the strategy to be used during applying resources. Defaults to ApplyOnce. This field is immutable. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


