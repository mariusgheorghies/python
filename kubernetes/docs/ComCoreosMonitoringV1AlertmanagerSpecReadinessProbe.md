# ComCoreosMonitoringV1AlertmanagerSpecReadinessProbe

Periodic probe of container service readiness. Container will be removed from service endpoints if the probe fails. Cannot be updated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_exec** | [**ComCoreosMonitoringV1AlertmanagerSpecLifecyclePostStartExec**](ComCoreosMonitoringV1AlertmanagerSpecLifecyclePostStartExec.md) |  | [optional] 
**failure_threshold** | **int** | Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3. Minimum value is 1. | [optional] 
**http_get** | [**ComCoreosMonitoringV1AlertmanagerSpecLifecyclePostStartHttpGet**](ComCoreosMonitoringV1AlertmanagerSpecLifecyclePostStartHttpGet.md) |  | [optional] 
**initial_delay_seconds** | **int** | Number of seconds after the container has started before liveness probes are initiated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes | [optional] 
**period_seconds** | **int** | How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1. | [optional] 
**success_threshold** | **int** | Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1. Must be 1 for liveness and startup. Minimum value is 1. | [optional] 
**tcp_socket** | [**ComCoreosMonitoringV1AlertmanagerSpecLifecyclePostStartTcpSocket**](ComCoreosMonitoringV1AlertmanagerSpecLifecyclePostStartTcpSocket.md) |  | [optional] 
**timeout_seconds** | **int** | Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


