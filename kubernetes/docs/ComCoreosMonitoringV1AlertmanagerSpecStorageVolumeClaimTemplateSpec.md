# ComCoreosMonitoringV1AlertmanagerSpecStorageVolumeClaimTemplateSpec

Spec defines the desired characteristics of a volume requested by a pod author. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_modes** | **list[str]** | AccessModes contains the desired access modes the volume should have. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes-1 | [optional] 
**data_source** | [**ComCoreosMonitoringV1AlertmanagerSpecStorageEphemeralVolumeClaimTemplateSpecDataSource**](ComCoreosMonitoringV1AlertmanagerSpecStorageEphemeralVolumeClaimTemplateSpecDataSource.md) |  | [optional] 
**data_source_ref** | [**ComCoreosMonitoringV1AlertmanagerSpecStorageEphemeralVolumeClaimTemplateSpecDataSourceRef**](ComCoreosMonitoringV1AlertmanagerSpecStorageEphemeralVolumeClaimTemplateSpecDataSourceRef.md) |  | [optional] 
**resources** | [**ComCoreosMonitoringV1AlertmanagerSpecStorageEphemeralVolumeClaimTemplateSpecResources**](ComCoreosMonitoringV1AlertmanagerSpecStorageEphemeralVolumeClaimTemplateSpecResources.md) |  | [optional] 
**selector** | [**ComCoreosMonitoringV1AlertmanagerSpecStorageEphemeralVolumeClaimTemplateSpecSelector**](ComCoreosMonitoringV1AlertmanagerSpecStorageEphemeralVolumeClaimTemplateSpecSelector.md) |  | [optional] 
**storage_class_name** | **str** | Name of the StorageClass required by the claim. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#class-1 | [optional] 
**volume_mode** | **str** | volumeMode defines what type of volume is required by the claim. Value of Filesystem is implied when not included in claim spec. | [optional] 
**volume_name** | **str** | VolumeName is the binding reference to the PersistentVolume backing this claim. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


