# IoArgoprojV1alpha1AppProjectSpecSyncWindows

SyncWindow contains the kind, time, duration and attributes that are used to assign the syncWindows to apps
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applications** | **list[str]** | Applications contains a list of applications that the window will apply to | [optional] 
**clusters** | **list[str]** | Clusters contains a list of clusters that the window will apply to | [optional] 
**duration** | **str** | Duration is the amount of time the sync window will be open | [optional] 
**kind** | **str** | Kind defines if the window allows or blocks syncs | [optional] 
**manual_sync** | **bool** | ManualSync enables manual syncs when they would otherwise be blocked | [optional] 
**namespaces** | **list[str]** | Namespaces contains a list of namespaces that the window will apply to | [optional] 
**schedule** | **str** | Schedule is the time the window will begin, specified in cron format | [optional] 
**time_zone** | **str** | TimeZone of the sync that will be applied to the schedule | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


