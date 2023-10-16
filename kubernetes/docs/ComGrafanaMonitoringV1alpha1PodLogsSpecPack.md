# ComGrafanaMonitoringV1alpha1PodLogsSpecPack

Pack is a transform stage that lets you embed extracted values and labels into the log line by packing the log line and labels inside of a JSON object.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ingest_timestamp** | **bool** | If the resulting log line should use any existing timestamp or use time.Now() when the line was created. Set to true when combining several log streams from different containers to avoid out of order errors. | [optional] 
**labels** | **list[str]** | Name from extracted data or line labels. Required. Labels provided here are automatically removed from output labels. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


