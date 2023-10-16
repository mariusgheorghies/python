# IoQuestdbCrdV1alpha1QuestDBSpecVolume

Volume configuration
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**encrypted** | **bool** | Encrypt volume | [optional] 
**filesystem** | **str** | Volume filesystem.  Currently supports ext4 (by default) or zfs | [optional] 
**iops** | **int** | Volume IOPS | [optional] 
**size** | [**object**](.md) | Volume size | [optional] 
**snapshot** | [**IoQuestdbCrdV1alpha1QuestDBSpecVolumeSnapshot**](IoQuestdbCrdV1alpha1QuestDBSpecVolumeSnapshot.md) |  | [optional] 
**throughput** | **int** | Volume throughput | [optional] 
**type** | **str** | Volume type or storage class (example: gp3) | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


