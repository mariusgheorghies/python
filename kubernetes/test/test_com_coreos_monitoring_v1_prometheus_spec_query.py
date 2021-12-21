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
from kubernetes.client.models.com_coreos_monitoring_v1_prometheus_spec_query import ComCoreosMonitoringV1PrometheusSpecQuery  # noqa: E501
from kubernetes.client.rest import ApiException

class TestComCoreosMonitoringV1PrometheusSpecQuery(unittest.TestCase):
    """ComCoreosMonitoringV1PrometheusSpecQuery unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ComCoreosMonitoringV1PrometheusSpecQuery
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.com_coreos_monitoring_v1_prometheus_spec_query.ComCoreosMonitoringV1PrometheusSpecQuery()  # noqa: E501
        if include_optional :
            return ComCoreosMonitoringV1PrometheusSpecQuery(
                lookback_delta = '0', 
                max_concurrency = 56, 
                max_samples = 56, 
                timeout = '0'
            )
        else :
            return ComCoreosMonitoringV1PrometheusSpecQuery(
        )

    def testComCoreosMonitoringV1PrometheusSpecQuery(self):
        """Test ComCoreosMonitoringV1PrometheusSpecQuery"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
