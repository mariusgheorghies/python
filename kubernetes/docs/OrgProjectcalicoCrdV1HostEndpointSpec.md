# OrgProjectcalicoCrdV1HostEndpointSpec

HostEndpointSpec contains the specification for a HostEndpoint resource.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expected_i_ps** | **list[str]** | The expected IP addresses (IPv4 and IPv6) of the endpoint. If \&quot;InterfaceName\&quot; is not present, Calico will look for an interface matching any of the IPs in the list and apply policy to that. Note:  When using the selector match criteria in an ingress or egress security Policy  or Profile, Calico converts the selector into a set of IP addresses. For host  endpoints, the ExpectedIPs field is used for that purpose. (If only the interface  name is specified, Calico does not learn the IPs of the interface for use in match  criteria.) | [optional] 
**interface_name** | **str** | Either \&quot;*\&quot;, or the name of a specific Linux interface to apply policy to; or empty.  \&quot;*\&quot; indicates that this HostEndpoint governs all traffic to, from or through the default network namespace of the host named by the \&quot;Node\&quot; field; entering and leaving that namespace via any interface, including those from/to non-host-networked local workloads.   If InterfaceName is not \&quot;*\&quot;, this HostEndpoint only governs traffic that enters or leaves the host through the specific interface named by InterfaceName, or - when InterfaceName is empty - through the specific interface that has one of the IPs in ExpectedIPs. Therefore, when InterfaceName is empty, at least one expected IP must be specified.  Only external interfaces (such as “eth0”) are supported here; it isn&#39;t possible for a HostEndpoint to protect traffic through a specific local workload interface.   Note: Only some kinds of policy are implemented for \&quot;*\&quot; HostEndpoints; initially just pre-DNAT policy.  Please check Calico documentation for the latest position. | [optional] 
**node** | **str** | The node name identifying the Calico node instance. | [optional] 
**ports** | [**list[OrgProjectcalicoCrdV1HostEndpointSpecPorts]**](OrgProjectcalicoCrdV1HostEndpointSpecPorts.md) | Ports contains the endpoint&#39;s named ports, which may be referenced in security policy rules. | [optional] 
**profiles** | **list[str]** | A list of identifiers of security Profile objects that apply to this endpoint. Each profile is applied in the order that they appear in this list.  Profile rules are applied after the selector-based security policy. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


