# ComCoreosMonitoringV1PrometheusSpecThanos

Thanos configuration allows configuring various aspects of a Prometheus server in a Thanos environment.   This section is experimental, it may change significantly without deprecation notice in any release.   This is experimental and may change significantly without backward compatibility in any release.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_image** | **str** | Thanos base image if other than default. Deprecated: use &#39;image&#39; instead | [optional] 
**grpc_server_tls_config** | [**ComCoreosMonitoringV1PrometheusSpecThanosGrpcServerTlsConfig**](ComCoreosMonitoringV1PrometheusSpecThanosGrpcServerTlsConfig.md) |  | [optional] 
**image** | **str** | Image if specified has precedence over baseImage, tag and sha combinations. Specifying the version is still necessary to ensure the Prometheus Operator knows what version of Thanos is being configured. | [optional] 
**listen_local** | **bool** | ListenLocal makes the Thanos sidecar listen on loopback, so that it does not bind against the Pod IP. | [optional] 
**log_format** | **str** | LogFormat for Thanos sidecar to be configured with. | [optional] 
**log_level** | **str** | LogLevel for Thanos sidecar to be configured with. | [optional] 
**min_time** | **str** | MinTime for Thanos sidecar to be configured with. Option can be a constant time in RFC3339 format or time duration relative to current time, such as -1d or 2h45m. Valid duration units are ms, s, m, h, d, w, y. | [optional] 
**object_storage_config** | [**ComCoreosMonitoringV1PrometheusSpecThanosObjectStorageConfig**](ComCoreosMonitoringV1PrometheusSpecThanosObjectStorageConfig.md) |  | [optional] 
**object_storage_config_file** | **str** | ObjectStorageConfigFile specifies the path of the object storage configuration file. When used alongside with ObjectStorageConfig, ObjectStorageConfigFile takes precedence. | [optional] 
**ready_timeout** | **str** | ReadyTimeout is the maximum time Thanos sidecar will wait for Prometheus to start. Eg 10m | [optional] 
**resources** | [**ComCoreosMonitoringV1PrometheusSpecThanosResources**](ComCoreosMonitoringV1PrometheusSpecThanosResources.md) |  | [optional] 
**sha** | **str** | SHA of Thanos container image to be deployed. Defaults to the value of &#x60;version&#x60;. Similar to a tag, but the SHA explicitly deploys an immutable container image. Version and Tag are ignored if SHA is set. Deprecated: use &#39;image&#39; instead.  The image digest can be specified as part of the image URL. | [optional] 
**tag** | **str** | Tag of Thanos sidecar container image to be deployed. Defaults to the value of &#x60;version&#x60;. Version is ignored if Tag is set. Deprecated: use &#39;image&#39; instead.  The image tag can be specified as part of the image URL. | [optional] 
**tracing_config** | [**ComCoreosMonitoringV1PrometheusSpecThanosTracingConfig**](ComCoreosMonitoringV1PrometheusSpecThanosTracingConfig.md) |  | [optional] 
**tracing_config_file** | **str** | TracingConfig specifies the path of the tracing configuration file. When used alongside with TracingConfig, TracingConfigFile takes precedence. | [optional] 
**version** | **str** | Version describes the version of Thanos to use. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


