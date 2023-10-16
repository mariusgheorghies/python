# IoCertManagerAcmeV1ChallengeSpecSolverDns01Route53

Use the AWS Route53 API to manage DNS01 challenge records.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_key_id** | **str** | The AccessKeyID is used for authentication. If not set we fall-back to using env vars, shared credentials file or AWS Instance metadata see: https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/configuring-sdk.html#specifying-credentials | [optional] 
**hosted_zone_id** | **str** | If set, the provider will manage only this zone in Route53 and will not do an lookup using the route53:ListHostedZonesByName api call. | [optional] 
**region** | **str** | Always set the region when using AccessKeyID and SecretAccessKey | 
**role** | **str** | Role is a Role ARN which the Route53 provider will assume using either the explicit credentials AccessKeyID/SecretAccessKey or the inferred credentials from environment variables, shared credentials file or AWS Instance metadata | [optional] 
**secret_access_key_secret_ref** | [**IoCertManagerAcmeV1ChallengeSpecSolverDns01Route53SecretAccessKeySecretRef**](IoCertManagerAcmeV1ChallengeSpecSolverDns01Route53SecretAccessKeySecretRef.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


