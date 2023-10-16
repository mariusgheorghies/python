# ComGrafanaMonitoringV1alpha1GrafanaAgentSpecMetricsQueueConfig

QueueConfig allows tuning of the remote_write queue parameters.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batch_send_deadline** | **str** | BatchSendDeadline is the maximum time a sample will wait in the buffer. | [optional] 
**capacity** | **int** | Capacity is the number of samples to buffer per shard before samples start being dropped. | [optional] 
**max_backoff** | **str** | MaxBackoff is the maximum retry delay. | [optional] 
**max_retries** | **int** | MaxRetries is the maximum number of times to retry a batch on recoverable errors. | [optional] 
**max_samples_per_send** | **int** | MaxSamplesPerSend is the maximum number of samples per send. | [optional] 
**max_shards** | **int** | MaxShards is the maximum number of shards, i.e., the amount of concurrency. | [optional] 
**min_backoff** | **str** | MinBackoff is the initial retry delay. MinBackoff is doubled for every retry. | [optional] 
**min_shards** | **int** | MinShards is the minimum number of shards, i.e., the amount of concurrency. | [optional] 
**retry_on_rate_limit** | **bool** | RetryOnRateLimit retries requests when encountering rate limits. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


