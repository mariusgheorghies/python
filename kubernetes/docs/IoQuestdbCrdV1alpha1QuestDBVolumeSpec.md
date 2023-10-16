# IoQuestdbCrdV1alpha1QuestDBVolumeSpec

QuestDBVolumeSpec defines the desired state of QuestDBVolume
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws** | [**IoQuestdbCrdV1alpha1QuestDBVolumeSpecAws**](IoQuestdbCrdV1alpha1QuestDBVolumeSpecAws.md) |  | [optional] 
**cloud_ids** | [**IoQuestdbCrdV1alpha1QuestDBCopySpecCloudIds**](IoQuestdbCrdV1alpha1QuestDBCopySpecCloudIds.md) |  | [optional] 
**filesystem** | **str** | Volume filesystem.  Currently supports ext4 (by default) or zfs | [optional] 
**size** | [**object**](.md) | Volume size | [optional] 
**snapshot** | [**IoQuestdbCrdV1alpha1QuestDBSpecVolumeSnapshot**](IoQuestdbCrdV1alpha1QuestDBSpecVolumeSnapshot.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


