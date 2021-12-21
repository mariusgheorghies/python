# IoCertManagerV1alpha2CertificateSpecPrivateKey

Options to control private keys used for the Certificate.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rotation_policy** | **str** | RotationPolicy controls how private keys should be regenerated when a re-issuance is being processed. If set to Never, a private key will only be generated if one does not already exist in the target &#x60;spec.secretName&#x60;. If one does exists but it does not have the correct algorithm or size, a warning will be raised to await user intervention. If set to Always, a private key matching the specified requirements will be generated whenever a re-issuance occurs. Default is &#39;Never&#39; for backward compatibility. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


