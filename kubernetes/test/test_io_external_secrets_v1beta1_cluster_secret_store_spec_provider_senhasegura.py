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
from kubernetes.client.models.io_external_secrets_v1beta1_cluster_secret_store_spec_provider_senhasegura import IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderSenhasegura  # noqa: E501
from kubernetes.client.rest import ApiException

class TestIoExternalSecretsV1beta1ClusterSecretStoreSpecProviderSenhasegura(unittest.TestCase):
    """IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderSenhasegura unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderSenhasegura
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.io_external_secrets_v1beta1_cluster_secret_store_spec_provider_senhasegura.IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderSenhasegura()  # noqa: E501
        if include_optional :
            return IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderSenhasegura(
                auth = kubernetes.client.models.io_external_secrets_v1beta1_cluster_secret_store_spec_provider_senhasegura_auth.io_external_secrets_v1beta1_ClusterSecretStore_spec_provider_senhasegura_auth(
                    kubernetes.client_id = '0', 
                    kubernetes.client_secret_secret_ref = kubernetes.client.models.io_external_secrets_v1alpha1_cluster_secret_store_spec_provider_akeyless_auth_secret_ref_secret_ref_access_type.io_external_secrets_v1alpha1_ClusterSecretStore_spec_provider_akeyless_authSecretRef_secretRef_accessType(
                        key = '0', 
                        name = '0', 
                        namespace = '0', ), ), 
                ignore_ssl_certificate = True, 
                module = '0', 
                url = '0'
            )
        else :
            return IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderSenhasegura(
                auth = kubernetes.client.models.io_external_secrets_v1beta1_cluster_secret_store_spec_provider_senhasegura_auth.io_external_secrets_v1beta1_ClusterSecretStore_spec_provider_senhasegura_auth(
                    kubernetes.client_id = '0', 
                    kubernetes.client_secret_secret_ref = kubernetes.client.models.io_external_secrets_v1alpha1_cluster_secret_store_spec_provider_akeyless_auth_secret_ref_secret_ref_access_type.io_external_secrets_v1alpha1_ClusterSecretStore_spec_provider_akeyless_authSecretRef_secretRef_accessType(
                        key = '0', 
                        name = '0', 
                        namespace = '0', ), ),
                module = '0',
                url = '0',
        )

    def testIoExternalSecretsV1beta1ClusterSecretStoreSpecProviderSenhasegura(self):
        """Test IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderSenhasegura"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()