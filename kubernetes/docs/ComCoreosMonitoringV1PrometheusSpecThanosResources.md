# ComCoreosMonitoringV1PrometheusSpecThanosResources

Resources defines the resource requirements for the Thanos sidecar. If not provided, no requests/limits will be set
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limits** | **dict(str, object)** | Limits describes the maximum amount of compute resources allowed. More info: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/ | [optional] 
**requests** | **dict(str, object)** | Requests describes the minimum amount of compute resources required. If Requests is omitted for a container, it defaults to Limits if that is explicitly specified, otherwise to an implementation-defined value. More info: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/ | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


