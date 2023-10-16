# ComGrafanaMonitoringV1alpha1PodLogsSpecTemplate

Template is a transform stage that manipulates the values in the extracted map using Go's template syntax.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** | Name from extracted data to parse. Required. If empty, defaults to using the log message. | 
**template** | **str** | Go template string to use. Required. In addition to normal template functions, ToLower, ToUpper, Replace, Trim, TrimLeft, TrimRight, TrimPrefix, and TrimSpace are also available. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


