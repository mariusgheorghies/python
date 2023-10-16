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
from kubernetes.client.models.io_questdb_crd_v1alpha1_quest_db_standby_node_spec import IoQuestdbCrdV1alpha1QuestDBStandbyNodeSpec  # noqa: E501
from kubernetes.client.rest import ApiException

class TestIoQuestdbCrdV1alpha1QuestDBStandbyNodeSpec(unittest.TestCase):
    """IoQuestdbCrdV1alpha1QuestDBStandbyNodeSpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IoQuestdbCrdV1alpha1QuestDBStandbyNodeSpec
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.io_questdb_crd_v1alpha1_quest_db_standby_node_spec.IoQuestdbCrdV1alpha1QuestDBStandbyNodeSpec()  # noqa: E501
        if include_optional :
            return IoQuestdbCrdV1alpha1QuestDBStandbyNodeSpec(
                aws = kubernetes.client.models.io_questdb_crd_v1alpha1_quest_db_standby_node_spec_aws.io_questdb_crd_v1alpha1_QuestDBStandbyNode_spec_aws(
                    default_security_group_ids = [
                        '0'
                        ], 
                    iam_instance_profile_arn = '0', 
                    image_id = '0', 
                    instance_type = '0', 
                    key_name = '0', 
                    region = '0', 
                    region_az = '0', 
                    subnet_id = '0', )
            )
        else :
            return IoQuestdbCrdV1alpha1QuestDBStandbyNodeSpec(
        )

    def testIoQuestdbCrdV1alpha1QuestDBStandbyNodeSpec(self):
        """Test IoQuestdbCrdV1alpha1QuestDBStandbyNodeSpec"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
