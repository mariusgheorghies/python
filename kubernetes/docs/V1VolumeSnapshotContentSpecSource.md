# V1VolumeSnapshotContentSpecSource

source specifies whether the snapshot is (or should be) dynamically provisioned or already exists, and just requires a Kubernetes object representation. This field is immutable after creation. Required.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snapshot_handle** | **str** | snapshotHandle specifies the CSI \&quot;snapshot_id\&quot; of a pre-existing snapshot on the underlying storage system for which a Kubernetes object representation was (or should be) created. This field is immutable. | [optional] 
**volume_handle** | **str** | volumeHandle specifies the CSI \&quot;volume_id\&quot; of the volume from which a snapshot should be dynamically taken from. This field is immutable. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


