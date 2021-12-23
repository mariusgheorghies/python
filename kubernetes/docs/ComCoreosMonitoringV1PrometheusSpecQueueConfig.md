# ComCoreosMonitoringV1PrometheusSpecQueueConfig

QueueConfig allows tuning of the remote write queue parameters.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batch_send_deadline** | **str** | BatchSendDeadline is the maximum time a sample will wait in buffer. | [optional] 
**capacity** | **int** | Capacity is the number of samples to buffer per shard before we start dropping them. | [optional] 
**max_backoff** | **str** | MaxBackoff is the maximum retry delay. | [optional] 
**max_retries** | **int** | MaxRetries is the maximum number of times to retry a batch on recoverable errors. | [optional] 
**max_samples_per_send** | **int** | MaxSamplesPerSend is the maximum number of samples per send. | [optional] 
**max_shards** | **int** | MaxShards is the maximum number of shards, i.e. amount of concurrency. | [optional] 
**min_backoff** | **str** | MinBackoff is the initial retry delay. Gets doubled for every retry. | [optional] 
**min_shards** | **int** | MinShards is the minimum number of shards, i.e. amount of concurrency. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


