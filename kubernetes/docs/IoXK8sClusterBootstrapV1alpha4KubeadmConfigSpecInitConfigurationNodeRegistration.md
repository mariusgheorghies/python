# IoXK8sClusterBootstrapV1alpha4KubeadmConfigSpecInitConfigurationNodeRegistration

NodeRegistration holds fields that relate to registering the new control-plane node to the cluster. When used in the context of control plane nodes, NodeRegistration should remain consistent across both InitConfiguration and JoinConfiguration
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cri_socket** | **str** | CRISocket is used to retrieve container runtime info. This information will be annotated to the Node API object, for later re-use | [optional] 
**ignore_preflight_errors** | **list[str]** | IgnorePreflightErrors provides a slice of pre-flight errors to be ignored when the current node is registered. | [optional] 
**kubelet_extra_args** | **dict(str, str)** | KubeletExtraArgs passes through extra arguments to the kubelet. The arguments here are passed to the kubelet command line via the environment file kubeadm writes at runtime for the kubelet to source. This overrides the generic base-level configuration in the kubelet-config-1.X ConfigMap Flags have higher priority when parsing. These values are local and specific to the node kubeadm is executing on. | [optional] 
**name** | **str** | Name is the &#x60;.Metadata.Name&#x60; field of the Node API object that will be created in this &#x60;kubeadm init&#x60; or &#x60;kubeadm join&#x60; operation. This field is also used in the CommonName field of the kubelet&#39;s kubernetes.client certificate to the API server. Defaults to the hostname of the node if not provided. | [optional] 
**taints** | [**list[IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecInitConfigurationNodeRegistrationTaints]**](IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecInitConfigurationNodeRegistrationTaints.md) | Taints specifies the taints the Node API object should be registered with. If this field is unset, i.e. nil, in the &#x60;kubeadm init&#x60; process it will be defaulted to []v1.Taint{&#39;node-role.kubernetes.io/master&#x3D;\&quot;\&quot;&#39;}. If you don&#39;t want to taint your control-plane node, set this field to an empty slice, i.e. &#x60;taints: {}&#x60; in the YAML file. This field is solely used for Node registration. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


