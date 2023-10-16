# ComGrafanaMonitoringV1alpha1PodLogsSpecDrop

Drop is a filtering stage that lets you drop certain logs.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**drop_counter_reason** | **str** | Every time a log line is dropped, the metric logentry_dropped_lines_total is incremented. A \&quot;reason\&quot; label is added, and can be customized by providing a custom value here. Defaults to \&quot;drop_stage\&quot;. | [optional] 
**expression** | **str** | RE2 regular expression.   If source is provided, the regex attempts to match the source.   If no source is provided, then the regex attempts to attach the log line.   If the provided regex matches the log line or a provided source, the line is dropped. | [optional] 
**longer_than** | **str** | LongerThan will drop a log line if it its content is longer than this value (in bytes). Can be expressed as an integer (8192) or a number with a suffix (8kb). | [optional] 
**older_than** | **str** | OlderThan will be parsed as a Go duration. If the log line&#39;s timestamp is older than the current time minus the provided duration, it will be dropped. | [optional] 
**source** | **str** | Name from the extract data to parse. If empty, uses the log message. | [optional] 
**value** | **str** | Value can only be specified when source is specified. If the value provided is an exact match for the given source then the line will be dropped.   Mutually exclusive with expression. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


