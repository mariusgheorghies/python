# IoCertManagerV1beta1CertificateSpecPrivateKey

Options to control private keys used for the Certificate.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algorithm** | **str** | Algorithm is the private key algorithm of the corresponding private key for this certificate. If provided, allowed values are either &#x60;RSA&#x60; or &#x60;ECDSA&#x60; If &#x60;algorithm&#x60; is specified and &#x60;size&#x60; is not provided, key size of 256 will be used for &#x60;ECDSA&#x60; key algorithm and key size of 2048 will be used for &#x60;RSA&#x60; key algorithm. | [optional] 
**encoding** | **str** | The private key cryptography standards (PKCS) encoding for this certificate&#39;s private key to be encoded in. If provided, allowed values are &#x60;PKCS1&#x60; and &#x60;PKCS8&#x60; standing for PKCS#1 and PKCS#8, respectively. Defaults to &#x60;PKCS1&#x60; if not specified. | [optional] 
**rotation_policy** | **str** | RotationPolicy controls how private keys should be regenerated when a re-issuance is being processed. If set to Never, a private key will only be generated if one does not already exist in the target &#x60;spec.secretName&#x60;. If one does exists but it does not have the correct algorithm or size, a warning will be raised to await user intervention. If set to Always, a private key matching the specified requirements will be generated whenever a re-issuance occurs. Default is &#39;Never&#39; for backward compatibility. | [optional] 
**size** | **int** | Size is the key bit size of the corresponding private key for this certificate. If &#x60;algorithm&#x60; is set to &#x60;RSA&#x60;, valid values are &#x60;2048&#x60;, &#x60;4096&#x60; or &#x60;8192&#x60;, and will default to &#x60;2048&#x60; if not specified. If &#x60;algorithm&#x60; is set to &#x60;ECDSA&#x60;, valid values are &#x60;256&#x60;, &#x60;384&#x60; or &#x60;521&#x60;, and will default to &#x60;256&#x60; if not specified. No other values are allowed. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


