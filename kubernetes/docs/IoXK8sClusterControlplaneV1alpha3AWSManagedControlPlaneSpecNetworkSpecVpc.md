# IoXK8sClusterControlplaneV1alpha3AWSManagedControlPlaneSpecNetworkSpecVpc

VPC configuration.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**availability_zone_selection** | **str** | AvailabilityZoneSelection specifies how AZs should be selected if there are more AZs in a region than specified by AvailabilityZoneUsageLimit. There are 2 selection schemes: Ordered - selects based on alphabetical order Random - selects AZs randomly in a region Defaults to Ordered | [optional] 
**availability_zone_usage_limit** | **int** | AvailabilityZoneUsageLimit specifies the maximum number of availability zones (AZ) that should be used in a region when automatically creating subnets. If a region has more than this number of AZs then this number of AZs will be picked randomly when creating default subnets. Defaults to 3 | [optional] 
**cidr_block** | **str** | CidrBlock is the CIDR block to be used when the provider creates a managed VPC. Defaults to 10.0.0.0/16. | [optional] 
**id** | **str** | ID is the vpc-id of the VPC this provider should use to create resources. | [optional] 
**internet_gateway_id** | **str** | InternetGatewayID is the id of the internet gateway associated with the VPC. | [optional] 
**tags** | **dict(str, str)** | Tags is a collection of tags describing the resource. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


