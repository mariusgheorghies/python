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
from kubernetes.client.models.v1_secret_projection import V1SecretProjection  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1SecretProjection(unittest.TestCase):
    """V1SecretProjection unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1SecretProjection
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1_secret_projection.V1SecretProjection()  # noqa: E501
        if include_optional :
            return V1SecretProjection(
                items = [
                    kubernetes.client.models.v1/key_to_path.v1.KeyToPath(
                        key = '0', 
                        mode = 56, 
                        path = '0', )
                    ], 
                name = '0', 
                optional = True
            )
        else :
            return V1SecretProjection(
        )

    def testV1SecretProjection(self):
        """Test V1SecretProjection"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
