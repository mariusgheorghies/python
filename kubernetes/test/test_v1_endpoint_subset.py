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
from kubernetes.client.models.v1_endpoint_subset import V1EndpointSubset  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1EndpointSubset(unittest.TestCase):
    """V1EndpointSubset unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1EndpointSubset
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1_endpoint_subset.V1EndpointSubset()  # noqa: E501
        if include_optional :
            return V1EndpointSubset(
                addresses = [
                    kubernetes.client.models.v1/endpoint_address.v1.EndpointAddress(
                        hostname = '0', 
                        ip = '0', 
                        node_name = '0', 
                        target_ref = kubernetes.client.models.v1/object_reference.v1.ObjectReference(
                            api_version = '0', 
                            field_path = '0', 
                            kind = '0', 
                            name = '0', 
                            namespace = '0', 
                            resource_version = '0', 
                            uid = '0', ), )
                    ], 
                not_ready_addresses = [
                    kubernetes.client.models.v1/endpoint_address.v1.EndpointAddress(
                        hostname = '0', 
                        ip = '0', 
                        node_name = '0', 
                        target_ref = kubernetes.client.models.v1/object_reference.v1.ObjectReference(
                            api_version = '0', 
                            field_path = '0', 
                            kind = '0', 
                            name = '0', 
                            namespace = '0', 
                            resource_version = '0', 
                            uid = '0', ), )
                    ], 
                ports = [
                    kubernetes.client.models.v1/endpoint_port.v1.EndpointPort(
                        app_protocol = '0', 
                        name = '0', 
                        port = 56, 
                        protocol = '0', )
                    ]
            )
        else :
            return V1EndpointSubset(
        )

    def testV1EndpointSubset(self):
        """Test V1EndpointSubset"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
