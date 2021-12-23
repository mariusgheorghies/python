# IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecClusterConfigurationEtcdLocal

Local provides configuration knobs for configuring the local etcd instance Local and External are mutually exclusive
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_dir** | **str** | DataDir is the directory etcd will place its data. Defaults to \&quot;/var/lib/etcd\&quot;. | [optional] 
**extra_args** | **dict(str, str)** | ExtraArgs are extra arguments provided to the etcd binary when run inside a static pod. | [optional] 
**image_repository** | **str** | ImageRepository sets the container registry to pull images from. if not set, the ImageRepository defined in ClusterConfiguration will be used instead. | [optional] 
**image_tag** | **str** | ImageTag allows to specify a tag for the image. In case this value is set, kubeadm does not change automatically the version of the above components during upgrades. | [optional] 
**peer_cert_sa_ns** | **list[str]** | PeerCertSANs sets extra Subject Alternative Names for the etcd peer signing cert. | [optional] 
**server_cert_sa_ns** | **list[str]** | ServerCertSANs sets extra Subject Alternative Names for the etcd server signing cert. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


