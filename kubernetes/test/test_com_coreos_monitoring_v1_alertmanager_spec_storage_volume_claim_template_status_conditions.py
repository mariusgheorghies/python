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
from kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_storage_volume_claim_template_status_conditions import ComCoreosMonitoringV1AlertmanagerSpecStorageVolumeClaimTemplateStatusConditions  # noqa: E501
from kubernetes.client.rest import ApiException

class TestComCoreosMonitoringV1AlertmanagerSpecStorageVolumeClaimTemplateStatusConditions(unittest.TestCase):
    """ComCoreosMonitoringV1AlertmanagerSpecStorageVolumeClaimTemplateStatusConditions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ComCoreosMonitoringV1AlertmanagerSpecStorageVolumeClaimTemplateStatusConditions
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.com_coreos_monitoring_v1_alertmanager_spec_storage_volume_claim_template_status_conditions.ComCoreosMonitoringV1AlertmanagerSpecStorageVolumeClaimTemplateStatusConditions()  # noqa: E501
        if include_optional :
            return ComCoreosMonitoringV1AlertmanagerSpecStorageVolumeClaimTemplateStatusConditions(
                last_probe_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                last_transition_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                message = '0', 
                reason = '0', 
                status = '0', 
                type = '0'
            )
        else :
            return ComCoreosMonitoringV1AlertmanagerSpecStorageVolumeClaimTemplateStatusConditions(
                status = '0',
                type = '0',
        )

    def testComCoreosMonitoringV1AlertmanagerSpecStorageVolumeClaimTemplateStatusConditions(self):
        """Test ComCoreosMonitoringV1AlertmanagerSpecStorageVolumeClaimTemplateStatusConditions"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
