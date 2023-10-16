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
from kubernetes.client.models.sh_karpenter_v1alpha5_provisioner_status_conditions import ShKarpenterV1alpha5ProvisionerStatusConditions  # noqa: E501
from kubernetes.client.rest import ApiException

class TestShKarpenterV1alpha5ProvisionerStatusConditions(unittest.TestCase):
    """ShKarpenterV1alpha5ProvisionerStatusConditions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ShKarpenterV1alpha5ProvisionerStatusConditions
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.sh_karpenter_v1alpha5_provisioner_status_conditions.ShKarpenterV1alpha5ProvisionerStatusConditions()  # noqa: E501
        if include_optional :
            return ShKarpenterV1alpha5ProvisionerStatusConditions(
                last_transition_time = '0', 
                message = '0', 
                reason = '0', 
                severity = '0', 
                status = '0', 
                type = '0'
            )
        else :
            return ShKarpenterV1alpha5ProvisionerStatusConditions(
                status = '0',
                type = '0',
        )

    def testShKarpenterV1alpha5ProvisionerStatusConditions(self):
        """Test ShKarpenterV1alpha5ProvisionerStatusConditions"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
