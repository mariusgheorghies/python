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
from kubernetes.client.models.io_questdb_crd_v1alpha1_quest_db_volume_spec import IoQuestdbCrdV1alpha1QuestDBVolumeSpec  # noqa: E501
from kubernetes.client.rest import ApiException

class TestIoQuestdbCrdV1alpha1QuestDBVolumeSpec(unittest.TestCase):
    """IoQuestdbCrdV1alpha1QuestDBVolumeSpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IoQuestdbCrdV1alpha1QuestDBVolumeSpec
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.io_questdb_crd_v1alpha1_quest_db_volume_spec.IoQuestdbCrdV1alpha1QuestDBVolumeSpec()  # noqa: E501
        if include_optional :
            return IoQuestdbCrdV1alpha1QuestDBVolumeSpec(
                aws = kubernetes.client.models.io_questdb_crd_v1alpha1_quest_db_volume_spec_aws.io_questdb_crd_v1alpha1_QuestDBVolume_spec_aws(
                    encrypted = True, 
                    iops = 56, 
                    region_az = '0', 
                    throughput = 56, 
                    type = '0', ), 
                cloud_ids = kubernetes.client.models.io_questdb_crd_v1alpha1_quest_db_copy_spec_cloud_ids.io_questdb_crd_v1alpha1_QuestDBCopy_spec_cloudIds(
                    db_name = '0', 
                    instance_uuid = '0', 
                    org_id = '0', 
                    volume_uuid = '0', ), 
                filesystem = '0', 
                size = kubernetes.client.models.size.size(), 
                snapshot = kubernetes.client.models.io_questdb_crd_v1alpha1_quest_db_spec_volume_snapshot.io_questdb_crd_v1alpha1_QuestDB_spec_volume_snapshot(
                    aws = kubernetes.client.models.io_questdb_crd_v1alpha1_quest_db_spec_volume_snapshot_aws.io_questdb_crd_v1alpha1_QuestDB_spec_volume_snapshot_aws(
                        snapshot_id = '0', ), )
            )
        else :
            return IoQuestdbCrdV1alpha1QuestDBVolumeSpec(
        )

    def testIoQuestdbCrdV1alpha1QuestDBVolumeSpec(self):
        """Test IoQuestdbCrdV1alpha1QuestDBVolumeSpec"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
