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
from kubernetes.client.models.io_questdb_crd_v1alpha1_quest_db_status import IoQuestdbCrdV1alpha1QuestDBStatus  # noqa: E501
from kubernetes.client.rest import ApiException

class TestIoQuestdbCrdV1alpha1QuestDBStatus(unittest.TestCase):
    """IoQuestdbCrdV1alpha1QuestDBStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IoQuestdbCrdV1alpha1QuestDBStatus
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.io_questdb_crd_v1alpha1_quest_db_status.IoQuestdbCrdV1alpha1QuestDBStatus()  # noqa: E501
        if include_optional :
            return IoQuestdbCrdV1alpha1QuestDBStatus(
                aws = kubernetes.client.models.io_questdb_crd_v1alpha1_quest_db_status_aws.io_questdb_crd_v1alpha1_QuestDB_status_aws(
                    hz_id = '0', 
                    hz_name = '0', 
                    sg_id = '0', 
                    sg_ready = True, ), 
                conditions = [
                    kubernetes.client.models.io_questdb_crd_v1alpha1_quest_db_status_conditions.io_questdb_crd_v1alpha1_QuestDB_status_conditions(
                        last_transition_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        message = '0', 
                        observed_generation = 0, 
                        reason = 'a', 
                        status = 'True', 
                        type = 'a', )
                    ], 
                dns_ready = True, 
                ilp_node_port = 56, 
                next_volume_modification_attempt = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                node_ip = '0', 
                node_name = '0', 
                node_ready = True, 
                psql_node_port = 56
            )
        else :
            return IoQuestdbCrdV1alpha1QuestDBStatus(
        )

    def testIoQuestdbCrdV1alpha1QuestDBStatus(self):
        """Test IoQuestdbCrdV1alpha1QuestDBStatus"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()