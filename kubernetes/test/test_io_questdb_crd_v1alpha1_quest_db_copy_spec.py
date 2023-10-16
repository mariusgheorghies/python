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
from kubernetes.client.models.io_questdb_crd_v1alpha1_quest_db_copy_spec import IoQuestdbCrdV1alpha1QuestDBCopySpec  # noqa: E501
from kubernetes.client.rest import ApiException

class TestIoQuestdbCrdV1alpha1QuestDBCopySpec(unittest.TestCase):
    """IoQuestdbCrdV1alpha1QuestDBCopySpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IoQuestdbCrdV1alpha1QuestDBCopySpec
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.io_questdb_crd_v1alpha1_quest_db_copy_spec.IoQuestdbCrdV1alpha1QuestDBCopySpec()  # noqa: E501
        if include_optional :
            return IoQuestdbCrdV1alpha1QuestDBCopySpec(
                cloud_ids = kubernetes.client.models.io_questdb_crd_v1alpha1_quest_db_copy_spec_cloud_ids.io_questdb_crd_v1alpha1_QuestDBCopy_spec_cloudIds(
                    db_name = '0', 
                    instance_uuid = '0', 
                    org_id = '0', 
                    volume_uuid = '0', ), 
                copy_instance_type = '0', 
                destination = kubernetes.client.models.io_questdb_crd_v1alpha1_quest_db_copy_spec_destination.io_questdb_crd_v1alpha1_QuestDBCopy_spec_destination(
                    quest_db_name = '0', 
                    table_name = '0', ), 
                options = kubernetes.client.models.io_questdb_crd_v1alpha1_quest_db_copy_spec_options.io_questdb_crd_v1alpha1_QuestDBCopy_spec_options(
                    delimiter = '0', 
                    headers = True, 
                    on_error = '0', 
                    partition_by = '0', 
                    timestamp_column = '0', 
                    timestamp_format = '0', ), 
                source = kubernetes.client.models.io_questdb_crd_v1alpha1_quest_db_copy_spec_source.io_questdb_crd_v1alpha1_QuestDBCopy_spec_source(
                    s3 = kubernetes.client.models.io_questdb_crd_v1alpha1_quest_db_copy_spec_source_s3.io_questdb_crd_v1alpha1_QuestDBCopy_spec_source_s3(
                        bucket = '0', 
                        key = '0', ), 
                    url = kubernetes.client.models.io_argoproj_v1alpha1_application_set_spec_git_files.io_argoproj_v1alpha1_ApplicationSet_spec_git_files(
                        path = '0', ), )
            )
        else :
            return IoQuestdbCrdV1alpha1QuestDBCopySpec(
                cloud_ids = kubernetes.client.models.io_questdb_crd_v1alpha1_quest_db_copy_spec_cloud_ids.io_questdb_crd_v1alpha1_QuestDBCopy_spec_cloudIds(
                    db_name = '0', 
                    instance_uuid = '0', 
                    org_id = '0', 
                    volume_uuid = '0', ),
                copy_instance_type = '0',
                destination = kubernetes.client.models.io_questdb_crd_v1alpha1_quest_db_copy_spec_destination.io_questdb_crd_v1alpha1_QuestDBCopy_spec_destination(
                    quest_db_name = '0', 
                    table_name = '0', ),
                source = kubernetes.client.models.io_questdb_crd_v1alpha1_quest_db_copy_spec_source.io_questdb_crd_v1alpha1_QuestDBCopy_spec_source(
                    s3 = kubernetes.client.models.io_questdb_crd_v1alpha1_quest_db_copy_spec_source_s3.io_questdb_crd_v1alpha1_QuestDBCopy_spec_source_s3(
                        bucket = '0', 
                        key = '0', ), 
                    url = kubernetes.client.models.io_argoproj_v1alpha1_application_set_spec_git_files.io_argoproj_v1alpha1_ApplicationSet_spec_git_files(
                        path = '0', ), ),
        )

    def testIoQuestdbCrdV1alpha1QuestDBCopySpec(self):
        """Test IoQuestdbCrdV1alpha1QuestDBCopySpec"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()