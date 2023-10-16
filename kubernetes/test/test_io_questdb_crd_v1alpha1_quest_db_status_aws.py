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
from kubernetes.client.models.io_questdb_crd_v1alpha1_quest_db_status_aws import IoQuestdbCrdV1alpha1QuestDBStatusAws  # noqa: E501
from kubernetes.client.rest import ApiException

class TestIoQuestdbCrdV1alpha1QuestDBStatusAws(unittest.TestCase):
    """IoQuestdbCrdV1alpha1QuestDBStatusAws unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IoQuestdbCrdV1alpha1QuestDBStatusAws
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.io_questdb_crd_v1alpha1_quest_db_status_aws.IoQuestdbCrdV1alpha1QuestDBStatusAws()  # noqa: E501
        if include_optional :
            return IoQuestdbCrdV1alpha1QuestDBStatusAws(
                hz_id = '0', 
                hz_name = '0', 
                sg_id = '0', 
                sg_ready = True
            )
        else :
            return IoQuestdbCrdV1alpha1QuestDBStatusAws(
        )

    def testIoQuestdbCrdV1alpha1QuestDBStatusAws(self):
        """Test IoQuestdbCrdV1alpha1QuestDBStatusAws"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()