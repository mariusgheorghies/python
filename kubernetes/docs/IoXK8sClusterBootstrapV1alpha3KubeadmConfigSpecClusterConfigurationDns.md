# IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecClusterConfigurationDns

DNS defines the options for the DNS add-on installed in the cluster.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image_repository** | **str** | ImageRepository sets the container registry to pull images from. if not set, the ImageRepository defined in ClusterConfiguration will be used instead. | [optional] 
**image_tag** | **str** | ImageTag allows to specify a tag for the image. In case this value is set, kubeadm does not change automatically the version of the above components during upgrades. | [optional] 
**type** | **str** | Type defines the DNS add-on to be used | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


