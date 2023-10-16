# ComGrafanaMonitoringV1alpha1GrafanaAgentSpecStorageVolumeClaimTemplate

A PVC spec to be used by the StatefulSet. The easiest way to use a volume that cannot be automatically provisioned (for whatever reason) is to use a label selector alongside manually created PersistentVolumes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the kubernetes.client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**ComCoreosMonitoringV1AlertmanagerSpecStorageVolumeClaimTemplateMetadata**](ComCoreosMonitoringV1AlertmanagerSpecStorageVolumeClaimTemplateMetadata.md) |  | [optional] 
**spec** | [**ComGrafanaMonitoringV1alpha1GrafanaAgentSpecStorageVolumeClaimTemplateSpec**](ComGrafanaMonitoringV1alpha1GrafanaAgentSpecStorageVolumeClaimTemplateSpec.md) |  | [optional] 
**status** | [**ComGrafanaMonitoringV1alpha1GrafanaAgentSpecStorageVolumeClaimTemplateStatus**](ComGrafanaMonitoringV1alpha1GrafanaAgentSpecStorageVolumeClaimTemplateStatus.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


