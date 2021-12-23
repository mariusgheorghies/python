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
from kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_env_from import ComCoreosMonitoringV1AlertmanagerSpecEnvFrom  # noqa: E501
from kubernetes.client.rest import ApiException

class TestComCoreosMonitoringV1AlertmanagerSpecEnvFrom(unittest.TestCase):
    """ComCoreosMonitoringV1AlertmanagerSpecEnvFrom unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ComCoreosMonitoringV1AlertmanagerSpecEnvFrom
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_env_from.ComCoreosMonitoringV1AlertmanagerSpecEnvFrom()  # noqa: E501
        if include_optional :
            return ComCoreosMonitoringV1AlertmanagerSpecEnvFrom(
                config_map_ref = kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_config_map_ref.com_coreos_monitoring_v1_Alertmanager_spec_configMapRef(
                    name = '0', 
                    optional = True, ), 
                prefix = '0', 
                secret_ref = kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_secret_ref.com_coreos_monitoring_v1_Alertmanager_spec_secretRef(
                    name = '0', 
                    optional = True, )
            )
        else :
            return ComCoreosMonitoringV1AlertmanagerSpecEnvFrom(
        )

    def testComCoreosMonitoringV1AlertmanagerSpecEnvFrom(self):
        """Test ComCoreosMonitoringV1AlertmanagerSpecEnvFrom"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
