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
from kubernetes.client.models.io_external_secrets_v1alpha1_cluster_secret_store_spec_provider_aws import IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderAws  # noqa: E501
from kubernetes.client.rest import ApiException

class TestIoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderAws(unittest.TestCase):
    """IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderAws unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderAws
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.io_external_secrets_v1alpha1_cluster_secret_store_spec_provider_aws.IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderAws()  # noqa: E501
        if include_optional :
            return IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderAws(
                auth = kubernetes.client.models.io_external_secrets_v1alpha1_cluster_secret_store_spec_provider_aws_auth.io_external_secrets_v1alpha1_ClusterSecretStore_spec_provider_aws_auth(
                    jwt = kubernetes.client.models.io_external_secrets_generators_v1alpha1_ecr_authorization_token_spec_auth_jwt.io_external_secrets_generators_v1alpha1_ECRAuthorizationToken_spec_auth_jwt(
                        service_account_ref = kubernetes.client.models.io_external_secrets_generators_v1alpha1_ecr_authorization_token_spec_auth_jwt_service_account_ref.io_external_secrets_generators_v1alpha1_ECRAuthorizationToken_spec_auth_jwt_serviceAccountRef(
                            audiences = [
                                '0'
                                ], 
                            name = '0', 
                            namespace = '0', ), ), 
                    secret_ref = kubernetes.client.models.io_external_secrets_v1alpha1_cluster_secret_store_spec_provider_aws_auth_secret_ref.io_external_secrets_v1alpha1_ClusterSecretStore_spec_provider_aws_auth_secretRef(
                        access_key_id_secret_ref = kubernetes.client.models.io_external_secrets_generators_v1alpha1_ecr_authorization_token_spec_auth_secret_ref_access_key_id_secret_ref.io_external_secrets_generators_v1alpha1_ECRAuthorizationToken_spec_auth_secretRef_accessKeyIDSecretRef(
                            key = '0', 
                            name = '0', 
                            namespace = '0', ), 
                        secret_access_key_secret_ref = kubernetes.client.models.io_external_secrets_generators_v1alpha1_ecr_authorization_token_spec_auth_secret_ref_secret_access_key_secret_ref.io_external_secrets_generators_v1alpha1_ECRAuthorizationToken_spec_auth_secretRef_secretAccessKeySecretRef(
                            key = '0', 
                            name = '0', 
                            namespace = '0', ), ), ), 
                region = '0', 
                role = '0', 
                service = 'SecretsManager'
            )
        else :
            return IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderAws(
                region = '0',
                service = 'SecretsManager',
        )

    def testIoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderAws(self):
        """Test IoExternalSecretsV1alpha1ClusterSecretStoreSpecProviderAws"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
