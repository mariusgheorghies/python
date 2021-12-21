# ComCoreosMonitoringV1AlertmanagerSpecLifecyclePreStop

PreStop is called immediately before a container is terminated due to an API request or management event such as liveness/startup probe failure, preemption, resource contention, etc. The handler is not called if the container crashes or exits. The reason for termination is passed to the handler. The Pod's termination grace period countdown begins before the PreStop hooked is executed. Regardless of the outcome of the handler, the container will eventually terminate within the Pod's termination grace period. Other management of the container blocks until the hook completes or until the termination grace period is reached. More info: https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/#container-hooks
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_exec** | [**ComCoreosMonitoringV1AlertmanagerSpecLifecyclePostStartExec**](ComCoreosMonitoringV1AlertmanagerSpecLifecyclePostStartExec.md) |  | [optional] 
**http_get** | [**ComCoreosMonitoringV1AlertmanagerSpecLifecyclePostStartHttpGet**](ComCoreosMonitoringV1AlertmanagerSpecLifecyclePostStartHttpGet.md) |  | [optional] 
**tcp_socket** | [**ComCoreosMonitoringV1AlertmanagerSpecLifecyclePostStartTcpSocket**](ComCoreosMonitoringV1AlertmanagerSpecLifecyclePostStartTcpSocket.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


