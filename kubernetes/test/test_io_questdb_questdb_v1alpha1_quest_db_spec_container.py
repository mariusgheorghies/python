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
from kubernetes.client.models.io_questdb_questdb_v1alpha1_quest_db_spec_container import IoQuestdbQuestdbV1alpha1QuestDBSpecContainer  # noqa: E501
from kubernetes.client.rest import ApiException

class TestIoQuestdbQuestdbV1alpha1QuestDBSpecContainer(unittest.TestCase):
    """IoQuestdbQuestdbV1alpha1QuestDBSpecContainer unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IoQuestdbQuestdbV1alpha1QuestDBSpecContainer
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.io_questdb_questdb_v1alpha1_quest_db_spec_container.IoQuestdbQuestdbV1alpha1QuestDBSpecContainer()  # noqa: E501
        if include_optional :
            return IoQuestdbQuestdbV1alpha1QuestDBSpecContainer(
                name = '0', 
                registry = '0', 
                tag = '0'
            )
        else :
            return IoQuestdbQuestdbV1alpha1QuestDBSpecContainer(
        )

    def testIoQuestdbQuestdbV1alpha1QuestDBSpecContainer(self):
        """Test IoQuestdbQuestdbV1alpha1QuestDBSpecContainer"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
