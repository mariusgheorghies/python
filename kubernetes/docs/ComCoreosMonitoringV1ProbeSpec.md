# ComCoreosMonitoringV1ProbeSpec

Specification of desired Ingress selection for target discovery by Prometheus.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorization** | [**ComCoreosMonitoringV1PodMonitorSpecAuthorization**](ComCoreosMonitoringV1PodMonitorSpecAuthorization.md) |  | [optional] 
**basic_auth** | [**ComCoreosMonitoringV1PodMonitorSpecBasicAuth**](ComCoreosMonitoringV1PodMonitorSpecBasicAuth.md) |  | [optional] 
**bearer_token_secret** | [**ComCoreosMonitoringV1ProbeSpecBearerTokenSecret**](ComCoreosMonitoringV1ProbeSpecBearerTokenSecret.md) |  | [optional] 
**interval** | **str** | Interval at which targets are probed using the configured prober. If not specified Prometheus&#39; global scrape interval is used. | [optional] 
**job_name** | **str** | The job name assigned to scraped metrics by default. | [optional] 
**label_limit** | **int** | Per-scrape limit on number of labels that will be accepted for a sample. Only valid in Prometheus versions 2.27.0 and newer. | [optional] 
**label_name_length_limit** | **int** | Per-scrape limit on length of labels name that will be accepted for a sample. Only valid in Prometheus versions 2.27.0 and newer. | [optional] 
**label_value_length_limit** | **int** | Per-scrape limit on length of labels value that will be accepted for a sample. Only valid in Prometheus versions 2.27.0 and newer. | [optional] 
**metric_relabelings** | [**list[ComCoreosMonitoringV1PodMonitorSpecMetricRelabelings]**](ComCoreosMonitoringV1PodMonitorSpecMetricRelabelings.md) | MetricRelabelConfigs to apply to samples before ingestion. | [optional] 
**module** | **str** | The module to use for probing specifying how to probe the target. Example module configuring in the blackbox exporter: https://github.com/prometheus/blackbox_exporter/blob/master/example.yml | [optional] 
**oauth2** | [**ComCoreosMonitoringV1PodMonitorSpecOauth2**](ComCoreosMonitoringV1PodMonitorSpecOauth2.md) |  | [optional] 
**prober** | [**ComCoreosMonitoringV1ProbeSpecProber**](ComCoreosMonitoringV1ProbeSpecProber.md) |  | [optional] 
**sample_limit** | **int** | SampleLimit defines per-scrape limit on number of scraped samples that will be accepted. | [optional] 
**scrape_timeout** | **str** | Timeout for scraping metrics from the Prometheus exporter. If not specified, the Prometheus global scrape interval is used. | [optional] 
**target_limit** | **int** | TargetLimit defines a limit on the number of scraped targets that will be accepted. | [optional] 
**targets** | [**ComCoreosMonitoringV1ProbeSpecTargets**](ComCoreosMonitoringV1ProbeSpecTargets.md) |  | [optional] 
**tls_config** | [**ComCoreosMonitoringV1PodMonitorSpecTlsConfig**](ComCoreosMonitoringV1PodMonitorSpecTlsConfig.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


