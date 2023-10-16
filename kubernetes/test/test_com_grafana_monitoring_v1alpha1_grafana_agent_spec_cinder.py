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
from kubernetes.client.models.com_grafana_monitoring_v1alpha1_grafana_agent_spec_cinder import ComGrafanaMonitoringV1alpha1GrafanaAgentSpecCinder  # noqa: E501
from kubernetes.client.rest import ApiException

class TestComGrafanaMonitoringV1alpha1GrafanaAgentSpecCinder(unittest.TestCase):
    """ComGrafanaMonitoringV1alpha1GrafanaAgentSpecCinder unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ComGrafanaMonitoringV1alpha1GrafanaAgentSpecCinder
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.com_grafana_monitoring_v1alpha1_grafana_agent_spec_cinder.ComGrafanaMonitoringV1alpha1GrafanaAgentSpecCinder()  # noqa: E501
        if include_optional :
            return ComGrafanaMonitoringV1alpha1GrafanaAgentSpecCinder(
                fs_type = '0', 
                read_only = True, 
                secret_ref = kubernetes.client.models.com_grafana_monitoring_v1alpha1_grafana_agent_spec_cinder_secret_ref.com_grafana_monitoring_v1alpha1_GrafanaAgent_spec_cinder_secretRef(
                    name = '0', ), 
                volume_id = '0'
            )
        else :
            return ComGrafanaMonitoringV1alpha1GrafanaAgentSpecCinder(
                volume_id = '0',
        )

    def testComGrafanaMonitoringV1alpha1GrafanaAgentSpecCinder(self):
        """Test ComGrafanaMonitoringV1alpha1GrafanaAgentSpecCinder"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()