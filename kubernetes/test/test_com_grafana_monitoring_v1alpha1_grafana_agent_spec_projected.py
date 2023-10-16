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
from kubernetes.client.models.com_grafana_monitoring_v1alpha1_grafana_agent_spec_projected import ComGrafanaMonitoringV1alpha1GrafanaAgentSpecProjected  # noqa: E501
from kubernetes.client.rest import ApiException

class TestComGrafanaMonitoringV1alpha1GrafanaAgentSpecProjected(unittest.TestCase):
    """ComGrafanaMonitoringV1alpha1GrafanaAgentSpecProjected unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ComGrafanaMonitoringV1alpha1GrafanaAgentSpecProjected
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.com_grafana_monitoring_v1alpha1_grafana_agent_spec_projected.ComGrafanaMonitoringV1alpha1GrafanaAgentSpecProjected()  # noqa: E501
        if include_optional :
            return ComGrafanaMonitoringV1alpha1GrafanaAgentSpecProjected(
                default_mode = 56, 
                sources = [
                    kubernetes.client.models.com_grafana_monitoring_v1alpha1_grafana_agent_spec_projected_sources.com_grafana_monitoring_v1alpha1_GrafanaAgent_spec_projected_sources(
                        config_map = kubernetes.client.models.com_grafana_monitoring_v1alpha1_grafana_agent_spec_projected_config_map.com_grafana_monitoring_v1alpha1_GrafanaAgent_spec_projected_configMap(
                            items = [
                                kubernetes.client.models.com_grafana_monitoring_v1alpha1_grafana_agent_spec_config_map_items.com_grafana_monitoring_v1alpha1_GrafanaAgent_spec_configMap_items(
                                    key = '0', 
                                    mode = 56, 
                                    path = '0', )
                                ], 
                            name = '0', 
                            optional = True, ), 
                        downward_api = kubernetes.client.models.com_grafana_monitoring_v1alpha1_grafana_agent_spec_projected_downward_api.com_grafana_monitoring_v1alpha1_GrafanaAgent_spec_projected_downwardAPI(), 
                        secret = kubernetes.client.models.com_grafana_monitoring_v1alpha1_grafana_agent_spec_projected_secret.com_grafana_monitoring_v1alpha1_GrafanaAgent_spec_projected_secret(
                            name = '0', 
                            optional = True, ), 
                        service_account_token = kubernetes.client.models.com_grafana_monitoring_v1alpha1_grafana_agent_spec_projected_service_account_token.com_grafana_monitoring_v1alpha1_GrafanaAgent_spec_projected_serviceAccountToken(
                            audience = '0', 
                            expiration_seconds = 56, 
                            path = '0', ), )
                    ]
            )
        else :
            return ComGrafanaMonitoringV1alpha1GrafanaAgentSpecProjected(
        )

    def testComGrafanaMonitoringV1alpha1GrafanaAgentSpecProjected(self):
        """Test ComGrafanaMonitoringV1alpha1GrafanaAgentSpecProjected"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()