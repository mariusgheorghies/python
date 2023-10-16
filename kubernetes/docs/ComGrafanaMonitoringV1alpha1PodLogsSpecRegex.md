# ComGrafanaMonitoringV1alpha1PodLogsSpecRegex

Regex is a parsing stage that parses a log line using a regular expression.  Named capture groups in the regex allows for adding data into the extracted map.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expression** | **str** | RE2 regular expression. Each capture group MUST be named. Required. | 
**source** | **str** | Name from extracted data to parse. If empty, defaults to using the log message. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

