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
from kubernetes.client.models.io_external_secrets_generators_v1alpha1_acr_access_token import IoExternalSecretsGeneratorsV1alpha1ACRAccessToken  # noqa: E501
from kubernetes.client.rest import ApiException

class TestIoExternalSecretsGeneratorsV1alpha1ACRAccessToken(unittest.TestCase):
    """IoExternalSecretsGeneratorsV1alpha1ACRAccessToken unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IoExternalSecretsGeneratorsV1alpha1ACRAccessToken
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.io_external_secrets_generators_v1alpha1_acr_access_token.IoExternalSecretsGeneratorsV1alpha1ACRAccessToken()  # noqa: E501
        if include_optional :
            return IoExternalSecretsGeneratorsV1alpha1ACRAccessToken(
                api_version = '0', 
                kind = '0', 
                metadata = kubernetes.client.models.v1/object_meta.v1.ObjectMeta(
                    annotations = {
                        'key' : '0'
                        }, 
                    creation_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    deletion_grace_period_seconds = 56, 
                    deletion_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    finalizers = [
                        '0'
                        ], 
                    generate_name = '0', 
                    generation = 56, 
                    labels = {
                        'key' : '0'
                        }, 
                    managed_fields = [
                        kubernetes.client.models.v1/managed_fields_entry.v1.ManagedFieldsEntry(
                            api_version = '0', 
                            fields_type = '0', 
                            fields_v1 = kubernetes.client.models.fields_v1.fieldsV1(), 
                            manager = '0', 
                            operation = '0', 
                            subresource = '0', 
                            time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                        ], 
                    name = '0', 
                    namespace = '0', 
                    owner_references = [
                        kubernetes.client.models.v1/owner_reference.v1.OwnerReference(
                            api_version = '0', 
                            block_owner_deletion = True, 
                            controller = True, 
                            kind = '0', 
                            name = '0', 
                            uid = '0', )
                        ], 
                    resource_version = '0', 
                    self_link = '0', 
                    uid = '0', ), 
                spec = kubernetes.client.models.io_external_secrets_generators_v1alpha1_acr_access_token_spec.io_external_secrets_generators_v1alpha1_ACRAccessToken_spec(
                    auth = kubernetes.client.models.io_external_secrets_generators_v1alpha1_acr_access_token_spec_auth.io_external_secrets_generators_v1alpha1_ACRAccessToken_spec_auth(
                        managed_identity = kubernetes.client.models.io_external_secrets_generators_v1alpha1_acr_access_token_spec_auth_managed_identity.io_external_secrets_generators_v1alpha1_ACRAccessToken_spec_auth_managedIdentity(
                            identity_id = '0', ), 
                        service_principal = kubernetes.client.models.io_external_secrets_generators_v1alpha1_acr_access_token_spec_auth_service_principal.io_external_secrets_generators_v1alpha1_ACRAccessToken_spec_auth_servicePrincipal(
                            secret_ref = kubernetes.client.models.io_external_secrets_generators_v1alpha1_acr_access_token_spec_auth_service_principal_secret_ref.io_external_secrets_generators_v1alpha1_ACRAccessToken_spec_auth_servicePrincipal_secretRef(
                                kubernetes.client_id = kubernetes.client.models.io_external_secrets_generators_v1alpha1_acr_access_token_spec_auth_service_principal_secret_ref_client_id.io_external_secrets_generators_v1alpha1_ACRAccessToken_spec_auth_servicePrincipal_secretRef_clientId(
                                    key = '0', 
                                    name = '0', 
                                    namespace = '0', ), 
                                kubernetes.client_secret = kubernetes.client.models.io_external_secrets_generators_v1alpha1_acr_access_token_spec_auth_service_principal_secret_ref_client_secret.io_external_secrets_generators_v1alpha1_ACRAccessToken_spec_auth_servicePrincipal_secretRef_clientSecret(
                                    key = '0', 
                                    name = '0', 
                                    namespace = '0', ), ), ), 
                        workload_identity = kubernetes.client.models.io_external_secrets_generators_v1alpha1_acr_access_token_spec_auth_workload_identity.io_external_secrets_generators_v1alpha1_ACRAccessToken_spec_auth_workloadIdentity(
                            service_account_ref = kubernetes.client.models.io_external_secrets_generators_v1alpha1_acr_access_token_spec_auth_workload_identity_service_account_ref.io_external_secrets_generators_v1alpha1_ACRAccessToken_spec_auth_workloadIdentity_serviceAccountRef(
                                audiences = [
                                    '0'
                                    ], 
                                name = '0', 
                                namespace = '0', ), ), ), 
                    environment_type = 'PublicCloud', 
                    registry = '0', 
                    scope = '0', 
                    tenant_id = '0', )
            )
        else :
            return IoExternalSecretsGeneratorsV1alpha1ACRAccessToken(
        )

    def testIoExternalSecretsGeneratorsV1alpha1ACRAccessToken(self):
        """Test IoExternalSecretsGeneratorsV1alpha1ACRAccessToken"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
