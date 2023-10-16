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
from kubernetes.client.models.com_coreos_monitoring_v1alpha1_alertmanager_config_spec_source_match import ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecSourceMatch  # noqa: E501
from kubernetes.client.rest import ApiException

class TestComCoreosMonitoringV1alpha1AlertmanagerConfigSpecSourceMatch(unittest.TestCase):
    """ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecSourceMatch unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecSourceMatch
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.com_coreos_monitoring_v1alpha1_alertmanager_config_spec_source_match.ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecSourceMatch()  # noqa: E501
        if include_optional :
            return ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecSourceMatch(
                match_type = '!=', 
                name = '0', 
                regex = True, 
                value = '0'
            )
        else :
            return ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecSourceMatch(
                name = '0',
        )

    def testComCoreosMonitoringV1alpha1AlertmanagerConfigSpecSourceMatch(self):
        """Test ComCoreosMonitoringV1alpha1AlertmanagerConfigSpecSourceMatch"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
