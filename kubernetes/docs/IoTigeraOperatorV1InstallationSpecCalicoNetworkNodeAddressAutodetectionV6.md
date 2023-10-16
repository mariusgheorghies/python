# IoTigeraOperatorV1InstallationSpecCalicoNetworkNodeAddressAutodetectionV6

NodeAddressAutodetectionV6 specifies an approach to automatically detect node IPv6 addresses. If not specified, IPv6 addresses will not be auto-detected.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_reach** | **str** | CanReach enables IP auto-detection based on which source address on the node is used to reach the specified IP or domain. | [optional] 
**cidrs** | **list[str]** | CIDRS enables IP auto-detection based on which addresses on the nodes are within one of the provided CIDRs. | [optional] 
**first_found** | **bool** | FirstFound uses default interface matching parameters to select an interface, performing best-effort filtering based on well-known interface names. | [optional] 
**interface** | **str** | Interface enables IP auto-detection based on interfaces that match the given regex. | [optional] 
**skip_interface** | **str** | SkipInterface enables IP auto-detection based on interfaces that do not match the given regex. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


