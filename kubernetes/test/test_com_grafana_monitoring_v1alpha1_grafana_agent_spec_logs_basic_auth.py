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
from kubernetes.client.models.com_grafana_monitoring_v1alpha1_grafana_agent_spec_logs_basic_auth import ComGrafanaMonitoringV1alpha1GrafanaAgentSpecLogsBasicAuth  # noqa: E501
from kubernetes.client.rest import ApiException

class TestComGrafanaMonitoringV1alpha1GrafanaAgentSpecLogsBasicAuth(unittest.TestCase):
    """ComGrafanaMonitoringV1alpha1GrafanaAgentSpecLogsBasicAuth unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ComGrafanaMonitoringV1alpha1GrafanaAgentSpecLogsBasicAuth
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.com_grafana_monitoring_v1alpha1_grafana_agent_spec_logs_basic_auth.ComGrafanaMonitoringV1alpha1GrafanaAgentSpecLogsBasicAuth()  # noqa: E501
        if include_optional :
            return ComGrafanaMonitoringV1alpha1GrafanaAgentSpecLogsBasicAuth(
                password = kubernetes.client.models.com_coreos_monitoring_v1_pod_monitor_spec_basic_auth_password.com_coreos_monitoring_v1_PodMonitor_spec_basicAuth_password(
                    key = '0', 
                    name = '0', 
                    optional = True, ), 
                username = kubernetes.client.models.com_coreos_monitoring_v1_pod_monitor_spec_basic_auth_username.com_coreos_monitoring_v1_PodMonitor_spec_basicAuth_username(
                    key = '0', 
                    name = '0', 
                    optional = True, )
            )
        else :
            return ComGrafanaMonitoringV1alpha1GrafanaAgentSpecLogsBasicAuth(
        )

    def testComGrafanaMonitoringV1alpha1GrafanaAgentSpecLogsBasicAuth(self):
        """Test ComGrafanaMonitoringV1alpha1GrafanaAgentSpecLogsBasicAuth"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
