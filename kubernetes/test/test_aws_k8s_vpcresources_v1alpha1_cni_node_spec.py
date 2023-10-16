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
from kubernetes.client.models.aws_k8s_vpcresources_v1alpha1_cni_node_spec import AwsK8sVpcresourcesV1alpha1CNINodeSpec  # noqa: E501
from kubernetes.client.rest import ApiException

class TestAwsK8sVpcresourcesV1alpha1CNINodeSpec(unittest.TestCase):
    """AwsK8sVpcresourcesV1alpha1CNINodeSpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AwsK8sVpcresourcesV1alpha1CNINodeSpec
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.aws_k8s_vpcresources_v1alpha1_cni_node_spec.AwsK8sVpcresourcesV1alpha1CNINodeSpec()  # noqa: E501
        if include_optional :
            return AwsK8sVpcresourcesV1alpha1CNINodeSpec(
                features = [
                    kubernetes.client.models.aws_k8s_vpcresources_v1alpha1_cni_node_spec_features.aws_k8s_vpcresources_v1alpha1_CNINode_spec_features(
                        name = '0', 
                        value = '0', )
                    ]
            )
        else :
            return AwsK8sVpcresourcesV1alpha1CNINodeSpec(
        )

    def testAwsK8sVpcresourcesV1alpha1CNINodeSpec(self):
        """Test AwsK8sVpcresourcesV1alpha1CNINodeSpec"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()