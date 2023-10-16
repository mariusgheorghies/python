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
from kubernetes.client.models.io_argoproj_v1alpha1_application_operation_sync_source_directory_jsonnet import IoArgoprojV1alpha1ApplicationOperationSyncSourceDirectoryJsonnet  # noqa: E501
from kubernetes.client.rest import ApiException

class TestIoArgoprojV1alpha1ApplicationOperationSyncSourceDirectoryJsonnet(unittest.TestCase):
    """IoArgoprojV1alpha1ApplicationOperationSyncSourceDirectoryJsonnet unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IoArgoprojV1alpha1ApplicationOperationSyncSourceDirectoryJsonnet
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.io_argoproj_v1alpha1_application_operation_sync_source_directory_jsonnet.IoArgoprojV1alpha1ApplicationOperationSyncSourceDirectoryJsonnet()  # noqa: E501
        if include_optional :
            return IoArgoprojV1alpha1ApplicationOperationSyncSourceDirectoryJsonnet(
                ext_vars = [
                    kubernetes.client.models.io_argoproj_v1alpha1_application_operation_sync_source_directory_jsonnet_ext_vars.io_argoproj_v1alpha1_Application_operation_sync_source_directory_jsonnet_extVars(
                        code = True, 
                        name = '0', 
                        value = '0', )
                    ], 
                libs = [
                    '0'
                    ], 
                tlas = [
                    kubernetes.client.models.io_argoproj_v1alpha1_application_operation_sync_source_directory_jsonnet_ext_vars.io_argoproj_v1alpha1_Application_operation_sync_source_directory_jsonnet_extVars(
                        code = True, 
                        name = '0', 
                        value = '0', )
                    ]
            )
        else :
            return IoArgoprojV1alpha1ApplicationOperationSyncSourceDirectoryJsonnet(
        )

    def testIoArgoprojV1alpha1ApplicationOperationSyncSourceDirectoryJsonnet(self):
        """Test IoArgoprojV1alpha1ApplicationOperationSyncSourceDirectoryJsonnet"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
