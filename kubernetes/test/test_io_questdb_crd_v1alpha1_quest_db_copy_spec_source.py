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
from kubernetes.client.models.io_questdb_crd_v1alpha1_quest_db_copy_spec_source import IoQuestdbCrdV1alpha1QuestDBCopySpecSource  # noqa: E501
from kubernetes.client.rest import ApiException

class TestIoQuestdbCrdV1alpha1QuestDBCopySpecSource(unittest.TestCase):
    """IoQuestdbCrdV1alpha1QuestDBCopySpecSource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IoQuestdbCrdV1alpha1QuestDBCopySpecSource
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.io_questdb_crd_v1alpha1_quest_db_copy_spec_source.IoQuestdbCrdV1alpha1QuestDBCopySpecSource()  # noqa: E501
        if include_optional :
            return IoQuestdbCrdV1alpha1QuestDBCopySpecSource(
                s3 = kubernetes.client.models.io_questdb_crd_v1alpha1_quest_db_copy_spec_source_s3.io_questdb_crd_v1alpha1_QuestDBCopy_spec_source_s3(
                    bucket = '0', 
                    key = '0', ), 
                url = kubernetes.client.models.io_argoproj_v1alpha1_application_set_spec_git_files.io_argoproj_v1alpha1_ApplicationSet_spec_git_files(
                    path = '0', )
            )
        else :
            return IoQuestdbCrdV1alpha1QuestDBCopySpecSource(
        )

    def testIoQuestdbCrdV1alpha1QuestDBCopySpecSource(self):
        """Test IoQuestdbCrdV1alpha1QuestDBCopySpecSource"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()