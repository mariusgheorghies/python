# OrgProjectcalicoCrdV1KubeControllersConfigurationSpecControllersNode

Node enables and configures the node controller. Enabled by default, set to nil to disable.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_endpoint** | [**OrgProjectcalicoCrdV1KubeControllersConfigurationSpecControllersNodeHostEndpoint**](OrgProjectcalicoCrdV1KubeControllersConfigurationSpecControllersNodeHostEndpoint.md) |  | [optional] 
**reconciler_period** | **str** | ReconcilerPeriod is the period to perform reconciliation with the Calico datastore. [Default: 5m] | [optional] 
**sync_labels** | **str** | SyncLabels controls whether to copy Kubernetes node labels to Calico nodes. [Default: Enabled] | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


