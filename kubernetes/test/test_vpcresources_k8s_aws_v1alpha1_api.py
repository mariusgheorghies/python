# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.25.12
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import kubernetes.client
from kubernetes.client.api.vpcresources_k8s_aws_v1alpha1_api import VpcresourcesK8sAwsV1alpha1Api  # noqa: E501
from kubernetes.client.rest import ApiException


class TestVpcresourcesK8sAwsV1alpha1Api(unittest.TestCase):
    """VpcresourcesK8sAwsV1alpha1Api unit test stubs"""

    def setUp(self):
        self.api = kubernetes.client.api.vpcresources_k8s_aws_v1alpha1_api.VpcresourcesK8sAwsV1alpha1Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_cni_node(self):
        """Test case for create_cni_node

        """
        pass

    def test_delete_cni_node(self):
        """Test case for delete_cni_node

        """
        pass

    def test_delete_collection_cni_node(self):
        """Test case for delete_collection_cni_node

        """
        pass

    def test_list_cni_node(self):
        """Test case for list_cni_node

        """
        pass

    def test_patch_cni_node(self):
        """Test case for patch_cni_node

        """
        pass

    def test_read_cni_node(self):
        """Test case for read_cni_node

        """
        pass

    def test_replace_cni_node(self):
        """Test case for replace_cni_node

        """
        pass


if __name__ == '__main__':
    unittest.main()
