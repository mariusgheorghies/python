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
from kubernetes.client.models.v1beta1_subject_rules_review_status import V1beta1SubjectRulesReviewStatus  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1beta1SubjectRulesReviewStatus(unittest.TestCase):
    """V1beta1SubjectRulesReviewStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1beta1SubjectRulesReviewStatus
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1beta1_subject_rules_review_status.V1beta1SubjectRulesReviewStatus()  # noqa: E501
        if include_optional :
            return V1beta1SubjectRulesReviewStatus(
                evaluation_error = '0', 
                incomplete = True, 
                non_resource_rules = [
                    kubernetes.client.models.v1beta1/non_resource_rule.v1beta1.NonResourceRule(
                        non_resource_ur_ls = [
                            '0'
                            ], 
                        verbs = [
                            '0'
                            ], )
                    ], 
                resource_rules = [
                    kubernetes.client.models.v1beta1/resource_rule.v1beta1.ResourceRule(
                        api_groups = [
                            '0'
                            ], 
                        resource_names = [
                            '0'
                            ], 
                        resources = [
                            '0'
                            ], 
                        verbs = [
                            '0'
                            ], )
                    ]
            )
        else :
            return V1beta1SubjectRulesReviewStatus(
                incomplete = True,
                non_resource_rules = [
                    kubernetes.client.models.v1beta1/non_resource_rule.v1beta1.NonResourceRule(
                        non_resource_ur_ls = [
                            '0'
                            ], 
                        verbs = [
                            '0'
                            ], )
                    ],
                resource_rules = [
                    kubernetes.client.models.v1beta1/resource_rule.v1beta1.ResourceRule(
                        api_groups = [
                            '0'
                            ], 
                        resource_names = [
                            '0'
                            ], 
                        resources = [
                            '0'
                            ], 
                        verbs = [
                            '0'
                            ], )
                    ],
        )

    def testV1beta1SubjectRulesReviewStatus(self):
        """Test V1beta1SubjectRulesReviewStatus"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
