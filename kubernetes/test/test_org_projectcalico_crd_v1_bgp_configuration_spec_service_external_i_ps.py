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
from kubernetes.client.models.org_projectcalico_crd_v1_bgp_configuration_spec_service_external_i_ps import OrgProjectcalicoCrdV1BGPConfigurationSpecServiceExternalIPs  # noqa: E501
from kubernetes.client.rest import ApiException

class TestOrgProjectcalicoCrdV1BGPConfigurationSpecServiceExternalIPs(unittest.TestCase):
    """OrgProjectcalicoCrdV1BGPConfigurationSpecServiceExternalIPs unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test OrgProjectcalicoCrdV1BGPConfigurationSpecServiceExternalIPs
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.org_projectcalico_crd_v1_bgp_configuration_spec_service_external_i_ps.OrgProjectcalicoCrdV1BGPConfigurationSpecServiceExternalIPs()  # noqa: E501
        if include_optional :
            return OrgProjectcalicoCrdV1BGPConfigurationSpecServiceExternalIPs(
                cidr = '0'
            )
        else :
            return OrgProjectcalicoCrdV1BGPConfigurationSpecServiceExternalIPs(
        )

    def testOrgProjectcalicoCrdV1BGPConfigurationSpecServiceExternalIPs(self):
        """Test OrgProjectcalicoCrdV1BGPConfigurationSpecServiceExternalIPs"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()