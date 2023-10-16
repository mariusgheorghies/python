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
from kubernetes.client.models.io_external_secrets_v1alpha1_cluster_secret_store_spec_provider_gcpsm_auth import IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderGcpsmAuth  # noqa: E501
from kubernetes.client.rest import ApiException

class TestIoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderGcpsmAuth(unittest.TestCase):
    """IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderGcpsmAuth unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderGcpsmAuth
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.io_external_secrets_v1alpha1_cluster_secret_store_spec_provider_gcpsm_auth.IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderGcpsmAuth()  # noqa: E501
        if include_optional :
            return IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderGcpsmAuth(
                secret_ref = kubernetes.client.models.io_external_secrets_generators_v1alpha1_gcr_access_token_spec_auth_secret_ref.io_external_secrets_generators_v1alpha1_GCRAccessToken_spec_auth_secretRef(
                    secret_access_key_secret_ref = kubernetes.client.models.io_external_secrets_generators_v1alpha1_ecr_authorization_token_spec_auth_secret_ref_secret_access_key_secret_ref.io_external_secrets_generators_v1alpha1_ECRAuthorizationToken_spec_auth_secretRef_secretAccessKeySecretRef(
                        key = '0', 
                        name = '0', 
                        namespace = '0', ), ), 
                workload_identity = kubernetes.client.models.io_external_secrets_generators_v1alpha1_gcr_access_token_spec_auth_workload_identity.io_external_secrets_generators_v1alpha1_GCRAccessToken_spec_auth_workloadIdentity(
                    cluster_location = '0', 
                    cluster_name = '0', 
                    cluster_project_id = '0', 
                    service_account_ref = kubernetes.client.models.io_external_secrets_generators_v1alpha1_ecr_authorization_token_spec_auth_jwt_service_account_ref.io_external_secrets_generators_v1alpha1_ECRAuthorizationToken_spec_auth_jwt_serviceAccountRef(
                        audiences = [
                            '0'
                            ], 
                        name = '0', 
                        namespace = '0', ), )
            )
        else :
            return IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderGcpsmAuth(
        )

    def testIoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderGcpsmAuth(self):
        """Test IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderGcpsmAuth"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
