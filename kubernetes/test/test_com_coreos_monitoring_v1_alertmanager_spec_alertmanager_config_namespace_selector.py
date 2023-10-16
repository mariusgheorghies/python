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
from kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_alertmanager_config_namespace_selector import ComCoreosMonitoringV1AlertmanagerSpecAlertmanagerConfigNamespaceSelector  # noqa: E501
from kubernetes.client.rest import ApiException

class TestComCoreosMonitoringV1AlertmanagerSpecAlertmanagerConfigNamespaceSelector(unittest.TestCase):
    """ComCoreosMonitoringV1AlertmanagerSpecAlertmanagerConfigNamespaceSelector unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ComCoreosMonitoringV1AlertmanagerSpecAlertmanagerConfigNamespaceSelector
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_alertmanager_config_namespace_selector.ComCoreosMonitoringV1AlertmanagerSpecAlertmanagerConfigNamespaceSelector()  # noqa: E501
        if include_optional :
            return ComCoreosMonitoringV1AlertmanagerSpecAlertmanagerConfigNamespaceSelector(
                match_expressions = [
                    kubernetes.client.models.aws_k8s_networking_v1alpha1_policy_endpoint_spec_pod_selector_match_expressions.aws_k8s_networking_v1alpha1_PolicyEndpoint_spec_podSelector_matchExpressions(
                        key = '0', 
                        operator = '0', 
                        values = [
                            '0'
                            ], )
                    ], 
                match_labels = {
                    'key' : '0'
                    }
            )
        else :
            return ComCoreosMonitoringV1AlertmanagerSpecAlertmanagerConfigNamespaceSelector(
        )

    def testComCoreosMonitoringV1AlertmanagerSpecAlertmanagerConfigNamespaceSelector(self):
        """Test ComCoreosMonitoringV1AlertmanagerSpecAlertmanagerConfigNamespaceSelector"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
