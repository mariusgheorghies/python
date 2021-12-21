# ComCoreosMonitoringV1PodMonitorSpecPodMetricsEndpoints

PodMetricsEndpoint defines a scrapeable endpoint of a Kubernetes Pod serving Prometheus metrics.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorization** | [**ComCoreosMonitoringV1PodMonitorSpecAuthorization**](ComCoreosMonitoringV1PodMonitorSpecAuthorization.md) |  | [optional] 
**basic_auth** | [**ComCoreosMonitoringV1PodMonitorSpecBasicAuth**](ComCoreosMonitoringV1PodMonitorSpecBasicAuth.md) |  | [optional] 
**bearer_token_secret** | [**ComCoreosMonitoringV1PodMonitorSpecBearerTokenSecret**](ComCoreosMonitoringV1PodMonitorSpecBearerTokenSecret.md) |  | [optional] 
**honor_labels** | **bool** | HonorLabels chooses the metric&#39;s labels on collisions with target labels. | [optional] 
**honor_timestamps** | **bool** | HonorTimestamps controls whether Prometheus respects the timestamps present in scraped data. | [optional] 
**interval** | **str** | Interval at which metrics should be scraped | [optional] 
**metric_relabelings** | [**list[ComCoreosMonitoringV1PodMonitorSpecMetricRelabelings]**](ComCoreosMonitoringV1PodMonitorSpecMetricRelabelings.md) | MetricRelabelConfigs to apply to samples before ingestion. | [optional] 
**oauth2** | [**ComCoreosMonitoringV1PodMonitorSpecOauth2**](ComCoreosMonitoringV1PodMonitorSpecOauth2.md) |  | [optional] 
**params** | **dict(str, list[str])** | Optional HTTP URL parameters | [optional] 
**path** | **str** | HTTP path to scrape for metrics. | [optional] 
**port** | **str** | Name of the pod port this endpoint refers to. Mutually exclusive with targetPort. | [optional] 
**proxy_url** | **str** | ProxyURL eg http://proxyserver:2195 Directs scrapes to proxy through this endpoint. | [optional] 
**relabelings** | [**list[ComCoreosMonitoringV1PodMonitorSpecMetricRelabelings]**](ComCoreosMonitoringV1PodMonitorSpecMetricRelabelings.md) | RelabelConfigs to apply to samples before scraping. Prometheus Operator automatically adds relabelings for a few standard Kubernetes fields and replaces original scrape job name with __tmp_prometheus_job_name. More info: https://prometheus.io/docs/prometheus/latest/configuration/configuration/#relabel_config | [optional] 
**scheme** | **str** | HTTP scheme to use for scraping. | [optional] 
**scrape_timeout** | **str** | Timeout after which the scrape is ended | [optional] 
**target_port** | [**object**](.md) | Deprecated: Use &#39;port&#39; instead. | [optional] 
**tls_config** | [**ComCoreosMonitoringV1PodMonitorSpecTlsConfig**](ComCoreosMonitoringV1PodMonitorSpecTlsConfig.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


