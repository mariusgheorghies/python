# V1VolumeSnapshotContentStatus

status represents the current information of a snapshot.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creation_time** | **int** | creationTime is the timestamp when the point-in-time snapshot is taken by the underlying storage system. In dynamic snapshot creation case, this field will be filled in by the CSI snapshotter sidecar with the \&quot;creation_time\&quot; value returned from CSI \&quot;CreateSnapshot\&quot; gRPC call. For a pre-existing snapshot, this field will be filled with the \&quot;creation_time\&quot; value returned from the CSI \&quot;ListSnapshots\&quot; gRPC call if the driver supports it. If not specified, it indicates the creation time is unknown. The format of this field is a Unix nanoseconds time encoded as an int64. On Unix, the command &#x60;date +%s%N&#x60; returns the current time in nanoseconds since 1970-01-01 00:00:00 UTC. | [optional] 
**error** | [**V1VolumeSnapshotContentStatusError**](V1VolumeSnapshotContentStatusError.md) |  | [optional] 
**ready_to_use** | **bool** | readyToUse indicates if a snapshot is ready to be used to restore a volume. In dynamic snapshot creation case, this field will be filled in by the CSI snapshotter sidecar with the \&quot;ready_to_use\&quot; value returned from CSI \&quot;CreateSnapshot\&quot; gRPC call. For a pre-existing snapshot, this field will be filled with the \&quot;ready_to_use\&quot; value returned from the CSI \&quot;ListSnapshots\&quot; gRPC call if the driver supports it, otherwise, this field will be set to \&quot;True\&quot;. If not specified, it means the readiness of a snapshot is unknown. | [optional] 
**restore_size** | **int** | restoreSize represents the complete size of the snapshot in bytes. In dynamic snapshot creation case, this field will be filled in by the CSI snapshotter sidecar with the \&quot;size_bytes\&quot; value returned from CSI \&quot;CreateSnapshot\&quot; gRPC call. For a pre-existing snapshot, this field will be filled with the \&quot;size_bytes\&quot; value returned from the CSI \&quot;ListSnapshots\&quot; gRPC call if the driver supports it. When restoring a volume from this snapshot, the size of the volume MUST NOT be smaller than the restoreSize if it is specified, otherwise the restoration will fail. If not specified, it indicates that the size is unknown. | [optional] 
**snapshot_handle** | **str** | snapshotHandle is the CSI \&quot;snapshot_id\&quot; of a snapshot on the underlying storage system. If not specified, it indicates that dynamic snapshot creation has either failed or it is still in progress. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


