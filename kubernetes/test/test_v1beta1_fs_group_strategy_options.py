# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import kubernetes.client
from kubernetes.client.models.v1beta1_fs_group_strategy_options import V1beta1FSGroupStrategyOptions  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1beta1FSGroupStrategyOptions(unittest.TestCase):
    """V1beta1FSGroupStrategyOptions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1beta1FSGroupStrategyOptions
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1beta1_fs_group_strategy_options.V1beta1FSGroupStrategyOptions()  # noqa: E501
        if include_optional :
            return V1beta1FSGroupStrategyOptions(
                ranges = [
                    kubernetes.client.models.v1beta1/id_range.v1beta1.IDRange(
                        max = 56, 
                        min = 56, )
                    ], 
                rule = '0'
            )
        else :
            return V1beta1FSGroupStrategyOptions(
        )

    def testV1beta1FSGroupStrategyOptions(self):
        """Test V1beta1FSGroupStrategyOptions"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
