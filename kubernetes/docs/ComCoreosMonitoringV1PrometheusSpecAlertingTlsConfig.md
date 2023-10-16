# ComCoreosMonitoringV1PrometheusSpecAlertingTlsConfig

TLS Config to use for alertmanager connection.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ca** | [**ComCoreosMonitoringV1PrometheusSpecAlertingTlsConfigCa**](ComCoreosMonitoringV1PrometheusSpecAlertingTlsConfigCa.md) |  | [optional] 
**ca_file** | **str** | Path to the CA cert in the Prometheus container to use for the targets. | [optional] 
**cert** | [**ComCoreosMonitoringV1PrometheusSpecAlertingTlsConfigCert**](ComCoreosMonitoringV1PrometheusSpecAlertingTlsConfigCert.md) |  | [optional] 
**cert_file** | **str** | Path to the kubernetes.client cert file in the Prometheus container for the targets. | [optional] 
**insecure_skip_verify** | **bool** | Disable target certificate validation. | [optional] 
**key_file** | **str** | Path to the kubernetes.client key file in the Prometheus container for the targets. | [optional] 
**key_secret** | [**ComCoreosMonitoringV1PodMonitorSpecTlsConfigKeySecret**](ComCoreosMonitoringV1PodMonitorSpecTlsConfigKeySecret.md) |  | [optional] 
**server_name** | **str** | Used to verify the hostname for the targets. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


