# ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecRoute

The Alertmanager route definition for alerts matching the resource’s namespace. If present, it will be added to the generated Alertmanager configuration as a first-level route.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_continue** | **bool** | Boolean indicating whether an alert should continue matching subsequent sibling nodes. It will always be overridden to true for the first-level route by the Prometheus operator. | [optional] 
**group_by** | **list[str]** | List of labels to group by. Labels must not be repeated (unique list). Special label \&quot;...\&quot; (aggregate by all possible labels), if provided, must be the only element in the list. | [optional] 
**group_interval** | **str** | How long to wait before sending an updated notification. Must match the regular expression&#x60;^(([0-9]+)y)?(([0-9]+)w)?(([0-9]+)d)?(([0-9]+)h)?(([0-9]+)m)?(([0-9]+)s)?(([0-9]+)ms)?$&#x60; Example: \&quot;5m\&quot; | [optional] 
**group_wait** | **str** | How long to wait before sending the initial notification. Must match the regular expression&#x60;^(([0-9]+)y)?(([0-9]+)w)?(([0-9]+)d)?(([0-9]+)h)?(([0-9]+)m)?(([0-9]+)s)?(([0-9]+)ms)?$&#x60; Example: \&quot;30s\&quot; | [optional] 
**matchers** | [**list[ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecSourceMatch]**](ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecSourceMatch.md) | List of matchers that the alert’s labels should match. For the first level route, the operator removes any existing equality and regexp matcher on the &#x60;namespace&#x60; label and adds a &#x60;namespace: &lt;object namespace&gt;&#x60; matcher. | [optional] 
**mute_time_intervals** | **list[str]** | Note: this comment applies to the field definition above but appears below otherwise it gets included in the generated manifest. CRD schema doesn&#39;t support self-referential types for now (see https://github.com/kubernetes/kubernetes/issues/62872). We have to use an alternative type to circumvent the limitation. The downside is that the Kube API can&#39;t validate the data beyond the fact that it is a valid JSON representation. MuteTimeIntervals is a list of MuteTimeInterval names that will mute this route when matched, | [optional] 
**receiver** | **str** | Name of the receiver for this route. If not empty, it should be listed in the &#x60;receivers&#x60; field. | [optional] 
**repeat_interval** | **str** | How long to wait before repeating the last notification. Must match the regular expression&#x60;^(([0-9]+)y)?(([0-9]+)w)?(([0-9]+)d)?(([0-9]+)h)?(([0-9]+)m)?(([0-9]+)s)?(([0-9]+)ms)?$&#x60; Example: \&quot;4h\&quot; | [optional] 
**routes** | **list[object]** | Child routes. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


