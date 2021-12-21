# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.20.7
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import kubernetes.client
from kubernetes.client.models.v1beta1_allowed_host_path import V1beta1AllowedHostPath  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1beta1AllowedHostPath(unittest.TestCase):
    """V1beta1AllowedHostPath unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1beta1AllowedHostPath
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1beta1_allowed_host_path.V1beta1AllowedHostPath()  # noqa: E501
        if include_optional :
            return V1beta1AllowedHostPath(
                path_prefix = '0', 
                read_only = True
            )
        else :
            return V1beta1AllowedHostPath(
        )

    def testV1beta1AllowedHostPath(self):
        """Test V1beta1AllowedHostPath"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
