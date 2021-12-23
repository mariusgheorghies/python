# IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecDiskSetupFilesystems

Filesystem defines the file systems to be created.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device** | **str** | Device specifies the device name | 
**extra_opts** | **list[str]** | ExtraOpts defined extra options to add to the command for creating the file system. | [optional] 
**filesystem** | **str** | Filesystem specifies the file system type. | 
**label** | **str** | Label specifies the file system label to be used. If set to None, no label is used. | 
**overwrite** | **bool** | Overwrite defines whether or not to overwrite any existing filesystem. If true, any pre-existing file system will be destroyed. Use with Caution. | [optional] 
**partition** | **str** | Partition specifies the partition to use. The valid options are: \&quot;auto|any\&quot;, \&quot;auto\&quot;, \&quot;any\&quot;, \&quot;none\&quot;, and &lt;NUM&gt;, where NUM is the actual partition number. | [optional] 
**replace_fs** | **str** | ReplaceFS is a special directive, used for Microsoft Azure that instructs cloud-init to replace a file system of &lt;FS_TYPE&gt;. NOTE: unless you define a label, this requires the use of the &#39;any&#39; partition directive. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


