# IoTigeraOperatorV1Installation

Installation configures an installation of Calico or Calico Enterprise. At most one instance of this resource is supported. It must be named \"default\". The Installation API installs core networking and network policy components, and provides general install-time configuration.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the kubernetes.client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) |  | [optional] 
**spec** | [**IoTigeraOperatorV1InstallationSpec**](IoTigeraOperatorV1InstallationSpec.md) |  | [optional] 
**status** | [**IoTigeraOperatorV1InstallationStatus**](IoTigeraOperatorV1InstallationStatus.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


