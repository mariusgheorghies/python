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
from kubernetes.client.models.rbac_v1beta1_subject import RbacV1beta1Subject  # noqa: E501
from kubernetes.client.rest import ApiException

class TestRbacV1beta1Subject(unittest.TestCase):
    """RbacV1beta1Subject unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RbacV1beta1Subject
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.rbac_v1beta1_subject.RbacV1beta1Subject()  # noqa: E501
        if include_optional :
            return RbacV1beta1Subject(
                api_group = '0', 
                kind = '0', 
                name = '0', 
                namespace = '0'
            )
        else :
            return RbacV1beta1Subject(
                kind = '0',
                name = '0',
        )

    def testRbacV1beta1Subject(self):
        """Test RbacV1beta1Subject"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
