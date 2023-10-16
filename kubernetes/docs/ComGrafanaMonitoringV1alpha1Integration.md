# ComGrafanaMonitoringV1alpha1Integration

Integration runs a single Grafana Agent integration. Integrations that generate telemetry must be configured to send that telemetry somewhere, such as autoscrape for exporter-based integrations.   Integrations have access to the LogsInstances and MetricsInstances in the same GrafanaAgent resource set, referenced by the <namespace>/<name> of the Instance resource.   For example, if there is a default/production MetricsInstance, you can configure a supported integration's autoscrape block with:   autoscrape: enable: true metrics_instance: default/production   There is currently no way for telemetry created by an Operator-managed integration to be collected from outside of the integration itself.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the kubernetes.client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) |  | [optional] 
**spec** | [**ComGrafanaMonitoringV1alpha1IntegrationSpec**](ComGrafanaMonitoringV1alpha1IntegrationSpec.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


