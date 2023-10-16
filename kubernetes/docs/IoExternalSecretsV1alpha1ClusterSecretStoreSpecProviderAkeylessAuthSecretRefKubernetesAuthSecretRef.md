# IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderAkeylessAuthSecretRefKubernetesAuthSecretRef

Optional secret field containing a Kubernetes ServiceAccount JWT used for authenticating with Akeyless. If a name is specified without a key, `token` is the default. If one is not specified, the one bound to the controller will be used.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The key of the entry in the Secret resource&#39;s &#x60;data&#x60; field to be used. Some instances of this field may be defaulted, in others it may be required. | [optional] 
**name** | **str** | The name of the Secret resource being referred to. | [optional] 
**namespace** | **str** | Namespace of the resource being referred to. Ignored if referent is not cluster-scoped. cluster-scoped defaults to the namespace of the referent. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


