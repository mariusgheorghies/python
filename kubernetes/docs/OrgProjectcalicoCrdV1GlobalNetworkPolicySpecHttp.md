# OrgProjectcalicoCrdV1GlobalNetworkPolicySpecHttp

HTTP contains match criteria that apply to HTTP requests.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**methods** | **list[str]** | Methods is an optional field that restricts the rule to apply only to HTTP requests that use one of the listed HTTP Methods (e.g. GET, PUT, etc.) Multiple methods are OR&#39;d together. | [optional] 
**paths** | [**list[OrgProjectcalicoCrdV1GlobalNetworkPolicySpecHttpPaths]**](OrgProjectcalicoCrdV1GlobalNetworkPolicySpecHttpPaths.md) | Paths is an optional field that restricts the rule to apply to HTTP requests that use one of the listed HTTP Paths. Multiple paths are OR&#39;d together. e.g: - exact: /foo - prefix: /bar NOTE: Each entry may ONLY specify either a &#x60;exact&#x60; or a &#x60;prefix&#x60; match. The validator will check for it. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


