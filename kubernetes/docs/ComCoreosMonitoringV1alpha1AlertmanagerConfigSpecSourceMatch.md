# ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecSourceMatch

Matcher defines how to match on alert's labels.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**match_type** | **str** | Match operation available with AlertManager &gt;&#x3D; v0.22.0 and takes precedence over Regex (deprecated) if non-empty. | [optional] 
**name** | **str** | Label to match. | 
**regex** | **bool** | Whether to match on equality (false) or regular-expression (true). Deprecated as of AlertManager &gt;&#x3D; v0.22.0 where a user should use MatchType instead. | [optional] 
**value** | **str** | Label value to match. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


