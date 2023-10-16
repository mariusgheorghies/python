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
from kubernetes.client.models.io_argoproj_v1alpha1_app_project_spec_cluster_resource_blacklist import IoArgoprojV1alpha1AppProjectSpecClusterResourceBlacklist  # noqa: E501
from kubernetes.client.rest import ApiException

class TestIoArgoprojV1alpha1AppProjectSpecClusterResourceBlacklist(unittest.TestCase):
    """IoArgoprojV1alpha1AppProjectSpecClusterResourceBlacklist unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IoArgoprojV1alpha1AppProjectSpecClusterResourceBlacklist
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.io_argoproj_v1alpha1_app_project_spec_cluster_resource_blacklist.IoArgoprojV1alpha1AppProjectSpecClusterResourceBlacklist()  # noqa: E501
        if include_optional :
            return IoArgoprojV1alpha1AppProjectSpecClusterResourceBlacklist(
                group = '0', 
                kind = '0'
            )
        else :
            return IoArgoprojV1alpha1AppProjectSpecClusterResourceBlacklist(
                group = '0',
                kind = '0',
        )

    def testIoArgoprojV1alpha1AppProjectSpecClusterResourceBlacklist(self):
        """Test IoArgoprojV1alpha1AppProjectSpecClusterResourceBlacklist"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()