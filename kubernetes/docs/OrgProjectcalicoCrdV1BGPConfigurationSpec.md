# OrgProjectcalicoCrdV1BGPConfigurationSpec

BGPConfigurationSpec contains the values of the BGP configuration.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**as_number** | **int** | ASNumber is the default AS number used by a node. [Default: 64512] | [optional] 
**communities** | [**list[OrgProjectcalicoCrdV1BGPConfigurationSpecCommunities]**](OrgProjectcalicoCrdV1BGPConfigurationSpecCommunities.md) | Communities is a list of BGP community values and their arbitrary names for tagging routes. | [optional] 
**listen_port** | **int** | ListenPort is the port where BGP protocol should listen. Defaults to 179 | [optional] 
**log_severity_screen** | **str** | LogSeverityScreen is the log severity above which logs are sent to the stdout. [Default: INFO] | [optional] 
**node_to_node_mesh_enabled** | **bool** | NodeToNodeMeshEnabled sets whether full node to node BGP mesh is enabled. [Default: true] | [optional] 
**prefix_advertisements** | [**list[OrgProjectcalicoCrdV1BGPConfigurationSpecPrefixAdvertisements]**](OrgProjectcalicoCrdV1BGPConfigurationSpecPrefixAdvertisements.md) | PrefixAdvertisements contains per-prefix advertisement configuration. | [optional] 
**service_cluster_i_ps** | [**list[OrgProjectcalicoCrdV1BGPConfigurationSpecServiceClusterIPs]**](OrgProjectcalicoCrdV1BGPConfigurationSpecServiceClusterIPs.md) | ServiceClusterIPs are the CIDR blocks from which service cluster IPs are allocated. If specified, Calico will advertise these blocks, as well as any cluster IPs within them. | [optional] 
**service_external_i_ps** | [**list[OrgProjectcalicoCrdV1BGPConfigurationSpecServiceExternalIPs]**](OrgProjectcalicoCrdV1BGPConfigurationSpecServiceExternalIPs.md) | ServiceExternalIPs are the CIDR blocks for Kubernetes Service External IPs. Kubernetes Service ExternalIPs will only be advertised if they are within one of these blocks. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


