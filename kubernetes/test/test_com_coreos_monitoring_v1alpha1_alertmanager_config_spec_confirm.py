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
from kubernetes.client.models.com_coreos_monitoring_v1alpha1_alertmanager_config_spec_confirm import ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecConfirm  # noqa: E501
from kubernetes.client.rest import ApiException

class TestComCoreosMonitoringV1alpha1AlertmanagerConfigSpecConfirm(unittest.TestCase):
    """ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecConfirm unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecConfirm
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.com_coreos_monitoring_v1alpha1_alertmanager_config_spec_confirm.ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecConfirm()  # noqa: E501
        if include_optional :
            return ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecConfirm(
                dismiss_text = '0', 
                ok_text = '0', 
                text = '0', 
                title = '0'
            )
        else :
            return ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecConfirm(
                text = '0',
        )

    def testComCoreosMonitoringV1alpha1AlertmanagerConfigSpecConfirm(self):
        """Test ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecConfirm"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
