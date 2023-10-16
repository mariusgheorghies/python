# OrgProjectcalicoCrdV1GlobalNetworkPolicySpecDestination

Destination contains the match criteria that apply to destination entity.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**namespace_selector** | **str** | NamespaceSelector is an optional field that contains a selector expression. Only traffic that originates from (or terminates at) endpoints within the selected namespaces will be matched. When both NamespaceSelector and Selector are defined on the same rule, then only workload endpoints that are matched by both selectors will be selected by the rule.   For NetworkPolicy, an empty NamespaceSelector implies that the Selector is limited to selecting only workload endpoints in the same namespace as the NetworkPolicy.   For NetworkPolicy, &#x60;global()&#x60; NamespaceSelector implies that the Selector is limited to selecting only GlobalNetworkSet or HostEndpoint.   For GlobalNetworkPolicy, an empty NamespaceSelector implies the Selector applies to workload endpoints across all namespaces. | [optional] 
**nets** | **list[str]** | Nets is an optional field that restricts the rule to only apply to traffic that originates from (or terminates at) IP addresses in any of the given subnets. | [optional] 
**not_nets** | **list[str]** | NotNets is the negated version of the Nets field. | [optional] 
**not_ports** | **list[object]** | NotPorts is the negated version of the Ports field. Since only some protocols have ports, if any ports are specified it requires the Protocol match in the Rule to be set to \&quot;TCP\&quot; or \&quot;UDP\&quot;. | [optional] 
**not_selector** | **str** | NotSelector is the negated version of the Selector field.  See Selector field for subtleties with negated selectors. | [optional] 
**ports** | **list[object]** | Ports is an optional field that restricts the rule to only apply to traffic that has a source (destination) port that matches one of these ranges/values. This value is a list of integers or strings that represent ranges of ports.   Since only some protocols have ports, if any ports are specified it requires the Protocol match in the Rule to be set to \&quot;TCP\&quot; or \&quot;UDP\&quot;. | [optional] 
**selector** | **str** | Selector is an optional field that contains a selector expression (see Policy for sample syntax).  Only traffic that originates from (terminates at) endpoints matching the selector will be matched.   Note that: in addition to the negated version of the Selector (see NotSelector below), the selector expression syntax itself supports negation.  The two types of negation are subtly different. One negates the set of matched endpoints, the other negates the whole match:    Selector &#x3D; \&quot;!has(my_label)\&quot; matches packets that are from other Calico-controlled  endpoints that do not have the label “my_label”.    NotSelector &#x3D; \&quot;has(my_label)\&quot; matches packets that are not from Calico-controlled  endpoints that do have the label “my_label”.   The effect is that the latter will accept packets from non-Calico sources whereas the former is limited to packets from Calico-controlled endpoints. | [optional] 
**service_accounts** | [**OrgProjectcalicoCrdV1GlobalNetworkPolicySpecDestinationServiceAccounts**](OrgProjectcalicoCrdV1GlobalNetworkPolicySpecDestinationServiceAccounts.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


