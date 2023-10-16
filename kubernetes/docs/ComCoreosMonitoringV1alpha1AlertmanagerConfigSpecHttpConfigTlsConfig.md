# ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecHttpConfigTlsConfig

TLS configuration for the kubernetes.client.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ca** | [**ComCoreosMonitoringV1PrometheusSpecAlertingTlsConfigCa**](ComCoreosMonitoringV1PrometheusSpecAlertingTlsConfigCa.md) |  | [optional] 
**cert** | [**ComCoreosMonitoringV1PrometheusSpecAlertingTlsConfigCert**](ComCoreosMonitoringV1PrometheusSpecAlertingTlsConfigCert.md) |  | [optional] 
**insecure_skip_verify** | **bool** | Disable target certificate validation. | [optional] 
**key_secret** | [**ComCoreosMonitoringV1PodMonitorSpecTlsConfigKeySecret**](ComCoreosMonitoringV1PodMonitorSpecTlsConfigKeySecret.md) |  | [optional] 
**server_name** | **str** | Used to verify the hostname for the targets. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


