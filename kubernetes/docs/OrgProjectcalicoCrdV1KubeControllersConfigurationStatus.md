# OrgProjectcalicoCrdV1KubeControllersConfigurationStatus

KubeControllersConfigurationStatus represents the status of the configuration. It's useful for admins to be able to see the actual config that was applied, which can be modified by environment variables on the kube-controllers process.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment_vars** | **dict(str, str)** | EnvironmentVars contains the environment variables on the kube-controllers that influenced the RunningConfig. | [optional] 
**running_config** | [**OrgProjectcalicoCrdV1KubeControllersConfigurationStatusRunningConfig**](OrgProjectcalicoCrdV1KubeControllersConfigurationStatusRunningConfig.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


