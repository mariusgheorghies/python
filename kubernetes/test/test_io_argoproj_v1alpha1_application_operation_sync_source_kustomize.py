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
from kubernetes.client.models.io_argoproj_v1alpha1_application_operation_sync_source_kustomize import IoArgoprojV1alpha1ApplicationOperationSyncSourceKustomize  # noqa: E501
from kubernetes.client.rest import ApiException

class TestIoArgoprojV1alpha1ApplicationOperationSyncSourceKustomize(unittest.TestCase):
    """IoArgoprojV1alpha1ApplicationOperationSyncSourceKustomize unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IoArgoprojV1alpha1ApplicationOperationSyncSourceKustomize
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.io_argoproj_v1alpha1_application_operation_sync_source_kustomize.IoArgoprojV1alpha1ApplicationOperationSyncSourceKustomize()  # noqa: E501
        if include_optional :
            return IoArgoprojV1alpha1ApplicationOperationSyncSourceKustomize(
                common_annotations = {
                    'key' : '0'
                    }, 
                common_annotations_envsubst = True, 
                common_labels = {
                    'key' : '0'
                    }, 
                force_common_annotations = True, 
                force_common_labels = True, 
                images = [
                    '0'
                    ], 
                name_prefix = '0', 
                name_suffix = '0', 
                namespace = '0', 
                replicas = [
                    kubernetes.client.models.io_argoproj_v1alpha1_application_operation_sync_source_kustomize_replicas.io_argoproj_v1alpha1_Application_operation_sync_source_kustomize_replicas(
                        count = kubernetes.client.models.count.count(), 
                        name = '0', )
                    ], 
                version = '0'
            )
        else :
            return IoArgoprojV1alpha1ApplicationOperationSyncSourceKustomize(
        )

    def testIoArgoprojV1alpha1ApplicationOperationSyncSourceKustomize(self):
        """Test IoArgoprojV1alpha1ApplicationOperationSyncSourceKustomize"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
