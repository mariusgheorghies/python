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
from kubernetes.client.models.v1_custom_resource_conversion import V1CustomResourceConversion  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1CustomResourceConversion(unittest.TestCase):
    """V1CustomResourceConversion unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1CustomResourceConversion
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1_custom_resource_conversion.V1CustomResourceConversion()  # noqa: E501
        if include_optional :
            return V1CustomResourceConversion(
                strategy = '0', 
                webhook = kubernetes.client.models.v1/webhook_conversion.v1.WebhookConversion(
                    kubernetes.client_config = kubernetes.client.models.apiextensions/v1/webhook_client_config.apiextensions.v1.WebhookClientConfig(
                        ca_bundle = 'YQ==', 
                        service = kubernetes.client.models.apiextensions/v1/service_reference.apiextensions.v1.ServiceReference(
                            name = '0', 
                            namespace = '0', 
                            path = '0', 
                            port = 56, ), 
                        url = '0', ), 
                    conversion_review_versions = [
                        '0'
                        ], )
            )
        else :
            return V1CustomResourceConversion(
                strategy = '0',
        )

    def testV1CustomResourceConversion(self):
        """Test V1CustomResourceConversion"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
