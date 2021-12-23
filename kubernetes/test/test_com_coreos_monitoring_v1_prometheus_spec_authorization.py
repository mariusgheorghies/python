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
from kubernetes.client.models.com_coreos_monitoring_v1_prometheus_spec_authorization import ComCoreosMonitoringV1PrometheusSpecAuthorization  # noqa: E501
from kubernetes.client.rest import ApiException

class TestComCoreosMonitoringV1PrometheusSpecAuthorization(unittest.TestCase):
    """ComCoreosMonitoringV1PrometheusSpecAuthorization unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ComCoreosMonitoringV1PrometheusSpecAuthorization
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.com_coreos_monitoring_v1_prometheus_spec_authorization.ComCoreosMonitoringV1PrometheusSpecAuthorization()  # noqa: E501
        if include_optional :
            return ComCoreosMonitoringV1PrometheusSpecAuthorization(
                credentials = kubernetes.client.models.com_coreos_monitoring_v1_pod_monitor_spec_authorization_credentials.com_coreos_monitoring_v1_PodMonitor_spec_authorization_credentials(
                    key = '0', 
                    name = '0', 
                    optional = True, ), 
                credentials_file = '0', 
                type = '0'
            )
        else :
            return ComCoreosMonitoringV1PrometheusSpecAuthorization(
        )

    def testComCoreosMonitoringV1PrometheusSpecAuthorization(self):
        """Test ComCoreosMonitoringV1PrometheusSpecAuthorization"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
