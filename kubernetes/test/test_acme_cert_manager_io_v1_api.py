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
from kubernetes.client.api.acme_cert_manager_io_v1_api import AcmeCertManagerIoV1Api  # noqa: E501
from kubernetes.client.rest import ApiException


class TestAcmeCertManagerIoV1Api(unittest.TestCase):
    """AcmeCertManagerIoV1Api unit test stubs"""

    def setUp(self):
        self.api = kubernetes.client.api.acme_cert_manager_io_v1_api.AcmeCertManagerIoV1Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_namespaced_challenge(self):
        """Test case for create_namespaced_challenge

        """
        pass

    def test_create_namespaced_order(self):
        """Test case for create_namespaced_order

        """
        pass

    def test_delete_collection_namespaced_challenge(self):
        """Test case for delete_collection_namespaced_challenge

        """
        pass

    def test_delete_collection_namespaced_order(self):
        """Test case for delete_collection_namespaced_order

        """
        pass

    def test_delete_namespaced_challenge(self):
        """Test case for delete_namespaced_challenge

        """
        pass

    def test_delete_namespaced_order(self):
        """Test case for delete_namespaced_order

        """
        pass

    def test_list_challenge_for_all_namespaces(self):
        """Test case for list_challenge_for_all_namespaces

        """
        pass

    def test_list_namespaced_challenge(self):
        """Test case for list_namespaced_challenge

        """
        pass

    def test_list_namespaced_order(self):
        """Test case for list_namespaced_order

        """
        pass

    def test_list_order_for_all_namespaces(self):
        """Test case for list_order_for_all_namespaces

        """
        pass

    def test_patch_namespaced_challenge(self):
        """Test case for patch_namespaced_challenge

        """
        pass

    def test_patch_namespaced_challenge_status(self):
        """Test case for patch_namespaced_challenge_status

        """
        pass

    def test_patch_namespaced_order(self):
        """Test case for patch_namespaced_order

        """
        pass

    def test_patch_namespaced_order_status(self):
        """Test case for patch_namespaced_order_status

        """
        pass

    def test_read_namespaced_challenge(self):
        """Test case for read_namespaced_challenge

        """
        pass

    def test_read_namespaced_challenge_status(self):
        """Test case for read_namespaced_challenge_status

        """
        pass

    def test_read_namespaced_order(self):
        """Test case for read_namespaced_order

        """
        pass

    def test_read_namespaced_order_status(self):
        """Test case for read_namespaced_order_status

        """
        pass

    def test_replace_namespaced_challenge(self):
        """Test case for replace_namespaced_challenge

        """
        pass

    def test_replace_namespaced_challenge_status(self):
        """Test case for replace_namespaced_challenge_status

        """
        pass

    def test_replace_namespaced_order(self):
        """Test case for replace_namespaced_order

        """
        pass

    def test_replace_namespaced_order_status(self):
        """Test case for replace_namespaced_order_status

        """
        pass


if __name__ == '__main__':
    unittest.main()