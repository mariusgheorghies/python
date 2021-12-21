# IoXK8sClusterClusterctlV1alpha3Provider

Provider defines an entry in the provider inventory.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the kubernetes.client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**V1ObjectMetaV2**](V1ObjectMetaV2.md) |  | [optional] 
**provider_name** | **str** | ProviderName indicates the name of the provider. | [optional] 
**type** | **str** | Type indicates the type of the provider. See ProviderType for a list of supported values | [optional] 
**version** | **str** | Version indicates the component version. | [optional] 
**watched_namespace** | **str** | WatchedNamespace indicates the namespace where the provider controller is is watching. if empty the provider controller is watching for objects in all namespaces. Deprecated: in clusterctl v1alpha4 all the providers watch all the namespaces; this field will be removed in a future version of this API | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


