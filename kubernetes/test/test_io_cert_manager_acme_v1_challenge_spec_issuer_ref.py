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
from kubernetes.client.models.io_cert_manager_acme_v1_challenge_spec_issuer_ref import IoCertManagerAcmeV1ChallengeSpecIssuerRef  # noqa: E501
from kubernetes.client.rest import ApiException

class TestIoCertManagerAcmeV1ChallengeSpecIssuerRef(unittest.TestCase):
    """IoCertManagerAcmeV1ChallengeSpecIssuerRef unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IoCertManagerAcmeV1ChallengeSpecIssuerRef
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.io_cert_manager_acme_v1_challenge_spec_issuer_ref.IoCertManagerAcmeV1ChallengeSpecIssuerRef()  # noqa: E501
        if include_optional :
            return IoCertManagerAcmeV1ChallengeSpecIssuerRef(
                group = '0', 
                kind = '0', 
                name = '0'
            )
        else :
            return IoCertManagerAcmeV1ChallengeSpecIssuerRef(
                name = '0',
        )

    def testIoCertManagerAcmeV1ChallengeSpecIssuerRef(self):
        """Test IoCertManagerAcmeV1ChallengeSpecIssuerRef"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
