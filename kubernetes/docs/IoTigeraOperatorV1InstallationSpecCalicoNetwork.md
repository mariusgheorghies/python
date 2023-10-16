# IoTigeraOperatorV1InstallationSpecCalicoNetwork

CalicoNetwork specifies networking configuration options for Calico.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bgp** | **str** | BGP configures whether or not to enable Calico&#39;s BGP capabilities. | [optional] 
**container_ip_forwarding** | **str** | ContainerIPForwarding configures whether ip forwarding will be enabled for containers in the CNI configuration. Default: Disabled | [optional] 
**host_ports** | **str** | HostPorts configures whether or not Calico will support Kubernetes HostPorts. Valid only when using the Calico CNI plugin. Default: Enabled | [optional] 
**ip_pools** | [**list[IoTigeraOperatorV1InstallationSpecCalicoNetworkIpPools]**](IoTigeraOperatorV1InstallationSpecCalicoNetworkIpPools.md) | IPPools contains a list of IP pools to create if none exist. At most one IP pool of each address family may be specified. If omitted, a single pool will be configured if needed. | [optional] 
**linux_dataplane** | **str** | LinuxDataplane is used to select the dataplane used for Linux nodes. In particular, it causes the operator to add required mounts and environment variables for the particular dataplane. If not specified, iptables mode is used. Default: Iptables | [optional] 
**mtu** | **int** | MTU specifies the maximum transmission unit to use on the pod network. If not specified, Calico will perform MTU auto-detection based on the cluster network. | [optional] 
**multi_interface_mode** | **str** | MultiInterfaceMode configures what will configure multiple interface per pod. Only valid for Calico Enterprise installations using the Calico CNI plugin. Default: None | [optional] 
**node_address_autodetection_v4** | [**IoTigeraOperatorV1InstallationSpecCalicoNetworkNodeAddressAutodetectionV4**](IoTigeraOperatorV1InstallationSpecCalicoNetworkNodeAddressAutodetectionV4.md) |  | [optional] 
**node_address_autodetection_v6** | [**IoTigeraOperatorV1InstallationSpecCalicoNetworkNodeAddressAutodetectionV6**](IoTigeraOperatorV1InstallationSpecCalicoNetworkNodeAddressAutodetectionV6.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


