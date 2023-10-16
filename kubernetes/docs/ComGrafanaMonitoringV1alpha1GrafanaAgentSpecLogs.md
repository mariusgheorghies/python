# ComGrafanaMonitoringV1alpha1GrafanaAgentSpecLogs

Logs controls the logging subsystem of the Agent and settings unique to logging-specific pods that are deployed.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kubernetes.clients** | [**list[ComGrafanaMonitoringV1alpha1GrafanaAgentSpecLogsClients]**](ComGrafanaMonitoringV1alpha1GrafanaAgentSpecLogsClients.md) | A global set of kubernetes.clients to use when a discovered LogsInstance does not have any kubernetes.clients defined. | [optional] 
**enforced_namespace_label** | **str** | EnforcedNamespaceLabel enforces adding a namespace label of origin for each metric that is user-created. The label value will always be the namespace of the object that is being created. | [optional] 
**ignore_namespace_selectors** | **bool** | IgnoreNamespaceSelectors, if true, will ignore NamespaceSelector settings from the PodLogs configs, and they will only discover endpoints within their current namespace. | [optional] 
**instance_namespace_selector** | [**ComGrafanaMonitoringV1alpha1GrafanaAgentSpecLogsInstanceNamespaceSelector**](ComGrafanaMonitoringV1alpha1GrafanaAgentSpecLogsInstanceNamespaceSelector.md) |  | [optional] 
**instance_selector** | [**ComGrafanaMonitoringV1alpha1GrafanaAgentSpecLogsInstanceSelector**](ComGrafanaMonitoringV1alpha1GrafanaAgentSpecLogsInstanceSelector.md) |  | [optional] 
**logs_external_label_name** | **str** | LogsExternalLabelName is the name of the external label used to denote Grafana Agent cluster. Defaults to \&quot;cluster.\&quot; External label will _not_ be added when value is set to the empty string. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


