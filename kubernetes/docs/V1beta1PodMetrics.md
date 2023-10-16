# V1beta1PodMetrics

PodMetrics sets resource usage metrics of a pod.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**containers** | [**list[V1beta1ContainerMetrics]**](V1beta1ContainerMetrics.md) | Metrics for all containers are collected within the same time window. | 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the kubernetes.client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**V1ObjectMetaV2**](V1ObjectMetaV2.md) |  | [optional] 
**timestamp** | **datetime** | The following fields define time interval from which metrics were collected from the interval [Timestamp-Window, Timestamp]. | 
**window** | **str** | Duration is a wrapper around time.Duration which supports correct marshaling to YAML and JSON. In particular, it marshals into strings, which can be used as map keys in json. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


