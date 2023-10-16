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
from kubernetes.client.api.vpcresources_k8s_aws_v1beta1_api import VpcresourcesK8sAwsV1beta1Api  # noqa: E501
from kubernetes.client.rest import ApiException


class TestVpcresourcesK8sAwsV1beta1Api(unittest.TestCase):
    """VpcresourcesK8sAwsV1beta1Api unit test stubs"""

    def setUp(self):
        self.api = kubernetes.client.api.vpcresources_k8s_aws_v1beta1_api.VpcresourcesK8sAwsV1beta1Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_namespaced_security_group_policy(self):
        """Test case for create_namespaced_security_group_policy

        """
        pass

    def test_delete_collection_namespaced_security_group_policy(self):
        """Test case for delete_collection_namespaced_security_group_policy

        """
        pass

    def test_delete_namespaced_security_group_policy(self):
        """Test case for delete_namespaced_security_group_policy

        """
        pass

    def test_list_namespaced_security_group_policy(self):
        """Test case for list_namespaced_security_group_policy

        """
        pass

    def test_list_security_group_policy_for_all_namespaces(self):
        """Test case for list_security_group_policy_for_all_namespaces

        """
        pass

    def test_patch_namespaced_security_group_policy(self):
        """Test case for patch_namespaced_security_group_policy

        """
        pass

    def test_read_namespaced_security_group_policy(self):
        """Test case for read_namespaced_security_group_policy

        """
        pass

    def test_replace_namespaced_security_group_policy(self):
        """Test case for replace_namespaced_security_group_policy

        """
        pass


if __name__ == '__main__':
    unittest.main()