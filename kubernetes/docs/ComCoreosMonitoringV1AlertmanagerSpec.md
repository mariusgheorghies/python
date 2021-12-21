# ComCoreosMonitoringV1AlertmanagerSpec

Specification of the desired behavior of the Alertmanager cluster. More info: https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#spec-and-status
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_peers** | **list[str]** | AdditionalPeers allows injecting a set of additional Alertmanagers to peer with to form a highly available cluster. | [optional] 
**affinity** | [**ComCoreosMonitoringV1AlertmanagerSpecAffinity**](ComCoreosMonitoringV1AlertmanagerSpecAffinity.md) |  | [optional] 
**alertmanager_config_namespace_selector** | [**ComCoreosMonitoringV1AlertmanagerSpecAlertmanagerConfigNamespaceSelector**](ComCoreosMonitoringV1AlertmanagerSpecAlertmanagerConfigNamespaceSelector.md) |  | [optional] 
**alertmanager_config_selector** | [**ComCoreosMonitoringV1AlertmanagerSpecAlertmanagerConfigSelector**](ComCoreosMonitoringV1AlertmanagerSpecAlertmanagerConfigSelector.md) |  | [optional] 
**base_image** | **str** | Base image that is used to deploy pods, without tag. Deprecated: use &#39;image&#39; instead | [optional] 
**cluster_advertise_address** | **str** | ClusterAdvertiseAddress is the explicit address to advertise in cluster. Needs to be provided for non RFC1918 [1] (public) addresses. [1] RFC1918: https://tools.ietf.org/html/rfc1918 | [optional] 
**cluster_gossip_interval** | **str** | Interval between gossip attempts. | [optional] 
**cluster_peer_timeout** | **str** | Timeout for cluster peering. | [optional] 
**cluster_pushpull_interval** | **str** | Interval between pushpull attempts. | [optional] 
**config_maps** | **list[str]** | ConfigMaps is a list of ConfigMaps in the same namespace as the Alertmanager object, which shall be mounted into the Alertmanager Pods. The ConfigMaps are mounted into /etc/alertmanager/configmaps/&lt;configmap-name&gt;. | [optional] 
**config_secret** | **str** | ConfigSecret is the name of a Kubernetes Secret in the same namespace as the Alertmanager object, which contains configuration for this Alertmanager instance. Defaults to &#39;alertmanager-&lt;alertmanager-name&gt;&#39; The secret is mounted into /etc/alertmanager/config. | [optional] 
**containers** | [**list[ComCoreosMonitoringV1AlertmanagerSpecContainers]**](ComCoreosMonitoringV1AlertmanagerSpecContainers.md) | Containers allows injecting additional containers. This is meant to allow adding an authentication proxy to an Alertmanager pod. Containers described here modify an operator generated container if they share the same name and modifications are done via a strategic merge patch. The current container names are: &#x60;alertmanager&#x60; and &#x60;config-reloader&#x60;. Overriding containers is entirely outside the scope of what the maintainers will support and by doing so, you accept that this behaviour may break at any time without notice. | [optional] 
**external_url** | **str** | The external URL the Alertmanager instances will be available under. This is necessary to generate correct URLs. This is necessary if Alertmanager is not served from root of a DNS name. | [optional] 
**force_enable_cluster_mode** | **bool** | ForceEnableClusterMode ensures Alertmanager does not deactivate the cluster mode when running with a single replica. Use case is e.g. spanning an Alertmanager cluster across Kubernetes clusters with a single replica in each. | [optional] 
**image** | **str** | Image if specified has precedence over baseImage, tag and sha combinations. Specifying the version is still necessary to ensure the Prometheus Operator knows what version of Alertmanager is being configured. | [optional] 
**image_pull_secrets** | [**list[ComCoreosMonitoringV1AlertmanagerSpecImagePullSecrets]**](ComCoreosMonitoringV1AlertmanagerSpecImagePullSecrets.md) | An optional list of references to secrets in the same namespace to use for pulling prometheus and alertmanager images from registries see http://kubernetes.io/docs/user-guide/images#specifying-imagepullsecrets-on-a-pod | [optional] 
**init_containers** | [**list[ComCoreosMonitoringV1AlertmanagerSpecContainers]**](ComCoreosMonitoringV1AlertmanagerSpecContainers.md) | InitContainers allows adding initContainers to the pod definition. Those can be used to e.g. fetch secrets for injection into the Alertmanager configuration from external sources. Any errors during the execution of an initContainer will lead to a restart of the Pod. More info: https://kubernetes.io/docs/concepts/workloads/pods/init-containers/ Using initContainers for any use case other then secret fetching is entirely outside the scope of what the maintainers will support and by doing so, you accept that this behaviour may break at any time without notice. | [optional] 
**listen_local** | **bool** | ListenLocal makes the Alertmanager server listen on loopback, so that it does not bind against the Pod IP. Note this is only for the Alertmanager UI, not the gossip communication. | [optional] 
**log_format** | **str** | Log format for Alertmanager to be configured with. | [optional] 
**log_level** | **str** | Log level for Alertmanager to be configured with. | [optional] 
**node_selector** | **dict(str, str)** | Define which Nodes the Pods are scheduled on. | [optional] 
**paused** | **bool** | If set to true all actions on the underlying managed objects are not goint to be performed, except for delete actions. | [optional] 
**pod_metadata** | [**ComCoreosMonitoringV1AlertmanagerSpecPodMetadata**](ComCoreosMonitoringV1AlertmanagerSpecPodMetadata.md) |  | [optional] 
**port_name** | **str** | Port name used for the pods and governing service. This defaults to web | [optional] 
**priority_class_name** | **str** | Priority class assigned to the Pods | [optional] 
**replicas** | **int** | Size is the expected size of the alertmanager cluster. The controller will eventually make the size of the running cluster equal to the expected size. | [optional] 
**resources** | [**ComCoreosMonitoringV1AlertmanagerSpecResources1**](ComCoreosMonitoringV1AlertmanagerSpecResources1.md) |  | [optional] 
**retention** | **str** | Time duration Alertmanager shall retain data for. Default is &#39;120h&#39;, and must match the regular expression &#x60;[0-9]+(ms|s|m|h)&#x60; (milliseconds seconds minutes hours). | [optional] 
**route_prefix** | **str** | The route prefix Alertmanager registers HTTP handlers for. This is useful, if using ExternalURL and a proxy is rewriting HTTP routes of a request, and the actual ExternalURL is still true, but the server serves requests under a different route prefix. For example for use with &#x60;kubectl proxy&#x60;. | [optional] 
**secrets** | **list[str]** | Secrets is a list of Secrets in the same namespace as the Alertmanager object, which shall be mounted into the Alertmanager Pods. The Secrets are mounted into /etc/alertmanager/secrets/&lt;secret-name&gt;. | [optional] 
**security_context** | [**ComCoreosMonitoringV1AlertmanagerSpecSecurityContext1**](ComCoreosMonitoringV1AlertmanagerSpecSecurityContext1.md) |  | [optional] 
**service_account_name** | **str** | ServiceAccountName is the name of the ServiceAccount to use to run the Prometheus Pods. | [optional] 
**sha** | **str** | SHA of Alertmanager container image to be deployed. Defaults to the value of &#x60;version&#x60;. Similar to a tag, but the SHA explicitly deploys an immutable container image. Version and Tag are ignored if SHA is set. Deprecated: use &#39;image&#39; instead.  The image digest can be specified as part of the image URL. | [optional] 
**storage** | [**ComCoreosMonitoringV1AlertmanagerSpecStorage**](ComCoreosMonitoringV1AlertmanagerSpecStorage.md) |  | [optional] 
**tag** | **str** | Tag of Alertmanager container image to be deployed. Defaults to the value of &#x60;version&#x60;. Version is ignored if Tag is set. Deprecated: use &#39;image&#39; instead.  The image tag can be specified as part of the image URL. | [optional] 
**tolerations** | [**list[ComCoreosMonitoringV1AlertmanagerSpecTolerations]**](ComCoreosMonitoringV1AlertmanagerSpecTolerations.md) | If specified, the pod&#39;s tolerations. | [optional] 
**topology_spread_constraints** | [**list[ComCoreosMonitoringV1AlertmanagerSpecTopologySpreadConstraints]**](ComCoreosMonitoringV1AlertmanagerSpecTopologySpreadConstraints.md) | If specified, the pod&#39;s topology spread constraints. | [optional] 
**version** | **str** | Version the cluster should be on. | [optional] 
**volume_mounts** | [**list[ComCoreosMonitoringV1AlertmanagerSpecVolumeMounts]**](ComCoreosMonitoringV1AlertmanagerSpecVolumeMounts.md) | VolumeMounts allows configuration of additional VolumeMounts on the output StatefulSet definition. VolumeMounts specified will be appended to other VolumeMounts in the alertmanager container, that are generated as a result of StorageSpec objects. | [optional] 
**volumes** | [**list[ComCoreosMonitoringV1AlertmanagerSpecVolumes]**](ComCoreosMonitoringV1AlertmanagerSpecVolumes.md) | Volumes allows configuration of additional volumes on the output StatefulSet definition. Volumes specified will be appended to other volumes that are generated as a result of StorageSpec objects. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


