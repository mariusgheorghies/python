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
from kubernetes.client.models.io_cert_manager_acme_v1_challenge_spec_solver_dns01_cloudflare_api_key_secret_ref import IoCertManagerAcmeV1ChallengeSpecSolverDns01CloudflareApiKeySecretRef  # noqa: E501
from kubernetes.client.rest import ApiException

class TestIoCertManagerAcmeV1ChallengeSpecSolverDns01CloudflareApiKeySecretRef(unittest.TestCase):
    """IoCertManagerAcmeV1ChallengeSpecSolverDns01CloudflareApiKeySecretRef unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IoCertManagerAcmeV1ChallengeSpecSolverDns01CloudflareApiKeySecretRef
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.io_cert_manager_acme_v1_challenge_spec_solver_dns01_cloudflare_api_key_secret_ref.IoCertManagerAcmeV1ChallengeSpecSolverDns01CloudflareApiKeySecretRef()  # noqa: E501
        if include_optional :
            return IoCertManagerAcmeV1ChallengeSpecSolverDns01CloudflareApiKeySecretRef(
                key = '0', 
                name = '0'
            )
        else :
            return IoCertManagerAcmeV1ChallengeSpecSolverDns01CloudflareApiKeySecretRef(
                name = '0',
        )

    def testIoCertManagerAcmeV1ChallengeSpecSolverDns01CloudflareApiKeySecretRef(self):
        """Test IoCertManagerAcmeV1ChallengeSpecSolverDns01CloudflareApiKeySecretRef"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
