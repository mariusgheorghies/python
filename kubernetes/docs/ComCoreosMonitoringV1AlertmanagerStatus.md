# ComCoreosMonitoringV1AlertmanagerStatus

Most recent observed status of the Alertmanager cluster. Read-only. Not included when requesting from the apiserver, only from the Prometheus Operator API itself. More info: https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#spec-and-status
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available_replicas** | **int** | Total number of available pods (ready for at least minReadySeconds) targeted by this Alertmanager cluster. | 
**paused** | **bool** | Represents whether any actions on the underlying managed objects are being performed. Only delete actions will be performed. | 
**replicas** | **int** | Total number of non-terminated pods targeted by this Alertmanager cluster (their labels match the selector). | 
**unavailable_replicas** | **int** | Total number of unavailable pods targeted by this Alertmanager cluster. | 
**updated_replicas** | **int** | Total number of non-terminated pods targeted by this Alertmanager cluster that have the desired version spec. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

