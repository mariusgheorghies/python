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
from kubernetes.client.models.io_external_secrets_v1alpha1_external_secret_spec_remote_ref import IoExternalSecretsV1alpha1ExternalSecretSpecRemoteRef  # noqa: E501
from kubernetes.client.rest import ApiException

class TestIoExternalSecretsV1alpha1ExternalSecretSpecRemoteRef(unittest.TestCase):
    """IoExternalSecretsV1alpha1ExternalSecretSpecRemoteRef unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IoExternalSecretsV1alpha1ExternalSecretSpecRemoteRef
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.io_external_secrets_v1alpha1_external_secret_spec_remote_ref.IoExternalSecretsV1alpha1ExternalSecretSpecRemoteRef()  # noqa: E501
        if include_optional :
            return IoExternalSecretsV1alpha1ExternalSecretSpecRemoteRef(
                conversion_strategy = '0', 
                key = '0', 
                _property = '0', 
                version = '0'
            )
        else :
            return IoExternalSecretsV1alpha1ExternalSecretSpecRemoteRef(
                key = '0',
        )

    def testIoExternalSecretsV1alpha1ExternalSecretSpecRemoteRef(self):
        """Test IoExternalSecretsV1alpha1ExternalSecretSpecRemoteRef"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()