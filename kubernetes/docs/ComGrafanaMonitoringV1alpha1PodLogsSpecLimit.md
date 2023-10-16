# ComGrafanaMonitoringV1alpha1PodLogsSpecLimit

Limit is a rate-limiting stage that throttles logs based on several options.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**burst** | **int** | The cap in the quantity of burst lines that Promtail will push to Loki. | [optional] 
**drop** | **bool** | When drop is true, log lines that exceed the current rate limit are discarded. When drop is false, log lines that exceed the current rate limit wait to enter the back pressure mode.   Defaults to false. | [optional] 
**rate** | **int** | The rate limit in lines per second that Promtail will push to Loki. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


