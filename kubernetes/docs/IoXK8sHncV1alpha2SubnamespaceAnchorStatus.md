# IoXK8sHncV1alpha2SubnamespaceAnchorStatus

SubnamespaceAnchorStatus defines the observed state of SubnamespaceAnchor.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Describes the state of the subnamespace anchor.   Currently, the supported values are:   - \&quot;Missing\&quot;: the subnamespace has not been created yet. This should be the default state when the anchor is just created.   - \&quot;Ok\&quot;: the subnamespace exists. This is the only good state of the anchor.   - \&quot;Conflict\&quot;: a namespace of the same name already exists. The admission controller will attempt to prevent this.   - \&quot;Forbidden\&quot;: the anchor was created in a namespace that doesn&#39;t allow children, such as kube-system or hnc-system. The admission controller will attempt to prevent this. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


