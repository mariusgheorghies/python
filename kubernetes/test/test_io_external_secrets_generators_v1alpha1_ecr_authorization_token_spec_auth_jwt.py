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
from kubernetes.client.models.io_external_secrets_generators_v1alpha1_ecr_authorization_token_spec_auth_jwt import IoExternalSecretsGeneratorsV1alpha1ECRAuthorizationTokenSpecAuthJwt  # noqa: E501
from kubernetes.client.rest import ApiException

class TestIoExternalSecretsGeneratorsV1alpha1ECRAuthorizationTokenSpecAuthJwt(unittest.TestCase):
    """IoExternalSecretsGeneratorsV1alpha1ECRAuthorizationTokenSpecAuthJwt unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IoExternalSecretsGeneratorsV1alpha1ECRAuthorizationTokenSpecAuthJwt
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.io_external_secrets_generators_v1alpha1_ecr_authorization_token_spec_auth_jwt.IoExternalSecretsGeneratorsV1alpha1ECRAuthorizationTokenSpecAuthJwt()  # noqa: E501
        if include_optional :
            return IoExternalSecretsGeneratorsV1alpha1ECRAuthorizationTokenSpecAuthJwt(
                service_account_ref = kubernetes.client.models.io_external_secrets_generators_v1alpha1_ecr_authorization_token_spec_auth_jwt_service_account_ref.io_external_secrets_generators_v1alpha1_ECRAuthorizationToken_spec_auth_jwt_serviceAccountRef(
                    audiences = [
                        '0'
                        ], 
                    name = '0', 
                    namespace = '0', )
            )
        else :
            return IoExternalSecretsGeneratorsV1alpha1ECRAuthorizationTokenSpecAuthJwt(
        )

    def testIoExternalSecretsGeneratorsV1alpha1ECRAuthorizationTokenSpecAuthJwt(self):
        """Test IoExternalSecretsGeneratorsV1alpha1ECRAuthorizationTokenSpecAuthJwt"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
