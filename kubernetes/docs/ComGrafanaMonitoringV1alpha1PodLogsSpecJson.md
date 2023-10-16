# ComGrafanaMonitoringV1alpha1PodLogsSpecJson

JSON is a parsing stage that reads the log line as JSON and accepts JMESPath expressions to extract data.   Information on JMESPath: http://jmespath.org/
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expressions** | **dict(str, str)** | Set of the key/value pairs of JMESPath expressions. The key will be the key in the extracted data while the expression will be the value, evaluated as a JMESPath from the source data.   Literal JMESPath expressions can be used by wrapping a key in double quotes, which then must be wrapped again in single quotes in YAML so they get passed to the JMESPath parser. | [optional] 
**source** | **str** | Name from the extracted data to parse as JSON. If empty, uses entire log message. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


