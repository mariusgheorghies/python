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
from kubernetes.client.api.crd_k8s_amazonaws_com_v1alpha1_api import CrdK8sAmazonawsComV1alpha1Api  # noqa: E501
from kubernetes.client.rest import ApiException


class TestCrdK8sAmazonawsComV1alpha1Api(unittest.TestCase):
    """CrdK8sAmazonawsComV1alpha1Api unit test stubs"""

    def setUp(self):
        self.api = kubernetes.client.api.crd_k8s_amazonaws_com_v1alpha1_api.CrdK8sAmazonawsComV1alpha1Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_eni_config(self):
        """Test case for create_eni_config

        """
        pass

    def test_delete_collection_eni_config(self):
        """Test case for delete_collection_eni_config

        """
        pass

    def test_delete_eni_config(self):
        """Test case for delete_eni_config

        """
        pass

    def test_list_eni_config(self):
        """Test case for list_eni_config

        """
        pass

    def test_patch_eni_config(self):
        """Test case for patch_eni_config

        """
        pass

    def test_read_eni_config(self):
        """Test case for read_eni_config

        """
        pass

    def test_replace_eni_config(self):
        """Test case for replace_eni_config

        """
        pass


if __name__ == '__main__':
    unittest.main()