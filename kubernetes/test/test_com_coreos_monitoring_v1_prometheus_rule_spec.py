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
from kubernetes.client.models.com_coreos_monitoring_v1_prometheus_rule_spec import ComCoreosMonitoringV1PrometheusRuleSpec  # noqa: E501
from kubernetes.client.rest import ApiException

class TestComCoreosMonitoringV1PrometheusRuleSpec(unittest.TestCase):
    """ComCoreosMonitoringV1PrometheusRuleSpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ComCoreosMonitoringV1PrometheusRuleSpec
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.com_coreos_monitoring_v1_prometheus_rule_spec.ComCoreosMonitoringV1PrometheusRuleSpec()  # noqa: E501
        if include_optional :
            return ComCoreosMonitoringV1PrometheusRuleSpec(
                groups = [
                    kubernetes.client.models.com_coreos_monitoring_v1_prometheus_rule_spec_groups.com_coreos_monitoring_v1_PrometheusRule_spec_groups(
                        interval = '0', 
                        name = '0', 
                        partial_response_strategy = '0', 
                        rules = [
                            kubernetes.client.models.com_coreos_monitoring_v1_prometheus_rule_spec_rules.com_coreos_monitoring_v1_PrometheusRule_spec_rules(
                                alert = '0', 
                                annotations = {
                                    'key' : '0'
                                    }, 
                                expr = kubernetes.client.models.expr.expr(), 
                                for = '0', 
                                labels = {
                                    'key' : '0'
                                    }, 
                                record = '0', )
                            ], )
                    ]
            )
        else :
            return ComCoreosMonitoringV1PrometheusRuleSpec(
        )

    def testComCoreosMonitoringV1PrometheusRuleSpec(self):
        """Test ComCoreosMonitoringV1PrometheusRuleSpec"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()