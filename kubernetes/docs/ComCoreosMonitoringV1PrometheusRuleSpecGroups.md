# ComCoreosMonitoringV1PrometheusRuleSpecGroups

RuleGroup is a list of sequentially evaluated recording and alerting rules. Note: PartialResponseStrategy is only used by ThanosRuler and will be ignored by Prometheus instances.  Valid values for this field are 'warn' or 'abort'.  More info: https://github.com/thanos-io/thanos/blob/main/docs/components/rule.md#partial-response
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interval** | **str** |  | [optional] 
**name** | **str** |  | 
**partial_response_strategy** | **str** |  | [optional] 
**rules** | [**list[ComCoreosMonitoringV1PrometheusRuleSpecRules]**](ComCoreosMonitoringV1PrometheusRuleSpecRules.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


