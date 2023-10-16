# IoArgoprojV1alpha1Application

Application is a definition of Application resource.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the kubernetes.client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) |  | 
**operation** | [**IoArgoprojV1alpha1ApplicationOperation**](IoArgoprojV1alpha1ApplicationOperation.md) |  | [optional] 
**spec** | [**IoArgoprojV1alpha1ApplicationSpec**](IoArgoprojV1alpha1ApplicationSpec.md) |  | 
**status** | [**IoArgoprojV1alpha1ApplicationStatus**](IoArgoprojV1alpha1ApplicationStatus.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


