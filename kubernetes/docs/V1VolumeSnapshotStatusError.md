# V1VolumeSnapshotStatusError

error is the last observed error during snapshot creation, if any. This field could be helpful to upper level controllers(i.e., application controller) to decide whether they should continue on waiting for the snapshot to be created based on the type of error reported. The snapshot controller will keep retrying when an error occurs during the snapshot creation. Upon success, this error field will be cleared.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | message is a string detailing the encountered error during snapshot creation if specified. NOTE: message may be logged, and it should not contain sensitive information. | [optional] 
**time** | **datetime** | time is the timestamp when the error was encountered. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


