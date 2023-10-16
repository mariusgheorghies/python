# ComGrafanaMonitoringV1alpha1GrafanaAgentSpecLogsTlsConfig

TLSConfig to use for the kubernetes.client. Only used when the protocol of the URL is https.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ca** | [**ComCoreosMonitoringV1PodMonitorSpecTlsConfigCa**](ComCoreosMonitoringV1PodMonitorSpecTlsConfigCa.md) |  | [optional] 
**ca_file** | **str** | Path to the CA cert in the Prometheus container to use for the targets. | [optional] 
**cert** | [**ComCoreosMonitoringV1PodMonitorSpecTlsConfigCert**](ComCoreosMonitoringV1PodMonitorSpecTlsConfigCert.md) |  | [optional] 
**cert_file** | **str** | Path to the kubernetes.client cert file in the Prometheus container for the targets. | [optional] 
**insecure_skip_verify** | **bool** | Disable target certificate validation. | [optional] 
**key_file** | **str** | Path to the kubernetes.client key file in the Prometheus container for the targets. | [optional] 
**key_secret** | [**ComCoreosMonitoringV1PodMonitorSpecTlsConfigKeySecret**](ComCoreosMonitoringV1PodMonitorSpecTlsConfigKeySecret.md) |  | [optional] 
**server_name** | **str** | Used to verify the hostname for the targets. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

