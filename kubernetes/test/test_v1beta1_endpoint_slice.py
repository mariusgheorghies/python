# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.20.7
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import kubernetes.client
from kubernetes.client.models.v1beta1_endpoint_slice import V1beta1EndpointSlice  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1beta1EndpointSlice(unittest.TestCase):
    """V1beta1EndpointSlice unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1beta1EndpointSlice
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1beta1_endpoint_slice.V1beta1EndpointSlice()  # noqa: E501
        if include_optional :
            return V1beta1EndpointSlice(
                address_type = '0', 
                api_version = '0', 
                endpoints = [
                    kubernetes.client.models.v1beta1/endpoint.v1beta1.Endpoint(
                        addresses = [
                            '0'
                            ], 
                        conditions = kubernetes.client.models.v1beta1/endpoint_conditions.v1beta1.EndpointConditions(
                            ready = True, 
                            serving = True, 
                            terminating = True, ), 
                        hostname = '0', 
                        node_name = '0', 
                        target_ref = kubernetes.client.models.v1/object_reference.v1.ObjectReference(
                            api_version = '0', 
                            field_path = '0', 
                            kind = '0', 
                            name = '0', 
                            namespace = '0', 
                            resource_version = '0', 
                            uid = '0', ), 
                        topology = {
                            'key' : '0'
                            }, )
                    ], 
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
                ports = [
                    kubernetes.client.models.v1beta1/endpoint_port.v1beta1.EndpointPort(
                        app_protocol = '0', 
                        name = '0', 
                        port = 56, 
                        protocol = '0', )
                    ]
            )
        else :
            return V1beta1EndpointSlice(
                address_type = '0',
                endpoints = [
                    kubernetes.client.models.v1beta1/endpoint.v1beta1.Endpoint(
                        addresses = [
                            '0'
                            ], 
                        conditions = kubernetes.client.models.v1beta1/endpoint_conditions.v1beta1.EndpointConditions(
                            ready = True, 
                            serving = True, 
                            terminating = True, ), 
                        hostname = '0', 
                        node_name = '0', 
                        target_ref = kubernetes.client.models.v1/object_reference.v1.ObjectReference(
                            api_version = '0', 
                            field_path = '0', 
                            kind = '0', 
                            name = '0', 
                            namespace = '0', 
                            resource_version = '0', 
                            uid = '0', ), 
                        topology = {
                            'key' : '0'
                            }, )
                    ],
        )

    def testV1beta1EndpointSlice(self):
        """Test V1beta1EndpointSlice"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
