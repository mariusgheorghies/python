# IoArgoprojV1alpha1ApplicationStatusOperationState

OperationState contains information about any ongoing operations, such as a sync
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**finished_at** | **datetime** | FinishedAt contains time of operation completion | [optional] 
**message** | **str** | Message holds any pertinent messages when attempting to perform operation (typically errors). | [optional] 
**operation** | [**IoArgoprojV1alpha1ApplicationStatusOperationStateOperation**](IoArgoprojV1alpha1ApplicationStatusOperationStateOperation.md) |  | 
**phase** | **str** | Phase is the current phase of the operation | 
**retry_count** | **int** | RetryCount contains time of operation retries | [optional] 
**started_at** | **datetime** | StartedAt contains time of operation start | 
**sync_result** | [**IoArgoprojV1alpha1ApplicationStatusOperationStateSyncResult**](IoArgoprojV1alpha1ApplicationStatusOperationStateSyncResult.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


