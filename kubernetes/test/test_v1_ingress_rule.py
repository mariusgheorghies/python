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
from kubernetes.client.models.v1_ingress_rule import V1IngressRule  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1IngressRule(unittest.TestCase):
    """V1IngressRule unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1IngressRule
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1_ingress_rule.V1IngressRule()  # noqa: E501
        if include_optional :
            return V1IngressRule(
                host = '0', 
                http = kubernetes.client.models.v1/http_ingress_rule_value.v1.HTTPIngressRuleValue(
                    paths = [
                        kubernetes.client.models.v1/http_ingress_path.v1.HTTPIngressPath(
                            backend = kubernetes.client.models.v1/ingress_backend.v1.IngressBackend(
                                resource = kubernetes.client.models.v1/typed_local_object_reference.v1.TypedLocalObjectReference(
                                    api_group = '0', 
                                    kind = '0', 
                                    name = '0', ), 
                                service = kubernetes.client.models.v1/ingress_service_backend.v1.IngressServiceBackend(
                                    name = '0', 
                                    port = kubernetes.client.models.v1/service_backend_port.v1.ServiceBackendPort(
                                        name = '0', 
                                        number = 56, ), ), ), 
                            path = '0', 
                            path_type = '0', )
                        ], )
            )
        else :
            return V1IngressRule(
        )

    def testV1IngressRule(self):
        """Test V1IngressRule"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
