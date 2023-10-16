# IoTigeraOperatorV1ImageSet

ImageSet is used to specify image digests for the images that the operator deploys. The name of the ImageSet is expected to be in the format `<variang>-<release>`. The `variant` used is `enterprise` if the InstallationSpec Variant is `TigeraSecureEnterprise` otherwise it is `calico`. The `release` must match the version of the variant that the operator is built to deploy, this version can be obtained by passing the `--version` flag to the operator binary.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the kubernetes.client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) |  | [optional] 
**spec** | [**IoTigeraOperatorV1ImageSetSpec**](IoTigeraOperatorV1ImageSetSpec.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


