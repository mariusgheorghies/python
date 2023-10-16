# IoCertManagerV1ClusterIssuerSpecVaultAuthAppRoleSecretRef

Reference to a key in a Secret that contains the App Role secret used to authenticate with Vault. The `key` field must be specified and denotes which entry within the Secret resource is used as the app role secret.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The key of the entry in the Secret resource&#39;s &#x60;data&#x60; field to be used. Some instances of this field may be defaulted, in others it may be required. | [optional] 
**name** | **str** | Name of the resource being referred to. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


