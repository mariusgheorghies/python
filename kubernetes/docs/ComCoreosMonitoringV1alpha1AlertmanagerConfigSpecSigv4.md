# ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecSigv4

Configures AWS's Signature Verification 4 signing process to sign requests.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_key** | [**ComCoreosMonitoringV1PrometheusSpecSigv4AccessKey**](ComCoreosMonitoringV1PrometheusSpecSigv4AccessKey.md) |  | [optional] 
**profile** | **str** | Profile is the named AWS profile used to authenticate. | [optional] 
**region** | **str** | Region is the AWS region. If blank, the region from the default credentials chain used. | [optional] 
**role_arn** | **str** | RoleArn is the named AWS profile used to authenticate. | [optional] 
**secret_key** | [**ComCoreosMonitoringV1PrometheusSpecSigv4SecretKey**](ComCoreosMonitoringV1PrometheusSpecSigv4SecretKey.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


