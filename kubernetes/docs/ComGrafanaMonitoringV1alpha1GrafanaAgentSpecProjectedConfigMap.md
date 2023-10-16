# ComGrafanaMonitoringV1alpha1GrafanaAgentSpecProjectedConfigMap

configMap information about the configMap data to project
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**list[ComGrafanaMonitoringV1alpha1GrafanaAgentSpecConfigMapItems]**](ComGrafanaMonitoringV1alpha1GrafanaAgentSpecConfigMapItems.md) | items if unspecified, each key-value pair in the Data field of the referenced ConfigMap will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the ConfigMap, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the &#39;..&#39; path or start with &#39;..&#39;. | [optional] 
**name** | **str** | Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid? | [optional] 
**optional** | **bool** | optional specify whether the ConfigMap or its keys must be defined | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

