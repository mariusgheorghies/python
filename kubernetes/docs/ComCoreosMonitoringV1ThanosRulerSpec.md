# ComCoreosMonitoringV1ThanosRulerSpec

Specification of the desired behavior of the ThanosRuler cluster. More info: https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#spec-and-status
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affinity** | [**ComCoreosMonitoringV1AlertmanagerSpecAffinity**](ComCoreosMonitoringV1AlertmanagerSpecAffinity.md) |  | [optional] 
**alert_drop_labels** | **list[str]** | AlertDropLabels configure the label names which should be dropped in ThanosRuler alerts. The replica label &#x60;thanos_ruler_replica&#x60; will always be dropped in alerts. | [optional] 
**alert_query_url** | **str** | The external Query URL the Thanos Ruler will set in the &#39;Source&#39; field of all alerts. Maps to the &#39;--alert.query-url&#39; CLI arg. | [optional] 
**alert_relabel_config_file** | **str** | AlertRelabelConfigFile specifies the path of the alert relabeling configuration file. When used alongside with AlertRelabelConfigs, alertRelabelConfigFile takes precedence. | [optional] 
**alert_relabel_configs** | [**ComCoreosMonitoringV1ThanosRulerSpecAlertRelabelConfigs**](ComCoreosMonitoringV1ThanosRulerSpecAlertRelabelConfigs.md) |  | [optional] 
**alertmanagers_config** | [**ComCoreosMonitoringV1ThanosRulerSpecAlertmanagersConfig**](ComCoreosMonitoringV1ThanosRulerSpecAlertmanagersConfig.md) |  | [optional] 
**alertmanagers_url** | **list[str]** | Define URLs to send alerts to Alertmanager.  For Thanos v0.10.0 and higher, AlertManagersConfig should be used instead.  Note: this field will be ignored if AlertManagersConfig is specified. Maps to the &#x60;alertmanagers.url&#x60; arg. | [optional] 
**containers** | [**list[ComCoreosMonitoringV1AlertmanagerSpecContainers]**](ComCoreosMonitoringV1AlertmanagerSpecContainers.md) | Containers allows injecting additional containers or modifying operator generated containers. This can be used to allow adding an authentication proxy to a ThanosRuler pod or to change the behavior of an operator generated container. Containers described here modify an operator generated container if they share the same name and modifications are done via a strategic merge patch. The current container names are: &#x60;thanos-ruler&#x60; and &#x60;config-reloader&#x60;. Overriding containers is entirely outside the scope of what the maintainers will support and by doing so, you accept that this behaviour may break at any time without notice. | [optional] 
**enforced_namespace_label** | **str** | EnforcedNamespaceLabel enforces adding a namespace label of origin for each alert and metric that is user created. The label value will always be the namespace of the object that is being created. | [optional] 
**evaluation_interval** | **str** | Interval between consecutive evaluations. | [optional] 
**external_prefix** | **str** | The external URL the Thanos Ruler instances will be available under. This is necessary to generate correct URLs. This is necessary if Thanos Ruler is not served from root of a DNS name. | [optional] 
**grpc_server_tls_config** | [**ComCoreosMonitoringV1PrometheusSpecThanosGrpcServerTlsConfig**](ComCoreosMonitoringV1PrometheusSpecThanosGrpcServerTlsConfig.md) |  | [optional] 
**image** | **str** | Thanos container image URL. | [optional] 
**image_pull_secrets** | [**list[ComCoreosMonitoringV1AlertmanagerSpecImagePullSecrets]**](ComCoreosMonitoringV1AlertmanagerSpecImagePullSecrets.md) | An optional list of references to secrets in the same namespace to use for pulling thanos images from registries see http://kubernetes.io/docs/user-guide/images#specifying-imagepullsecrets-on-a-pod | [optional] 
**init_containers** | [**list[ComCoreosMonitoringV1AlertmanagerSpecContainers]**](ComCoreosMonitoringV1AlertmanagerSpecContainers.md) | InitContainers allows adding initContainers to the pod definition. Those can be used to e.g. fetch secrets for injection into the ThanosRuler configuration from external sources. Any errors during the execution of an initContainer will lead to a restart of the Pod. More info: https://kubernetes.io/docs/concepts/workloads/pods/init-containers/ Using initContainers for any use case other then secret fetching is entirely outside the scope of what the maintainers will support and by doing so, you accept that this behaviour may break at any time without notice. | [optional] 
**labels** | **dict(str, str)** | Labels configure the external label pairs to ThanosRuler. A default replica label &#x60;thanos_ruler_replica&#x60; will be always added  as a label with the value of the pod&#39;s name and it will be dropped in the alerts. | [optional] 
**listen_local** | **bool** | ListenLocal makes the Thanos ruler listen on loopback, so that it does not bind against the Pod IP. | [optional] 
**log_format** | **str** | Log format for ThanosRuler to be configured with. | [optional] 
**log_level** | **str** | Log level for ThanosRuler to be configured with. | [optional] 
**min_ready_seconds** | **int** | Minimum number of seconds for which a newly created pod should be ready without any of its container crashing for it to be considered available. Defaults to 0 (pod will be considered available as soon as it is ready) This is an alpha field and requires enabling StatefulSetMinReadySeconds feature gate. | [optional] 
**node_selector** | **dict(str, str)** | Define which Nodes the Pods are scheduled on. | [optional] 
**object_storage_config** | [**ComCoreosMonitoringV1PrometheusSpecThanosObjectStorageConfig**](ComCoreosMonitoringV1PrometheusSpecThanosObjectStorageConfig.md) |  | [optional] 
**object_storage_config_file** | **str** | ObjectStorageConfigFile specifies the path of the object storage configuration file. When used alongside with ObjectStorageConfig, ObjectStorageConfigFile takes precedence. | [optional] 
**paused** | **bool** | When a ThanosRuler deployment is paused, no actions except for deletion will be performed on the underlying objects. | [optional] 
**pod_metadata** | [**ComCoreosMonitoringV1ThanosRulerSpecPodMetadata**](ComCoreosMonitoringV1ThanosRulerSpecPodMetadata.md) |  | [optional] 
**port_name** | **str** | Port name used for the pods and governing service. This defaults to web | [optional] 
**priority_class_name** | **str** | Priority class assigned to the Pods | [optional] 
**prometheus_rules_excluded_from_enforce** | [**list[ComCoreosMonitoringV1PrometheusSpecPrometheusRulesExcludedFromEnforce]**](ComCoreosMonitoringV1PrometheusSpecPrometheusRulesExcludedFromEnforce.md) | PrometheusRulesExcludedFromEnforce - list of Prometheus rules to be excluded from enforcing of adding namespace labels. Works only if enforcedNamespaceLabel set to true. Make sure both ruleNamespace and ruleName are set for each pair | [optional] 
**query_config** | [**ComCoreosMonitoringV1ThanosRulerSpecQueryConfig**](ComCoreosMonitoringV1ThanosRulerSpecQueryConfig.md) |  | [optional] 
**query_endpoints** | **list[str]** | QueryEndpoints defines Thanos querier endpoints from which to query metrics. Maps to the --query flag of thanos ruler. | [optional] 
**replicas** | **int** | Number of thanos ruler instances to deploy. | [optional] 
**resources** | [**ComCoreosMonitoringV1ThanosRulerSpecResources**](ComCoreosMonitoringV1ThanosRulerSpecResources.md) |  | [optional] 
**retention** | **str** | Time duration ThanosRuler shall retain data for. Default is &#39;24h&#39;, and must match the regular expression &#x60;[0-9]+(ms|s|m|h|d|w|y)&#x60; (milliseconds seconds minutes hours days weeks years). | [optional] 
**route_prefix** | **str** | The route prefix ThanosRuler registers HTTP handlers for. This allows thanos UI to be served on a sub-path. | [optional] 
**rule_namespace_selector** | [**ComCoreosMonitoringV1ThanosRulerSpecRuleNamespaceSelector**](ComCoreosMonitoringV1ThanosRulerSpecRuleNamespaceSelector.md) |  | [optional] 
**rule_selector** | [**ComCoreosMonitoringV1ThanosRulerSpecRuleSelector**](ComCoreosMonitoringV1ThanosRulerSpecRuleSelector.md) |  | [optional] 
**security_context** | [**ComCoreosMonitoringV1AlertmanagerSpecSecurityContext1**](ComCoreosMonitoringV1AlertmanagerSpecSecurityContext1.md) |  | [optional] 
**service_account_name** | **str** | ServiceAccountName is the name of the ServiceAccount to use to run the Thanos Ruler Pods. | [optional] 
**storage** | [**ComCoreosMonitoringV1PrometheusSpecStorage**](ComCoreosMonitoringV1PrometheusSpecStorage.md) |  | [optional] 
**tolerations** | [**list[ComCoreosMonitoringV1AlertmanagerSpecTolerations]**](ComCoreosMonitoringV1AlertmanagerSpecTolerations.md) | If specified, the pod&#39;s tolerations. | [optional] 
**topology_spread_constraints** | [**list[ComCoreosMonitoringV1AlertmanagerSpecTopologySpreadConstraints]**](ComCoreosMonitoringV1AlertmanagerSpecTopologySpreadConstraints.md) | If specified, the pod&#39;s topology spread constraints. | [optional] 
**tracing_config** | [**ComCoreosMonitoringV1PrometheusSpecThanosTracingConfig**](ComCoreosMonitoringV1PrometheusSpecThanosTracingConfig.md) |  | [optional] 
**volumes** | [**list[ComCoreosMonitoringV1AlertmanagerSpecVolumes]**](ComCoreosMonitoringV1AlertmanagerSpecVolumes.md) | Volumes allows configuration of additional volumes on the output StatefulSet definition. Volumes specified will be appended to other volumes that are generated as a result of StorageSpec objects. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


