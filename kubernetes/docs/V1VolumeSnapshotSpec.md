# V1VolumeSnapshotSpec

spec defines the desired characteristics of a snapshot requested by a user. More info: https://kubernetes.io/docs/concepts/storage/volume-snapshots#volumesnapshots Required.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | [**V1VolumeSnapshotSpecSource**](V1VolumeSnapshotSpecSource.md) |  | 
**volume_snapshot_class_name** | **str** | VolumeSnapshotClassName is the name of the VolumeSnapshotClass requested by the VolumeSnapshot. VolumeSnapshotClassName may be left nil to indicate that the default SnapshotClass should be used. A given cluster may have multiple default Volume SnapshotClasses: one default per CSI Driver. If a VolumeSnapshot does not specify a SnapshotClass, VolumeSnapshotSource will be checked to figure out what the associated CSI Driver is, and the default VolumeSnapshotClass associated with that CSI Driver will be used. If more than one VolumeSnapshotClass exist for a given CSI Driver and more than one have been marked as default, CreateSnapshot will fail and generate an event. Empty string is not allowed for this field. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


