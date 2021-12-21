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
from kubernetes.client.models.v2beta1_container_resource_metric_status import V2beta1ContainerResourceMetricStatus  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV2beta1ContainerResourceMetricStatus(unittest.TestCase):
    """V2beta1ContainerResourceMetricStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V2beta1ContainerResourceMetricStatus
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v2beta1_container_resource_metric_status.V2beta1ContainerResourceMetricStatus()  # noqa: E501
        if include_optional :
            return V2beta1ContainerResourceMetricStatus(
                container = '0', 
                current_average_utilization = 56, 
                current_average_value = '0', 
                name = '0'
            )
        else :
            return V2beta1ContainerResourceMetricStatus(
                container = '0',
                current_average_value = '0',
                name = '0',
        )

    def testV2beta1ContainerResourceMetricStatus(self):
        """Test V2beta1ContainerResourceMetricStatus"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
