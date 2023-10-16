# IoTigeraOperatorV1InstallationSpecCertificateManagement

CertificateManagement configures pods to submit a CertificateSigningRequest to the certificates.k8s.io/v1beta1 API in order to obtain TLS certificates. This feature requires that you bring your own CSR signing and approval process, otherwise pods will be stuck during initialization.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ca_cert** | **str** | Certificate of the authority that signs the CertificateSigningRequests in PEM format. | 
**key_algorithm** | **str** | Specify the algorithm used by pods to generate a key pair that is associated with the X.509 certificate request. Default: RSAWithSize2048 | [optional] 
**signature_algorithm** | **str** | Specify the algorithm used for the signature of the X.509 certificate request. Default: SHA256WithRSA | [optional] 
**signer_name** | **str** | When a CSR is issued to the certificates.k8s.io API, the signerName is added to the request in order to accommodate for clusters with multiple signers. Must be formatted as: &#x60;&lt;my-domain&gt;/&lt;my-signername&gt;&#x60;. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


