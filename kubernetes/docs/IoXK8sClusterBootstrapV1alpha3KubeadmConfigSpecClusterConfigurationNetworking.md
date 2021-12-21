# IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecClusterConfigurationNetworking

Networking holds configuration for the networking topology of the cluster. NB: This value defaults to the Cluster object spec.clusterNetwork.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dns_domain** | **str** | DNSDomain is the dns domain used by k8s services. Defaults to \&quot;cluster.local\&quot;. | [optional] 
**pod_subnet** | **str** | PodSubnet is the subnet used by pods. If unset, the API server will not allocate CIDR ranges for every node. Defaults to a comma-delimited string of the Cluster object&#39;s spec.clusterNetwork.services.cidrBlocks if that is set | [optional] 
**service_subnet** | **str** | ServiceSubnet is the subnet used by k8s services. Defaults to a comma-delimited string of the Cluster object&#39;s spec.clusterNetwork.pods.cidrBlocks, or to \&quot;10.96.0.0/12\&quot; if that&#39;s unset. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


