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
from kubernetes.client.models.io_argoproj_v1alpha1_app_project_spec_orphaned_resources_ignore import IoArgoprojV1alpha1AppProjectSpecOrphanedResourcesIgnore  # noqa: E501
from kubernetes.client.rest import ApiException

class TestIoArgoprojV1alpha1AppProjectSpecOrphanedResourcesIgnore(unittest.TestCase):
    """IoArgoprojV1alpha1AppProjectSpecOrphanedResourcesIgnore unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IoArgoprojV1alpha1AppProjectSpecOrphanedResourcesIgnore
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.io_argoproj_v1alpha1_app_project_spec_orphaned_resources_ignore.IoArgoprojV1alpha1AppProjectSpecOrphanedResourcesIgnore()  # noqa: E501
        if include_optional :
            return IoArgoprojV1alpha1AppProjectSpecOrphanedResourcesIgnore(
                group = '0', 
                kind = '0', 
                name = '0'
            )
        else :
            return IoArgoprojV1alpha1AppProjectSpecOrphanedResourcesIgnore(
        )

    def testIoArgoprojV1alpha1AppProjectSpecOrphanedResourcesIgnore(self):
        """Test IoArgoprojV1alpha1AppProjectSpecOrphanedResourcesIgnore"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
