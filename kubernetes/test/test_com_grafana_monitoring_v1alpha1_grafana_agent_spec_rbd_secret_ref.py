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
from kubernetes.client.models.com_grafana_monitoring_v1alpha1_grafana_agent_spec_rbd_secret_ref import ComGrafanaMonitoringV1alpha1GrafanaAgentSpecRbdSecretRef  # noqa: E501
from kubernetes.client.rest import ApiException

class TestComGrafanaMonitoringV1alpha1GrafanaAgentSpecRbdSecretRef(unittest.TestCase):
    """ComGrafanaMonitoringV1alpha1GrafanaAgentSpecRbdSecretRef unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ComGrafanaMonitoringV1alpha1GrafanaAgentSpecRbdSecretRef
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.com_grafana_monitoring_v1alpha1_grafana_agent_spec_rbd_secret_ref.ComGrafanaMonitoringV1alpha1GrafanaAgentSpecRbdSecretRef()  # noqa: E501
        if include_optional :
            return ComGrafanaMonitoringV1alpha1GrafanaAgentSpecRbdSecretRef(
                name = '0'
            )
        else :
            return ComGrafanaMonitoringV1alpha1GrafanaAgentSpecRbdSecretRef(
        )

    def testComGrafanaMonitoringV1alpha1GrafanaAgentSpecRbdSecretRef(self):
        """Test ComGrafanaMonitoringV1alpha1GrafanaAgentSpecRbdSecretRef"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
