# OrgProjectcalicoCrdV1BGPPeerSpec

BGPPeerSpec contains the specification for a BGPPeer resource.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**as_number** | **int** | The AS Number of the peer. | [optional] 
**keep_original_next_hop** | **bool** | Option to keep the original nexthop field when routes are sent to a BGP Peer. Setting \&quot;true\&quot; configures the selected BGP Peers node to use the \&quot;next hop keep;\&quot; instead of \&quot;next hop self;\&quot;(default) in the specific branch of the Node on \&quot;bird.cfg\&quot;. | [optional] 
**node** | **str** | The node name identifying the Calico node instance that is targeted by this peer. If this is not set, and no nodeSelector is specified, then this BGP peer selects all nodes in the cluster. | [optional] 
**node_selector** | **str** | Selector for the nodes that should have this peering.  When this is set, the Node field must be empty. | [optional] 
**password** | [**OrgProjectcalicoCrdV1BGPPeerSpecPassword**](OrgProjectcalicoCrdV1BGPPeerSpecPassword.md) |  | [optional] 
**peer_ip** | **str** | The IP address of the peer followed by an optional port number to peer with. If port number is given, format should be &#x60;[&lt;IPv6&gt;]:port&#x60; or &#x60;&lt;IPv4&gt;:&lt;port&gt;&#x60; for IPv4. If optional port number is not set, and this peer IP and ASNumber belongs to a calico/node with ListenPort set in BGPConfiguration, then we use that port to peer. | [optional] 
**peer_selector** | **str** | Selector for the remote nodes to peer with.  When this is set, the PeerIP and ASNumber fields must be empty.  For each peering between the local node and selected remote nodes, we configure an IPv4 peering if both ends have NodeBGPSpec.IPv4Address specified, and an IPv6 peering if both ends have NodeBGPSpec.IPv6Address specified.  The remote AS number comes from the remote node&#39;s NodeBGPSpec.ASNumber, or the global default if that is not set. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


