# OrgProjectcalicoCrdV1ClusterInformationSpec

ClusterInformationSpec contains the values of describing the cluster.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**calico_version** | **str** | CalicoVersion is the version of Calico that the cluster is running | [optional] 
**cluster_guid** | **str** | ClusterGUID is the GUID of the cluster | [optional] 
**cluster_type** | **str** | ClusterType describes the type of the cluster | [optional] 
**datastore_ready** | **bool** | DatastoreReady is used during significant datastore migrations to signal to components such as Felix that it should wait before accessing the datastore. | [optional] 
**variant** | **str** | Variant declares which variant of Calico should be active. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


