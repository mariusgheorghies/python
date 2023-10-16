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
from kubernetes.client.models.org_projectcalico_crd_v1_bgp_peer_spec_password import OrgProjectcalicoCrdV1BGPPeerSpecPassword  # noqa: E501
from kubernetes.client.rest import ApiException

class TestOrgProjectcalicoCrdV1BGPPeerSpecPassword(unittest.TestCase):
    """OrgProjectcalicoCrdV1BGPPeerSpecPassword unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test OrgProjectcalicoCrdV1BGPPeerSpecPassword
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.org_projectcalico_crd_v1_bgp_peer_spec_password.OrgProjectcalicoCrdV1BGPPeerSpecPassword()  # noqa: E501
        if include_optional :
            return OrgProjectcalicoCrdV1BGPPeerSpecPassword(
                secret_key_ref = kubernetes.client.models.org_projectcalico_crd_v1_bgp_peer_spec_password_secret_key_ref.org_projectcalico_crd_v1_BGPPeer_spec_password_secretKeyRef(
                    key = '0', 
                    name = '0', 
                    optional = True, )
            )
        else :
            return OrgProjectcalicoCrdV1BGPPeerSpecPassword(
        )

    def testOrgProjectcalicoCrdV1BGPPeerSpecPassword(self):
        """Test OrgProjectcalicoCrdV1BGPPeerSpecPassword"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
