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
from kubernetes.client.models.io_external_secrets_generators_v1alpha1_vault_dynamic_secret_spec_provider_auth_ldap import IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderAuthLdap  # noqa: E501
from kubernetes.client.rest import ApiException

class TestIoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderAuthLdap(unittest.TestCase):
    """IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderAuthLdap unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderAuthLdap
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.io_external_secrets_generators_v1alpha1_vault_dynamic_secret_spec_provider_auth_ldap.IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderAuthLdap()  # noqa: E501
        if include_optional :
            return IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderAuthLdap(
                path = '0', 
                secret_ref = kubernetes.client.models.io_external_secrets_generators_v1alpha1_vault_dynamic_secret_spec_provider_auth_ldap_secret_ref.io_external_secrets_generators_v1alpha1_VaultDynamicSecret_spec_provider_auth_ldap_secretRef(
                    key = '0', 
                    name = '0', 
                    namespace = '0', ), 
                username = '0'
            )
        else :
            return IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderAuthLdap(
                path = '0',
                username = '0',
        )

    def testIoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderAuthLdap(self):
        """Test IoExternalSecretsGeneratorsV1alpha1VaultDynamicSecretSpecProviderAuthLdap"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
