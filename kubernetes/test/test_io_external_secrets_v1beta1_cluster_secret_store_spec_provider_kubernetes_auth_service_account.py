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
from kubernetes.client.models.io_external_secrets_v1beta1_cluster_secret_store_spec_provider_kubernetes_auth_service_account import IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderKubernetesAuthServiceAccount  # noqa: E501
from kubernetes.client.rest import ApiException

class TestIoExternalSecretsV1beta1ClusterSecretStoreSpecProviderKubernetesAuthServiceAccount(unittest.TestCase):
    """IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderKubernetesAuthServiceAccount unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderKubernetesAuthServiceAccount
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.io_external_secrets_v1beta1_cluster_secret_store_spec_provider_kubernetes_auth_service_account.IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderKubernetesAuthServiceAccount()  # noqa: E501
        if include_optional :
            return IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderKubernetesAuthServiceAccount(
                audiences = [
                    '0'
                    ], 
                name = '0', 
                namespace = '0'
            )
        else :
            return IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderKubernetesAuthServiceAccount(
                name = '0',
        )

    def testIoExternalSecretsV1beta1ClusterSecretStoreSpecProviderKubernetesAuthServiceAccount(self):
        """Test IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderKubernetesAuthServiceAccount"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
