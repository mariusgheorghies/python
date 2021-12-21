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
from kubernetes.client.models.io_cert_manager_acme_v1_challenge_status import IoCertManagerAcmeV1ChallengeStatus  # noqa: E501
from kubernetes.client.rest import ApiException

class TestIoCertManagerAcmeV1ChallengeStatus(unittest.TestCase):
    """IoCertManagerAcmeV1ChallengeStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IoCertManagerAcmeV1ChallengeStatus
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.io_cert_manager_acme_v1_challenge_status.IoCertManagerAcmeV1ChallengeStatus()  # noqa: E501
        if include_optional :
            return IoCertManagerAcmeV1ChallengeStatus(
                presented = True, 
                processing = True, 
                reason = '0', 
                state = 'valid'
            )
        else :
            return IoCertManagerAcmeV1ChallengeStatus(
        )

    def testIoCertManagerAcmeV1ChallengeStatus(self):
        """Test IoCertManagerAcmeV1ChallengeStatus"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
