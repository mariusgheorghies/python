# IoCertManagerAcmeV1ChallengeSpecSolverDns01Webhook

Configure an external webhook based DNS01 challenge solver to manage DNS01 challenge records.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | [**object**](.md) | Additional configuration that should be passed to the webhook apiserver when challenges are processed. This can contain arbitrary JSON data. Secret values should not be specified in this stanza. If secret values are needed (e.g. credentials for a DNS service), you should use a SecretKeySelector to reference a Secret resource. For details on the schema of this field, consult the webhook provider implementation&#39;s documentation. | [optional] 
**group_name** | **str** | The API group name that should be used when POSTing ChallengePayload resources to the webhook apiserver. This should be the same as the GroupName specified in the webhook provider implementation. | 
**solver_name** | **str** | The name of the solver to use, as defined in the webhook provider implementation. This will typically be the name of the provider, e.g. &#39;cloudflare&#39;. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


