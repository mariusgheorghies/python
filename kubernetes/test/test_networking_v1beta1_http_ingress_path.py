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
from kubernetes.client.models.networking_v1beta1_http_ingress_path import NetworkingV1beta1HTTPIngressPath  # noqa: E501
from kubernetes.client.rest import ApiException

class TestNetworkingV1beta1HTTPIngressPath(unittest.TestCase):
    """NetworkingV1beta1HTTPIngressPath unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test NetworkingV1beta1HTTPIngressPath
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.networking_v1beta1_http_ingress_path.NetworkingV1beta1HTTPIngressPath()  # noqa: E501
        if include_optional :
            return NetworkingV1beta1HTTPIngressPath(
                backend = kubernetes.client.models.networking/v1beta1/ingress_backend.networking.v1beta1.IngressBackend(
                    resource = kubernetes.client.models.v1/typed_local_object_reference.v1.TypedLocalObjectReference(
                        api_group = '0', 
                        kind = '0', 
                        name = '0', ), 
                    service_name = '0', 
                    service_port = kubernetes.client.models.service_port.servicePort(), ), 
                path = '0', 
                path_type = '0'
            )
        else :
            return NetworkingV1beta1HTTPIngressPath(
                backend = kubernetes.client.models.networking/v1beta1/ingress_backend.networking.v1beta1.IngressBackend(
                    resource = kubernetes.client.models.v1/typed_local_object_reference.v1.TypedLocalObjectReference(
                        api_group = '0', 
                        kind = '0', 
                        name = '0', ), 
                    service_name = '0', 
                    service_port = kubernetes.client.models.service_port.servicePort(), ),
        )

    def testNetworkingV1beta1HTTPIngressPath(self):
        """Test NetworkingV1beta1HTTPIngressPath"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
