# IoTigeraOperatorV1InstallationStatusComputed

Computed is the final installation including overlaid resources.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**calico_network** | [**IoTigeraOperatorV1InstallationSpecCalicoNetwork**](IoTigeraOperatorV1InstallationSpecCalicoNetwork.md) |  | [optional] 
**certificate_management** | [**IoTigeraOperatorV1InstallationSpecCertificateManagement**](IoTigeraOperatorV1InstallationSpecCertificateManagement.md) |  | [optional] 
**cni** | [**IoTigeraOperatorV1InstallationSpecCni**](IoTigeraOperatorV1InstallationSpecCni.md) |  | [optional] 
**component_resources** | [**list[IoTigeraOperatorV1InstallationSpecComponentResources]**](IoTigeraOperatorV1InstallationSpecComponentResources.md) | ComponentResources can be used to customize the resource requirements for each component. Node, Typha, and KubeControllers are supported for installations. | [optional] 
**control_plane_node_selector** | **dict(str, str)** | ControlPlaneNodeSelector is used to select control plane nodes on which to run Calico components. This is globally applied to all resources created by the operator excluding daemonsets. | [optional] 
**control_plane_tolerations** | [**list[ComCoreosMonitoringV1AlertmanagerSpecTolerations]**](ComCoreosMonitoringV1AlertmanagerSpecTolerations.md) | ControlPlaneTolerations specify tolerations which are then globally applied to all resources created by the operator. | [optional] 
**flex_volume_path** | **str** | FlexVolumePath optionally specifies a custom path for FlexVolume. If not specified, FlexVolume will be enabled by default. If set to &#39;None&#39;, FlexVolume will be disabled. The default is based on the kubernetesProvider. | [optional] 
**image_path** | **str** | ImagePath allows for the path part of an image to be specified. If specified then the specified value will be used as the image path for each image. If not specified or empty, the default for each image will be used. A special case value, UseDefault, is supported to explicitly specify the default image path will be used for each image.   Image format:    &#x60;&lt;registry&gt;/&lt;imagePath&gt;/&lt;imagePrefix&gt;&lt;imageName&gt;:&lt;image-tag&gt;&#x60;   This option allows configuring the &#x60;&lt;imagePath&gt;&#x60; portion of the above format. | [optional] 
**image_prefix** | **str** | ImagePrefix allows for the prefix part of an image to be specified. If specified then the given value will be used as a prefix on each image. If not specified or empty, no prefix will be used. A special case value, UseDefault, is supported to explicitly specify the default image prefix will be used for each image.   Image format:    &#x60;&lt;registry&gt;/&lt;imagePath&gt;/&lt;imagePrefix&gt;&lt;imageName&gt;:&lt;image-tag&gt;&#x60;   This option allows configuring the &#x60;&lt;imagePrefix&gt;&#x60; portion of the above format. | [optional] 
**image_pull_secrets** | [**list[ComCoreosMonitoringV1AlertmanagerSpecImagePullSecrets]**](ComCoreosMonitoringV1AlertmanagerSpecImagePullSecrets.md) | ImagePullSecrets is an array of references to container registry pull secrets to use. These are applied to all images to be pulled. | [optional] 
**kubernetes_provider** | **str** | KubernetesProvider specifies a particular provider of the Kubernetes platform and enables provider-specific configuration. If the specified value is empty, the Operator will attempt to automatically determine the current provider. If the specified value is not empty, the Operator will still attempt auto-detection, but will additionally compare the auto-detected value to the specified value to confirm they match. | [optional] 
**node_metrics_port** | **int** | NodeMetricsPort specifies which port calico/node serves prometheus metrics on. By default, metrics are not enabled. If specified, this overrides any FelixConfiguration resources which may exist. If omitted, then prometheus metrics may still be configured through FelixConfiguration. | [optional] 
**node_update_strategy** | [**IoTigeraOperatorV1InstallationSpecNodeUpdateStrategy**](IoTigeraOperatorV1InstallationSpecNodeUpdateStrategy.md) |  | [optional] 
**registry** | **str** | Registry is the default Docker registry used for component Docker images. If specified, all images will be pulled from this registry. If not specified then the default registries will be used. A special case value, UseDefault, is supported to explicitly specify the default registries will be used.   Image format:    &#x60;&lt;registry&gt;/&lt;imagePath&gt;/&lt;imagePrefix&gt;&lt;imageName&gt;:&lt;image-tag&gt;&#x60;   This option allows configuring the &#x60;&lt;registry&gt;&#x60; portion of the above format. | [optional] 
**typha_affinity** | [**IoTigeraOperatorV1InstallationSpecTyphaAffinity**](IoTigeraOperatorV1InstallationSpecTyphaAffinity.md) |  | [optional] 
**typha_metrics_port** | **int** | TyphaMetricsPort specifies which port calico/typha serves prometheus metrics on. By default, metrics are not enabled. | [optional] 
**variant** | **str** | Variant is the product to install - one of Calico or TigeraSecureEnterprise Default: Calico | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


