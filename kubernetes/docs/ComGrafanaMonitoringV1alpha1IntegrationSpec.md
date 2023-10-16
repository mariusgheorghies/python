# ComGrafanaMonitoringV1alpha1IntegrationSpec

Specifies the desired behavior of the Integration.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | [**object**](.md) | The configuration for the named integration. Note that Integrations are deployed with the integrations-next feature flag, which has different common settings:   https://grafana.com/docs/agent/latest/configuration/integrations/integrations-next/ | 
**config_maps** | [**list[ComGrafanaMonitoringV1alpha1IntegrationSpecConfigMaps]**](ComGrafanaMonitoringV1alpha1IntegrationSpecConfigMaps.md) | An extra list of keys from ConfigMaps in the same namespace as the Integration which will be mounted into the Grafana Agent pod running this Integration.   ConfigMaps are mounted at /etc/grafana-agent/integrations/configMaps/&lt;configmap_namespace&gt;/&lt;configmap_name&gt;/&lt;key&gt;. | [optional] 
**name** | **str** | Name of the integration to run (e.g., \&quot;node_exporter\&quot;, \&quot;mysqld_exporter\&quot;). | 
**secrets** | [**list[ComGrafanaMonitoringV1alpha1IntegrationSpecSecrets]**](ComGrafanaMonitoringV1alpha1IntegrationSpecSecrets.md) | An extra list of keys from Secrets in the same namespace as the Integration which will be mounted into the Grafana Agent pod running this Integration.   Secrets will be mounted at /etc/grafana-agent/integrations/secrets/&lt;secret_namespace&gt;/&lt;secret_name&gt;/&lt;key&gt;. | [optional] 
**type** | [**ComGrafanaMonitoringV1alpha1IntegrationSpecType**](ComGrafanaMonitoringV1alpha1IntegrationSpecType.md) |  | 
**volume_mounts** | [**list[ComCoreosMonitoringV1AlertmanagerSpecVolumeMounts]**](ComCoreosMonitoringV1AlertmanagerSpecVolumeMounts.md) | An extra list of VolumeMounts to be associated with the Grafana Agent pods running this integration. VolumeMount names are mutated to be unique across all used IntegrationSpecs.   Mount paths should include the namespace/name of the Integration CR to avoid potentially colliding with other resources. | [optional] 
**volumes** | [**list[ComGrafanaMonitoringV1alpha1GrafanaAgentSpecVolumes]**](ComGrafanaMonitoringV1alpha1GrafanaAgentSpecVolumes.md) | An extra list of Volumes to be associated with the Grafana Agent pods running this integration. Volume names are mutated to be unique across all Integrations. Note that the specified volumes should be able to tolerate existing on multiple pods at once when type is daemonset.   Don&#39;t use volumes for loading Secrets or ConfigMaps from the same namespace as the Integration; use the Secrets and ConfigMaps fields instead. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


