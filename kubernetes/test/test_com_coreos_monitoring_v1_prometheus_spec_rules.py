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
from kubernetes.client.models.com_coreos_monitoring_v1_prometheus_spec_rules import ComCoreosMonitoringV1PrometheusSpecRules  # noqa: E501
from kubernetes.client.rest import ApiException

class TestComCoreosMonitoringV1PrometheusSpecRules(unittest.TestCase):
    """ComCoreosMonitoringV1PrometheusSpecRules unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ComCoreosMonitoringV1PrometheusSpecRules
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.com_coreos_monitoring_v1_prometheus_spec_rules.ComCoreosMonitoringV1PrometheusSpecRules()  # noqa: E501
        if include_optional :
            return ComCoreosMonitoringV1PrometheusSpecRules(
                alert = kubernetes.client.models.com_coreos_monitoring_v1_prometheus_spec_rules_alert.com_coreos_monitoring_v1_Prometheus_spec_rules_alert(
                    for_grace_period = '0', 
                    for_outage_tolerance = '0', 
                    resend_delay = '0', )
            )
        else :
            return ComCoreosMonitoringV1PrometheusSpecRules(
        )

    def testComCoreosMonitoringV1PrometheusSpecRules(self):
        """Test ComCoreosMonitoringV1PrometheusSpecRules"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
