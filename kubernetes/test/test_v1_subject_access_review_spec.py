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
from kubernetes.client.models.v1_subject_access_review_spec import V1SubjectAccessReviewSpec  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1SubjectAccessReviewSpec(unittest.TestCase):
    """V1SubjectAccessReviewSpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1SubjectAccessReviewSpec
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1_subject_access_review_spec.V1SubjectAccessReviewSpec()  # noqa: E501
        if include_optional :
            return V1SubjectAccessReviewSpec(
                extra = {
                    'key' : [
                        '0'
                        ]
                    }, 
                groups = [
                    '0'
                    ], 
                non_resource_attributes = kubernetes.client.models.v1/non_resource_attributes.v1.NonResourceAttributes(
                    path = '0', 
                    verb = '0', ), 
                resource_attributes = kubernetes.client.models.v1/resource_attributes.v1.ResourceAttributes(
                    group = '0', 
                    name = '0', 
                    namespace = '0', 
                    resource = '0', 
                    subresource = '0', 
                    verb = '0', 
                    version = '0', ), 
                uid = '0', 
                user = '0'
            )
        else :
            return V1SubjectAccessReviewSpec(
        )

    def testV1SubjectAccessReviewSpec(self):
        """Test V1SubjectAccessReviewSpec"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
