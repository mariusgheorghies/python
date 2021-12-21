# IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecClusterConfigurationEtcdExternal

External describes how to connect to an external etcd cluster Local and External are mutually exclusive
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ca_file** | **str** | CAFile is an SSL Certificate Authority file used to secure etcd communication. Required if using a TLS connection. | 
**cert_file** | **str** | CertFile is an SSL certification file used to secure etcd communication. Required if using a TLS connection. | 
**endpoints** | **list[str]** | Endpoints of etcd members. Required for ExternalEtcd. | 
**key_file** | **str** | KeyFile is an SSL key file used to secure etcd communication. Required if using a TLS connection. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


