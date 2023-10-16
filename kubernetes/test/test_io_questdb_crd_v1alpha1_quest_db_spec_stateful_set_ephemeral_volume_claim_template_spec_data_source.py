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
from kubernetes.client.models.io_questdb_crd_v1alpha1_quest_db_spec_stateful_set_ephemeral_volume_claim_template_spec_data_source import IoQuestdbCrdV1alpha1QuestDBSpecStatefulSetEphemeralVolumeClaimTemplateSpecDataSource  # noqa: E501
from kubernetes.client.rest import ApiException

class TestIoQuestdbCrdV1alpha1QuestDBSpecStatefulSetEphemeralVolumeClaimTemplateSpecDataSource(unittest.TestCase):
    """IoQuestdbCrdV1alpha1QuestDBSpecStatefulSetEphemeralVolumeClaimTemplateSpecDataSource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IoQuestdbCrdV1alpha1QuestDBSpecStatefulSetEphemeralVolumeClaimTemplateSpecDataSource
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.io_questdb_crd_v1alpha1_quest_db_spec_stateful_set_ephemeral_volume_claim_template_spec_data_source.IoQuestdbCrdV1alpha1QuestDBSpecStatefulSetEphemeralVolumeClaimTemplateSpecDataSource()  # noqa: E501
        if include_optional :
            return IoQuestdbCrdV1alpha1QuestDBSpecStatefulSetEphemeralVolumeClaimTemplateSpecDataSource(
                api_group = '0', 
                kind = '0', 
                name = '0'
            )
        else :
            return IoQuestdbCrdV1alpha1QuestDBSpecStatefulSetEphemeralVolumeClaimTemplateSpecDataSource(
                kind = '0',
                name = '0',
        )

    def testIoQuestdbCrdV1alpha1QuestDBSpecStatefulSetEphemeralVolumeClaimTemplateSpecDataSource(self):
        """Test IoQuestdbCrdV1alpha1QuestDBSpecStatefulSetEphemeralVolumeClaimTemplateSpecDataSource"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
