# ComCoreosMonitoringV1ProbeSpec

Specification of desired Ingress selection for target discovery by Prometheus.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interval** | **str** | Interval at which targets are probed using the configured prober. If not specified Prometheus&#39; global scrape interval is used. | [optional] 
**job_name** | **str** | The job name assigned to scraped metrics by default. | [optional] 
**module** | **str** | The module to use for probing specifying how to probe the target. Example module configuring in the blackbox exporter: https://github.com/prometheus/blackbox_exporter/blob/master/example.yml | [optional] 
**prober** | [**ComCoreosMonitoringV1ProbeSpecProber**](ComCoreosMonitoringV1ProbeSpecProber.md) |  | [optional] 
**scrape_timeout** | **str** | Timeout for scraping metrics from the Prometheus exporter. | [optional] 
**targets** | [**ComCoreosMonitoringV1ProbeSpecTargets**](ComCoreosMonitoringV1ProbeSpecTargets.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


