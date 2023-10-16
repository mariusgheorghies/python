# ComCoreosMonitoringV1PrometheusSpecQuery

QuerySpec defines the query command line flags when starting Prometheus.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lookback_delta** | **str** | The delta difference allowed for retrieving metrics during expression evaluations. | [optional] 
**max_concurrency** | **int** | Number of concurrent queries that can be run at once. | [optional] 
**max_samples** | **int** | Maximum number of samples a single query can load into memory. Note that queries will fail if they would load more samples than this into memory, so this also limits the number of samples a query can return. | [optional] 
**timeout** | **str** | Maximum time a query may take before being aborted. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


