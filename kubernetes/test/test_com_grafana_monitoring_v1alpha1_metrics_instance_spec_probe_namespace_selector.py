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
from kubernetes.client.models.com_grafana_monitoring_v1alpha1_metrics_instance_spec_probe_namespace_selector import ComGrafanaMonitoringV1alpha1MetricsInstanceSpecProbeNamespaceSelector  # noqa: E501
from kubernetes.client.rest import ApiException

class TestComGrafanaMonitoringV1alpha1MetricsInstanceSpecProbeNamespaceSelector(unittest.TestCase):
    """ComGrafanaMonitoringV1alpha1MetricsInstanceSpecProbeNamespaceSelector unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ComGrafanaMonitoringV1alpha1MetricsInstanceSpecProbeNamespaceSelector
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.com_grafana_monitoring_v1alpha1_metrics_instance_spec_probe_namespace_selector.ComGrafanaMonitoringV1alpha1MetricsInstanceSpecProbeNamespaceSelector()  # noqa: E501
        if include_optional :
            return ComGrafanaMonitoringV1alpha1MetricsInstanceSpecProbeNamespaceSelector(
                match_expressions = [
                    kubernetes.client.models.aws_k8s_networking_v1alpha1_policy_endpoint_spec_pod_selector_match_expressions.aws_k8s_networking_v1alpha1_PolicyEndpoint_spec_podSelector_matchExpressions(
                        key = '0', 
                        operator = '0', 
                        values = [
                            '0'
                            ], )
                    ], 
                match_labels = {
                    'key' : '0'
                    }
            )
        else :
            return ComGrafanaMonitoringV1alpha1MetricsInstanceSpecProbeNamespaceSelector(
        )

    def testComGrafanaMonitoringV1alpha1MetricsInstanceSpecProbeNamespaceSelector(self):
        """Test ComGrafanaMonitoringV1alpha1MetricsInstanceSpecProbeNamespaceSelector"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()