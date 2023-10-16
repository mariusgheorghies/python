# OrgProjectcalicoCrdV1GlobalNetworkPolicySpecEgress

A Rule encapsulates a set of match criteria and an action.  Both selector-based security Policy and security Profiles reference rules - separated out as a list of rules for both ingress and egress packet matching.   Each positive match criteria has a negated version, prefixed with ”Not”. All the match criteria within a rule must be satisfied for a packet to match. A single rule can contain the positive and negative version of a match and both must be satisfied for the rule to match.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**destination** | [**OrgProjectcalicoCrdV1GlobalNetworkPolicySpecDestination**](OrgProjectcalicoCrdV1GlobalNetworkPolicySpecDestination.md) |  | [optional] 
**http** | [**OrgProjectcalicoCrdV1GlobalNetworkPolicySpecHttp**](OrgProjectcalicoCrdV1GlobalNetworkPolicySpecHttp.md) |  | [optional] 
**icmp** | [**OrgProjectcalicoCrdV1GlobalNetworkPolicySpecIcmp**](OrgProjectcalicoCrdV1GlobalNetworkPolicySpecIcmp.md) |  | [optional] 
**ip_version** | **int** | IPVersion is an optional field that restricts the rule to only match a specific IP version. | [optional] 
**metadata** | [**OrgProjectcalicoCrdV1GlobalNetworkPolicySpecMetadata**](OrgProjectcalicoCrdV1GlobalNetworkPolicySpecMetadata.md) |  | [optional] 
**not_icmp** | [**OrgProjectcalicoCrdV1GlobalNetworkPolicySpecNotICMP**](OrgProjectcalicoCrdV1GlobalNetworkPolicySpecNotICMP.md) |  | [optional] 
**not_protocol** | [**object**](.md) | NotProtocol is the negated version of the Protocol field. | [optional] 
**protocol** | [**object**](.md) | Protocol is an optional field that restricts the rule to only apply to traffic of a specific IP protocol. Required if any of the EntityRules contain Ports (because ports only apply to certain protocols).   Must be one of these string values: \&quot;TCP\&quot;, \&quot;UDP\&quot;, \&quot;ICMP\&quot;, \&quot;ICMPv6\&quot;, \&quot;SCTP\&quot;, \&quot;UDPLite\&quot; or an integer in the range 1-255. | [optional] 
**source** | [**OrgProjectcalicoCrdV1GlobalNetworkPolicySpecSource**](OrgProjectcalicoCrdV1GlobalNetworkPolicySpecSource.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


