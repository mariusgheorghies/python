# IoXK8sClusterBootstrapV1alpha4KubeadmConfigSpec

KubeadmConfigSpec defines the desired state of KubeadmConfig. Either ClusterConfiguration and InitConfiguration should be defined or the JoinConfiguration should be defined.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_configuration** | [**IoXK8sClusterBootstrapV1alpha4KubeadmConfigSpecClusterConfiguration**](IoXK8sClusterBootstrapV1alpha4KubeadmConfigSpecClusterConfiguration.md) |  | [optional] 
**disk_setup** | [**IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecDiskSetup**](IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecDiskSetup.md) |  | [optional] 
**files** | [**list[IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecFiles]**](IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecFiles.md) | Files specifies extra files to be passed to user_data upon creation. | [optional] 
**format** | **str** | Format specifies the output format of the bootstrap data | [optional] 
**init_configuration** | [**IoXK8sClusterBootstrapV1alpha4KubeadmConfigSpecInitConfiguration**](IoXK8sClusterBootstrapV1alpha4KubeadmConfigSpecInitConfiguration.md) |  | [optional] 
**join_configuration** | [**IoXK8sClusterBootstrapV1alpha4KubeadmConfigSpecJoinConfiguration**](IoXK8sClusterBootstrapV1alpha4KubeadmConfigSpecJoinConfiguration.md) |  | [optional] 
**mounts** | **list[list[str]]** | Mounts specifies a list of mount points to be setup. | [optional] 
**ntp** | [**IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecNtp**](IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecNtp.md) |  | [optional] 
**post_kubeadm_commands** | **list[str]** | PostKubeadmCommands specifies extra commands to run after kubeadm runs | [optional] 
**pre_kubeadm_commands** | **list[str]** | PreKubeadmCommands specifies extra commands to run before kubeadm runs | [optional] 
**use_experimental_retry_join** | **bool** | UseExperimentalRetryJoin replaces a basic kubeadm command with a shell script with retries for joins.   This is meant to be an experimental temporary workaround on some environments where joins fail due to timing (and other issues). The long term goal is to add retries to kubeadm proper and use that functionality.   This will add about 40KB to userdata   For more information, refer to https://github.com/kubernetes-sigs/cluster-api/pull/2763#discussion_r397306055. | [optional] 
**users** | [**list[IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecUsers]**](IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecUsers.md) | Users specifies extra users to add | [optional] 
**verbosity** | **int** | Verbosity is the number for the kubeadm log level verbosity. It overrides the &#x60;--v&#x60; flag in kubeadm commands. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


