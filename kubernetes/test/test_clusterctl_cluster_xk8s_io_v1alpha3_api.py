# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.20.7
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import kubernetes.client
from kubernetes.client.api.clusterctl_cluster_xk8s_io_v1alpha3_api import ClusterctlClusterXK8sIoV1alpha3Api  # noqa: E501
from kubernetes.client.rest import ApiException


class TestClusterctlClusterXK8sIoV1alpha3Api(unittest.TestCase):
    """ClusterctlClusterXK8sIoV1alpha3Api unit test stubs"""

    def setUp(self):
        self.api = kubernetes.client.api.clusterctl_cluster_xk8s_io_v1alpha3_api.ClusterctlClusterXK8sIoV1alpha3Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_namespaced_provider(self):
        """Test case for create_namespaced_provider

        """
        pass

    def test_delete_collection_namespaced_provider(self):
        """Test case for delete_collection_namespaced_provider

        """
        pass

    def test_delete_namespaced_provider(self):
        """Test case for delete_namespaced_provider

        """
        pass

    def test_list_namespaced_provider(self):
        """Test case for list_namespaced_provider

        """
        pass

    def test_list_provider_for_all_namespaces(self):
        """Test case for list_provider_for_all_namespaces

        """
        pass

    def test_patch_namespaced_provider(self):
        """Test case for patch_namespaced_provider

        """
        pass

    def test_read_namespaced_provider(self):
        """Test case for read_namespaced_provider

        """
        pass

    def test_replace_namespaced_provider(self):
        """Test case for replace_namespaced_provider

        """
        pass


if __name__ == '__main__':
    unittest.main()
