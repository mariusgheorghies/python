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
from kubernetes.client.models.com_grafana_monitoring_v1alpha1_grafana_agent_spec_gce_persistent_disk import ComGrafanaMonitoringV1alpha1GrafanaAgentSpecGcePersistentDisk  # noqa: E501
from kubernetes.client.rest import ApiException

class TestComGrafanaMonitoringV1alpha1GrafanaAgentSpecGcePersistentDisk(unittest.TestCase):
    """ComGrafanaMonitoringV1alpha1GrafanaAgentSpecGcePersistentDisk unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ComGrafanaMonitoringV1alpha1GrafanaAgentSpecGcePersistentDisk
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.com_grafana_monitoring_v1alpha1_grafana_agent_spec_gce_persistent_disk.ComGrafanaMonitoringV1alpha1GrafanaAgentSpecGcePersistentDisk()  # noqa: E501
        if include_optional :
            return ComGrafanaMonitoringV1alpha1GrafanaAgentSpecGcePersistentDisk(
                fs_type = '0', 
                partition = 56, 
                pd_name = '0', 
                read_only = True
            )
        else :
            return ComGrafanaMonitoringV1alpha1GrafanaAgentSpecGcePersistentDisk(
                pd_name = '0',
        )

    def testComGrafanaMonitoringV1alpha1GrafanaAgentSpecGcePersistentDisk(self):
        """Test ComGrafanaMonitoringV1alpha1GrafanaAgentSpecGcePersistentDisk"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()