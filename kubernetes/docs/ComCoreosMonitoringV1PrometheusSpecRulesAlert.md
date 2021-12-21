# ComCoreosMonitoringV1PrometheusSpecRulesAlert

/--rules.alert.*/ command-line arguments
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**for_grace_period** | **str** | Minimum duration between alert and restored &#39;for&#39; state. This is maintained only for alerts with configured &#39;for&#39; time greater than grace period. | [optional] 
**for_outage_tolerance** | **str** | Max time to tolerate prometheus outage for restoring &#39;for&#39; state of alert. | [optional] 
**resend_delay** | **str** | Minimum amount of time to wait before resending an alert to Alertmanager. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


