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
from kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_downward_api_items import ComCoreosMonitoringV1AlertmanagerSpecDownwardAPIItems  # noqa: E501
from kubernetes.client.rest import ApiException

class TestComCoreosMonitoringV1AlertmanagerSpecDownwardAPIItems(unittest.TestCase):
    """ComCoreosMonitoringV1AlertmanagerSpecDownwardAPIItems unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ComCoreosMonitoringV1AlertmanagerSpecDownwardAPIItems
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_downward_api_items.ComCoreosMonitoringV1AlertmanagerSpecDownwardAPIItems()  # noqa: E501
        if include_optional :
            return ComCoreosMonitoringV1AlertmanagerSpecDownwardAPIItems(
                field_ref = kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_downward_api_field_ref.com_coreos_monitoring_v1_Alertmanager_spec_downwardAPI_fieldRef(
                    api_version = '0', 
                    field_path = '0', ), 
                mode = 56, 
                path = '0', 
                resource_field_ref = kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_downward_api_resource_field_ref.com_coreos_monitoring_v1_Alertmanager_spec_downwardAPI_resourceFieldRef(
                    container_name = '0', 
                    divisor = kubernetes.client.models.divisor.divisor(), 
                    resource = '0', )
            )
        else :
            return ComCoreosMonitoringV1AlertmanagerSpecDownwardAPIItems(
                path = '0',
        )

    def testComCoreosMonitoringV1AlertmanagerSpecDownwardAPIItems(self):
        """Test ComCoreosMonitoringV1AlertmanagerSpecDownwardAPIItems"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
