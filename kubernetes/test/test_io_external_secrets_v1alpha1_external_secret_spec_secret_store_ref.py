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
from kubernetes.client.models.io_external_secrets_v1alpha1_external_secret_spec_secret_store_ref import IoExternalSecretsV1alpha1ExternalSecretSpecSecretStoreRef  # noqa: E501
from kubernetes.client.rest import ApiException

class TestIoExternalSecretsV1alpha1ExternalSecretSpecSecretStoreRef(unittest.TestCase):
    """IoExternalSecretsV1alpha1ExternalSecretSpecSecretStoreRef unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IoExternalSecretsV1alpha1ExternalSecretSpecSecretStoreRef
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.io_external_secrets_v1alpha1_external_secret_spec_secret_store_ref.IoExternalSecretsV1alpha1ExternalSecretSpecSecretStoreRef()  # noqa: E501
        if include_optional :
            return IoExternalSecretsV1alpha1ExternalSecretSpecSecretStoreRef(
                kind = '0', 
                name = '0'
            )
        else :
            return IoExternalSecretsV1alpha1ExternalSecretSpecSecretStoreRef(
                name = '0',
        )

    def testIoExternalSecretsV1alpha1ExternalSecretSpecSecretStoreRef(self):
        """Test IoExternalSecretsV1alpha1ExternalSecretSpecSecretStoreRef"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
