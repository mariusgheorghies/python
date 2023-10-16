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
from kubernetes.client.models.io_cert_manager_v1_cluster_issuer_spec_vault_auth_token_secret_ref import IoCertManagerV1ClusterIssuerSpecVaultAuthTokenSecretRef  # noqa: E501
from kubernetes.client.rest import ApiException

class TestIoCertManagerV1ClusterIssuerSpecVaultAuthTokenSecretRef(unittest.TestCase):
    """IoCertManagerV1ClusterIssuerSpecVaultAuthTokenSecretRef unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IoCertManagerV1ClusterIssuerSpecVaultAuthTokenSecretRef
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.io_cert_manager_v1_cluster_issuer_spec_vault_auth_token_secret_ref.IoCertManagerV1ClusterIssuerSpecVaultAuthTokenSecretRef()  # noqa: E501
        if include_optional :
            return IoCertManagerV1ClusterIssuerSpecVaultAuthTokenSecretRef(
                key = '0', 
                name = '0'
            )
        else :
            return IoCertManagerV1ClusterIssuerSpecVaultAuthTokenSecretRef(
                name = '0',
        )

    def testIoCertManagerV1ClusterIssuerSpecVaultAuthTokenSecretRef(self):
        """Test IoCertManagerV1ClusterIssuerSpecVaultAuthTokenSecretRef"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()