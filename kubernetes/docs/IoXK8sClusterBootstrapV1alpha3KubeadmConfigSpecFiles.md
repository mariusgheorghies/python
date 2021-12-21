# IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecFiles

File defines the input for generating write_files in cloud-init.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** | Content is the actual content of the file. | [optional] 
**content_from** | [**IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecContentFrom**](IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecContentFrom.md) |  | [optional] 
**encoding** | **str** | Encoding specifies the encoding of the file contents. | [optional] 
**owner** | **str** | Owner specifies the ownership of the file, e.g. \&quot;root:root\&quot;. | [optional] 
**path** | **str** | Path specifies the full path on disk where to store the file. | 
**permissions** | **str** | Permissions specifies the permissions to assign to the file, e.g. \&quot;0640\&quot;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


