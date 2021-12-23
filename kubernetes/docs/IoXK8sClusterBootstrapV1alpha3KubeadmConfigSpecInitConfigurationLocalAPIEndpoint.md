# IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecInitConfigurationLocalAPIEndpoint

LocalAPIEndpoint represents the endpoint of the API server instance that's deployed on this control plane node In HA setups, this differs from ClusterConfiguration.ControlPlaneEndpoint in the sense that ControlPlaneEndpoint is the global endpoint for the cluster, which then loadbalances the requests to each individual API server. This configuration object lets you customize what IP/DNS name and port the local API server advertises it's accessible on. By default, kubeadm tries to auto-detect the IP of the default interface and use that, but in case that process fails you may set the desired value here.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advertise_address** | **str** | AdvertiseAddress sets the IP address for the API server to advertise. | 
**bind_port** | **int** | BindPort sets the secure port for the API Server to bind to. Defaults to 6443. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


