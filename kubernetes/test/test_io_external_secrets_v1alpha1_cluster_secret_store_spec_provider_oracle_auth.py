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
from kubernetes.client.models.io_external_secrets_v1alpha1_cluster_secret_store_spec_provider_oracle_auth import IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderOracleAuth  # noqa: E501
from kubernetes.client.rest import ApiException

class TestIoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderOracleAuth(unittest.TestCase):
    """IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderOracleAuth unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderOracleAuth
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.io_external_secrets_v1alpha1_cluster_secret_store_spec_provider_oracle_auth.IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderOracleAuth()  # noqa: E501
        if include_optional :
            return IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderOracleAuth(
                secret_ref = kubernetes.client.models.io_external_secrets_v1alpha1_cluster_secret_store_spec_provider_oracle_auth_secret_ref.io_external_secrets_v1alpha1_ClusterSecretStore_spec_provider_oracle_auth_secretRef(
                    fingerprint = kubernetes.client.models.io_external_secrets_v1alpha1_cluster_secret_store_spec_provider_oracle_auth_secret_ref_fingerprint.io_external_secrets_v1alpha1_ClusterSecretStore_spec_provider_oracle_auth_secretRef_fingerprint(
                        key = '0', 
                        name = '0', 
                        namespace = '0', ), 
                    privatekey = kubernetes.client.models.io_external_secrets_v1alpha1_cluster_secret_store_spec_provider_oracle_auth_secret_ref_privatekey.io_external_secrets_v1alpha1_ClusterSecretStore_spec_provider_oracle_auth_secretRef_privatekey(
                        key = '0', 
                        name = '0', 
                        namespace = '0', ), ), 
                tenancy = '0', 
                user = '0'
            )
        else :
            return IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderOracleAuth(
                secret_ref = kubernetes.client.models.io_external_secrets_v1alpha1_cluster_secret_store_spec_provider_oracle_auth_secret_ref.io_external_secrets_v1alpha1_ClusterSecretStore_spec_provider_oracle_auth_secretRef(
                    fingerprint = kubernetes.client.models.io_external_secrets_v1alpha1_cluster_secret_store_spec_provider_oracle_auth_secret_ref_fingerprint.io_external_secrets_v1alpha1_ClusterSecretStore_spec_provider_oracle_auth_secretRef_fingerprint(
                        key = '0', 
                        name = '0', 
                        namespace = '0', ), 
                    privatekey = kubernetes.client.models.io_external_secrets_v1alpha1_cluster_secret_store_spec_provider_oracle_auth_secret_ref_privatekey.io_external_secrets_v1alpha1_ClusterSecretStore_spec_provider_oracle_auth_secretRef_privatekey(
                        key = '0', 
                        name = '0', 
                        namespace = '0', ), ),
                tenancy = '0',
                user = '0',
        )

    def testIoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderOracleAuth(self):
        """Test IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderOracleAuth"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
