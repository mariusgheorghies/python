# IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecDiskSetupPartitions

Partition defines how to create and layout a partition.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device** | **str** | Device is the name of the device. | 
**layout** | **bool** | Layout specifies the device layout. If it is true, a single partition will be created for the entire device. When layout is false, it means don&#39;t partition or ignore existing partitioning. | 
**overwrite** | **bool** | Overwrite describes whether to skip checks and create the partition if a partition or filesystem is found on the device. Use with caution. Default is &#39;false&#39;. | [optional] 
**table_type** | **str** | TableType specifies the tupe of partition table. The following are supported: &#39;mbr&#39;: default and setups a MS-DOS partition table &#39;gpt&#39;: setups a GPT partition table | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


