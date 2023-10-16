# ComGrafanaMonitoringV1alpha1GrafanaAgentSpecMetricsSigv4AccessKey

AccessKey holds the secret of the AWS API access key to use for signing. If not provided, the environment variable AWS_ACCESS_KEY_ID is used.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The key of the secret to select from.  Must be a valid secret key. | 
**name** | **str** | Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names TODO: Add other useful fields. apiVersion, kind, uid? | [optional] 
**optional** | **bool** | Specify whether the Secret or its key must be defined | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


