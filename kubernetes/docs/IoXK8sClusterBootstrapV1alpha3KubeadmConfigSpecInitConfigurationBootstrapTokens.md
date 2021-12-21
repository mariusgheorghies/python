# IoXK8sClusterBootstrapV1alpha3KubeadmConfigSpecInitConfigurationBootstrapTokens

BootstrapToken describes one bootstrap token, stored as a Secret in the cluster.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description sets a human-friendly message why this token exists and what it&#39;s used for, so other administrators can know its purpose. | [optional] 
**expires** | **datetime** | Expires specifies the timestamp when this token expires. Defaults to being set dynamically at runtime based on the TTL. Expires and TTL are mutually exclusive. | [optional] 
**groups** | **list[str]** | Groups specifies the extra groups that this token will authenticate as when/if used for authentication | [optional] 
**token** | **str** | Token is used for establishing bidirectional trust between nodes and control-planes. Used for joining nodes in the cluster. | 
**ttl** | **str** | TTL defines the time to live for this token. Defaults to 24h. Expires and TTL are mutually exclusive. | [optional] 
**usages** | **list[str]** | Usages describes the ways in which this token can be used. Can by default be used for establishing bidirectional trust, but that can be changed here. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


