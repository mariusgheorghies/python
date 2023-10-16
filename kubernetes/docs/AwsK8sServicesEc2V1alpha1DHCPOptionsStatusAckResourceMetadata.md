# AwsK8sServicesEc2V1alpha1DHCPOptionsStatusAckResourceMetadata

All CRs managed by ACK have a common `Status.ACKResourceMetadata` member that is used to contain resource sync state, account ownership, constructed ARN for the resource
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arn** | **str** | ARN is the Amazon Resource Name for the resource. This is a globally-unique identifier and is set only by the ACK service controller once the controller has orchestrated the creation of the resource OR when it has verified that an \&quot;adopted\&quot; resource (a resource where the ARN annotation was set by the Kubernetes user on the CR) exists and matches the supplied CR&#39;s Spec field values. TODO(vijat@): Find a better strategy for resources that do not have ARN in CreateOutputResponse https://github.com/aws/aws-controllers-k8s/issues/270 | [optional] 
**owner_account_id** | **str** | OwnerAccountID is the AWS Account ID of the account that owns the backend AWS service API resource. | 
**region** | **str** | Region is the AWS region in which the resource exists or will exist. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


