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
from kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_lifecycle_post_start_http_get_http_headers import ComCoreosMonitoringV1AlertmanagerSpecLifecyclePostStartHttpGetHttpHeaders  # noqa: E501
from kubernetes.client.rest import ApiException

class TestComCoreosMonitoringV1AlertmanagerSpecLifecyclePostStartHttpGetHttpHeaders(unittest.TestCase):
    """ComCoreosMonitoringV1AlertmanagerSpecLifecyclePostStartHttpGetHttpHeaders unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ComCoreosMonitoringV1AlertmanagerSpecLifecyclePostStartHttpGetHttpHeaders
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_lifecycle_post_start_http_get_http_headers.ComCoreosMonitoringV1AlertmanagerSpecLifecyclePostStartHttpGetHttpHeaders()  # noqa: E501
        if include_optional :
            return ComCoreosMonitoringV1AlertmanagerSpecLifecyclePostStartHttpGetHttpHeaders(
                name = '0', 
                value = '0'
            )
        else :
            return ComCoreosMonitoringV1AlertmanagerSpecLifecyclePostStartHttpGetHttpHeaders(
                name = '0',
                value = '0',
        )

    def testComCoreosMonitoringV1AlertmanagerSpecLifecyclePostStartHttpGetHttpHeaders(self):
        """Test ComCoreosMonitoringV1AlertmanagerSpecLifecyclePostStartHttpGetHttpHeaders"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
