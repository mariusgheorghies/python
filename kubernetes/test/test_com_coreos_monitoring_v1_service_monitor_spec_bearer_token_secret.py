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
from kubernetes.client.models.com_coreos_monitoring_v1_service_monitor_spec_bearer_token_secret import ComCoreosMonitoringV1ServiceMonitorSpecBearerTokenSecret  # noqa: E501
from kubernetes.client.rest import ApiException

class TestComCoreosMonitoringV1ServiceMonitorSpecBearerTokenSecret(unittest.TestCase):
    """ComCoreosMonitoringV1ServiceMonitorSpecBearerTokenSecret unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ComCoreosMonitoringV1ServiceMonitorSpecBearerTokenSecret
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.com_coreos_monitoring_v1_service_monitor_spec_bearer_token_secret.ComCoreosMonitoringV1ServiceMonitorSpecBearerTokenSecret()  # noqa: E501
        if include_optional :
            return ComCoreosMonitoringV1ServiceMonitorSpecBearerTokenSecret(
                key = '0', 
                name = '0', 
                optional = True
            )
        else :
            return ComCoreosMonitoringV1ServiceMonitorSpecBearerTokenSecret(
                key = '0',
        )

    def testComCoreosMonitoringV1ServiceMonitorSpecBearerTokenSecret(self):
        """Test ComCoreosMonitoringV1ServiceMonitorSpecBearerTokenSecret"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
