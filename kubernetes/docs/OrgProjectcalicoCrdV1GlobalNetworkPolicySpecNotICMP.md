# OrgProjectcalicoCrdV1GlobalNetworkPolicySpecNotICMP

NotICMP is the negated version of the ICMP field.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | Match on a specific ICMP code.  If specified, the Type value must also be specified. This is a technical limitation imposed by the kernel&#39;s iptables firewall, which Calico uses to enforce the rule. | [optional] 
**type** | **int** | Match on a specific ICMP type.  For example a value of 8 refers to ICMP Echo Request (i.e. pings). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


