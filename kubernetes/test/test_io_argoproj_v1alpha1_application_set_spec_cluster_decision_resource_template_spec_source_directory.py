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
from kubernetes.client.models.io_argoproj_v1alpha1_application_set_spec_cluster_decision_resource_template_spec_source_directory import IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSourceDirectory  # noqa: E501
from kubernetes.client.rest import ApiException

class TestIoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSourceDirectory(unittest.TestCase):
    """IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSourceDirectory unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSourceDirectory
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.io_argoproj_v1alpha1_application_set_spec_cluster_decision_resource_template_spec_source_directory.IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSourceDirectory()  # noqa: E501
        if include_optional :
            return IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSourceDirectory(
                exclude = '0', 
                include = '0', 
                jsonnet = kubernetes.client.models.io_argoproj_v1alpha1_application_set_spec_cluster_decision_resource_template_spec_source_directory_jsonnet.io_argoproj_v1alpha1_ApplicationSet_spec_clusterDecisionResource_template_spec_source_directory_jsonnet(
                    ext_vars = [
                        kubernetes.client.models.io_argoproj_v1alpha1_application_set_spec_cluster_decision_resource_template_spec_source_directory_jsonnet_ext_vars.io_argoproj_v1alpha1_ApplicationSet_spec_clusterDecisionResource_template_spec_source_directory_jsonnet_extVars(
                            code = True, 
                            name = '0', 
                            value = '0', )
                        ], 
                    libs = [
                        '0'
                        ], 
                    tlas = [
                        kubernetes.client.models.io_argoproj_v1alpha1_application_set_spec_cluster_decision_resource_template_spec_source_directory_jsonnet_ext_vars.io_argoproj_v1alpha1_ApplicationSet_spec_clusterDecisionResource_template_spec_source_directory_jsonnet_extVars(
                            code = True, 
                            name = '0', 
                            value = '0', )
                        ], ), 
                recurse = True
            )
        else :
            return IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSourceDirectory(
        )

    def testIoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSourceDirectory(self):
        """Test IoArgoprojV1alpha1ApplicationSetSpecClusterDecisionResourceTemplateSpecSourceDirectory"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
