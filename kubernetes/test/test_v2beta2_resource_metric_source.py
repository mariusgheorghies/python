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
from kubernetes.client.models.v2beta2_resource_metric_source import V2beta2ResourceMetricSource  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV2beta2ResourceMetricSource(unittest.TestCase):
    """V2beta2ResourceMetricSource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V2beta2ResourceMetricSource
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v2beta2_resource_metric_source.V2beta2ResourceMetricSource()  # noqa: E501
        if include_optional :
            return V2beta2ResourceMetricSource(
                name = '0', 
                target = kubernetes.client.models.v2beta2/metric_target.v2beta2.MetricTarget(
                    average_utilization = 56, 
                    average_value = '0', 
                    type = '0', 
                    value = '0', )
            )
        else :
            return V2beta2ResourceMetricSource(
                name = '0',
                target = kubernetes.client.models.v2beta2/metric_target.v2beta2.MetricTarget(
                    average_utilization = 56, 
                    average_value = '0', 
                    type = '0', 
                    value = '0', ),
        )

    def testV2beta2ResourceMetricSource(self):
        """Test V2beta2ResourceMetricSource"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
