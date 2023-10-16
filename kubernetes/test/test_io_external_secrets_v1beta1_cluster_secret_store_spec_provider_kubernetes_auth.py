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
from kubernetes.client.models.io_external_secrets_v1beta1_cluster_secret_store_spec_provider_kubernetes_auth import IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderKubernetesAuth  # noqa: E501
from kubernetes.client.rest import ApiException

class TestIoExternalSecretsV1beta1ClusterSecretStoreSpecProviderKubernetesAuth(unittest.TestCase):
    """IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderKubernetesAuth unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderKubernetesAuth
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.io_external_secrets_v1beta1_cluster_secret_store_spec_provider_kubernetes_auth.IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderKubernetesAuth()  # noqa: E501
        if include_optional :
            return IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderKubernetesAuth(
                cert = kubernetes.client.models.io_external_secrets_v1alpha1_cluster_secret_store_spec_provider_kubernetes_auth_cert.io_external_secrets_v1alpha1_ClusterSecretStore_spec_provider_kubernetes_auth_cert(
                    kubernetes.client_cert = kubernetes.client.models.io_external_secrets_v1alpha1_cluster_secret_store_spec_provider_akeyless_auth_secret_ref_secret_ref_access_type.io_external_secrets_v1alpha1_ClusterSecretStore_spec_provider_akeyless_authSecretRef_secretRef_accessType(
                        key = '0', 
                        name = '0', 
                        namespace = '0', ), 
                    kubernetes.client_key = kubernetes.client.models.io_external_secrets_v1alpha1_cluster_secret_store_spec_provider_akeyless_auth_secret_ref_secret_ref_access_type.io_external_secrets_v1alpha1_ClusterSecretStore_spec_provider_akeyless_authSecretRef_secretRef_accessType(
                        key = '0', 
                        name = '0', 
                        namespace = '0', ), ), 
                service_account = kubernetes.client.models.io_external_secrets_v1beta1_cluster_secret_store_spec_provider_kubernetes_auth_service_account.io_external_secrets_v1beta1_ClusterSecretStore_spec_provider_kubernetes_auth_serviceAccount(
                    audiences = [
                        '0'
                        ], 
                    name = '0', 
                    namespace = '0', ), 
                token = kubernetes.client.models.io_external_secrets_v1alpha1_cluster_secret_store_spec_provider_kubernetes_auth_token.io_external_secrets_v1alpha1_ClusterSecretStore_spec_provider_kubernetes_auth_token(
                    bearer_token = kubernetes.client.models.io_external_secrets_v1alpha1_cluster_secret_store_spec_provider_akeyless_auth_secret_ref_secret_ref_access_type.io_external_secrets_v1alpha1_ClusterSecretStore_spec_provider_akeyless_authSecretRef_secretRef_accessType(
                        key = '0', 
                        name = '0', 
                        namespace = '0', ), )
            )
        else :
            return IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderKubernetesAuth(
        )

    def testIoExternalSecretsV1beta1ClusterSecretStoreSpecProviderKubernetesAuth(self):
        """Test IoExternalSecretsV1beta1ClusterSecretStoreSpecProviderKubernetesAuth"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
