# IoQuestdbCrdV1alpha1QuestDBStatus

QuestDBStatus defines the observed state of QuestDB
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws** | [**IoQuestdbCrdV1alpha1QuestDBStatusAws**](IoQuestdbCrdV1alpha1QuestDBStatusAws.md) |  | [optional] 
**conditions** | [**list[IoQuestdbCrdV1alpha1QuestDBStatusConditions]**](IoQuestdbCrdV1alpha1QuestDBStatusConditions.md) | Conditions include status for whether the statefulset and deployment pods are ready | [optional] 
**dns_ready** | **bool** | Are DNS records created for the node&#39;s IP address? These are used for ILP and Psql only.  HTTPS DNS is controlled elsewhere | [optional] 
**ilp_node_port** | **int** | ILP port | [optional] 
**next_volume_modification_attempt** | **datetime** | Next available time that the controller will let you increase the volume size. AWS prevents volume size changes from happening too often, so we limit the time that you can modify the volume size to 6 hours after the last change | [optional] 
**node_ip** | **str** | The database node&#39;s external IP address | [optional] 
**node_name** | **str** | Name of the database node | [optional] 
**node_ready** | **bool** | Is the database node&#39;s status \&quot;Ready\&quot;? | [optional] 
**psql_node_port** | **int** | PGWire port | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


