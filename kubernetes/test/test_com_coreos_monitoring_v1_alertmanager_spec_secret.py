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
from kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_secret import ComCoreosMonitoringV1AlertmanagerSpecSecret  # noqa: E501
from kubernetes.client.rest import ApiException

class TestComCoreosMonitoringV1AlertmanagerSpecSecret(unittest.TestCase):
    """ComCoreosMonitoringV1AlertmanagerSpecSecret unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ComCoreosMonitoringV1AlertmanagerSpecSecret
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_secret.ComCoreosMonitoringV1AlertmanagerSpecSecret()  # noqa: E501
        if include_optional :
            return ComCoreosMonitoringV1AlertmanagerSpecSecret(
                default_mode = 56, 
                items = [
                    kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_config_map_items.com_coreos_monitoring_v1_Alertmanager_spec_configMap_items(
                        key = '0', 
                        mode = 56, 
                        path = '0', )
                    ], 
                optional = True, 
                secret_name = '0'
            )
        else :
            return ComCoreosMonitoringV1AlertmanagerSpecSecret(
        )

    def testComCoreosMonitoringV1AlertmanagerSpecSecret(self):
        """Test ComCoreosMonitoringV1AlertmanagerSpecSecret"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()