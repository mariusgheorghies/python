# ComGrafanaMonitoringV1alpha1GrafanaAgentSpecStorageVolumeClaimTemplateSpec

Spec defines the desired characteristics of a volume requested by a pod author. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_modes** | **list[str]** | accessModes contains the desired access modes the volume should have. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes-1 | [optional] 
**data_source** | [**ComGrafanaMonitoringV1alpha1GrafanaAgentSpecStorageEphemeralVolumeClaimTemplateSpecDataSource**](ComGrafanaMonitoringV1alpha1GrafanaAgentSpecStorageEphemeralVolumeClaimTemplateSpecDataSource.md) |  | [optional] 
**data_source_ref** | [**ComGrafanaMonitoringV1alpha1GrafanaAgentSpecStorageEphemeralVolumeClaimTemplateSpecDataSourceRef**](ComGrafanaMonitoringV1alpha1GrafanaAgentSpecStorageEphemeralVolumeClaimTemplateSpecDataSourceRef.md) |  | [optional] 
**resources** | [**ComGrafanaMonitoringV1alpha1GrafanaAgentSpecStorageEphemeralVolumeClaimTemplateSpecResources**](ComGrafanaMonitoringV1alpha1GrafanaAgentSpecStorageEphemeralVolumeClaimTemplateSpecResources.md) |  | [optional] 
**selector** | [**ComGrafanaMonitoringV1alpha1GrafanaAgentSpecStorageEphemeralVolumeClaimTemplateSpecSelector**](ComGrafanaMonitoringV1alpha1GrafanaAgentSpecStorageEphemeralVolumeClaimTemplateSpecSelector.md) |  | [optional] 
**storage_class_name** | **str** | storageClassName is the name of the StorageClass required by the claim. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#class-1 | [optional] 
**volume_mode** | **str** | volumeMode defines what type of volume is required by the claim. Value of Filesystem is implied when not included in claim spec. | [optional] 
**volume_name** | **str** | volumeName is the binding reference to the PersistentVolume backing this claim. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


