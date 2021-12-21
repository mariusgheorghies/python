# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import kubernetes.client
from kubernetes.client.models.authentication_v1_token_request import AuthenticationV1TokenRequest  # noqa: E501
from kubernetes.client.rest import ApiException

class TestAuthenticationV1TokenRequest(unittest.TestCase):
    """AuthenticationV1TokenRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AuthenticationV1TokenRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.authentication_v1_token_request.AuthenticationV1TokenRequest()  # noqa: E501
        if include_optional :
            return AuthenticationV1TokenRequest(
                api_version = '0', 
                kind = '0', 
                metadata = kubernetes.client.models.v1/object_meta.v1.ObjectMeta(
                    annotations = {
                        'key' : '0'
                        }, 
                    cluster_name = '0', 
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
                spec = kubernetes.client.models.v1/token_request_spec.v1.TokenRequestSpec(
                    audiences = [
                        '0'
                        ], 
                    bound_object_ref = kubernetes.client.models.v1/bound_object_reference.v1.BoundObjectReference(
                        api_version = '0', 
                        kind = '0', 
                        name = '0', 
                        uid = '0', ), 
                    expiration_seconds = 56, ), 
                status = kubernetes.client.models.v1/token_request_status.v1.TokenRequestStatus(
                    expiration_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    token = '0', )
            )
        else :
            return AuthenticationV1TokenRequest(
                spec = kubernetes.client.models.v1/token_request_spec.v1.TokenRequestSpec(
                    audiences = [
                        '0'
                        ], 
                    bound_object_ref = kubernetes.client.models.v1/bound_object_reference.v1.BoundObjectReference(
                        api_version = '0', 
                        kind = '0', 
                        name = '0', 
                        uid = '0', ), 
                    expiration_seconds = 56, ),
        )

    def testAuthenticationV1TokenRequest(self):
        """Test AuthenticationV1TokenRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
