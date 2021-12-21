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
from kubernetes.client.models.v1beta1_non_resource_attributes import V1beta1NonResourceAttributes  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1beta1NonResourceAttributes(unittest.TestCase):
    """V1beta1NonResourceAttributes unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1beta1NonResourceAttributes
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1beta1_non_resource_attributes.V1beta1NonResourceAttributes()  # noqa: E501
        if include_optional :
            return V1beta1NonResourceAttributes(
                path = '0', 
                verb = '0'
            )
        else :
            return V1beta1NonResourceAttributes(
        )

    def testV1beta1NonResourceAttributes(self):
        """Test V1beta1NonResourceAttributes"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
