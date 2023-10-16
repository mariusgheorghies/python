# ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecSnsConfigs

SNSConfig configures notifications via AWS SNS. See https://prometheus.io/docs/alerting/latest/configuration/#sns_configs
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_url** | **str** | The SNS API URL i.e. https://sns.us-east-2.amazonaws.com. If not specified, the SNS API URL from the SNS SDK will be used. | [optional] 
**attributes** | **dict(str, str)** | SNS message attributes. | [optional] 
**http_config** | [**ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecHttpConfig**](ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecHttpConfig.md) |  | [optional] 
**message** | **str** | The message content of the SNS notification. | [optional] 
**phone_number** | **str** | Phone number if message is delivered via SMS in E.164 format. If you don&#39;t specify this value, you must specify a value for the TopicARN or TargetARN. | [optional] 
**send_resolved** | **bool** | Whether or not to notify about resolved alerts. | [optional] 
**sigv4** | [**ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecSigv4**](ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecSigv4.md) |  | [optional] 
**subject** | **str** | Subject line when the message is delivered to email endpoints. | [optional] 
**target_arn** | **str** | The  mobile platform endpoint ARN if message is delivered via mobile notifications. If you don&#39;t specify this value, you must specify a value for the topic_arn or PhoneNumber. | [optional] 
**topic_arn** | **str** | SNS topic ARN, i.e. arn:aws:sns:us-east-2:698519295917:My-Topic If you don&#39;t specify this value, you must specify a value for the PhoneNumber or TargetARN. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


