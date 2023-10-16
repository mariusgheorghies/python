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
from kubernetes.client.models.io_questdb_crd_v1alpha1_quest_db_copy_status import IoQuestdbCrdV1alpha1QuestDBCopyStatus  # noqa: E501
from kubernetes.client.rest import ApiException

class TestIoQuestdbCrdV1alpha1QuestDBCopyStatus(unittest.TestCase):
    """IoQuestdbCrdV1alpha1QuestDBCopyStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IoQuestdbCrdV1alpha1QuestDBCopyStatus
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.io_questdb_crd_v1alpha1_quest_db_copy_status.IoQuestdbCrdV1alpha1QuestDBCopyStatus()  # noqa: E501
        if include_optional :
            return IoQuestdbCrdV1alpha1QuestDBCopyStatus(
                copy_id = '0', 
                copy_logs = [
                    kubernetes.client.models.io_questdb_crd_v1alpha1_quest_db_copy_status_copy_logs.io_questdb_crd_v1alpha1_QuestDBCopy_status_copyLogs(
                        errors = 56, 
                        file = '0', 
                        id = '0', 
                        message = '0', 
                        phase = '0', 
                        rows_handled = 56, 
                        rows_imported = 56, 
                        status = '0', 
                        table = '0', 
                        ts = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ], 
                filename = '0', 
                original_instance_type = '0', 
                phase = '0', 
                transition_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else :
            return IoQuestdbCrdV1alpha1QuestDBCopyStatus(
        )

    def testIoQuestdbCrdV1alpha1QuestDBCopyStatus(self):
        """Test IoQuestdbCrdV1alpha1QuestDBCopyStatus"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
