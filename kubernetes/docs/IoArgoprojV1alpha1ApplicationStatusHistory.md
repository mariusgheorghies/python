# IoArgoprojV1alpha1ApplicationStatusHistory

RevisionHistory contains history information about a previous sync
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deploy_started_at** | **datetime** | DeployStartedAt holds the time the sync operation started | [optional] 
**deployed_at** | **datetime** | DeployedAt holds the time the sync operation completed | 
**id** | **int** | ID is an auto incrementing identifier of the RevisionHistory | 
**revision** | **str** | Revision holds the revision the sync was performed against | [optional] 
**revisions** | **list[str]** | Revisions holds the revision of each source in sources field the sync was performed against | [optional] 
**source** | [**IoArgoprojV1alpha1ApplicationStatusSource**](IoArgoprojV1alpha1ApplicationStatusSource.md) |  | [optional] 
**sources** | [**list[IoArgoprojV1alpha1ApplicationOperationSyncSources]**](IoArgoprojV1alpha1ApplicationOperationSyncSources.md) | Sources is a reference to the application sources used for the sync operation | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


