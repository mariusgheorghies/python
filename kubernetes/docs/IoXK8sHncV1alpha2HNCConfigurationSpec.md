# IoXK8sHncV1alpha2HNCConfigurationSpec

HNCConfigurationSpec defines the desired state of HNC configuration.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resources** | [**list[IoXK8sHncV1alpha2HNCConfigurationSpecResources]**](IoXK8sHncV1alpha2HNCConfigurationSpecResources.md) | Resources defines the cluster-wide settings for resource synchronization. Note that &#39;roles&#39; and &#39;rolebindings&#39; are pre-configured by HNC with &#39;Propagate&#39; mode and are omitted in the spec. Any configuration of &#39;roles&#39; or &#39;rolebindings&#39; are not allowed. To learn more, see https://github.com/kubernetes-sigs/hierarchical-namespaces/blob/master/docs/user-guide/how-to.md#admin-types | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


