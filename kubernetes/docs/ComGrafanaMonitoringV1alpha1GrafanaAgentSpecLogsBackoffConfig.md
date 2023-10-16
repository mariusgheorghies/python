# ComGrafanaMonitoringV1alpha1GrafanaAgentSpecLogsBackoffConfig

Configures how to retry requests to Loki when a request fails. Defaults to a minPeriod of 500ms, maxPeriod of 5m, and maxRetries of 10.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_period** | **str** | Maximum backoff time between retries. | [optional] 
**max_retries** | **int** | Maximum number of retries to perform before giving up a request. | [optional] 
**min_period** | **str** | Initial backoff time between retries. Time between retries is increased exponentially. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


