# IoArgoprojV1alpha1ApplicationStatusOperationStateSyncResult

SyncResult is the result of a Sync operation
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resources** | [**list[IoArgoprojV1alpha1ApplicationStatusOperationStateSyncResultResources]**](IoArgoprojV1alpha1ApplicationStatusOperationStateSyncResultResources.md) | Resources contains a list of sync result items for each individual resource in a sync operation | [optional] 
**revision** | **str** | Revision holds the revision this sync operation was performed to | 
**revisions** | **list[str]** | Revisions holds the revision this sync operation was performed for respective indexed source in sources field | [optional] 
**source** | [**IoArgoprojV1alpha1ApplicationStatusOperationStateSyncResultSource**](IoArgoprojV1alpha1ApplicationStatusOperationStateSyncResultSource.md) |  | [optional] 
**sources** | [**list[IoArgoprojV1alpha1ApplicationOperationSyncSources]**](IoArgoprojV1alpha1ApplicationOperationSyncSources.md) | Source records the application source information of the sync, used for comparing auto-sync | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


