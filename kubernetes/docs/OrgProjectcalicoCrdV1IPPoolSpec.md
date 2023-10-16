# OrgProjectcalicoCrdV1IPPoolSpec

IPPoolSpec contains the specification for an IPPool resource.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block_size** | **int** | The block size to use for IP address assignments from this pool. Defaults to 26 for IPv4 and 112 for IPv6. | [optional] 
**cidr** | **str** | The pool CIDR. | 
**disabled** | **bool** | When disabled is true, Calico IPAM will not assign addresses from this pool. | [optional] 
**ipip** | [**OrgProjectcalicoCrdV1IPPoolSpecIpip**](OrgProjectcalicoCrdV1IPPoolSpecIpip.md) |  | [optional] 
**ipip_mode** | **str** | Contains configuration for IPIP tunneling for this pool. If not specified, then this is defaulted to \&quot;Never\&quot; (i.e. IPIP tunneling is disabled). | [optional] 
**nat_outgoing** | **bool** | Deprecated: this field is only used for APIv1 backwards compatibility. Setting this field is not allowed, this field is for internal use only. | [optional] 
**nat_outgoing** | **bool** | When nat-outgoing is true, packets sent from Calico networked containers in this pool to destinations outside of this pool will be masqueraded. | [optional] 
**node_selector** | **str** | Allows IPPool to allocate for a specific node by label selector. | [optional] 
**vxlan_mode** | **str** | Contains configuration for VXLAN tunneling for this pool. If not specified, then this is defaulted to \&quot;Never\&quot; (i.e. VXLAN tunneling is disabled). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


