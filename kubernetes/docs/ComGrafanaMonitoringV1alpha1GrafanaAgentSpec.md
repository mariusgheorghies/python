# ComGrafanaMonitoringV1alpha1GrafanaAgentSpec

Spec holds the specification of the desired behavior for the Grafana Agent cluster.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affinity** | [**ComGrafanaMonitoringV1alpha1GrafanaAgentSpecAffinity**](ComGrafanaMonitoringV1alpha1GrafanaAgentSpecAffinity.md) |  | [optional] 
**api_server** | [**ComGrafanaMonitoringV1alpha1GrafanaAgentSpecApiServer**](ComGrafanaMonitoringV1alpha1GrafanaAgentSpecApiServer.md) |  | [optional] 
**config_maps** | **list[str]** | ConfigMaps is a list of config maps in the same namespace as the GrafanaAgent object which will be mounted into each running Grafana Agent pod. The ConfigMaps are mounted into /etc/grafana-agent/extra-configmaps/&lt;configmap-name&gt;. | [optional] 
**containers** | [**list[ComGrafanaMonitoringV1alpha1GrafanaAgentSpecContainers]**](ComGrafanaMonitoringV1alpha1GrafanaAgentSpecContainers.md) | Containers lets you inject additional containers or modify operator-generated containers. This can be used to add an authentication proxy to a Grafana Agent pod or to change the behavior of an operator-generated container. Containers described here modify an operator-generated container if they share the same name and if modifications are done via a strategic merge patch. The current container names are: &#x60;grafana-agent&#x60; and &#x60;config-reloader&#x60;. Overriding containers is entirely outside the scope of what the Grafana Agent team supports and by doing so, you accept that this behavior may break at any time without notice. | [optional] 
**disable_reporting** | **bool** | disableReporting disables reporting of enabled feature flags to Grafana. | [optional] 
**disable_support_bundle** | **bool** | disableSupportBundle disables the generation of support bundles. | [optional] 
**enable_config_read_api** | **bool** | enableConfigReadAPI enables the read API for viewing the currently running config port 8080 on the agent. | [optional] 
**image** | **str** | Image, when specified, overrides the image used to run Agent. Specify the image along with a tag. You still need to set the version to ensure Grafana Agent Operator knows which version of Grafana Agent is being configured. | [optional] 
**image_pull_secrets** | [**list[ComCoreosMonitoringV1AlertmanagerSpecImagePullSecrets]**](ComCoreosMonitoringV1AlertmanagerSpecImagePullSecrets.md) | ImagePullSecrets holds an optional list of references to Secrets within the same namespace used for pulling the Grafana Agent image from registries. More info: https://kubernetes.io/docs/concepts/containers/images/#specifying-imagepullsecrets-on-a-pod | [optional] 
**init_containers** | [**list[ComGrafanaMonitoringV1alpha1GrafanaAgentSpecContainers]**](ComGrafanaMonitoringV1alpha1GrafanaAgentSpecContainers.md) | InitContainers let you add initContainers to the pod definition. These can be used to, for example, fetch secrets for injection into the Grafana Agent configuration from external sources. Errors during the execution of an initContainer cause the pod to restart. More info: https://kubernetes.io/docs/concepts/workloads/pods/init-containers/ Using initContainers for any use case other than secret fetching is entirely outside the scope of what the Grafana Agent maintainers support and by doing so, you accept that this behavior may break at any time without notice. | [optional] 
**integrations** | [**ComGrafanaMonitoringV1alpha1GrafanaAgentSpecIntegrations**](ComGrafanaMonitoringV1alpha1GrafanaAgentSpecIntegrations.md) |  | [optional] 
**log_format** | **str** | LogFormat controls the logging format of the generated pods. Defaults to \&quot;logfmt\&quot; if not set. | [optional] 
**log_level** | **str** | LogLevel controls the log level of the generated pods. Defaults to \&quot;info\&quot; if not set. | [optional] 
**logs** | [**ComGrafanaMonitoringV1alpha1GrafanaAgentSpecLogs**](ComGrafanaMonitoringV1alpha1GrafanaAgentSpecLogs.md) |  | [optional] 
**metrics** | [**ComGrafanaMonitoringV1alpha1GrafanaAgentSpecMetrics**](ComGrafanaMonitoringV1alpha1GrafanaAgentSpecMetrics.md) |  | [optional] 
**node_selector** | **dict(str, str)** | NodeSelector defines which nodes pods should be scheduling on. | [optional] 
**paused** | **bool** | Paused prevents actions except for deletion to be performed on the underlying managed objects. | [optional] 
**pod_metadata** | [**ComGrafanaMonitoringV1alpha1GrafanaAgentSpecPodMetadata**](ComGrafanaMonitoringV1alpha1GrafanaAgentSpecPodMetadata.md) |  | [optional] 
**port_name** | **str** | Port name used for the pods and governing service. This defaults to agent-metrics. | [optional] 
**priority_class_name** | **str** | PriorityClassName is the priority class assigned to pods. | [optional] 
**resources** | [**ComGrafanaMonitoringV1alpha1GrafanaAgentSpecResources1**](ComGrafanaMonitoringV1alpha1GrafanaAgentSpecResources1.md) |  | [optional] 
**runtime_class_name** | **str** | RuntimeClassName is the runtime class assigned to pods. | [optional] 
**secrets** | **list[str]** | Secrets is a list of secrets in the same namespace as the GrafanaAgent object which will be mounted into each running Grafana Agent pod. The secrets are mounted into /etc/grafana-agent/extra-secrets/&lt;secret-name&gt;. | [optional] 
**security_context** | [**ComGrafanaMonitoringV1alpha1GrafanaAgentSpecSecurityContext**](ComGrafanaMonitoringV1alpha1GrafanaAgentSpecSecurityContext.md) |  | [optional] 
**service_account_name** | **str** | ServiceAccountName is the name of the ServiceAccount to use for running Grafana Agent pods. | [optional] 
**storage** | [**ComGrafanaMonitoringV1alpha1GrafanaAgentSpecStorage**](ComGrafanaMonitoringV1alpha1GrafanaAgentSpecStorage.md) |  | [optional] 
**tolerations** | [**list[ComCoreosMonitoringV1AlertmanagerSpecTolerations]**](ComCoreosMonitoringV1AlertmanagerSpecTolerations.md) | Tolerations, if specified, controls the pod&#39;s tolerations. | [optional] 
**topology_spread_constraints** | [**list[ComGrafanaMonitoringV1alpha1GrafanaAgentSpecTopologySpreadConstraints]**](ComGrafanaMonitoringV1alpha1GrafanaAgentSpecTopologySpreadConstraints.md) | TopologySpreadConstraints, if specified, controls the pod&#39;s topology spread constraints. | [optional] 
**version** | **str** | Version of Grafana Agent to be deployed. | [optional] 
**volume_mounts** | [**list[ComCoreosMonitoringV1AlertmanagerSpecVolumeMounts]**](ComCoreosMonitoringV1AlertmanagerSpecVolumeMounts.md) | VolumeMounts lets you configure additional VolumeMounts on the output StatefulSet definition. Specified VolumeMounts are appended to other VolumeMounts generated as a result of StorageSpec objects in the Grafana Agent container. | [optional] 
**volumes** | [**list[ComGrafanaMonitoringV1alpha1GrafanaAgentSpecVolumes]**](ComGrafanaMonitoringV1alpha1GrafanaAgentSpecVolumes.md) | Volumes allows configuration of additional volumes on the output StatefulSet definition. The volumes specified are appended to other volumes that are generated as a result of StorageSpec objects. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


