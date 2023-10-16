# V1VolumeSnapshotContentSpec

spec defines properties of a VolumeSnapshotContent created by the underlying storage system. Required.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deletion_policy** | **str** | deletionPolicy determines whether this VolumeSnapshotContent and its physical snapshot on the underlying storage system should be deleted when its bound VolumeSnapshot is deleted. Supported values are \&quot;Retain\&quot; and \&quot;Delete\&quot;. \&quot;Retain\&quot; means that the VolumeSnapshotContent and its physical snapshot on underlying storage system are kept. \&quot;Delete\&quot; means that the VolumeSnapshotContent and its physical snapshot on underlying storage system are deleted. For dynamically provisioned snapshots, this field will automatically be filled in by the CSI snapshotter sidecar with the \&quot;DeletionPolicy\&quot; field defined in the corresponding VolumeSnapshotClass. For pre-existing snapshots, users MUST specify this field when creating the VolumeSnapshotContent object. Required. | 
**driver** | **str** | driver is the name of the CSI driver used to create the physical snapshot on the underlying storage system. This MUST be the same as the name returned by the CSI GetPluginName() call for that driver. Required. | 
**source** | [**V1VolumeSnapshotContentSpecSource**](V1VolumeSnapshotContentSpecSource.md) |  | 
**source_volume_mode** | **str** | SourceVolumeMode is the mode of the volume whose snapshot is taken. Can be either “Filesystem” or “Block”. If not specified, it indicates the source volume&#39;s mode is unknown. This field is immutable. This field is an alpha field. | [optional] 
**volume_snapshot_class_name** | **str** | name of the VolumeSnapshotClass from which this snapshot was (or will be) created. Note that after provisioning, the VolumeSnapshotClass may be deleted or recreated with different set of values, and as such, should not be referenced post-snapshot creation. | [optional] 
**volume_snapshot_ref** | [**V1VolumeSnapshotContentSpecVolumeSnapshotRef**](V1VolumeSnapshotContentSpecVolumeSnapshotRef.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


