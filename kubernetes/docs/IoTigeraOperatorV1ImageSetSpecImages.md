# IoTigeraOperatorV1ImageSetSpecImages

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**digest** | **str** | Digest is the image identifier that will be used for the Image. The field should not include a leading &#x60;@&#x60; and must be prefixed with &#x60;sha256:&#x60;. | 
**image** | **str** | Image is an image that the operator deploys and instead of using the built in tag the operator will use the Digest for the image identifier. The value should be the image name without registry or tag or digest. For the image &#x60;docker.io/calico/node:v3.17.1&#x60; it should be represented as &#x60;calico/node&#x60; | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


