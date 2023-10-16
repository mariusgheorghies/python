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
from kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_fc import ComCoreosMonitoringV1AlertmanagerSpecFc  # noqa: E501
from kubernetes.client.rest import ApiException

class TestComCoreosMonitoringV1AlertmanagerSpecFc(unittest.TestCase):
    """ComCoreosMonitoringV1AlertmanagerSpecFc unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ComCoreosMonitoringV1AlertmanagerSpecFc
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_fc.ComCoreosMonitoringV1AlertmanagerSpecFc()  # noqa: E501
        if include_optional :
            return ComCoreosMonitoringV1AlertmanagerSpecFc(
                fs_type = '0', 
                lun = 56, 
                read_only = True, 
                target_ww_ns = [
                    '0'
                    ], 
                wwids = [
                    '0'
                    ]
            )
        else :
            return ComCoreosMonitoringV1AlertmanagerSpecFc(
        )

    def testComCoreosMonitoringV1AlertmanagerSpecFc(self):
        """Test ComCoreosMonitoringV1AlertmanagerSpecFc"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()