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
from kubernetes.client.models.v1_preferred_scheduling_term import V1PreferredSchedulingTerm  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1PreferredSchedulingTerm(unittest.TestCase):
    """V1PreferredSchedulingTerm unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1PreferredSchedulingTerm
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1_preferred_scheduling_term.V1PreferredSchedulingTerm()  # noqa: E501
        if include_optional :
            return V1PreferredSchedulingTerm(
                preference = kubernetes.client.models.v1/node_selector_term.v1.NodeSelectorTerm(
                    match_expressions = [
                        kubernetes.client.models.v1/node_selector_requirement.v1.NodeSelectorRequirement(
                            key = '0', 
                            operator = '0', 
                            values = [
                                '0'
                                ], )
                        ], 
                    match_fields = [
                        kubernetes.client.models.v1/node_selector_requirement.v1.NodeSelectorRequirement(
                            key = '0', 
                            operator = '0', )
                        ], ), 
                weight = 56
            )
        else :
            return V1PreferredSchedulingTerm(
                preference = kubernetes.client.models.v1/node_selector_term.v1.NodeSelectorTerm(
                    match_expressions = [
                        kubernetes.client.models.v1/node_selector_requirement.v1.NodeSelectorRequirement(
                            key = '0', 
                            operator = '0', 
                            values = [
                                '0'
                                ], )
                        ], 
                    match_fields = [
                        kubernetes.client.models.v1/node_selector_requirement.v1.NodeSelectorRequirement(
                            key = '0', 
                            operator = '0', )
                        ], ),
                weight = 56,
        )

    def testV1PreferredSchedulingTerm(self):
        """Test V1PreferredSchedulingTerm"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
