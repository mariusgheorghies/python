# V1VolumeSnapshotContentStatusError

error is the last observed error during snapshot creation, if any. Upon success after retry, this error field will be cleared.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | message is a string detailing the encountered error during snapshot creation if specified. NOTE: message may be logged, and it should not contain sensitive information. | [optional] 
**time** | **datetime** | time is the timestamp when the error was encountered. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


