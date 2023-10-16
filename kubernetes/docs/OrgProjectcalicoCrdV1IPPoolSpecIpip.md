# OrgProjectcalicoCrdV1IPPoolSpecIpip

Deprecated: this field is only used for APIv1 backwards compatibility. Setting this field is not allowed, this field is for internal use only.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | When enabled is true, ipip tunneling will be used to deliver packets to destinations within this pool. | [optional] 
**mode** | **str** | The IPIP mode.  This can be one of \&quot;always\&quot; or \&quot;cross-subnet\&quot;.  A mode of \&quot;always\&quot; will also use IPIP tunneling for routing to destination IP addresses within this pool.  A mode of \&quot;cross-subnet\&quot; will only use IPIP tunneling when the destination node is on a different subnet to the originating node.  The default value (if not specified) is \&quot;always\&quot;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


