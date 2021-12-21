# ComCoreosMonitoringV1AlertmanagerSpecLifecyclePostStart

PostStart is called immediately after a container is created. If the handler fails, the container is terminated and restarted according to its restart policy. Other management of the container blocks until the hook completes. More info: https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/#container-hooks
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_exec** | [**ComCoreosMonitoringV1AlertmanagerSpecLifecyclePostStartExec**](ComCoreosMonitoringV1AlertmanagerSpecLifecyclePostStartExec.md) |  | [optional] 
**http_get** | [**ComCoreosMonitoringV1AlertmanagerSpecLifecyclePostStartHttpGet**](ComCoreosMonitoringV1AlertmanagerSpecLifecyclePostStartHttpGet.md) |  | [optional] 
**tcp_socket** | [**ComCoreosMonitoringV1AlertmanagerSpecLifecyclePostStartTcpSocket**](ComCoreosMonitoringV1AlertmanagerSpecLifecyclePostStartTcpSocket.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


