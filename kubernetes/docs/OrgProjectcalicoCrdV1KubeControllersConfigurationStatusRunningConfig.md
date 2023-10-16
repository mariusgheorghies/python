# OrgProjectcalicoCrdV1KubeControllersConfigurationStatusRunningConfig

RunningConfig contains the effective config that is running in the kube-controllers pod, after merging the API resource with any environment variables.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**controllers** | [**OrgProjectcalicoCrdV1KubeControllersConfigurationSpecControllers**](OrgProjectcalicoCrdV1KubeControllersConfigurationSpecControllers.md) |  | 
**etcd_v3_compaction_period** | **str** | EtcdV3CompactionPeriod is the period between etcdv3 compaction requests. Set to 0 to disable. [Default: 10m] | [optional] 
**health_checks** | **str** | HealthChecks enables or disables support for health checks [Default: Enabled] | [optional] 
**log_severity_screen** | **str** | LogSeverityScreen is the log severity above which logs are sent to the stdout. [Default: Info] | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


