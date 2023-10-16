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
from kubernetes.client.models.io_argoproj_v1alpha1_application_set_spec_cluster_decision_resource_template_spec_ignore_differences import IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecIgnoreDifferences  # noqa: E501
from kubernetes.client.rest import ApiException

class TestIoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecIgnoreDifferences(unittest.TestCase):
    """IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecIgnoreDifferences unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecIgnoreDifferences
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.io_argoproj_v1alpha1_application_set_spec_cluster_decision_resource_template_spec_ignore_differences.IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecIgnoreDifferences()  # noqa: E501
        if include_optional :
            return IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecIgnoreDifferences(
                group = '0', 
                jq_path_expressions = [
                    '0'
                    ], 
                json_pointers = [
                    '0'
                    ], 
                kind = '0', 
                managed_fields_managers = [
                    '0'
                    ], 
                name = '0', 
                namespace = '0'
            )
        else :
            return IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecIgnoreDifferences(
                kind = '0',
        )

    def testIoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecIgnoreDifferences(self):
        """Test IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecIgnoreDifferences"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()