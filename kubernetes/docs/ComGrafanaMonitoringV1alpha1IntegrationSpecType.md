# ComGrafanaMonitoringV1alpha1IntegrationSpecType

Type informs Grafana Agent Operator about how to manage the integration being configured.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**all_nodes** | **bool** | When true, the configured integration should be run on every Node in the cluster. This is required for Integrations that generate Node-specific metrics like node_exporter, otherwise it must be false to avoid generating duplicate metrics. | [optional] 
**unique** | **bool** | Whether this integration can only be defined once for a Grafana Agent process, such as statsd_exporter. It is invalid for a GrafanaAgent to discover multiple unique Integrations with the same Integration name (i.e., a single GrafanaAgent cannot deploy two statsd_exporters). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


