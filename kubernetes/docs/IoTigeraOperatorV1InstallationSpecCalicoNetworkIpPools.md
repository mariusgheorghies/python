# IoTigeraOperatorV1InstallationSpecCalicoNetworkIpPools

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block_size** | **int** | BlockSize specifies the CIDR prefex length to use when allocating per-node IP blocks from the main IP pool CIDR. Default: 26 (IPv4), 122 (IPv6) | [optional] 
**cidr** | **str** | CIDR contains the address range for the IP Pool in classless inter-domain routing format. | 
**encapsulation** | **str** | Encapsulation specifies the encapsulation type that will be used with the IP Pool. Default: IPIP | [optional] 
**nat_outgoing** | **str** | NATOutgoing specifies if NAT will be enabled or disabled for outgoing traffic. Default: Enabled | [optional] 
**node_selector** | **str** | NodeSelector specifies the node selector that will be set for the IP Pool. Default: &#39;all()&#39; | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


