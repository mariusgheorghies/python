# ComGrafanaMonitoringV1alpha1PodLogsSpecMatch

Match is a filtering stage that conditionally applies a set of stages or drop entries when a log entry matches a configurable LogQL stream selector and filter expressions.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Determines what action is taken when the selector matches the log line. Can be keep or drop. Defaults to keep. When set to drop, entries are dropped and no later metrics are recorded. Stages must be empty when dropping metrics. | [optional] 
**drop_counter_reason** | **str** | Every time a log line is dropped, the metric logentry_dropped_lines_total is incremented. A \&quot;reason\&quot; label is added, and can be customized by providing a custom value here. Defaults to \&quot;match_stage.\&quot; | [optional] 
**pipeline_name** | **str** | Names the pipeline. When defined, creates an additional label in the pipeline_duration_seconds histogram, where the value is concatenated with job_name using an underscore. | [optional] 
**selector** | **str** | LogQL stream selector and filter expressions. Required. | 
**stages** | **str** | Nested set of pipeline stages to execute when action is keep and the log line matches selector.   An example value for stages may be:   stages: | - json: {} - labelAllow: [foo, bar]   Note that stages is a string because SIG API Machinery does not support recursive types, and so it cannot be validated for correctness. Be careful not to mistype anything. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


