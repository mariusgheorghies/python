# ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecRoute

The Alertmanager route definition for alerts matching the resource’s namespace. If present, it will be added to the generated Alertmanager configuration as a first-level route.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_continue** | **bool** | Boolean indicating whether an alert should continue matching subsequent sibling nodes. It will always be overridden to true for the first-level route by the Prometheus operator. | [optional] 
**group_by** | **list[str]** | List of labels to group by. | [optional] 
**group_interval** | **str** | How long to wait before sending an updated notification. Must match the regular expression &#x60;[0-9]+(ms|s|m|h)&#x60; (milliseconds seconds minutes hours). | [optional] 
**group_wait** | **str** | How long to wait before sending the initial notification. Must match the regular expression &#x60;[0-9]+(ms|s|m|h)&#x60; (milliseconds seconds minutes hours). | [optional] 
**matchers** | [**list[ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecSourceMatch]**](ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecSourceMatch.md) | List of matchers that the alert’s labels should match. For the first level route, the operator removes any existing equality and regexp matcher on the &#x60;namespace&#x60; label and adds a &#x60;namespace: &lt;object namespace&gt;&#x60; matcher. | [optional] 
**receiver** | **str** | Name of the receiver for this route. If not empty, it should be listed in the &#x60;receivers&#x60; field. | [optional] 
**repeat_interval** | **str** | How long to wait before repeating the last notification. Must match the regular expression &#x60;[0-9]+(ms|s|m|h)&#x60; (milliseconds seconds minutes hours). | [optional] 
**routes** | **list[object]** | Child routes. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


