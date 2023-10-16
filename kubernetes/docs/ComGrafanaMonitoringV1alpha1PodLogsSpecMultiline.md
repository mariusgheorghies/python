# ComGrafanaMonitoringV1alpha1PodLogsSpecMultiline

Multiline stage merges multiple lines into a multiline block before passing it on to the next stage in the pipeline.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_line** | **str** | RE2 regular expression. Creates a new multiline block when matched. Required. | 
**max_lines** | **int** | Maximum number of lines a block can have. A new block is started if the number of lines surpasses this value. Defaults to 128. | [optional] 
**max_wait_time** | **str** | Maximum time to wait before passing on the multiline block to the next stage if no new lines are received. Defaults to 3s. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


