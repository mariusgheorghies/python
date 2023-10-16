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
from kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_value_from_secret_key_ref import ComCoreosMonitoringV1AlertmanagerSpecValueFromSecretKeyRef  # noqa: E501
from kubernetes.client.rest import ApiException

class TestComCoreosMonitoringV1AlertmanagerSpecValueFromSecretKeyRef(unittest.TestCase):
    """ComCoreosMonitoringV1AlertmanagerSpecValueFromSecretKeyRef unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ComCoreosMonitoringV1AlertmanagerSpecValueFromSecretKeyRef
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_value_from_secret_key_ref.ComCoreosMonitoringV1AlertmanagerSpecValueFromSecretKeyRef()  # noqa: E501
        if include_optional :
            return ComCoreosMonitoringV1AlertmanagerSpecValueFromSecretKeyRef(
                key = '0', 
                name = '0', 
                optional = True
            )
        else :
            return ComCoreosMonitoringV1AlertmanagerSpecValueFromSecretKeyRef(
                key = '0',
        )

    def testComCoreosMonitoringV1AlertmanagerSpecValueFromSecretKeyRef(self):
        """Test ComCoreosMonitoringV1AlertmanagerSpecValueFromSecretKeyRef"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()