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
from kubernetes.client.models.io_xk8s_cluster_bootstrap_v1alpha3_eks_config_template_spec import IoXK8sClusterBootstrapV1alpha3EKSConfigTemplateSpec  # noqa: E501
from kubernetes.client.rest import ApiException

class TestIoXK8sClusterBootstrapV1alpha3EKSConfigTemplateSpec(unittest.TestCase):
    """IoXK8sClusterBootstrapV1alpha3EKSConfigTemplateSpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IoXK8sClusterBootstrapV1alpha3EKSConfigTemplateSpec
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.io_xk8s_cluster_bootstrap_v1alpha3_eks_config_template_spec.IoXK8sClusterBootstrapV1alpha3EKSConfigTemplateSpec()  # noqa: E501
        if include_optional :
            return IoXK8sClusterBootstrapV1alpha3EKSConfigTemplateSpec(
                template = kubernetes.client.models.io_x_k8s_cluster_bootstrap_v1alpha3_eks_config_template_spec_template.io_x_k8s_cluster_bootstrap_v1alpha3_EKSConfigTemplate_spec_template(
                    spec = kubernetes.client.models.io_x_k8s_cluster_bootstrap_v1alpha3_eks_config_spec.io_x_k8s_cluster_bootstrap_v1alpha3_EKSConfig_spec(
                        kubelet_extra_args = {
                            'key' : '0'
                            }, ), )
            )
        else :
            return IoXK8sClusterBootstrapV1alpha3EKSConfigTemplateSpec(
                template = kubernetes.client.models.io_x_k8s_cluster_bootstrap_v1alpha3_eks_config_template_spec_template.io_x_k8s_cluster_bootstrap_v1alpha3_EKSConfigTemplate_spec_template(
                    spec = kubernetes.client.models.io_x_k8s_cluster_bootstrap_v1alpha3_eks_config_spec.io_x_k8s_cluster_bootstrap_v1alpha3_EKSConfig_spec(
                        kubelet_extra_args = {
                            'key' : '0'
                            }, ), ),
        )

    def testIoXK8sClusterBootstrapV1alpha3EKSConfigTemplateSpec(self):
        """Test IoXK8sClusterBootstrapV1alpha3EKSConfigTemplateSpec"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
