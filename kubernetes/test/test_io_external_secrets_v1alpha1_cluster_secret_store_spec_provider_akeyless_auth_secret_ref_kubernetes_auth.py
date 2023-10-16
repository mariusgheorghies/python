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
from kubernetes.client.models.io_external_secrets_v1alpha1_cluster_secret_store_spec_provider_akeyless_auth_secret_ref_kubernetes_auth import IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderAkeylessAuthSecretRefKubernetesAuth  # noqa: E501
from kubernetes.client.rest import ApiException

class TestIoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderAkeylessAuthSecretRefKubernetesAuth(unittest.TestCase):
    """IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderAkeylessAuthSecretRefKubernetesAuth unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderAkeylessAuthSecretRefKubernetesAuth
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.io_external_secrets_v1alpha1_cluster_secret_store_spec_provider_akeyless_auth_secret_ref_kubernetes_auth.IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderAkeylessAuthSecretRefKubernetesAuth()  # noqa: E501
        if include_optional :
            return IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderAkeylessAuthSecretRefKubernetesAuth(
                access_id = '0', 
                k8s_conf_name = '0', 
                secret_ref = kubernetes.client.models.io_external_secrets_v1alpha1_cluster_secret_store_spec_provider_akeyless_auth_secret_ref_kubernetes_auth_secret_ref.io_external_secrets_v1alpha1_ClusterSecretStore_spec_provider_akeyless_authSecretRef_kubernetesAuth_secretRef(
                    key = '0', 
                    name = '0', 
                    namespace = '0', ), 
                service_account_ref = kubernetes.client.models.io_external_secrets_v1alpha1_cluster_secret_store_spec_provider_akeyless_auth_secret_ref_kubernetes_auth_service_account_ref.io_external_secrets_v1alpha1_ClusterSecretStore_spec_provider_akeyless_authSecretRef_kubernetesAuth_serviceAccountRef(
                    audiences = [
                        '0'
                        ], 
                    name = '0', 
                    namespace = '0', )
            )
        else :
            return IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderAkeylessAuthSecretRefKubernetesAuth(
                access_id = '0',
                k8s_conf_name = '0',
        )

    def testIoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderAkeylessAuthSecretRefKubernetesAuth(self):
        """Test IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderAkeylessAuthSecretRefKubernetesAuth"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()