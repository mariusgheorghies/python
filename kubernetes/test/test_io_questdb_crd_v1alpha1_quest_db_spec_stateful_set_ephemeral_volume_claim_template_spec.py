# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.25.12
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import kubernetes.client
from kubernetes.client.models.io_questdb_crd_v1alpha1_quest_db_spec_stateful_set_ephemeral_volume_claim_template_spec import IoQuestdbCrdV1alpha1QuestDBSpecStatefulSetEphemeralVolumeClaimTemplateSpec  # noqa: E501
from kubernetes.client.rest import ApiException

class TestIoQuestdbCrdV1alpha1QuestDBSpecStatefulSetEphemeralVolumeClaimTemplateSpec(unittest.TestCase):
    """IoQuestdbCrdV1alpha1QuestDBSpecStatefulSetEphemeralVolumeClaimTemplateSpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IoQuestdbCrdV1alpha1QuestDBSpecStatefulSetEphemeralVolumeClaimTemplateSpec
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.io_questdb_crd_v1alpha1_quest_db_spec_stateful_set_ephemeral_volume_claim_template_spec.IoQuestdbCrdV1alpha1QuestDBSpecStatefulSetEphemeralVolumeClaimTemplateSpec()  # noqa: E501
        if include_optional :
            return IoQuestdbCrdV1alpha1QuestDBSpecStatefulSetEphemeralVolumeClaimTemplateSpec(
                access_modes = [
                    '0'
                    ], 
                data_source = kubernetes.client.models.io_questdb_crd_v1alpha1_quest_db_spec_stateful_set_ephemeral_volume_claim_template_spec_data_source.io_questdb_crd_v1alpha1_QuestDB_spec_statefulSet_ephemeral_volumeClaimTemplate_spec_dataSource(
                    api_group = '0', 
                    kind = '0', 
                    name = '0', ), 
                data_source_ref = kubernetes.client.models.io_questdb_crd_v1alpha1_quest_db_spec_stateful_set_ephemeral_volume_claim_template_spec_data_source_ref.io_questdb_crd_v1alpha1_QuestDB_spec_statefulSet_ephemeral_volumeClaimTemplate_spec_dataSourceRef(
                    api_group = '0', 
                    kind = '0', 
                    name = '0', ), 
                resources = kubernetes.client.models.io_questdb_crd_v1alpha1_quest_db_spec_stateful_set_ephemeral_volume_claim_template_spec_resources.io_questdb_crd_v1alpha1_QuestDB_spec_statefulSet_ephemeral_volumeClaimTemplate_spec_resources(
                    limits = {
                        'key' : None
                        }, 
                    requests = {
                        'key' : None
                        }, ), 
                selector = kubernetes.client.models.com_grafana_monitoring_v1alpha1_grafana_agent_spec_storage_ephemeral_volume_claim_template_spec_selector.com_grafana_monitoring_v1alpha1_GrafanaAgent_spec_storage_ephemeral_volumeClaimTemplate_spec_selector(
                    match_expressions = [
                        kubernetes.client.models.aws_k8s_networking_v1alpha1_policy_endpoint_spec_pod_selector_match_expressions.aws_k8s_networking_v1alpha1_PolicyEndpoint_spec_podSelector_matchExpressions(
                            key = '0', 
                            operator = '0', 
                            values = [
                                '0'
                                ], )
                        ], 
                    match_labels = {
                        'key' : '0'
                        }, ), 
                storage_class_name = '0', 
                volume_mode = '0', 
                volume_name = '0'
            )
        else :
            return IoQuestdbCrdV1alpha1QuestDBSpecStatefulSetEphemeralVolumeClaimTemplateSpec(
        )

    def testIoQuestdbCrdV1alpha1QuestDBSpecStatefulSetEphemeralVolumeClaimTemplateSpec(self):
        """Test IoQuestdbCrdV1alpha1QuestDBSpecStatefulSetEphemeralVolumeClaimTemplateSpec"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
