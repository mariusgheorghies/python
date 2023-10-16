# ComGrafanaMonitoringV1alpha1PodLogsSpecTimestamp

Timestamp is an action stage that can change the timestamp of a log line before it is sent to Loki. If not present, the timestamp of a log line defaults to the time when the log line was read.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_on_failure** | **str** | Action to take when the timestamp can&#39;t be extracted or parsed. Can be skip or fudge. Defaults to fudge. | [optional] 
**fallback_formats** | **list[str]** | Fallback formats to try if format fails. | [optional] 
**format** | **str** | Determines format of the time string. Required. Can be one of: ANSIC, UnixDate, RubyDate, RFC822, RFC822Z, RFC850, RFC1123, RFC1123Z, RFC3339, RFC3339Nano, Unix, UnixMs, UnixUs, UnixNs. | 
**location** | **str** | IANA Timezone Database string. | [optional] 
**source** | **str** | Name from extracted data to use as the timestamp. Required. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


