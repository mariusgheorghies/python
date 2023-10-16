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
from kubernetes.client.models.v1beta2_limit_response import V1beta2LimitResponse  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1beta2LimitResponse(unittest.TestCase):
    """V1beta2LimitResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1beta2LimitResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1beta2_limit_response.V1beta2LimitResponse()  # noqa: E501
        if include_optional :
            return V1beta2LimitResponse(
                queuing = kubernetes.client.models.v1beta2/queuing_configuration.v1beta2.QueuingConfiguration(
                    hand_size = 56, 
                    queue_length_limit = 56, 
                    queues = 56, ), 
                type = '0'
            )
        else :
            return V1beta2LimitResponse(
                type = '0',
        )

    def testV1beta2LimitResponse(self):
        """Test V1beta2LimitResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()