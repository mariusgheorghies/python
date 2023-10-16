# ComGrafanaMonitoringV1alpha1GrafanaAgentSpecMetricsSigv4

SigV4 configures SigV4-based authentication to the remote_write endpoint. SigV4-based authentication is used if SigV4 is defined, even with an empty object.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_key** | [**ComGrafanaMonitoringV1alpha1GrafanaAgentSpecMetricsSigv4AccessKey**](ComGrafanaMonitoringV1alpha1GrafanaAgentSpecMetricsSigv4AccessKey.md) |  | [optional] 
**profile** | **str** | Profile is the named AWS profile to use for authentication. | [optional] 
**region** | **str** | Region of the AWS endpoint. If blank, the region from the default credentials chain is used. | [optional] 
**role_arn** | **str** | RoleARN is the AWS Role ARN to use for authentication, as an alternative for using the AWS API keys. | [optional] 
**secret_key** | [**ComGrafanaMonitoringV1alpha1GrafanaAgentSpecMetricsSigv4SecretKey**](ComGrafanaMonitoringV1alpha1GrafanaAgentSpecMetricsSigv4SecretKey.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


