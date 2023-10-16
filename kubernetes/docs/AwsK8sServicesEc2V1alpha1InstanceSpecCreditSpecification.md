# AwsK8sServicesEc2V1alpha1InstanceSpecCreditSpecification

The credit option for CPU usage of the burstable performance instance. Valid values are standard and unlimited. To change this attribute after launch, use ModifyInstanceCreditSpecification (https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyInstanceCreditSpecification.html). For more information, see Burstable performance instances (https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-performance-instances.html) in the Amazon EC2 User Guide.   Default: standard (T2 instances) or unlimited (T3/T3a/T4g instances)   For T3 instances with host tenancy, only standard is supported.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu_credits** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


