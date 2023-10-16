# ComCoreosMonitoringV1ServiceMonitorSpecEndpoints

Endpoint defines a scrapeable endpoint serving Prometheus metrics.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorization** | [**ComCoreosMonitoringV1PodMonitorSpecAuthorization**](ComCoreosMonitoringV1PodMonitorSpecAuthorization.md) |  | [optional] 
**basic_auth** | [**ComCoreosMonitoringV1ServiceMonitorSpecBasicAuth**](ComCoreosMonitoringV1ServiceMonitorSpecBasicAuth.md) |  | [optional] 
**bearer_token_file** | **str** | File to read bearer token for scraping targets. | [optional] 
**bearer_token_secret** | [**ComCoreosMonitoringV1ServiceMonitorSpecBearerTokenSecret**](ComCoreosMonitoringV1ServiceMonitorSpecBearerTokenSecret.md) |  | [optional] 
**enable_http2** | **bool** | Whether to enable HTTP2. | [optional] 
**filter_running** | **bool** | Drop pods that are not running. (Failed, Succeeded). Enabled by default. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-phase | [optional] 
**follow_redirects** | **bool** | FollowRedirects configures whether scrape requests follow HTTP 3xx redirects. | [optional] 
**honor_labels** | **bool** | HonorLabels chooses the metric&#39;s labels on collisions with target labels. | [optional] 
**honor_timestamps** | **bool** | HonorTimestamps controls whether Prometheus respects the timestamps present in scraped data. | [optional] 
**interval** | **str** | Interval at which metrics should be scraped If not specified Prometheus&#39; global scrape interval is used. | [optional] 
**metric_relabelings** | [**list[ComCoreosMonitoringV1PodMonitorSpecMetricRelabelings]**](ComCoreosMonitoringV1PodMonitorSpecMetricRelabelings.md) | MetricRelabelConfigs to apply to samples before ingestion. | [optional] 
**oauth2** | [**ComCoreosMonitoringV1PodMonitorSpecOauth2**](ComCoreosMonitoringV1PodMonitorSpecOauth2.md) |  | [optional] 
**params** | **dict(str, list[str])** | Optional HTTP URL parameters | [optional] 
**path** | **str** | HTTP path to scrape for metrics. If empty, Prometheus uses the default value (e.g. &#x60;/metrics&#x60;). | [optional] 
**port** | **str** | Name of the service port this endpoint refers to. Mutually exclusive with targetPort. | [optional] 
**proxy_url** | **str** | ProxyURL eg http://proxyserver:2195 Directs scrapes to proxy through this endpoint. | [optional] 
**relabelings** | [**list[ComCoreosMonitoringV1PodMonitorSpecMetricRelabelings]**](ComCoreosMonitoringV1PodMonitorSpecMetricRelabelings.md) | RelabelConfigs to apply to samples before scraping. Prometheus Operator automatically adds relabelings for a few standard Kubernetes fields. The original scrape job&#39;s name is available via the &#x60;__tmp_prometheus_job_name&#x60; label. More info: https://prometheus.io/docs/prometheus/latest/configuration/configuration/#relabel_config | [optional] 
**scheme** | **str** | HTTP scheme to use for scraping. | [optional] 
**scrape_timeout** | **str** | Timeout after which the scrape is ended If not specified, the Prometheus global scrape timeout is used unless it is less than &#x60;Interval&#x60; in which the latter is used. | [optional] 
**target_port** | [**object**](.md) | Name or number of the target port of the Pod behind the Service, the port must be specified with container port property. Mutually exclusive with port. | [optional] 
**tls_config** | [**ComCoreosMonitoringV1ServiceMonitorSpecTlsConfig**](ComCoreosMonitoringV1ServiceMonitorSpecTlsConfig.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

