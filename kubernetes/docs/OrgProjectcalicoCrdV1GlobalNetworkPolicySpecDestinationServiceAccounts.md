# OrgProjectcalicoCrdV1GlobalNetworkPolicySpecDestinationServiceAccounts

ServiceAccounts is an optional field that restricts the rule to only apply to traffic that originates from (or terminates at) a pod running as a matching service account.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**names** | **list[str]** | Names is an optional field that restricts the rule to only apply to traffic that originates from (or terminates at) a pod running as a service account whose name is in the list. | [optional] 
**selector** | **str** | Selector is an optional field that restricts the rule to only apply to traffic that originates from (or terminates at) a pod running as a service account that matches the given label selector. If both Names and Selector are specified then they are AND&#39;ed. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


