# IoXK8sClusterBootstrapV1alpha4KubeadmConfigSpecClusterConfiguration

ClusterConfiguration along with InitConfiguration are the configurations necessary for the init command
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_server** | [**IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecClusterConfigurationApiServer**](IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecClusterConfigurationApiServer.md) |  | [optional] 
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**certificates_dir** | **str** | CertificatesDir specifies where to store or look for all required certificates. NB: if not provided, this will default to &#x60;/etc/kubernetes/pki&#x60; | [optional] 
**cluster_name** | **str** | The cluster name | [optional] 
**control_plane_endpoint** | **str** | ControlPlaneEndpoint sets a stable IP address or DNS name for the control plane; it can be a valid IP address or a RFC-1123 DNS subdomain, both with optional TCP port. In case the ControlPlaneEndpoint is not specified, the AdvertiseAddress + BindPort are used; in case the ControlPlaneEndpoint is specified but without a TCP port, the BindPort is used. Possible usages are: e.g. In a cluster with more than one control plane instances, this field should be assigned the address of the external load balancer in front of the control plane instances. e.g.  in environments with enforced node recycling, the ControlPlaneEndpoint could be used for assigning a stable DNS to the control plane. NB: This value defaults to the first value in the Cluster object status.apiEndpoints array. | [optional] 
**controller_manager** | [**IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecClusterConfigurationControllerManager**](IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecClusterConfigurationControllerManager.md) |  | [optional] 
**dns** | [**IoXK8sClusterBootstrapV1alpha4KubeadmConfigSpecClusterConfigurationDns**](IoXK8sClusterBootstrapV1alpha4KubeadmConfigSpecClusterConfigurationDns.md) |  | [optional] 
**etcd** | [**IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecClusterConfigurationEtcd**](IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecClusterConfigurationEtcd.md) |  | [optional] 
**feature_gates** | **dict(str, bool)** | FeatureGates enabled by the user. | [optional] 
**image_repository** | **str** | ImageRepository sets the container registry to pull images from. If empty, &#x60;k8s.gcr.io&#x60; will be used by default; in case of kubernetes version is a CI build (kubernetes version starts with &#x60;ci/&#x60; or &#x60;ci-cross/&#x60;) &#x60;gcr.io/k8s-staging-ci-images&#x60; will be used as a default for control plane components and for kube-proxy, while &#x60;k8s.gcr.io&#x60; will be used for all the other images. | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the kubernetes.client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**kubernetes_version** | **str** | KubernetesVersion is the target version of the control plane. NB: This value defaults to the Machine object spec.version | [optional] 
**networking** | [**IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecClusterConfigurationNetworking**](IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecClusterConfigurationNetworking.md) |  | [optional] 
**scheduler** | [**IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecClusterConfigurationScheduler**](IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecClusterConfigurationScheduler.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


